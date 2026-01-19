# AI Utility Selection Guide

This document helps AI models and developers select the appropriate utility function for specific Databricks-related tasks.

## Decision Tree

```
Start: What do you need to do?
│
├─ File Operations?
│  ├─ Upload files to workspace?
│  │  └─ Use: databricks_workspace.upload_csv_to_workspace()
│  │
│  ├─ Extract files from archives?
│  │  └─ Use: unzip_csvs.unzip_files_and_add_source_name()
│  │
│  └─ List/manage workspace files?
│     └─ Use: Databricks Workspace API directly
│
├─ Job Execution?
│  ├─ Run notebook as job?
│  │  └─ Use: DatabricksJobRunner.create_and_run()
│  │
│  ├─ Check job status?
│  │  └─ Use: DatabricksJobRunner.monitor_job()
│  │
│  └─ Get job output?
│     └─ Use: DatabricksJobRunner.get_task_output()
│
├─ Table Operations?
│  ├─ Inspect table structure/stats?
│  │  └─ Use: TableInspector.get_table_stats()
│  │
│  ├─ Check for duplicates?
│  │  └─ Use: TableInspector.check_duplicates_by_column()
│  │
│  ├─ Find data conflicts?
│  │  └─ Use: TableInspector.check_cross_column_conflicts()
│  │
│  ├─ Convert CSV to table?
│  │  └─ Use: csv_to_table.create_table_from_csvs()
│  │
│  └─ Compare CSV with table?
│     └─ Use: TableInspector.compare_csv_to_table()
│
└─ SQL Execution?
   ├─ Run single query?
   │  └─ Use: query_util.execute_query()
   │
   ├─ Run SQL file?
   │  └─ Use: run_sql_file.run_sql_file()
   │
   └─ Interactive SQL?
      └─ Use: interactive_sql.interactive_session()
```

## Utility Reference

### 1. File Operations

#### Upload CSV to Workspace
**Utility**: `databricks_workspace.upload_csv_to_workspace()`

**When to Use**:
- Uploading CSV files to Databricks workspace
- Files need to be visible in workspace browser
- Files are < 100MB (for API limits)

**Example**:
```python
from utils.databricks_workspace import upload_csv_to_workspace

result = upload_csv_to_workspace(
    csv_file_path="local/file.csv",
    csv_filename="file.csv",
    databricks_path="/Workspace/path/to/folder",
    workspace_host="https://your-workspace.cloud.databricks.com",
    token="your-token"
)
```

**Alternatives**:
- For large files: Use DBFS API with chunked upload
- For binary files: Use workspace/import with BINARY format

#### Extract Files from Archives
**Utility**: `unzip_csvs.unzip_files_and_add_source_name()`

**When to Use**:
- Extracting CSV files from ZIP archives
- Adding source filename prefix to extracted files
- Preparing files for upload

**Example**:
```python
from unzip_csvs import unzip_files_and_add_source_name

results = unzip_files_and_add_source_name(
    source_dir="~/Downloads/zips",
    output_dir="~/Downloads/extracted"
)
```

### 2. Job Execution

#### Run Notebook as Job
**Utility**: `DatabricksJobRunner.create_and_run()`

**When to Use**:
- Running notebooks programmatically
- Scheduling notebook execution
- Need to track job status and output

**Example**:
```python
from utils import DatabricksJobRunner

runner = DatabricksJobRunner()
result = runner.create_and_run(
    notebook_path="/Workspace/path/to/notebook",
    notebook_content="# Databricks notebook source\nprint('Hello')",
    job_name="My Analysis Job",
    timeout_seconds=3600
)
```

**Key Features**:
- Creates notebook in workspace
- Submits as job
- Monitors execution
- Retrieves output

**When NOT to Use**:
- Quick interactive queries (use SQL connector directly)
- One-time manual execution (use Databricks UI)

#### Monitor Job Status
**Utility**: `DatabricksJobRunner.monitor_job()`

