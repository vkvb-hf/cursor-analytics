# Databricks Python Toolkit

A comprehensive, well-organized toolkit for working with Databricks. This repository provides utilities for running SQL queries, creating and executing notebooks, exploring tables, and building business solutions.

## 📁 Project Structure

```
cursor_databricks/
├── config.py                    # ✅ Databricks connection configuration (DO NOT COMMIT)
├── config.py.example            # ✅ Template for config.py
├── README.md                    # ✅ Main documentation (this file)
├── databricks_api.py            # ✅ Main Python API entry point
├── databricks_cli.py            # ✅ Main CLI entry point
├── requirements.txt             # ✅ Python dependencies
├── requirements-test.txt        # ✅ Test dependencies
│
├── core/                        # 🔧 Core reusable utilities
│   ├── __init__.py              # Package exports
│   ├── databricks_job_runner.py # Job creation and execution
│   ├── databricks_workspace.py  # Workspace file operations
│   ├── table_inspector.py       # Table inspection and validation
│   ├── query_util.py            # SQL query execution utilities
│   ├── interactive_sql.py      # Interactive SQL shell
│   ├── run_sql_file.py          # Execute SQL from files
│   ├── csv_to_table.py          # CSV to Delta table conversion
│   ├── upload_csvs.py           # CSV upload utilities
│   ├── unzip_csvs.py            # File extraction utilities
│   └── create_table.py          # Table creation utilities
│
├── scripts/                     # 🚀 CLI entry points
│   ├── run_sql.py              # Run SQL queries from files
│   ├── interactive_sql.py      # Interactive SQL shell
│   ├── inspect_table.py        # Inspect table schema and data
│   ├── create_notebook.py      # Create and run notebooks
│   ├── run_query_now.py        # Quick query runner
│   └── verify_setup.py         # Setup verification utility
│
├── notebooks/                   # 📓 Notebook utilities (reusable only)
│   ├── README.md               # Notebook utilities documentation
│   └── [reusable notebook utilities]
│
├── examples/                    # 📝 Example scripts and templates
│   ├── example_notebook_with_output.py
│   ├── example_query.py
│   └── notebook_template.py
│
├── data/                        # 📊 Data files (CSV, exports, etc.)
│   └── [data files]
│
├── projects/                    # 💼 Business use case implementations
│   ├── adhoc/                  # 🔍 Ad-hoc investigations and analysis
│   │   ├── exploration/        # Temporary exploration/test scripts
│   │   ├── notebooks/          # One-time notebook tasks
│   │   ├── queries/            # One-time investigation queries
│   │   └── [other investigation files]
│   ├── adyen_ml/               # Adyen ML project
│   │   ├── README.md
│   │   └── [project-specific files]
│   └── p0_metrics/             # P0 Metrics project
│       └── [project-specific files]
│
├── tests/                       # 🧪 Test files
│   ├── README.md
│   └── [all test files]
│
└── docs/                        # 📚 Documentation (organized)
    ├── AI_UTILITY_GUIDE.md     # AI utility selection guide
    ├── ARCHITECTURE.md          # Architecture documentation
    ├── guides/                  # User guides
    │   ├── SETUP.md
    │   ├── QUICK_START.md
    │   ├── INSTRUCTIONS.md
    │   └── [other guides]
    ├── reference/               # Reference documentation
    │   ├── PROJECT_STRUCTURE.md
    │   └── CORE_FUNCTIONS_LIST.md
    ├── status/                  # Status and cleanup docs
    │   ├── CLEANUP_COMPLETE.md
    │   └── [other status docs]
    ├── notes/                   # Notes and summaries
    │   └── [notes files]
    ├── examples/                # Example documentation
    │   └── USAGE_EXAMPLE.md
    └── guidelines/              # Guidelines
        └── AI_DATASET_EXPLORATION_GUIDELINES.md
```

## 🚀 Quick Start

### 🎯 **NEW: Using Cursor Effectively**

**Want to maximize your productivity?** Read the **[Cursor Mastery Guide](docs/guides/CURSOR_MASTERY_GUIDE.md)** first!

**Key insight**: Instead of writing code manually, **ask Cursor to do it**:
```
You: "Query the duplicate_customers table for clusters > 100"
Cursor: [Uses databricks_api automatically and shows results]
```

**10x faster** than writing code yourself!

### 📓 Create and Run Notebooks (Terminal Output)

**Most Important**: To see output in terminal, notebooks must write to DBFS files.

```bash
# Run the example script
python create_and_run_notebook_job.py
```

**See `HOW_TO_CREATE_AND_RUN_NOTEBOOKS.md` for complete instructions!**

### 1. Setup Configuration

```bash
cp config.py.example config.py
# Edit config.py with your Databricks credentials
```

**Required Configuration:**
- `SERVER_HOSTNAME`: Your workspace hostname
- `HTTP_PATH`: SQL warehouse HTTP path
- `TOKEN`: Personal access token
- `DATABRICKS_HOST`: Full workspace URL

