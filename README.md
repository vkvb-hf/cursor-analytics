# Cursor Analytics

A toolkit for working with Databricks and other data services via MCP (Model Context Protocol).

## Project Structure

```
cursor-analytics/
├── mcp/                        # MCP Servers (all 5)
│   ├── databricks/             # Databricks MCP (7 tools)
│   ├── google_sheets/          # Google Sheets MCP (4 tools)
│   ├── atlassian/              # Atlassian MCP docs (28 tools)
│   ├── atlan/                  # Atlan MCP docs (12 tools)
│   └── github/                 # GitHub MCP docs (26 tools)
│
├── core/                       # Pure functions (6 modules)
│   ├── databricks_job_runner.py
│   ├── table_inspector.py
│   ├── query_util.py
│   ├── workspace_sync.py
│   ├── run_sql_file.py
│   └── _config.py
│
├── use_cases/                  # Composite scripts
│   ├── csv_to_table.py
│   ├── create_table.py
│   └── interactive_sql.py
│
├── scripts/                    # CLI entry points
│   ├── smoke_test.py
│   └── ...
│
├── tests/                      # Test files
├── docs/                       # Documentation
├── archive/                    # Historical reference
│
├── databricks_api.py           # High-level Python API
├── databricks_cli.py           # CLI interface
└── requirements.txt
```

## Quick Start

### 1. Configure Databricks

Copy `config.py.example` to `config.py` and fill in your credentials:

```python
DATABRICKS_HOST = "https://your-workspace.cloud.databricks.com"
DATABRICKS_TOKEN = "your-token"
DATABRICKS_HTTP_PATH = "/sql/1.0/warehouses/your-warehouse"
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Use with Cursor

The MCP servers are configured in `~/.cursor/mcp.json`. Restart Cursor to load them.

## MCP Servers

| Server | Type | Tools | Description |
|--------|------|-------|-------------|
| **Databricks** | Local | 7 | SQL, notebooks, workspace sync |
| **Google Sheets** | Local | 4 | Read spreadsheets |
| **Atlassian** | Remote | 28 | Jira, Confluence |
| **Atlan** | Remote | 12 | Data catalog, lineage |
| **GitHub** | NPM | 26 | Repos, PRs, issues |

See `mcp/README.md` for detailed documentation.

## Core Functions

```python
from core import (
    DatabricksJobRunner,  # Create and run Databricks jobs
    TableInspector,       # Inspect table schemas
    run_query,            # Execute SQL queries
    print_table,          # Format query results
    run_sql_file,         # Execute SQL from files
    WorkspaceSync,        # Sync files with Databricks
)
```

## Python API

```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()

# Run SQL
results = db.run_sql("SELECT * FROM my_table LIMIT 10")

# Inspect table
schema = db.inspect_table("my_schema.my_table")
```

## CLI

```bash
# Run SQL
python databricks_cli.py sql "SELECT * FROM table LIMIT 10"

# Run SQL file
python databricks_cli.py sql-file queries/my_query.sql

# Inspect table
python databricks_cli.py table inspect schema.table
```

## Testing

```bash
# Quick smoke test
python scripts/smoke_test.py --quick

# Full test suite
pytest tests/
```

## Architecture

- **mcp/**: All MCP servers in one place
- **core/**: Pure functions with no side effects
- **use_cases/**: Scripts that combine core functions
- **archive/**: Historical projects and unused code
