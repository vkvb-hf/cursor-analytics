# MCP Tools Guide

Complete reference for all MCP tools available in cursor-analytics.

---

## Databricks MCP (7 Tools)

### execute_sql

Execute any SQL query on Databricks.

**Parameters:**
- `query` (required): SQL query to execute
- `limit` (optional): Max rows to return (default: 100)

**Returns:** JSON with `success`, `row_count`, `columns`, `data[]`, `execution_time_ms`

**Examples:**

```sql
-- List tables
SHOW TABLES IN payments_hf

-- Describe table
DESCRIBE payments_hf.chargebacks_dashboard

-- Sample data
SELECT * FROM payments_hf.chargebacks_dashboard LIMIT 10

-- Find duplicates
SELECT psp_reference, COUNT(*) as cnt 
FROM payments_hf.chargebacks_dashboard 
GROUP BY psp_reference 
HAVING COUNT(*) > 1

-- Profile column
SELECT 
  COUNT(*) as total,
  COUNT(status) as non_null,
  COUNT(DISTINCT status) as unique_values
FROM payments_hf.chargebacks_dashboard

-- Create table
CREATE TABLE analytics.my_analysis AS
SELECT * FROM source_table WHERE condition
```

---

### run_sql_file

Execute SQL from a local .sql file.

**Parameters:**
- `file_path` (required): Path to the SQL file
- `output_format` (optional): `json` (default) or `show` (text)
- `limit` (optional): Max rows to return (default: 100)

**Returns:** JSON with `success`, `row_count`, `columns`, `data[]`, `file_path`

**Example:**
```
file_path: /path/to/query.sql
output_format: json
limit: 500
```

---

### create_notebook

Create a Python notebook in Databricks workspace.

**Parameters:**
- `notebook_path` (required): Path in Databricks workspace
- `content` (required): Python notebook content
- `overwrite` (optional): Overwrite if exists (default: true)

**Returns:** JSON with `success`, `notebook_path`, `action`

**Example:**
```python
notebook_path: /Workspace/Users/user@company.com/my_analysis
content: |
  # Databricks notebook source
  # MAGIC %md
  # MAGIC # My Analysis
  
  # COMMAND ----------
  
  df = spark.sql("SELECT * FROM table")
  display(df)
overwrite: true
```

---

### run_notebook

Create and run a notebook as a Databricks job. Waits for completion.

**Parameters:**
- `notebook_path` (required): Path in Databricks workspace
- `notebook_content` (required): Python notebook content
- `job_name` (required): Name for the Databricks job

**Returns:** JSON with `success`, `job_id`, `run_id`, `state`, `result_state`, `outputs[]`

**Example:**
```
notebook_path: /Workspace/Users/user@company.com/analysis_job
notebook_content: <notebook content>
job_name: Weekly Analysis Job
```

---

### get_job_status

Check the status of a Databricks job run.

**Parameters:**
- `run_id` (required): Databricks job run ID

**Returns:** JSON with `success`, `run_id`, `life_cycle_state`, `result_state`, `is_running`, `is_complete`, `is_success`

**States:**
- `life_cycle_state`: PENDING, RUNNING, TERMINATING, TERMINATED, SKIPPED, INTERNAL_ERROR
- `result_state`: SUCCESS, FAILED, TIMEDOUT, CANCELED

---

### sync_to_workspace

Upload local files to Databricks workspace.

**Parameters:**
- `local_dir` (required): Local directory path
- `workspace_dir` (required): Databricks workspace directory
- `pattern` (optional): File pattern (default: `**/*.py`)
- `dry_run` (optional): Preview without uploading (default: false)

**Returns:** JSON with `success`, `files_synced`, `local_dir`, `workspace_dir`

---

### sync_from_workspace

Download files from Databricks workspace to local directory.

**Parameters:**
- `local_dir` (required): Local directory path
- `workspace_dir` (required): Databricks workspace directory
- `dry_run` (optional): Preview without downloading (default: false)

**Returns:** JSON with `success`, `files_synced`, `local_dir`, `workspace_dir`

---

## Google Sheets MCP (4 Tools)

### read_sheet

Read data from a Google Sheet.

**Parameters:**
- `spreadsheet_id` (required): The ID from the sheet URL
- `range_name` (optional): A1 notation range (default: "Sheet1")

**Returns:** JSON with `success`, `headers`, `row_count`, `data[]`

---

### get_sheet_info

Get spreadsheet metadata (sheet names, dimensions).

**Parameters:**
- `spreadsheet_id` (required): The ID from the sheet URL

**Returns:** JSON with `success`, `spreadsheet_title`, `sheets[]`

---

### read_multiple_ranges

Read multiple ranges from a sheet at once.

**Parameters:**
- `spreadsheet_id` (required): The ID from the sheet URL
- `ranges` (required): List of A1 notation ranges

**Returns:** JSON with `success`, `ranges{}`

---

### read_comments

Extract cell comments from a sheet.

**Parameters:**
- `spreadsheet_id` (required): The ID from the sheet URL
- `sheet_name` (optional): Specific sheet name
- `range_name` (optional): A1 notation range

**Returns:** JSON with `success`, `comment_count`, `comments[]`

---

## External MCPs

### Atlassian (28 tools)

Configured via `mcp.atlassian.com`. Tools for:
- Jira: Create/update issues, search, transitions
- Confluence: Create/read pages, search

### Atlan (12 tools)

Configured via `hellofresh.atlan.com/mcp`. Tools for:
- Data catalog search
- Lineage exploration
- Metadata management

### GitHub (26 tools)

NPM package `@modelcontextprotocol/server-github`. Tools for:
- Repository operations
- Pull requests
- Issues
- Code search

---

## Response Format

All tools return structured JSON:

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

On error:
```json
{
  "success": false,
  "error": "Error message",
  "tool": "execute_sql",
  "arguments": {...}
}
```

---

## Best Practices

1. **Always add LIMIT** to SELECT queries for exploration
2. **Use structured output** - parse JSON responses
3. **Check success field** before processing data
4. **Use run_sql_file** for complex queries stored in files
5. **Use run_notebook** for Spark-based analysis (large data)
6. **Use dry_run** before sync operations
