# Root Cause Analysis: LL0 Missing Business Units in Deep Insights

## Problem Statement

For "Acceptance LL0 (Initial Charge)" metric in W08 steering report:
- **Expected**: Business Units like AT (-2.70%), CH (-6.03%), GQ (+28.57%) should appear in Deep Insights
- **Actual**: Only Dimensions appear, no Business Units

## Key Finding

### Report Output Comparison

**Payment Checkout Approval Rate (WORKING):**
```
**Deep Insights**
[2.5% - 19%] - Business Units: **SE** (↑4.40%), **BE** (↓5.44%), **TV** (↓17.02%), **TT** (↑4.87%), **CG** (↑9.06%)
[2.5% - 19%] - Dimensions: **RTE** PM Others (↓6.52%), **WL** PM Credit Card (↑3.27%)
```

**Acceptance LL0 (BROKEN):**
```
**Deep Insights**
[2.5% - 19%] - Dimensions: **Overall** PP No Payment (↓6.11%), **HF-INTL** PP No Payment (↓12.37%)
```

### SQL Data Verification

For LL0, **11 BUs should pass the filter** (threshold >= 2.5% OR volume > 30):

| BU | abs_rel_change | volume_impacted | Filter Result | Expected Bucket |
|----|----------------|-----------------|---------------|----------------|
| GQ | 28.57% | 0.29 | PASS_THRESHOLD | **MEDIUM** |
| LU | 9.09% | 5.55 | PASS_THRESHOLD | LOW |
| CH | 6.03% | 12.47 | PASS_THRESHOLD | LOW |
| AT | 2.70% | 18.78 | PASS_THRESHOLD | LOW |
| NL | 2.69% | 35.49 | PASS_THRESHOLD | LOW |
| NZ | 2.53% | 21.59 | PASS_THRESHOLD | LOW |
| GN | 2.47% | 45.39 | PASS_VOLUME | LOW |
| FR | 2.29% | 245.89 | PASS_VOLUME | LOW |
| GB | 2.21% | 236.42 | PASS_VOLUME | LOW |
| ER | 1.78% | 46.43 | PASS_VOLUME | LOW |
| DE | 1.02% | 96.48 | PASS_VOLUME | LOW |

**GQ should be in MEDIUM bucket (28.57% >= 20%)!**

## Confirmed Facts

1. ✅ Raw data exists in `payments_hf.payments_p0_metrics`
2. ✅ `bu_level` rows exist for LL0
3. ✅ BUs pass the significance filter (threshold OR volume)
4. ✅ SQL bucket assignment logic is correct
5. ❌ BUs do NOT appear in the generated report

## Root Cause Hypothesis

The issue is in the Python code's `bucket_by_percentage` function or the code path that calls it.

Debug output showed:
```
[DEBUG AR] - all_significant_bu_deep count: 8
[DEBUG AR] ⚠️ No significant insights found!
```

This means:
1. 8 BUs were collected in `all_significant_bu_deep`
2. But after `bucket_by_percentage`, all buckets are empty
3. The "No significant insights" message is triggered

## Next Steps

1. Add more granular debug logging inside `bucket_by_percentage` to trace each row
2. Verify the DataFrame structure passed to `bucket_by_percentage`
3. Check if there's a data type mismatch (e.g., string vs float for abs_rel_change)
4. Test `bucket_by_percentage` in isolation with the exact data

## Files in This Branch

- `debug/COMPARISON_RESULTS.md` - Initial comparison results
- `debug/ROOT_CAUSE_ANALYSIS.md` - This file
- `debug/comparison_queries.sql` - SQL queries used
- `debug/test_bucket_bug.py` - Test notebook for bucket function
- `debug/test_bucket_exact.py` - Exact replication test
- `debug/compare_working_broken.py` - Full comparison notebook
