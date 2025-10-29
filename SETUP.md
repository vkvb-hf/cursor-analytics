# Databricks Connection Setup Guide

This guide explains how to set up the connection between Cursor IDE and Databricks.

## Prerequisites

1. **Databricks Account**: You need access to a Databricks workspace
2. **Python Environment**: Python 3.7+ installed
3. **Databricks Personal Access Token**: See section below

## Step 1: Create a Databricks Personal Access Token

1. Log in to your Databricks workspace: `https://hf-gp.cloud.databricks.com` (or your workspace URL)
2. Click on your username in the top-right corner
3. Select **Settings** → **User Settings**
4. Go to the **Access Tokens** tab
5. Click **Generate New Token**
6. Give it a description (e.g., "Cursor IDE Access")
7. Click **Generate**
8. **Copy the token immediately** - you won't be able to see it again!

   ⚠️ **Important**: Save this token securely. You'll need it for the connection.

## Step 2: Identify Your Cluster Information

### Option A: Using Databricks UI (Easiest)

1. In Databricks, go to **SQL** → **SQL Warehouses** (or **Compute** → **Clusters**)
2. Find your cluster and click on it
3. In the cluster details, look for:
   - **Server Hostname**: Usually `https://your-workspace.cloud.databricks.com`
   - **HTTP Path**: Found in the connection details tab

### Option B: Extract from JDBC URL

If you have a JDBC connection string, it looks like:
```
jdbc:databricks://<server-hostname>:443/default;transportMode=http;ssl=1;httpPath=<http-path>;AuthMech=3;UID=token;PWD=<token>
```

- **SERVER_HOSTNAME**: Extract the hostname (without `https://`)
- **HTTP_PATH**: The value after `httpPath=` (e.g., `sql/protocolv1/o/4157495209488006/0319-154505-47yntzz2`)

## Step 3: Configure Connection Settings

1. Open `config.py` in this directory
2. Update the following values:

```python
# Databricks Connection Settings
SERVER_HOSTNAME = 'your-workspace.cloud.databricks.com'  # Your Databricks workspace hostname
HTTP_PATH = 'sql/protocolv1/o/YOUR_ORG_ID/YOUR_CLUSTER_ID'  # Your HTTP path
TOKEN = 'dapi...'  # Your personal access token

# Cluster Settings (for cluster management)
CLUSTER_ID = 'YOUR_CLUSTER_ID'  # Your cluster ID
DATABRICKS_HOST = 'https://your-workspace.cloud.databricks.com'  # Full URL to your workspace
```

### Finding Cluster ID

1. Go to **Compute** → **Clusters** in Databricks UI
2. Click on your cluster
3. The cluster ID is in the URL or in the cluster details
   - Format: Usually something like `0319-154505-xxxxx`

### Finding Organization ID (in HTTP_PATH)

The HTTP_PATH typically contains:
- Protocol: `sql/protocolv1/o/`
- Organization ID: `4157495209488006` (8+ digits)
- Cluster ID: `0319-154505-47yntzz2`

Combine them: `sql/protocolv1/o/{ORG_ID}/{CLUSTER_ID}`

## Step 4: Set Up Python Environment

1. Navigate to the databricks directory:
   ```bash
   cd /Users/visal.kumar/Documents/databricks
   ```

2. Create virtual environment (if not already created):
   ```bash
   python3 -m venv databricks_env
   ```

3. Activate the virtual environment:
   ```bash
   source databricks_env/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install databricks-sql-connector[pyarrow]
   pip install requests  # For cluster management
   pip install pandas    # For CSV/JSON export (optional)
   ```

## Step 5: Test the Connection

1. Activate your environment:
   ```bash
   cd /Users/visal.kumar/Documents/databricks
   source databricks_env/bin/activate
   cd cursor_databricks
   ```

2. Run a test query:
   ```bash
   python query_util.py "SELECT 1 as test"
   ```

3. You should see:
   ```
   ✓ Connected successfully!
   ✓ Query completed! (1 rows returned)
   ```

4. Check cluster status:
   ```bash
   python check_cluster.py
   ```

## Troubleshooting

### Connection Timeout

- **Issue**: Connection times out or fails to connect
- **Solutions**:
  1. Verify your cluster is running: `python check_cluster.py`
  2. Check your internet connection
  3. Verify SERVER_HOSTNAME doesn't include `https://` (use hostname only)
  4. Ensure HTTP_PATH is correct (no leading/trailing slashes)

### Authentication Failed

- **Issue**: "Authentication failed" or "Invalid token"
- **Solutions**:
  1. Verify your token is correct in `config.py`
  2. Check if the token has expired (tokens can be set to expire)
  3. Generate a new token if needed
  4. Ensure token has necessary permissions

### Cluster Not Found

- **Issue**: "Cluster not found" or wrong cluster
- **Solutions**:
  1. Verify CLUSTER_ID in `config.py` matches your cluster
  2. Check HTTP_PATH includes the correct cluster ID
  3. Ensure you have access to the cluster

### Import Errors

- **Issue**: `ModuleNotFoundError: No module named 'databricks'`
- **Solutions**:
  1. Ensure virtual environment is activated
  2. Reinstall dependencies: `pip install databricks-sql-connector[pyarrow]`
  3. Check Python version: `python --version` (should be 3.7+)

## Connection Settings Reference

All connection settings are stored in `config.py`:

| Setting | Description | Example |
|---------|-------------|---------|
| `SERVER_HOSTNAME` | Databricks workspace hostname (no https://) | `hf-gp.cloud.databricks.com` |
| `HTTP_PATH` | SQL connector HTTP path | `sql/protocolv1/o/4157495209488006/0319-154505-47yntzz2` |
| `TOKEN` | Personal access token | `dapi23a8938a0795f23be871c979326f63d8` |
| `CLUSTER_ID` | Cluster identifier | `0319-154505-47yntzz2` |
| `DATABRICKS_HOST` | Full workspace URL | `https://hf-gp.cloud.databricks.com` |

## Security Best Practices

1. **Never commit `config.py` to version control** if it contains real tokens
2. Consider using environment variables for sensitive data
3. Rotate tokens periodically
4. Use tokens with minimal required permissions
5. Store tokens securely (password manager, etc.)

## Next Steps

Once your connection is set up, you can:

- **Query tables**: Use `python query_util.py "SELECT * FROM table LIMIT 10"`
- **Run SQL files**: Use `python run_sql_file.py query.sql show 100`
- **Create tables**: Use `python create_table.py query.sql schema.table_name`
- **Interactive SQL**: Use `python interactive_sql.py`

See [README.md](./README.md) for usage examples and [QUICK_START.md](./QUICK_START.md) for daily workflow.

