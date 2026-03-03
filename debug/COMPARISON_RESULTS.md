# Debug Results: Working vs Broken Metric Comparison

## Summary

| Metric | Threshold | Total BUs | Significant | LOW Bucket |
|--------|-----------|-----------|-------------|------------|
| WORKING (Payment Checkout Approval Rate) | 10% | 15 | 12 | 12 |
| BROKEN (Acceptance LL0) | 2.5% | 16 | 8 | 8 |

**Key Finding**: Both metrics have BUs that should be in the LOW bucket based on SQL logic.
- WORKING: 12 BUs in LOW bucket
- BROKEN: 8 BUs in LOW bucket

## BROKEN Metric (Acceptance LL0) - Detailed BU Analysis

| BU | abs_rel_change | volume_impacted | Passes Threshold (>=2.5%) | Passes Volume (>30) | Expected Bucket |
|----|----------------|-----------------|---------------------------|---------------------|----------------|
| LU | 9.09% | 5.55 | YES | NO | LOW |
| CH | 6.03% | 12.47 | YES | NO | LOW |
| AT | 2.70% | 18.78 | YES | NO | LOW |
| NL | 2.69% | 35.49 | YES | YES | LOW |
| NZ | 2.53% | 21.59 | YES | NO | LOW |
| FR | 2.29% | 245.89 | NO | YES | LOW |
| GB | 2.21% | 236.42 | NO | YES | LOW |
| DE | 1.02% | 96.48 | NO | YES | LOW |
| NO | 2.18% | 26.02 | NO | NO | NONE |
| SE | 1.47% | 21.45 | NO | NO | NONE |
| IT | 1.28% | 0.23 | NO | NO | NONE |
| DK | 1.23% | 23.00 | NO | NO | NONE |
| ES | 1.12% | 7.54 | NO | NO | NONE |
| IE | 0.55% | 8.07 | NO | NO | NONE |
| AU | 0.49% | 18.92 | NO | NO | NONE |
| BE | 0.32% | 6.06 | NO | NO | NONE |

**8 BUs should be in LOW bucket**: LU, CH, AT, NL, NZ, FR, GB, DE

## WORKING Metric (Payment Checkout Approval Rate) - Detailed BU Analysis

| BU | abs_rel_change | volume_impacted | Passes Threshold (>=10%) | Passes Volume (>30) | Expected Bucket |
|----|----------------|-----------------|--------------------------|---------------------|----------------|
| ES | 13.35% | 290.29 | YES | YES | LOW |
| FR | 11.53% | 2516.49 | YES | YES | LOW |
| NL | 9.99% | 292.89 | NO | YES | LOW |
| SE | 8.99% | 216.35 | NO | YES | LOW |
| NO | 7.01% | 139.67 | NO | YES | LOW |
| IE | 4.05% | 125.30 | NO | YES | LOW |
| BE | 3.15% | 79.61 | NO | YES | LOW |
| AU | 3.02% | 254.21 | NO | YES | LOW |
| AT | 2.82% | 43.24 | NO | YES | LOW |
| DK | 1.92% | 52.01 | NO | YES | LOW |
| DE | 0.83% | 166.31 | NO | YES | LOW |
| GB | 0.75% | 161.47 | NO | YES | LOW |
| CH | 4.05% | 21.59 | NO | NO | NONE |
| LU | 1.84% | 1.55 | NO | NO | NONE |
| NZ | 1.13% | 24.14 | NO | NO | NONE |

**12 BUs should be in LOW bucket**: ES, FR, NL, SE, NO, IE, BE, AU, AT, DK, DE, GB

## Key Observation

The SQL logic correctly identifies significant BUs for both metrics. The issue is NOT in:
1. Raw data availability
2. Threshold calculation
3. Filter logic (threshold OR volume)
4. Bucket assignment logic

## Hypothesis

The issue must be in the Python code execution path. Possible causes:
1. The `bucket_by_percentage` function is not being called with the correct data
2. There's a code path difference between WORKING and BROKEN metrics
3. The debug output showing empty buckets is from a different code version

## Next Steps

1. Check if there's a different code path for AR metrics vs non-AR metrics
2. Verify the actual `bucket_by_percentage` function being executed matches the expected logic
3. Add more granular debug logging to trace exactly where the data is lost
