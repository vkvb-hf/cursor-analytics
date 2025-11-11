# How to Create and Run Databricks Notebooks with Terminal Output

This guide shows you how to create Databricks notebooks and run them as jobs, **with all output visible in your terminal** - staying in Cursor without switching to the Databricks UI.

## 🎯 Key Requirement: Showing Output in Terminal

**Important**: To see notebook cell output in the terminal, you must write the output to a DBFS file in your notebook. The Databricks Jobs API does not capture stdout/stderr from print statements or DataFrame.show().

## 📝 Method 1: Using the Script (Recommended)

### Quick Start

```bash
cd /Users/visal.kumar/Documents/databricks/cursor_databricks
source ../databricks_env/bin/activate
python create_and_run_notebook_job.py
```

This script:
1. ✅ Creates a notebook with the SQL query
2. ✅ Submits it as a job
3. ✅ Monitors execution
4. ✅ **Reads output from DBFS and displays it in terminal**

### How It Works

The script automatically:
- Creates a notebook that writes output to DBFS
- Waits for job completion
- Reads the output file from DBFS
- Displays it in your terminal

## 📝 Method 2: Create Your Own Notebook

### Step 1: Write Your Notebook Code

Create a Python file with your notebook content. **Important**: Write output to DBFS so it can be retrieved.

```python
# Your notebook content
notebook_content = """# Databricks notebook source
# MAGIC %md
# MAGIC # My Analysis
# MAGIC 
# MAGIC This notebook performs data analysis.

# COMMAND ----------

# Run your SQL query
query = \"\"\"SELECT *
FROM schema.table_name
WHERE condition = 'value'
LIMIT 10\"\"\"

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
output_lines.append(f"Total records: {len(pandas_df)}")
output_lines.append("=" * 100)

# IMPORTANT: Write output to DBFS file so we can retrieve it
output_text = "\\n".join(output_lines)
output_file_path = "/tmp/notebook_output.txt"
dbutils.fs.put(output_file_path, output_text, overwrite=True)

# Also display in notebook (for UI visibility)
print(output_text)

# COMMAND ----------

# Add more cells as needed
# Each cell that produces output should write to DBFS
"""
```

### Step 2: Create and Run Using Python API

```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()

# Create and run notebook
result = db.job_runner.create_and_run(
    notebook_path="/Shared/my_analysis",
    notebook_content=notebook_content,
    job_name="my_analysis_job",
    timeout_seconds=3600,
    poll_interval=5,
    max_wait=300,
    show_output=True
)

# Read output from DBFS
if result.get('success'):
    import requests
    from config import DATABRICKS_HOST, TOKEN
    
    headers = {"Authorization": f"Bearer {TOKEN}"}
    read_url = f"{DATABRICKS_HOST}/api/2.0/dbfs/read"
    read_payload = {"path": "/tmp/notebook_output.txt"}
    read_response = requests.get(read_url, headers=headers, json=read_payload)
    
    if read_response.status_code == 200:
        file_data = read_response.json()
        if 'data' in file_data:
            import base64
            output_content = base64.b64decode(file_data['data']).decode('utf-8')
            print("\n" + "=" * 80)
            print("NOTEBOOK OUTPUT:")
            print("=" * 80)
            print(output_content)
```

### Step 3: Using the CLI Tool

```bash
# Create notebook file
cat > my_notebook.py << 'EOF'
# Databricks notebook source
# Your notebook code here
EOF

# Run using CLI
python databricks_cli.py notebook run /Shared/my_notebook \
    --file my_notebook.py \
    --job-name my_job
```

## 📋 Best Practices for Output Capture

### ✅ DO: Write Output to DBFS

```python
# Good: Write output to DBFS
output_text = result_df.toPandas().to_string()
dbutils.fs.put("/tmp/my_output.txt", output_text, overwrite=True)
print(output_text)  # Also print for UI visibility
```

### ❌ DON'T: Only Use Print Statements

```python
# Bad: This won't be captured by API
print(result_df.toPandas().to_string())
# Output only visible in UI, not in terminal
```

### ✅ DO: Use Structured Output

```python
# Good: Write structured data
import json
results = result_df.toPandas().to_dict('records')
output = {
    "total_records": len(results),
    "data": results
}
dbutils.fs.put("/tmp/output.json", json.dumps(output, indent=2), overwrite=True)
```

