# Troubleshooting NotebookOutput Framework

## Issue: "output variable not available"

### Symptoms
- Notebook runs successfully
- Regular `print()` statements work
- But `output.print()` fails with `NameError: name 'output' is not defined`

### Possible Causes

1. **Auto-injection failed silently**
   - The injection might have failed but the error wasn't shown
   - Check if you see "✅ NotebookOutput framework initialized" in the output

2. **Cell execution order issue**
   - The cell with `output` initialization might not have executed
   - Check the job logs for any errors in the first cell

3. **Scope issue in Databricks**
   - Variables should persist across cells, but sometimes they don't
   - This is rare but can happen

### Solutions

#### Solution 1: Check if auto-injection is enabled

```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()

result = db.run_notebook_job(
    notebook_path="/Workspace/path/to/notebook",
    notebook_content=notebook,
    job_name="My Job",
    auto_inject_output=True  # Make sure this is True
)
```

#### Solution 2: Manually add NotebookOutput to your notebook

If auto-injection isn't working, add it manually:

```python
# Databricks notebook source
# MAGIC %md
# MAGIC # My Notebook

# COMMAND ----------

# Add NotebookOutput manually
class NotebookOutput:
    # ... (copy from examples/notebook_with_output_template.py)
    pass

output = NotebookOutput(output_path="/tmp/notebook_outputs/my_output.txt")

# COMMAND ----------

# Your code here
output.print("This will work now!")
```

#### Solution 3: Use regular print() statements

Regular `print()` statements are automatically captured even without `output.print()`:

```python
# This works automatically (captured by the framework)
print("Hello World")
print("This is captured automatically")
```

#### Solution 4: Check the actual notebook in Databricks

1. Go to Databricks workspace
2. Open the notebook that was created
3. Check if the NotebookOutput class and `output = NotebookOutput(...)` are present
4. Run the first cell manually to see if there are any errors

### Debugging Steps

1. **Check injection status**:
   ```python
   # In your notebook, add this at the beginning
   try:
       print(f"output variable available: {'output' in globals()}")
       print(f"output type: {type(output)}")
   except:
       print("output variable NOT available")
   ```

2. **Check job logs**:
   - Look for "✅ NotebookOutput framework initialized" message
   - Look for any error messages about NotebookOutput

3. **Test with minimal notebook**:
   ```python
   notebook = """
   # Databricks notebook source
   # COMMAND ----------
   print("Test")
   try:
       output.print("Test")
   except NameError:
       print("output not available")
   """
   ```

### If Nothing Works

Use the manual approach - add NotebookOutput directly to your notebook code instead of relying on auto-injection.

