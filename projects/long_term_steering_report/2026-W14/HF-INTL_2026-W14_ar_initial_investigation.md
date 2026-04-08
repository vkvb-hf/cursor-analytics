# AR Initial (LL0) Investigation: HF-INTL 2026-W14

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 90.12% → 90.13% (+0.01%)  
**Volume:** 31,165 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) for HF-INTL remained essentially flat in 2026-W14, increasing marginally from 90.12% to 90.13% (+0.01%), a statistically insignificant change on 31,165 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate stable at ~90%, but volume declining from 52,771 (W07) to 31,165 (W14) | +0.01% | ✅ |
| L1: Country Impact | 6 countries exceeded ±2.5% threshold (LU -8.41%, DK -7.22%, AT -7.04%, DE -4.41%, AU -4.14%, CH +11.33%) | Mixed | ⚠️ |
| L1: Dimension Scan | Payment methods and providers stable; "Others" payment method +4.05% | <±2% | ✅ |
| L2: Root Cause | Multiple countries show "Insufficient Funds" as primary decline driver (+5-7pp) | Consistent pattern | ⚠️ |
| L3: Related Metrics | All funnel metrics (FirstRunAR, PostDunningAR, PaymentApprovalRate) stable within ±0.2% | <±1% | ✅ |

**Key Findings:**
- **Volume decline is significant:** Total order volume dropped 41% over 8 weeks (52,771 → 31,165), with DE (-22.1%), DK (-31.0%), NO (-46.4%), and AT (-25.6%) showing major volume drops
- **Insufficient Funds is the dominant decline reason:** LU (+7.61pp), AT (+5.67pp), DK (+5.55pp), and DE (+2.51pp) all show increased "Insufficient Funds" declines
- **Country-level rate declines offset each other:** While LU, DK, AT, DE, and AU declined, CH improved +11.33% and GB improved +2.37%, resulting in a flat overall rate
- **Adyen and Braintree showing localized issues:** Adyen dropped significantly in AT (-55.0%) and DK (-10.6%); Braintree declined in LU (-10.3%)
- **Credit card performance deteriorating:** DE credit cards dropped -18.4%, AT credit cards dropped -15.9%

**Action:** **Monitor** – The overall metric is stable and statistically insignificant. However, recommend tracking the "Insufficient Funds" trend across EU markets (LU, DK, AT, DE) and the continued volume decline pattern. If volume erosion continues or "Insufficient Funds" rates persist above 10%, escalate for customer payment method health assessment.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % (vs prior week) |
|------|--------|--------|---------------------|
| 2026-W14 | 90.13% | 31,165 | +0.01% ← REPORTED CHANGE |
| 2026-W13 | 90.12% | 34,718 | -1.28% |
| 2026-W12 | 91.29% | 39,323 | -0.29% |
| 2026-W11 | 91.56% | 42,918 | +1.24% |
| 2026-W10 | 90.44% | 47,739 | +2.70% |
| 2026-W09 | 88.06% | 46,648 | -2.38% |
| 2026-W08 | 90.21% | 46,404 | -1.62% |
| 2026-W07 | 91.7% | 52,771 | +nan% |

---

## L1: Country Breakdown

| Country | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|---------|--------|--------|----------|----------|----------|------|
| LU | 79.38% | 86.67% | -8.41% | 97 | 90 | ⚠️ |
| DK | 82.39% | 88.8% | -7.22% | 1,153 | 1,670 | ⚠️ |
| AT | 80.4% | 86.49% | -7.04% | 699 | 940 | ⚠️ |
| DE | 81.58% | 85.34% | -4.41% | 8,587 | 11,022 | ⚠️ |
| AU | 64.13% | 66.91% | -4.14% | 6,365 | 6,989 | ⚠️ |
| FR | 84.43% | 85.35% | -1.08% | 11,444 | 10,870 |  |
| GB | 80.08% | 78.23% | +2.37% | 14,083 | 14,166 |  |
| CH | 86.03% | 77.27% | +11.33% | 229 | 198 | ⚠️ |

