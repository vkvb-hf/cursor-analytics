# Cursor-Analytics Refactor Plan

## Guiding Principles

1. **Never break what works** - MCP server and core utilities stay untouched until Phase 4
2. **One phase at a time** - Complete each phase before moving to next
3. **Smoke test after every change** - Run `scripts/smoke_test.py` after each step
4. **Git commits at each step** - Easy rollback if something breaks
5. **Backward compatibility** - Old import paths work during transition

---

## Phase 0: Preparation (MUST DO FIRST)

### Step 0.1: Create refactor branch
```bash
cd /Users/visal.kumar/Documents/databricks/cursor-analytics
git checkout -b refactor/cleanup-v1
git push -u origin refactor/cleanup-v1
```

### Step 0.2: Run smoke test to establish baseline
```bash
python scripts/smoke_test.py
```
Save the output - this is your "known good" state.

### Step 0.3: Commit the smoke test
```bash
git add scripts/smoke_test.py REFACTOR_PLAN.md
git commit -m "Add refactor plan and smoke test baseline"
```

---

## Phase 1: Safe Cleanup (Zero Risk)

**Goal**: Remove/archive dead code without touching any working code.

### Step 1.1: Archive failed_projects/
```bash
mkdir -p archive
mv failed_projects archive/
git add -A && git commit -m "Archive failed_projects (parallel_query_execution)"
python scripts/smoke_test.py  # Verify nothing broke
```

### Step 1.2: Move report outputs to data/
```bash
mkdir -p data/outputs/steering_reports
mv projects/long_term_steering_report/W*.md data/outputs/steering_reports/
mv projects/long_term_steering_report/threshold_analysis_table.md data/outputs/steering_reports/
git add -A && git commit -m "Move report outputs to data/outputs/"
python scripts/smoke_test.py
```

### Step 1.3: Archive status docs
```bash
mkdir -p docs/archive/status
mv docs/status/* docs/archive/status/
rmdir docs/status
mv docs/test_archive docs/archive/test_archive
git add -A && git commit -m "Archive status and test docs"
python scripts/smoke_test.py
```

### Step 1.4: Clean up projects/adhoc/exploration
```bash
# These are one-off test scripts - archive them
mkdir -p archive/adhoc_exploration
mv projects/adhoc/exploration/*.py archive/adhoc_exploration/
git add -A && git commit -m "Archive adhoc exploration scripts"
python scripts/smoke_test.py
```

**Phase 1 Complete Checkpoint:**
- [ ] Smoke test passes
- [ ] MCP server still works
- [ ] `from databricks_api import DatabricksAPI` still works

---

## Phase 2: Documentation Consolidation

**Goal**: Single source of truth for each topic.

### Step 2.1: Create canonical README.md
Keep existing README.md but simplify it. Remove duplicate sections.

### Step 2.2: Consolidate guides
```bash
# Keep only these in docs/guides/:
# - SETUP.md (merge from QUICK_START.md, INSTRUCTIONS.md)
# - MCP_GUIDE.md (already good, move to root)
# - CURSOR_USAGE.md (merge CURSOR_MASTERY_GUIDE.md into it)

mkdir -p docs/archive/guides
mv docs/guides/QUICK_START.md docs/archive/guides/
mv docs/guides/QUICK_REFERENCE.md docs/archive/guides/
mv docs/guides/QUICK_START_NOTEBOOKS.md docs/archive/guides/
# ... etc for other redundant guides
```

### Step 2.3: Update root-level docs
```bash
# Keep at root:
# - README.md
# - MCP_GUIDE.md
# - CHANGELOG.md

# Archive the rest:
mv CURSOR_QUICK_REFERENCE.md docs/archive/
mv CURSOR_QUICK_START.md docs/archive/
mv FULL_WORKSPACE_SYNC.md docs/archive/
mv SYNC_*.md docs/archive/
mv WORKSPACE_SYNC_QUICK_START.md docs/archive/
```

**Phase 2 Complete Checkpoint:**
- [ ] Smoke test passes
- [ ] Can find setup instructions easily
- [ ] MCP guide is clear and accessible

---

## Phase 3: Package Structure (Careful!)

**Goal**: Proper Python package without breaking existing imports.

