# Cursor Analytics

An **MCP-first toolkit** for product analysts to interact with Databricks and data services directly from Cursor IDE. Instead of writing scripts, AI agents invoke MCP tools to execute SQL, run notebooks, and perform data exploration.

## Why This Exists

**Traditional workflow:**
```python
# Write a script, configure connection, run manually
from databricks import sql
conn = sql.connect(...)  # Setup boilerplate
cursor.execute("SELECT * FROM table")
```

**MCP workflow (what we use):**
```
# Just ask Cursor AI:
"Run this SQL: SELECT * FROM payments_hf.chargebacks LIMIT 10"
# AI invokes execute_sql tool → structured JSON response
```

**Benefits:**
- No boilerplate code for one-time queries
- Structured JSON responses for reliable parsing
- AI agents can chain operations intelligently
- Works with Databricks, Google Sheets, Jira, Atlan, GitHub

---

## Quick Start

### 1. Install

```bash
cd cursor-analytics
pip install -e .
```

### 2. Configure Databricks

Create `.env` in the repository root:

```bash
DATABRICKS_HOST=https://your-workspace.cloud.databricks.com
DATABRICKS_TOKEN=your-personal-access-token
DATABRICKS_HTTP_PATH=/sql/1.0/warehouses/your-warehouse-id
DATABRICKS_SERVER_HOSTNAME=your-workspace.cloud.databricks.com
CLUSTER_ID=your-cluster-id
```

