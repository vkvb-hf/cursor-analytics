#!/usr/bin/env python3
"""
Verify if identifiers from CSV match those in payments_hf.customer_identifiers table.
This helps verify that CSV data format is correct and normalization will work.
"""

import sys
import os
from datetime import datetime

# Add cursor_databricks directory to path
script_dir = os.path.dirname(os.path.abspath(__file__))
cursor_databricks_dir = os.path.dirname(os.path.dirname(script_dir))
sys.path.insert(0, cursor_databricks_dir)

from databricks_api import DatabricksAPI

def verify_csv_identifiers_match():
    """Verify CSV identifiers match customer_identifiers table."""
    
    db = DatabricksAPI()
    
    print("=" * 100)
    print("VERIFYING CSV IDENTIFIERS MATCH customer_identifiers TABLE")
    print("=" * 100)
    
    verification_notebook = """# Databricks notebook source
# MAGIC %md
# MAGIC # CSV Identifiers Match Verification
# MAGIC 
# MAGIC This notebook checks if identifiers from CSV match those in payments_hf.customer_identifiers table.

# COMMAND ----------

from pyspark.sql import functions as F
from datetime import datetime

save_path = "s3://hf-payments-data-lake-live-main/voucher_abuse/neptune_backfill/20250305"

print("=" * 100)
print("CSV IDENTIFIERS MATCH VERIFICATION")
print("=" * 100)

# Read CSV edges
print("\\n📥 Reading CSV edges...")
csv_edges_df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "false")
    .csv(f"{save_path}/edges")
)

csv_count = csv_edges_df.count()
print(f"✅ Read {csv_count:,} edges from CSV")

# Get sample of CSV identifiers
print("\\n📊 Sample CSV edges (first 10):")
csv_edges_df.select("~from", "~to", "~label").show(10, truncate=False)

# Extract unique identifiers from CSV
csv_identifiers = csv_edges_df.select(
    F.col("~from").alias("csv_src"),
    F.col("~to").alias("csv_dst"),
    F.col("~label").alias("csv_identifier_source")
).distinct()

print(f"\\n📊 Unique CSV identifiers: {csv_identifiers.count():,}")

# Read customer_identifiers table
print("\\n📥 Reading payments_hf.customer_identifiers table...")
spark.sql("REFRESH TABLE payments_hf.customer_identifiers")
customer_identifiers_df = spark.table("payments_hf.customer_identifiers")

table_count = customer_identifiers_df.count()
print(f"✅ Read {table_count:,} records from customer_identifiers table")

# Show sample from table
print("\\n📊 Sample from customer_identifiers table (first 10):")
customer_identifiers_df.select("src", "dst", "identifier_source").show(10, truncate=False)

# Check 1: Direct match on dst (identifier) and identifier_source
print("\\n" + "=" * 100)
print("CHECK 1: Direct Match on dst and identifier_source")
print("=" * 100)

csv_for_match = csv_identifiers.select(
    F.col("csv_dst").alias("dst"),
    F.col("csv_identifier_source").alias("identifier_source")
).distinct()

table_for_match = customer_identifiers_df.select(
    "dst",
    "identifier_source"
).distinct()

# Join to find matches
match_on_identifier = csv_for_match.join(
    table_for_match,
    on=["dst", "identifier_source"],
    how="inner"
)

csv_unique_identifiers = csv_for_match.count()
table_unique_identifiers = table_for_match.count()
matched_identifiers = match_on_identifier.count()

print(f"\\n📊 Unique identifier combinations:")
print(f"   CSV: {csv_unique_identifiers:,}")
print(f"   Table: {table_unique_identifiers:,}")
print(f"   Matched: {matched_identifiers:,} ({matched_identifiers/csv_unique_identifiers*100:.1f}%)")

if matched_identifiers > 0:
    print("\\n✅ Sample matched identifiers:")
    match_on_identifier.limit(10).show(truncate=False)
else:
    print("\\n⚠️  No matches found on dst + identifier_source")

# Check 2: Match on src format
print("\\n" + "=" * 100)
print("CHECK 2: Match on src format")
print("=" * 100)

# Extract business_unit and customer_id from CSV src
csv_src_parsed = csv_identifiers.withColumn(
    "src_parts",
    F.split(F.col("csv_src"), "_", 2)
).withColumn(
    "csv_business_unit",
    F.col("src_parts")[0]
).withColumn(
    "csv_customer_id",
    F.when(F.size(F.col("src_parts")) > 1, F.col("src_parts")[1]).otherwise(F.lit(None))
).drop("src_parts")

# Parse table src (could be customer:business_unit_customer_uuid or business_unit_customer_id)
table_src_parsed = customer_identifiers_df.select(
    "src",
    "business_unit",
    "customer_id",
    "dst",
    "identifier_source"
).withColumn(
    "src_has_customer_prefix",
    F.col("src").rlike("^customer:")
).withColumn(
    "src_without_prefix",
    F.when(
        F.col("src").rlike("^customer:"),
        F.regexp_replace(F.col("src"), "^customer:", "")
    ).otherwise(F.col("src"))
)

print("\\n📊 Table src format analysis:")
table_src_formats = table_src_parsed.agg(
    F.sum(F.when(F.col("src_has_customer_prefix"), 1).otherwise(0)).alias("with_customer_prefix"),
    F.sum(F.when(~F.col("src_has_customer_prefix"), 1).otherwise(0)).alias("without_customer_prefix")
).collect()[0]

total_table = customer_identifiers_df.count()
with_prefix = table_src_formats["with_customer_prefix"]
without_prefix = table_src_formats["without_customer_prefix"]

print(f"   Total records: {total_table:,}")
print(f"   With 'customer:' prefix: {with_prefix:,} ({with_prefix/total_table*100:.1f}%)")
print(f"   Without 'customer:' prefix: {without_prefix:,} ({without_prefix/total_table*100:.1f}%)")

# Try matching on business_unit + customer_id + dst + identifier_source
print("\\n📊 Matching on business_unit + customer_id + dst + identifier_source...")

csv_for_join = csv_src_parsed.select(
    F.col("csv_business_unit").alias("business_unit"),
    F.col("csv_customer_id").cast("bigint").alias("customer_id"),
    F.col("csv_dst").alias("dst"),
    F.col("csv_identifier_source").alias("identifier_source")
).distinct()

# Filter table to records without customer: prefix (original format)
table_for_join = table_src_parsed.filter(
    ~F.col("src_has_customer_prefix")
).select(
    "business_unit",
    F.col("customer_id").cast("bigint").alias("customer_id"),
    "dst",
    "identifier_source"
).distinct()

# Join
match_on_all = csv_for_join.join(
    table_for_join,
    on=["business_unit", "customer_id", "dst", "identifier_source"],
    how="inner"
)

csv_unique_combos = csv_for_join.count()
table_unique_combos = table_for_join.count()
matched_combos = match_on_all.count()

print(f"\\n📊 Unique combinations:")
print(f"   CSV: {csv_unique_combos:,}")
print(f"   Table (without customer: prefix): {table_unique_combos:,}")
print(f"   Matched: {matched_combos:,} ({matched_combos/csv_unique_combos*100:.1f}%)")

if matched_combos > 0:
    print("\\n✅ Sample matched combinations:")
    match_on_all.limit(10).show(truncate=False)
    
    # Show sample of matched records with full details
    print("\\n📊 Sample matched records with full details:")
    matched_full = csv_src_parsed.join(
        match_on_all,
        on=["business_unit", "customer_id", "dst", "identifier_source"],
        how="inner"
    ).select(
        "csv_src",
        "business_unit",
        "customer_id",
        "dst",
        "identifier_source"
    ).limit(10)
    matched_full.show(truncate=False)
else:
    print("\\n⚠️  No matches found on business_unit + customer_id + dst + identifier_source")
    
    # Debug: Show sample from each side
    print("\\n📊 Sample CSV combinations:")
    csv_for_join.limit(10).show(truncate=False)
    
    print("\\n📊 Sample Table combinations:")
    table_for_join.limit(10).show(truncate=False)

# Check 3: Compare src formats
print("\\n" + "=" * 100)
print("CHECK 3: src Format Comparison")
print("=" * 100)

print("\\n📊 CSV src format samples:")
csv_src_samples = csv_identifiers.select("csv_src").distinct().limit(10).collect()
for i, row in enumerate(csv_src_samples, 1):
    print(f"   {i}. {row['csv_src']}")

print("\\n📊 Table src format samples (without customer: prefix):")
table_src_samples = table_src_parsed.filter(
    ~F.col("src_has_customer_prefix")
).select("src").distinct().limit(10).collect()
for i, row in enumerate(table_src_samples, 1):
    print(f"   {i}. {row['src']}")

# Summary
print("\\n" + "=" * 100)
print("SUMMARY")
print("=" * 100)

output_lines = []
output_lines.append("=" * 100)
output_lines.append("CSV IDENTIFIERS MATCH VERIFICATION RESULTS")
output_lines.append("=" * 100)
output_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
output_lines.append("")
output_lines.append(f"CSV edges: {csv_count:,}")
output_lines.append(f"Table records: {table_count:,}")
output_lines.append("")
output_lines.append("Identifier Match (dst + identifier_source):")
output_lines.append(f"  CSV unique: {csv_unique_identifiers:,}")
output_lines.append(f"  Table unique: {table_unique_identifiers:,}")
output_lines.append(f"  Matched: {matched_identifiers:,} ({matched_identifiers/csv_unique_identifiers*100:.1f}%)")
output_lines.append("")
output_lines.append("Full Match (business_unit + customer_id + dst + identifier_source):")
output_lines.append(f"  CSV unique: {csv_unique_combos:,}")
output_lines.append(f"  Table unique (without customer: prefix): {table_unique_combos:,}")
output_lines.append(f"  Matched: {matched_combos:,} ({matched_combos/csv_unique_combos*100:.1f}%)")
output_lines.append("")
output_lines.append("Table src format:")
output_lines.append(f"  With 'customer:' prefix: {with_prefix:,} ({with_prefix/total_table*100:.1f}%)")
output_lines.append(f"  Without 'customer:' prefix: {without_prefix:,} ({without_prefix/total_table*100:.1f}%)")
output_lines.append("")
output_lines.append("=" * 100)

output_path = f"/tmp/notebook_outputs/verify_identifiers_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
dbutils.fs.mkdirs("/tmp/notebook_outputs")
dbutils.fs.put(output_path, "\\n".join(output_lines), overwrite=True)
print(f"\\n✅ Output written to: {output_path}")
"""
    
    try:
        notebook_path = "/Workspace/Users/visal.kumar@hellofresh.com/_temp_verify_identifiers_match"
        job_name = f"verify_identifiers_match_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
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
    verify_csv_identifiers_match()






