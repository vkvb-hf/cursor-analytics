# Long Term Steering Report

This project contains a parameterized notebook for generating long-term steering reports that compare metrics across different time periods.

## Overview

The project consists of a single parameterized notebook that can generate two types of comparisons:

1. **Week vs Previous Year Week** (`COMPARISON_TYPE = 'week_yoy'`)
   - Compares current week metrics against the same week from the previous year
   - Uses year-over-year comparison to identify long-term trends

2. **Quarter vs Previous Quarter** (`COMPARISON_TYPE = 'quarter_prev'`)
   - Compares current quarter (last 13 weeks) against previous quarter (previous 13 weeks)
   - Uses quarter-over-quarter comparison to identify sequential trends

## Files

### Active Files (Final Working Version)
- `long_term_steering_report.py` - Main parameterized notebook for both comparison types
- `run_long_term_steering.py` - Runner script to execute all comparison types
- `validate_output.py` - Validates generated report files
- `check_unknown_dimension.py` - Utility to check for unknown dimensions in data
- `README.md` - This file

### Archived Files
Old and duplicate versions have been moved to `archive/` directory:
- `generate_steering_report.py` - Old full-featured version (1948 lines)
- `generate_steering_report_notebook.py` - Old simplified version (427 lines)
- `generate_steering_report_from_source.py` - Incomplete alternative approach (338 lines)
- `run_generate_steering_report.py` - Runner for old generate_steering_report.py

See `WHY_MANY_FILES.md` for details on why these files existed.

## Usage

### ⚠️ Important: Use Virtual Environment

**Always activate the virtual environment before running scripts:**

```bash
# Navigate to databricks directory
cd /path/to/databricks

# Activate virtual environment
source databricks_env/bin/activate

# Then run scripts
cd cursor_databricks/projects/long_term_steering_report
python run_long_term_steering.py
```

The virtual environment (`databricks_env`) contains all required dependencies (requests, databricks-sql-connector, pandas, etc.).

### Running the Report

#### Option 1: Using the Runner Script (Recommended)

```bash
# Activate virtual environment first
source databricks_env/bin/activate

# Run all comparison types
cd cursor_databricks/projects/long_term_steering_report
python run_long_term_steering.py

# Or run specific comparison types
python run_long_term_steering.py week_yoy quarter_prev
```

This will:
1. Create/update the notebook in Databricks workspace
2. Run it as a job for each comparison type
3. Download output files to the project directory
4. Save files to `output/` directory

#### Option 2: Running the Notebook Directly in Databricks

The notebook can be run directly in Databricks. To select the comparison type, set the `COMPARISON_TYPE` parameter at the top of the notebook:

```python
COMPARISON_TYPE = 'week_yoy'  # or 'quarter_prev'
```

The notebook will:

1. Automatically detect the latest complete week
2. Calculate the appropriate comparison periods based on the selected type
3. Query metrics from `payments_hf.payments_p0_metrics` table
4. Generate detailed summary reports

### Output Files

The notebook generates a detailed summary text file based on the comparison type:

- **Week vs Previous Week** (`week_prev`): `detailed_summary_week_vs_prev_week.txt`
- **Week vs Previous Year Week** (`week_yoy`): `detailed_summary_week_vs_prev_yr_week.txt`
- **Quarter vs Previous Quarter** (`quarter_prev`): `detailed_summary_quarter_vs_prev_quarter.txt`

Output files are saved to:
- **Local project directory**: `output/` folder (when using runner script)
- **Databricks workspace**: `/Workspace/Users/visal.kumar@hellofresh.com/long-term-steering-{week}`
- **DBFS**: `/tmp/{filename}`

**Note**: When using `run_long_term_steering.py`, files are automatically downloaded to the `output/` directory.

## Metrics Included

Both notebooks analyze the following steering metrics:

1. Payment Page Visit to Success (Frontend)
2. Payment Page Visit to Success (Backend)
3. Select to Success
4. Total Duplicate Rate
5. Total Duplicate Block Rate
6. Payment Fraud Block Rate
7. Reactivation Rate
8. AR Pre Dunning
9. Acceptance LL0 (Initial Charge)
10. Acceptance LL0 and LL1+ (Recurring Charge)
11. Ship Rate
12. Recovery W0
13. Recovery W12
14. Dunning Profit

## Reporting Clusters

Metrics are analyzed across the following reporting clusters:
- Overall
- HF-NA
- HF-INTL
- RTE
- WL

## Key Features

- **Statistical Significance Testing**: Uses z-score calculations to determine if changes are statistically significant
- **Business Impact Analysis**: Identifies positive/negative impacts based on metric directionality
- **Dimension-Level Analysis**: Breaks down metrics by dimensions (country, payment method, etc.)
- **Business Unit Analysis**: Provides insights at the business unit level
- **Volume Impact Calculation**: Estimates the volume impacted by metric changes

## Comparison Logic

### Week vs Previous Year Week
- Compares current week to the same week from the previous year
- Uses `prev_yr_metric_value_numerator` and `prev_yr_metric_value_denominator` columns
- Example: 2025-W44 vs 2024-W44

### Quarter vs Previous Quarter
- Aggregates metrics across the last 13 weeks (current quarter)
- Aggregates metrics across the previous 13 weeks (previous quarter)
- Compares aggregated values
- Example: 2025-W32 to 2025-W44 vs 2025-W19 to 2025-W31

## Notes

- Both notebooks automatically refresh the `payments_hf.payments_p0_metrics` table before querying
- The notebooks filter for P0 metrics only (`flag_is_p0 = 'TRUE'`)
- Only ratio and dollar-ratio metric types are included
- Certain metrics and dimensions are excluded (see code for details)

## Quick Reference

### Always Use Virtual Environment
```bash
source databricks_env/bin/activate
cd cursor_databricks/projects/long_term_steering_report
python run_long_term_steering.py
```

See `USAGE.md` for detailed usage instructions.

## Related Projects

This project is related to the `p0_metrics` project which contains the main steering output generation logic. The files in this project are simplified versions focused on specific long-term comparisons.

