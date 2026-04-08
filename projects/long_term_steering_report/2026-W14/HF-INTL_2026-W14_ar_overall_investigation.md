# AR Overall Investigation: HF-INTL 2026-W14

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 94.16% → 93.64% (-0.55%)  
**Volume:** 784,389 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate for HF-INTL declined from 94.16% to 93.64% (-0.55%) in 2026-W14, representing a statistically non-significant change across 784,389 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | First authorization attempt | -0.86% | ⚠️ |
| 2_PreDunningAR | Pre-dunning recovery | -0.55% | ⚠️ |
| 3_PostDunningAR | Post-dunning recovery | -0.42% | ⚠️ |
| 6_PaymentApprovalRate | Final approval | -0.13% | ✅ |

**Key Findings:**
- **Denmark (DK)** experienced the largest decline at -2.78%, driven by a 100% drop in "None" payment method volume and a +2.09pp increase in "Insufficient Funds" declines
- **Austria (AT)** declined -2.51%, similarly impacted by loss of "None" payment method volume and +1.51pp increase in Insufficient Funds
- **Switzerland (CH)** improved +2.98%, primarily through Apple Pay performance increasing +5.35% and Insufficient Funds declines decreasing by -1.96pp
- **Norway (NO)** shows a major volume shift with -46.6% order reduction, though rate impact was -2.24%
- All payment providers showed slight declines (-0.40% to -0.83%), with no single provider identified as the primary driver

**Action:** **Monitor** - The change is not statistically significant. Continue tracking DK and AT for sustained "Insufficient Funds" elevation over the next 1-2 weeks before escalating.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % (vs prior week) |
|------|--------|--------|---------------------|
| 2026-W14 | 93.64% | 784,389 | -0.55% ← REPORTED CHANGE |
| 2026-W13 | 94.16% | 842,480 | -0.47% |
| 2026-W12 | 94.6% | 877,187 | -0.32% |
| 2026-W11 | 94.9% | 897,106 | +1.17% |
| 2026-W10 | 93.8% | 916,831 | +0.72% |
| 2026-W09 | 93.13% | 896,537 | -0.45% |
| 2026-W08 | 93.55% | 884,970 | -0.78% |
| 2026-W07 | 94.29% | 920,370 | +nan% |

---

## L1: Country Breakdown

| Country | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|---------|--------|--------|----------|----------|----------|------|
| DK | 94.03% | 96.72% | -2.78% | 30,036 | 41,607 | ⚠️ |
| AT | 92.8% | 95.19% | -2.51% | 12,458 | 14,386 | ⚠️ |
| NO | 90.27% | 92.35% | -2.24% | 13,551 | 25,359 |  |
| BE | 94.01% | 95.32% | -1.38% | 74,093 | 75,558 |  |
| DE | 96.44% | 97.22% | -0.80% | 205,169 | 225,448 |  |
| FR | 92.95% | 93.7% | -0.80% | 158,169 | 161,317 |  |
| CH | 93.93% | 91.21% | +2.98% | 2,174 | 2,401 | ⚠️ |

**Countries exceeding ±2.5% threshold:** DK, AT, CH

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 87.52% | 88.27% | -0.85% | 105,676 | 113,387 |  |
| Credit Card | 91.6% | 92.31% | -0.77% | 354,933 | 350,055 |  |
| Paypal | 97.23% | 97.66% | -0.44% | 193,296 | 210,289 |  |
| Others | 98.85% | 97.61% | +1.27% | 130,484 | 168,749 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| ProcessOut | 91.13% | 91.89% | -0.83% | 226,595 | 247,011 |  |
| Braintree | 94.19% | 94.69% | -0.53% | 292,920 | 318,019 |  |
| Adyen | 95.21% | 95.59% | -0.40% | 258,061 | 270,063 |  |
| No Payment | 100.0% | 99.94% | +0.06% | 4,352 | 5,257 |  |
| Unknown | 84.32% | 82.07% | +2.74% | 2,461 | 2,130 | ⚠️ |

---

## L2: DK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 70.59% | 0.0% | +nan% | 34 | 0 |  |
| None | 0.0% | 97.71% | -100.00% | 0 | 18,900 | ⚠️ |
| applepay | 90.48% | 94.79% | -4.55% | 6,038 | 8,427 |  |
| credit_card | 94.92% | 96.55% | -1.69% | 22,890 | 12,829 |  |
| paypal | 94.78% | 95.74% | -1.00% | 901 | 1,245 |  |
| cashcredit | 100.0% | 100.0% | +0.00% | 173 | 206 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 62.5% | 78.13% | -20.00% | 24 | 32 | ⚠️ |
| Braintree | 91.04% | 94.91% | -4.08% | 6,939 | 9,672 |  |
| Adyen | 94.18% | 96.67% | -2.58% | 6,113 | 8,376 |  |
| ProcessOut | 95.19% | 97.48% | -2.34% | 16,787 | 23,320 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 173 | 207 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 28,242 | 40,241 | 94.03% | 96.72% | -2.69 |
| Insufficient Funds | 1,286 | 911 | 4.28% | 2.19% | +2.09 |
| Other reasons | 309 | 241 | 1.03% | 0.58% | +0.45 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 189 | 199 | 0.63% | 0.48% | +0.15 |
| Unknown | 10 | 15 | 0.03% | 0.04% | +0.00 |

