# P0 Metrics - Steering Output Generation

This project generates comprehensive steering metrics reports for P0 payment metrics with flexible comparison capabilities across multiple time periods.

## Overview

The steering metrics system generates detailed reports comparing current performance against previous periods, including:
- **Activation metrics** (Checkout Funnel, Payment Page Visit to Success)
- **Fraud metrics** (Duplicate Rate, Payment Fraud Block Rate)
- **Reactivation metrics**
- **Active customer metrics** (AR, Ship Rate, Recovery, Dunning Profit)

## Project Structure

```
p0_metrics/
├── README.md                                    # This file
├── steering_output_generation_parametrized.py   # Main Databricks notebook
├── run_steering_output.py                        # Script to run the notebook
├── verify_metrics_comparison.py                 # Verification script
├── generate_steering_report.py                  # Report generator (optional)
├── steering_metrics_notebook.py                 # Original full notebook (reference)
├── outputs/                                     # Generated output files
│   ├── detailed_summary_*.txt                   # Summary files for each comparison
│   ├── metrics_comparison_table.csv             # Verification comparison table
│   └── W44_steering_*.md                        # Generated steering reports
├── tests/                                       # Test and debug scripts
│   ├── test_join_logic.py
│   ├── test_join_simulation.py
│   ├── test_build_query.py
│   └── debug_prev_values.py
└── docs/                                        # Documentation
    └── DEBUGGING_SUMMARY.md
```

## Quick Start

### Prerequisites

1. Python 3.8+ with required packages:
   ```bash
   pip install pyspark pandas requests databricks-sql-connector
   ```

2. Databricks credentials configured in `config.py`:
   - `DATABRICKS_HOST`
   - `TOKEN`
   - `CLUSTER_ID`
   - `SERVER_HOSTNAME`
   - `HTTP_PATH`

### Run Steering Output Generation

```bash
cd /Users/visal.kumar/Documents/databricks/cursor_databricks
source ../databricks_env/bin/activate
cd projects/p0_metrics
python run_steering_output.py
```

This will:
1. Upload the parametrized notebook to Databricks workspace
2. Run it as a job
3. Download all 6 detailed summary files to `outputs/` folder

## Comparison Types

The system supports **6 comparison types**:

### 1. Week vs Previous Week (`week_prev`)
- Current week compared to immediately previous week
- Example: 2025-W44 vs 2025-W43
- Uses `prev_metric_value` columns directly from table

### 2. Week vs Previous Year Week (`week_yoy`)
- Current week compared to same week last year
- Example: 2025-W44 vs 2024-W44
- Uses `prev_yr_metric_value` columns from table

### 3. Month vs Previous Month (`month_prev`)
- Last 4 completed weeks vs previous 4 weeks
- Example: 2025-W41,42,43,44 vs 2025-W37,38,39,40
- Aggregates `current_metric_value` across weeks and joins

### 4. Month vs Previous Year Month (`month_yoy`)
- Last 4 completed weeks vs same 4 weeks from last year
- Example: 2025-W41,42,43,44 vs 2024-W41,42,43,44
- Uses `prev_yr_metric_value` aggregated across weeks

### 5. Quarter vs Previous Quarter (`quarter_prev`)
- Last 13 completed weeks vs previous 13 weeks
- Example: 2025-W32-44 vs 2025-W19-31
- Aggregates `current_metric_value` across weeks and joins

### 6. Quarter vs Previous Year Quarter (`quarter_yoy`)
- Last 13 completed weeks vs same 13 weeks from last year
- Example: 2025-W32-44 vs 2024-W32-44
- Uses `prev_yr_metric_value` aggregated across weeks

## Configuration

### Notebook Configuration

In `steering_output_generation_parametrized.py`, configure:

```python
# Generate all 6 comparisons
COMPARISON_MODES = 'all'

# Or specify specific comparisons
COMPARISON_MODES = ['week_prev', 'week_yoy']  # Only week comparisons
COMPARISON_MODES = ['month_prev', 'month_yoy']  # Only month comparisons
COMPARISON_MODES = ['quarter_prev', 'quarter_yoy']  # Only quarter comparisons
```

### Workspace Configuration

```python
WORKSPACE_FOLDER = '/Workspace/Users/visal.kumar@hellofresh.com'
```

### Metrics Configuration

The notebook tracks **14 steering metrics**:
- Checkout funnel metrics (frontend and backend)
- Voucher fraud metrics
- Payment fraud metrics
- Reactivation rates
- Pre-dunning AR metrics
- Ship rates and recovery metrics
- Dunning profit metrics

## Output Files

### Generated Files

The notebook generates 6 separate detailed summary files:

1. `detailed_summary_week_vs_prev_week.txt`
2. `detailed_summary_week_vs_prev_yr_week.txt`
3. `detailed_summary_month_vs_prev_month.txt`
4. `detailed_summary_month_vs_prev_yr_month.txt`
5. `detailed_summary_quarter_vs_prev_quarter.txt`
6. `detailed_summary_quarter_vs_prev_yr_quarter.txt`

Each file includes:
- Period information in header (list of weeks)
- Overall cluster summary
- Dimension-level breakdowns
- Business unit-level breakdowns
- Statistical significance indicators
- Volume impact calculations

### Output Location

