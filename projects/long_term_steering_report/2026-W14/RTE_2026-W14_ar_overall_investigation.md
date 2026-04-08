# AR Overall Investigation: RTE 2026-W14

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 92.79% → 92.46% (-0.36%)  
**Volume:** 431,853 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate declined modestly from 92.79% to 92.46% (-0.36%) in W14, representing a statistically non-significant change across 431,853 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Upstream impact | -0.52% | ⚠️ |
| 2_PreDunningAR | Primary metric | -0.35% | ⚠️ |
| 3_PostDunningAR | Downstream recovery | -0.31% | ⚠️ |
| 6_PaymentApprovalRate | Final approval | -0.20% | ⚠️ |

**Key Findings:**
- **Consistent decline across funnel:** All related AR metrics showed parallel declines (-0.20% to -0.52%), indicating the issue originates at FirstRunAR (-0.52%) rather than being isolated to pre-dunning
- **No country exceeded threshold:** All 7 countries remained within ±2.5% tolerance; TK showed the largest decline at -1.63% but with minimal volume (1,779 orders)
- **Payment provider anomalies flagged:** "Unknown" provider showed +332.23% change and "No Payment" showed +2.66%, but both have negligible volume (83 and 534 orders respectively)
- **Credit Card segment leads decline:** Credit Card payments declined -0.42% representing 316,124 orders (73% of volume), making it the primary contributor to the overall drop
- **Three-week declining trend:** Rate has dropped consecutively from 93.20% (W11) to 92.46% (W14), a cumulative decline of -0.74pp over 4 weeks

**Action:** **Monitor** — The decline is not statistically significant and no individual dimension breached investigation thresholds. Continue monitoring the three-week downward trend; if W15 continues declining, escalate for deeper FirstRunAR investigation.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % (vs prior week) |
|------|--------|--------|---------------------|
| 2026-W14 | 92.46% | 431,853 | -0.36% ← REPORTED CHANGE |
| 2026-W13 | 92.79% | 442,530 | -0.32% |
| 2026-W12 | 93.09% | 443,994 | -0.12% |
| 2026-W11 | 93.2% | 458,408 | +1.80% |
| 2026-W10 | 91.55% | 467,998 | +0.24% |
| 2026-W09 | 91.33% | 466,696 | +0.29% |
| 2026-W08 | 91.07% | 462,049 | -0.28% |
| 2026-W07 | 91.33% | 474,461 | +nan% |

---

## L1: Country Breakdown

| Country | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|---------|--------|--------|----------|----------|----------|------|
| TK | 88.65% | 90.12% | -1.63% | 1,779 | 2,155 |  |
| TZ | 90.11% | 91.42% | -1.43% | 3,013 | 3,310 |  |
| YE | 88.15% | 88.62% | -0.53% | 45,214 | 47,830 |  |
| FJ | 93.62% | 93.97% | -0.37% | 397,332 | 409,231 |  |
| CF | 93.47% | 93.7% | -0.24% | 52,140 | 52,939 |  |
| TT | 97.2% | 96.27% | +0.97% | 4,924 | 4,903 |  |
| TV | 93.41% | 92.01% | +1.52% | 2,065 | 2,191 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Credit Card | 92.08% | 92.47% | -0.42% | 316,124 | 323,597 |  |
| Apple Pay | 90.02% | 90.19% | -0.19% | 54,874 | 55,464 |  |
| Paypal | 96.45% | 96.52% | -0.07% | 55,378 | 57,290 |  |
| Others | 98.28% | 97.93% | +0.36% | 5,477 | 6,179 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Braintree | 93.41% | 93.75% | -0.36% | 293,781 | 310,634 |  |
| ProcessOut | 91.66% | 91.81% | -0.17% | 60,625 | 52,341 |  |
| Adyen | 89.45% | 89.58% | -0.14% | 76,830 | 78,208 |  |
| No Payment | 100.0% | 97.41% | +2.66% | 534 | 1,312 | ⚠️ |
| Unknown | 49.4% | 11.43% | +332.23% | 83 | 35 | ⚠️ |

---



## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.82% | 91.29% | -0.52% | 431,853 | 442,530 |  |
| 2_PreDunningAR | 92.46% | 92.79% | -0.35% | 431,853 | 442,530 |  |
| 3_PostDunningAR | 94.12% | 94.41% | -0.31% | 431,853 | 442,530 |  |
| 6_PaymentApprovalRate | 94.76% | 94.94% | -0.20% | 431,853 | 442,530 |  |

---

## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 409,231 | 397,332 | -2.9% | Stable |
| CF | High (>92%) | 52,939 | 52,140 | -1.5% | Stable |
| YE | Medium (>85%) | 47,830 | 45,214 | -5.5% | Stable |
| TT | High (>92%) | 4,903 | 4,924 | +0.4% | Stable |
| TO | Medium (>85%) | 3,508 | 3,480 | -0.8% | Stable |
| TZ | Medium (>85%) | 3,310 | 3,013 | -9.0% | Stable |
| TV | High (>92%) | 2,191 | 2,065 | -5.8% | Stable |
| TK | Medium (>85%) | 2,155 | 1,779 | -17.4% | Stable |

---

## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

## SQL Queries

<details>
<summary>L0: 8-Week Trend</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'RTE' as cluster,
    '2_PreDunningAR' as ar_metric, '1_1_Overall Total Box Candidates' as metric_group
),
completed_weeks AS (
  SELECT iso_year_week as week
  FROM dimensions.date_dimension
  WHERE date_string_backwards <= date_sub(CURRENT_DATE, 1)
  GROUP BY iso_year_week
  HAVING COUNT(*) = 7
),
weekly_rates AS (
  SELECT p.date_value as week,
    ROUND(SUM(p.current_metric_value_numerator) / NULLIF(SUM(p.current_metric_value_denominator), 0) * 100, 2) as rate_pct,
    SUM(p.current_metric_value_denominator) as volume
  FROM payments_hf.payments_p0_metrics p
  JOIN completed_weeks cw ON p.date_value = cw.week
  WHERE p.metric_name = (SELECT ar_metric FROM params) 
    AND p.metric_group = (SELECT metric_group FROM params)
    AND p.dimension_name = '_Overall' 
    AND p.date_granularity = 'WEEK' 
    AND p.reporting_cluster = (SELECT cluster FROM params)
  GROUP BY p.date_value 
  ORDER BY p.date_value DESC 
  LIMIT 8
)
SELECT week, rate_pct, volume, 
  ROUND((rate_pct - LAG(rate_pct) OVER (ORDER BY week ASC)) / NULLIF(LAG(rate_pct) OVER (ORDER BY week ASC), 0) * 100, 2) as change_pct_vs_prior_week
FROM weekly_rates 
ORDER BY week DESC

```

</details>

<details>
<summary>L1a: Country Breakdown</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'RTE' as cluster
),
weeks AS (
  SELECT 
    (SELECT affected_week FROM params) as affected_week,
    LAG(hellofresh_week) OVER (ORDER BY hellofresh_week) as prev_week
  FROM (SELECT DISTINCT hellofresh_week FROM dimensions.date_dimension WHERE hellofresh_week >= '2021-W01')
  WHERE hellofresh_week <= (SELECT affected_week FROM params)
  QUALIFY hellofresh_week = (SELECT affected_week FROM params)
),
countries AS (
  SELECT business_unit as country
  FROM payments_hf.business_units
  WHERE ARRAY_CONTAINS(reporting_cluster_array, (SELECT cluster FROM params))
),
curr AS (
  SELECT country,
    SUM(order_count) as orders,
    SUM(`2_PreDunningAR`) / NULLIF(SUM(order_count), 0) as rate
  FROM payments_hf.payments_p0_metrics_box_candidates
  CROSS JOIN weeks w
  WHERE hellofresh_week = w.affected_week
    AND country IN (SELECT country FROM countries)
    
  GROUP BY country
),
prev AS (
  SELECT country,
    SUM(order_count) as orders,
    SUM(`2_PreDunningAR`) / NULLIF(SUM(order_count), 0) as rate
  FROM payments_hf.payments_p0_metrics_box_candidates
  CROSS JOIN weeks w
  WHERE hellofresh_week = w.prev_week
    AND country IN (SELECT country FROM countries)
    
  GROUP BY country
),
combined AS (
  SELECT 
    c.country,
    ROUND(c.rate * 100, 2) as curr_rate_pct,
    ROUND(p.rate * 100, 2) as prev_rate_pct,
    ROUND((c.rate - p.rate) / NULLIF(p.rate, 0) * 100, 2) as change_pct,
    c.orders as curr_volume,
    p.orders as prev_volume,
    ABS(c.orders * (c.rate - p.rate)) as contribution
  FROM curr c
  JOIN prev p ON c.country = p.country
),
ranked AS (
  SELECT *,
    ROW_NUMBER() OVER (ORDER BY contribution DESC) as rank_contribution,
    ROW_NUMBER() OVER (ORDER BY ABS(change_pct) DESC) as rank_change
  FROM combined
),
top_countries AS (
  SELECT * FROM ranked
  WHERE rank_contribution <= 4 OR rank_change <= 4
  ORDER BY rank_contribution
  LIMIT 8
)
SELECT country, curr_rate_pct, prev_rate_pct, change_pct, curr_volume, prev_volume,
  CASE WHEN ABS(change_pct) > 2.5 THEN '⚠️' ELSE '' END as flag,
  rank_contribution, rank_change
FROM top_countries
ORDER BY change_pct ASC

```