**When to Use**:
- Checking status of running jobs
- Getting job output after completion
- Polling for job completion

### 3. Table Operations

#### Inspect Table
**Utility**: `TableInspector.get_table_stats()`

**When to Use**:
- Getting basic table information
- Checking row counts
- Viewing column list

**Example**:
```python
from utils.table_inspector import TableInspector

inspector = TableInspector()
stats = inspector.get_table_stats("my_schema.my_table")
print(f"Rows: {stats['total_rows']:,}")
```

#### Check for Duplicates
**Utility**: `TableInspector.check_duplicates_by_column()`

**When to Use**:
- Finding duplicate values in a column
- Data quality checks
- Validation after data load

**Example**:
```python
duplicates = inspector.check_duplicates_by_column(
    "my_schema.my_table",
    "PSP_Reference",
    limit=20
)
```

#### Find Data Conflicts
**Utility**: `TableInspector.check_cross_column_conflicts()`

**When to Use**:
- Checking if same identifier has conflicting attributes
- Validating data consistency
- Finding data quality issues

**Example**:
```python
conflicts = inspector.check_cross_column_conflicts(
    "my_schema.my_table",
    identifier_column="PSP_Reference",
    check_columns=["Status", "risk_profile"],
    limit=20
)
```

#### Convert CSV to Table
**Utility**: `csv_to_table.create_table_from_csvs()`

**When to Use**:
- Bulk loading CSV data into Delta tables
- Creating tables from multiple CSV files
- Schema inference needed

**Example**:
```python
from utils.csv_to_table import create_table_from_csvs

success = create_table_from_csvs(
    workspace_path="/Workspace/path/to/csvs",
    table_name="my_schema.my_table",
    custom_columns={'source_file': lambda f: f},
    drop_if_exists=True
)
```

**When NOT to Use**:
- Very large datasets (use Spark directly)
- Real-time streaming (use Spark Streaming)
- Simple queries (use SQL connector)

#### Compare CSV with Table
**Utility**: `TableInspector.compare_csv_to_table()`

**When to Use**:
- Validating data completeness
- Verifying uploads
- Data reconciliation

### 4. SQL Execution

#### Execute Query
**Utility**: `query_util.execute_query()`

**When to Use**:
- Running single SQL queries
- Quick data retrieval
- Simple operations

**Example**:
```python
from utils.query_util import execute_query

results = execute_query("SELECT COUNT(*) FROM my_table")
```

#### Run SQL File
**Utility**: `run_sql_file.run_sql_file()`

**When to Use**:
- Executing pre-written SQL files
- Batch SQL operations
- Reusable SQL scripts

## Common Use Case Patterns

### Pattern 1: Upload and Process CSV Files
```python
# 1. Extract files
from unzip_csvs import unzip_files_and_add_source_name
results = unzip_files_and_add_source_name("source/", "output/")

# 2. Upload to workspace
from utils.databricks_workspace import upload_csv_to_workspace
for file in results['files']:
    upload_csv_to_workspace(...)

# 3. Create table
from utils.csv_to_table import create_table_from_csvs
create_table_from_csvs(...)

# 4. Validate
from utils.table_inspector import TableInspector
inspector = TableInspector()
stats = inspector.get_table_stats("my_table")
```

### Pattern 2: Run Analysis as Job
```python
# 1. Create notebook content
notebook_content = """
# Databricks notebook source
# MAGIC %md
# MAGIC # My Analysis

# COMMAND ----------
df = spark.sql("SELECT * FROM my_table")
df.show()
"""

# 2. Run as job
from utils import DatabricksJobRunner
runner = DatabricksJobRunner()
result = runner.create_and_run(
    notebook_path="/Workspace/my_analysis",
    notebook_content=notebook_content,
    job_name="My Analysis"
)
```

