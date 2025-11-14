# Quick Start: Create and Run Notebooks with Terminal Output

## 🎯 The Requirement

**You want to see notebook cell output in your terminal after job execution.**

## ✅ The Solution

Notebooks must write output to DBFS files. The Databricks Jobs API doesn't capture stdout/stderr.

## 📝 Step-by-Step Guide

### Step 1: Write Your Notebook Code

Your notebook code must include writing output to DBFS:

```python
# Your notebook content
notebook_content = """# Databricks notebook source
# MAGIC %md
# MAGIC # My Analysis

# COMMAND ----------

# Run your query
query = \"\"\"SELECT * FROM schema.table LIMIT 10\"\"\"
result_df = spark.sql(query)

# IMPORTANT: Write output to DBFS
import pandas as pd
output_text = result_df.toPandas().to_string()
dbutils.fs.put("/tmp/notebook_output.txt", output_text, overwrite=True)

# Also print for UI visibility
print(output_text)
"""
```

### Step 2: Create and Run the Notebook

```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()

# Create and run
result = db.job_runner.create_and_run(
    notebook_path="/Shared/my_notebook",
    notebook_content=notebook_content,
    job_name="my_job"
)
```

### Step 3: Read Output from DBFS

The script automatically reads the output file, but here's how to do it manually:

```python
import requests
import base64
from config import DATABRICKS_HOST, TOKEN

headers = {"Authorization": f"Bearer {TOKEN}"}
read_url = f"{DATABRICKS_HOST}/api/2.0/dbfs/read"
response = requests.get(read_url, headers=headers, json={"path": "/tmp/notebook_output.txt"})

if response.status_code == 200:
    file_data = response.json()
    output = base64.b64decode(file_data['data']).decode('utf-8')
    print(output)
```

## 🎯 Complete Working Example

```python
from databricks_api import DatabricksAPI
import requests
import base64
from config import DATABRICKS_HOST, TOKEN

# Initialize
db = DatabricksAPI()

# Notebook with output to DBFS
notebook = """# Databricks notebook source
query = \"\"\"SELECT * FROM payments_hf.adyen_ml_test_cust_data WHERE customer_uuid IS NOT NULL LIMIT 10\"\"\"
result_df = spark.sql(query)

import pandas as pd
output = result_df.toPandas().to_string()
dbutils.fs.put("/tmp/output.txt", output, overwrite=True)
print(output)
"""

# Create and run
result = db.job_runner.create_and_run(
    notebook_path="/Shared/my_query",
    notebook_content=notebook,
    job_name="my_query_job"
)

# Read output
if result.get('success'):
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(
        f"{DATABRICKS_HOST}/api/2.0/dbfs/read",
        headers=headers,
        json={"path": "/tmp/output.txt"}
    )
    if response.status_code == 200:
        content = base64.b64decode(response.json()['data']).decode('utf-8')
        print("\nNOTEBOOK OUTPUT:")
        print(content)
```

## 🔑 Key Points

1. **Always use `dbutils.fs.put()`** to write output to DBFS
2. **Use unique file names** (include timestamp or UUID)
3. **Read the file after job completes**
4. **The script `create_and_run_notebook_job.py` does this automatically**

## 📚 Full Documentation

See `HOW_TO_CREATE_AND_RUN_NOTEBOOKS.md` for:
- Detailed examples
- Best practices
- Template code
- Troubleshooting


