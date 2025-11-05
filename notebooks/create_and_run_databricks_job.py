#!/usr/bin/env python3
"""
Create a Databricks notebook and run it as a job.
Then monitor and show the output.
"""

import requests
import json
import time
import sys
from config import DATABRICKS_HOST, TOKEN

# Notebook content
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

# Step 1: Get CSV file paths using dbutils
print("\\n📋 Step 1: Getting CSV file paths...")

files = dbutils.fs.ls(workspace_path)
csv_paths = [f.path for f in files if f.name.endswith('.csv')]

if not csv_paths:
    raise Exception("No CSV files found!")

print(f"✅ Found {len(csv_paths)} CSV files")

# Show files
print("\\n📄 Files to process:")
for i, csv_path in enumerate(csv_paths[:10], 1):
    filename = csv_path.split('/')[-1]
    print(f"   [{i:2d}] {filename}")
if len(csv_paths) > 10:
    print(f"   ... and {len(csv_paths) - 10} more files")

# COMMAND ----------

# Step 2: Read all CSV files in parallel with Spark
print(f"\\n📥 Step 2: Reading {len(csv_paths)} CSV files in parallel...")
print("   ⚡ Spark will automatically parallelize this operation...")

df = spark.read \\
    .option("header", "true") \\
    .option("inferSchema", "false") \\
    .option("comment", "#") \\
    .option("multiLine", "false") \\
    .option("ignoreLeadingWhiteSpace", "true") \\
    .option("ignoreTrailingWhiteSpace", "true") \\
    .csv(csv_paths)

row_count = df.count()
print(f"\\n✅ Successfully read DataFrame")
print(f"   📊 Total rows: {row_count:,}")
print(f"   📋 Columns: {len(df.columns)}")
print(f"   📝 Columns: {', '.join(df.columns)}")

# COMMAND ----------

# Step 3: Add custom columns
print("\\n🔧 Step 3: Adding custom columns...")

from pyspark.sql.functions import (
    col, 
    input_file_name, 
    regexp_extract,
    when,
    lit
)

# Get filename from input_file_name() - extract just the filename
df = df.withColumn(
    "source_filename",
    regexp_extract(input_file_name(), r"([^/]+\\\\.csv)$", 1)
)