### Pattern 3: Data Quality Validation
```python
from utils.table_inspector import TableInspector

inspector = TableInspector()

# Check duplicates
dups = inspector.check_duplicates_by_column("my_table", "id")

# Check conflicts
conflicts = inspector.check_cross_column_conflicts(
    "my_table",
    identifier_column="transaction_id",
    check_columns=["status", "amount"]
)

# Compare with source
comparison = inspector.compare_csv_to_table(
    "my_table",
    csv_row_counts=[{"filename": "file.csv", "rows": 1000}]
)
```

## Selection Criteria

### Choose Generic Utilities When:
- ✅ Task is reusable across projects
- ✅ No project-specific business logic
- ✅ Well-defined, standard operation
- ✅ Need to maintain consistency

### Keep Project-Specific When:
- ✅ Contains business-specific logic
- ✅ One-time or experimental
- ✅ Tightly coupled to specific data model
- ✅ Not reusable

## Anti-Patterns to Avoid

❌ **Don't**: Copy-paste utility code into project files
✅ **Do**: Import and use utilities from `utils/`

❌ **Don't**: Mix generic and project-specific code
✅ **Do**: Keep them separated

❌ **Don't**: Create utilities for one-time use
✅ **Do**: Keep one-time scripts in projects or tests

## Error Handling

All utilities should:
- Return structured results (dict with 'success', 'error' keys)
- Raise exceptions for fatal errors
- Log warnings for recoverable issues
- Provide clear error messages

## Performance Considerations

- **Large files**: Use Spark/DBFS APIs directly, not workspace API
- **Many files**: Batch operations, use parallel processing
- **Large tables**: Use Spark, not SQL connector
- **Frequent queries**: Cache results, use connection pooling

## Questions to Ask

1. **Is this reusable?** → Generic utility
2. **Is this project-specific?** → Project folder
3. **Is this a test/debug?** → Tests folder
4. **Is this documentation?** → Docs folder

---

## 📁 File Organization Rules for AI

**CRITICAL**: When creating or saving files, you MUST follow these rules. Use the validation script to check your work.

### Root Directory Rules

**✅ ALLOWED in Root** (Only these 7 files):
- `config.py` - Configuration (DO NOT COMMIT)
- `config.py.example` - Template
- `README.md` - Main documentation
- `databricks_api.py` - Main Python API entry point
- `databricks_cli.py` - Main CLI entry point
- `requirements.txt` - Dependencies
- `requirements-test.txt` - Test dependencies

**❌ NEVER create in Root**:
- Test files (`.py` files starting with `test_`)
- Documentation files (`.md` files except `README.md`)
- Example files (`.py` files starting with `example_`)
- Data files (`.csv`, `.json`, etc.)
- One-time scripts
- Investigation/analysis scripts

### Directory-Specific Rules

#### `core/` - Core Reusable Utilities
**✅ PUT HERE**:
- Reusable utilities that work across all projects
- Generic, project-agnostic functions
- Well-tested, documented code

**❌ DON'T PUT HERE**:
- Project-specific code
- One-time scripts
- Test files
- Business logic

**Example**: `core/query_util.py`, `core/table_inspector.py`

#### `scripts/` - CLI Entry Points
**✅ PUT HERE**:
- Command-line scripts
- Executable utilities
- Scripts that use `argparse`

**❌ DON'T PUT HERE**:
- One-time task scripts
- Investigation scripts
- Test scripts

**Example**: `scripts/run_sql.py`, `scripts/interactive_sql.py`

#### `notebooks/` - Reusable Notebook Utilities
**✅ PUT HERE**:
- Reusable notebook utilities (ONLY)
- Functions for creating/managing notebooks
- Generic notebook helpers

**❌ DON'T PUT HERE**:
- One-time notebook tasks
- Analysis notebooks
- Test notebooks
- Task-specific notebooks

**Example**: `notebooks/create_and_run_databricks_job.py`

#### `tests/` - Test Files
**✅ PUT HERE**:
- All test files (`test_*.py`)
- Test fixtures
- Test utilities

