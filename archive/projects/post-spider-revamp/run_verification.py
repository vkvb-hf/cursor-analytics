#!/usr/bin/env python3
"""
Run verification to check CSV normalization and compare with Spider output.
This script creates and runs a verification notebook in Databricks.
"""

import sys
import os
from datetime import datetime

# Add cursor_databricks directory to path
script_dir = os.path.dirname(os.path.abspath(__file__))
cursor_databricks_dir = os.path.dirname(os.path.dirname(script_dir))
sys.path.insert(0, cursor_databricks_dir)

from databricks_api import DatabricksAPI

def run_verification():
    """Run verification in Databricks to check normalization."""
    
    db = DatabricksAPI()
    
    print("=" * 100)
    print("RUNNING NORMALIZATION VERIFICATION IN DATABRICKS")
    print("=" * 100)
    
    # Verification notebook content
    verification_notebook = """# Databricks notebook source
# MAGIC %md
# MAGIC # CSV Normalization Verification
# MAGIC 
# MAGIC This notebook verifies that CSV normalization produces the same structure as Spider processing.

# COMMAND ----------

from pyspark.sql import functions as F
from pyspark.sql.window import Window
from datetime import datetime

save_path = "s3://hf-payments-data-lake-live-main/voucher_abuse/neptune_backfill/20250305"

print("=" * 100)
print("CSV NORMALIZATION VERIFICATION")
print("=" * 100)

# Read CSV files
print("\\n📥 Reading CSV files...")
vertices_df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "false")
    .csv(f"{save_path}/vertices")
)

csv_edges_df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "false")
    .csv(f"{save_path}/edges")
)

print(f"✅ Read {vertices_df.count():,} vertices and {csv_edges_df.count():,} edges")

# Sample edges for testing
print("\\n📊 Testing normalization on sample of 100 edges...")
csv_test = csv_edges_df.limit(100).select(
    F.col("~from").alias("src"),
    F.col("~to").alias("dst"),
    F.col("~label").alias("identifier_source")
)

# Extract business_unit and customer_id
csv_test = csv_test.withColumn(
    "src_parts",
    F.split(F.col("src"), "_", 2)
).withColumn(
    "business_unit",
    F.col("src_parts")[0]
).withColumn(
    "customer_id",
    F.when(F.size(F.col("src_parts")) > 1, F.col("src_parts")[1]).otherwise(F.lit(None))
).drop("src_parts")

csv_test = csv_test.withColumn("customer_id", F.col("customer_id").cast("string"))

print("\\n📊 Sample after extraction:")
csv_test.select("src", "business_unit", "customer_id", "dst").show(10, truncate=False)

# Join with customer table
print("\\n🔗 Joining with public_edw_base_grain_live.customer...")
spark.sql("REFRESH TABLE public_edw_base_grain_live.customer")
customer_lookup = (
    spark.table("public_edw_base_grain_live.customer")
    .select(
        F.col("bob_entity_code").alias("business_unit"),
        F.col("customer_id").cast("string").alias("customer_id"),
        F.col("customer_uuid")
    )
    .distinct()
)

csv_test = csv_test.join(customer_lookup, on=["business_unit", "customer_id"], how="left")

matched = csv_test.filter(F.col("customer_uuid").isNotNull()).count()
total = csv_test.count()
print(f"✅ Matched {matched}/{total} records with customer_uuid ({matched/total*100:.1f}%)")

# Debug: Show sample of unmatched records
if matched < total:
    print("\\n⚠️  Sample unmatched records (customer_uuid is NULL):")
    unmatched_sample = csv_test.filter(F.col("customer_uuid").isNull()).select(
        "src", "business_unit", "customer_id"
    ).limit(5)
    unmatched_sample.show(truncate=False)
    
    # Check if customer table has data
    customer_count = customer_lookup.count()
    print(f"\\n📊 Customer lookup table has {customer_count:,} records")
    
    # Show sample from customer table
    print("\\n📊 Sample from customer lookup table:")
    customer_lookup.limit(5).show(truncate=False)

# Join with vertices
print("\\n🔗 Joining with vertices for created_at...")
customer_vertices = vertices_df.filter(
    (F.col("~label") == "customer") & F.col("created_at").isNotNull()
).select(
    F.col("~id").alias("src_original"),
    F.col("created_at")
)

csv_test = csv_test.withColumn(
    "src_original",
    F.concat(F.col("business_unit"), F.lit("_"), F.col("customer_id"))
).join(customer_vertices, on="src_original", how="left").drop("src_original")

has_created_at = csv_test.filter(F.col("created_at").isNotNull()).count()
print(f"✅ {has_created_at}/{total} records have created_at ({has_created_at/total*100:.1f}%)")

# Normalize src
print("\\n🔄 Normalizing src to Spider format...")
csv_test = csv_test.withColumn(
    "src",
    F.when(
        F.col("customer_uuid").isNotNull(),
        F.concat(F.lit("customer:"), F.col("business_unit"), F.lit("_"), F.col("customer_uuid"))
    ).otherwise(F.col("src"))
)

csv_test = csv_test.withColumn("subscribed_at_local", F.to_timestamp(F.col("created_at")))

# Calculate relationships
print("\\n📊 Calculating relationships...")
window_spec_identifier = Window.partitionBy("dst")
csv_test = csv_test.withColumn("count_connections", F.count("*").over(window_spec_identifier))

identifier_key_array = ["dst"]
csv_test = csv_test.withColumn("created_at_ts", F.to_timestamp(F.col("created_at")))

window_spec = Window.partitionBy(*identifier_key_array).orderBy("created_at_ts").rowsBetween(Window.unboundedPreceding, -1)
window_spec_bu = Window.partitionBy(*(["business_unit"] + identifier_key_array)).orderBy("created_at_ts").rowsBetween(Window.unboundedPreceding, -1)

self_id_col = F.concat(F.col("business_unit"), F.lit("_"), F.col("customer_id"))

csv_test = csv_test.withColumn(
    "has_direct_parent_in_business_unit",
    F.first(F.lit(True)).over(window_spec_bu).isNotNull(),
).withColumn(
    "direct_parent_in_business_unit",
    F.first(F.concat(F.col("business_unit"), F.lit("_"), F.col("customer_id"))).over(window_spec_bu),
).withColumn(
    "has_direct_parent", 
    F.first(F.lit(True)).over(window_spec).isNotNull()
).withColumn(
    "direct_parent",
    F.first(F.concat(F.col("business_unit"), F.lit("_"), F.col("customer_id"))).over(window_spec),
).drop("created_at_ts")

csv_test = csv_test.withColumn(
    "direct_parent_in_business_unit",
    F.when(self_id_col == F.col("direct_parent_in_business_unit"), F.lit(None)).otherwise(F.col("direct_parent_in_business_unit"))
).withColumn(
    "direct_parent",
    F.when(self_id_col == F.col("direct_parent"), F.lit(None)).otherwise(F.col("direct_parent"))
)

# Final output
csv_final = csv_test.select(
    "business_unit", "customer_id", "customer_uuid", "created_at", "subscribed_at_local",
    "src", "dst", "identifier_source",
    "has_direct_parent_in_business_unit", "direct_parent_in_business_unit",
    "has_direct_parent", "direct_parent", "count_connections"
)

print("\\n" + "=" * 100)
print("FINAL CSV OUTPUT")
print("=" * 100)
print("\\nSchema:")
csv_final.printSchema()

print("\\nSample data (first 10):")
csv_final.show(10, truncate=False)

# Statistics
print("\\n" + "=" * 100)
print("STATISTICS")
print("=" * 100)
total_final = csv_final.count()
normalized = csv_final.filter(F.col("customer_uuid").isNotNull()).count()
src_formatted = csv_final.filter(F.col("src").rlike("^customer:")).count()
has_created_at_final = csv_final.filter(F.col("created_at").isNotNull()).count()
has_parent_bu = csv_final.filter(F.col("direct_parent_in_business_unit").isNotNull()).count()
has_parent = csv_final.filter(F.col("direct_parent").isNotNull()).count()

print(f"\\nTotal records: {total_final}")
print(f"With customer_uuid: {normalized} ({normalized/total_final*100:.1f}%)")
print(f"With 'customer:' prefix in src: {src_formatted} ({src_formatted/total_final*100:.1f}%)")
print(f"With created_at: {has_created_at_final} ({has_created_at_final/total_final*100:.1f}%)")
print(f"With direct_parent_in_business_unit: {has_parent_bu} ({has_parent_bu/total_final*100:.1f}%)")
print(f"With direct_parent: {has_parent} ({has_parent/total_final*100:.1f}%)")

# Write output to DBFS
output_lines = []
output_lines.append("=" * 100)
output_lines.append("CSV NORMALIZATION VERIFICATION RESULTS")
output_lines.append("=" * 100)
output_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
output_lines.append("")
output_lines.append(f"Total records tested: {total_final}")
output_lines.append(f"Successfully normalized: {normalized} ({normalized/total_final*100:.1f}%)")
output_lines.append(f"With 'customer:' prefix: {src_formatted} ({src_formatted/total_final*100:.1f}%)")
output_lines.append(f"With created_at: {has_created_at_final} ({has_created_at_final/total_final*100:.1f}%)")
output_lines.append("")
output_lines.append("=" * 100)

output_path = f"/tmp/notebook_outputs/verification_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
dbutils.fs.mkdirs("/tmp/notebook_outputs")
dbutils.fs.put(output_path, "\\n".join(output_lines), overwrite=True)
print(f"\\n✅ Output written to: {output_path}")
"""
    
    try:
        notebook_path = "/Workspace/Users/visal.kumar@hellofresh.com/_temp_verification_normalization"
        job_name = f"verification_normalization_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        print(f"\n📝 Creating verification notebook: {notebook_path}")
        print(f"🚀 Running as job: {job_name}")
        
        result = db.run_notebook_job(
            notebook_path=notebook_path,
            notebook_content=verification_notebook,
            job_name=job_name,
            auto_inject_output=True,
            auto_read_output=True
        )
        
        if result and result.get('success'):
            print("\n✅ Verification completed successfully!")
            if result.get('output'):
                print("\n" + "=" * 100)
                print("VERIFICATION RESULTS:")
                print("=" * 100)
                print(result['output'])
        else:
            print("\n⚠️  Verification completed with warnings")
            if result:
                print(f"Status: {result.get('status', 'unknown')}")
                
    except Exception as e:
        print(f"\n❌ Error running verification: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run_verification()
