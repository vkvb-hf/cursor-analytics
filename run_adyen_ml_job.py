#!/usr/bin/env python3
"""
Run Adyen ML Test Data creation using the generic job runner.
"""

import sys
from databricks_job_runner import DatabricksJobRunner
from config import DATABRICKS_HOST

# Notebook content (workspace_host will be inserted dynamically)
NOTEBOOK_CONTENT = """# Databricks notebook source
# MAGIC %md
# MAGIC # Create Adyen ML Test Data Table using PySpark
# MAGIC 
# MAGIC This notebook reads all CSV files in parallel and creates a Delta table.

# COMMAND ----------

# Risk profile mapping
RISK_PROFILE_MAPPING = {
    'THLH73H2VSWDN842': 'Jade1314 CANADA ML',
    'QNN7MK9V6T5T87F3': 'Very_High_ecomm',
    'TBDLJCJZX8LLWWF3': 'Medium_ecomm',
    'J2M3VKGZMHZNZ4Q9': 'Medium',
    'DXPLDK9V6T5T87F3': 'High_ecomm',
    'QLKKNG4S2Q9428Q9': 'Very_High',
    'ZDGX3H4S2Q9428Q9': 'High'
}

workspace_path = "/Workspace/Users/visal.kumar@hellofresh.com/adyen-ml-test"
table_name = "payments_hf.adyen_ml_test_data"
drop_if_exists = True

print("=" * 80)
print("Create Table using PySpark (Fast Parallel Processing)")
print("=" * 80)
print(f"\\n📁 Workspace path: {workspace_path}")
print(f"🎯 Table name: {table_name}")
print("=" * 80)

# COMMAND ----------

# Step 1: Get CSV files using your exact pattern (confirmed to work in jobs)
print("\\n📋 Step 1: Getting CSV file paths...")

import pandas as pd
import numpy as np
import os
from os import listdir
from os.path import isfile, join

# Use your exact pattern from CSV uploader notebook
os.chdir(workspace_path)
csv_files = [f for f in listdir(workspace_path) if isfile(join(workspace_path, f)) and f.endswith('.csv')]

if not csv_files:
    raise Exception("No CSV files found!")

print(f"✅ Found {len(csv_files)} CSV files")

# Show files
print("\\n📄 Files to process:")
for i, filename in enumerate(csv_files[:10], 1):
    print(f"   [{i:2d}] {filename}")
if len(csv_files) > 10:
    print(f"   ... and {len(csv_files) - 10} more files")

# COMMAND ----------

# Step 2: Download files from workspace to DBFS, then read with Spark
print(f"\\n📥 Step 2: Processing {len(csv_files)} CSV files...")
print("   Step 2a: Downloading files from workspace to DBFS...")

import requests
import base64
import os

# Get token for Workspace API
token = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()
if not token:
    token = os.environ.get('DATABRICKS_TOKEN', '')

if not token:
    raise Exception("No token available for Workspace API")

workspace_host = "{DATABRICKS_HOST}"
headers = {"Authorization": f"Bearer {token}"}
dbfs_temp_path = "/tmp/adyen_ml_csvs"
dbfs_file_paths = []

# Download all files to DBFS
dbutils.fs.mkdirs(dbfs_temp_path)

for i, f in enumerate(csv_files, 1):
    workspace_file_path = join(workspace_path, f)
    dbfs_file_path = f"{dbfs_temp_path}/{f}"
    
    if i % 10 == 0 or i == 1:
        print(f"   Downloading [{i}/{len(csv_files)}]: {f}")
    
    # Download file via Workspace API
    export_url = f"{workspace_host}/api/2.0/workspace/export"
    response = requests.get(export_url, headers=headers, params={"path": workspace_file_path, "format": "SOURCE"})
    
    if response.status_code == 200:
        data = response.json()
        content_b64 = data.get('content', '')
        content = base64.b64decode(content_b64).decode('utf-8')
        dbutils.fs.put(dbfs_file_path, content, overwrite=True)
        dbfs_file_paths.append(dbfs_file_path)
    else:
        print(f"   ⚠️  Warning: Failed to download {f}: {response.text}")

print(f"\\n✅ Downloaded {len(dbfs_file_paths)}/{len(csv_files)} files to DBFS")

# COMMAND ----------

# Step 2b: Read files individually and add filename as literal (more reliable than input_file_name)
print(f"\\n📥 Step 2b: Reading {len(dbfs_file_paths)} CSV files from DBFS with Spark...")
print("   ⚡ Reading files individually and adding source_filename...")

from pyspark.sql.functions import lit

# Read first file to get schema
first_file = dbfs_file_paths[0]
first_filename = first_file.split('/')[-1]  # Extract just filename
print(f"   Reading [1/{len(dbfs_file_paths)}]: {first_filename}")

df_sample = spark.read \\
    .option("header", "true") \\
    .option("inferSchema", "false") \\
    .option("comment", "#") \\
    .option("multiLine", "false") \\
    .option("ignoreLeadingWhiteSpace", "true") \\
    .option("ignoreTrailingWhiteSpace", "true") \\
    .csv(first_file)

# Add source filename as literal (more reliable)
df_sample = df_sample.withColumn("source_filename", lit(first_filename))

# Read remaining files and union
dataframes = [df_sample]

for i, file_path in enumerate(dbfs_file_paths[1:], 2):
    filename = file_path.split('/')[-1]  # Extract just filename
    
    if i % 10 == 0 or i <= 5:
        print(f"   Reading [{i}/{len(dbfs_file_paths)}]: {filename}")
    
    df_temp = spark.read \\
        .option("header", "true") \\
        .option("inferSchema", "false") \\
        .option("comment", "#") \\
        .option("multiLine", "false") \\
        .option("ignoreLeadingWhiteSpace", "true") \\
        .option("ignoreTrailingWhiteSpace", "true") \\
        .csv(file_path)
    
    # Add source filename as literal (more reliable than input_file_name)
    df_temp = df_temp.withColumn("source_filename", lit(filename))
    dataframes.append(df_temp)

# Union all dataframes
from functools import reduce
df = reduce(lambda a, b: a.unionByName(b, allowMissingColumns=True), dataframes)

row_count = df.count()
print(f"\\n✅ Successfully read DataFrame")
print(f"   📊 Total rows: {row_count:,}")
print(f"   📋 Columns: {len(df.columns)}")

# Show stats
print(f"\\n{'=' * 80}")
print("📊 Data Statistics:")
print(f"{'=' * 80}")
print(f"Total Rows: {row_count:,}")
print(f"Total Columns: {len(df.columns)}")
print(f"\\nColumn Names:")
for i, col in enumerate(df.columns, 1):
    print(f"   [{i:2d}] {col}")
    
print(f"\\nSample Data (first 2 rows):")
df.show(2, truncate=False)
print(f"{'=' * 80}")

# COMMAND ----------

# Step 3: Add custom columns (source_filename already added in Step 2b)
print("\\n🔧 Step 3: Adding custom columns...")

from pyspark.sql.functions import (
    col, 
    regexp_extract,
    when,
    lit
)

# Extract profile reference from filename
# Filename format: COUNTRY_PROFILEREF_Jade1314 timestamp.csv
# Profile reference is the second part when split by underscore (13 characters)
# Example: AU_TBDLJCJZX8LLWWF3_Jade1314... -> TBDLJCJZX8LLWWF3
from pyspark.sql.functions import split, element_at
df = df.withColumn(
    "profile_reference",
    element_at(split(col("source_filename"), "_"), 2)
)

# Map risk profile based on profile_reference
risk_profile_expr = when(
    col("profile_reference") == "THLH73H2VSWDN842", lit("Jade1314 CANADA ML")
).when(
    col("profile_reference") == "QNN7MK9V6T5T87F3", lit("Very_High_ecomm")
).when(
    col("profile_reference") == "TBDLJCJZX8LLWWF3", lit("Medium_ecomm")
).when(
    col("profile_reference") == "J2M3VKGZMHZNZ4Q9", lit("Medium")
).when(
    col("profile_reference") == "DXPLDK9V6T5T87F3", lit("High_ecomm")
).when(
    col("profile_reference") == "QLKKNG4S2Q9428Q9", lit("Very_High")
).when(
    col("profile_reference") == "ZDGX3H4S2Q9428Q9", lit("High")
).otherwise(lit("Unknown"))

df = df.withColumn("risk_profile", risk_profile_expr)

print("✅ Added columns: source_filename, profile_reference, risk_profile")

# COMMAND ----------

# Step 4: Sanitize column names
print("\\n🧹 Step 4: Sanitizing column names...")

for col_name in df.columns:
    if ' ' in col_name or any(char in col_name for char in [',', ';', '{', '}', '(', ')']):
        new_name = col_name.replace(' ', '_').replace(',', '_').replace(';', '_') \\
            .replace('{', '_').replace('}', '_').replace('(', '_').replace(')', '_')
        df = df.withColumnRenamed(col_name, new_name)

print("✅ Column names sanitized")
print(f"   Columns: {', '.join(df.columns[:10])}...")

# COMMAND ----------

# Step 5: Remove duplicates
print("\\n🔍 Step 5: Removing duplicates...")

row_count_before = df.count()
print(f"   Rows before deduplication: {row_count_before:,}")

df = df.dropDuplicates()
row_count_after = df.count()
duplicates_removed = row_count_before - row_count_after

print(f"✅ Removed {duplicates_removed:,} duplicate rows")
print(f"   Remaining rows: {row_count_after:,}")

# COMMAND ----------

# Step 6: Create Delta table
print(f"\\n💾 Step 6: Creating Delta table '{table_name}'...")

schema, table = table_name.split('.') if '.' in table_name else ('default', table_name)
table_location = f"s3://hf-payments-data-lake-live-main/{schema}/{table}_v2"

if drop_if_exists:
    print("   Dropping existing table if it exists...")
    spark.sql(f"DROP TABLE IF EXISTS {table_name}")

# Write to Delta table partitioned by source_filename for better performance
print(f"   Writing to: {table_location}")
print(f"   Partitioned by: source_filename")
print("   ⚡ Spark will write in parallel...")

df.write \\
    .format("delta") \\
    .mode("overwrite") \\
    .option("path", table_location) \\
    .option("overwriteSchema", "true") \\
    .partitionBy("source_filename") \\
    .saveAsTable(table_name)

print("✅ Delta table created successfully!")

# COMMAND ----------

# Step 7: Verification
print("\\n📊 Step 7: Verification...")

result_df = spark.table(table_name)
total_rows = result_df.count()
distinct_files = result_df.select("source_filename").distinct().count()

print(f"✅ Table verification:")
print(f"   Total rows: {total_rows:,}")
print(f"   Distinct files: {distinct_files}")
print(f"   Columns: {len(result_df.columns)}")

# Show sample data
print("\\n📋 Sample data:")
result_df.select("source_filename", "profile_reference", "risk_profile").distinct().show(20, truncate=False)

# COMMAND ----------

print("\\n" + "=" * 80)
print("✅ SUCCESS! Table created using PySpark")
print(f"📊 Query your table: SELECT * FROM {table_name} LIMIT 10")
print("=" * 80)
"""


