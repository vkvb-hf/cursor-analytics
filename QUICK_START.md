# Quick Start Guide

Quick reference for daily Databricks usage from Cursor.

## Setup (One Time)

If you haven't set up your connection yet, see [SETUP.md](./SETUP.md).

```bash
cd /Users/visal.kumar/Documents/databricks
source databricks_env/bin/activate
cd cursor_databricks
```

## Daily Usage

### 1. Query Tables (Exploration)

The main tool for querying tables:

```bash
# Quick query
python query_util.py "SELECT * FROM payments_hf.chargebacks_dashboard LIMIT 10"

# With custom limit
python query_util.py "SELECT country, COUNT(*) as count FROM payments_hf.chargebacks_dashboard GROUP BY country" --limit 5
```

### 2. Create/Drop Tables from SQL Files

Your primary workflow for table management:

```bash
# Create table from SQL file
python create_table.py path/to/query.sql schema.table_name

# Drop and recreate
python create_table.py path/to/query.sql schema.table_name --drop-if-exists
```

Example:
```bash
python create_table.py ../../GitHub/ddi-pays-pipelines/ddi_pays_pipelines/analytics_etl/queries/chargebacks_dashboard.sql payments_hf.chargebacks_dashboard --drop-if-exists
```

### 3. Run SQL Files (Exploration)

Execute SQL files with formatted output or export:

```bash
# Show in terminal (formatted table)
python run_sql_file.py query.sql show 50

# Export to CSV
python run_sql_file.py query.sql csv

# Export to JSON
python run_sql_file.py query.sql json
```

### 4. Interactive SQL Shell

For quick exploration:

```bash
python interactive_sql.py
```

Then type queries:
```
SQL> SELECT * FROM payments_hf.chargebacks_dashboard WHERE country='US' LIMIT 10
SQL> SELECT country, COUNT(*) FROM payments_hf.chargebacks_dashboard GROUP BY country
SQL> exit
```

### 5. Check Cluster Status

Before running large queries:

```bash
python check_cluster.py
```

If cluster is terminated, it will auto-start (may take 5-10 minutes).

## Files Reference

| File | Purpose |
|------|---------|
| `query_util.py` | ⭐ Main query tool - use for exploration |
| `create_table.py` | Create/drop tables from SQL files |
| `run_sql_file.py` | Run SQL files with output options |
| `interactive_sql.py` | Interactive SQL shell |
| `check_cluster.py` | Check/manage cluster status |
| `config.py` | Connection settings (edit to change connection) |

## Configuration

Connection details are in `config.py`. Currently configured for:
- **Workspace**: https://hf-gp.cloud.databricks.com
- **Cluster**: analytics-all-purpose-vkvb (0319-154505-47yntzz2)

To change connection, edit `config.py` or see [SETUP.md](./SETUP.md).

## Tips

- ✅ Use `query_util.py` for quick table exploration
- ✅ Use `create_table.py` for creating tables from SQL files
- ✅ Check cluster status before large queries
- ✅ Use `--limit` flag to control output size
- ✅ Use `interactive_sql.py` for iterative exploration

## Troubleshooting

**Connection timeout**: Cluster may be starting. Run `python check_cluster.py`

**Query hangs**: Check cluster is RUNNING state

**Import errors**: Make sure virtual environment is activated (`source databricks_env/bin/activate`)

**See [INSTRUCTIONS.md](./INSTRUCTIONS.md) for detailed troubleshooting**
