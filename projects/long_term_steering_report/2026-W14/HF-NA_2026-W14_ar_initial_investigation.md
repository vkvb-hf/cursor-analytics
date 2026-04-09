# AR Initial (LL0) Investigation: HF-NA 2026-W14

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 89.1% → 89.66% (+0.63%)  
**Volume:** 17,242 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate for HF-NA initial charges improved from 89.1% to 89.66% (+0.63%) in W14, a positive but statistically not significant change within normal weekly fluctuation range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (89.37%-90.82%) | +0.63% | ✅ |
| L1: Country Breakdown | US exceeds ±2.5% threshold (+4.43%) | +4.43% US | ⚠️ |
| L1: Payment Provider | Adyen shows -4.74% decline (low volume: 218) | -4.74% Adyen | ⚠️ |
| L2: US Deep-Dive | ProcessOut +6.32%, Apple Pay +5.21% | Positive shift | ✅ |
| L2: Decline Reasons | Insufficient Funds decreased -1.70pp | -1.70pp | ✅ |
| L3: Related Metrics | All AR metrics improved consistently (+0.54% to +0.77%) | Aligned | ✅ |

**Key Findings:**
- **US drove the improvement:** US acceptance rate increased +4.43% (66.77% → 69.72%), with ProcessOut showing +6.32% improvement and Apple Pay +5.21% improvement
- **Decline reasons improved:** "Insufficient Funds" declined by -1.70pp (21.42% → 19.72%) and "Refused" declined by -1.14pp (8.53% → 7.39%), indicating healthier payment attempts
- **Volume shift to ProcessOut:** ProcessOut volume increased from 8,584 to 11,351 orders (+32%) while Braintree decreased from 14,632 to 12,833 (-12%), suggesting intentional routing changes
- **Adyen volume drop:** Adyen volume decreased significantly from 668 to 218 orders (-67%) with rate declining -4.74%, though low volume limits impact
- **Canada stable:** CA showed minimal change (+0.18%) with consistent volume, not contributing to the overall shift

**Action:** **Monitor** - The improvement is positive but not statistically significant. Continue monitoring ProcessOut performance as volume shifts toward this provider. No escalation needed.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % (vs prior week) |
|------|--------|--------|---------------------|
| 2026-W14 | 89.66% | 17,242 | +0.63% ← REPORTED CHANGE |
| 2026-W13 | 89.1% | 16,215 | -0.60% |
| 2026-W12 | 89.64% | 21,080 | -1.30% |
| 2026-W11 | 90.82% | 21,784 | +1.09% |
| 2026-W10 | 89.84% | 25,446 | +0.25% |
| 2026-W09 | 89.62% | 25,208 | -0.19% |
| 2026-W08 | 89.79% | 25,674 | +0.47% |
| 2026-W07 | 89.37% | 28,927 | +nan% |

---

## L1: Country Breakdown

| Country | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|---------|--------|--------|----------|----------|----------|------|
| CA | 80.88% | 80.74% | +0.18% | 7,779 | 7,706 |  |
| US | 69.72% | 66.77% | +4.43% | 24,598 | 23,515 | ⚠️ |

**Countries exceeding ±2.5% threshold:** US

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Paypal | 90.25% | 90.77% | -0.58% | 1,333 | 1,268 |  |
| Credit Card | 89.43% | 89.0% | +0.49% | 9,781 | 9,096 |  |
| Others | 98.85% | 98.0% | +0.86% | 866 | 1,101 |  |
| Apple Pay | 88.43% | 86.78% | +1.90% | 5,262 | 4,750 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Adyen | 93.12% | 97.75% | -4.74% | 218 | 668 | ⚠️ |
| No Payment | 100.0% | 99.5% | +0.50% | 163 | 201 |  |
| Braintree | 88.7% | 88.18% | +0.59% | 6,980 | 7,739 |  |
| ProcessOut | 89.54% | 88.7% | +0.94% | 9,260 | 7,256 |  |
| Unknown | 98.39% | 95.16% | +3.40% | 621 | 351 | ⚠️ |

---

## L2: US Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 95.37% | 0.0% | +nan% | 216 | 0 |  |
| None | 0.0% | 93.2% | -100.00% | 0 | 103 | ⚠️ |
| venmo | 0.0% | 100.0% | -100.00% | 0 | 3 | ⚠️ |
| cashcredit | 100.0% | 100.0% | +0.00% | 198 | 196 |  |
| paypal | 70.41% | 69.37% | +1.50% | 1,967 | 1,985 |  |
| credit_card | 68.66% | 65.85% | +4.26% | 13,934 | 13,532 |  |
| applepay | 69.95% | 66.49% | +5.21% | 8,283 | 7,696 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Braintree | 61.86% | 62.49% | -1.01% | 12,833 | 14,632 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 198 | 198 |  |
| Unknown | 95.37% | 93.07% | +2.47% | 216 | 101 |  |
| ProcessOut | 77.59% | 72.97% | +6.32% | 11,351 | 8,584 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 17,150 | 15,700 | 69.72% | 66.77% | +2.96 |
| Insufficient Funds | 4,851 | 5,036 | 19.72% | 21.42% | -1.70 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 1,818 | 2,007 | 7.39% | 8.53% | -1.14 |
| Other reasons | 770 | 771 | 3.13% | 3.28% | -0.15 |
| Unknown | 4 | 0 | 0.02% | 0.00% | +0.02 |
| PROVIDER_ERROR: failure executing charge with provider | 5 | 1 | 0.02% | 0.00% | +0.02 |

**Root Cause:** None + ProcessOut + Insufficient

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.42% | 87.75% | +0.77% | 17,242 | 16,215 |  |
| 2_PreDunningAR | 89.66% | 89.1% | +0.63% | 17,242 | 16,215 |  |
| 3_PostDunningAR | 89.83% | 89.26% | +0.63% | 17,242 | 16,215 |  |
| 6_PaymentApprovalRate | 90.08% | 89.59% | +0.54% | 17,242 | 16,215 |  |

---

## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Low (>85%) | 23,515 | 24,598 | +4.6% | Stable |
| CA | Low (>85%) | 7,706 | 7,779 | +0.9% | Stable |

---

## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| US | ↑ +4.43% | None -100.0% | ProcessOut +6.3% | Insufficient Funds -1.70pp | None + ProcessOut + Insufficient |

---

## SQL Queries

<details>
<summary>L0: 8-Week Trend</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'HF-NA' as cluster,
    '2_PreDunningAR' as ar_metric, '1_2_Loyalty: LL0 (Initial charges)' as metric_group
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
  SELECT '2026-W14' as affected_week, 'HF-NA' as cluster
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
    AND customer_loyalty_segment = 'a. 0'
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
    AND customer_loyalty_segment = 'a. 0'
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
  SELECT '2026-W14' as affected_week, 'HF-NA' as cluster,
    '2_PreDunningAR' as ar_metric, '1_2_Loyalty: LL0 (Initial charges)' as metric_group
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
  SELECT '2026-W14' as affected_week, 'HF-NA' as cluster,
    '1_2_Loyalty: LL0 (Initial charges)' as metric_group
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

*Report: 2026-04-09*
