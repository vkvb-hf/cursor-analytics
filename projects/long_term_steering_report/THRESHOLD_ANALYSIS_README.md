# Data-Driven Threshold Analysis

This document explains how to use the new data-driven threshold analysis feature for determining meaningful metric change thresholds.

## Overview

The steering report uses thresholds to determine which metric changes are "significant" enough to report. Previously, these were fixed thresholds:
- AR metrics: 5% for all comparisons
- Other metrics: 10% for week-over-week, 20% for long-term and year-over-year

The new data-driven approach analyzes historical trends at the Overall level to determine what level of change is actually meaningful for each metric.

## How It Works

1. **Historical Data Collection**: For each metric, queries the last N weeks (default: 52 weeks) of data at Overall level
2. **Change Calculation**: Calculates week-over-week percentage changes
3. **Statistical Analysis**: Uses one of several methods to determine a threshold:
   - **Standard Deviation**: `mean + (multiplier * std_dev)` (default: 2.0 = ~95% confidence)
   - **Percentile**: Uses 95th percentile of historical changes
   - **Z-Score**: Uses statistical significance (default: 2.576 = 99% confidence)
   - **Hybrid**: Averages std_dev and percentile methods (default)
   - **Conservative**: Uses maximum of std_dev and percentile
   - **Aggressive**: Uses minimum of std_dev and percentile

4. **Comparison Type Adjustment**: Long-term and YoY comparisons use 1.5x the week-over-week threshold (longer periods have more variability)

## Usage

### Enable Data-Driven Thresholds

In `generate_steering_report.py`, set:

```python
USE_DATA_DRIVEN_THRESHOLDS = True
```

### Configure Analysis Parameters

```python
# Number of historical weeks to analyze (default: 52 = 1 year)
HISTORICAL_WEEKS_FOR_ANALYSIS = 52

# Method to use (in get_threshold_for_comparison function, line ~112)
method='hybrid'  # Options: 'std_dev', 'percentile', 'z_score', 'hybrid', 'conservative', 'aggressive'
```

### Test Different Methods

You can test different methods by changing the `method` parameter in `get_threshold_for_comparison()`:

```python
# In get_threshold_for_comparison(), around line 112:
data_driven_threshold = get_data_driven_threshold(
    metric_full_name, 
    comparison_type, 
    method='hybrid'  # Change this to test different methods
)
```

## Methods Explained

### Standard Deviation (`std_dev`)
- **Formula**: `mean + (2.0 * std_dev)`
- **Interpretation**: Captures ~95% of normal variation
- **Use when**: You want to flag changes that are statistically unusual
- **Pros**: Statistically sound, accounts for variability
- **Cons**: Can be sensitive to outliers

### Percentile (`percentile`)
- **Formula**: 95th percentile of historical changes
- **Interpretation**: Only flag changes larger than 95% of historical changes
- **Use when**: You want to focus on truly exceptional changes
- **Pros**: Robust to outliers, easy to understand
- **Cons**: May miss important trends if historical data is limited

### Z-Score (`z_score`)
- **Formula**: `mean + (2.576 * std_dev)` (99% confidence)
- **Interpretation**: Statistical significance at 99% level
- **Use when**: You want very high confidence before flagging changes
- **Pros**: Most statistically rigorous
- **Cons**: May be too conservative, missing important changes

### Hybrid (`hybrid`) - **Recommended**
- **Formula**: Average of std_dev and percentile methods
- **Interpretation**: Balances statistical rigor with practical sensitivity
- **Use when**: You want a balanced approach (default)
- **Pros**: Best of both worlds
- **Cons**: May not be optimal for all metrics

### Conservative (`conservative`)
- **Formula**: Maximum of std_dev and percentile
- **Interpretation**: Only flag when both methods agree it's significant
- **Use when**: You want to minimize false positives
- **Pros**: Very few false alarms
- **Cons**: May miss important changes

### Aggressive (`aggressive`)
- **Formula**: Minimum of std_dev and percentile
- **Interpretation**: Flag when either method suggests significance
- **Use when**: You want to catch all potentially important changes
- **Pros**: Catches more changes
- **Cons**: More false positives

## Fallback Behavior

If data-driven analysis fails (e.g., insufficient historical data), the system automatically falls back to the original fixed thresholds:
- AR metrics: 5%
- Other metrics: 10% (week-over-week) or 20% (long-term/YoY)

## Debugging

The system includes debug output that shows:
- Which metrics are using data-driven thresholds
- The calculated threshold values
- When fallback to fixed thresholds occurs

Look for `[THRESHOLD ANALYSIS]` messages in the debug output.

## Example Output

```
[THRESHOLD ANALYSIS] Retrieved 52 weeks of historical data for: Payment Page Visit to Success
[THRESHOLD ANALYSIS] Payment Page Visit to Success (week_prev): threshold=8.3% (method=hybrid)
[THRESHOLD ANALYSIS] Payment Page Visit to Success (long_term): threshold=12.5% (method=hybrid)
```

## Testing Recommendations

1. **Start with Hybrid Method**: This provides a good balance
2. **Compare Results**: Run with `USE_DATA_DRIVEN_THRESHOLDS = False` and `True` to compare
3. **Adjust Historical Weeks**: Try 26, 52, or 104 weeks to see impact
4. **Test Different Methods**: Compare std_dev, percentile, and hybrid for your metrics
5. **Review Debug Output**: Check which metrics are using data-driven thresholds

## Limitations

1. **Requires Historical Data**: Needs at least 10 weeks of data (preferably 52+)
2. **Overall Level Only**: Analysis is based on Overall level trends
3. **Week-over-Week Focus**: Analysis is based on week-over-week changes, then adjusted for longer periods
4. **No Seasonality Adjustment**: Does not account for seasonal patterns (future enhancement)

## Future Enhancements

Potential improvements:
- Seasonality adjustment
- Business unit-specific thresholds
- Dimension-specific thresholds
- Moving average smoothing
- Trend detection (not just variability)

## Questions?

If you need help:
1. Check the debug output for threshold calculation details
2. Review the `get_historical_metric_data()` function to understand data collection
3. Examine the threshold calculation functions to understand the methods

