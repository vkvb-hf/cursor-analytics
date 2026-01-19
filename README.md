# Cursor Analytics

A toolkit for working with Databricks and other data services via MCP (Model Context Protocol).

## Project Structure

```
cursor-analytics/
├── mcp/                        # MCP Servers (primary interface)
│   ├── databricks/server.py    # Databricks MCP (7 tools)
│   ├── google_sheets/server.py # Google Sheets MCP (4 tools)
│   ├── atlassian/              # Atlassian MCP docs
│   ├── atlan/                  # Atlan MCP docs
│   └── github/                 # GitHub MCP docs
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
├── scripts/                    # CLI tools
├── tests/                      # Test files
├── docs/                       # Documentation
└── archive/                    # Historical reference
```

## Quick Start

### 1. Configure Databricks

Create `.env` in `mcp/databricks/`:

```bash
DATABRICKS_HOST=https://your-workspace.cloud.databricks.com
DATABRICKS_TOKEN=your-token
DATABRICKS_HTTP_PATH=/sql/1.0/warehouses/your-warehouse
CLUSTER_ID=your-cluster-id
```

### 2. Use with Cursor

MCP servers are configured in `~/.cursor/mcp.json`. Restart Cursor to load them.

## MCP Servers

| Server | Type | Tools | Description |
|--------|------|-------|-------------|
| **Databricks** | Local | 7 | SQL, notebooks, workspace sync |
| **Google Sheets** | Local | 4 | Read spreadsheets |
| **Atlassian** | Remote | 28 | Jira, Confluence |
| **Atlan** | Remote | 12 | Data catalog, lineage |
| **GitHub** | NPM | 26 | Repos, PRs, issues |

See `mcp/README.md` for detailed documentation.

## Testing

```bash
python scripts/smoke_test.py --quick
```