### Step 3.1: Create pyproject.toml
```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "cursor-analytics"
version = "1.0.0"
description = "Databricks toolkit for product analytics"
requires-python = ">=3.9"
dependencies = [
    "databricks-sql-connector>=3.0.0",
    "requests>=2.28.0",
    "pandas>=1.5.0",
    "python-dotenv>=1.0.0",
    "mcp>=1.0.0",
]

[project.optional-dependencies]
test = ["pytest>=7.0.0", "pytest-mock>=3.10.0"]

[tool.setuptools.packages.find]
where = ["."]
include = ["core*", "scripts*"]
```

### Step 3.2: Install in editable mode
```bash
pip install -e .
python scripts/smoke_test.py  # CRITICAL: verify imports still work
```

### Step 3.3: Gradually update imports (ONE FILE AT A TIME)
For each file with `sys.path.insert`:
1. Remove the sys.path hack
2. Run smoke test
3. If it fails, revert and investigate
4. If it passes, commit

**DO NOT** update all files at once!

---

## Phase 4: MCP Server Consolidation (Last!)

**Goal**: Single MCP server with configuration options.

### Step 4.1: Audit the three servers
```bash
# Compare what's different:
diff mcp_server.py mcp_server_optimized.py
diff mcp_server.py mcp_server_standalone.py
```

### Step 4.2: Merge into single server
Keep `mcp_server.py` as the canonical version. Add configuration flags for:
- Connection pooling (from optimized)
- Standalone mode (from standalone)

### Step 4.3: Archive old servers
```bash
mkdir -p archive/mcp_servers
mv mcp_server_optimized.py archive/mcp_servers/
mv mcp_server_standalone.py archive/mcp_servers/
```

### Step 4.4: Update MCP configuration
Update `~/.cursor/mcp.json` to point to the single server.

---

## Phase 5: Agent Optimization (Enhancement)

### Step 5.1: Create .cursorrules
```
# .cursorrules for cursor-analytics

## Repository Context
This is a Databricks toolkit for product analytics. The main entry points are:
- `databricks_api.py` - Python API
- `databricks_cli.py` - CLI tool  
- `mcp_server.py` - MCP server for Cursor

## When working with this repo:
1. Always use `from databricks_api import DatabricksAPI` for Databricks operations
2. SQL queries should use the MCP `execute_sql` tool
3. New utilities go in `core/`
4. New projects go in `projects/{project_name}/`
5. Run `python scripts/smoke_test.py` after changes

## File locations:
- Core utilities: `core/`
- CLI scripts: `scripts/`
- Projects: `projects/`
- Tests: `tests/`
- Documentation: `docs/` and root markdown files
```

### Step 5.2: Add structured responses to MCP tools
Update MCP tools to return JSON with consistent structure:
```python
{
    "success": true,
    "data": [...],
    "metadata": {"row_count": 100, "execution_time_ms": 234}
}
```

---

## Rollback Procedures

### If smoke test fails after any step:
```bash
git checkout -- .  # Discard all changes
# OR
git reset --hard HEAD~1  # Undo last commit
```

### If MCP server breaks:
```bash
# Restore from archive
cp archive/mcp_servers/mcp_server_optimized.py mcp_server.py
# Update mcp.json to point to working version
```

### Nuclear option:
```bash
git checkout main  # Go back to main branch
git branch -D refactor/cleanup-v1  # Delete refactor branch
```

---

## Success Criteria

After all phases complete:
- [ ] `python scripts/smoke_test.py` passes
- [ ] MCP server responds to all tools
- [ ] `from databricks_api import DatabricksAPI` works
- [ ] `python databricks_cli.py --help` works
- [ ] Documentation is clear and non-redundant
- [ ] File count reduced by ~50%
- [ ] No `sys.path.insert` hacks in core modules

---

## Timeline Estimate

| Phase | Effort | Risk |
|-------|--------|------|
| Phase 0 | 30 min | None |
| Phase 1 | 1 hour | Very Low |
| Phase 2 | 1 hour | Low |
| Phase 3 | 2 hours | Medium |
| Phase 4 | 1 hour | Medium |
| Phase 5 | 1 hour | Low |

**Total: ~6-7 hours spread across multiple sessions**

---

## Notes

- Do NOT rush Phase 3 (package structure) - this is where things can break
- Phase 1 and 2 are safe to do anytime
- Phase 4 should only happen after Phase 3 is stable
- Keep the refactor branch until everything is verified working for a week
