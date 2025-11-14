# Cursor Quick Reference - Databricks Toolkit

**Quick reference for daily use with Cursor + Databricks**

## 🚀 Running Notebooks with Terminal Output

### The Simple Way

```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()

notebook = """
# Your notebook code
show_output("Title", "Content")
show_query_results("Results", pandas_df)
"""

result = db.run_notebook_job(
    notebook_path="/Workspace/path/to/notebook",
    notebook_content=notebook,
    job_name="My Job"
)
# Output automatically appears in terminal! 🎉
```

### Available Helper Functions (Auto-Injected)

- **`show_output(title, content)`** - Add simple output section
- **`show_query_results(title, pandas_df, summary=None)`** - Show query results
- **`_add_output(text)`** - Add raw text (advanced)

### Example: Query with Output

```python
notebook = """
query = "SELECT * FROM table LIMIT 10"
result_df = spark.sql(query)
pandas_df = result_df.toPandas()

show_query_results(
    "Query Results",
    pandas_df,
    summary=f"Total: {len(pandas_df)} records"
)
"""
```

## 📊 Running SQL Queries

```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()
results = db.run_query("SELECT * FROM table LIMIT 10")
```

## 🔍 Inspecting Tables

```python
from core import TableInspector

inspector = TableInspector()
schema = inspector.get_table_schema("schema.table")
sample = inspector.get_table_sample("schema.table", limit=10)
```

## 📝 Common Patterns

### Pattern 1: Query → Show Results

```python
notebook = """
query = "SELECT ..."
result_df = spark.sql(query)
pandas_df = result_df.toPandas()
show_query_results("Results", pandas_df)
"""
```

### Pattern 2: Multiple Output Sections

```python
notebook = """
show_output("Step 1", "Processing...")
# ... do work ...
show_output("Step 2", "Complete!")
show_query_results("Final Results", df)
"""
```

### Pattern 3: Error Handling

```python
notebook = """
try:
    result_df = spark.sql(query)
    pandas_df = result_df.toPandas()
    show_query_results("Results", pandas_df)
except Exception as e:
    show_output("Error", f"Query failed: {str(e)}")
"""
```

## 🎯 Key Points

✅ **Auto-Injection**: Helper functions automatically available in all notebooks  
✅ **No Setup**: Everything configured automatically  
✅ **Terminal Output**: Output automatically appears in terminal  
✅ **Simple API**: Just use `show_output()` or `show_query_results()`

## 📚 Full Documentation

- **Quick Start**: `docs/guides/QUICK_START.md`
- **Auto DBFS Output**: `docs/guides/AUTO_DBFS_OUTPUT.md`
- **Cursor Mastery**: `docs/guides/CURSOR_MASTERY_GUIDE.md`
- **Main README**: `README.md`

