# Recommended Folder Structure for Workspace Sync

## Your Databricks Workspace Path

Based on your existing setup, your Databricks workspace user path is:
```
/Workspace/Users/visal.kumar@hellofresh.com/
```

## Recommended Folder Structure

### Option 1: Dedicated Notebooks Folder (Recommended)

**Local Directory:**
```bash
~/databricks_notebooks
# or
~/Documents/databricks_notebooks
```

**Databricks Workspace Directory:**
```
/Workspace/Users/visal.kumar@hellofresh.com/notebooks
```

**Sync Command:**
```bash
python databricks_cli.py sync to_workspace \
  --local-dir ~/databricks_notebooks \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com/notebooks
```

### Option 2: Project-Based Structure (For Multiple Projects)

**Local Directory:**
```bash
~/Documents/databricks_projects
```

**Structure:**
```
~/Documents/databricks_projects/
├── notebooks/          # General notebooks
├── project1/          # Project-specific notebooks
│   └── notebooks/
└── project2/
    └── notebooks/
```

**Databricks Workspace:**
```
/Workspace/Users/visal.kumar@hellofresh.com/
├── notebooks/          # General notebooks
├── project1/           # Project-specific
│   └── notebooks/
└── project2/
    └── notebooks/
```

**Sync Commands:**
```bash
# Sync general notebooks
python databricks_cli.py sync to_workspace \
  --local-dir ~/Documents/databricks_projects/notebooks \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com/notebooks

# Sync project1 notebooks
python databricks_cli.py sync to_workspace \
  --local-dir ~/Documents/databricks_projects/project1/notebooks \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com/project1/notebooks
```

### Option 3: Inside Your Current Project (For Development)

**Local Directory:**
```bash
/Users/visal.kumar/Documents/databricks/cursor_databricks/notebooks
```

**Databricks Workspace:**
```
/Workspace/Users/visal.kumar@hellofresh.com/cursor_databricks/notebooks
```

**Sync Command:**
```bash
cd /Users/visal.kumar/Documents/databricks/cursor_databricks

python databricks_cli.py sync to_workspace \
  --local-dir ./notebooks \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com/cursor_databricks/notebooks
```

## Recommended Setup (Quick Start)

I recommend **Option 1** for simplicity:

```bash
# 1. Create local directory
mkdir -p ~/databricks_notebooks

# 2. Create your first notebook
cat > ~/databricks_notebooks/my_first_notebook.py << 'EOF'
# Databricks notebook source
# MAGIC %md
# MAGIC # My First Synced Notebook

# MAGIC %sql
# MAGIC SELECT CURRENT_TIMESTAMP() as current_time
EOF

# 3. Sync to workspace
cd /Users/visal.kumar/Documents/databricks/cursor_databricks
python databricks_cli.py sync to_workspace \
  --local-dir ~/databricks_notebooks \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com/notebooks
```

## Your Current Workspace Structure

Based on your existing files, you already have:
```
/Workspace/Users/visal.kumar@hellofresh.com/
├── long_term_steering_report          # Existing notebook
└── [other existing notebooks/files]
```

You can:
1. **Keep existing notebooks where they are** (don't sync them)
2. **Create a new `notebooks/` folder** for synced notebooks
3. **Or sync to a different folder** like `synced_notebooks/`

## Watch Mode Setup

For active development, set up watch mode:

```bash
# Terminal 1: Start watch mode
python databricks_cli.py sync watch \
  --local-dir ~/databricks_notebooks \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com/notebooks

# Terminal 2: Edit notebooks
# Changes automatically sync!
```

## Best Practices

1. **Use a dedicated folder** - Keep synced notebooks separate from other files
2. **Version control** - Add your local notebooks folder to git:
   ```bash
   cd ~/databricks_notebooks
   git init
   git add .
   git commit -m "Initial notebooks"
   ```
3. **Organize by project** - Use subfolders for different projects
4. **Use watch mode** - For active development, use watch mode instead of manual sync

## Quick Reference

**Your email:** `visal.kumar@hellofresh.com`

**Recommended workspace path:**
```
/Workspace/Users/visal.kumar@hellofresh.com/notebooks
```

**Recommended local path:**
```
~/databricks_notebooks
```

**Quick sync command:**
```bash
python databricks_cli.py sync to_workspace \
  --local-dir ~/databricks_notebooks \
  --workspace-dir /Workspace/Users/visal.kumar@hellofresh.com/notebooks
```






