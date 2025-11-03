# Project Structure Reference

This document provides a quick reference for the project structure and file organization.

## Directory Structure

```
cursor_databricks/
│
├── config.py                    # Databricks connection configuration (DO NOT COMMIT)
├── config.py.example            # Template for config.py
│
├── utils/                       # 🔧 Generic, reusable utilities
│   ├── __init__.py              # Package initialization
│   ├── databricks_job_runner.py # Job creation and execution
│   ├── databricks_workspace.py  # Workspace file operations
│   ├── table_inspector.py       # Table inspection and validation
│   ├── csv_to_table.py         # CSV to Delta table conversion
│   ├── upload_csvs.py           # CSV upload utilities
│   ├── unzip_csvs.py            # File extraction utilities
│   ├── query_util.py            # SQL query utilities
│   ├── interactive_sql.py       # Interactive SQL shell
│   ├── run_sql_file.py          # SQL file execution
│   └── create_table.py          # Table creation from SQL
│
├── projects/                    # 📁 Project-specific implementations
│   └── adyen_ml/               # Adyen ML project
│       ├── README.md           # Project documentation
│       ├── run_adyen_ml_job.py # Main ETL script
│       ├── check_duplicates.py  # Data validation
│       ├── check_conflicting_attributes.py
│       ├── verify_table_counts.py
│       └── ...
│
├── tests/                       # 🧪 Test and debugging scripts
│   ├── check_cluster.py
│   ├── check_job_status.py
│   ├── test_file_access.py
│   └── ...
│
├── docs/                        # 📚 Documentation
│   └── AI_UTILITY_GUIDE.md     # AI utility selection guide
│
├── README.md                    # Main project README
├── SETUP.md                     # Setup instructions
├── QUICK_START.md              # Quick start guide
├── INSTRUCTIONS.md             # Detailed instructions
└── CSV_UPLOAD_README.md        # CSV upload documentation
```

## File Categories

### 🔧 Generic Utilities (`utils/`)
**Purpose**: Reusable across all projects

**Rules**:
- Must be generic and project-agnostic
- Should have clear docstrings
- Should follow consistent patterns
- Can depend on `config.py` and other utilities

**Examples**:
- `databricks_job_runner.py`: Works for any notebook
- `table_inspector.py`: Works for any table
- `csv_to_table.py`: Works for any CSV → table conversion

### 📁 Project-Specific (`projects/`)
**Purpose**: Implementation for specific business use cases

**Rules**:
- Contains business-specific logic
- Can import from `utils/`
- Should have its own README
- Can reference specific tables/schemas

**Examples**:
- `projects/adyen_ml/`: Adyen ML payment data processing
- Could add: `projects/fraud_detection/`, `projects/reporting/`

### 🧪 Tests (`tests/`)
**Purpose**: Testing, debugging, and validation scripts

**Rules**:
- Temporary or exploratory scripts
- Not part of main workflow
- Can be deleted after use

### 📚 Documentation (`docs/`)
**Purpose**: Comprehensive documentation

**Rules**:
- Reference documentation
- Guides for AI models
- Best practices

## Import Paths

### From Project Root
```python
from utils import DatabricksJobRunner
from utils.table_inspector import TableInspector
from config import SERVER_HOSTNAME, TOKEN
```

### From Project-Specific Files
```python
# In projects/adyen_ml/run_adyen_ml_job.py
import sys
sys.path.append('../..')  # Add root to path

from utils import DatabricksJobRunner
from config import SERVER_HOSTNAME, TOKEN
```

### From Utilities
```python
# In utils/databricks_job_runner.py
from config import DATABRICKS_HOST, TOKEN
```

## Adding New Files

### New Generic Utility?
1. Place in `utils/`
2. Add to `utils/__init__.py`
3. Update `docs/AI_UTILITY_GUIDE.md`
4. Add docstrings and type hints

### New Project?
1. Create `projects/my_project/`
2. Add `projects/my_project/README.md`
3. Import from `utils/` as needed
4. Keep project-specific logic here

### New Test/Debug Script?
1. Place in `tests/`
2. Use descriptive names
3. Can be temporary

## File Naming Conventions

- **Utilities**: `snake_case.py`
- **Projects**: `project_name/` directory
- **Tests**: `test_*.py` or `check_*.py`
- **Docs**: `UPPERCASE.md` or `snake_case.md`

## Configuration

- **`config.py`**: Contains credentials (DO NOT COMMIT)
- **`config.py.example`**: Template (safe to commit)
- All utilities should import from `config.py`

## Best Practices

1. ✅ Use generic utilities from `utils/`
2. ✅ Keep project code in `projects/`
3. ✅ Write tests in `tests/`
4. ✅ Document in `docs/`
5. ❌ Don't mix generic and project code
6. ❌ Don't commit `config.py`
7. ❌ Don't duplicate utility code

