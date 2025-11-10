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

- `long_term_steering_report.py` - Parameterized notebook for both comparison types
- `README.md` - This file

## Usage

### Running the Notebook

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

- **Week vs Previous Year Week** (`week_yoy`): `detailed_summary_week_vs_prev_yr_week.txt`
- **Quarter vs Previous Quarter** (`quarter_prev`): `detailed_summary_quarter_vs_prev_quarter.txt`

Output files are saved to:
- Local workspace: `/Workspace/Users/visal.kumar@hellofresh.com/long-term-steering-{type}-{week}`
- DBFS: `/tmp/{filename}`

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

## Related Projects

This project is related to the `p0_metrics` project which contains the main steering output generation logic. The files in this project are simplified versions focused on specific long-term comparisons.