**❌ DON'T PUT HERE**:
- Production code
- Scripts
- Documentation

#### `examples/` - Example Scripts
**✅ PUT HERE**:
- Example scripts
- Templates
- Sample code

**Example**: `examples/example_notebook_with_output.py`

#### `data/` - Data Files
**✅ PUT HERE**:
- CSV files
- JSON exports
- Data dumps
- Generated data files

**❌ DON'T PUT HERE**:
- Code files
- Configuration files

#### `projects/` - Project-Specific Code
**✅ PUT HERE**:
- Business-specific implementations
- Project-specific logic
- One-time analysis scripts

**Subdirectories**:
- `projects/adhoc/` - Temporary/one-time files
  - `projects/adhoc/exploration/` - Temporary exploration/test scripts
  - `projects/adhoc/notebooks/` - One-time notebook tasks
  - `projects/adhoc/queries/` - One-time investigation queries
- `projects/adyen_ml/` - Adyen ML project
- `projects/p0_metrics/` - P0 Metrics project

**❌ DON'T PUT HERE**:
- Reusable utilities (use `core/`)
- CLI scripts (use `scripts/`)

#### `docs/` - Documentation
**✅ PUT HERE**:
- All documentation files (`.md`)
- Organized by subdirectory:
  - `docs/guides/` - User guides
  - `docs/reference/` - Reference documentation
  - `docs/status/` - Status/cleanup docs
  - `docs/notes/` - Notes
  - `docs/examples/` - Example documentation
  - `docs/guidelines/` - Guidelines

**❌ DON'T PUT HERE**:
- Code files
- Data files
- Configuration files

### Decision Tree for File Placement

```
What type of file are you creating?
│
├─ Reusable utility function?
│  └─ → core/
│
├─ CLI script (command-line tool)?
│  └─ → scripts/
│
├─ Reusable notebook utility?
│  └─ → notebooks/
│
├─ Test file?
│  └─ → tests/
│
├─ Example/template?
│  └─ → examples/
│
├─ Data file (CSV, JSON)?
│  └─ → data/
│
├─ Documentation?
│  └─ → docs/ (with appropriate subdirectory)
│
├─ One-time task/analysis?
│  └─ → projects/adhoc/
│     ├─ Exploration/test script? → projects/adhoc/exploration/
│     ├─ One-time notebook? → projects/adhoc/notebooks/
│     └─ Investigation query? → projects/adhoc/queries/
│
└─ Project-specific code?
   └─ → projects/[project_name]/
```

### File Naming Conventions

- **Python files**: `snake_case.py`
- **Test files**: `test_*.py` (must be in `tests/`)
- **Example files**: `example_*.py` (must be in `examples/`)
- **SQL files**: `descriptive_name.sql`
- **Documentation**: `UPPERCASE.md` or `snake_case.md`

### Validation

**ALWAYS run the validation script after creating files**:
```bash
python scripts/validate_file_placement.py
```

This will check:
- ✅ No files in root (except allowed 7)
- ✅ Test files in `tests/`
- ✅ Examples in `examples/`
- ✅ Data files in `data/`
- ✅ Documentation in `docs/`
- ✅ One-time tasks in `projects/adhoc/`

### Common Mistakes to Avoid

❌ **DON'T**: Create test files in root
✅ **DO**: Put in `tests/`

❌ **DON'T**: Create one-time scripts in `notebooks/`
✅ **DO**: Put in `projects/adhoc/notebooks/`

❌ **DON'T**: Create investigation queries in root
✅ **DO**: Put in `projects/adhoc/queries/`

❌ **DON'T**: Create documentation in root
✅ **DO**: Put in `docs/` with appropriate subdirectory

❌ **DON'T**: Create reusable utilities in `projects/`
✅ **DO**: Put in `core/`

---

**Last Updated**: 2025-01-XX
**Version**: 2.0



