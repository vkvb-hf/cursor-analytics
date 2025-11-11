#!/usr/bin/env python3
"""
Example: Create and run a Databricks notebook with terminal output

This demonstrates the pattern for creating notebooks that show output in terminal.
"""
import sys
import os
import requests
import base64

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from databricks_api import DatabricksAPI
from config import DATABRICKS_HOST, TOKEN

def main():
    """Example of creating and running a notebook with terminal output."""
    
    # Initialize API
    db = DatabricksAPI()
    
    # IMPORTANT: Notebook must write output to DBFS file
    # This is the key requirement for seeing output in terminal
    output_file = "/tmp/my_analysis_output.txt"
    
    notebook_content = f"""# Databricks notebook source
# MAGIC %md
# MAGIC # Example Analysis
# MAGIC 
# MAGIC This notebook demonstrates how to show output in terminal.

# COMMAND ----------

# Your SQL query
query = \"\"\"SELECT *
FROM payments_hf.adyen_ml_test_cust_data
WHERE customer_uuid IS NOT NULL
LIMIT 10\"\"\"

# Execute query
result_df = spark.sql(query)

# Format output
import pandas as pd
pandas_df = result_df.toPandas()

# Build output string
output_lines = []
output_lines.append("=" * 100)
output_lines.append("QUERY RESULTS:")
output_lines.append("=" * 100)
output_lines.append(pandas_df.to_string())
output_lines.append("\\n")
output_lines.append(f"Total records: {{len(pandas_df)}}")
output_lines.append("=" * 100)

# CRITICAL: Write output to DBFS file
# This allows us to read it back after job completion
output_text = "\\n".join(output_lines)
dbutils.fs.put("{output_file}", output_text, overwrite=True)

# Also print for UI visibility
print(output_text)
"""
    
    # Create and run notebook
    print("=" * 80)
    print("Creating and running notebook...")
    print("=" * 80)
    
    result = db.job_runner.create_and_run(
        notebook_path="/Shared/example_notebook",
        notebook_content=notebook_content,
        job_name="example_notebook_job",
        timeout_seconds=3600,
        poll_interval=5,
        max_wait=300,
        show_output=True
    )
    
    # Read output from DBFS
    if result.get('success'):
        print("\n" + "=" * 80)
        print("READING OUTPUT FROM DBFS:")
        print("=" * 80)
        
        headers = {"Authorization": f"Bearer {TOKEN}"}
        read_url = f"{DATABRICKS_HOST}/api/2.0/dbfs/read"
        read_response = requests.get(
            read_url,
            headers=headers,
            json={"path": output_file}
        )
        
        if read_response.status_code == 200:
            file_data = read_response.json()
            if 'data' in file_data:
                output_content = base64.b64decode(file_data['data']).decode('utf-8')
                
                print("\n" + "=" * 80)
                print("NOTEBOOK OUTPUT (Visible in Terminal):")
                print("=" * 80)
                print(output_content)
                print("=" * 80)
            else:
                print("⚠️  Output file exists but is empty")
        else:
            print(f"⚠️  Could not read output file (status: {read_response.status_code})")
    else:
        print("✗ Job failed or encountered an error")
        if result.get('error'):
            print(f"Error: {result.get('error')}")

if __name__ == "__main__":
    main()


