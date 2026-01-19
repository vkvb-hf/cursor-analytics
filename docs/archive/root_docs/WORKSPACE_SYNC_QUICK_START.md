# Workspace Sync - Quick Start

## Your Use Case: Create Notebooks → Run Jobs → See Changes

### Step 1: Create Notebooks Locally

```bash
# Create a directory for your notebooks
mkdir -p ~/databricks_notebooks
cd ~/databricks_notebooks

# Create a notebook file
cat > my_analysis.py << 'EOF'
# Databricks notebook source
# MAGIC %md
# MAGIC # My Analysis Notebook

# MAGIC %sql
# MAGIC SELECT * FROM my_table LIMIT 10
EOF
```

### Step 2: Sync to Databricks Workspace

```bash
cd /Users/visal.kumar/Documents/databricks/cursor_databricks

python databricks_cli.py sync to_workspace \
  --local-dir ~/databricks_notebooks \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com/notebooks
```

**Output:**
```
📤 Syncing local files to workspace...
   Local: /Users/visal.kumar/databricks_notebooks
   Workspace: /Workspace/Users/visal.kumar@hellofresh.com/notebooks
   Pattern: **/*.py
   ✅ my_analysis.py -> /Workspace/Users/visal.kumar@hellofresh.com/notebooks/my_analysis.py

📊 Sync complete: 1 succeeded, 0 failed
```

### Step 3: Run as Job

```bash
python databricks_cli.py notebook run \
  /Workspace/Users/visal.kumar@hellofresh.com/notebooks/my_analysis \
  --file ~/databricks_notebooks/my_analysis.py \
  --job-name "My Analysis Job"
```

### Step 4: View in Databricks UI

1. Open Databricks workspace
2. Navigate to: `/Workspace/Users/visal.kumar@hellofresh.com/notebooks/my_analysis`
3. See your notebook with all changes!

## Auto-Sync Mode (Recommended for Development)

Watch for changes and automatically sync:

```bash
# Terminal 1: Start watch mode
python databricks_cli.py sync watch \
  --local-dir ~/databricks_notebooks \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com/notebooks

# Terminal 2: Edit your notebooks
# Changes are automatically synced to workspace!
```

## Common Commands

```bash
# Sync local → workspace
python databricks_cli.py sync to_workspace \
  --local-dir ~/databricks_notebooks \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com/notebooks

# Sync workspace → local
python databricks_cli.py sync from_workspace \
  --local-dir ~/databricks_notebooks \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com/notebooks

# Watch mode (auto-sync)
python databricks_cli.py sync watch \
  --local-dir ~/databricks_notebooks \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com/notebooks

# Preview what would be synced
python databricks_cli.py sync to_workspace \
  --local-dir ~/databricks_notebooks \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com/notebooks \
  --dry-run
```

## Using Python API

```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()

# Sync to workspace
result = db.sync_to_workspace(
    local_dir="~/databricks_notebooks",
    workspace_dir="/Workspace/Users/visal.kumar@hellofresh.com/notebooks"
)

# Run notebook as job
result = db.run_notebook_job(
    notebook_path="/Workspace/Users/visal.kumar@hellofresh.com/notebooks/my_analysis",
    notebook_content=open("~/databricks_notebooks/my_analysis.py").read(),
    job_name="My Analysis"
)
```

## See Full Documentation

For complete documentation, see: [docs/guides/WORKSPACE_SYNC.md](docs/guides/WORKSPACE_SYNC.md)






