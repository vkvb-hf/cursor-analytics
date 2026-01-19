# How to Effectively Use the cursor_databricks Folder

## Quick Start Guide

### 1. Always Use Virtual Environment

**CRITICAL**: Always activate the virtual environment before running any scripts.

```bash
# Navigate to databricks directory
cd /path/to/databricks

# Activate virtual environment
source databricks_env/bin/activate

# You should see (databricks_env) in your prompt
```

**Why?** The virtual environment contains all required dependencies (requests, databricks-sql-connector, pandas, etc.). Without it, you'll get `ModuleNotFoundError`.

### 2. Configuration Setup

**Required**: Set up `config.py` with your Databricks credentials.

```bash
# Copy example config
cp config.py.example config.py

# Edit config.py with your credentials:
# - SERVER_HOSTNAME: Your workspace hostname
# - HTTP_PATH: SQL warehouse HTTP path
# - TOKEN: Personal access token
# - DATABRICKS_HOST: Full workspace URL
# - CLUSTER_ID: Your cluster ID
```

**Security**: Never commit `config.py` to version control if it contains real credentials!

### 3. Core Functionality

#### Run SQL Queries

**From SQL file:**
```bash
cd cursor_databricks
python scripts/run_sql.py queries/my_query.sql csv 1000
```

**Interactive SQL shell:**
```bash
python scripts/interactive_sql.py
```

#### Run Databricks Notebooks as Jobs

```bash
cd cursor_databricks
python scripts/run_notebook.py /path/to/notebook.py "Job Name"
```

#### Upload CSV Files to Workspace

```bash
python scripts/upload_csvs.py /path/to/csvs/ /Workspace/path/destination/
```

### 4. Long Term Steering Report Project

**Location**: `projects/long_term_steering_report/`

**To run the steering report:**

```bash
# 1. Activate virtual environment
source databricks_env/bin/activate

# 2. Navigate to project
cd cursor_databricks/projects/long_term_steering_report

# 3. Run all comparison types
python run_long_term_steering.py

# Or run specific comparison types
python run_long_term_steering.py week_yoy quarter_prev
```

**Output:**
- Files are generated in Databricks workspace: `/Workspace/Users/visal.kumar@hellofresh.com/long-term-steering-{week}/`
- Files are automatically downloaded to local `output/` directory

**Comparison Types:**
- `week_prev`: Current week vs previous week
- `week_yoy`: Current week vs previous year same week
- `quarter_prev`: Current quarter (last 13 weeks) vs previous quarter

### 5. Project Structure

```
cursor_databricks/
├── core/                    # Core modules
│   ├── databricks_job_runner.py
│   ├── table_inspector.py
│   ├── query_util.py
│   └── ...
├── scripts/                 # Executable scripts
│   ├── run_sql.py
│   ├── interactive_sql.py
│   └── ...
├── queries/                 # SQL query files
├── projects/                # Project-specific code
│   └── long_term_steering_report/
│       ├── long_term_steering_report.py  # Main notebook
│       ├── run_long_term_steering.py     # Runner script
│       └── output/                        # Generated reports
├── tests/                   # Test files
├── config.py               # Configuration (not in git)
├── requirements.txt        # Dependencies
└── README.md               # Main documentation
```

### 6. Common Tasks

#### Test Imports

```bash
cd cursor_databricks
python tests/test_manual.py
```

#### Run Integration Tests

```bash
cd cursor_databricks
pytest tests/
```

#### Check Table Schema

```python
from core.table_inspector import TableInspector
inspector = TableInspector()
inspector.inspect_table("schema.table_name")
```

#### Run a Query and Get Results

```python
from core.query_util import run_query, print_table
results = run_query("SELECT * FROM table LIMIT 10")
print_table(results)
```

### 7. Troubleshooting

#### "ModuleNotFoundError: No module named 'requests'"
**Solution**: Activate virtual environment:
```bash
source databricks_env/bin/activate
```

#### "ImportError: No module named 'config'"
**Solution**: Make sure you're in the `cursor_databricks` directory and `config.py` exists.

#### "Failed to create notebook"
**Solution**: Check your Databricks credentials in `config.py`:
- Verify `DATABRICKS_HOST` is correct
- Verify `TOKEN` is valid
- Verify `CLUSTER_ID` exists

#### Files not persisting in Databricks workspace
**Solution**: The code now includes explicit file flush and sync. If issues persist:
- Check job logs for errors
- Verify file paths are correct
- Check workspace permissions

### 8. Best Practices

1. **Always use virtual environment** - Prevents dependency conflicts
2. **Test locally first** - Use `test_manual.py` to verify imports
3. **Check job logs** - Databricks UI shows detailed execution logs
4. **Use output/ directory** - Generated files are automatically organized
5. **Read README files** - Each project has its own documentation

### 9. Key Files Reference

- **Main README**: `README.md` - Overview of entire repository
- **Project README**: `projects/long_term_steering_report/README.md` - Steering report docs
- **Usage Guide**: `projects/long_term_steering_report/USAGE.md` - Detailed usage
- **File Locations**: `projects/long_term_steering_report/DATABRICKS_FILE_LOCATIONS.md` - Where files are saved

### 10. Workflow Example

**Complete workflow for running steering report:**

```bash
# 1. Activate environment
cd /Users/visal.kumar/Documents/databricks
source databricks_env/bin/activate

# 2. Navigate to project
cd cursor_databricks/projects/long_term_steering_report

# 3. Run report
python run_long_term_steering.py

# 4. Check results
ls -lh output/

# 5. Verify files in Databricks (optional)
# Check: https://hf-gp.cloud.databricks.com/#workspace/Users/visal.kumar@hellofresh.com/long-term-steering-2025-W45
```

### 11. Important Notes

- **Virtual environment is required** - Don't skip this step!
- **Config must be set up** - Without valid credentials, nothing will work
- **Files are auto-downloaded** - Check `output/` directory after running
- **Jobs run sequentially** - There's a 5-second delay between runs
- **All files persist** - The fix ensures all 3 comparison files are saved

### 12. Getting Help

1. Check the relevant README file
2. Review job logs in Databricks UI
3. Check `tests/` directory for examples
4. Review `FILE_PERSISTENCE_ISSUE.md` if files aren't appearing

---

## Quick Reference Card

```bash
# Setup
source databricks_env/bin/activate
cd cursor_databricks

# Run SQL
python scripts/run_sql.py queries/my_query.sql csv 1000

# Run Steering Report
cd projects/long_term_steering_report
python run_long_term_steering.py

# Test
python tests/test_manual.py
```

**Remember**: Always activate virtual environment first! 🐍

