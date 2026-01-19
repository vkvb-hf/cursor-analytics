# Full Workspace Sync Guide

## Sync Entire Workspace

Sync your entire Databricks workspace to local:

**From:** `/Workspace/Users/visal.kumar@hellofresh.com/`  
**To:** `/Users/visal.kumar/Documents/databricks/visal.kumar@hellofresh.com/`

## Quick Start

### Option 1: Use the Helper Script (Easiest)

```bash
cd /Users/visal.kumar/Documents/databricks/cursor_databricks
python sync_full_workspace.py
```

This will:
1. Download all files from your workspace
2. Save them to the local directory
3. Show a summary of what was synced

### Option 2: Use CLI Directly

```bash
cd /Users/visal.kumar/Documents/databricks/cursor_databricks

# Download everything from workspace
python databricks_cli.py sync from_workspace \
  --local-dir /Users/visal.kumar/Documents/databricks/visal.kumar@hellofresh.com \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com
```

### Option 3: Use Python API

```python
from databricks_api import DatabricksAPI

db = DatabricksAPI()

# Download entire workspace
result = db.sync_from_workspace(
    local_dir="/Users/visal.kumar/Documents/databricks/visal.kumar@hellofresh.com",
    workspace_dir="/Workspace/Users/visal.kumar@hellofresh.com"
)

print(f"Synced {len(result['success'])} files")
```

## Bidirectional Sync

### Upload Local → Workspace

```bash
# Upload all local files to workspace
python databricks_cli.py sync to_workspace \
  --local-dir /Users/visal.kumar/Documents/databricks/visal.kumar@hellofresh.com \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com \
  --pattern "**/*"
```

### Download Workspace → Local

```bash
# Download all workspace files to local
python databricks_cli.py sync from_workspace \
  --local-dir /Users/visal.kumar/Documents/databricks/visal.kumar@hellofresh.com \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com
```

## Watch Mode (Auto-Sync)

Watch for changes and automatically sync:

```bash
# Watch workspace and sync to local
python databricks_cli.py sync watch \
  --local-dir /Users/visal.kumar/Documents/databricks/visal.kumar@hellofresh.com \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com \
  --direction from_workspace

# Or watch local and sync to workspace
python databricks_cli.py sync watch \
  --local-dir /Users/visal.kumar/Documents/databricks/visal.kumar@hellofresh.com \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com \
  --direction to_workspace
```

## Directory Structure

After syncing, your local directory will mirror your workspace:

```
/Users/visal.kumar/Documents/databricks/visal.kumar@hellofresh.com/
├── long_term_steering_report          # Notebook
├── notebooks/                          # If you have a notebooks folder
├── [other files and folders from workspace]
└── ...
```

## What Gets Synced?

- ✅ **Notebooks** (`.py`, `.sql`, `.scala`, `.r`)
- ✅ **Files** (any text files)
- ✅ **Folders** (directory structure is preserved)
- ❌ **Binary files** (may not sync correctly - notebooks are text-based)

## Best Practices

### 1. Initial Sync

First time syncing? Download everything first:

```bash
python sync_full_workspace.py
```

### 2. Regular Updates

For regular updates, you can:

**Option A: Manual sync when needed**
```bash
python databricks_cli.py sync from_workspace \
  --local-dir /Users/visal.kumar/Documents/databricks/visal.kumar@hellofresh.com \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com
```

**Option B: Watch mode (for active development)**
```bash
# Keep this running in a terminal
python databricks_cli.py sync watch \
  --local-dir /Users/visal.kumar/Documents/databricks/visal.kumar@hellofresh.com \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com \
  --direction from_workspace
```

### 3. Version Control

Add your synced workspace to git:

```bash
cd /Users/visal.kumar/Documents/databricks/visal.kumar@hellofresh.com
git init
git add .
git commit -m "Initial workspace sync"
```

### 4. Dry Run (Preview)

See what would be synced without actually syncing:

```bash
python databricks_cli.py sync from_workspace \
  --local-dir /Users/visal.kumar/Documents/databricks/visal.kumar@hellofresh.com \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com \
  --dry-run
```

## Troubleshooting

### Large Workspace

If your workspace is very large:
- First sync might take a while
- Consider syncing specific folders instead
- Use `--pattern` to filter files

### Conflicts

If files exist in both locations:
- **Workspace → Local**: Workspace files overwrite local files
- **Local → Workspace**: Local files overwrite workspace files

**Recommendation**: Use version control to track changes

### Permissions

Make sure you have:
- Read access to workspace files
- Write access to local directory
- Valid Databricks token

## Quick Reference

**Local Directory:**
```
/Users/visal.kumar/Documents/databricks/visal.kumar@hellofresh.com
```

**Workspace Directory:**
```
/Workspace/Users/visal.kumar@hellofresh.com
```

**Download (Workspace → Local):**
```bash
python databricks_cli.py sync from_workspace \
  --local-dir /Users/visal.kumar/Documents/databricks/visal.kumar@hellofresh.com \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com
```

**Upload (Local → Workspace):**
```bash
python databricks_cli.py sync to_workspace \
  --local-dir /Users/visal.kumar/Documents/databricks/visal.kumar@hellofresh.com \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com \
  --pattern "**/*"
```






