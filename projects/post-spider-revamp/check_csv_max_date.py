#!/usr/bin/env python3
"""
Check max created_at date in CSV files from S3
"""

import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from databricks_api import DatabricksAPI

def check_max_date():
    """Check max created_at date in CSV files."""
    
    save_path = "s3://hf-payments-data-lake-live-main/voucher_abuse/neptune_backfill/20250305"
    
    print("=" * 80)
    print("Check Max Created Date in CSV Files")
    print("=" * 80)
    print(f"\n📁 S3 Path: {save_path}")
    
    # Create notebook to check max date
    notebook_content = f"""# Databricks notebook source
# MAGIC %md
# MAGIC # Check Max Created Date in CSV Files

# COMMAND ----------

from pyspark.sql import functions as F

save_path = "{save_path}"

# COMMAND ----------

# MAGIC %md
# MAGIC ## Read Vertices CSV

# COMMAND ----------

vertices_df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "false")
    .csv(f"{{save_path}}/vertices")
)

print(f"Total vertices: {{vertices_df.count():,}}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Check Max Created Date

# COMMAND ----------

# Filter for customer vertices (they have created_at)
customer_vertices = vertices_df.filter(
    F.col("~label") == "customer"
).filter(
    F.col("created_at").isNotNull()
)

print(f"Customer vertices with created_at: {{customer_vertices.count():,}}")

# COMMAND ----------

# Get max created_at
max_date_result = customer_vertices.agg(
    F.max("created_at").alias("max_created_at"),
    F.min("created_at").alias("min_created_at"),
    F.count("*").alias("total_customers")
).collect()[0]

print("\\n" + "=" * 80)
print("📊 Date Statistics:")
print("=" * 80)
print(f"Max created_at: {{max_date_result['max_created_at']}}")
print(f"Min created_at: {{max_date_result['min_created_at']}}")
print(f"Total customers: {{max_date_result['total_customers']:,}}")
print("=" * 80)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Sample Dates

# COMMAND ----------

print("\\n📅 Sample created_at dates (sorted):")
customer_vertices.select("created_at").distinct().orderBy(F.col("created_at").desc()).show(20, truncate=False)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Date Distribution

# COMMAND ----------

print("\\n📊 Date distribution (by date):")
customer_vertices.withColumn(
    "date_only",
    F.to_date(F.col("created_at"))
).groupBy("date_only").agg(
    F.count("*").alias("count")
).orderBy("date_only").show(100, truncate=False)
"""
    
    db = DatabricksAPI()
    
    print("\n📤 Creating temporary notebook to check max date...")
    
    result = db.run_notebook_job(
        notebook_path="/Workspace/Users/visal.kumar@hellofresh.com/temp_check_csv_max_date",
        notebook_content=notebook_content,
        job_name="Check CSV Max Date",
        auto_inject_output=True,
        auto_read_output=True
    )
    
    if result:
        print("\n✅ Check complete!")
        return True
    else:
        print("\n❌ Failed to check max date")
        return False

if __name__ == "__main__":
    success = check_max_date()
    sys.exit(0 if success else 1)






