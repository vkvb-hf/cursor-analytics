# Usage Guide - Long Term Steering Report

## ⚠️ Important: Always Use Virtual Environment

**You must activate the virtual environment before running any scripts.**

## Quick Start

### 1. Activate Virtual Environment

```bash
# Navigate to databricks directory
cd /path/to/databricks

# Activate virtual environment
source databricks_env/bin/activate
```

You should see `(databricks_env)` in your terminal prompt.

### 2. Navigate to Project Directory

```bash
cd cursor_databricks/projects/long_term_steering_report
```

### 3. Run the Report

```bash
# Run all comparison types (default)
python run_long_term_steering.py

# Or run specific comparison types
python run_long_term_steering.py week_yoy
python run_long_term_steering.py week_prev quarter_prev
```

## What Happens When You Run

1. **Notebook Creation**: Creates/updates `long_term_steering_report.py` in Databricks workspace
2. **Job Execution**: Runs the notebook as a Databricks job for each comparison type
3. **Output Generation**: Generates detailed summary text files
4. **File Download**: Downloads output files to local `output/` directory

## Output Files

After running, you'll find these files in the `output/` directory:

- `detailed_summary_week_vs_prev_week.txt` - Week vs previous week comparison
- `detailed_summary_week_vs_prev_yr_week.txt` - Week vs previous year week comparison
- `detailed_summary_quarter_vs_prev_quarter.txt` - Quarter vs previous quarter comparison

## Comparison Types

### `week_prev`
- Compares current week to previous week
- Example: 2025-W45 vs 2025-W44

### `week_yoy`
- Compares current week to same week from previous year
- Example: 2025-W45 vs 2024-W45

### `quarter_prev`
- Compares current quarter (last 13 weeks) to previous quarter (previous 13 weeks)
- Example: 2025-W33 to 2025-W45 vs 2025-W20 to 2025-W32

## Troubleshooting

### "ModuleNotFoundError: No module named 'requests'"
**Solution**: Activate the virtual environment:
```bash
source databricks_env/bin/activate
```

### "ImportError: No module named 'config'"
**Solution**: Make sure you're running from the project directory and config.py exists in the root cursor_databricks directory.

### "Failed to create notebook"
**Solution**: Check your Databricks credentials in `config.py`:
- `DATABRICKS_HOST` - Your workspace URL
- `TOKEN` - Your personal access token
- `CLUSTER_ID` - Your cluster ID

## Example Session

```bash
# 1. Activate virtual environment
cd /Users/visal.kumar/Documents/databricks
source databricks_env/bin/activate

# 2. Navigate to project
cd cursor_databricks/projects/long_term_steering_report

# 3. Run report
python run_long_term_steering.py

# Output:
# 📊 Running long term steering reports for: week_prev, week_yoy, quarter_prev
# ✅ Successfully generated 3 file(s)
# 📁 All files saved to: output/
```

## Notes

- The script automatically handles all three comparison types by default
- Each comparison runs as a separate Databricks job
- There's a 5-second delay between runs to avoid overwhelming the system
- Output files are automatically downloaded and saved to `output/` directory
- Files are also available in Databricks workspace for manual download if needed

