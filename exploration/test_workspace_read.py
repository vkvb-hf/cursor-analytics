#!/usr/bin/env python3
"""Test if we can read workspace files using your exact pattern in a job."""

import sys
from databricks_job_runner import DatabricksJobRunner

# Test using your EXACT pattern from CSV uploader
TEST_NOTEBOOK = """# Databricks notebook source
# MAGIC %md
# MAGIC # Test: Read Files Using Your CSV Uploader Pattern
# MAGIC 
# MAGIC Using exact same approach as your working CSV uploader

# COMMAND ----------

import pandas as pd
import numpy as np
import os
from os import listdir
from os.path import isfile, join

print("=" * 80)
print("Test: Your CSV Uploader Pattern")
print("=" * 80)

# Use YOUR exact pattern
mypath = "/Workspace/Users/visal.kumar@hellofresh.com/adyen-ml-test"

print(f"\\nPath: {mypath}")
print("\\nUsing your exact pattern:")
print("  os.chdir(mypath)")
print("  for f in listdir(mypath):")
print("    if isfile(join(mypath, f)):")
print("      df_temp = pd.read_csv(f)")

# COMMAND ----------

os.chdir(mypath)
print(f"✅ os.chdir() succeeded")

files = listdir(mypath)
csv_files = [f for f in files if isfile(join(mypath, f)) and f.endswith('.csv')]

print(f"✅ listdir() succeeded")
print(f"✅ Found {len(csv_files)} CSV files")

if csv_files:
    print(f"\\n📄 Testing with first file: {csv_files[0]}")
    
    # Try your exact pattern
    try:
        df_temp = pd.read_csv(csv_files[0], comment='#')
        print(f"✅ pd.read_csv() SUCCEEDED!")
        print(f"\\n{'=' * 80}")
        print("📊 File Statistics:")
        print(f"{'=' * 80}")
        print(f"Rows: {len(df_temp):,}")
        print(f"Columns: {len(df_temp.columns)}")
        print(f"\\nColumn Names:")
        for i, col in enumerate(df_temp.columns[:10], 1):
            print(f"   [{i:2d}] {col}")
        if len(df_temp.columns) > 10:
            print(f"   ... and {len(df_temp.columns) - 10} more columns")
        
        print(f"\\nSample Data (first row):")
        print(df_temp.head(1).to_string())
        
        print(f"\\nData Types:")
        print(df_temp.dtypes.to_string())
        
        print(f"\\n{'=' * 80}")
        print("✅ CONFIRMED: Your pattern WORKS!")
        print(f"{'=' * 80}")
    except Exception as e:
        print(f"❌ pd.read_csv() FAILED: {e}")
        import traceback
        traceback.print_exc()
else:
    print("⚠️  No CSV files found")
"""


def main():
    """Run test."""
    runner = DatabricksJobRunner()
    
    result = runner.create_and_run(
        notebook_path="/Workspace/Users/visal.kumar@hellofresh.com/test_workspace_read",
        notebook_content=TEST_NOTEBOOK,
        job_name="Test Workspace Read (Your Pattern)",
        timeout_seconds=300,
        poll_interval=5,
        max_wait=300,
        show_output=True
    )
    
    print("\n" + "=" * 80)
    if result.get('success'):
        print("✅ Test PASSED - Files readable with your pattern!")
    else:
        print("⚠️  Need to check output")
    print("=" * 80)
    
    return result.get('success')


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
