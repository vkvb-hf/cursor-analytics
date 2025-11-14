# Auto-Inject NotebookOutput Framework

**Feature**: Automatically enable NotebookOutput framework in all Databricks notebooks executed as jobs.

## 🎯 Overview

By default, **all notebooks executed as jobs automatically have the NotebookOutput framework injected**. This means:

- ✅ No manual setup required
- ✅ All print statements automatically captured
- ✅ Output automatically retrieved and displayed
- ✅ Works with any notebook code

## 🚀 How It Works

### Automatic Injection (Default)

When you run a notebook as a job, the framework is automatically injected:

```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()

# Your notebook code (no NotebookOutput setup needed!)
notebook = """
# Databricks notebook source
# MAGIC %md
# MAGIC # My Analysis

# COMMAND ----------

# Just use regular print statements - they're automatically captured!
print("Starting analysis...")
print("Processing data...")

# Your code here
result = spark.sql("SELECT * FROM table LIMIT 10")
print(result.toPandas().to_string())
"""

# Run with auto-injection (default)
result = db.run_notebook_job(
    notebook_path="/Workspace/path/to/notebook",
    notebook_content=notebook,
    job_name="My Analysis"
)

# Output automatically displayed! 🎉
```

### What Gets Injected

The framework automatically adds:

1. **NotebookOutput class** - Full implementation
2. **output variable** - Pre-initialized and ready to use
3. **Auto-write** - Automatically calls `output.write_to_dbfs()` at the end

### Using output.print()

You can also use `output.print()` for better control:

```python
# Your notebook
notebook = """
# output variable is automatically available!

output.print("Starting analysis...")
output.print("Processing data...")

# Regular print() also works (automatically captured)
print("This is also captured!")

# output.write_to_dbfs() is automatically called at the end
"""
```

## ⚙️ Configuration

### Enable/Disable Auto-Injection

```python
# Enable (default)
result = db.run_notebook_job(
    notebook_path="/Workspace/path/to/notebook",
    notebook_content=notebook,
    job_name="My Analysis",
    auto_inject_output=True  # Default
)

# Disable
result = db.run_notebook_job(
    notebook_path="/Workspace/path/to/notebook",
    notebook_content=notebook,
    job_name="My Analysis",
    auto_inject_output=False  # Disable auto-injection
)
```

### Using Job Runner Directly

```python
from core.databricks_job_runner import DatabricksJobRunner

runner = DatabricksJobRunner()

result = runner.create_and_run(
    notebook_path="/Workspace/path/to/notebook",
    notebook_content=notebook,
    job_name="My Analysis",
    auto_inject_output=True  # Enable auto-injection
)
```

## 📋 Examples

### Example 1: Simple Notebook (Auto-Injection)

```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()

notebook = """
# Databricks notebook source
# MAGIC %md
# MAGIC # Simple Analysis

# COMMAND ----------

print("Hello from Databricks!")
print("This output will be automatically captured!")

query = "SELECT 1 as test"
result = spark.sql(query)
print(result.toPandas().to_string())
"""

result = db.run_notebook_job(
    notebook_path="/Workspace/Users/user@example.com/simple_test",
    notebook_content=notebook,
    job_name="Simple Test"
)

# Output automatically displayed!
```

### Example 2: Using output.print()

```python
notebook = """
# Databricks notebook source
# output variable is automatically available!

output.print("=" * 80)
output.print("Starting Analysis")
output.print("=" * 80)

query = "SELECT * FROM table LIMIT 10"
result = spark.sql(query)
pandas_df = result.toPandas()

output.print("\\nQuery Results:")
output.print(pandas_df.to_string())

# output.write_to_dbfs() is automatically called at the end
"""

result = db.run_notebook_job(
    notebook_path="/Workspace/path/to/notebook",
    notebook_content=notebook,
    job_name="Analysis with Output"
)
```

### Example 3: Manual Control (Disable Auto-Injection)

```python
# If you want to manually control NotebookOutput
notebook = """
# Databricks notebook source
# Your custom NotebookOutput setup
class MyCustomOutput:
    # ... your custom implementation
    pass

output = MyCustomOutput()
# ... your code
"""

result = db.run_notebook_job(
    notebook_path="/Workspace/path/to/notebook",
    notebook_content=notebook,
    job_name="Custom Output",
    auto_inject_output=False  # Disable auto-injection
)
```

## 🔍 How It Works Internally

1. **Detection**: Checks if NotebookOutput is already present
2. **Injection**: If not present, injects the framework at the beginning
3. **Initialization**: Creates `output` variable automatically
4. **Auto-Write**: Adds `output.write_to_dbfs()` at the end
5. **Execution**: Notebook runs with output framework enabled
6. **Retrieval**: Output automatically read and displayed after job completes

## ✅ Benefits

### No Manual Setup
- ✅ No need to add NotebookOutput class to every notebook
- ✅ No need to initialize output variable
- ✅ No need to call write_to_dbfs()

### Automatic Capture
- ✅ All print statements automatically captured
- ✅ Works with existing code (no changes needed)
- ✅ Can also use output.print() for better control

### Consistent Behavior
- ✅ Same output format for all notebooks
- ✅ Same file structure in DBFS
- ✅ Same retrieval mechanism

## 🎯 Best Practices

### Use Regular print() Statements
```python
# Good: Regular print statements work automatically
print("Starting analysis...")
print("Processing data...")
```

### Use output.print() for Better Control
```python
# Better: More control with output.print()
output.print("=" * 80)
output.print("Analysis Results")
output.print("=" * 80)
```

### Use output.add_section() for Structured Output
```python
# Best: Structured output with sections
output.add_section("Summary", "Total records: 1000")
output.add_dataframe("Results", result_df)
```

## ⚠️ Notes

### Already Has NotebookOutput?
If your notebook already has NotebookOutput, auto-injection will:
- ✅ Detect it and skip injection
- ✅ Still add auto-write if not present
- ✅ Work seamlessly with your existing code

### Custom Output Path
You can specify a custom output path:

```python
result = db.job_runner.create_and_run(
    notebook_path="/Workspace/path/to/notebook",
    notebook_content=notebook,
    job_name="My Analysis",
    output_path="/tmp/custom_output.txt"  # Custom path
)
```

## 📚 See Also

- [Notebook Output Framework Guide](NOTEBOOK_OUTPUT_FRAMEWORK.md) - Complete framework documentation
- [Integration Framework](INTEGRATION_FRAMEWORK.md) - Other integration features
- `core/notebook_output_injector.py` - Implementation details

---

## 🎉 Summary

**Auto-injection is enabled by default!** Just write your notebook code normally, and all output will be automatically captured and displayed.

```python
# That's it! No setup needed!
result = db.run_notebook_job(
    notebook_path="/Workspace/path/to/notebook",
    notebook_content=your_notebook_code,
    job_name="My Analysis"
)
# Output automatically displayed! 🎉
```

