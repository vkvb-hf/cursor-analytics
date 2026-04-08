# AR Overall Investigation: US-HF 2026-W14

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 91.98% → 91.93% (-0.05%)  
**Volume:** 415,885 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Pre-Dunning Acceptance Rate for US-HF declined marginally from 91.98% to 91.93% (-0.05%) in 2026-W14, representing a statistically non-significant change across 415,885 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | 90.46% → 90.67% | +0.24% | ✅ |
| 2_PreDunningAR | 91.98% → 91.93% | -0.05% | ✅ |
| 3_PostDunningAR | 93.02% → 92.92% | -0.10% | ✅ |
| 6_PaymentApprovalRate | 93.59% → 93.63% | +0.05% | ✅ |

**Key Findings:**
- The -0.05% decline is within normal weekly fluctuation; the 8-week trend shows rates oscillating between 91.48% and 92.09%, with W14 at 91.93% being consistent with this range
- No countries exceeded the ±2.5% threshold; US (the only country in cluster) showed a minor -0.06% change
- PaymentProvider "Unknown" flagged with +8.23% improvement, but represents minimal volume (249 orders vs 131 prior week) with no material impact
- All payment methods showed stable performance: Others (-0.29%), PayPal (-0.11%), Credit Card (-0.06%), Apple Pay (+0.15%)
- Volume declined by ~2% week-over-week (415,885 vs 424,103), continuing a gradual downward trend observed since W07

**Action:** Monitor — No investigation required. The change is not statistically significant and falls within normal operating variance. Continue standard weekly monitoring.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % (vs prior week) |
|------|--------|--------|---------------------|
| 2026-W14 | 91.93% | 415,885 | -0.05% ← REPORTED CHANGE |
| 2026-W13 | 91.98% | 424,103 | +0.05% |
| 2026-W12 | 91.93% | 433,761 | -0.17% |
| 2026-W11 | 92.09% | 444,619 | +0.14% |
| 2026-W10 | 91.96% | 457,610 | +0.34% |
| 2026-W09 | 91.65% | 455,121 | +0.19% |
| 2026-W08 | 91.48% | 453,781 | -0.20% |
| 2026-W07 | 91.66% | 470,140 | +nan% |

---

## L1: Country Breakdown

| Country | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|---------|--------|--------|----------|----------|----------|------|
| US | 92.79% | 92.85% | -0.06% | 497,052 | 505,599 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Others | 98.37% | 98.65% | -0.29% | 2,202 | 2,230 |  |
| Paypal | 95.34% | 95.44% | -0.11% | 51,200 | 52,426 |  |
| Credit Card | 92.7% | 92.76% | -0.06% | 305,088 | 311,435 |  |
| Apple Pay | 84.57% | 84.44% | +0.15% | 57,395 | 58,012 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Braintree | 92.44% | 92.49% | -0.05% | 372,325 | 382,647 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 1,924 | 2,065 |  |
| Adyen | 95.05% | 94.99% | +0.07% | 364 | 399 |  |
| ProcessOut | 86.9% | 86.57% | +0.38% | 41,023 | 38,861 |  |
| Unknown | 86.75% | 80.15% | +8.23% | 249 | 131 | ⚠️ |

---



## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.67% | 90.46% | +0.24% | 415,885 | 424,103 |  |
| 2_PreDunningAR | 91.93% | 91.98% | -0.05% | 415,885 | 424,103 |  |
| 3_PostDunningAR | 92.92% | 93.02% | -0.10% | 415,885 | 424,103 |  |
| 6_PaymentApprovalRate | 93.63% | 93.59% | +0.05% | 415,885 | 424,103 |  |

---

## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 505,599 | 497,052 | -1.7% | Stable |

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
  SELECT '2026-W14' as affected_week, 'US-HF' as cluster,
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
  SELECT '2026-W14' as affected_week, 'US-HF' as cluster
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
  SELECT '2026-W14' as affected_week, 'US-HF' as cluster,
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
  SELECT '2026-W14' as affected_week, 'US-HF' as cluster,
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
