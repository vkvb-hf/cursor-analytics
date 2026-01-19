# Databricks File Locations

## Where Files Are Saved in Databricks

### 1. Notebook Location
**Notebook file:**
```
/Workspace/Users/visal.kumar@hellofresh.com/long_term_steering_report
```

This is the main notebook that gets created/updated in Databricks workspace.

### 2. Output Files Location

**Output folder (based on latest week):**
```
/Workspace/Users/visal.kumar@hellofresh.com/long-term-steering-{YYYY}-W{ww}
```

**Example from latest run:**
```
/Workspace/Users/visal.kumar@hellofresh.com/long-term-steering-2025-W45
```

**Files in this folder:**
- `detailed_summary_week_vs_prev_week.txt` - Week vs previous week
- `detailed_summary_week_vs_prev_yr_week.txt` - Week vs previous year week
- `detailed_summary_quarter_vs_prev_quarter.txt` - Quarter vs previous quarter

### 3. DBFS Location (Temporary)

Files are also copied to DBFS for easy access:
```
/tmp/detailed_summary_week_vs_prev_week.txt
/tmp/detailed_summary_week_vs_prev_yr_week.txt
/tmp/detailed_summary_quarter_vs_prev_quarter.txt
```

## How to Access Files in Databricks

### Option 1: Via Databricks UI

1. **Open Databricks Workspace**
2. **Navigate to**: `Users` → `visal.kumar@hellofresh.com`
3. **Find folder**: `long-term-steering-2025-W45` (or latest week)
4. **Download files** directly from the UI

### Option 2: Via Workspace API

The `run_long_term_steering.py` script automatically downloads files from:
```
/Workspace/Users/visal.kumar@hellofresh.com/long-term-steering-{week}/{filename}
```

### Option 3: Via DBFS

Files are also available in DBFS:
```python
# In Databricks notebook
dbutils.fs.ls("/tmp/detailed_summary_*.txt")
```

## File Structure in Databricks

```
/Workspace/Users/visal.kumar@hellofresh.com/
├── long_term_steering_report                    # Notebook file
│
└── long-term-steering-2025-W45/                 # Output folder (latest week)
    ├── detailed_summary_week_vs_prev_week.txt
    ├── detailed_summary_week_vs_prev_yr_week.txt
    └── detailed_summary_quarter_vs_prev_quarter.txt
```

## Finding the Latest Files

The folder name includes the week number, so the latest files are in the folder with the highest week number:
- `long-term-steering-2025-W45` (latest)
- `long-term-steering-2025-W44` (previous)
- `long-term-steering-2025-W43` (older)

## Accessing Files Programmatically

### From Python (using Databricks API)

```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()

# List files in workspace folder
workspace_path = "/Workspace/Users/visal.kumar@hellofresh.com/long-term-steering-2025-W45"
files = db.workspace.list(workspace_path)

# Download a file
file_content = db.workspace.export(f"{workspace_path}/detailed_summary_week_vs_prev_week.txt")
```

### From Databricks Notebook

```python
# Read file from workspace
with open('/Workspace/Users/visal.kumar@hellofresh.com/long-term-steering-2025-W45/detailed_summary_week_vs_prev_week.txt', 'r') as f:
    content = f.read()

# Or from DBFS
content = dbutils.fs.head("/tmp/detailed_summary_week_vs_prev_week.txt")
```

## Summary

- **Notebook**: `/Workspace/Users/visal.kumar@hellofresh.com/long_term_steering_report`
- **Output Files**: `/Workspace/Users/visal.kumar@hellofresh.com/long-term-steering-{week}/`
- **DBFS Copy**: `/tmp/{filename}`

All files are automatically downloaded to local `output/` directory when using `run_long_term_steering.py`.

