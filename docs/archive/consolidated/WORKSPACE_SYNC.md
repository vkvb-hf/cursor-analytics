# Workspace Sync Guide

Complete guide for syncing files between your local environment and Databricks workspace.

## Overview

The workspace sync utility enables bidirectional synchronization between your local filesystem and Databricks workspace. This allows you to:

1. **Create notebooks locally** - Edit notebooks in your favorite editor
2. **Sync to Databricks** - Automatically upload changes to workspace
3. **Run as jobs** - Execute notebooks using Databricks jobs
4. **See changes** - View updated notebooks in Databricks UI

## Quick Start

### 1. Basic Sync (One-time)

**Sync local files to workspace:**
```bash
python databricks_cli.py sync to_workspace \
  --local-dir ./notebooks \
  --workspace-dir /Workspace/Users/your.email@example.com/notebooks
```

**Sync workspace files to local:**
```bash
python databricks_cli.py sync from_workspace \
  --local-dir ./notebooks \
  --workspace-dir /Workspace/Users/your.email@example.com/notebooks
```

### 2. Watch Mode (Auto-sync)

Watch for file changes and automatically sync to workspace:

```bash
python databricks_cli.py sync watch \
  --local-dir ./notebooks \
  --workspace-dir /Workspace/Users/your.email@example.com/notebooks \
  --pattern "**/*.py"
```

Press `Ctrl+C` to stop watching.

### 3. Dry Run (Preview)

See what would be synced without actually syncing:

```bash
python databricks_cli.py sync to_workspace \
  --local-dir ./notebooks \
  --workspace-dir /Workspace/Users/your.email@example.com/notebooks \
  --dry-run
```

## Complete Workflow

### Step 1: Create Notebooks Locally

Create your notebooks in a local directory:

```bash
mkdir -p notebooks
cd notebooks

# Create a notebook file
cat > my_analysis.py << 'EOF'
# Databricks notebook source
# MAGIC %md
# MAGIC # My Analysis

# MAGIC %sql
# MAGIC SELECT * FROM my_table LIMIT 10
EOF
```

### Step 2: Sync to Workspace

Upload your notebooks to Databricks:

```bash
cd /path/to/databricks/cursor_databricks
python databricks_cli.py sync to_workspace \
  --local-dir ~/notebooks \
  --workspace-dir /Workspace/Users/your.email@example.com/notebooks
```

### Step 3: Run as Job

Now you can run the notebook as a job:

```bash
python databricks_cli.py notebook run \
  /Workspace/Users/your.email@example.com/notebooks/my_analysis \
  --file ~/notebooks/my_analysis.py \
  --job-name "My Analysis Job"
```

### Step 4: View in Databricks UI

Open Databricks workspace and navigate to:
```
/Workspace/Users/your.email@example.com/notebooks/my_analysis
```

You'll see your notebook with all changes synced!

## Using Python API

### Basic Usage

```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()

# Sync local files to workspace
result = db.sync_to_workspace(
    local_dir="./notebooks",
    workspace_dir="/Workspace/Users/your.email@example.com/notebooks",
    pattern="**/*.py"
)

print(f"Synced {len(result['success'])} files")
```

### Advanced Usage

```python
from core.workspace_sync import WorkspaceSync

# Create sync instance
sync = WorkspaceSync(
    local_dir="./notebooks",
    workspace_dir="/Workspace/Users/your.email@example.com/notebooks"
)

# Upload a specific file
result = sync.upload_file(
    local_path=Path("./notebooks/my_notebook.py"),
    workspace_path="/Workspace/Users/your.email@example.com/notebooks/my_notebook"
)

# Download a specific file
result = sync.download_file(
    workspace_path="/Workspace/Users/your.email@example.com/notebooks/my_notebook",
    local_path=Path("./notebooks/my_notebook.py")
)

# List workspace files
files = sync.list_workspace_files()
for file in files:
    print(file)
```

## File Patterns

Control which files are synced using glob patterns:

