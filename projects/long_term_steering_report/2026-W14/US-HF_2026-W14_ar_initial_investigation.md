# AR Initial (LL0) Investigation: US-HF 2026-W14

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 87.53% → 88.84% (+1.50%)  
**Volume:** 11,716 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) for US-HF improved significantly from 87.53% to 88.84% (+1.50%) in 2026-W14, representing a recovery from the prior week's decline.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (87.53%-90.11%) | +1.31pp | ✅ |
| L1: Country Impact | US exceeded ±2.5% threshold (+4.43%) | +2.95pp | ⚠️ |
| L1: PaymentMethod | Apple Pay exceeded threshold (+2.60%) | +2.21pp | ⚠️ |
| L1: PaymentProvider | ProcessOut near threshold (+2.07%) | +1.82pp | ✅ |
| L2: US Deep-Dive | ProcessOut +6.32%, applepay +5.21% | Multiple drivers | ⚠️ |
| L3: Related Metrics | All AR metrics improved consistently (+1.37% to +1.53%) | Aligned | ✅ |

**Key Findings:**
- **ProcessOut volume shift driving improvement:** ProcessOut volume increased from 8,584 to 11,351 orders (+32%) with acceptance rate improving +6.32%, while Braintree volume decreased from 14,632 to 12,833 (-12%)
- **Decline reasons improved:** "Insufficient Funds" declines dropped by 1.70pp (21.42% → 19.72%) and "Refused" declines dropped by 1.14pp (8.53% → 7.39%)
- **Apple Pay showing strong recovery in US:** Apple Pay acceptance improved +5.21% (66.49% → 69.95%) with volume increasing from 7,696 to 8,283 orders
- **Volume remains suppressed:** Current week volume of 11,716 orders is significantly below 8-week highs (21,838 in W07), though up 7% from prior week
- **Credit card acceptance improved:** US credit card rate increased from 65.85% to 68.66% (+4.26%), the largest payment method by volume

**Action:** **Monitor** - The improvement appears driven by favorable mix shift toward ProcessOut and reduced decline rates. Continue monitoring ProcessOut performance and volume allocation between providers.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % (vs prior week) |
|------|--------|--------|---------------------|
| 2026-W14 | 88.84% | 11,716 | +1.50% ← REPORTED CHANGE |
| 2026-W13 | 87.53% | 10,955 | -1.30% |
| 2026-W12 | 88.68% | 14,786 | -1.59% |
| 2026-W11 | 90.11% | 15,868 | +0.95% |
| 2026-W10 | 89.26% | 19,259 | +0.01% |
| 2026-W09 | 89.25% | 18,657 | -0.36% |
| 2026-W08 | 89.57% | 18,802 | +0.88% |
| 2026-W07 | 88.79% | 21,838 | +nan% |

---

## L1: Country Breakdown

| Country | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|---------|--------|--------|----------|----------|----------|------|
| US | 69.72% | 66.77% | +4.43% | 24,598 | 23,515 | ⚠️ |

**Countries exceeding ±2.5% threshold:** US

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Paypal | 90.57% | 91.05% | -0.53% | 870 | 883 |  |
| Others | 98.1% | 98.4% | -0.31% | 315 | 187 |  |
| Credit Card | 89.22% | 88.26% | +1.09% | 6,531 | 6,192 |  |
| Apple Pay | 87.13% | 84.92% | +2.60% | 4,000 | 3,693 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 104 | 89 |  |
| Unknown | 97.16% | 96.91% | +0.26% | 211 | 97 |  |
| Braintree | 87.69% | 87.2% | +0.56% | 5,255 | 6,297 |  |
| ProcessOut | 89.36% | 87.54% | +2.07% | 6,146 | 4,472 |  |

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
| 1_FirstRunAR | 87.64% | 86.32% | +1.53% | 11,716 | 10,955 |  |
| 2_PreDunningAR | 88.84% | 87.53% | +1.50% | 11,716 | 10,955 |  |
| 3_PostDunningAR | 89.02% | 87.74% | +1.45% | 11,716 | 10,955 |  |
| 6_PaymentApprovalRate | 89.28% | 88.07% | +1.37% | 11,716 | 10,955 |  |

---

## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Low (>85%) | 23,515 | 24,598 | +4.6% | Stable |

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
  SELECT '2026-W14' as affected_week, 'US-HF' as cluster,
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
  SELECT '2026-W14' as affected_week, 'US-HF' as cluster,
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
  SELECT '2026-W14' as affected_week, 'US-HF' as cluster,
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

*Report: 2026-04-08*
