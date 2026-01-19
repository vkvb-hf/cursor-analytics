# Notebook Output Framework: Complete Guide

**Problem**: Print statements in Databricks notebooks don't show up in job output when retrieved via API.

**Solution**: Write all output to DBFS files in a structured format, then automatically retrieve and display after job completion.

---

## 🎯 Quick Start

### Step 1: Use the Output Framework in Your Notebook

```python
# In your Databricks notebook

# Define NotebookOutput class (or import if available)
class NotebookOutput:
    def __init__(self, output_path="/tmp/notebook_outputs/my_output.txt"):
        self.output_path = output_path
        self.sections = []
        self.errors = []
    
    def print(self, *args, sep=" ", end="\n"):
        message = sep.join(str(arg) for arg in args) + end
        print(message, end="")  # Print to console
        self.add_section("Print Output", message.strip())  # Capture for file
    
    def add_section(self, title, content):
        self.sections.append({'title': title, 'content': content})
    
    def write_to_dbfs(self):
        # Build formatted output
        output_lines = []
        output_lines.append("=" * 100)
        output_lines.append("NOTEBOOK OUTPUT")
        output_lines.append("=" * 100)
        # ... (see template for full implementation)
        
        # Write to DBFS
        dbutils.fs.put(self.output_path, output_text, overwrite=True)

# Initialize
output = NotebookOutput(output_path="/tmp/notebook_outputs/my_job_output.txt")

# Use output.print() instead of print()
output.print("Hello World")
output.print("Starting analysis...")

# At the end, write to DBFS
output.write_to_dbfs()
```

### Step 2: Run Notebook with Auto-Output Retrieval

```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()

result = db.job_runner.create_and_run(
    notebook_path="/Workspace/Users/user@example.com/my_notebook",
    notebook_content=notebook_content,
    job_name="My Analysis Job",
    auto_read_output=True  # Automatically read output after job completes
)

# Output is automatically displayed in terminal!
```

---

## 📁 DBFS File Structure

### Standard Structure

```
/tmp/notebook_outputs/
├── my_job_20240101_120000.txt
├── my_job_20240101_130000.txt
├── analysis_20240101_140000.txt
└── ...
```

### File Naming Convention

- Format: `{job_name}_{timestamp}.txt`
- Job name is sanitized (spaces → underscores, slashes → underscores)
- Timestamp format: `YYYYMMDD_HHMMSS`
- All files stored in `/tmp/notebook_outputs/`

### Benefits

- ✅ Organized by job name
- ✅ Timestamped for versioning
- ✅ Easy to find latest output
- ✅ Can list all outputs for a job

---

## 🔧 Usage Patterns

### Pattern 1: Simple Print Statements

```python
output = NotebookOutput()

output.print("Starting analysis...")
output.print("Processing data...")
output.print("Analysis complete!")

output.write_to_dbfs()
```

### Pattern 2: Query Results

```python
output = NotebookOutput()

query = "SELECT * FROM table LIMIT 10"
result_df = spark.sql(query)
pandas_df = result_df.toPandas()

output.print("Query Results:")
output.print(pandas_df.to_string())

# Also add as structured section
output.add_section("Query Results", pandas_df.to_string())

output.write_to_dbfs()
```

### Pattern 3: Multiple Sections

```python
output = NotebookOutput()

# Section 1: Summary
output.add_section("Summary", "Total records: 1000")

# Section 2: Query Results
output.add_section("Query Results", result_df.to_string())

# Section 3: Statistics
output.add_section("Statistics", stats_df.to_string())

output.write_to_dbfs()
```

### Pattern 4: Error Handling

```python
output = NotebookOutput()

try:
    result = spark.sql(query)
    output.add_section("Results", result.toPandas().to_string())
except Exception as e:
    output.errors.append(f"Query failed: {str(e)}")
    output.print(f"❌ Error: {str(e)}")

output.write_to_dbfs()
```

---

## 🚀 Integration with Job Runner

### Automatic Output Retrieval

The enhanced `DatabricksJobRunner.create_and_run()` method automatically:

1. ✅ Creates notebook
2. ✅ Runs job
3. ✅ Monitors execution
4. ✅ **Automatically reads output from DBFS**
5. ✅ **Displays output in terminal**

```python
result = db.job_runner.create_and_run(
    notebook_path="/Workspace/path/to/notebook",
    notebook_content=notebook_content,
    job_name="My Job",
    auto_read_output=True  # Enable automatic output retrieval
)
```

### Manual Output Reading

If you need to read output manually:

