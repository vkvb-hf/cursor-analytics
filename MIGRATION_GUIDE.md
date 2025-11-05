# Migration Guide

This guide helps you update existing scripts to work with the new structure.

## Key Changes

### Directory Structure Changes

- `utils/` → `core/` (renamed for clarity)
- New `scripts/` directory for CLI entry points
- New `notebooks/` directory for notebook utilities
- New `queries/` directory for SQL files
- New `exploration/` directory for test/analysis scripts
- `tests/` → merged into `exploration/`

### Import Path Updates

#### Old Import Style
```python
from utils import DatabricksJobRunner
from utils.table_inspector import TableInspector
from utils.query_util import run_query
```

#### New Import Style
```python
from core import DatabricksJobRunner, TableInspector
from core.query_util import run_query, print_table
from core.run_sql_file import run_sql_file
```

### Script Updates

#### Running SQL Queries

**Old:**
```bash
python utils/run_sql_file.py query.sql
```

**New:**
```bash
python scripts/run_sql.py queries/query.sql
```

#### Interactive SQL

**Old:**
```bash
python utils/interactive_sql.py
```

**New:**
```bash
python scripts/interactive_sql.py
```

#### Inspecting Tables

**Old:**
```bash
python inspect_table.py schema.table
```

**New:**
```bash
python scripts/inspect_table.py schema.table --stats --schema
```

## Updating Project Files

If you have project-specific files that import from the old structure:

1. **Update imports:**
   ```python
   # Old
   import sys
   sys.path.append('../..')
   from utils import DatabricksJobRunner
   
   # New
   import sys
   import os
   sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
   from core import DatabricksJobRunner
   ```

2. **Update file paths:**
   - Move SQL queries to `queries/` directory
   - Move test/exploration scripts to `exploration/`
   - Keep project-specific code in `projects/`

## Configuration

The `config.py` file remains at the root level. All utilities automatically find it.

## Common Issues

### ImportError: No module named 'utils'
- Update imports to use `core` instead of `utils`

### ImportError: No module named 'config'
- Make sure you're running scripts from the project root
- Or add the root directory to `sys.path` as shown above

### FileNotFoundError for SQL files
- Move SQL files to `queries/` directory
- Update paths in your scripts to reference `queries/`

## Need Help?

Check the main README.md for comprehensive usage examples and documentation.

