# Linting Guide for ddi-pays-pipelines

## Overview
When adding or modifying Python files in `ddi-pays-pipelines`, you should run linting checks locally before committing to catch issues early and match the CI/CD pipeline checks.

## Quick Start

### Run Linting on Your Files
```bash
cd /Users/visal.kumar/Documents/databricks/cursor_databricks
python core/lint_check.py ddi_pays_pipelines/generic_etls/ascs_decision_service_simulation.py
```

### Common Usage Patterns

**Single file:**
```bash
python core/lint_check.py ddi_pays_pipelines/generic_etls/ascs_decision_service_simulation.py
```

**Multiple files:**
```bash
python core/lint_check.py ddi_pays_pipelines/generic_etls/ascs_decision_service_simulation.py ddi_pays_pipelines/generic_etl_runner/etls.py
```

**All Python files in a directory:**
```bash
python core/lint_check.py ddi_pays_pipelines/generic_etls/*.py
```

## Linting Rules

The project uses **flake8** with the following configuration (from `.flake8`):
- Max line length: 120 characters
- Max complexity: 10

### Common Issues and Fixes

#### W293: Blank line contains whitespace
**Issue:** Blank lines have spaces or tabs
**Fix:** Remove all whitespace from blank lines

#### W292: No newline at end of file
**Issue:** File doesn't end with a newline
**Fix:** Add a single newline at the end

#### W391: Blank line at end of file
**Issue:** Extra blank lines at the end
**Fix:** Remove trailing blank lines

#### F401: Module imported but unused
**Issue:** Import statement not used
**Fix:** Remove the unused import

#### F541: f-string is missing placeholders
**Issue:** Using f-string without any `{variables}`
**Fix:** Change to regular string: `f"text"` → `"text"`

## Auto-Fix Common Issues

You can use sed to auto-fix whitespace issues:

```bash
cd ~/Documents/GitHub/ddi-pays-pipelines

# Remove trailing whitespace from blank lines
sed -i '' 's/^[[:space:]]*$//' ddi_pays_pipelines/generic_etls/ascs_decision_service_simulation.py

# Remove trailing newline
perl -pi -e 'chomp if eof' ddi_pays_pipelines/generic_etls/ascs_decision_service_simulation.py
```

## CI/CD Pipeline

The GitHub Actions workflow uses:
- `hellofresh/jetstream-ci-scripts/actions/super-linter@master`
- `hellofresh/jetstream-ci-scripts/actions/linter-configs@master`
- `hellofresh/jetstream-ci-scripts/actions/super-linter-hf@master`

Running locally with `lint_check.py` helps catch issues before they fail in CI.

## Workflow

When adding new Python files to ddi-pays-pipelines:

1. **Write your code**
   ```bash
   # Create new file
   vim ddi_pays_pipelines/generic_etls/my_new_etl.py
   ```

2. **Run linting**
   ```bash
   cd ~/Documents/databricks/cursor_databricks
   python core/lint_check.py ddi_pays_pipelines/generic_etls/my_new_etl.py
   ```

3. **Fix issues** (if any)
   - Follow the error messages
   - Re-run linting to verify

4. **Commit when clean**
   ```bash
   git add ddi_pays_pipelines/generic_etls/my_new_etl.py
   git commit -m "Add my_new_etl [Cursor_Code]"
   ```

## Example Session

```bash
$ cd ~/Documents/databricks/cursor_databricks
$ python core/lint_check.py ddi_pays_pipelines/generic_etls/ascs_decision_service_simulation.py
================================================================================
Running flake8 linter
================================================================================
Workspace: /Users/visal.kumar/Documents/GitHub/ddi-pays-pipelines
Files: ddi_pays_pipelines/generic_etls/ascs_decision_service_simulation.py

✅ No linting issues found!
```

## Tips

1. **Run linting frequently** during development, not just at the end
2. **Fix issues immediately** - they're easier to fix in context
3. **Use auto-formatters** for whitespace issues (sed, perl)
4. **Check multiple files** if you modified dependencies

## Related Files

- `ddi-pays-pipelines/.flake8` - Flake8 configuration
- `cursor_databricks/core/lint_check.py` - Local linting utility






