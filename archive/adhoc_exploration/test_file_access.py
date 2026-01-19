#!/usr/bin/env python3
"""
Test notebook to check file access methods in Databricks.
Run this as a job to see which method works.
"""

import sys
from databricks_job_runner import DatabricksJobRunner

# Simple test notebook
TEST_NOTEBOOK = """# Databricks notebook source
# MAGIC %md
# MAGIC # Test File Access Methods
# MAGIC 
# MAGIC Testing different ways to access workspace files.

# COMMAND ----------

workspace_path = "/Workspace/Users/visal.kumar@hellofresh.com/adyen-ml-test"

results = []

print("=" * 80)
print("Testing File Access Methods")
print("=" * 80)
print(f"\\nTarget path: {workspace_path}")
results.append(f"Target path: {workspace_path}")

# COMMAND ----------

# Method 1: dbutils.fs.ls (DBFS)
print("\\n" + "=" * 80)
print("Method 1: dbutils.fs.ls")
print("=" * 80)
results.append("\\nMethod 1: dbutils.fs.ls")
try:
    files = dbutils.fs.ls(workspace_path)
    csv_files = [f for f in files if f.name.endswith('.csv')]
    msg = f"✅ SUCCESS! Found {len(csv_files)} CSV files"
    print(msg)
    results.append(msg)
    print(f"   Sample files:")
    results.append("   Sample files:")
    for f in csv_files[:3]:
        line = f"     - {f.name} (path: {f.path})"
        print(line)
        results.append(line)
except Exception as e:
    msg = f"❌ FAILED: {str(e)}"
    print(msg)
    results.append(msg)

# COMMAND ----------

# Method 2: dbutils.workspace.ls (Workspace)
print("\\n" + "=" * 80)
print("Method 2: dbutils.workspace.ls")
print("=" * 80)
results.append("\\nMethod 2: dbutils.workspace.ls")
try:
    files = dbutils.workspace.ls(workspace_path)
    csv_files = [f for f in files if f.path.endswith('.csv')]
    msg = f"✅ SUCCESS! Found {len(csv_files)} CSV files"
    print(msg)
    results.append(msg)
    print(f"   Sample files:")
    results.append("   Sample files:")
    for f in csv_files[:3]:
        line = f"     - {f.name} (path: {f.path})"
        print(line)
        results.append(line)
except Exception as e:
    msg = f"❌ FAILED: {str(e)}"
    print(msg)
    results.append(msg)

# COMMAND ----------

# Method 3: Spark read with workspace path pattern
print("\\n" + "=" * 80)
print("Method 3: Try Spark read with workspace:// prefix")
print("=" * 80)
try:
    # Try reading one file with workspace://
    test_path = workspace_path + "/*.csv"
    test_path_workspace = test_path.replace("/Workspace", "workspace://")
    print(f"   Trying path: {test_path_workspace}")
    
    # Try to list with glob pattern
    files = dbutils.fs.ls(workspace_path + "/*.csv")
    print(f"✅ SUCCESS! Found files")
except Exception as e:
    print(f"❌ FAILED: {e}")
    print("   Note: May need different path format")

# COMMAND ----------

# Method 4: Check if files are accessible via Spark
print("\\n" + "=" * 80)
print("Method 4: Test Spark read access")
print("=" * 80)
results.append("\\nMethod 4: Test Spark read access")
try:
    # Try to get file paths from method 2 (workspace.ls)
    files = dbutils.workspace.ls(workspace_path)
    csv_files = [f for f in files if f.path.endswith('.csv')]
    
    if csv_files:
        test_file = csv_files[0].path
        msg = f"   Testing read of: {test_file}"
        print(msg)
        results.append(msg)
        
        # Try reading with Spark - use the path as-is
        df = spark.read.option("header", "true").csv(test_file)
        count = df.count()
        msg1 = f"✅ SUCCESS! Spark can read file"
        msg2 = f"   Rows: {count}"
        msg3 = f"   Columns: {len(df.columns)}"
        print(msg1)
        print(msg2)
        print(msg3)
        results.extend([msg1, msg2, msg3])
    else:
        msg = "⚠️  No CSV files found to test"
        print(msg)
        results.append(msg)
except Exception as e:
    msg = f"❌ FAILED: {str(e)}"
    print(msg)
    results.append(msg)

# COMMAND ----------

# Final Summary
print("\\n" + "=" * 80)
print("Final Summary")
print("=" * 80)
print("\\n".join(results))
print("\\n" + "=" * 80)
print("Test complete!")
"""


def main():
    """Run the test notebook as a job."""
    runner = DatabricksJobRunner()
    
    result = runner.create_and_run(
        notebook_path="/Workspace/Users/visal.kumar@hellofresh.com/test_file_access",
        notebook_content=TEST_NOTEBOOK,
        job_name="Test File Access Methods",
        timeout_seconds=300,  # 5 minutes should be enough for test
        poll_interval=5,
        max_wait=300,
        show_output=True
    )
    
    print("\n" + "=" * 80)
    print("Test Complete!")
    print("=" * 80)
    
    if result.get('success'):
        print("✅ Test job completed successfully!")
        print("\nCheck the output above to see which file access methods work.")
    else:
        print("⚠️  Test job did not complete successfully")
        print(f"   State: {result.get('result_state')}")
    
    return result.get('success')


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
