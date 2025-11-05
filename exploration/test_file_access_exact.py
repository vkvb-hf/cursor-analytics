#!/usr/bin/env python3
"""Test file access using the exact pattern from CSV uploader notebook."""

import sys
from databricks_job_runner import DatabricksJobRunner

# Test notebook using exact pattern from CSV uploader
TEST_NOTEBOOK = """# Databricks notebook source
import pandas as pd
import numpy as np
import os
from os import listdir
from os.path import isfile, join

print("=" * 80)
print("Test: Access Files Using Your CSV Uploader Pattern")
print("=" * 80)

# Use the exact pattern from your CSV uploader
workspace_path = "/Workspace/Users/visal.kumar@hellofresh.com/adyen-ml-test"

print(f"\\nTesting path: {workspace_path}")

try:
    os.chdir(workspace_path)
    print(f"✅ os.chdir() succeeded")
    
    files = listdir(workspace_path)
    csv_files = [f for f in files if isfile(join(workspace_path, f)) and f.endswith('.csv')]
    
    print(f"✅ os.listdir() succeeded")
    print(f"✅ Found {len(csv_files)} CSV files")
    
    if csv_files:
        # Try reading one file with pandas (like your uploader)
        test_file = csv_files[0]
        print(f"\\n📄 Testing read of: {test_file}")
        
        df_temp = pd.read_csv(test_file, comment='#')
        print(f"✅ pd.read_csv() succeeded!")
        print(f"   Rows: {len(df_temp)}")
        print(f"   Columns: {len(df_temp.columns)}")
        print(f"   Sample columns: {', '.join(df_temp.columns[:5])}")
        
        # Show sample files
        print(f"\\n📋 Sample CSV files found:")
        for i, f in enumerate(csv_files[:5], 1):
            print(f"   [{i}] {f}")
        
        print("\\n" + "=" * 80)
        print("✅ SUCCESS: Files ARE accessible using your pattern!")
        print("=" * 80)
    else:
        print("⚠️  No CSV files found")
        
except Exception as e:
    print(f"\\n❌ FAILED: {e}")
    import traceback
    traceback.print_exc()
    print("=" * 80)
"""


def main():
    """Run test notebook as a job."""
    runner = DatabricksJobRunner()
    
    result = runner.create_and_run(
        notebook_path="/Workspace/Users/visal.kumar@hellofresh.com/test_file_access_exact",
        notebook_content=TEST_NOTEBOOK,
        job_name="Test File Access (Exact Pattern)",
        timeout_seconds=300,
        poll_interval=5,
        max_wait=300,
        show_output=True
    )
    
    print("\n" + "=" * 80)
    if result.get('success'):
        print("✅ Test PASSED - Files ARE accessible!")
    else:
        print("❌ Test FAILED - Files not accessible")
        print(f"   State: {result.get('result_state')}")
    print("=" * 80)
    
    return result.get('success')


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
