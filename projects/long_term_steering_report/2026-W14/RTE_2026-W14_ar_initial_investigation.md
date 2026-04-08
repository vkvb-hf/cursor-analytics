# AR Initial (LL0) Investigation: RTE 2026-W14

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 91.4% → 90.89% (-0.56%)  
**Volume:** 31,900 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) declined from 91.4% to 90.89% (-0.56%) in W14, continuing a downward trend from 93.59% in W09, though the change is flagged as not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Sustained decline from W09 (93.59%) to W14 (90.89%) | -2.70pp over 5 weeks | ⚠️ |
| L1: Country Variance | 4 countries exceed ±2.5% threshold | TO -4.77%, TK +9.33% | ⚠️ |
| L1: Dimension Scan | No payment method or provider exceeds threshold | Max change -0.80% (Credit Card) | ✅ |
| L2: Root Cause - TO | Adyen -6.94%, Insufficient Funds +2.85pp | Primary driver of decline | ⚠️ |
| L3: Related Metrics | All AR metrics declining in parallel | FirstRunAR -0.69%, PostDunningAR -0.44% | ⚠️ |
| Mix Shift | TK volume dropped 33.3% (348→232) | Low-AR country shrinking | ✅ |

**Key Findings:**
- TO (Tonga) is the primary negative contributor with AR dropping 4.77% (71.79%→68.36%), driven by Adyen credit card declines and a +2.85pp increase in "Insufficient Funds" decline reasons
- Three countries showed significant improvement: TK (+9.33%), TV (+4.98%), and TT (+2.62%), all showing reduced "Insufficient Funds" declines
- Volume declined 12.4% week-over-week (36,413→31,900 orders), consistent with the 8-week downward volume trend from 52,390 in W07
- The decline pattern appears across all related metrics (FirstRunAR, PostDunningAR, PaymentApprovalRate), suggesting a systemic issue rather than isolated to pre-dunning
- Credit card payments show the largest absolute volume (20,181 orders) with a -0.80% rate change, though below the significance threshold

**Action:** Monitor — The change is not statistically significant, and improving countries (TK, TV, TT) partially offset TO's decline. Continue tracking the sustained downward trend and monitor TO's Adyen + Insufficient Funds pattern for persistence in W15.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % (vs prior week) |
|------|--------|--------|---------------------|
| 2026-W14 | 90.89% | 31,900 | -0.56% ← REPORTED CHANGE |
| 2026-W13 | 91.4% | 36,413 | -1.25% |
| 2026-W12 | 92.56% | 42,779 | +0.05% |
| 2026-W11 | 92.51% | 46,365 | -0.24% |
| 2026-W10 | 92.73% | 48,166 | -0.92% |
| 2026-W09 | 93.59% | 46,087 | +0.47% |
| 2026-W08 | 93.15% | 46,567 | +0.33% |
| 2026-W07 | 92.84% | 52,390 | +nan% |

---

## L1: Country Breakdown

| Country | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|---------|--------|--------|----------|----------|----------|------|
| TO | 68.36% | 71.79% | -4.77% | 629 | 677 | ⚠️ |
| FJ | 82.6% | 83.13% | -0.64% | 38,808 | 39,892 |  |
| YE | 75.74% | 76.16% | -0.55% | 6,365 | 6,413 |  |
| CF | 84.9% | 84.67% | +0.27% | 7,763 | 7,705 |  |
| TT | 94.46% | 92.05% | +2.62% | 722 | 742 | ⚠️ |
| TV | 91.67% | 87.32% | +4.98% | 408 | 481 | ⚠️ |
| TK | 89.22% | 81.61% | +9.33% | 232 | 348 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TO, TT, TV, TK

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Credit Card | 89.99% | 90.71% | -0.80% | 20,181 | 22,733 |  |
| Paypal | 95.65% | 95.97% | -0.33% | 3,814 | 4,167 |  |
| Apple Pay | 90.02% | 90.08% | -0.07% | 7,026 | 7,965 |  |
| Others | 97.95% | 96.06% | +1.97% | 879 | 1,548 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 77.55% | 0.0% | +nan% | 49 | 16 |  |
| Adyen | 89.21% | 89.79% | -0.65% | 9,422 | 9,337 |  |
| Braintree | 91.68% | 92.02% | -0.38% | 11,390 | 21,813 |  |
| ProcessOut | 91.53% | 91.32% | +0.23% | 10,970 | 4,469 |  |
| No Payment | 100.0% | 95.76% | +4.43% | 69 | 778 | ⚠️ |

