# Archive Directory

This directory contains old and duplicate versions of steering report files that have been replaced by the final working version.

## Archived Files

### Old Main Files
- **`generate_steering_report.py`** (1948 lines)
  - Old full-featured Databricks notebook
  - Generated all 3 comparison types in one run
  - Replaced by: `long_term_steering_report.py`

- **`generate_steering_report_notebook.py`** (427 lines)
  - Old simplified notebook version
  - Lighter version of generate_steering_report.py
  - Replaced by: `long_term_steering_report.py`

- **`generate_steering_report_from_source.py`** (338 lines)
  - Incomplete alternative approach
  - Used DatabricksAPI for local execution
  - Status: Incomplete/template

### Old Runner Scripts
- **`run_generate_steering_report.py`** (280 lines)
  - Runner for old generate_steering_report.py
  - Replaced by: `run_long_term_steering.py`

## Current Active Files

The final working version uses:
- `long_term_steering_report.py` - Main parameterized notebook
- `run_long_term_steering.py` - Runner script
- `validate_output.py` - Output validator
- `check_unknown_dimension.py` - Utility script

## Why Archived?

These files were archived because:
1. **Duplication**: Multiple files with overlapping functionality
2. **Evolution**: Project evolved to use parameterized approach
3. **Maintenance**: Easier to maintain one main file
4. **Clarity**: Clear which files are active vs historical

## Restoring Archived Files

If you need to restore any archived file:
```bash
cp archive/filename.py .
```

However, the current active files (`long_term_steering_report.py` and `run_long_term_steering.py`) are recommended as they are the final working version.