# Extract profile reference from filename
df = df.withColumn(
    "profile_reference",
    regexp_extract(col("source_filename"), r"_([A-Z0-9]{13})_", 1)
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


def create_notebook(notebook_path: str, content: str) -> bool:
    """Create a notebook in Databricks workspace."""
    print(f"📝 Creating notebook: {notebook_path}")
    
    headers = {"Authorization": f"Bearer {TOKEN}"}
    
    # Encode content as base64
    import base64
    content_b64 = base64.b64encode(content.encode('utf-8')).decode('utf-8')
    
    url = f"{DATABRICKS_HOST}/api/2.0/workspace/import"
    payload = {
        "path": notebook_path,
        "content": content_b64,
        "format": "SOURCE",
        "language": "PYTHON",
        "overwrite": True
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        print(f"✅ Notebook created successfully!")
        return True
    except Exception as e:
        print(f"❌ Error creating notebook: {e}")
        if hasattr(e, 'response'):
            print(f"   Response: {e.response.text}")
        return False


def get_cluster_id() -> str:
    """Get the cluster ID from config."""
    from config import CLUSTER_ID
    return CLUSTER_ID


def create_and_run_job(notebook_path: str) -> str:
    """Create a Databricks job and run it."""
    print(f"\n🚀 Creating and running Databricks job...")
    
    headers = {"Authorization": f"Bearer {TOKEN}"}
    cluster_id = get_cluster_id()
    
    # Create job
    url = f"{DATABRICKS_HOST}/api/2.1/jobs/create"
    payload = {
        "name": "Create Adyen ML Test Data Table",
        "tasks": [{
            "task_key": "run_notebook",
            "notebook_task": {
                "notebook_path": notebook_path
            },
            "existing_cluster_id": cluster_id,
            "timeout_seconds": 3600
        }],
        "timeout_seconds": 3600,
        "max_concurrent_runs": 1
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        job_data = response.json()
        job_id = job_data['job_id']
        print(f"✅ Job created! Job ID: {job_id}")
        
        # Run the job
        run_url = f"{DATABRICKS_HOST}/api/2.1/jobs/run-now"
        run_payload = {"job_id": job_id}
        
        run_response = requests.post(run_url, headers=headers, json=run_payload)
        run_response.raise_for_status()
        run_data = run_response.json()
        run_id = run_data['run_id']
        
        print(f"✅ Job run started! Run ID: {run_id}")
        return run_id
        
    except Exception as e:
        print(f"❌ Error creating/running job: {e}")
        if hasattr(e, 'response'):
            print(f"   Response: {e.response.text}")
        return None


def get_run_status(run_id: str) -> dict:
    """Get the status of a job run."""
    headers = {"Authorization": f"Bearer {TOKEN}"}
    url = f"{DATABRICKS_HOST}/api/2.1/jobs/runs/get?run_id={run_id}"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"❌ Error getting run status: {e}")
        return None


def get_run_output(run_id: str) -> dict:
    """Get the output of a job run."""
    headers = {"Authorization": f"Bearer {TOKEN}"}
    url = f"{DATABRICKS_HOST}/api/2.1/jobs/runs/get-output?run_id={run_id}"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"❌ Error getting run output: {e}")
        return None


def monitor_job(run_id: str):
    """Monitor job progress and show output."""
    print(f"\n📊 Monitoring job run: {run_id}")
    print("=" * 80)
    
    states = {
        'PENDING': '⏳ Pending',
        'RUNNING': '⚡ Running',
        'TERMINATING': '🔄 Terminating',
        'TERMINATED': '✅ Terminated',
        'SKIPPED': '⏭️  Skipped',
        'INTERNAL_ERROR': '❌ Internal Error'
    }
    
    last_state = None
    max_wait = 3600  # 1 hour max
    start_time = time.time()
    
    while True:
        status = get_run_status(run_id)
        if not status:
            break
        
        state = status['state'].get('life_cycle_state', 'UNKNOWN')
        result_state = status['state'].get('result_state')
        
        # Show state change
        if state != last_state:
            print(f"\n{states.get(state, state)}: {state}")
            if result_state:
                print(f"   Result: {result_state}")
            last_state = state
        
        # If job is finished
        if state in ['TERMINATED', 'SKIPPED', 'INTERNAL_ERROR']:
            print("\n" + "=" * 80)
            
            # Get task run outputs (for jobs with tasks)
            if 'tasks' in status:
                print("\n📋 Task Outputs:")
                print("=" * 80)
                for task in status.get('tasks', []):
                    task_run_id = task.get('run_id')
                    if task_run_id:
                        print(f"\n📌 Task: {task.get('task_key', 'unknown')}")
                        task_output = get_run_output(task_run_id)
                        if task_output:
                            if 'notebook_output' in task_output and 'result' in task_output['notebook_output']:
                                result = task_output['notebook_output']['result']
                                if result.get('data'):
                                    for item in result.get('data', []):
                                        if 'text/plain' in item:
                                            print(item['text/plain'])
                                if result.get('errorSummary'):
                                    print(f"\n❌ Error: {result['errorSummary']}")
                                if result.get('cause'):
                                    print(f"   Cause: {result['cause']}")
                        print("-" * 80)
            
            # Also try to get direct output
            output = get_run_output(run_id)
            if output:
                if 'notebook_output' in output and 'result' in output['notebook_output']:
                    result = output['notebook_output']['result']
                    
                    if result.get('data'):
                        print("\n📋 Job Output:")
                        print("=" * 80)
                        
                        # Print text output
                        for item in result.get('data', []):
                            if 'text/plain' in item:
                                print(item['text/plain'])
                            elif 'text/html' in item:
                                # Skip HTML for now
                                pass
                        
                        print("=" * 80)
                    
                    # Show error if any
                    if result.get('errorSummary'):
                        print(f"\n❌ Error: {result['errorSummary']}")
                    if result.get('cause'):
                        print(f"   Cause: {result['cause']}")
                
                elif 'error' in output:
                    print(f"\n❌ Error: {output['error']}")
                elif 'error_trace' in output:
                    print(f"\n❌ Error Trace: {output['error_trace']}")
                
                # Also try to get logs
                try:
                    logs_url = f"{DATABRICKS_HOST}/api/2.0/jobs/runs/get-output?run_id={run_id}"
                    logs_response = requests.get(logs_url, headers=headers)
                    if logs_response.status_code == 200:
                        logs_data = logs_response.json()
                        if 'error' in logs_data:
                            print(f"\n❌ Job Error: {logs_data['error']}")
                        if 'error_trace' in logs_data:
                            print(f"\n❌ Error Trace: {logs_data['error_trace']}")
                except:
                    pass
            
            # Final status
            if result_state == 'SUCCESS':
                print("\n✅ Job completed successfully!")
            else:
                print(f"\n⚠️  Job finished with state: {result_state}")
            
            break
        
        # Check timeout
        if time.time() - start_time > max_wait:
            print("\n⏱️  Timeout reached. Job may still be running.")
            print(f"   Check job status in Databricks UI")
            break
        
        time.sleep(10)  # Check every 10 seconds


def main():
    """Main function."""
    notebook_path = "/Workspace/Users/visal.kumar@hellofresh.com/create_adyen_ml_test_data"
    
    print("=" * 80)
    print("Create Databricks Notebook and Run as Job")
    print("=" * 80)
    
    # Step 1: Create notebook
    if not create_notebook(notebook_path, NOTEBOOK_CONTENT):
        print("❌ Failed to create notebook")
        sys.exit(1)
    
    # Step 2: Create and run job
    run_id = create_and_run_job(notebook_path)
    if not run_id:
        print("❌ Failed to create/run job")
        sys.exit(1)
    
    # Step 3: Monitor job
    monitor_job(run_id)
    
    print("\n" + "=" * 80)
    print("✅ Process completed!")
    print(f"📊 Check your table: SELECT * FROM payments_hf.adyen_ml_test_data LIMIT 10")
    print("=" * 80)


if __name__ == "__main__":
    main()