### 2. Setup Virtual Environment (Recommended)

**Important**: Always use the virtual environment for running scripts.

```bash
# Navigate to databricks directory
cd /path/to/databricks

# Activate virtual environment
source databricks_env/bin/activate

# Install dependencies (if not already installed)
pip install -r cursor_databricks/requirements.txt
```

**Alternative**: Install dependencies globally (not recommended):
```bash
pip install databricks-sql-connector requests pandas
```

### 3. Run SQL Queries

**From SQL file:**
```bash
python scripts/run_sql.py queries/my_query.sql csv 1000
```

**Interactive SQL shell:**
```bash
python scripts/interactive_sql.py
```

**From Python:**
```python
from core.run_sql_file import run_sql_file
run_sql_file('queries/my_query.sql', output_format='csv', limit=1000)
```

### 4. Inspect Tables

```bash
python scripts/inspect_table.py schema.table_name --stats --schema --sample 20
```

### 5. Create and Run Notebooks

```python
from core import DatabricksJobRunner

runner = DatabricksJobRunner()
result = runner.create_and_run(
    notebook_path="/Workspace/path/to/notebook",
    notebook_content="# Your notebook code",
    job_name="My Job"
)
```

## 📚 Core Utilities

### Query Execution

**`core.query_util`** - Execute SQL queries with formatted output
```python
from core.query_util import run_query, print_table
results = run_query("SELECT * FROM table LIMIT 10")
print_table(results)
```

**`core.run_sql_file`** - Execute SQL from files
```python
from core.run_sql_file import run_sql_file
run_sql_file('queries/my_query.sql', output_format='csv')
```

**`core.interactive_sql`** - Interactive SQL shell
```python
from core.interactive_sql import main
main()  # Starts interactive shell
```

### Job Management

**`core.databricks_job_runner`** - Create and run Databricks jobs
```python
from core import DatabricksJobRunner

runner = DatabricksJobRunner()
result = runner.create_and_run(
    notebook_path="/Workspace/notebooks/my_notebook",
    notebook_content="# Databricks notebook code",
    job_name="My Scheduled Job"
)
```

### Table Inspection

**`core.table_inspector`** - Inspect and validate tables
```python
from core import TableInspector

inspector = TableInspector()
schema = inspector.get_table_schema("schema.table")
stats = inspector.get_table_stats("schema.table")
sample = inspector.get_table_sample("schema.table", limit=10)
```

### Workspace Management

**`core.databricks_workspace`** - Manage workspace files
```python
from core.databricks_workspace import create_workspace_directory, upload_csv_to_workspace

create_workspace_directory("/Workspace/my_directory")
upload_csv_to_workspace("local_file.csv", "/Workspace/my_directory/file.csv")
```

## 📓 Creating and Running Notebooks

**Important**: To see notebook output in the terminal, notebooks must write output to DBFS files.

### Quick Example

```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()

# Notebook that writes output to DBFS
notebook_content = """# Databricks notebook source
query = "SELECT * FROM table LIMIT 10"
result_df = spark.sql(query)

# Write output to DBFS (required for terminal display)
output_text = result_df.toPandas().to_string()
dbutils.fs.put("/tmp/output.txt", output_text, overwrite=True)
print(output_text)  # Also print for UI
"""

# Create and run
result = db.job_runner.create_and_run(
    notebook_path="/Shared/my_notebook",
    notebook_content=notebook_content,
    job_name="my_job"
)

# Read output from DBFS (script does this automatically)
# See HOW_TO_CREATE_AND_RUN_NOTEBOOKS.md for details
```

**📖 See `HOW_TO_CREATE_AND_RUN_NOTEBOOKS.md` for complete instructions**

## 🎯 Common Use Cases

### 1. Run SQL Query via Databricks

```bash
# Save your SQL query in queries/my_analysis.sql
python scripts/run_sql.py queries/my_analysis.sql csv
```

### 2. Create and Execute Databricks Notebook

```python
from core import DatabricksJobRunner

notebook_content = """
# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT * FROM my_table LIMIT 100
"""

runner = DatabricksJobRunner()
result = runner.create_and_run(
    notebook_path="/Workspace/notebooks/my_analysis",
    notebook_content=notebook_content,
    job_name="Daily Analysis"
)
```

### 3. Run Exploration Analysis on SQL Tables

```python
from core import TableInspector
from core.query_util import run_query

# Inspect table structure
inspector = TableInspector()
schema = inspector.get_table_schema("schema.table_name")
print(schema)

# Run exploration queries
results = run_query("""
    SELECT 
        COUNT(*) as total_rows,
        COUNT(DISTINCT id) as unique_ids,
        MIN(created_at) as earliest,
        MAX(created_at) as latest
    FROM schema.table_name
""")
```

### 4. Build Business Products (Notebooks)

Create a new project in `projects/`:

