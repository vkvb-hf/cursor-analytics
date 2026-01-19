# Quick Reference Guide

## 🚀 Common Tasks

### Run SQL Query
```bash
python scripts/run_sql.py queries/my_query.sql csv 1000
```

### Interactive SQL Shell
```bash
python scripts/interactive_sql.py
```

### Inspect Table
```bash
python scripts/inspect_table.py schema.table_name --stats --schema --sample 20
```

### Create and Run Notebook as Job
```python
from core import DatabricksJobRunner

runner = DatabricksJobRunner()
result = runner.create_and_run(
    notebook_path="/Workspace/notebooks/my_notebook",
    notebook_content="# Databricks notebook code",
    job_name="My Job"
)
```

## 📁 Directory Quick Guide

| Directory | Purpose | Example |
|-----------|---------|---------|
| `core/` | Reusable utilities | `DatabricksJobRunner`, `TableInspector` |
| `scripts/` | CLI entry points | `run_sql.py`, `interactive_sql.py` |
| `notebooks/` | Notebook utilities | `create_and_run_databricks_job.py` |
| `queries/` | SQL query files | `my_analysis.sql` |
| `exploration/` | Test/analysis scripts | `test_*.py`, `check_*.py` |
| `projects/` | Business use cases | `adyen_ml/`, `p0_metrics/` |

## 🔧 Core Utilities

### Query Execution
```python
from core.query_util import run_query, print_table
results = run_query("SELECT * FROM table LIMIT 10")
print_table(results)
```

### Table Inspection
```python
from core import TableInspector
inspector = TableInspector()
schema = inspector.get_table_schema("schema.table")
stats = inspector.get_table_stats("schema.table")
```

### Job Management
```python
from core import DatabricksJobRunner
runner = DatabricksJobRunner()
result = runner.create_and_run(...)
```

### Workspace Operations
```python
from core.databricks_workspace import create_workspace_directory, upload_csv_to_workspace
create_workspace_directory("/Workspace/my_dir")
upload_csv_to_workspace("local.csv", "/Workspace/my_dir/file.csv")
```

## 📊 Output Formats

When running SQL queries:
- `show` - Display in terminal (default)
- `csv` - Save as CSV file
- `json` - Save as JSON file

## 🎯 Use Cases

### 1. Run SQL Query via Databricks
```bash
python scripts/run_sql.py queries/my_analysis.sql csv
```

### 2. Create and Execute Databricks Notebook
```python
from core import DatabricksJobRunner
# See example above
```

### 3. Run Exploration Analysis
```python
from core import TableInspector, run_query
# Inspect and query tables
```

### 4. Build Business Products
Create in `projects/my_project/` and use `core` utilities.

## 📝 Configuration

Edit `config.py` with your Databricks credentials:
- `SERVER_HOSTNAME`
- `HTTP_PATH`
- `TOKEN`
- `DATABRICKS_HOST`

**⚠️ Never commit `config.py` with real credentials!**