```bash
# Sync only Python files
--pattern "**/*.py"

# Sync Python and SQL files
--pattern "**/*.{py,sql}"

# Sync all files in notebooks directory
--pattern "notebooks/**/*"

# Sync specific file
--pattern "my_notebook.py"
```

## Supported File Types

The sync utility automatically detects file types and sets the correct Databricks language:

- `.py` → Python notebooks
- `.sql` → SQL notebooks
- `.scala` → Scala notebooks
- `.r` → R notebooks

## Best Practices

### 1. Organize Your Workspace

Create a clear directory structure:

```
/Workspace/Users/your.email@example.com/
├── notebooks/          # Your notebooks
├── projects/           # Project-specific notebooks
└── shared/             # Shared notebooks
```

### 2. Use Watch Mode During Development

When actively developing, use watch mode:

```bash
# Terminal 1: Watch and auto-sync
python databricks_cli.py sync watch \
  --local-dir ./notebooks \
  --workspace-dir /Workspace/Users/your.email@example.com/notebooks

# Terminal 2: Edit your notebooks
# Changes are automatically synced!
```

### 3. Version Control

Keep your local notebooks in version control:

```bash
git init
git add notebooks/
git commit -m "Initial notebooks"
```

### 4. Dry Run Before Major Syncs

Always preview what will be synced:

```bash
python databricks_cli.py sync to_workspace \
  --local-dir ./notebooks \
  --workspace-dir /Workspace/Users/your.email@example.com/notebooks \
  --dry-run
```

## Troubleshooting

### Files Not Syncing

**Check file permissions:**
```bash
ls -la notebooks/
```

**Check workspace path:**
- Ensure workspace path starts with `/Workspace/`
- Verify your user path is correct

**Check authentication:**
```bash
python databricks_cli.py sql --query "SELECT 1"
```

### Watch Mode Not Detecting Changes

- Ensure you're editing files in the watched directory
- Check that file pattern matches your files
- Try increasing the watch interval (modify code if needed)

### Sync Conflicts

If a file exists in both locations:
- Local → Workspace: Local file overwrites workspace file
- Workspace → Local: Workspace file overwrites local file

**Recommendation:** Use version control to track changes and resolve conflicts.

## Examples

### Example 1: Daily Development Workflow

```bash
# 1. Start watch mode in background
python databricks_cli.py sync watch \
  --local-dir ~/projects/my_project/notebooks \
  --workspace-dir /Workspace/Users/your.email@example.com/my_project/notebooks &

# 2. Edit notebooks locally
# 3. Changes automatically sync to workspace
# 4. Run jobs as needed
python databricks_cli.py notebook run \
  /Workspace/Users/your.email@example.com/my_project/notebooks/analysis \
  --file ~/projects/my_project/notebooks/analysis.py \
  --job-name "Daily Analysis"
```

### Example 2: One-time Sync

```bash
# Sync all notebooks to workspace
python databricks_cli.py sync to_workspace \
  --local-dir ./notebooks \
  --workspace-dir /Workspace/Users/your.email@example.com/notebooks \
  --pattern "**/*.py"
```

### Example 3: Download Existing Notebooks

```bash
# Download all notebooks from workspace
python databricks_cli.py sync from_workspace \
  --local-dir ./notebooks_backup \
  --workspace-dir /Workspace/Users/your.email@example.com/notebooks
```

## Integration with Jobs

After syncing notebooks, you can run them as jobs:

```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()

# 1. Sync notebooks
db.sync_to_workspace(
    local_dir="./notebooks",
    workspace_dir="/Workspace/Users/your.email@example.com/notebooks"
)

# 2. Run notebook as job
result = db.run_notebook_job(
    notebook_path="/Workspace/Users/your.email@example.com/notebooks/my_analysis",
    notebook_content=open("./notebooks/my_analysis.py").read(),
    job_name="My Analysis"
)
```

## See Also

- [Quick Start Guide](QUICK_START.md)
- [Notebook Creation Guide](HOW_TO_CREATE_AND_RUN_NOTEBOOKS.md)
- [CLI Reference](../README.md)