---

## L2: TO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.0% | 16.67% | -100.00% | 0 | 6 | ⚠️ |
| bancontact | 0.0% | 100.0% | -100.00% | 0 | 1 | ⚠️ |
| sepadirectdebit | 0.0% | 100.0% | -100.00% | 0 | 1 | ⚠️ |
| credit_card | 64.99% | 69.68% | -6.74% | 377 | 409 | ⚠️ |
| applepay | 62.09% | 65.19% | -4.75% | 153 | 158 |  |
| paypal | 90.32% | 92.93% | -2.81% | 93 | 99 |  |
| cashcredit | 100.0% | 100.0% | +0.00% | 6 | 3 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.0% | 0.0% | +nan% | 0 | 5 |  |
| Adyen | 64.99% | 69.83% | -6.94% | 377 | 411 | ⚠️ |
| Braintree | 72.76% | 75.88% | -4.10% | 246 | 257 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 6 | 4 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 430 | 486 | 68.36% | 71.79% | -3.42 |
| Insufficient Funds | 109 | 98 | 17.33% | 14.48% | +2.85 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 45 | 43 | 7.15% | 6.35% | +0.80 |
| Other reasons | 45 | 50 | 7.15% | 7.39% | -0.23 |

**Root Cause:** None + Adyen + Insufficient

---

## L2: TT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 14.29% | 0.0% | +nan% | 7 | 0 |  |
| sepadirectdebit | 100.0% | 0.0% | +nan% | 1 | 0 |  |
| None | 0.0% | 14.29% | -100.00% | 0 | 14 | ⚠️ |
| cashcredit | 0.0% | 100.0% | -100.00% | 0 | 2 | ⚠️ |
| credit_card | 68.89% | 78.95% | -12.74% | 45 | 57 | ⚠️ |
| klarna | 87.27% | 88.71% | -1.62% | 55 | 62 |  |
| ideal | 100.0% | 99.23% | +0.78% | 533 | 520 |  |
| paypal | 68.18% | 66.67% | +2.27% | 22 | 21 |  |
| applepay | 89.83% | 74.24% | +21.00% | 59 | 66 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.0% | 0.0% | +nan% | 6 | 11 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 1 | 4 |  |
| Adyen | 96.69% | 96.25% | +0.45% | 634 | 640 |  |
| Braintree | 83.95% | 72.41% | +15.93% | 81 | 87 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 682 | 683 | 94.46% | 92.05% | +2.41 |
| Other reasons | 2 | 12 | 0.28% | 1.62% | -1.34 |
| PROVIDER_ERROR: failure executing charge with provider | 0 | 8 | 0.00% | 1.08% | -1.08 |
| Insufficient Funds | 14 | 22 | 1.94% | 2.96% | -1.03 |
| Unknown | 6 | 0 | 0.83% | 0.00% | +0.83 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 18 | 17 | 2.49% | 2.29% | +0.20 |

**Root Cause:** None + Braintree + Other

---