```python
from core.notebook_output_reader import NotebookOutputReader

reader = NotebookOutputReader()

# Read specific file
reader.display_output("/tmp/notebook_outputs/my_job_20240101_120000.txt")

# Get latest output for a job
latest = reader.get_latest_output(job_name="My Job")
if latest:
    reader.display_output(latest)
```

---

## 📋 Complete Example

### Notebook Content

```python
# Databricks notebook source

# Define NotebookOutput (or import)
class NotebookOutput:
    # ... (see template for full implementation)
    pass

# Initialize
output = NotebookOutput(output_path="/tmp/notebook_outputs/my_analysis.txt")

# Your analysis code
output.print("Starting analysis...")

query = "SELECT * FROM payments_hf.duplicate_customers LIMIT 10"
result_df = spark.sql(query)
pandas_df = result_df.toPandas()

output.print("\\nQuery Results:")
output.print(pandas_df.to_string())

output.add_section("Query Results", pandas_df.to_string())

# Write output
output.write_to_dbfs()
```

### Run from Python

```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()

result = db.job_runner.create_and_run(
    notebook_path="/Workspace/Users/user@example.com/my_analysis",
    notebook_content=notebook_content,
    job_name="My Analysis",
    auto_read_output=True
)

# Output automatically displayed!
```

---

## 🎨 Output Format

### Standard Format

```
====================================================================================================
NOTEBOOK OUTPUT
====================================================================================================
Generated: 2024-01-01 12:00:00

----------------------------------------------------------------------------------------------------
📊 [1] Print Output
----------------------------------------------------------------------------------------------------
Starting analysis...

----------------------------------------------------------------------------------------------------
📊 [2] Print Output
----------------------------------------------------------------------------------------------------
Query Results:

----------------------------------------------------------------------------------------------------
📊 [3] Query Results
----------------------------------------------------------------------------------------------------
Query:
SELECT * FROM table LIMIT 10

Results:
   column1  column2
0       1       A
1       2       B

====================================================================================================
```

---

## ✅ Best Practices

### 1. Always Use Structured Paths

```python
# Good: Organized by job name
output = NotebookOutput(output_path="/tmp/notebook_outputs/my_job_output.txt")

# Better: Auto-generated with job name
output = NotebookOutput(job_name="My Job")  # Auto-generates path
```

### 2. Write Output at the End

```python
# Always call write_to_dbfs() at the end
output.write_to_dbfs()
```

### 3. Use output.print() Instead of print()

```python
# Good
output.print("Message")

# Bad (won't be captured)
print("Message")
```

### 4. Handle Errors

```python
try:
    result = spark.sql(query)
    output.add_section("Results", result.toPandas().to_string())
except Exception as e:
    output.errors.append(f"Error: {str(e)}")
    output.print(f"❌ {str(e)}")
```

### 5. Use Sections for Organization

```python
output.add_section("Summary", summary_text)
output.add_section("Query Results", results_text)
output.add_section("Statistics", stats_text)
```

---

## 🔍 Troubleshooting

### Output Not Showing

1. **Check if output file was created**:
   ```python
   # In Databricks notebook
   dbutils.fs.ls("/tmp/notebook_outputs/")
   ```

2. **Verify write_to_dbfs() was called**:
   - Make sure `output.write_to_dbfs()` is called at the end

3. **Check file path**:
   - Ensure directory exists: `dbutils.fs.mkdirs("/tmp/notebook_outputs/")`

### Output File Not Found

1. **Check job name matching**:
   - Job name must match (sanitized) for auto-detection

2. **Use specific path**:
   ```python
   result = db.job_runner.create_and_run(
       ...,
       output_path="/tmp/notebook_outputs/specific_file.txt"
   )
   ```

### Output Format Issues

1. **Check encoding**: All output is UTF-8
2. **Check line endings**: Use `\n` for newlines
3. **Check special characters**: May need escaping

---

## 📚 See Also

- `examples/run_notebook_with_output.py` - Complete working example
- `examples/notebook_with_output_template.py` - Template notebook
- `core/notebook_output.py` - Output framework implementation
- `core/notebook_output_reader.py` - Output reader implementation

---

## 🎯 Summary

**The Framework**:
1. ✅ Use `NotebookOutput` class in your notebook
2. ✅ Use `output.print()` instead of `print()`
3. ✅ Call `output.write_to_dbfs()` at the end
4. ✅ Run with `auto_read_output=True`
5. ✅ Output automatically displayed in terminal!

**Benefits**:
- ✅ All print statements captured
- ✅ Structured, readable output
- ✅ Automatic retrieval
- ✅ Organized file storage
- ✅ Easy to use