- **Databricks Workspace**: `/Workspace/Users/{username}/steering-parametrized-{YYYY-Www}/`
- **Local**: `outputs/detailed_summary_*.txt`

## Key Features

### Statistical Significance Testing
- Uses z-scores to determine statistical significance
- Thresholds: |z-score| > 1.96 (significant), > 2.58 (highly significant)

### Multi-level Reporting
- **Overall cluster level**: Aggregated across all business units
- **Dimension level**: By PaymentMethod, ChannelCategory, etc.
- **Business unit level**: HF-NA, HF-INTL, US-HF, RTE, WL

### Volume Impact Calculation
- Shows how many units (orders, boxes, etc.) are impacted by the change
- Only displays changes with:
  - Relative change > 10%, OR
  - Volume impacted > 30

### Business Impact Direction
- Positive/Negative based on metric type (`flag_more_is_good`)
- Automatically determines if increase/decrease is good or bad

## Data Sources

### Primary Table
- **`payments_hf.payments_p0_metrics`**
  - Contains pre-aggregated metrics at week granularity
  - Columns:
    - `current_metric_value_numerator/denominator` - Current period values
    - `prev_metric_value_numerator/denominator` - Previous period values (week/month)
    - `prev_yr_metric_value_numerator/denominator` - Previous year same period values

### Data Flow

1. **Single Week Comparisons** (week_prev, week_yoy):
   - Direct query from table using `prev_metric_value` or `prev_yr_metric_value` columns
   - No aggregation needed

2. **Multi-Week Comparisons** (month_prev, quarter_prev):
   - Query `current_metric_value` for current period weeks
   - Query `current_metric_value` for previous period weeks
   - Aggregate (SUM) across weeks
   - Join on metric dimensions
   - Rename previous period columns to `prev_metric_value`

3. **Year-over-Year Multi-Week** (month_yoy, quarter_yoy):
   - Query `prev_yr_metric_value` for current period weeks
   - Aggregate (SUM) across weeks
   - Direct use (no join needed)

## Verification

### Verify Metrics Accuracy

Run the verification script to compare generated files with direct table queries:

```bash
python verify_metrics_comparison.py
```

This generates `outputs/metrics_comparison_table.csv` showing:
- File values vs table values for each comparison type
- Difference calculations
- Summary statistics

### Expected Accuracy
- Week comparisons: < 0.01% difference (rounding)
- Month/Quarter comparisons: < 0.1% difference (aggregation rounding)

## Troubleshooting

### Job Fails with Timeout
- Increase `timeout_seconds` in `run_steering_output.py` (default: 7200 seconds)
- Check Databricks cluster availability

### Output Files Not Found
- Check Databricks workspace: `/Workspace/Users/{username}/steering-parametrized-{week}`
- Verify job completed successfully (check job logs)
- Manual download instructions are printed if automatic download fails

### Zero Values in Month/Quarter Comparisons
- **Fixed**: Issue was with PySpark join key data type consistency
- Solution: Explicit casting of join keys, especially `dimension_value` (None → 'None')
- See `docs/DEBUGGING_SUMMARY.md` for details

### Join Failures
- Ensure join keys have consistent data types
- Check for null value handling in `dimension_value` column
- Verify all join columns exist in both DataFrames

## Development

### Testing

Test scripts are available in `tests/`:
- `test_join_logic.py` - Test SQL query logic
- `test_join_simulation.py` - Simulate PySpark join behavior
- `test_build_query.py` - Test query building function
- `debug_prev_values.py` - Debug month/quarter comparison issues

### Adding New Metrics

1. Add metric name to `STEERING_METRICS` list in notebook
2. Ensure metric exists in `payments_hf.payments_p0_metrics` table
3. Verify metric has `flag_is_p0 = 'TRUE'`
4. Run verification script to confirm accuracy

### Modifying Comparison Logic

Key functions in `steering_output_generation_parametrized.py`:
- `build_metrics_query()` - Builds SQL queries for different comparison types
- `process_comparison_data()` - Processes and calculates significance
- `write_single_comparison_output()` - Writes output files

## Reporting Clusters

- **Overall**: Aggregated across all business units
- **HF-NA**: HelloFresh North America
- **HF-INTL**: HelloFresh International
- **US-HF**: US HelloFresh
- **RTE**: Ready-to-Eat
- **WL**: Weight Watchers

## Example Output

```
Steering Metrics - 4-Week Period vs Previous 4-Week Period
================================================================================

Current Period: 2025-W41, 2025-W42, 2025-W43, 2025-W44
Previous Period: 2025-W37, 2025-W38, 2025-W39, 2025-W40

================================================================================
1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess
================================================================================

For Overall cluster, the 1_Activation (Paid + Referrals) - 1_Checkout Funnel - 
1_PaymentPageVisitToSuccess increased from 31.34% to 33.23%, a slight 6.02% 
increase (volume impacted: 73.1K). This change is significant and has a 
positive business impact. [4-Week Period vs Previous 4-Week Period]
```

## Version History

- **v2.0** (Current): Added quarter comparisons, fixed month/quarter join issues
- **v1.0**: Initial parameterized version with week and month comparisons

## Support

For issues or questions:
1. Check `docs/DEBUGGING_SUMMARY.md` for known issues
2. Review Databricks job logs
3. Run verification script to check data accuracy
4. Check test scripts in `tests/` for debugging examples

## License

Internal HelloFresh project - Confidential
