#!/usr/bin/env python3
"""
Create payments_hf.ascs_customer_attributes table using Databricks notebook job
This approach is better for complex queries that may take a long time
"""
import sys
import os

# Add cursor_databricks to path
cursor_databricks_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, cursor_databricks_root)

from databricks_api import DatabricksAPI

def main():
    # Read SQL file
    sql_file_path = "/Users/visal.kumar/Documents/GitHub/ddi-pays-pipelines/ddi_pays_pipelines/analytics_etl/queries/ascs_customer_attributes.sql"
    
    with open(sql_file_path, 'r') as f:
        sql_query = f.read()
    
    # Create notebook content with better error handling
    notebook_content = f"""# Databricks notebook source
# MAGIC %md
# MAGIC # Create ASCS Customer Attributes Table
# MAGIC 
# MAGIC This notebook creates the `payments_hf.ascs_customer_attributes` table
# MAGIC Date Filter: 2025-11-01

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS payments_hf.ascs_customer_attributes;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Create the table
# MAGIC CREATE OR REPLACE TABLE payments_hf.ascs_customer_attributes AS
# MAGIC {sql_query}

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Verify table creation and get row count
# MAGIC SELECT COUNT(*) as row_count FROM payments_hf.ascs_customer_attributes;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Show sample data
# MAGIC SELECT * FROM payments_hf.ascs_customer_attributes LIMIT 10;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Table Creation Complete
# MAGIC 
# MAGIC Table `payments_hf.ascs_customer_attributes` has been created successfully.
"""
    
    print("=" * 80)
    print("Creating ASCS Customer Attributes Table via Notebook Job")
    print("=" * 80)
    print(f"SQL File: {sql_file_path}")
    print(f"Table: payments_hf.ascs_customer_attributes")
    print(f"Date Filter: 2025-11-01")
    print("=" * 80)
    print()
    
    # Initialize API
    db = DatabricksAPI()
    
    # Run as notebook job
    notebook_path = "/Workspace/Users/visal.kumar@hellofresh.com/create_ascs_customer_attributes"
    job_name = "Create ASCS Customer Attributes Table"
    
    print(f"Creating and running notebook job: {job_name}")
    print(f"Notebook path: {notebook_path}")
    print("This may take several minutes...")
    print()
    
    result = db.run_notebook_job(
        notebook_path=notebook_path,
        notebook_content=notebook_content,
        job_name=job_name,
        auto_inject_output=True,
        auto_read_output=True
    )
    
    if result:
        print("\n" + "=" * 80)
        print("✓ SUCCESS: Table creation job completed!")
        print("=" * 80)
        if 'run_id' in result:
            print(f"Job Run ID: {result['run_id']}")
        return 0
    else:
        print("\n" + "=" * 80)
        print("✗ FAILED: Table creation job failed")
        print("=" * 80)
        return 1

if __name__ == "__main__":
    sys.exit(main())

