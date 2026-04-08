# AR Overall Investigation: RTE 2026-W14

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W08 → 2026-W14  
**Observation:** 92.79% → 92.46% (-0.33pp)  
**Volume:** 431,853 orders  
**Validation:** PASS

---

## Executive Summary

**Overall:** The Pre-Dunning Acceptance Rate for RTE declined modestly from 92.79% to 92.46% (-0.33pp) in 2026-W14, representing a below-average decline compared to most other clusters.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall RTE Change | -0.33pp decline | -0.33pp | ✅ |
| L0: Cluster Comparison | RTE performing better than 6 of 9 clusters | -0.33pp vs -0.37pp overall | ✅ |
| L0: INTL-startup Outlier | Largest decline across all clusters | -2.85pp | ⚠️ |
| L0: 8-Week Trend | W14 decline follows W13 decline (-0.30pp) | -0.33pp | ✅ |
| L0: Volume Validation | 431,853 orders processed | N/A | ✅ |

**Key Findings:**
- RTE's -0.33pp decline is smaller than the Overall portfolio decline of -0.37pp, indicating RTE is performing relatively well
- INTL-startup cluster shows a significant -2.85pp decline (88.37% from 91.23%) with 10,141 orders, flagged as an anomaly requiring attention
- The 8-week trend shows W14 is part of a two-week consecutive decline (W13: -0.30pp, W14: -0.33pp), though W15 data already shows recovery (+0.46pp to 92.92%)
- INTL-growing cluster contributes the highest volume (370,655 orders) with a moderate -0.86pp decline
- HF-NA and US-HF clusters remained stable with minimal movement (-0.05pp each)

**Action:** Monitor - The change is <2pp and RTE-specific anomaly flags are not present. However, recommend investigating the INTL-startup cluster separately due to its ⚠️ flag and -2.85pp decline.

---

---

## L0: Cluster Comparison

| Cluster | Curr % | Prev % | Change pp | Volume | Flag |
|---------|--------|--------|-----------|--------|------|
| INTL-startup | 88.37% | 91.23% | -2.85pp | 10,141 | ⚠️ |
| INTL-growing | 94.23% | 95.08% | -0.86pp | 370,655 |  |
| HF-INTL | 93.64% | 94.16% | -0.53pp | 784,387 |  |
| WL | 89.33% | 89.72% | -0.39pp | 165,018 |  |
| Overall | 92.6% | 92.97% | -0.37pp | 1,888,446 |  |
| HF-TOTAL | 93.06% | 93.43% | -0.36pp | 1,291,575 |  |
| **RTE** | 92.46% | 92.79% | -0.33pp | 431,853 |  |
| INTL-mature | 93.23% | 93.4% | -0.17pp | 403,591 |  |
| HF-NA | 92.18% | 92.23% | -0.05pp | 507,188 |  |
| US-HF | 91.93% | 91.98% | -0.05pp | 415,885 |  |

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ pp (vs prior week) |
|------|--------|--------|----------------------|
| 2026-W15 | 92.92% | 420,769 | +0.46pp |
| 2026-W14 | 92.46% | 431,853 | -0.33pp ← REPORTED CHANGE |
| 2026-W13 | 92.79% | 442,530 | -0.30pp |
| 2026-W12 | 93.09% | 443,994 | -0.11pp |
| 2026-W11 | 93.2% | 458,408 | +1.65pp |
| 2026-W10 | 91.55% | 467,998 | +0.22pp |
| 2026-W09 | 91.33% | 466,696 | +0.26pp |
| 2026-W08 | 91.07% | 462,049 | nanpp |

---

## Summary

The RTE Pre-Dunning Acceptance Rate decline of -0.33pp in 2026-W14 falls within normal operational variance and does not meet escalation thresholds. The metric has already shown recovery in W15 (+0.46pp), suggesting this was a temporary fluctuation rather than a systemic issue. While RTE itself requires only monitoring, the INTL-startup cluster warrants a separate investigation given its outsized -2.85pp decline despite representing only 10K orders.

---

## Recommendation

- [ ] Monitor: if change <2pp and no anomaly flags
- [ ] Investigate: if anomaly flags present
- [ ] Escalate P1: if >3pp drop AND >10K orders

---

## SQL Queries

<details>
<summary>L0: Cluster Comparison</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'RTE' as cluster,
    '2_PreDunningAR' as ar_metric, '1_1_Overall Total Box Candidates' as metric_group
)
SELECT reporting_cluster,
  ROUND(SUM(current_metric_value_numerator) / NULLIF(SUM(current_metric_value_denominator), 0) * 100, 2) as curr_rate_pct,
  ROUND(SUM(prev_metric_value_numerator) / NULLIF(SUM(prev_metric_value_denominator), 0) * 100, 2) as prev_rate_pct,
  ROUND((SUM(current_metric_value_numerator) / NULLIF(SUM(current_metric_value_denominator), 0) - 
         SUM(prev_metric_value_numerator) / NULLIF(SUM(prev_metric_value_denominator), 0)) * 100, 2) as change_pp,
  SUM(current_metric_value_denominator) as volume
FROM payments_hf.payments_p0_metrics
WHERE metric_name = (SELECT ar_metric FROM params) AND metric_group = (SELECT metric_group FROM params)
  AND dimension_name = '_Overall' AND date_granularity = 'WEEK' AND date_value = (SELECT affected_week FROM params)
GROUP BY reporting_cluster ORDER BY change_pp ASC

```

</details>

<details>
<summary>L0: 8-Week Trend</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'RTE' as cluster,
    '2_PreDunningAR' as ar_metric, '1_1_Overall Total Box Candidates' as metric_group
),
weekly_rates AS (
  SELECT date_value as week,
    ROUND(SUM(current_metric_value_numerator) / NULLIF(SUM(current_metric_value_denominator), 0) * 100, 2) as rate_pct,
    SUM(current_metric_value_denominator) as volume
  FROM payments_hf.payments_p0_metrics
  WHERE metric_name = (SELECT ar_metric FROM params) AND metric_group = (SELECT metric_group FROM params)
    AND dimension_name = '_Overall' AND date_granularity = 'WEEK' AND reporting_cluster = (SELECT cluster FROM params)
  GROUP BY date_value ORDER BY date_value DESC LIMIT 8
)
SELECT week, rate_pct, volume, ROUND(rate_pct - LAG(rate_pct) OVER (ORDER BY week ASC), 2) as change_pp_vs_prior_week
FROM weekly_rates ORDER BY week DESC

```

</details>

---

*Report: 2026-04-08*