### ✅ DO: Handle Multiple Outputs

```python
# Good: Write multiple outputs
output_lines = []

# Output 1: Query results
output_lines.append("QUERY RESULTS:")
output_lines.append(result_df.toPandas().to_string())

# Output 2: Summary statistics
output_lines.append("\\nSUMMARY:")
output_lines.append(f"Total: {len(result_df)}")

# Write all outputs
dbutils.fs.put("/tmp/output.txt", "\\n".join(output_lines), overwrite=True)
```

## 🔧 Template for SQL Queries

Here's a template you can use for any SQL query:

```python
notebook_template = """# Databricks notebook source
# MAGIC %md
# MAGIC # {title}
# MAGIC 
# MAGIC {description}

# COMMAND ----------

# Run SQL query
query = \"\"\"{sql_query}\"\"\"

result_df = spark.sql(query)

# Format output
import pandas as pd
pandas_df = result_df.toPandas()

# Build output
output_lines = []
output_lines.append("=" * 100)
output_lines.append("QUERY RESULTS:")
output_lines.append("=" * 100)
output_lines.append(pandas_df.to_string())
output_lines.append("\\n")
output_lines.append(f"Total records: {len(pandas_df)}")
output_lines.append("=" * 100)

# Write to DBFS
output_text = "\\n".join(output_lines)
output_file = "/tmp/notebook_output.txt"
dbutils.fs.put(output_file, output_text, overwrite=True)

# Display
print(output_text)
"""
```

## 📊 Complete Example

```python
from databricks_api import DatabricksAPI
import requests
import base64
from config import DATABRICKS_HOST, TOKEN

# Initialize API
db = DatabricksAPI()

# Your notebook with output written to DBFS
notebook_content = """# Databricks notebook source
# MAGIC %md
# MAGIC # Sample Query

# COMMAND ----------

query = \"\"\"SELECT *
FROM payments_hf.adyen_ml_test_cust_data
WHERE customer_uuid IS NOT NULL
LIMIT 10\"\"\"

result_df = spark.sql(query)
import pandas as pd
pandas_df = result_df.toPandas()

# Write output to DBFS
output_text = pandas_df.to_string()
dbutils.fs.put("/tmp/notebook_output.txt", output_text, overwrite=True)
print(output_text)
"""

# Create and run notebook
result = db.job_runner.create_and_run(
    notebook_path="/Shared/my_query",
    notebook_content=notebook_content,
    job_name="my_query_job"
)

# Retrieve output from DBFS
if result.get('success'):
    headers = {"Authorization": f"Bearer {TOKEN}"}
    read_url = f"{DATABRICKS_HOST}/api/2.0/dbfs/read"
    read_response = requests.get(
        read_url, 
        headers=headers, 
        json={"path": "/tmp/notebook_output.txt"}
    )
    
    if read_response.status_code == 200:
        file_data = read_response.json()
        output_content = base64.b64decode(file_data['data']).decode('utf-8')
        print("\n" + "=" * 80)
        print("NOTEBOOK OUTPUT:")
        print("=" * 80)
        print(output_content)
```

## 🎯 Key Points to Remember

1. **Always write output to DBFS**: Use `dbutils.fs.put()` to write output files
2. **Use unique file names**: Include timestamps or UUIDs to avoid conflicts
3. **Read output after job completes**: Wait for job to finish before reading
4. **Handle errors**: Check if file exists before reading
5. **Clean up**: Optionally delete output files after reading

## 🚀 Quick Reference

```python
# Write output
dbutils.fs.put("/tmp/output.txt", my_output, overwrite=True)

# Read output (after job completes)
import requests
from config import DATABRICKS_HOST, TOKEN
headers = {"Authorization": f"Bearer {TOKEN}"}
response = requests.get(
    f"{DATABRICKS_HOST}/api/2.0/dbfs/read",
    headers=headers,
    json={"path": "/tmp/output.txt"}
)
content = base64.b64decode(response.json()['data']).decode('utf-8')
print(content)
```

## 📚 See Also

- `create_and_run_notebook_job.py` - Working example
- `databricks_api.py` - Python API for notebooks
- `databricks_cli.py` - CLI tool for notebooks


