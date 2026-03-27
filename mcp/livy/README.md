# Livy MCP Server

Submit and manage Livy jobs for `ddi-pays-pipelines`.

## Setup

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "livy-jobs": {
      "type": "stdio",
      "command": "uv",
      "args": ["run", "--directory", "/Users/visal.kumar/Documents/GitHub/utlis/livy-mcp", "python", "livy_mcp_server.py"],
      "cwd": "/Users/visal.kumar/Documents/GitHub/utlis/livy-mcp"
    }
  }
}
```

## Tools (6)

| Tool | Purpose |
|------|---------|
| `submit_analytics_etl` | Analytics ETLs (`ddi_pays_pipelines.analytics_etl`) |
| `submit_generic_etl` | Generic ETLs (`ddi_pays_pipelines.generic_etl_runner`) |
| `submit_generic_etl_batch` | Backfill over date ranges in batches |
| `get_livy_batches` | List recent jobs on a cluster |
| `get_batch_status` | Check specific job status |
| `kill_batch` | Cancel a running job |

## Reference

**EMR Hosts:** `live-01`, `live-02`, `live-03`, `live-04`

**Spark Profiles:**
- `analytics` - 12g driver/executor
- `generic_etl` - 16g driver, 32g executor (default)
- `generic_etl_heavy` - 32g driver, 64g executor
