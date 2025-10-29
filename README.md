# Cursor Databricks Integration

Run SQL queries against Databricks directly from Cursor IDE. Create/drop tables from SQL files and explore data with formatted output.

## 📋 Quick Links

- **[SETUP.md](./SETUP.md)** - Complete connection setup guide (read this first!)
- **[QUICK_START.md](./QUICK_START.md)** - Daily usage workflow
- **[INSTRUCTIONS.md](./INSTRUCTIONS.md)** - Detailed workflow and best practices

## Quick Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vkvb-hf/cursor-databricks.git
   cd cursor-databricks
   ```

2. **Set up connection** (one-time): Follow [SETUP.md](./SETUP.md) to configure your Databricks credentials
   - Copy `config.py.example` to `config.py`
   - Update `config.py` with your Databricks credentials

3. **Activate virtual environment**:
   ```bash
   cd /Users/visal.kumar/Documents/databricks
   source databricks_env/bin/activate
   cd cursor_databricks
   ```

## Main Use Cases

### 1. Query Tables for Exploration

Run SQL queries with formatted output:

```bash
# Quick query with default limit (20 rows)
python query_util.py "SELECT * FROM payments_hf.chargebacks_dashboard LIMIT 10"

# Custom limit
python query_util.py "SELECT * FROM table" --limit 50

# Show all rows
python query_util.py "SELECT * FROM table" --limit 0

# With custom title
python query_util.py "SELECT * FROM table" --title "Chargeback Analysis"
```

### 2. Create/Drop Tables from SQL Files

Create or replace tables using SQL SELECT statements:

```bash
# Create table
python create_table.py path/to/query.sql schema.table_name

# Drop existing table and recreate
python create_table.py path/to/query.sql schema.table_name --drop-if-exists
```

Example:
```bash
python create_table.py ../GitHub/ddi-pays-pipelines/ddi_pays_pipelines/analytics_etl/queries/chargebacks_dashboard.sql payments_hf.chargebacks_dashboard --drop-if-exists
```

### 3. Run SQL Files for Exploration

Execute SQL files with various output formats:

```bash
# Show results in terminal (formatted table)
python run_sql_file.py query.sql show 100

# Save to CSV
python run_sql_file.py query.sql csv

# Save to JSON
python run_sql_file.py query.sql json
```

### 4. Interactive SQL Shell

For exploratory queries and quick testing:

```bash
python interactive_sql.py
```

Then enter SQL queries directly:
```
SQL> SELECT * FROM payments_hf.chargebacks_dashboard LIMIT 5
SQL> SELECT country, COUNT(*) FROM payments_hf.chargebacks_dashboard GROUP BY country
SQL> exit
```

## File Structure

### Core Files

- **`config.py`** - Centralized connection configuration (update this with your credentials)
- **`query_util.py`** - Main query tool with formatted output (⭐ use this for exploration)
- **`create_table.py`** - Create/drop tables from SQL files
- **`run_sql_file.py`** - Execute SQL files with various output formats
- **`check_cluster.py`** - Check cluster status and start if needed

### Interactive Tools

- **`interactive_sql.py`** - Interactive SQL shell for ad-hoc queries

### Documentation

- **`SETUP.md`** - Connection setup instructions
- **`QUICK_START.md`** - Quick reference for daily usage
- **`INSTRUCTIONS.md`** - Detailed workflow and best practices
- **`README.md`** - This file

## Configuration

All connection settings are in `config.py`. To change your connection:

1. Open `config.py`
2. Update:
   - `SERVER_HOSTNAME` - Your Databricks workspace hostname
   - `HTTP_PATH` - SQL connector HTTP path (from SQL Warehouses)
   - `TOKEN` - Your personal access token
   - `CLUSTER_ID` - Your cluster ID
   - `DATABRICKS_HOST` - Full workspace URL

See [SETUP.md](./SETUP.md) for detailed instructions on finding these values.

## Common Workflows

### Before Running Any Scripts

1. **Activate environment**:
   ```bash
   source databricks_env/bin/activate
   cd cursor_databricks
   ```

2. **Check cluster status**:
   ```bash
   python check_cluster.py
   ```

3. **Run your script** (see examples above)

### Creating a Table

```bash
# 1. Check cluster is running
python check_cluster.py

# 2. Create table from SQL file
python create_table.py query.sql payments_hf.my_table --drop-if-exists

# 3. Verify table was created
python query_util.py "SELECT COUNT(*) FROM payments_hf.my_table"
```

### Exploring Data

```bash
# Quick exploration
python query_util.py "SELECT * FROM payments_hf.chargebacks_dashboard LIMIT 10"

# More detailed exploration
python interactive_sql.py
```

## How It Works

This uses the [Databricks SQL Connector for Python](https://docs.databricks.com/aws/en/dev-tools/python-sql-connector) which:
- Connects to your Databricks cluster via HTTP
- Works with any cluster mode (Single User, Shared, User Isolation)
- No need for Databricks Connect version matching
- Simple and reliable

## Troubleshooting

### Connection Issues
- Verify connection settings in `config.py`
- Check cluster is running: `python check_cluster.py`
- Test connection: `python query_util.py "SELECT 1"`

### Import Errors
- Ensure virtual environment is activated
- Reinstall: `pip install databricks-sql-connector[pyarrow]`

### Query Errors
- Validate SQL syntax in Databricks UI first
- Add LIMIT clauses for large datasets
- Check cluster has sufficient resources

See [INSTRUCTIONS.md](./INSTRUCTIONS.md) for more detailed troubleshooting.

## Next Steps

1. **First time setup**: Read [SETUP.md](./SETUP.md)
2. **Daily usage**: See [QUICK_START.md](./QUICK_START.md)
3. **Best practices**: Review [INSTRUCTIONS.md](./INSTRUCTIONS.md)
