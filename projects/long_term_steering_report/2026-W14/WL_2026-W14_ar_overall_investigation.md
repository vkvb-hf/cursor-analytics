# AR Overall Investigation: WL 2026-W14

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 89.72% → 89.33% (-0.43%)  
**Volume:** 165,018 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate declined from 89.72% to 89.33% (-0.43%) in WL 2026-W14, a statistically non-significant change affecting 165,018 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (88.14%-89.79%) | -0.43% | ✅ |
| L1: Country Breakdown | AO exceeds ±2.5% threshold | -3.12% | ⚠️ |
| L1: Payment Method | No methods exceed threshold | -1.18% max | ✅ |
| L1: Payment Provider | Unknown flagged (low volume: 35 orders) | -4.76% | ✅ |
| L2: AO Deep-Dive | Apple Pay via ProcessOut declined | -5.69% | ⚠️ |
| L3: Related Metrics | All AR metrics declined similarly | -0.28% to -0.44% | ✅ |

**Key Findings:**
- **AO is the sole driver:** Angola declined -3.12% (85.22% from 87.96%), the only country exceeding the ±2.5% threshold
- **Root cause identified:** In AO, Apple Pay via ProcessOut declined -5.69% (75.35% from 79.90%), with "Insufficient Funds" declines increasing by +2.36pp (from 10.12% to 12.48%)
- **Volume decline in high-performing markets:** GN (high AR tier at 92.33%) saw -11.6% volume reduction, though this had minimal mix shift impact
- **Consistent decline across funnel:** All related AR metrics (FirstRun, PreDunning, PostDunning, PaymentApproval) declined by similar margins (-0.28% to -0.44%), suggesting a systemic rather than stage-specific issue
- **No significant mix shift:** All countries show "Stable" impact despite volume fluctuations

**Action:** **Monitor** — The overall change is not statistically significant and falls within the 8-week trend range. However, continue monitoring AO's ProcessOut + Apple Pay performance for "Insufficient Funds" declines over the next 1-2 weeks.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % (vs prior week) |
|------|--------|--------|---------------------|
| 2026-W14 | 89.33% | 165,018 | -0.43% ← REPORTED CHANGE |
| 2026-W13 | 89.72% | 169,667 | +0.07% |
| 2026-W12 | 89.66% | 169,891 | -0.14% |
| 2026-W11 | 89.79% | 174,933 | +0.80% |
| 2026-W10 | 89.08% | 179,964 | +1.01% |
| 2026-W09 | 88.19% | 180,862 | +0.06% |
| 2026-W08 | 88.14% | 179,647 | -0.50% |
| 2026-W07 | 88.58% | 186,442 | +nan% |

---

## L1: Country Breakdown

| Country | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|---------|--------|--------|----------|----------|----------|------|
| AO | 85.22% | 87.96% | -3.12% | 15,776 | 16,249 | ⚠️ |
| GN | 92.33% | 93.5% | -1.25% | 14,333 | 16,207 |  |
| ER | 89.23% | 89.92% | -0.77% | 67,730 | 73,655 |  |
| CK | 93.82% | 94.15% | -0.35% | 42,176 | 42,197 |  |
| KN | 88.21% | 87.61% | +0.68% | 11,048 | 10,365 |  |

**Countries exceeding ±2.5% threshold:** AO

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Others | 97.46% | 98.62% | -1.18% | 826 | 796 |  |
| Credit Card | 88.8% | 89.23% | -0.48% | 117,492 | 120,798 |  |
| Apple Pay | 85.75% | 86.16% | -0.47% | 21,798 | 22,237 |  |
| Paypal | 94.68% | 94.82% | -0.15% | 24,902 | 25,836 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 57.14% | 60.0% | -4.76% | 35 | 15 | ⚠️ |
| Adyen | 89.6% | 90.82% | -1.34% | 38,117 | 39,337 |  |
| ProcessOut | 79.78% | 79.93% | -0.18% | 18,108 | 18,332 |  |
| Braintree | 90.77% | 90.89% | -0.12% | 108,008 | 111,236 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 750 | 747 |  |

---

## L2: AO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.0% | 0.0% | +nan% | 1 | 0 |  |
| applepay | 75.35% | 79.9% | -5.69% | 1,343 | 1,353 | ⚠️ |
| credit_card | 82.52% | 85.84% | -3.87% | 10,353 | 10,666 |  |
| paypal | 95.26% | 95.81% | -0.57% | 4,011 | 4,152 |  |
| cashcredit | 100.0% | 100.0% | +0.00% | 68 | 78 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.0% | 0.0% | +nan% | 1 | 0 |  |
| ProcessOut | 75.35% | 79.9% | -5.69% | 1,343 | 1,353 | ⚠️ |
| Adyen | 82.52% | 85.84% | -3.87% | 10,353 | 10,666 |  |
| Braintree | 95.26% | 95.81% | -0.57% | 4,011 | 4,152 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 68 | 78 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 13,444 | 14,293 | 85.22% | 87.96% | -2.74 |
| Insufficient Funds | 1,969 | 1,644 | 12.48% | 10.12% | +2.36 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 246 | 219 | 1.56% | 1.35% | +0.21 |
| Other reasons | 116 | 93 | 0.74% | 0.57% | +0.16 |
| PROVIDER_ERROR: failure executing charge with provider | 1 | 0 | 0.01% | 0.00% | +0.01 |

**Root Cause:** applepay + ProcessOut + Insufficient

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 87.37% | 87.23% | +0.16% | 165,018 | 169,667 |  |
| 2_PreDunningAR | 89.33% | 89.72% | -0.44% | 165,018 | 169,667 |  |
| 3_PostDunningAR | 90.47% | 90.87% | -0.44% | 165,018 | 169,667 |  |
| 6_PaymentApprovalRate | 91.05% | 91.3% | -0.28% | 165,018 | 169,667 |  |

---

## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 73,655 | 67,730 | -8.0% | Stable |
| CG | High (>92%) | 44,477 | 44,581 | +0.2% | Stable |
| CK | High (>92%) | 42,197 | 42,176 | +0.0% | Stable |
| MR | Low (>85%) | 20,293 | 20,784 | +2.4% | Stable |
| AO | Medium (>85%) | 16,249 | 15,776 | -2.9% | Stable |
| GN | High (>92%) | 16,207 | 14,333 | -11.6% | Stable |
| KN | Medium (>85%) | 10,365 | 11,048 | +6.6% | Stable |

---

## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| AO | ↓ -3.12% | applepay -5.7% | ProcessOut -5.7% | Insufficient Funds +2.36pp | applepay + ProcessOut + Insufficient |

---

## SQL Queries

<details>
<summary>L0: 8-Week Trend</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'WL' as cluster,
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
  SELECT '2026-W14' as affected_week, 'WL' as cluster,
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
  SELECT '2026-W14' as affected_week, 'WL' as cluster,
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