```python
# projects/my_business_case/analysis_notebook.py
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from core import DatabricksJobRunner

# Business logic here
notebook_content = """
# Databricks notebook source
# Business-specific analysis
"""

runner = DatabricksJobRunner()
runner.create_and_run(
    notebook_path="/Workspace/projects/my_business_case",
    notebook_content=notebook_content,
    job_name="My Business Case Analysis"
)
```

## 📖 Documentation

Documentation is organized in the `docs/` directory:

### Quick Start & Guides
- **`docs/guides/QUICK_START.md`** - Quick start guide
- **`docs/guides/SETUP.md`** - Setup instructions
- **`docs/guides/INSTRUCTIONS.md`** - Detailed workflow instructions
- **`docs/guides/HOW_TO_CREATE_AND_RUN_NOTEBOOKS.md`** - Notebook creation guide
- **`docs/guides/TESTING.md`** - Testing guide

### 🚀 Cursor Mastery (NEW!)
- **`docs/guides/CURSOR_MASTERY_GUIDE.md`** - ⭐ **START HERE** - How to use Cursor effectively with this toolkit
- **`docs/guides/CURSOR_WORKFLOW_EXAMPLES.md`** - Real-world workflow examples
- **`docs/guides/CURSOR_USAGE.md`** - Basic Cursor integration guide

### Reference
- **`docs/reference/PROJECT_STRUCTURE.md`** - Complete project structure reference
- **`docs/reference/CORE_FUNCTIONS_LIST.md`** - Core functions listing
- **`docs/ARCHITECTURE.md`** - Architecture documentation

### Other Documentation
- **`docs/AI_UTILITY_GUIDE.md`** - Guide for AI models to select utilities
- **`notebooks/README.md`** - Notebook utilities documentation
- **`projects/adhoc/`** - Temporary investigation and analysis scripts
  - `projects/adhoc/exploration/` - Temporary exploration/test scripts
  - `projects/adhoc/notebooks/` - One-time notebook tasks
  - `projects/adhoc/queries/` - One-time investigation queries
- **`projects/*/README.md`** - Project-specific documentation

## 🔧 Best Practices

1. **Use Core Utilities**: Always use utilities from `core/` for reusable functionality
2. **Project Structure**: Keep business-specific code in `projects/`
3. **Temporary Files**: Place one-time tasks, exploration scripts, and investigation queries in `projects/adhoc/`
4. **Notebook Utilities**: Use `notebooks/` only for reusable notebook utilities (not one-time tasks)
5. **Examples**: Reference `examples/` directory for templates and sample code
6. **Documentation**: Place documentation in `docs/` with appropriate subdirectories
7. **Tests**: All test files should be in `tests/` directory
8. **Data Files**: Store data files (CSV, exports) in `data/` directory
9. **Configuration**: Never commit `config.py` with real credentials
10. **Cleanup**: Regularly review and delete files in `projects/adhoc/` when no longer needed
11. **Validation**: Always run `python scripts/validate_file_placement.py` after creating files to ensure correct placement

## 🧪 Testing & Exploration

### Running Tests

**Manual tests (no pytest required):**
```bash
python tests/test_manual.py
```

**Full test suite (requires pytest):**
```bash
pip install pytest pytest-mock
pytest tests/ -v
```

**Comprehensive integration test:**
```bash
pytest tests/test_all_functions_integration.py -v
```

The test suite includes:
- ✅ Import tests for all core modules
- ✅ Function unit tests
- ✅ Integration tests with sample use cases
- ✅ Error handling tests

### Exploration Scripts

Place test and exploration scripts in `exploration/`:
- Test scripts: `test_*.py`
- Validation scripts: `check_*.py`
- Verification scripts: `verify_*.py`

## 📝 Adding New Functionality

### New Core Utility?
1. Add to `core/` directory
2. Update `core/__init__.py` to export it
3. Update this README
4. Add docstrings and type hints

### New Project?
1. Create `projects/my_project/`
2. Add `projects/my_project/README.md`
3. Import from `core/` as needed
4. Keep project-specific logic isolated

### New Query?
1. Save in `queries/` directory
2. Organize by use case or table
3. Use descriptive names
4. Document in query comments

## 🔧 Recent Updates

### Import Fixes (Latest)
- ✅ Fixed relative import issues in `core/interactive_sql.py`
- ✅ Fixed relative import issues in `core/upload_csvs.py`
- ✅ All imports now use absolute paths for better compatibility
- ✅ Comprehensive import tests added to verify all modules work

### Testing Improvements
- ✅ Added `test_all_functions_integration.py` - comprehensive test using all functions
- ✅ Enhanced `test_manual.py` with complete import coverage
- ✅ All core functions tested with sample use cases
- ✅ Error handling tests added

### Known Issues Fixed
- ✅ Import errors when running modules as scripts
- ✅ Relative imports causing `ImportError` in some contexts
- ✅ Missing test coverage for import functionality

## ⚠️ Security Notes

- **Never commit `config.py`** with real credentials
- Use environment variables for sensitive data in production
- Rotate tokens regularly
- Follow your organization's security policies

## 📄 License

Internal use only.
