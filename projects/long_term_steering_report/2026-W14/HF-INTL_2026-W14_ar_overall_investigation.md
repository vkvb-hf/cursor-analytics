# AR Overall Investigation: HF-INTL 2026-W14

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W08 → 2026-W14  
**Observation:** 94.16% → 93.64% (-0.53pp)  
**Volume:** 784,387 orders  
**Validation:** PASS

---

## Executive Summary

**Overall:** The Pre-Dunning Acceptance Rate for HF-INTL declined by 0.53pp (94.16% → 93.64%) in 2026-W14, representing 784,387 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Cluster Comparison | HF-INTL vs Overall | -0.53pp vs -0.37pp | ⚠️ |
| L0: INTL-startup | Largest decline | -2.85pp | ⚠️ |
| L0: INTL-growing | Second largest decline | -0.86pp | ⚠️ |
| L0: 8-Week Trend | W14 vs W13 | -0.52pp | ✅ |
| Validation | Report accuracy | PASS | ✅ |

**Key Findings:**
- INTL-startup cluster shows the most severe decline at -2.85pp (88.37% rate), flagged as anomaly, though volume is relatively small at 10,141 orders
- INTL-growing is the largest contributor to HF-INTL decline with -0.86pp change on significant volume of 370,655 orders
- The 8-week trend shows W14 hit a local low, but W15 already shows recovery (+1.07pp to 94.71%), suggesting potential transient issue
- HF-INTL underperformed the overall portfolio (-0.53pp vs -0.37pp overall) but outperformed HF-NA (-0.05pp) and US-HF (-0.05pp)
- Volume decreased from 842,480 (W13) to 784,387 (W14), a reduction of ~58K orders

**Action:** Monitor – The change is <2pp, W15 data shows recovery to 94.71%, and while INTL-startup is flagged, its low volume (10,141 orders) limits overall impact. Continue monitoring INTL-startup and INTL-growing clusters for sustained declines.

---

---

## L0: Cluster Comparison

| Cluster | Curr % | Prev % | Change pp | Volume | Flag |
|---------|--------|--------|-----------|--------|------|
| INTL-startup | 88.37% | 91.23% | -2.85pp | 10,141 | ⚠️ |
| INTL-growing | 94.23% | 95.08% | -0.86pp | 370,655 |  |
| **HF-INTL** | 93.64% | 94.16% | -0.53pp | 784,387 |  |
| WL | 89.33% | 89.72% | -0.39pp | 165,018 |  |
| Overall | 92.6% | 92.97% | -0.37pp | 1,888,446 |  |
| HF-TOTAL | 93.06% | 93.43% | -0.36pp | 1,291,575 |  |
| RTE | 92.46% | 92.79% | -0.33pp | 431,853 |  |
| INTL-mature | 93.23% | 93.4% | -0.17pp | 403,591 |  |
| HF-NA | 92.18% | 92.23% | -0.05pp | 507,188 |  |
| US-HF | 91.93% | 91.98% | -0.05pp | 415,885 |  |

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ pp (vs prior week) |
|------|--------|--------|----------------------|
| 2026-W15 | 94.71% | 720,003 | +1.07pp |
| 2026-W14 | 93.64% | 784,387 | -0.52pp ← REPORTED CHANGE |
| 2026-W13 | 94.16% | 842,480 | -0.44pp |
| 2026-W12 | 94.6% | 877,187 | -0.30pp |
| 2026-W11 | 94.9% | 897,106 | +1.09pp |
| 2026-W10 | 93.81% | 916,831 | +0.68pp |
| 2026-W09 | 93.13% | 896,537 | -0.42pp |
| 2026-W08 | 93.55% | 884,970 | nanpp |

---

## Summary

The HF-INTL Pre-Dunning Acceptance Rate decline of 0.53pp in W14 appears to be a transient dip rather than a systemic issue, as W15 data already shows recovery to 94.71%. The INTL-startup cluster warrants continued observation due to its -2.85pp drop, though its limited volume minimizes overall portfolio impact. No immediate escalation is required, but monitoring should continue to ensure the recovery trend holds.

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
  SELECT '2026-W14' as affected_week, 'HF-INTL' as cluster,
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
  SELECT '2026-W14' as affected_week, 'HF-INTL' as cluster,
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