**Countries exceeding ±2.5% threshold:** LU, DK, AT, DE, AU, CH

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Credit Card | 87.07% | 88.66% | -1.79% | 11,431 | 11,372 |  |
| Apple Pay | 86.33% | 86.1% | +0.27% | 9,417 | 10,325 |  |
| Paypal | 95.94% | 94.95% | +1.04% | 5,118 | 6,360 |  |
| Others | 98.04% | 94.22% | +4.05% | 5,199 | 6,661 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| ProcessOut | 85.91% | 86.51% | -0.69% | 12,528 | 13,986 |  |
| Adyen | 97.08% | 97.49% | -0.42% | 3,395 | 3,630 |  |
| Braintree | 91.09% | 90.91% | +0.20% | 13,267 | 15,307 |  |
| Unknown | 98.49% | 96.51% | +2.05% | 1,917 | 1,661 |  |
| No Payment | 100.0% | 97.76% | +2.29% | 58 | 134 |  |

---

## L2: LU Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 100.0% | 0.0% | +nan% | 11 | 0 |  |
| None | 0.0% | 100.0% | -100.00% | 0 | 20 | ⚠️ |
| applepay | 66.67% | 76.0% | -12.28% | 45 | 25 | ⚠️ |
| credit_card | 82.14% | 83.33% | -1.43% | 28 | 30 |  |
| sepadirectdebit | 100.0% | 100.0% | +0.00% | 3 | 3 |  |
| paypal | 100.0% | 91.67% | +9.09% | 10 | 12 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Braintree | 72.73% | 81.08% | -10.30% | 55 | 37 | ⚠️ |
| Adyen | 83.87% | 84.85% | -1.15% | 31 | 33 |  |
| Unknown | 100.0% | 100.0% | +0.00% | 11 | 20 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Insufficient Funds | 16 | 8 | 16.49% | 8.89% | +7.61 |
| 1. SUCCESSFULL | 77 | 78 | 79.38% | 86.67% | -7.29 |
| Other reasons | 0 | 2 | 0.00% | 2.22% | -2.22 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 4 | 2 | 4.12% | 2.22% | +1.90 |

**Root Cause:** None + Braintree + Insufficient

---

## L2: DK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 96.0% | 0.0% | +nan% | 25 | 0 |  |
| None | 0.0% | 89.96% | -100.00% | 0 | 687 | ⚠️ |
| applepay | 77.39% | 86.54% | -10.57% | 460 | 661 | ⚠️ |
| credit_card | 85.2% | 91.23% | -6.60% | 642 | 285 | ⚠️ |
| cashcredit | 100.0% | 100.0% | +0.00% | 4 | 10 |  |
| paypal | 86.36% | 85.19% | +1.38% | 22 | 27 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Adyen | 85.0% | 95.12% | -10.64% | 20 | 41 | ⚠️ |
| Braintree | 77.8% | 86.48% | -10.04% | 482 | 688 | ⚠️ |
| ProcessOut | 85.42% | 90.13% | -5.23% | 631 | 902 | ⚠️ |
| No Payment | 100.0% | 100.0% | +0.00% | 4 | 11 |  |
| Unknown | 93.75% | 89.29% | +5.00% | 16 | 28 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 950 | 1,483 | 82.39% | 88.80% | -6.41 |
| Insufficient Funds | 162 | 142 | 14.05% | 8.50% | +5.55 |
| Other reasons | 23 | 25 | 1.99% | 1.50% | +0.50 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 17 | 18 | 1.47% | 1.08% | +0.40 |
| Unknown | 1 | 2 | 0.09% | 0.12% | -0.03 |

**Root Cause:** None + Adyen + Insufficient

---

## L2: AT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.0% | 78.57% | -100.00% | 0 | 238 | ⚠️ |
| credit_card | 70.72% | 84.14% | -15.94% | 304 | 145 | ⚠️ |
| applepay | 81.82% | 86.54% | -5.45% | 209 | 312 | ⚠️ |
| paypal | 94.59% | 95.47% | -0.92% | 185 | 243 |  |
| cashcredit | 100.0% | 100.0% | +0.00% | 1 | 2 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Adyen | 40.0% | 88.89% | -55.00% | 10 | 9 | ⚠️ |
| ProcessOut | 71.77% | 80.43% | -10.77% | 294 | 373 | ⚠️ |
| Braintree | 87.82% | 90.45% | -2.91% | 394 | 555 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 1 | 3 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 562 | 813 | 80.40% | 86.49% | -6.09 |
| Insufficient Funds | 111 | 96 | 15.88% | 10.21% | +5.67 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 14 | 16 | 2.00% | 1.70% | +0.30 |
| Other reasons | 12 | 15 | 1.72% | 1.60% | +0.12 |

