# AR Initial (LL0) Investigation: WL 2026-W14

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 89.23% → 89.84% (+0.68%)  
**Volume:** 12,781 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Pre-Dunning Acceptance Rate (Initial Charges) for WL cluster improved slightly from 89.23% to 89.84% (+0.68%) in 2026-W14, representing a partial recovery after two consecutive weeks of decline, though the change is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate recovering from W13 low | +0.68% | ✅ |
| L1: Country Variance | 3 countries exceed ±2.5% threshold (GN, AO, ER) | GN -3.50%, AO -2.99%, ER +3.53% | ⚠️ |
| L1: Payment Method | "Others" category declined significantly | -6.62% | ⚠️ |
| L1: Payment Provider | Braintree improved, ProcessOut declined | Braintree +3.17%, ProcessOut -2.31% | ⚠️ |
| L2: Root Causes | Insufficient Funds driving declines in GN/AO | +1.79pp (GN), +2.34pp (AO) | ⚠️ |
| L3: Related Metrics | All AR metrics improved in parallel | +0.67% to +1.03% | ✅ |

**Key Findings:**
- **Volume decline continues:** Total order volume dropped from 12,904 to 12,781 (-1.0%), continuing an 8-week downward trend from 15,670 orders in W07
- **GN underperformance:** GN saw a -3.50% rate decline (82.6% → 79.7%) with Insufficient Funds increasing by +1.79pp, coupled with a significant -14.3% volume drop
- **AO Apple Pay/ProcessOut issue:** AO declined -2.99% driven specifically by Apple Pay (-9.05%) via ProcessOut (-9.05%), with Insufficient Funds rising +2.34pp
- **ER positive outlier:** ER improved +3.53% (60.82% → 62.97%) with PayPal showing strong gains (+8.61%) and "Other reasons" declines dropping -1.35pp
- **Braintree recovery:** Braintree improved +3.17% globally (89.93% → 92.79%), partially offsetting ProcessOut weakness

**Action:** **Monitor** - The overall metric change is not significant and represents a recovery from W13. However, continue monitoring GN and AO for sustained Insufficient Funds increases, and investigate the ProcessOut/Apple Pay combination in AO if the trend persists next week.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % (vs prior week) |
|------|--------|--------|---------------------|
| 2026-W14 | 89.84% | 12,781 | +0.68% ← REPORTED CHANGE |
| 2026-W13 | 89.23% | 12,904 | -1.39% |
| 2026-W12 | 90.49% | 13,906 | -1.63% |
| 2026-W11 | 91.99% | 14,300 | +1.10% |
| 2026-W10 | 90.99% | 14,879 | -0.32% |
| 2026-W09 | 91.28% | 15,292 | +0.60% |
| 2026-W08 | 90.74% | 15,382 | +0.86% |
| 2026-W07 | 89.97% | 15,670 | +nan% |

---

## L1: Country Breakdown

| Country | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|---------|--------|--------|----------|----------|----------|------|
| GN | 79.7% | 82.6% | -3.50% | 1,823 | 2,126 | ⚠️ |
| AO | 63.95% | 65.92% | -2.99% | 1,559 | 1,429 | ⚠️ |
| CK | 79.09% | 81.08% | -2.45% | 3,386 | 3,752 |  |
| ER | 62.97% | 60.82% | +3.53% | 5,023 | 5,197 | ⚠️ |

**Countries exceeding ±2.5% threshold:** GN, AO, ER

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Others | 89.83% | 96.2% | -6.62% | 59 | 79 | ⚠️ |
| Paypal | 94.88% | 95.06% | -0.19% | 1,561 | 1,518 |  |
| Apple Pay | 90.92% | 90.95% | -0.04% | 3,963 | 3,944 |  |
| Credit Card | 88.15% | 87.03% | +1.29% | 7,198 | 7,363 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| ProcessOut | 87.62% | 89.69% | -2.31% | 3,877 | 3,995 |  |
| Adyen | 84.72% | 86.25% | -1.77% | 2,160 | 2,334 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 22 | 66 |  |
| Unknown | 76.92% | 75.0% | +2.56% | 26 | 12 | ⚠️ |
| Braintree | 92.79% | 89.93% | +3.17% | 6,696 | 6,497 | ⚠️ |

---

## L2: GN Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 100.0% | 0.0% | +nan% | 28 | 0 |  |
| cashcredit | 100.0% | 0.0% | +nan% | 9 | 0 |  |
| None | 0.0% | 100.0% | -100.00% | 0 | 31 | ⚠️ |
| applepay | 78.31% | 81.41% | -3.80% | 890 | 1,124 |  |
| credit_card | 74.85% | 77.51% | -3.44% | 648 | 676 |  |
| paypal | 94.35% | 96.95% | -2.68% | 248 | 295 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 100.0% | 0.0% | +nan% | 15 | 0 |  |
| Braintree | 81.81% | 84.64% | -3.34% | 1,138 | 1,419 |  |
| Adyen | 75.23% | 77.51% | -2.95% | 658 | 676 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 12 | 31 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,453 | 1,756 | 79.70% | 82.60% | -2.89 |
| Insufficient Funds | 283 | 292 | 15.52% | 13.73% | +1.79 |
| Other reasons | 22 | 10 | 1.21% | 0.47% | +0.74 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 65 | 68 | 3.57% | 3.20% | +0.37 |

