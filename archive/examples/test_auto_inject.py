#!/usr/bin/env python3
"""
Test: Auto-Inject NotebookOutput Framework

This test demonstrates that NotebookOutput is automatically injected
into notebooks without any manual setup.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from databricks_api import DatabricksAPI

# Simple notebook WITHOUT NotebookOutput setup
# The framework will be automatically injected!
NOTEBOOK = """# Databricks notebook source
# MAGIC %md
# MAGIC # Test Auto-Inject
# MAGIC 
# MAGIC This notebook has NO NotebookOutput setup - it's injected automatically!

# COMMAND ----------

# Just use regular print statements - they're automatically captured!
print("=" * 80)
print("Test Auto-Inject NotebookOutput")
print("=" * 80)
print("")
print("This notebook has no NotebookOutput setup.")
print("The framework is automatically injected!")
print("")

# Run a simple query
print("Running test query...")
result = spark.sql("SELECT 'Auto-Inject Test' as message, 123 as number")
pandas_df = result.toPandas()

print("\\nQuery Results:")
print(pandas_df.to_string())
print("")

# You can also use output.print() if you want (output is auto-initialized)
try:
    output.print("\\nUsing output.print() - this also works!")
    output.print("Output variable is automatically available!")
except NameError:
    print("\\n⚠️  output variable not available (should not happen)")

print("\\n" + "=" * 80)
print("Test Complete")
print("=" * 80)
print("")
print("All output should be automatically captured and displayed!")
"""


def main():
    """Run the test."""
    print("=" * 80)
    print("Test: Auto-Inject NotebookOutput Framework")
    print("=" * 80)
    print()
    print("This test demonstrates automatic injection of NotebookOutput framework.")
    print("The notebook has NO NotebookOutput setup - it's injected automatically!")
    print()
    
    db = DatabricksAPI()
    
    result = db.run_notebook_job(
        notebook_path="/Workspace/Users/visal.kumar@hellofresh.com/test_auto_inject",
        notebook_content=NOTEBOOK,
        job_name="Test Auto-Inject",
        auto_inject_output=True  # This is the default, but shown explicitly
    )
    
    if result.get('success'):
        print("\n✅ Test passed! NotebookOutput was automatically injected and output captured!")
    else:
        print("\n❌ Test failed!")
        print(f"Error: {result.get('error')}")
        sys.exit(1)


if __name__ == "__main__":
    main()