## L2: TV Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| cashcredit | 100.0% | 100.0% | +0.00% | 2 | 6 |  |
| applepay | 82.47% | 81.91% | +0.68% | 97 | 94 |  |
| klarna | 99.01% | 98.14% | +0.89% | 202 | 215 |  |
| credit_card | 85.71% | 77.42% | +10.71% | 98 | 155 | ⚠️ |
| paypal | 88.89% | 54.55% | +62.96% | 9 | 11 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 2 | 6 |  |
| Braintree | 83.02% | 79.05% | +5.02% | 106 | 105 | ⚠️ |
| Adyen | 94.67% | 89.46% | +5.82% | 300 | 370 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 374 | 420 | 91.67% | 87.32% | +4.35 |
| Insufficient Funds | 29 | 46 | 7.11% | 9.56% | -2.46 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 2 | 8 | 0.49% | 1.66% | -1.17 |
| Other reasons | 3 | 7 | 0.74% | 1.46% | -0.72 |

**Root Cause:** credit_card + Braintree + Insufficient

---

## L2: TK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.0% | 0.0% | +nan% | 0 | 1 |  |
| cashcredit | 100.0% | 100.0% | +0.00% | 2 | 4 |  |
| credit_card | 88.65% | 83.5% | +6.17% | 141 | 200 | ⚠️ |
| applepay | 88.61% | 79.69% | +11.19% | 79 | 128 | ⚠️ |
| paypal | 100.0% | 73.33% | +36.36% | 10 | 15 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.0% | 0.0% | +nan% | 0 | 1 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 2 | 4 |  |
| Adyen | 88.65% | 83.5% | +6.17% | 141 | 200 | ⚠️ |
| Braintree | 89.89% | 79.02% | +13.75% | 89 | 143 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 207 | 284 | 89.22% | 81.61% | +7.61 |
| Insufficient Funds | 22 | 51 | 9.48% | 14.66% | -5.17 |
| Other reasons | 1 | 7 | 0.43% | 2.01% | -1.58 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 2 | 6 | 0.86% | 1.72% | -0.86 |

**Root Cause:** credit_card + Adyen + Insufficient

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.49% | 89.1% | -0.69% | 31,900 | 36,413 |  |
| 2_PreDunningAR | 90.89% | 91.4% | -0.56% | 31,900 | 36,413 |  |
| 3_PostDunningAR | 91.25% | 91.65% | -0.44% | 31,900 | 36,413 |  |
| 6_PaymentApprovalRate | 91.43% | 91.79% | -0.39% | 31,900 | 36,413 |  |

---

## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | Low (>85%) | 39,892 | 38,808 | -2.7% | Stable |
| CF | Low (>85%) | 7,705 | 7,763 | +0.8% | Stable |
| YE | Low (>85%) | 6,413 | 6,365 | -0.7% | Stable |
| TT | High (>92%) | 742 | 722 | -2.7% | Stable |
| TO | Low (>85%) | 677 | 629 | -7.1% | Stable |
| TZ | Low (>85%) | 632 | 536 | -15.2% | Stable |
| TV | Medium (>85%) | 481 | 408 | -15.2% | Stable |
| TK | Low (>85%) | 348 | 232 | -33.3% | ⚠️ Volume drop |

---

## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TO | ↓ -4.77% | None -100.0% | Adyen -6.9% | Insufficient Funds +2.85pp | None + Adyen + Insufficient |
| TT | ↑ +2.62% | None -100.0% | Braintree +15.9% | Other reasons -1.34pp | None + Braintree + Other |
| TV | ↑ +4.98% | credit_card +10.7% | Braintree +5.0% | Insufficient Funds -2.46pp | credit_card + Braintree + Insufficient |
| TK | ↑ +9.33% | credit_card +6.2% | Adyen +6.2% | Insufficient Funds -5.17pp | credit_card + Adyen + Insufficient |

---

## SQL Queries

<details>
<summary>L0: 8-Week Trend</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'RTE' as cluster,
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
  SELECT '2026-W14' as affected_week, 'RTE' as cluster,
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
  SELECT '2026-W14' as affected_week, 'RTE' as cluster,
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
