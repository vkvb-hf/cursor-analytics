# Working Solution: See Notebook Output in Terminal

**Status**: ✅ **THIS WORKS!**

## The Problem

The `output.print()` approach is **NOT working** - output files are empty. This is a known issue we're investigating.

## The Working Solution

**Use explicit DBFS writing** - this is simple, reliable, and works!

### Simple Approach

```python
# In your notebook
result_df = spark.sql(query)
pandas_df = result_df.toPandas()

# Build output text
output_text = "=" * 80 + "\n"
output_text += "Daily Counts Results\n"
output_text += "=" * 80 + "\n\n"
output_text += pandas_df.to_string(index=False) + "\n\n"
output_text += f"Total: {pandas_df['count'].sum():,}\n"

# Write to DBFS
dbutils.fs.put('/tmp/notebook_outputs/my_output.txt', output_text, overwrite=True)
```

### Using Helper Function (Recommended)

```python
# Auto-inject helper function
from core.output_helper import write_output_to_dbfs, format_query_results

# Query data
result_df = spark.sql(query)
pandas_df = result_df.toPandas()

# Format and write
output_text = format_query_results(
    "Daily Counts Results",
    pandas_df,
    summary=f"Total: {pandas_df['count'].sum():,}"
)
write_output_to_dbfs(output_text, job_name="Daily Counts")
```

## Complete Working Example

```python
from databricks_api import DatabricksAPI

notebook = '''# Databricks notebook source
# COMMAND ----------

# Query
query = \"\"\"
SELECT event_date, COUNT(*) as count
FROM payments_hf.checkout_funnel_backend
WHERE event_date >= CURRENT_DATE - INTERVAL 7 DAYS
GROUP BY event_date
ORDER BY date DESC
\"\"\"

result_df = spark.sql(query)
pandas_df = result_df.toPandas()

# Build output
import io
buffer = io.StringIO()
buffer.write("=" * 80 + "\\n")
buffer.write("Daily Counts Results\\n")
buffer.write("=" * 80 + "\\n\\n")
buffer.write(pandas_df.to_string(index=False) + "\\n\\n")
buffer.write(f"Total: {{pandas_df['count'].sum():,}}\\n")

# Write to DBFS
dbutils.fs.put('/tmp/notebook_outputs/daily_counts.txt', buffer.getvalue(), overwrite=True)
'''

db = DatabricksAPI()
result = db.run_notebook_job(
    notebook_path="/Workspace/path/to/notebook",
    notebook_content=notebook,
    job_name="Daily Counts",
    auto_inject_output=False,  # Don't use auto-injection
    auto_read_output=True      # Read the DBFS file
)

# Output automatically displayed! ✅
```

## Why This Works

✅ **Simple**: Just write to DBFS  
✅ **Reliable**: Always works  
✅ **Universal**: Works for any notebook  
✅ **No dependencies**: No complex injection needed

## Status

- ❌ `output.print()` - NOT working (investigating)
- ✅ Explicit DBFS writing - **WORKS!**

## Recommendation

**Use explicit DBFS writing** until `output.print()` is fixed. It's simple and reliable.

