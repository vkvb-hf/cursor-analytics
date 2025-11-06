# P0 Metrics - Steering Metrics Generation

This project contains Databricks notebooks for generating steering metrics reports with flexible comparison capabilities.

## Overview

The steering metrics notebooks generate weekly reports for P0 payment metrics, including:
- Activation metrics (Checkout Funnel, Payment Page Visit to Success)
- Fraud metrics (Duplicate Rate, Payment Fraud Block Rate)
- Reactivation metrics
- Active customer metrics (AR, Ship Rate, Recovery, Dunning Profit)

## Files

### Active Files

- **`steering_output_generation_parametrized.py`** - Main Databricks notebook (RECOMMENDED)
  - Supports multiple comparison types (week/week, week/year, 4-week periods)
  - Generates combined output with all comparisons
  
- **`run_steering_output.py`** - Script to run the parametrized notebook
  - Automatically uploads notebook to Databricks
  - Runs as a job and downloads the output file
  
- **`steering_metrics_notebook.py`** - Original full P0 metrics notebook
  - Contains complete metrics generation logic
  - Used as reference/backup

### Output Files

- **`detailed_summary_combined.txt`** - Combined output with all comparison types
- Individual metric folders (generated in Databricks workspace)

## Quick Start

### Run Steering Output Generation

```bash
cd /Users/visal.kumar/Documents/databricks/cursor_databricks
source ../databricks_env/bin/activate
python projects/p0_metrics/run_steering_output.py
```

This will:
1. Upload the parametrized notebook to Databricks
2. Run it as a job
3. Download `detailed_summary_combined.txt` to the local folder

## Comparison Types Supported

The parameterized version supports four comparison types:

1. **Week vs Previous Week** (`week_prev`)
   - Current week compared to immediately previous week
   - Example: 2025-W44 vs 2025-W43

2. **Week vs Previous Year Week** (`week_yoy`)
   - Current week compared to same week last year
   - Example: 2025-W44 vs 2024-W44

3. **4-Week Period vs Previous 4-Week Period** (`month_prev`)
   - Last 4 completed weeks vs previous 4 weeks
   - Example: 2025-W41-44 vs 2025-W37-40

4. **4-Week Period vs Previous Year 4-Week Period** (`month_yoy`)
   - Last 4 completed weeks vs same 4 weeks from last year
   - Example: 2025-W41-44 vs 2024-W41-44

## Configuration

In `steering_output_generation_parametrized.py`, set the `COMPARISON_MODES` variable:

```python
# Generate all 4 comparisons
COMPARISON_MODES = 'all'

# Or specify specific comparisons
COMPARISON_MODES = ['week_prev', 'week_yoy']  # Only week comparisons
COMPARISON_MODES = ['month_prev']  # Only 4-week period comparisons
```

## Key Features

1. **Statistical Significance Testing**: Uses z-scores to determine statistical significance of metric changes
2. **Multi-level Reporting**: Generates reports at:
   - Overall cluster level
   - Dimension level (by PaymentMethod, ChannelCategory, etc.)
   - Business unit level
3. **Volume Impact Calculation**: Shows how many units are impacted by the change
4. **Business Impact Direction**: Positive/Negative based on metric type (more_is_good flag)
5. **Filtering**: Only shows changes with:
   - Relative change > 10%, OR
   - Volume impacted > 30
6. **Combined View**: All comparisons shown together for easy comparison

## Reporting Clusters

- Overall
- HF-NA
- HF-INTL
- US-HF
- RTE
- WL

## Metrics Tracked

14 steering metrics covering:
- Checkout funnel metrics (frontend and backend)
- Voucher fraud metrics
- Payment fraud metrics
- Reactivation rates
- Pre-dunning AR metrics
- Ship rates and recovery metrics
- Dunning profit metrics

## Output Structure

The notebook generates reports in the format:
```
/Workspace/Users/{username}/steering-parametrized-{YYYY-Www}/
├── detailed_summary_combined.txt  # Main combined output
└── {metric_name}/
    └── summary.txt
```

Local output is saved as:
```
projects/p0_metrics/detailed_summary_combined.txt
```

## Data Sources

The notebook uses the `payments_hf.payments_p0_metrics` table which contains:
- `current_metric_value_numerator/denominator` - Current period values
- `prev_metric_value_numerator/denominator` - Previous period values (week/month)
- `prev_yr_metric_value_numerator/denominator` - Previous year same period values

## Example Output Format

```
================================================================================
1_Activation (Paid + Referrals) - 1_Checkout Funnel - 1_PaymentPageVisitToSuccess
================================================================================

--- vs Previous Period (2025-W44) ---

For Overall cluster, the 1_Activation... increased from 32.96% to 34.14%, 
a slight 3.58% increase (volume impacted: 10.2K). This change is significant 
and has a positive business impact. [vs Previous Period]

--- 4-Week Period vs Previous 4-Week Period (2025-W41-2025-W44) ---

For Overall cluster, the 1_Activation... increased from 31.42% to 32.98%, 
a slight 4.97% increase (volume impacted: 43.2K). This change is significant 
and has a positive business impact. [4-Week Period vs Previous 4-Week Period]
```

## Troubleshooting

### Job fails with timeout
- Increase `timeout_seconds` in `run_steering_output.py`
- The default is 7200 seconds (2 hours)

### Output file not found
- Check Databricks workspace: `/Workspace/Users/{username}/steering-parametrized-{week}`
- Verify the job completed successfully
- Manual download instructions are printed if automatic download fails

### Verification Queries

If you need to verify the 4-week aggregation logic, you can use the verification scripts (temporary):
- `check_4week_data.py` - Check data availability
- `check_join_issue.py` - Verify join logic
- `verify_4week_computation.py` - Run verification queries

## Source

- Original notebook from Databricks Job ID: 863174042909812
- Notebook ID: 3549820133656532