**Root Cause:** None + Unknown + Insufficient

---

## L2: AT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.0% | 92.9% | -100.00% | 0 | 3,083 | ⚠️ |
| credit_card | 89.87% | 94.49% | -4.88% | 5,530 | 3,265 |  |
| applepay | 88.45% | 91.09% | -2.90% | 1,732 | 2,110 |  |
| paypal | 96.99% | 97.98% | -1.00% | 4,354 | 4,989 |  |
| sepadirectdebit | 99.23% | 99.52% | -0.30% | 775 | 835 |  |
| cashcredit | 100.0% | 100.0% | +0.00% | 65 | 102 |  |
| klarna | 100.0% | 100.0% | +0.00% | 2 | 2 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| ProcessOut | 89.58% | 93.1% | -3.78% | 4,116 | 4,696 |  |
| Adyen | 93.75% | 96.82% | -3.18% | 2,191 | 2,488 |  |
| Braintree | 94.56% | 95.93% | -1.43% | 6,086 | 7,099 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 65 | 103 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 11,561 | 13,694 | 92.80% | 95.19% | -2.39 |
| Insufficient Funds | 577 | 449 | 4.63% | 3.12% | +1.51 |
| Other reasons | 146 | 96 | 1.17% | 0.67% | +0.50 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 174 | 147 | 1.40% | 1.02% | +0.37 |

**Root Cause:** None + Insufficient

---

## L2: CH Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.0% | 0.0% | +nan% | 1 | 0 |  |
| cashcredit | 100.0% | 100.0% | +0.00% | 16 | 23 |  |
| paypal | 95.91% | 93.58% | +2.49% | 416 | 452 |  |
| credit_card | 94.22% | 91.79% | +2.65% | 1,385 | 1,523 |  |
| applepay | 90.45% | 85.86% | +5.35% | 356 | 403 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.0% | 0.0% | +nan% | 1 | 0 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 16 | 23 |  |
| ProcessOut | 94.52% | 92.34% | +2.36% | 985 | 1,057 |  |
| Adyen | 93.5% | 90.56% | +3.25% | 400 | 466 |  |
| Braintree | 93.39% | 89.94% | +3.84% | 772 | 855 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 2,042 | 2,190 | 93.93% | 91.21% | +2.72 |
| Insufficient Funds | 86 | 142 | 3.96% | 5.91% | -1.96 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 28 | 47 | 1.29% | 1.96% | -0.67 |
| Other reasons | 18 | 22 | 0.83% | 0.92% | -0.09 |

**Root Cause:** applepay + Insufficient

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.51% | 92.31% | -0.86% | 784,389 | 842,480 |  |
| 2_PreDunningAR | 93.64% | 94.16% | -0.55% | 784,389 | 842,480 |  |
| 3_PostDunningAR | 96.2% | 96.6% | -0.42% | 784,389 | 842,480 |  |
| 6_PaymentApprovalRate | 97.04% | 97.17% | -0.13% | 784,389 | 842,480 |  |

---

## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| DE | High (>92%) | 225,448 | 205,169 | -9.0% | Stable |
| GB | High (>92%) | 222,020 | 205,597 | -7.4% | Stable |
| FR | High (>92%) | 161,317 | 158,169 | -2.0% | Stable |
| NL | High (>92%) | 117,860 | 118,174 | +0.3% | Stable |
| AU | Medium (>85%) | 99,793 | 96,469 | -3.3% | Stable |
| BE | High (>92%) | 75,558 | 74,093 | -1.9% | Stable |
| DK | High (>92%) | 41,607 | 30,036 | -27.8% | ⚠️ Volume drop |
| SE | High (>92%) | 40,582 | 35,624 | -12.2% | Stable |
| NO | High (>92%) | 25,359 | 13,551 | -46.6% | ⚠️ Major mix shift |
| IE | Medium (>85%) | 19,567 | 18,775 | -4.0% | Stable |
| NZ | Medium (>85%) | 19,514 | 19,364 | -0.8% | Stable |
| AT | High (>92%) | 14,386 | 12,458 | -13.4% | Stable |
| LU | High (>92%) | 3,441 | 2,765 | -19.6% | Stable |
| CH | Medium (>85%) | 2,401 | 2,174 | -9.5% | Stable |

---

## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| DK | ↓ -2.78% | None -100.0% | Unknown -20.0% | Insufficient Funds +2.09pp | None + Unknown + Insufficient |
| AT | ↓ -2.51% | None -100.0% | → Stable | Insufficient Funds +1.51pp | None + Insufficient |
| CH | ↑ +2.98% | applepay +5.3% | → Stable | Insufficient Funds -1.96pp | applepay + Insufficient |

---

## SQL Queries

<details>
<summary>L0: 8-Week Trend</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'HF-INTL' as cluster,
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
  SELECT '2026-W14' as affected_week, 'HF-INTL' as cluster
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
  SELECT '2026-W14' as affected_week, 'HF-INTL' as cluster,
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
  SELECT '2026-W14' as affected_week, 'HF-INTL' as cluster,
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
