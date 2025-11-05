#!/usr/bin/env python3
"""
Create a Databricks notebook, submit it as a job, run it, and capture the output.

Using only files from cursor_databricks folder structure.

IMPORTANT: To see output in terminal, the notebook MUST write output to DBFS.
The Databricks Jobs API does not capture stdout/stderr from print() or DataFrame.show().

See HOW_TO_CREATE_AND_RUN_NOTEBOOKS.md for detailed instructions.
"""
import sys
import os
import time

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from databricks_api import DatabricksAPI
from core.databricks_workspace import create_workspace_directory
from config import DATABRICKS_HOST, TOKEN
import requests
import json

def main():
    # Initialize the API
    db = DatabricksAPI()
    
    # Notebook content - writes output to DBFS so we can read it back
    import uuid
    output_file_id = str(uuid.uuid4())[:8]
    output_file_path = f"/tmp/notebook_output_{output_file_id}.txt"
    
    notebook_content = f"""# Databricks notebook source
# MAGIC %md
# MAGIC # Sample Records from adyen_ml_test_cust_data
# MAGIC 
# MAGIC Query to show sample records where customer_uuid is not null

# COMMAND ----------

# Run SQL query and display results
query = \"\"\"SELECT *
FROM payments_hf.adyen_ml_test_cust_data
WHERE customer_uuid IS NOT NULL
LIMIT 10\"\"\"

# Execute query and get results
result_df = spark.sql(query)

# Convert to pandas for formatting
import pandas as pd
pandas_df = result_df.toPandas()

# Build output string
output_lines = []
output_lines.append("=" * 100)
output_lines.append("QUERY RESULTS:")
output_lines.append("=" * 100)
output_lines.append("\\n")
output_lines.append(pandas_df.to_string())
output_lines.append("\\n")
output_lines.append("=" * 100)
output_lines.append(f"Total records: {{len(pandas_df)}}")
output_lines.append("=" * 100)

# Write output to file in DBFS so we can retrieve it
output_text = "\\n".join(output_lines)
dbutils.fs.put("{output_file_path}", output_text, overwrite=True)

# Also display in notebook (for UI visibility)
print(output_text)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Query completed successfully!
# MAGIC Output written to: {output_file_path}
"""
    
    # Try Shared workspace which should always exist
    notebook_path = "/Shared/sample_adyen_ml_query"
    job_name = "sample_adyen_ml_cust_data_query"
    
    print("=" * 80)
    print("Creating Databricks Notebook and Job")
    print("=" * 80)
    print(f"Notebook Path: {notebook_path}")
    print(f"Job Name: {job_name}")
    print()
    
    # First, create the notebook directly (notebook creation)
    print("Step 1: Creating notebook...")
    notebook_created = db.job_runner.create_notebook(
        notebook_path=notebook_path,
        content=notebook_content,
        overwrite=True
    )
    
    if not notebook_created:
        print("✗ Failed to create notebook. Trying alternative approach...")
        # If Shared doesn't work, try creating user directory first
        print("Creating user directory...")
        try:
            create_workspace_directory(
                databricks_path="/Users/visal.kumar@deliveroo.com",
                workspace_host=DATABRICKS_HOST,
                token=TOKEN
            )
            notebook_path = "/Users/visal.kumar@deliveroo.com/sample_adyen_ml_query"
            notebook_created = db.job_runner.create_notebook(
                notebook_path=notebook_path,
                content=notebook_content,
                overwrite=True
            )
            if not notebook_created:
                print("✗ Failed to create notebook in user directory")
                return 1
        except Exception as e:
            print(f"✗ Could not create user directory: {e}")
            return 1
    
    print("✓ Notebook created successfully")
    print()
    
    # Now create and run the job
    print("Step 2: Creating and running job...")
    print()
    
    result = db.job_runner.create_and_run(
        notebook_path=notebook_path,
        notebook_content=notebook_content,  # Not needed since notebook exists, but method requires it
        job_name=job_name,
        timeout_seconds=3600,
        poll_interval=5,
        max_wait=300,
        show_output=True
    )
    
    print()
    print("=" * 80)
    print("Final Results")
    print("=" * 80)
    
    if result.get('success'):
        print("✓ Job completed successfully!")
        print(f"✓ Job ID: {result.get('job_id')}")
        print(f"✓ Run ID: {result.get('run_id')}")
        
        # Get and display notebook output using Databricks Jobs API
        print("\n" + "=" * 80)
        print("RETRIEVING NOTEBOOK OUTPUT FROM DATABRICKS JOB")
        print("=" * 80)
        
        # Get the task run ID to retrieve notebook output
        task_run_id = None
        cluster_id = None
        if result.get('run_id'):
            # Get the full run status to find task run IDs and cluster info
            run_status = db.job_runner.get_run_status(str(result.get('run_id')))
            if run_status and 'tasks' in run_status:
                for task in run_status['tasks']:
                    task_run_id = task.get('run_id')
                    # Get cluster ID for potential log access
                    if 'cluster_instance' in task:
                        cluster_id = task['cluster_instance'].get('cluster_id')
                    if task_run_id:
                        break
        
        # Retrieve notebook output using the API
        if task_run_id:
            print(f"\nFetching output from task run: {task_run_id}...")
            headers = {"Authorization": f"Bearer {TOKEN}"}
            
            # Get output using the Jobs API
            output_url = f"{DATABRICKS_HOST}/api/2.1/jobs/runs/get-output?run_id={task_run_id}"
            try:
                output_response = requests.get(output_url, headers=headers)
                output_response.raise_for_status()
                notebook_output = output_response.json()
                
                print("\n" + "=" * 80)
                print("NOTEBOOK EXECUTION OUTPUT:")
                print("=" * 80)
                
                # Extract and display notebook output
                if 'notebook_output' in notebook_output:
                    output = notebook_output['notebook_output']
                    
                    # Extract and display results
                    if 'result' in output:
                        result_data = output['result']
                        
                        # Display text/plain output (print statements, SQL results)
                        if 'data' in result_data:
                            found_output = False
                            for item in result_data['data']:
                                if 'text/plain' in item:
                                    print(item['text/plain'])
                                    found_output = True
                                elif 'text/html' in item:
                                    # HTML output - might contain formatted tables
                                    html_content = item['text/html']
                                    print("HTML Output:")
                                    print(html_content)
                                    found_output = True
                                elif 'application/vnd.databricks.result' in item:
                                    # Structured result (DataFrame output)
                                    result_obj = item['application/vnd.databricks.result']
                                    print("Structured Result:")
                                    print(json.dumps(result_obj, indent=2)[:5000])
                                    found_output = True
                            
                            if not found_output:
                                print("Output data structure:")
                                print(json.dumps(result_data, indent=2)[:3000])
                        
                        # Display errors if any
                        if 'errorSummary' in result_data:
                            print(f"\n❌ Error: {result_data['errorSummary']}")
                        if 'cause' in result_data:
                            print(f"   Cause: {result_data['cause']}")
                    else:
                        # Show raw output structure
                        print("Raw notebook output:")
                        print(json.dumps(output, indent=2)[:5000])
                
                # Also check for error output
                if 'error' in notebook_output:
                    print(f"\n❌ Job Error: {notebook_output['error']}")
                if 'error_trace' in notebook_output:
                    print(f"\n❌ Error Trace: {notebook_output['error_trace']}")
                
                # Read output from DBFS file (notebook writes output to file)
                print("\n" + "=" * 80)
                print("RETRIEVING NOTEBOOK OUTPUT FROM DBFS:")
                print("=" * 80)
                
                # Extract output file path from notebook content
                import re
                output_file_match = re.search(r'dbutils\.fs\.put\("([^"]+)"', notebook_content)
                if output_file_match:
                    dbfs_file_path = output_file_match.group(1)
                    print(f"Reading output from: {dbfs_file_path}")
                    
                    try:
                        # Read file from DBFS using Databricks API
                        read_url = f"{DATABRICKS_HOST}/api/2.0/dbfs/read"
                        read_payload = {"path": dbfs_file_path}
                        read_response = requests.get(read_url, headers=headers, json=read_payload)
                        
                        if read_response.status_code == 200:
                            file_data = read_response.json()
                            if 'data' in file_data:
                                import base64
                                output_content = base64.b64decode(file_data['data']).decode('utf-8')
                                
                                print("\n" + "=" * 80)
                                print("NOTEBOOK EXECUTION OUTPUT:")
                                print("=" * 80)
                                print(output_content)
                                print("=" * 80)
                            else:
                                print("⚠️  File exists but no data found")
                                print(f"Response: {json.dumps(file_data, indent=2)}")
                        else:
                            print(f"⚠️  Could not read file (status: {read_response.status_code})")
                            print(f"   Response: {read_response.text}")
                    except Exception as e:
                        print(f"⚠️  Error reading output file: {e}")
                        import traceback
                        traceback.print_exc()
                else:
                    print("⚠️  Could not extract output file path from notebook")
                
            except Exception as e:
                print(f"\n⚠️  Error retrieving output: {e}")
                print("Output may not be available via API yet.")
        else:
            print("\n⚠️  Could not find task run ID to retrieve output")
        
        print("\n" + "=" * 80)
        print(f"📊 View notebook execution in Databricks UI:")
        print(f"   https://hf-gp.cloud.databricks.com/?o=4157495209488006#job/{result.get('job_id')}/run/{result.get('run_id')}")
        print("=" * 80)
        
        return 0
    else:
        print("✗ Job failed or encountered an error")
        if result.get('error'):
            print(f"Error: {result.get('error')}")
        if result.get('run_id'):
            print(f"Run ID: {result.get('run_id')}")
            print(f"Check status in Databricks UI:")
            print(f"  https://hf-gp.cloud.databricks.com/#job/{result.get('job_id')}/run/{result.get('run_id')}")
        return 1

if __name__ == "__main__":
    sys.exit(main())