</details>

<details>
<summary>L1b: Dimension Scan</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'RTE' as cluster,
    '2_PreDunningAR' as ar_metric, '1_1_Overall Total Box Candidates' as metric_group
)
SELECT dimension_name, dimension_value,
  ROUND(SUM(current_metric_value_numerator) / NULLIF(SUM(current_metric_value_denominator), 0) * 100, 2) as curr_rate_pct,
  ROUND(SUM(prev_metric_value_numerator) / NULLIF(SUM(prev_metric_value_denominator), 0) * 100, 2) as prev_rate_pct,
  ROUND((SUM(current_metric_value_numerator) / NULLIF(SUM(current_metric_value_denominator), 0) - 
         SUM(prev_metric_value_numerator) / NULLIF(SUM(prev_metric_value_denominator), 0)) / 
         NULLIF(SUM(prev_metric_value_numerator) / NULLIF(SUM(prev_metric_value_denominator), 0), 0) * 100, 2) as change_pct,
  SUM(current_metric_value_denominator) as curr_volume,
  SUM(prev_metric_value_denominator) as prev_volume
FROM payments_hf.payments_p0_metrics
WHERE metric_name = (SELECT ar_metric FROM params) 
  AND metric_group = (SELECT metric_group FROM params)
  AND date_granularity = 'WEEK' 
  AND date_value = (SELECT affected_week FROM params)
  AND reporting_cluster = (SELECT cluster FROM params)
  AND dimension_name IN ('PaymentMethod', 'PaymentProvider')
GROUP BY dimension_name, dimension_value
ORDER BY dimension_name, change_pct ASC

```

</details>

<details>
<summary>L3: Related Metrics</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'RTE' as cluster,
    '1_1_Overall Total Box Candidates' as metric_group
)
SELECT metric_name,
  ROUND(SUM(current_metric_value_numerator) / NULLIF(SUM(current_metric_value_denominator), 0) * 100, 2) as curr_rate_pct,
  ROUND(SUM(prev_metric_value_numerator) / NULLIF(SUM(prev_metric_value_denominator), 0) * 100, 2) as prev_rate_pct,
  ROUND((SUM(current_metric_value_numerator) / NULLIF(SUM(current_metric_value_denominator), 0) - 
         SUM(prev_metric_value_numerator) / NULLIF(SUM(prev_metric_value_denominator), 0)) /
         NULLIF(SUM(prev_metric_value_numerator) / NULLIF(SUM(prev_metric_value_denominator), 0), 0) * 100, 2) as change_pct,
  SUM(current_metric_value_denominator) as curr_volume,
  SUM(prev_metric_value_denominator) as prev_volume
FROM payments_hf.payments_p0_metrics
WHERE metric_group = (SELECT metric_group FROM params)
  AND dimension_name = '_Overall' 
  AND date_granularity = 'WEEK' 
  AND date_value = (SELECT affected_week FROM params)
  AND reporting_cluster = (SELECT cluster FROM params)
  AND metric_name IN ('1_FirstRunAR', '2_PreDunningAR', '3_PostDunningAR', '6_PaymentApprovalRate')
GROUP BY metric_name
ORDER BY metric_name

```

</details>

---

*Report: 2026-04-08*
