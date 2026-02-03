# Databricks MCP Server

A standalone Model Context Protocol server for Databricks operations.

## Tools

| Tool | Description |
|------|-------------|
| `execute_sql` | Run any SQL query on Databricks |
| `run_sql_file` | Execute SQL from a local .sql file |
| `create_notebook` | Create a notebook in Databricks workspace |
| `run_notebook` | Create and run a notebook as a job |
| `get_job_status` | Check job run status |
| `sync_to_workspace` | Upload local files to Databricks |
| `sync_from_workspace` | Download files from Databricks |
| `create_workspace_folder` | Create a folder in Databricks workspace |

## Configuration

### Environment Variables

Create a `.env` file in this directory or set system environment variables:

```bash
DATABRICKS_HOST=https://your-workspace.cloud.databricks.com
DATABRICKS_TOKEN=your-personal-access-token
DATABRICKS_HTTP_PATH=/sql/1.0/warehouses/your-warehouse-id
DATABRICKS_SERVER_HOSTNAME=your-workspace.cloud.databricks.com
CLUSTER_ID=your-cluster-id  # For notebook jobs
```

### Cursor Configuration

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "databricks": {
      "command": "/path/to/databricks_env/bin/python",
      "args": ["/path/to/cursor-analytics/mcp/databricks/server.py"],
      "cwd": "/path/to/cursor-analytics/mcp/databricks"
    }
  }
}
```

## Dependencies

```bash
pip install mcp databricks-sql-connector python-dotenv requests
```

## Usage Examples

### Execute SQL
```
Use execute_sql to run: SELECT * FROM my_schema.my_table LIMIT 10
```

### Run SQL File
```
Use run_sql_file with file_path: /path/to/query.sql
```

### Sync to Workspace
```
Use sync_to_workspace with:
- local_dir: /path/to/local/notebooks
- workspace_dir: /Workspace/Users/you@company.com/project
```

### Create Workspace Folder
```
Use create_workspace_folder with:
- folder_path: /Workspace/Users/you@company.com/my_project/subfolder
```
