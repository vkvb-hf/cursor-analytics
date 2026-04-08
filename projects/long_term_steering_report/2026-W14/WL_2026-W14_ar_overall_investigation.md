# AR Overall Investigation: WL 2026-W14

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W08 → 2026-W14  
**Observation:** 89.72% → 89.33% (-0.39pp)  
**Volume:** 165,018 orders  
**Validation:** PASS

---

## Executive Summary

**Overall:** The WL Pre-Dunning Acceptance Rate declined by -0.39pp (from 89.72% to 89.33%) in 2026-W14, representing 165,018 orders, which falls within normal variance and passes validation.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Cluster Comparison | WL vs Overall | -0.39pp vs -0.37pp | ✅ |
| L0: INTL-startup | Outlier Check | -2.85pp | ⚠️ |
| L0: 8-Week Trend | Trend Direction | Recovering in W15 (+1.27pp) | ✅ |
| Volume Threshold | >10K orders | 165,018 orders | ✅ |

**Key Findings:**
- WL cluster decline of -0.39pp is consistent with the overall portfolio decline of -0.37pp, indicating no cluster-specific anomaly
- INTL-startup shows a significant outlier decline of -2.85pp (10,141 orders) and warrants separate investigation
- 8-week trend shows WL has been gradually improving from 88.14% (W08) to 89.33% (W14), with W14 being a minor setback in an upward trajectory
- W15 data already shows strong recovery to 90.6% (+1.27pp), suggesting W14 decline was transient
- The decline magnitude (-0.39pp) is well below the P1 escalation threshold of >3pp

**Action:** Monitor - The change is <2pp, no critical anomaly flags for WL specifically, and W15 shows recovery. Consider separate investigation into INTL-startup's -2.85pp decline.

---

---

## L0: Cluster Comparison

| Cluster | Curr % | Prev % | Change pp | Volume | Flag |
|---------|--------|--------|-----------|--------|------|
| INTL-startup | 88.37% | 91.23% | -2.85pp | 10,141 | ⚠️ |
| INTL-growing | 94.23% | 95.08% | -0.86pp | 370,655 |  |
| HF-INTL | 93.64% | 94.16% | -0.53pp | 784,387 |  |
| **WL** | 89.33% | 89.72% | -0.39pp | 165,018 |  |
| Overall | 92.6% | 92.97% | -0.37pp | 1,888,446 |  |
| HF-TOTAL | 93.06% | 93.43% | -0.36pp | 1,291,575 |  |
| RTE | 92.46% | 92.79% | -0.33pp | 431,853 |  |
| INTL-mature | 93.23% | 93.4% | -0.17pp | 403,591 |  |
| US-HF | 91.93% | 91.98% | -0.05pp | 415,885 |  |
| HF-NA | 92.18% | 92.23% | -0.05pp | 507,188 |  |

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ pp (vs prior week) |
|------|--------|--------|----------------------|
| 2026-W15 | 90.6% | 137,132 | +1.27pp |
| 2026-W14 | 89.33% | 165,018 | -0.39pp ← REPORTED CHANGE |
| 2026-W13 | 89.72% | 169,667 | +0.06pp |
| 2026-W12 | 89.66% | 169,891 | -0.13pp |
| 2026-W11 | 89.79% | 174,933 | +0.71pp |
| 2026-W10 | 89.08% | 179,964 | +0.89pp |
| 2026-W09 | 88.19% | 180,862 | +0.05pp |
| 2026-W08 | 88.14% | 179,647 | nanpp |

---

## Summary

The WL Pre-Dunning Acceptance Rate experienced a minor decline of -0.39pp in 2026-W14, which aligns with broader portfolio trends and does not indicate a WL-specific issue. The 8-week trend demonstrates overall metric improvement since W08, and early W15 data confirms recovery to 90.6%. No immediate escalation is required for WL; however, the INTL-startup cluster's -2.85pp decline should be flagged for separate review.

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
  SELECT '2026-W14' as affected_week, 'WL' as cluster,
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
  SELECT '2026-W14' as affected_week, 'WL' as cluster,
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
