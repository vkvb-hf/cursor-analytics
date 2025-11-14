#!/usr/bin/env python3
"""
Verify that all CSV data is present in the Databricks table.
Counts rows in each CSV file and compares with table row count.
"""

import sys
import os
import requests
import base64
from databricks import sql
from databricks_job_runner import DatabricksJobRunner
from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN, DATABRICKS_HOST

VERIFICATION_NOTEBOOK = """# Databricks notebook source
# MAGIC %md
# MAGIC # Verify Adyen ML Test Data Table
# MAGIC 
# MAGIC This notebook counts rows in each CSV file and compares with the table.

# COMMAND ----------

import pandas as pd
import requests
import base64
import os
from os import listdir
from os.path import isfile, join

workspace_path = "/Workspace/Users/visal.kumar@hellofresh.com/adyen-ml-test"
table_name = "payments_hf.adyen_ml_test_data"

print("=" * 80)
print("Verify Data Completeness")
print("=" * 80)
print(f"\\n📁 Workspace path: {workspace_path}")
print(f"🎯 Table: {table_name}")
print("=" * 80)

# COMMAND ----------

# Step 1: List all CSV files
print("\\n📋 Step 1: Listing CSV files...")

os.chdir(workspace_path)
csv_files = [f for f in listdir(workspace_path) if isfile(join(workspace_path, f)) and f.endswith('.csv')]

if not csv_files:
    raise Exception("No CSV files found!")

print(f"✅ Found {len(csv_files)} CSV files")

# COMMAND ----------

# Step 2: Count rows in each CSV file
print(f"\\n📊 Step 2: Counting rows in each CSV file...")

# Get token for Workspace API
token = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()
if not token:
    token = os.environ.get('DATABRICKS_TOKEN', '')

if not token:
    raise Exception("No token available for Workspace API")

workspace_host = DATABRICKS_HOST
headers = {"Authorization": f"Bearer {token}"}
dbfs_temp_path = "/tmp/verify_adyen_csvs"

# Create temp directory
dbutils.fs.mkdirs(dbfs_temp_path)

csv_row_counts = []
total_csv_rows = 0

for i, f in enumerate(csv_files, 1):
    workspace_file_path = join(workspace_path, f)
    dbfs_file_path = f"{dbfs_temp_path}/{f}"
    
    if i % 10 == 0 or i <= 5:
        print(f"   Processing [{i}/{len(csv_files)}]: {f}")
    
    try:
        # Download file via Workspace API
        export_url = f"{workspace_host}/api/2.0/workspace/export"
        response = requests.get(export_url, headers=headers, params={"path": workspace_file_path, "format": "SOURCE"})
        
        if response.status_code == 200:
            data = response.json()
            content_b64 = data.get('content', '')
            content = base64.b64decode(content_b64).decode('utf-8')
            
            # Write to DBFS
            dbutils.fs.put(dbfs_file_path, content, overwrite=True)
            
            # Count rows (excluding header and comment lines)
            lines = content.split('\\n')
            # Remove comment lines and empty lines
            data_lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]
            # Subtract 1 for header
            row_count = len(data_lines) - 1 if len(data_lines) > 0 else 0
            
            csv_row_counts.append({
                'filename': f,
                'rows': row_count
            })
            total_csv_rows += row_count
        else:
            print(f"   ⚠️  Warning: Failed to download {f}")
            csv_row_counts.append({
                'filename': f,
                'rows': 0,
                'error': response.text
            })
    except Exception as e:
        print(f"   ⚠️  Error processing {f}: {e}")
        csv_row_counts.append({
            'filename': f,
            'rows': 0,
            'error': str(e)
        })

print(f"\\n✅ Processed {len(csv_row_counts)} files")
print(f"📊 Total rows in CSVs: {total_csv_rows:,}")

# COMMAND ----------

# Step 3: Count rows in table
print(f"\\n📊 Step 3: Counting rows in table...")

table_count_query = f"SELECT COUNT(*) as row_count FROM {table_name}"
table_count_result = spark.sql(table_count_query).collect()
table_row_count = table_count_result[0]['row_count']

print(f"✅ Table row count: {table_row_count:,}")

# COMMAND ----------

# Step 4: Compare and report
print(f"\\n{'=' * 80}")
print("📊 VERIFICATION RESULTS")
print(f"{'=' * 80}")

print(f"\\nCSV Files:")
print(f"   Total files: {len(csv_files)}")
print(f"   Total rows in CSVs: {total_csv_rows:,}")

print(f"\\nTable:")
print(f"   Table name: {table_name}")
print(f"   Total rows in table: {table_row_count:,}")

difference = total_csv_rows - table_row_count
print(f"\\nComparison:")
print(f"   Difference: {difference:,} rows")

if difference == 0:
    print(f"   ✅ PERFECT MATCH! All data loaded correctly.")
elif difference > 0:
    print(f"   ⚠️  Table has fewer rows than CSVs (missing {difference:,} rows)")
    print(f"   This might be due to:")
    print(f"      - Duplicate removal")
    print(f"      - Data type conversion issues")
    print(f"      - NULL/empty row filtering")
else:
    print(f"   ⚠️  Table has more rows than CSVs (extra {abs(difference):,} rows)")
    print(f"   This should not happen - please investigate!")

# COMMAND ----------

# Show per-file breakdown
print(f"\\n{'=' * 80}")
print("📄 Per-File Row Counts (Sample - first 20 files):")
print(f"{'=' * 80}")

for i, file_info in enumerate(csv_row_counts[:20], 1):
    filename = file_info['filename']
    rows = file_info['rows']
    status = "✅" if rows > 0 else "❌"
    print(f"   [{i:2d}] {status} {filename}: {rows:,} rows")
    if 'error' in file_info:
        print(f"        Error: {file_info['error']}")

if len(csv_row_counts) > 20:
    print(f"   ... and {len(csv_row_counts) - 20} more files")

# COMMAND ----------

# Verify table has source_filename column and check distribution
print(f"\\n{'=' * 80}")
print("📊 Table Column Verification:")
print(f"{'=' * 80}")

# Check if source_filename exists
columns_query = f"DESCRIBE {table_name}"
columns_df = spark.sql(columns_query)
print("\\nTable columns:")
columns_df.show(100, truncate=False)

# Count by source_filename
if 'source_filename' in [row['col_name'] for row in columns_df.collect()]:
    print(f"\\n📊 Row count by source_filename (sample):")
    filename_dist_query = f"SELECT source_filename, COUNT(*) as row_count FROM {table_name} GROUP BY source_filename ORDER BY row_count DESC LIMIT 20"
    spark.sql(filename_dist_query).show(100, truncate=False)
    
    # Get total unique filenames
    unique_files_query = f"SELECT COUNT(DISTINCT source_filename) as unique_files FROM {table_name}"
    unique_files_result = spark.sql(unique_files_query).collect()
    unique_files_count = unique_files_result[0]['unique_files']
    print(f"\\n📁 Unique source filenames in table: {unique_files_count}")
    print(f"📁 Total CSV files: {len(csv_files)}")

print(f"\\n{'=' * 80}")
print("✅ Verification complete!")
print(f"{'=' * 80}")
"""


def main():
    """Run verification notebook."""
    print("=" * 80)
    print("Verify Table Data Completeness")
    print("=" * 80)
    
    runner = DatabricksJobRunner()
    
    result = runner.create_and_run(
        notebook_path="/Workspace/Users/visal.kumar@hellofresh.com/verify_adyen_ml_data",
        notebook_content=VERIFICATION_NOTEBOOK,
        job_name="Verify Adyen ML Data",
        timeout_seconds=1800,
        poll_interval=10,
        max_wait=1800,
        show_output=True
    )
    
    success = result.get('success', False)
    
    if success:
        print("\n✅ Verification completed successfully!")
    else:
        print("\n❌ Verification failed!")
        if 'error' in result:
            print(f"   Error: {result['error']}")
    
    return success


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

