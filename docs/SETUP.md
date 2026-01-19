# Setup Guide

Complete setup instructions for cursor-analytics.

## Prerequisites

- Python 3.9+
- Databricks workspace access
- Personal Access Token (PAT)

## Quick Setup

### 1. Clone and Install

```bash
cd /Users/visal.kumar/Documents/databricks/cursor-analytics
pip install -e .
```

### 2. Configure Databricks Connection

Create `.env` file in `mcp/databricks/`:

```bash
# mcp/databricks/.env
DATABRICKS_HOST=https://your-workspace.cloud.databricks.com
DATABRICKS_TOKEN=dapi_your_token_here
DATABRICKS_HTTP_PATH=/sql/1.0/warehouses/your-warehouse-id
DATABRICKS_SERVER_HOSTNAME=your-workspace.cloud.databricks.com
CLUSTER_ID=your-cluster-id
```

### 3. Configure MCP in Cursor

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "databricks": {
      "command": "/path/to/python",
      "args": ["/path/to/cursor-analytics/mcp/databricks/server.py"],
      "cwd": "/path/to/cursor-analytics/mcp/databricks"
    }
  }
}
```

### 4. Restart Cursor

Restart Cursor IDE to load the MCP server.

### 5. Verify Setup

Run the smoke test:

```bash
python scripts/smoke_test.py --quick
```

---

## Detailed Configuration

### Getting Your Databricks Credentials

#### Personal Access Token (PAT)

1. Log in to Databricks workspace
2. Click username → **Settings** → **Developer**
3. Click **Manage** under Access Tokens
4. Click **Generate New Token**
5. Copy the token immediately (shown only once)

#### Server Hostname

Found in your workspace URL: `https://<hostname>.cloud.databricks.com`

#### HTTP Path

1. Go to **SQL Warehouses** in Databricks
2. Click on your warehouse
3. Go to **Connection Details** tab
4. Copy the **HTTP Path**

#### Cluster ID

1. Go to **Compute** → **Clusters**
2. Click on your cluster
3. Find the cluster ID in the URL or details panel

---

## Environment Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABRICKS_HOST` | Full workspace URL | `https://hf-gp.cloud.databricks.com` |
| `DATABRICKS_TOKEN` | Personal access token | `dapi23a8938a...` |
| `DATABRICKS_HTTP_PATH` | SQL warehouse path | `/sql/1.0/warehouses/abc123` |
| `DATABRICKS_SERVER_HOSTNAME` | Hostname only | `hf-gp.cloud.databricks.com` |
| `CLUSTER_ID` | Cluster identifier | `0319-154505-47yntzz2` |

---

## Google Sheets MCP (Optional)

### 1. Create Service Account

1. Go to Google Cloud Console
2. Create a service account
3. Download JSON key file
4. Share your sheets with the service account email

### 2. Configure

```bash
# mcp/google_sheets/.env
GOOGLE_SERVICE_ACCOUNT_FILE=/path/to/service-account.json
```

### 3. Add to MCP Config

```json
{
  "mcpServers": {
    "google-sheets": {
      "command": "/path/to/python",
      "args": ["/path/to/cursor-analytics/mcp/google_sheets/server.py"],
      "cwd": "/path/to/cursor-analytics/mcp/google_sheets",
      "env": {
        "GOOGLE_SERVICE_ACCOUNT_FILE": "/path/to/service-account.json"
      }
    }
  }
}
```

---

## Troubleshooting

### Connection Timeout

- Verify cluster is running in Databricks UI
- Check `DATABRICKS_HOST` doesn't have trailing slash
- Ensure `DATABRICKS_HTTP_PATH` is correct

### Authentication Failed

- Regenerate PAT if expired
- Verify token is copied correctly (no extra spaces)
- Check token has required permissions

### MCP Not Loading

- Check `~/.cursor/mcp.json` syntax (valid JSON)
- Verify Python path is correct
- Check MCP server logs in Cursor

### Import Errors

```bash
# Reinstall in editable mode
pip install -e .

# Or install dependencies directly
pip install -r requirements.txt
```

---

## Next Steps

Once setup is complete:

1. Use MCP tools via Cursor for SQL queries
2. See `.cursorrules` for usage patterns
3. Run `python scripts/smoke_test.py` to verify everything works
