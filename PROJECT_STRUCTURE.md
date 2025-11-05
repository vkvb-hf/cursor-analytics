# Project Structure Reference

This document provides a quick reference for the project structure and file organization.

## Directory Structure

```
cursor_databricks/
│
├── config.py                    # Databricks connection configuration (DO NOT COMMIT)
├── config.py.example            # Template for config.py
│
├── core/                        # 🔧 Core reusable utilities
│   ├── __init__.py              # Package exports
│   ├── databricks_job_runner.py # Job creation and execution
│   ├── databricks_workspace.py  # Workspace file operations
│   ├── table_inspector.py       # Table inspection and validation
│   ├── query_util.py            # SQL query execution utilities
│   ├── interactive_sql.py       # Interactive SQL shell
│   ├── run_sql_file.py          # Execute SQL from files
│   ├── csv_to_table.py         # CSV to Delta table conversion
│   ├── upload_csvs.py           # CSV upload utilities
│   ├── unzip_csvs.py            # File extraction utilities
│   ├── create_table.py          # Table creation utilities
│   └── inspect_table.py         # Legacy inspection utility
│
├── scripts/                     # 🚀 CLI entry points
│   ├── run_sql.py              # Run SQL queries from files
│   ├── interactive_sql.py      # Interactive SQL shell
│   ├── inspect_table.py        # Inspect table schema and data
│   └── create_notebook.py      # Create and run notebooks
│
├── notebooks/                   # 📓 Notebook management utilities
│   ├── README.md               # Notebook utilities documentation
│   ├── create_and_run_databricks_job.py
│   ├── get_job_output.py
│   ├── get_notebook_content.py
│   ├── get_notebook_from_job.py
│   ├── get_notebook_from_url.py
│   └── check_job_status.py
│
├── queries/                     # 📊 SQL query files
│   ├── README.md               # Query organization guide
│   └── [organize by use case or table]
│
├── exploration/                 # 🔍 Ad-hoc analysis & testing
│   ├── README.md               # Exploration guidelines
│   └── [test scripts, exploration notebooks]
│
├── projects/                    # 💼 Business use case implementations
│   ├── adyen_ml/               # Adyen ML project
│   │   ├── README.md
│   │   └── [project-specific files]
│   └── p0_metrics/             # P0 Metrics project
│       └── [project-specific files]
│
└── docs/                        # 📚 Documentation
    └── AI_UTILITY_GUIDE.md     # AI utility selection guide
```

## File Categories

### 🔧 Core Utilities (`core/`)
**Purpose**: Reusable across all projects

**Rules**:
- Must be generic and project-agnostic
- Should have clear docstrings
- Should follow consistent patterns
- Can depend on `config.py` and other utilities
- Automatically add parent directory to path for config imports

**Examples**:
- `databricks_job_runner.py`: Works for any notebook
- `table_inspector.py`: Works for any table
- `csv_to_table.py`: Works for any CSV → table conversion
- `query_util.py`: Works for any SQL query

### 🚀 CLI Scripts (`scripts/`)
**Purpose**: Entry points for common tasks

**Rules**:
- Should be executable from command line
- Add parent directory to path for imports
- Use argparse for command-line arguments
- Provide clear usage instructions

**Examples**:
- `run_sql.py`: Run SQL files
- `interactive_sql.py`: Interactive SQL shell
- `inspect_table.py`: Inspect tables

### 📓 Notebook Utilities (`notebooks/`)
**Purpose**: Utilities for creating and managing Databricks notebooks

**Rules**:
- Focus on notebook-related operations
- Can import from `core/`
- Should handle notebook-specific tasks

### 📊 SQL Queries (`queries/`)
**Purpose**: SQL query files organized by purpose

**Rules**:
- Organize by use case, table, or type
- Use descriptive names
- Document in query comments
- Can be run via `scripts/run_sql.py`

### 🔍 Exploration (`exploration/`)
**Purpose**: Ad-hoc analysis, testing, and debugging

**Rules**:
- Temporary or exploratory scripts
- Can be deleted after use
- Use descriptive names for future reference

### 💼 Projects (`projects/`)
**Purpose**: Business-specific implementations

**Rules**:
- Contains business-specific logic
- Can import from `core/`
- Should have its own README
- Can reference specific tables/schemas

**Examples**:
- `projects/adyen_ml/`: Adyen ML payment data processing
- `projects/p0_metrics/`: P0 metrics analysis

### 📚 Documentation (`docs/`)
**Purpose**: Comprehensive documentation

**Rules**:
- Reference documentation
- Guides for AI models
- Best practices

## Import Paths

### From Project Root
```python
from core import DatabricksJobRunner, TableInspector
from core.query_util import run_query, print_table
from config import SERVER_HOSTNAME, TOKEN
```

### From Project-Specific Files
```python
# In projects/my_project/my_script.py
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from core import DatabricksJobRunner
from config import SERVER_HOSTNAME, TOKEN
```

### From Core Utilities
```python
# In core/my_utility.py
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import SERVER_HOSTNAME, TOKEN
```

### From Scripts
```python
# In scripts/my_script.py
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core import DatabricksJobRunner
from config import SERVER_HOSTNAME, TOKEN
```

## Adding New Files

### New Core Utility?
1. Place in `core/`
2. Add to `core/__init__.py`
3. Update `docs/AI_UTILITY_GUIDE.md`
4. Add docstrings and type hints
5. Add path fix for config imports

### New CLI Script?
1. Place in `scripts/`
2. Add parent directory to path
3. Use argparse for arguments
4. Provide clear usage instructions

### New Project?
1. Create `projects/my_project/`
2. Add `projects/my_project/README.md`
3. Import from `core/` as needed
4. Keep project-specific logic here

### New Query?
1. Save in `queries/` directory
2. Organize by use case or table
3. Use descriptive names
4. Document in query comments

### New Test/Exploration Script?
1. Place in `exploration/`
2. Use descriptive names
3. Can be temporary

## File Naming Conventions

- **Core Utilities**: `snake_case.py`
- **Projects**: `project_name/` directory
- **Tests**: `test_*.py` or `check_*.py`
- **Docs**: `UPPERCASE.md` or `snake_case.md`
- **Queries**: `descriptive_name.sql`

## Configuration

- **`config.py`**: Contains credentials (DO NOT COMMIT)
- **`config.py.example`**: Template (safe to commit)
- All utilities should import from `config.py`
- Path fixes are added automatically in core utilities

## Best Practices

1. ✅ Use generic utilities from `core/`
2. ✅ Keep project code in `projects/`
3. ✅ Write tests in `exploration/`
4. ✅ Document in `docs/`
5. ✅ Organize queries in `queries/`
6. ✅ Use CLI scripts in `scripts/`
7. ❌ Don't mix generic and project code
8. ❌ Don't commit `config.py`
9. ❌ Don't duplicate utility code
10. ❌ Don't create loose files at root level
