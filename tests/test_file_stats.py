#!/usr/bin/env python3
"""Test reading one file and printing stats."""

import sys
from databricks_job_runner import DatabricksJobRunner

# Test notebook - read one file and show stats
TEST_NOTEBOOK = """# Databricks notebook source
import pandas as pd
import numpy as np
import os
from os import listdir
from os.path import isfile, join

print("=" * 80)
print("Test: Read One File and Print Stats")
print("=" * 80)

workspace_path = "/Workspace/Users/visal.kumar@hellofresh.com/adyen-ml-test"

# Get CSV files
os.chdir(workspace_path)
csv_files = [f for f in listdir(workspace_path) if isfile(join(workspace_path, f)) and f.endswith('.csv')]

if not csv_files:
    raise Exception("No CSV files found!")

print(f"\\n✅ Found {len(csv_files)} CSV files")
print(f"\\n📄 Testing with first file: {csv_files[0]}")

# Workaround: Download via Workspace API to DBFS, then read with Spark
test_file = csv_files[0]
workspace_file_path = join(workspace_path, test_file)
dbfs_temp_path = "/tmp/test_adyen_csv"
dbfs_file_path = f"{dbfs_temp_path}/{test_file}"

print(f"   File: {test_file}")
print(f"   Downloading from workspace to DBFS...")

# Download file content via Workspace API and write to DBFS
import requests
import base64
import os

# Get Databricks token (jobs have access to this)
token = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()
if not token:
    # Try from environment
    token = os.environ.get('DATABRICKS_TOKEN', '')

if token:
    workspace_host = "https://hf-gp.cloud.databricks.com"
    headers = {"Authorization": f"Bearer {token}"}
    
    # Download file from workspace
    export_url = f"{workspace_host}/api/2.0/workspace/export"
    response = requests.get(export_url, headers=headers, params={"path": workspace_file_path, "format": "SOURCE"})
    
    if response.status_code == 200:
        data = response.json()
        content_b64 = data.get('content', '')
        content = base64.b64decode(content_b64).decode('utf-8')
        
        # Write to DBFS
        dbutils.fs.mkdirs(dbfs_temp_path)
        dbutils.fs.put(dbfs_file_path, content, overwrite=True)
        print(f"   ✅ File downloaded and written to DBFS")
        
        # Read from DBFS with pandas
        df_temp = pd.read_csv(f"/dbfs{dbfs_file_path}", comment='#')
        print(f"   ✅ File read successfully")
    else:
        raise Exception(f"Failed to download: {response.text}")
else:
    raise Exception("No token available for Workspace API")

print(f"\\n{'=' * 80}")
print("📊 File Statistics:")
print(f"{'=' * 80}")
print(f"Rows: {len(df_temp):,}")
print(f"Columns: {len(df_temp.columns)}")
print(f"\\nColumn Names:")
for i, col in enumerate(df_temp.columns, 1):
    print(f"   [{i:2d}] {col}")

print(f"\\nSample Data (first 3 rows):")
print(df_temp.head(3).to_string(max_cols=8))

print(f"\\nData Types:")
for col in df_temp.columns[:10]:
    dtype = str(df_temp[col].dtype)
    print(f"   {col}: {dtype}")

print(f"\\n{'=' * 80}")
print("✅ Test complete!")
print(f"{'=' * 80}")
"""


def main():
    """Run test notebook."""
    runner = DatabricksJobRunner()
    
    result = runner.create_and_run(
        notebook_path="/Workspace/Users/visal.kumar@hellofresh.com/test_file_stats",
        notebook_content=TEST_NOTEBOOK,
        job_name="Test File Stats",
        timeout_seconds=300,
        poll_interval=5,
        max_wait=300,
        show_output=True
    )
    
    return result.get('success')


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