### 3. Add to Cursor

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "databricks": {
      "command": "/path/to/python",
      "args": ["/path/to/cursor-analytics/mcp/databricks/server.py"],
      "cwd": "/path/to/cursor-analytics"
    }
  }
}
```

### 4. Restart Cursor

MCP tools are now available. Ask Cursor AI to run SQL queries directly.

---

## MCP Tools

### Databricks (7 tools)

| Tool | Purpose | Example Use |
|------|---------|-------------|
| `execute_sql` | Run any SQL query | `SELECT * FROM table LIMIT 10` |
| `run_sql_file` | Execute SQL from .sql files | Complex queries stored in files |
| `create_notebook` | Create Python notebooks in Databricks | Setup analysis notebooks |
| `run_notebook` | Create + run notebook as a job | Long-running analysis with plots |
| `get_job_status` | Check job run status | Monitor notebook execution |
| `sync_to_workspace` | Upload local files to Databricks | Deploy code changes |
| `sync_from_workspace` | Download files from Databricks | Backup or review code |

### Google Sheets (4 tools)

| Tool | Purpose |
|------|---------|
| `read_sheet` | Read data from a spreadsheet |
| `get_sheet_info` | Get sheet names and metadata |
| `read_multiple_ranges` | Read multiple ranges at once |
| `read_comments` | Extract cell comments |

### Tableau (12 tools)

| Tool | Purpose |
|------|---------|
| `list-workbooks` | List workbooks with filtering |
| `get-workbook` | Get workbook details and views |
| `list-views` | List views across workbooks |
| `get-view-image` | Get screenshot of a view |
| `get-view-data` | Get view data as CSV |
| `refresh-workbook-extract` | Trigger extract refresh |
| `list-datasources` | List published datasources |
| `get-datasource-metadata` | Get field metadata |
| `query-datasource` | Run VizQL queries |
| `get-job-status` | Check async job status |
| `search-content` | Search across content types |

### External MCPs (configured separately)

| MCP | Tools | Use For |
|-----|-------|---------|
| Atlassian | 28 | Jira tickets, Confluence docs |
| Atlan | 12 | Data catalog, lineage, metadata |
| GitHub | 26 | Repos, PRs, issues |

---

## Response Format

All MCP tools return structured JSON:

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

---

## Project Structure

```
cursor-analytics/
├── mcp/                      # MCP Servers (primary interface)
│   ├── databricks/           # Databricks MCP server (7 tools)
│   │   └── server.py         # Main server implementation
│   ├── google_sheets/        # Google Sheets MCP server (4 tools)
│   └── */README.md           # External MCP setup guides (Atlan, Atlassian, GitHub)
├── core/                     # Reusable Python utilities
│   ├── connection_pool.py    # Shared SQL connection pool
│   ├── databricks_job_runner.py  # Create and run Databricks jobs
│   ├── table_inspector.py    # Inspect table schemas
│   ├── query_util.py         # SQL execution helpers
│   ├── workspace_sync.py     # Sync files with Databricks workspace
│   └── _config.py            # Configuration loading
├── scripts/                  # CLI tools (alternative to MCP)
│   ├── smoke_test.py         # Quick validation script
│   ├── run_sql.py            # CLI SQL runner
│   └── inspect_table.py      # CLI table inspector
├── use_cases/                # Composite operations
│   ├── csv_to_table.py       # Create tables from CSV files
│   └── create_table.py       # Table creation utilities
├── tests/                    # Test suite (18 test files)
├── docs/                     # Documentation
│   ├── SETUP.md              # Detailed setup instructions
│   ├── MCP_GUIDE.md          # MCP tools reference
│   └── ARCHITECTURE.md       # Design philosophy
├── .cursorrules              # AI agent guidance for Cursor
├── .env                      # Credentials (git-ignored)
└── pyproject.toml            # Package configuration
```

---

## Usage Examples

### Data Exploration

Ask Cursor AI:
```
"Show me the tables in payments_hf schema"
"Describe the checkout_funnel_backend table"
"Get 10 sample rows from payments_hf.chargebacks"
```

### Run Analysis

Ask Cursor AI:
```
"Create a notebook to analyze conversion rates by week for NL customers"
"Run this SQL file: /path/to/query.sql"
```

### Data Quality

Ask Cursor AI:
```
"Find duplicate records in this table by customer_id"
"Check for nulls in the status column"
```

---

## For AI Agents

The `.cursorrules` file provides comprehensive guidance for AI agents, including:

- **MCP tool reference** - When to use each tool
- **Common workflows** - Data exploration, quality checks, analysis
- **EDA guidelines** - Required context, validation queries, pitfalls to avoid
- **File organization** - Where to put different types of files

Key principles:
1. **Use MCP tools** for all Databricks operations (don't write scripts)
2. **Validate assumptions** before running analysis (check data types, nulls)
3. **Save ad-hoc analysis** to temp folders, not this repository
4. **Return structured JSON** from any new utilities

---

## Testing

```bash
# Quick validation (no Databricks connection needed)
python scripts/smoke_test.py --quick

# Full test suite
pytest tests/ -v

# Specific module
pytest tests/test_mcp_databricks.py -v
```

---

## Documentation

| Document | Description |
|----------|-------------|
| [docs/SETUP.md](docs/SETUP.md) | Complete setup instructions with screenshots |
| [docs/MCP_GUIDE.md](docs/MCP_GUIDE.md) | Detailed MCP tools reference |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Design philosophy and extension guide |
| [.cursorrules](.cursorrules) | AI agent guidance (read by Cursor) |

---

## Troubleshooting

### MCP Connection Issues
1. Check `~/.cursor/mcp.json` syntax (valid JSON)
2. Verify `.env` file exists in repo root with correct credentials
3. Ensure `cwd` in mcp.json points to repo root (not mcp/databricks/)
4. Restart Cursor IDE

### Query Timeouts
1. Add `LIMIT` clause to exploratory queries
2. Check cluster status in Databricks UI
3. Use `run_notebook` for long-running queries (runs on cluster)

### Import Errors
```bash
pip install -e .  # Reinstall in editable mode
```

---

## Requirements

- Python ≥3.9
- Databricks workspace access
- Personal Access Token (PAT)

### Dependencies

```
databricks-sql-connector>=3.0.0
requests>=2.28.0
pandas>=1.5.0
python-dotenv>=1.0.0
mcp>=1.0.0  # For MCP servers
```

---

## License

Proprietary - Product Analytics Team
