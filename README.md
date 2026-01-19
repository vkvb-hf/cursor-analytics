# Cursor Analytics

A toolkit for product analysts to work with Databricks and data services via MCP (Model Context Protocol) in Cursor IDE.

## Quick Start

### 1. Install

```bash
pip install -e .
```

### 2. Configure

Create `mcp/databricks/.env`:

```bash
DATABRICKS_HOST=https://your-workspace.cloud.databricks.com
DATABRICKS_TOKEN=your-token
DATABRICKS_HTTP_PATH=/sql/1.0/warehouses/your-warehouse
CLUSTER_ID=your-cluster-id
```

### 3. Add to Cursor

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "databricks": {
      "command": "python",
      "args": ["/path/to/cursor-analytics/mcp/databricks/server.py"],
      "cwd": "/path/to/cursor-analytics/mcp/databricks"
    }
  }
}
```

### 4. Restart Cursor

The MCP tools are now available in Cursor.

---

## MCP Tools

| Tool | Description |
|------|-------------|
| `execute_sql` | Run any SQL query |
| `run_sql_file` | Execute SQL from .sql files |
| `create_notebook` | Create Databricks notebooks |
| `run_notebook` | Run notebooks as jobs |
| `get_job_status` | Check job status |
| `sync_to_workspace` | Upload files to Databricks |
| `sync_from_workspace` | Download files from Databricks |

All tools return structured JSON with `success`, `data`, `row_count`, etc.

---

## Project Structure

```
cursor-analytics/
├── mcp/                    # MCP Servers
│   ├── databricks/         # Databricks MCP (7 tools)
│   └── google_sheets/      # Google Sheets MCP (4 tools)
├── core/                   # Core utilities
├── scripts/                # CLI tools
├── tests/                  # Tests
├── docs/                   # Documentation
│   ├── SETUP.md           # Setup instructions
│   └── MCP_GUIDE.md       # MCP tools reference
└── archive/                # Historical (ignore)
```

---

## Documentation

| Document | Description |
|----------|-------------|
| [docs/SETUP.md](docs/SETUP.md) | Complete setup instructions |
| [docs/MCP_GUIDE.md](docs/MCP_GUIDE.md) | MCP tools reference |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Design philosophy |
| [.cursorrules](.cursorrules) | AI agent guidance |

---

## Testing

```bash
# Quick validation
python scripts/smoke_test.py --quick

# Full test suite
pytest tests/ -v
```

---

## Common Workflows

### Query Data

```sql
-- Via MCP execute_sql tool
SELECT * FROM schema.table LIMIT 10
```

### Find Duplicates

```sql
SELECT column, COUNT(*) 
FROM table 
GROUP BY column 
HAVING COUNT(*) > 1
```

### Create Table

```sql
CREATE TABLE schema.new_table AS
SELECT * FROM source WHERE condition
```

---

## External MCPs

| MCP | Tools | Description |
|-----|-------|-------------|
| Atlassian | 28 | Jira, Confluence |
| Atlan | 12 | Data catalog, lineage |
| GitHub | 26 | Repos, PRs, issues |

See [docs/MCP_GUIDE.md](docs/MCP_GUIDE.md) for configuration.

---

## License

Proprietary - Product Analytics Team
