# Databricks Cursor Integration - Instructions

This document provides step-by-step instructions for using the Databricks integration tools in this folder.

## Prerequisites

1. **Activate the virtual environment:**
   ```bash
   cd /Users/visal.kumar/Documents/databricks
   source databricks_env/bin/activate
   cd cursor_databricks
   ```

2. **Verify dependencies are installed:**
   ```bash
   pip list | grep databricks
   ```
   Should show: `databricks-sql-connector`

## Setup (First Time)

If you haven't configured your connection yet, see [SETUP.md](./SETUP.md) for detailed setup instructions.

## Workflow: Before Running Any Scripts

### Step 1: Check Databricks Connection
Always verify the connection works before running any scripts:

```bash
python query_util.py "SELECT 1 as test_connection"
```

**Expected output:** Should show "✓ Connected successfully!" and return a test row.

**If connection fails:**
- Check your internet connection
- Verify Databricks token is valid
- Check if Databricks workspace is accessible

### Step 2: Check Cluster Status
Verify the cluster is active and start if needed:

```bash
python check_cluster.py
```

**Expected outputs:**
- `✓ Cluster is RUNNING. Ready to use!` - Proceed to Step 3
- `⚠️ Cluster is TERMINATED. Starting now...` - Wait 5-10 minutes, then recheck
- `⏳ Cluster is PENDING/RESTARTING` - Wait and recheck

**If cluster fails to start:**
- Check Databricks workspace permissions
- Verify cluster ID is correct
- Contact Databricks admin if issues persist

### Step 3: Execute Your Script
Once connection and cluster are confirmed, run your desired script:

#### For Quick Queries:
```bash
python query_util.py "YOUR_SQL_QUERY_HERE"
```

#### For Interactive SQL:
```bash
python interactive_sql.py
```

#### For SQL Files:
```bash
python run_sql_file.py path/to/your/query.sql show 100
python run_sql_file.py path/to/your/query.sql csv     # Save to CSV
python run_sql_file.py path/to/your/query.sql json    # Save to JSON
```

#### For Creating Tables:
```bash
python create_table.py path/to/your/query.sql schema.table_name
python create_table.py path/to/your/query.sql schema.table_name --drop-if-exists
```

### Step 4: Basic Sense Checks (For Table Creation)

After creating a table, always perform these basic checks:

#### 4.1 Row Count Verification
```bash
python query_util.py "SELECT COUNT(*) as total_rows FROM schema.table_name"
```

#### 4.2 Data Quality Checks
```bash
# Check for NULL values in key columns
python query_util.py "SELECT COUNT(*) as null_count FROM schema.table_name WHERE key_column IS NULL"

# Check distinct values in categorical columns
python query_util.py "SELECT DISTINCT category_column FROM schema.table_name ORDER BY category_column"

# Check date ranges
python query_util.py "SELECT MIN(date_column) as min_date, MAX(date_column) as max_date FROM schema.table_name"
```

#### 4.3 Sample Data Review
```bash
# Review first 5 rows
python query_util.py "SELECT * FROM schema.table_name LIMIT 5"

# Check data distribution
python query_util.py "SELECT column_name, COUNT(*) as count FROM schema.table_name GROUP BY column_name ORDER BY count DESC LIMIT 10"
```

## Common Commands Reference

### Connection & Cluster Management
```bash
# Test connection
python query_util.py "SELECT 1"

# Check cluster status
python check_cluster.py

# Interactive SQL session
python interactive_sql.py
```

### Data Exploration
```bash
# List all tables
python query_util.py "SHOW TABLES"

# Describe table schema
python query_util.py "DESCRIBE schema.table_name"

# Get table info
python query_util.py "SHOW TABLE EXTENDED schema.table_name"
```

### Table Operations
```bash
# Create table from SQL file
python create_table.py query.sql schema.table_name --drop-if-exists

# Export table to CSV
python run_sql_file.py "SELECT * FROM schema.table_name" csv 10000

# Export table to JSON
python run_sql_file.py "SELECT * FROM schema.table_name" json 10000
```

## Troubleshooting

### Connection Issues
- **Error: "Connection timeout"** → Check internet connection, retry
- **Error: "Authentication failed"** → Verify Databricks token
- **Error: "Cluster not found"** → Check cluster ID in scripts

### Cluster Issues
- **Cluster won't start** → Check permissions, contact admin
- **Cluster keeps terminating** → Check auto-termination settings
- **Slow performance** → Consider cluster size/type

### Query Issues
- **Syntax errors** → Validate SQL in Databricks UI first
- **Timeout errors** → Add LIMIT clause, optimize query
- **Memory errors** → Reduce data volume, use filters

## Best Practices

1. **Always follow the workflow:** Connection → Cluster → Execute → Verify
2. **Use LIMIT clauses** for large datasets during exploration
3. **Test queries** in Databricks UI before running scripts
4. **Monitor cluster costs** - terminate when not needed
5. **Keep sensitive data** out of query strings (use parameters)
6. **Document table schemas** and data lineage
7. **Regular backups** of important tables

## File Descriptions

- `config.py` - Centralized connection configuration (update with your credentials)
- `query_util.py` - Main query runner for ad-hoc SQL exploration ⭐
- `interactive_sql.py` - Interactive SQL shell
- `run_sql_file.py` - Execute SQL files with output options
- `create_table.py` - Create/drop tables from SQL files
- `check_cluster.py` - Check cluster status and start if needed
- `SETUP.md` - Connection setup guide
- `QUICK_START.md` - Quick reference for daily usage
- `README.md` - Overview and main documentation
- `INSTRUCTIONS.md` - This file (detailed workflow)

## Support

For issues with:
- **Databricks connectivity** → Check workspace status
- **Cluster management** → Contact Databricks admin
- **SQL syntax** → Use Databricks SQL editor
- **Script bugs** → Check this documentation, review error messages

---

**Remember:** Always verify connection and cluster status before running any scripts!