**Root Cause:** None + Insufficient

---

## L2: AO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.0% | 0.0% | +nan% | 1 | 0 |  |
| applepay | 64.06% | 70.44% | -9.05% | 512 | 504 | ⚠️ |
| credit_card | 58.74% | 59.22% | -0.82% | 841 | 748 |  |
| cashcredit | 100.0% | 100.0% | +0.00% | 4 | 5 |  |
| paypal | 85.07% | 80.81% | +5.27% | 201 | 172 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.0% | 0.0% | +nan% | 1 | 0 |  |
| ProcessOut | 64.06% | 70.44% | -9.05% | 512 | 504 | ⚠️ |
| Adyen | 58.74% | 59.22% | -0.82% | 841 | 748 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 4 | 5 |  |
| Braintree | 85.07% | 80.81% | +5.27% | 201 | 172 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Insufficient Funds | 486 | 412 | 31.17% | 28.83% | +2.34 |
| 1. SUCCESSFULL | 997 | 942 | 63.95% | 65.92% | -1.97 |
| Other reasons | 27 | 28 | 1.73% | 1.96% | -0.23 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 48 | 47 | 3.08% | 3.29% | -0.21 |
| PROVIDER_ERROR: failure executing charge with provider | 1 | 0 | 0.06% | 0.00% | +0.06 |

**Root Cause:** applepay + ProcessOut + Insufficient

---

## L2: ER Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.0% | 0.0% | +nan% | 5 | 0 |  |
| venmo | 50.0% | 0.0% | +nan% | 2 | 1 |  |
| None | 0.0% | 100.0% | -100.00% | 0 | 2 | ⚠️ |
| cashcredit | 100.0% | 100.0% | +0.00% | 11 | 7 |  |
| applepay | 71.11% | 69.85% | +1.81% | 1,409 | 1,403 |  |
| credit_card | 57.39% | 55.81% | +2.84% | 3,077 | 3,288 |  |
| paypal | 73.8% | 67.94% | +8.61% | 519 | 496 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.0% | 0.0% | +nan% | 5 | 0 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 11 | 9 |  |
| ProcessOut | 59.31% | 57.91% | +2.43% | 2,846 | 3,036 |  |
| Braintree | 67.75% | 64.78% | +4.58% | 2,161 | 2,152 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 3,163 | 3,161 | 62.97% | 60.82% | +2.15 |
| Other reasons | 551 | 640 | 10.97% | 12.31% | -1.35 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 338 | 378 | 6.73% | 7.27% | -0.54 |
| Insufficient Funds | 966 | 1,018 | 19.23% | 19.59% | -0.36 |
| Unknown | 4 | 0 | 0.08% | 0.00% | +0.08 |
| PROVIDER_ERROR: failure executing charge with provider | 1 | 0 | 0.02% | 0.00% | +0.02 |

**Root Cause:** None + Other

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 86.39% | 85.52% | +1.03% | 12,781 | 12,904 |  |
| 2_PreDunningAR | 89.84% | 89.23% | +0.68% | 12,781 | 12,904 |  |
| 3_PostDunningAR | 90.08% | 89.48% | +0.67% | 12,781 | 12,904 |  |
| 6_PaymentApprovalRate | 90.24% | 89.64% | +0.67% | 12,781 | 12,904 |  |

---

## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Low (>85%) | 5,197 | 5,023 | -3.3% | Stable |
| CK | Low (>85%) | 3,752 | 3,386 | -9.8% | Stable |
| MR | Low (>85%) | 3,600 | 3,558 | -1.2% | Stable |
| CG | Medium (>85%) | 2,930 | 2,951 | +0.7% | Stable |
| KN | High (>92%) | 2,374 | 2,973 | +25.2% | Stable |
| GN | Low (>85%) | 2,126 | 1,823 | -14.3% | Stable |
| AO | Low (>85%) | 1,429 | 1,559 | +9.1% | Stable |

---

## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| GN | ↓ -3.50% | None -100.0% | → Stable | Insufficient Funds +1.79pp | None + Insufficient |
| AO | ↓ -2.99% | applepay -9.1% | ProcessOut -9.1% | Insufficient Funds +2.34pp | applepay + ProcessOut + Insufficient |
| ER | ↑ +3.53% | None -100.0% | → Stable | Other reasons -1.35pp | None + Other |

---

## SQL Queries

<details>
<summary>L0: 8-Week Trend</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'WL' as cluster,
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
  SELECT '2026-W14' as affected_week, 'WL' as cluster
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
  SELECT '2026-W14' as affected_week, 'WL' as cluster,
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
  SELECT '2026-W14' as affected_week, 'WL' as cluster,
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
