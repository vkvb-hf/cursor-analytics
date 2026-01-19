# Architecture & Design Philosophy

## MCP-First Architecture for Cursor IDE

This repository is designed around **Model Context Protocol (MCP)** as the primary interface for AI agents in Cursor IDE. Instead of traditional Python APIs or CLI tools, all Databricks operations are exposed as MCP tools that Cursor can invoke directly.

## Why MCP-First?

**Traditional approach (not used):**
```python
# Would require manual script execution
from some_api import sql
results = sql("SELECT * FROM table")
```

**MCP approach (what we use):**
```
# Cursor AI can directly call MCP tools
Use execute_sql tool with query: "SELECT * FROM table"
```

**Benefits of MCP-first:**
- ✅ AI agents can invoke tools directly without code
- ✅ Structured JSON responses for reliable parsing
- ✅ No import/setup required in user scripts
- ✅ Tools are discoverable by Cursor IDE
- ✅ Consistent interface across all operations

## Architecture Layers

```
┌─────────────────────────────────────────────────┐
│  Cursor IDE / AI Agent                          │
│  (Invokes MCP tools directly)                   │
└─────────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────┐
│  MCP Servers (mcp/)                             │
│  • databricks/server.py - 7 tools               │
│  • google_sheets/server.py - 4 tools            │
│  • External: Atlassian, Atlan, GitHub           │
└─────────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────┐
│  Core Utilities (core/)                         │
│  • connection_pool.py - SQL connections         │
│  • databricks_job_runner.py - Job management    │
│  • table_inspector.py - Table inspection        │
│  • workspace_sync.py - Workspace operations     │
│  • query_util.py - Query formatting             │
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

### Pattern 1: MCP Tools (Primary - Recommended)

All Databricks operations should go through MCP tools:

```
# Via Cursor AI - just describe what you want:
"Run this SQL: SELECT * FROM payments_hf.chargebacks LIMIT 10"
"Create a notebook at /Workspace/Users/me/analysis with this content..."
"Sync my local files to Databricks workspace"
```

The AI will use the appropriate MCP tool (`execute_sql`, `create_notebook`, `sync_to_workspace`).

### Pattern 2: Direct Core Import (Advanced/Scripts)

For custom scripts or advanced use cases, import from `core/`:

```python
from core import DatabricksJobRunner, TableInspector
from core.connection_pool import get_pool

# Use specific utilities directly
pool = get_pool()
results = pool.execute("SELECT * FROM table")
```

### Pattern 3: Use Cases (Composite Operations)

For complex workflows, use the `use_cases/` modules:

```python
from use_cases.csv_to_table import create_table_from_csvs

create_table_from_csvs(
    workspace_path="/Workspace/data",
    table_name="schema.my_table"
)
```

## File Organization

### `mcp/` - MCP Servers (Primary Interface)
- **databricks/server.py** - Main Databricks MCP server (7 tools)
- **google_sheets/server.py** - Google Sheets MCP server (4 tools)
- **External MCPs** - Configuration docs for Atlassian, Atlan, GitHub

### `core/` - Reusable Utilities
- **Why separate files?** Each utility has a single, clear purpose
- **Why not one big file?** Would be 2000+ lines, hard to navigate
- **Benefit:** MCP servers import from here; no code duplication

### `scripts/` - CLI Tools
- Standalone scripts for specific tasks
- Can be run directly from terminal
- Useful for automation outside of Cursor

### `use_cases/` - Composite Operations
- Complex workflows combining multiple core utilities
- Example: `csv_to_table.py` - Create tables from CSV files

### `tests/` - Test Suite
- Unit tests for core modules
- Integration tests for MCP servers
- Run with `pytest tests/ -v`

## Design Principles

### 1. MCP Tools Return Structured JSON

All MCP tools return consistent JSON:

```json
{
  "success": true,
  "data": [...],
  "row_count": 100,
  "columns": ["col1", "col2"],
  "execution_time_ms": 234,
  "error": null
}
```

### 2. Core Modules Are Pure Functions

Core utilities should:
- Have no side effects beyond their stated purpose
- Be independently testable
- Accept configuration via parameters (not globals)

### 3. MCP Servers Import from Core

MCP servers should NOT duplicate logic:

```python
# Good - import from core
from core.connection_pool import get_pool
results = get_pool().execute(query)

# Bad - duplicating logic in MCP server
def execute_query(query):
    # ... reimplementing connection logic
```

### 4. Configuration via Environment

All configuration comes from environment variables:
- No hardcoded defaults for sensitive values
- `.env` files for local development
- Clear error messages when config is missing

## Extending the Architecture

### Adding a New MCP Tool

1. Add the tool definition in `mcp/databricks/server.py`:
```python
Tool(
    name="new_tool",
    description="...",
    inputSchema={...}
)
```

2. Add the handler in `call_tool()`:
```python
elif name == "new_tool":
    # Implementation using core utilities
```

3. Add tests in `tests/test_mcp_databricks.py`

### Adding a New Core Utility

1. Create `core/new_utility.py`
2. Export in `core/__init__.py`
3. Add tests in `tests/test_new_utility.py`
4. Use in MCP server if needed

### Adding a New MCP Server

1. Create `mcp/new_service/server.py`
2. Add `mcp/new_service/README.md` with setup instructions
3. Add configuration to `~/.cursor/mcp.json`
4. Add tests in `tests/test_mcp_new_service.py`

## Conclusion

This architecture prioritizes:

1. **MCP-first** - AI agents interact via MCP tools
2. **Modular core** - Reusable utilities with no duplication
3. **Structured responses** - Consistent JSON for reliable parsing
4. **Secure configuration** - No hardcoded credentials
5. **Extensibility** - Easy to add new tools and services