**Root Cause:** None + Adyen + Insufficient

---

## L2: DE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 47.83% | 0.0% | +nan% | 46 | 0 |  |
| None | 0.0% | 66.96% | -100.00% | 0 | 115 | ⚠️ |
| credit_card | 48.89% | 59.92% | -18.40% | 1,628 | 2,041 | ⚠️ |
| applepay | 79.07% | 83.72% | -5.56% | 1,648 | 2,095 | ⚠️ |
| paypal | 92.16% | 93.74% | -1.69% | 4,819 | 6,676 |  |
| cashcredit | 100.0% | 100.0% | +0.00% | 38 | 63 |  |
| klarna | 99.26% | 96.88% | +2.47% | 408 | 32 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 45.45% | 64.15% | -29.14% | 44 | 106 | ⚠️ |
| ProcessOut | 52.97% | 64.17% | -17.47% | 1,467 | 1,845 | ⚠️ |
| Braintree | 88.82% | 91.35% | -2.77% | 6,467 | 8,771 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 39 | 70 |  |
| Adyen | 74.56% | 31.3% | +138.18% | 570 | 230 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 7,005 | 9,406 | 81.58% | 85.34% | -3.76 |
| Insufficient Funds | 843 | 805 | 9.82% | 7.30% | +2.51 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 447 | 481 | 5.21% | 4.36% | +0.84 |
| Other reasons | 269 | 322 | 3.13% | 2.92% | +0.21 |
| Unknown | 17 | 1 | 0.20% | 0.01% | +0.19 |
| PROVIDER_ERROR: failure executing charge with provider | 6 | 7 | 0.07% | 0.06% | +0.01 |

**Root Cause:** None + Unknown + Insufficient

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 87.97% | 88.12% | -0.17% | 31,165 | 34,718 |  |
| 2_PreDunningAR | 90.13% | 90.12% | +0.02% | 31,165 | 34,718 |  |
| 3_PostDunningAR | 90.67% | 90.65% | +0.01% | 31,165 | 34,718 |  |
| 6_PaymentApprovalRate | 91.02% | 90.98% | +0.04% | 31,165 | 34,718 |  |

---

## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | Low (>85%) | 14,166 | 14,083 | -0.6% | Stable |
| DE | Medium (>85%) | 11,022 | 8,587 | -22.1% | ⚠️ Volume drop |
| FR | Medium (>85%) | 10,870 | 11,444 | +5.3% | Stable |
| AU | Low (>85%) | 6,989 | 6,365 | -8.9% | Stable |
| NL | High (>92%) | 3,082 | 2,894 | -6.1% | Stable |
| BE | Low (>85%) | 2,435 | 2,669 | +9.6% | Stable |
| IE | Low (>85%) | 1,994 | 2,062 | +3.4% | Stable |
| SE | Low (>85%) | 1,894 | 1,558 | -17.7% | Stable |
| NZ | Low (>85%) | 1,783 | 1,607 | -9.9% | Stable |
| DK | Medium (>85%) | 1,670 | 1,153 | -31.0% | ⚠️ Volume drop |
| NO | Low (>85%) | 1,443 | 773 | -46.4% | ⚠️ Volume drop |
| AT | Medium (>85%) | 940 | 699 | -25.6% | ⚠️ Volume drop |
| CH | Low (>85%) | 198 | 229 | +15.7% | Stable |
| LU | Medium (>85%) | 90 | 97 | +7.8% | Stable |

---

## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| LU | ↓ -8.41% | None -100.0% | Braintree -10.3% | Insufficient Funds +7.61pp | None + Braintree + Insufficient |
| DK | ↓ -7.22% | None -100.0% | Adyen -10.6% | Insufficient Funds +5.55pp | None + Adyen + Insufficient |
| AT | ↓ -7.04% | None -100.0% | Adyen -55.0% | Insufficient Funds +5.67pp | None + Adyen + Insufficient |
| DE | ↓ -4.41% | None -100.0% | Unknown -29.1% | Insufficient Funds +2.51pp | None + Unknown + Insufficient |

---

## SQL Queries

<details>
<summary>L0: 8-Week Trend</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'HF-INTL' as cluster,
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
  SELECT '2026-W14' as affected_week, 'HF-INTL' as cluster,
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
  SELECT '2026-W14' as affected_week, 'HF-INTL' as cluster,
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
