# Solution: Capturing Notebook Output in Terminal

## Current Limitation

The Databricks Jobs API `get-output` endpoint **does not capture stdout/stderr** from:
- `print()` statements
- `DataFrame.show()` output
- Any console output

The output is visible in the UI but returns empty `{}` via the API.

## Solution: Configure Cluster Log Delivery

To see notebook execution output (including print statements and DataFrame.show()) in the terminal, you need to:

### 1. Configure Cluster to Write Logs to DBFS

When creating/editing the cluster used for jobs:
1. Go to Cluster Configuration → Advanced Options → Logging
2. Enable "Cluster Log Delivery"
3. Set destination to: `dbfs:/cluster-logs/{cluster-id}/`
4. Save cluster configuration

### 2. Update Script to Read Logs from DBFS

Once configured, the script will automatically:
- Wait for job completion
- Read stdout/stderr logs from DBFS
- Display the output in terminal

## Alternative: Use SQL Queries Instead

For SQL queries, you can:
- Use `%sql` magic commands (but output still not captured)
- Or use the SQL API directly (which we already do as fallback)

## Current Status

The script now:
1. ✅ Creates notebook
2. ✅ Submits as job
3. ✅ Monitors execution
4. ✅ Attempts to retrieve output via API
5. ⚠️  Output is empty (API limitation)
6. ⚠️  Cluster logs not configured (404 error)

**To enable output capture: Configure cluster log delivery to DBFS.**