def main():
    """Main function."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Run Adyen ML table creation job')
    parser.add_argument('--drop-if-exists', action='store_true', help='Drop table if exists')
    parser.add_argument('--timeout', type=int, default=3600, help='Job timeout in seconds')
    
    args = parser.parse_args()
    
    notebook_path = "/Workspace/Users/visal.kumar@hellofresh.com/create_adyen_ml_test_data"
    job_name = "Create Adyen ML Test Data Table"
    
    # Update content based on args if needed
    if args.drop_if_exists:
        # Content already has drop_if_exists = True
        pass
    
    # Format notebook content with DATABRICKS_HOST from config (use replace due to dict literals in content)
    formatted_notebook_content = NOTEBOOK_CONTENT.replace('{DATABRICKS_HOST}', DATABRICKS_HOST)
    
    # Create runner and execute
    runner = DatabricksJobRunner()
    result = runner.create_and_run(
        notebook_path=notebook_path,
        notebook_content=formatted_notebook_content,
        job_name=job_name,
        timeout_seconds=args.timeout,
        poll_interval=10,
        max_wait=args.timeout,
        show_output=True
    )
    
    # Final summary
    print("\n" + "=" * 80)
    if result.get('success'):
        print("✅ Job completed successfully!")
        print(f"📊 Table: payments_hf.adyen_ml_test_data")
        print(f"📊 Query: SELECT * FROM payments_hf.adyen_ml_test_data LIMIT 10")
    else:
        print("⚠️  Job did not complete successfully")
        if result.get('result_state'):
            print(f"   Final state: {result['result_state']}")
    print("=" * 80)
    
    sys.exit(0 if result.get('success') else 1)


if __name__ == "__main__":
    main()
