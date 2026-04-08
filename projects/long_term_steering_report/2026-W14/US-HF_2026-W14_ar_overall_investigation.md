# AR Overall Investigation: US-HF 2026-W14

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W08 → 2026-W14  
**Observation:** 91.98% → 91.93% (-0.05pp)  
**Volume:** 415,885 orders  
**Validation:** PASS

---

## Executive Summary

**Overall:** The US-HF Pre-Dunning Acceptance Rate showed a minimal decline of -0.05pp (91.98% → 91.93%) in 2026-W14, representing stable performance within normal operating range across 415,885 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Change | US-HF rate change | -0.05pp | ✅ |
| L0: Cluster Comparison | US-HF vs other clusters | Best performer (smallest decline) | ✅ |
| L0: 8-Week Trend | Trend stability | Range: 91.48% - 92.44% | ✅ |
| Validation | Pass/Fail threshold | PASS | ✅ |

**Key Findings:**
- US-HF performed as the **best cluster** with the smallest decline (-0.05pp), tied with HF-NA (-0.05pp), compared to overall portfolio decline of -0.37pp
- **INTL-startup shows concerning decline** of -2.85pp (88.37% from 91.23%) with 10,141 orders volume - warrants separate investigation
- 8-week trend shows **stable oscillation** between 91.48% and 92.44%, with W14's rate (91.93%) within normal range
- Week 2026-W15 shows **recovery to 92.44%** (+0.51pp), indicating the W14 dip was transient
- Volume declined from 453,781 (W08) to 415,885 (W14), representing approximately 8% reduction in order volume over the period

**Action:** ✅ **Monitor** - Change is <2pp, no anomaly flags present for US-HF, and validation status is PASS. The metric remains stable within historical norms.

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
| **US-HF** | 91.93% | 91.98% | -0.05pp | 415,885 |  |
| HF-NA | 92.18% | 92.23% | -0.05pp | 507,188 |  |

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ pp (vs prior week) |
|------|--------|--------|----------------------|
| 2026-W15 | 92.44% | 364,598 | +0.51pp |
| 2026-W14 | 91.93% | 415,885 | -0.05pp ← REPORTED CHANGE |
| 2026-W13 | 91.98% | 424,103 | +0.05pp |
| 2026-W12 | 91.93% | 433,761 | -0.16pp |
| 2026-W11 | 92.09% | 444,619 | +0.13pp |
| 2026-W10 | 91.96% | 457,610 | +0.31pp |
| 2026-W09 | 91.65% | 455,121 | +0.17pp |
| 2026-W08 | 91.48% | 453,781 | nanpp |

---

## Summary

The US-HF Pre-Dunning Acceptance Rate decline of -0.05pp in 2026-W14 is negligible and represents normal week-over-week fluctuation within an established stable range. No investigation or escalation is required for US-HF; however, the INTL-startup cluster's -2.85pp decline should be flagged for separate review. Continued monitoring is recommended with the next scheduled weekly assessment.

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
  SELECT '2026-W14' as affected_week, 'US-HF' as cluster,
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
  SELECT '2026-W14' as affected_week, 'US-HF' as cluster,
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
