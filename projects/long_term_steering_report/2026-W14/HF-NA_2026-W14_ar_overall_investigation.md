# AR Overall Investigation: HF-NA 2026-W14

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W08 → 2026-W14  
**Observation:** 92.23% → 92.18% (-0.05pp)  
**Volume:** 507,188 orders  
**Validation:** PASS

---

## Executive Summary

## Executive Summary

**Overall:** The HF-NA Pre-Dunning Acceptance Rate showed a minimal decline of -0.05pp (92.23% → 92.18%) in 2026-W14, representing the smallest change among all clusters and well within normal fluctuation range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Cluster Comparison | HF-NA vs Overall | -0.05pp vs -0.37pp | ✅ |
| L0: 8-Week Trend | Stability Check | Range: 91.35% - 92.65% | ✅ |
| Volume Check | 507,188 orders | Sufficient sample | ✅ |
| Anomaly Flags | HF-NA flagged | No flag | ✅ |

**Key Findings:**
- HF-NA (-0.05pp) significantly outperformed the Overall cluster average decline of -0.37pp
- INTL-startup showed the largest decline at -2.85pp with 10,141 orders and is flagged (⚠️) for attention
- The 8-week trend shows HF-NA improving overall from 91.35% (W08) to 92.18% (W14), a net gain of +0.83pp
- W15 data already shows recovery to 92.65% (+0.47pp), indicating the W14 dip was temporary
- US-HF, the largest component of HF-NA (415,885 orders), mirrors the same -0.05pp change

**Action:** ☑️ **Monitor** — Change is <2pp with no anomaly flags. The metric remains stable and within normal operating range.

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
| RTE | 92.46% | 92.79% | -0.33pp | 431,853 |  |
| INTL-mature | 93.23% | 93.4% | -0.17pp | 403,591 |  |
| **HF-NA** | 92.18% | 92.23% | -0.05pp | 507,188 |  |
| US-HF | 91.93% | 91.98% | -0.05pp | 415,885 |  |

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ pp (vs prior week) |
|------|--------|--------|----------------------|
| 2026-W15 | 92.65% | 445,692 | +0.47pp |
| 2026-W14 | 92.18% | 507,188 | -0.05pp ← REPORTED CHANGE |
| 2026-W13 | 92.23% | 517,599 | +0.09pp |
| 2026-W12 | 92.14% | 526,516 | -0.14pp |
| 2026-W11 | 92.28% | 539,763 | +0.27pp |
| 2026-W10 | 92.01% | 554,777 | +0.42pp |
| 2026-W09 | 91.59% | 553,112 | +0.24pp |
| 2026-W08 | 91.35% | 548,921 | nanpp |

---

## Summary

The HF-NA Pre-Dunning Acceptance Rate decline of -0.05pp in 2026-W14 represents negligible movement that requires no immediate action. The 8-week trend demonstrates consistent stability with an overall positive trajectory, and W15 data confirms recovery. Attention should instead be directed to the INTL-startup cluster, which experienced a significant -2.85pp decline warranting separate investigation.

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
  SELECT '2026-W14' as affected_week, 'HF-NA' as cluster,
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
  SELECT '2026-W14' as affected_week, 'HF-NA' as cluster,
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
