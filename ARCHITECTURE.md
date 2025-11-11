# Architecture & Design Philosophy

## Re-thinking the Architecture for Cursor IDE

You asked: "Is having different .py files the best way to do these things? In the end I want to do the main goals, just from Cursor."

**Short answer:** For Cursor IDE usage, having separate .py files is actually a good approach, but we've improved it with unified entry points.

## Why This Architecture Works for Cursor

### 1. **Unified Entry Points** (New)

Instead of remembering multiple scripts, you now have:

#### Option A: Python API (`databricks_api.py`)
```python
# In Cursor, just type:
from databricks_api import DatabricksAPI, sql, inspect, notebook

# Quick SQL execution
results = sql("SELECT * FROM table LIMIT 10")

# Inspect table
schema = inspect("schema.table", sample=10)

# Create notebook job
job = notebook("/Workspace/path", content, "my_job")
```

#### Option B: Unified CLI (`databricks_cli.py`)
```bash
# All operations through one command
python databricks_cli.py sql --query "SELECT * FROM table"
python databricks_cli.py table inspect schema.table --stats
python databricks_cli.py notebook run /Workspace/path --file notebook.py
```

### 2. **Modular Core Utilities** (Existing)

The `core/` directory contains reusable utilities that:
- Can be imported individually if needed
- Are well-tested and documented
- Follow single responsibility principle
- Can be composed together

### 3. **Why Not a Single Monolithic File?**

**Problems with a single file:**
- ❌ Hard to maintain (1000+ lines)
- ❌ Hard to test (everything mixed together)
- ❌ Hard to reuse (can't import just what you need)
- ❌ Hard to understand (too many responsibilities)

**Benefits of modular approach:**
- ✅ Easy to test (each module has focused tests)
- ✅ Easy to reuse (import only what you need)
- ✅ Easy to maintain (clear separation of concerns)
- ✅ Easy to extend (add new utilities without breaking existing)

## Architecture Layers

```
┌─────────────────────────────────────────────────┐
│  Cursor IDE / Your Scripts                      │
│  (Use databricks_api.py or databricks_cli.py)   │
└─────────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────┐
│  Unified Entry Points                            │
│  • databricks_api.py (Python API)               │
│  • databricks_cli.py (CLI tool)                 │
└─────────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────┐
│  Core Utilities (core/)                         │
│  • query_util.py - SQL execution                │
│  • databricks_job_runner.py - Job management   │
│  • table_inspector.py - Table inspection        │
│  • databricks_workspace.py - Workspace ops     │
│  • ... (other utilities)                        │
└─────────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────┐
│  Databricks APIs                                │
│  • SQL Warehouse API                            │
│  • Jobs API                                     │
│  • Workspace API                                │
└─────────────────────────────────────────────────┘
```

## Usage Patterns in Cursor

### Pattern 1: Quick One-liners (API)
```python
from databricks_api import sql, inspect

# Run query
results = sql("SELECT COUNT(*) FROM schema.table")

# Inspect table
info = inspect("schema.table", sample=5)
```

### Pattern 2: Full Control (API Class)
```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()
results = db.run_sql("SELECT * FROM table", limit=100, display=False)
schema = db.inspect_table("schema.table", include_stats=True)
```

### Pattern 3: CLI from Terminal
```bash
python databricks_cli.py sql --query "SELECT * FROM table"
python databricks_cli.py table inspect schema.table --stats
```

### Pattern 4: Direct Core Import (Advanced)
```python
from core import DatabricksJobRunner, TableInspector
from core.query_util import run_query

# Use specific utilities directly
```

## File Organization Rationale

### `core/` - Reusable Utilities
- **Why separate files?** Each utility has a single, clear purpose
- **Why not one big file?** Would be 2000+ lines, hard to navigate
- **Benefit:** Easy to find what you need, easy to test

### `databricks_api.py` - Unified Python Interface
- **Why?** Provides a clean, simple API for Cursor usage
- **Benefit:** One import, all functionality

### `databricks_cli.py` - Unified CLI
- **Why?** Single command for all operations from terminal
- **Benefit:** Easy to remember, consistent interface

### `scripts/` - Legacy Scripts (Optional)
- **Why keep?** Backward compatibility, some users prefer direct scripts
- **Can be deprecated:** Eventually all functionality is in CLI/API

## Alternative Approaches Considered

### ❌ Single `databricks.py` file
**Problems:**
- 2000+ lines in one file
- Hard to navigate and maintain
- Can't import just what you need
- All tests in one place

### ❌ Plugin-based architecture
**Problems:**
- Over-engineered for the use case
- Harder for Cursor to discover functionality
- More complex setup

### ✅ Current approach (Modular + Unified Entry Points)
**Benefits:**
- Clean separation of concerns
- Easy to use from Cursor (API)
- Easy to extend (modular)
- Easy to test (focused tests)
- Best of both worlds

## Recommendations for Cursor Usage

### For Quick Tasks:
```python
from databricks_api import sql, inspect, notebook
```

### For Complex Workflows:
```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()
# Build up complex operations
```

### For Scripts:
```bash
python databricks_cli.py [command] [options]
```

## Conclusion

The current architecture is optimal for Cursor IDE because:

1. **Simple API** (`databricks_api.py`) for quick usage
2. **Modular core** for maintainability and testing
3. **Unified CLI** for terminal operations
4. **Flexible** - use what you need, when you need it

You don't need to know about all the core utilities - just use the API or CLI. The modular structure is there for maintainability and extensibility.


