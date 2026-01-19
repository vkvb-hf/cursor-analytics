# How Workspace Sync Works

## ⚠️ Important: Sync is NOT Automatic

**By default, sync is MANUAL** - you need to run a command to sync files.

### Creating Files Locally → Databricks

**Step 1:** Create/edit files locally
```bash
# Edit a notebook locally
vim ~/databricks_notebooks/my_notebook.py
```

**Step 2:** Sync to Databricks (MANUAL)
```bash
python databricks_cli.py sync to_workspace \
  --local-dir ~/databricks_notebooks \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com/notebooks
```

**Result:** Files are now visible in Databricks workspace.

### Creating Files in Databricks → Local

**Step 1:** Create/edit files in Databricks UI

**Step 2:** Sync to local (MANUAL)
```bash
python databricks_cli.py sync from_workspace \
  --local-dir ~/databricks_notebooks \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com/notebooks
```

**Result:** Files are now in your local directory.

## 🔄 Auto-Sync Mode (Watch Mode)

If you want **automatic syncing**, use watch mode:

### Watch Local → Workspace (Auto-upload)

```bash
# Terminal 1: Start watch mode
python databricks_cli.py sync watch \
  --local-dir ~/databricks_notebooks \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com/notebooks \
  --direction to_workspace

# Terminal 2: Edit files locally
# Changes automatically sync to Databricks!
```

**How it works:**
- Watches your local directory for file changes
- When you save a file, it automatically uploads to Databricks
- You'll see the changes in Databricks UI within seconds

### Watch Workspace → Local (Auto-download)

```bash
# Terminal: Start watch mode
python databricks_cli.py sync watch \
  --local-dir ~/databricks_notebooks \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com/notebooks \
  --direction from_workspace
```

**How it works:**
- Periodically checks Databricks workspace for changes
- Downloads any new/changed files to local
- Note: This checks every 2 seconds, so there's a small delay

## 📋 Summary

| Action | Command | Automatic? |
|--------|---------|------------|
| Upload local → workspace | `sync to_workspace` | ❌ Manual |
| Download workspace → local | `sync from_workspace` | ❌ Manual |
| Auto-upload (watch mode) | `sync watch --direction to_workspace` | ✅ Yes |
| Auto-download (watch mode) | `sync watch --direction from_workspace` | ✅ Yes (with delay) |

## 🎯 Recommended Workflow

### For Active Development

**Use watch mode for auto-sync:**

```bash
# Terminal 1: Auto-sync local → workspace
python databricks_cli.py sync watch \
  --local-dir ~/databricks_notebooks \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com/notebooks \
  --direction to_workspace

# Terminal 2: Edit your notebooks
# Changes automatically appear in Databricks!
```

### For One-Time Sync

**Use manual sync commands:**

```bash
# Upload everything
python databricks_cli.py sync to_workspace \
  --local-dir ~/databricks_notebooks \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com/notebooks

# Download everything
python databricks_cli.py sync from_workspace \
  --local-dir ~/databricks_notebooks \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com/notebooks
```

## ❓ FAQ

**Q: If I create a file locally, will it automatically appear in Databricks?**  
A: **No** - you need to either:
- Run `sync to_workspace` command, OR
- Use watch mode (which auto-syncs)

**Q: If I edit a file in Databricks UI, will it sync to local?**  
A: **No** - you need to either:
- Run `sync from_workspace` command, OR
- Use watch mode with `--direction from_workspace`

**Q: Can I sync both directions automatically?**  
A: You need to run two watch processes:
- One for `to_workspace` (local → Databricks)
- One for `from_workspace` (Databricks → local)

**Q: How fast is watch mode?**  
A: 
- Local → Workspace: Near-instant (detects file save)
- Workspace → Local: ~2 second delay (checks every 2 seconds)






