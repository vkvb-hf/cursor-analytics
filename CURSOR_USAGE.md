# Using Databricks Tools from Cursor IDE

This guide shows you how to use the Databricks toolkit directly from Cursor IDE.

## Quick Start (Recommended)

### Option 1: Python API (Easiest for Cursor)

```python
# In any Python file in Cursor, just import:
from databricks_api import sql, inspect, notebook, DatabricksAPI

# Run SQL query
results = sql("SELECT * FROM schema.table LIMIT 10")

# Inspect a table
info = inspect("schema.table", sample=10)

# Create and run a notebook
job = notebook(
    "/Workspace/path/to/notebook",
    notebook_content="# Databricks notebook code",
    job_name="my_job"
)
```

### Option 2: Full API Class

```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()

# Run SQL (with display)
results = db.run_sql("SELECT COUNT(*) FROM schema.table")

# Run SQL (silent, just get results)
results = db.run_sql("SELECT * FROM table", display=False)

# Inspect table
info = db.inspect_table("schema.table", include_stats=True, sample_rows=20)

# Find duplicates
duplicates = db.find_duplicates("schema.table", key_column="id")

# Create notebook
db.create_notebook("/Workspace/path", content="# Notebook code")

# Run notebook as job
job = db.run_notebook_job("/Workspace/path", content="# Code", job_name="my_job")

# Check job status
status = db.get_job_status(run_id=123)
```

## Common Use Cases

### 1. Run SQL Query via Databricks

```python
from databricks_api import sql

# Simple query
results = sql("SELECT * FROM payments_hf.f_pvs_replica LIMIT 100")

# Query with results processing
results = sql("""
    SELECT 
        date_trunc('day', created_at) as day,
        COUNT(*) as count
    FROM schema.table
    WHERE created_at >= CURRENT_DATE - INTERVAL 7 DAYS
    GROUP BY day
    ORDER BY day
""")
```

### 2. Create and Execute Databricks Notebook

```python
from databricks_api import notebook

notebook_content = """
# Databricks notebook source
# MAGIC %md
# MAGIC # My Analysis
# MAGIC 
# MAGIC This notebook performs data analysis.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM schema.table LIMIT 100

# COMMAND ----------

import pandas as pd
df = spark.sql("SELECT * FROM schema.table").toPandas()
print(df.head())
"""

job = notebook(
    notebook_path="/Workspace/notebooks/my_analysis",
    notebook_content=notebook_content,
    job_name="Daily Analysis"
)

print(f"Job created: {job['job_id']}")
print(f"Run ID: {job['run_id']}")
```

### 3. Run Exploration Analysis on SQL Tables

```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()

# Inspect table structure
table_info = db.inspect_table(
    "schema.table_name",
    include_schema=True,
    include_stats=True,
    sample_rows=20
)

print("Schema:", table_info['schema'])
print("Stats:", table_info['stats'])
print("Sample:", table_info['sample'])

# Find duplicates
duplicates = db.find_duplicates("schema.table", key_column="id", limit=50)

# Run exploration queries
results = db.run_sql("""
    SELECT 
        column1,
        COUNT(*) as count,
        AVG(column2) as avg_value
    FROM schema.table
    GROUP BY column1
    ORDER BY count DESC
    LIMIT 10
""")
```

### 4. Build Business Products (Notebooks)

```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()

# Build your notebook content
notebook_content = """
# Databricks notebook source
# MAGIC %md
# MAGIC # Payment Fraud Dashboard
# MAGIC 
# MAGIC This notebook generates the payment fraud dashboard.

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Your SQL queries here
# MAGIC SELECT * FROM schema.payment_fraud_dashboard
"""

# Create and run as scheduled job
job = db.run_notebook_job(
    notebook_path="/Workspace/projects/fraud_dashboard",
    notebook_content=notebook_content,
    job_name="Fraud Dashboard Daily"
)

# Check job status later
status = db.get_job_status(job['run_id'])
print(f"Job status: {status['state']['life_cycle_state']}")
```

## Integration with Your Workflow

### In Cursor Chat

You can ask Cursor to:
- "Run this SQL query on Databricks: SELECT * FROM table"
- "Inspect the schema.table table"
- "Create a notebook that does X and run it as a job"

Cursor can use the API directly:
```python
from databricks_api import sql
results = sql("YOUR_QUERY_HERE")
```

### In Your Python Scripts

Just import and use:
```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()
# Use db for all your operations
```

### Running SQL Files

```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()
db.run_sql_file("queries/my_analysis.sql", output_format="csv", limit=1000)
```

## CLI Alternative

If you prefer command line (from Cursor's terminal):

```bash
# Run SQL
python databricks_cli.py sql --query "SELECT * FROM table LIMIT 10"

# Run SQL file
python databricks_cli.py sql --file queries/my_query.sql --format csv

# Inspect table
python databricks_cli.py table inspect schema.table --stats --sample 20

# Create notebook
python databricks_cli.py notebook create /Workspace/path --file my_notebook.py

# Run notebook as job
python databricks_cli.py notebook run /Workspace/path --file my_notebook.py --job-name my_job

# Interactive SQL shell
python databricks_cli.py interactive
```

## Tips for Cursor Usage

1. **Keep it simple**: Use the convenience functions (`sql`, `inspect`, `notebook`)
2. **For complex workflows**: Use the `DatabricksAPI` class
3. **Error handling**: All functions return `None` on error, so check results
4. **Configuration**: Make sure `config.py` is set up with your credentials

## Example: Complete Workflow

```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()

# 1. Inspect a table
info = db.inspect_table("schema.table", sample_rows=10)
print("Table has", info['stats']['row_count'], "rows")

# 2. Run analysis query
results = db.run_sql("""
    SELECT 
        date_trunc('day', created_at) as day,
        COUNT(*) as transactions,
        SUM(amount) as total_amount
    FROM schema.table
    WHERE created_at >= CURRENT_DATE - INTERVAL 30 DAYS
    GROUP BY day
    ORDER BY day
""")

# 3. Create notebook with results
notebook_content = f"""
# Databricks notebook source
# MAGIC %md
# MAGIC # Analysis Results
# MAGIC 
# MAGIC Found {len(results)} rows of data.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM schema.table LIMIT 100
"""

# 4. Run as job
job = db.run_notebook_job(
    "/Workspace/analysis/daily_report",
    notebook_content,
    "Daily Analysis Report"
)

print(f"Job started: {job['run_id']}")
```

## Benefits of This Approach

✅ **Simple**: One import, all functionality  
✅ **Flexible**: Use what you need, when you need it  
✅ **Tested**: All utilities have unit tests  
✅ **Maintainable**: Modular structure, easy to extend  
✅ **Cursor-friendly**: Works seamlessly in Cursor IDE  

No need to remember multiple scripts or complex commands - just use the API!

