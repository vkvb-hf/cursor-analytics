# Fraud Investigation: WL 2026-W14

**Metric:** Fraud Approval Rate  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 92.73% → 93.06% (+0.35%)  
**Volume:** 13,609 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) for WL cluster improved marginally from 92.73% to 93.06% (+0.35%) in 2026-W14, a change that is **not statistically significant** based on the 13,609 customers reaching fraud service.

**Funnel Analysis:**

| Step | Check | Δ % | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | FAR within normal range (89.36%-94.31%) | +0.35% | ✅ |
| L1: Country Scan | KN exceeds ±2.5% threshold | -2.90% | ⚠️ |
| L1: Channel Scan | No channels exceed threshold | +0.28% / -1.40% | ✅ |
| L2: KN Deep-Dive | Referral channel severe degradation | -16.06% | ⚠️ |

**Key Findings:**
- **KN Referral channel critically impacted:** FAR dropped 16.06% (84.3% → 70.8%) with duplicate rate surging +74.36% and duplicate block rate up +92.36%, indicating a likely voucher abuse campaign targeting referral signups
- **KN duplicate metrics spiking:** Country-level duplicate rate increased +32.40% and duplicate block rate rose +42.15%, driving the -2.90% FAR decline in KN
- **Payment fraud blocks decreased significantly in KN:** PF Block rate dropped -80.55% (0.25% → 0.05%), suggesting fraud vectors shifted from payment fraud to voucher/duplicate abuse
- **Overall cluster stability maintained:** Despite KN issues, the WL cluster FAR remains stable at 93.06%, within the 8-week range, due to KN's relatively small volume (2,310 of 13,609 total)
- **Volume trend declining:** Cluster volume decreased from 19,099 (W07) to 13,609 (W14), a 29% reduction over 8 weeks

**Action:** **Investigate** — The KN Referral channel requires immediate attention due to the severe FAR decline (-16.06%) driven by duplicate abuse. Recommend reviewing duplicate detection rules and referral voucher controls specific to KN market.

---

---

## L0: 8-Week Trend (WL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W14 | 93.06% | 15.81% | 5.25% | 0.84% | 13,609 | +0.35% ← REPORTED CHANGE |
| 2026-W13 | 92.73% | 15.53% | 5.07% | 0.80% | 14,394 | -0.32% |
| 2026-W12 | 93.03% | 15.96% | 4.88% | 0.43% | 15,081 | -1.35% |
| 2026-W11 | 94.31% | 14.77% | 4.13% | 0.35% | 16,403 | +0.50% |
| 2026-W10 | 93.84% | 15.79% | 4.48% | 0.45% | 17,316 | +0.41% |
| 2026-W09 | 93.46% | 15.27% | 4.66% | 0.54% | 16,428 | +0.09% |
| 2026-W08 | 93.37% | 15.19% | 4.89% | 0.49% | 16,797 | +4.50% |
| 2026-W07 | 89.36% | 14.40% | 4.28% | 5.17% | 19,099 | - |

---

## L1: Country Breakdown

| Country | Curr vs Prev | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|---------|--------------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| KN | 92.9→90.2 | 90.22% | -2.90% | 9.13% | +32.40% | 8.23% | +42.15% | 0.04% | -80.55% | 2,310 | ⚠️ |
| CG | 92.6→93.5 | 93.52% | +0.98% | 12.63% | -2.05% | 4.38% | +8.03% | 1.54% | -3.56% | 2,145 |  |
| AO | 86.2→88.1 | 88.13% | +2.28% | 26.84% | +1.91% | 11.18% | +2.41% | 0.00% | -100.00% | 868 |  |
| CK | 91.7→94.0 | 94.02% | +2.49% | 24.84% | -6.67% | 5.01% | -18.16% | 0.08% | - | 2,576 |  |

**Countries exceeding ±2.5% threshold:** KN

---

## L1: Channel Category Scan

**Note:** Fraud rates vary significantly by channel - Paid channels typically have higher duplicate rates due to voucher abuse.

| Category | Curr vs Prev | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|--------------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 96.1→96.3 | 96.34% | +0.28% | 13.87% | +2.29% | 1.88% | +17.17% | 0.91% | +5.15% | 11,510 |  |
| Referral | 76.1→75.0 | 75.04% | -1.40% | 26.44% | +4.12% | 23.77% | +6.32% | 0.43% | -6.22% | 2,099 |  |

---

## L2: KN Deep-Dive

### Channel Category

**Note:** Channel mix shifts can significantly impact country-level FAR.

| Category | Curr vs Prev | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|--------------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 93.6→91.4 | 91.38% | -2.40% | 7.84% | +30.32% | 6.97% | +39.00% | 0.05% | -80.95% | 2,180 |  |
| Referral | 84.3→70.8 | 70.77% | -16.06% | 30.77% | +74.36% | 29.23% | +92.36% | 0.00% | - | 130 | ⚠️ |

### Payment Method (Payment Fraud Block Rate)

| Payment Method | Curr vs Prev | PF Block % | Δ % | Volume | Flag |
|----------------|--------------|------------|-----|--------|------|
| Paypal | 0.00→0.00 | 0.00% | - | 235 |  |
| Others | 0.25→0.05 | 0.05% | -80.56% | 2,040 | ⚠️ |

**Root Cause:** Dup Rate ↑ + Dup Block ↑ + PF Block ↓

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| KN | ↓ -2.90% | Referral -16.1% | +32.4% | +42.2% | -80.6% | Dup Rate ↑ + Dup Block ↑ + PF Block ↓ |

---

## SQL Queries

<details>
<summary>L0: 8-Week Trend</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'WL' as cluster
),
completed_weeks AS (
  SELECT hellofresh_week as week
  FROM dimensions.date_dimension
  WHERE date_string_backwards <= date_sub(CURRENT_DATE, 1)
  GROUP BY hellofresh_week
  HAVING COUNT(*) = 7
),
countries AS (
  SELECT business_unit as country
  FROM payments_hf.business_units
  WHERE ARRAY_CONTAINS(reporting_cluster_array, (SELECT cluster FROM params))
),
weekly_metrics AS (
  SELECT 
    p.hellofresh_week as week,
    SUM(CASE WHEN is_fs_check = 1 AND NOT is_fraud_service_block THEN customer_count ELSE 0 END) * 100.0 /
      NULLIF(SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END), 0) AS fraud_approval_rate,
    SUM(CASE WHEN is_fs_check = 1 AND is_duplicate_at_pre_checkout = 1 THEN customer_count ELSE 0 END) * 100.0 /
      NULLIF(SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END), 0) AS duplicate_rate,
    SUM(CASE WHEN is_fs_check = 1 AND is_voucher_fraud_block = 1 THEN customer_count ELSE 0 END) * 100.0 /
      NULLIF(SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END), 0) AS duplicate_block_rate,
    SUM(CASE WHEN is_fs_check = 1 AND is_payment_fraud_block = 1 THEN customer_count ELSE 0 END) * 100.0 /
      NULLIF(SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END), 0) AS payment_fraud_block_rate,
    SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END) AS volume
  FROM payments_hf.payments_p0_metrics_checkout_funnel p
  JOIN completed_weeks cw ON p.hellofresh_week = cw.week
  WHERE p.country IN (SELECT country FROM countries)
    AND p.is_different_checkout = FALSE
  GROUP BY p.hellofresh_week
  ORDER BY p.hellofresh_week DESC
  LIMIT 8
)
SELECT 
  week,
  ROUND(fraud_approval_rate, 2) as far_pct,
  ROUND(duplicate_rate, 2) as dup_rate_pct,
  ROUND(duplicate_block_rate, 2) as dup_block_pct,
  ROUND(payment_fraud_block_rate, 2) as pf_block_pct,
  volume,
  ROUND((fraud_approval_rate - LAG(fraud_approval_rate) OVER (ORDER BY week ASC)) / 
        NULLIF(LAG(fraud_approval_rate) OVER (ORDER BY week ASC), 0) * 100, 2) as change_pct
FROM weekly_metrics
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
  SELECT 
    country,
    SUM(CASE WHEN is_fs_check = 1 AND NOT is_fraud_service_block THEN customer_count ELSE 0 END) * 100.0 /
      NULLIF(SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END), 0) AS far,
    SUM(CASE WHEN is_fs_check = 1 AND is_duplicate_at_pre_checkout = 1 THEN customer_count ELSE 0 END) * 100.0 /
      NULLIF(SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END), 0) AS dup_rate,
    SUM(CASE WHEN is_fs_check = 1 AND is_voucher_fraud_block = 1 THEN customer_count ELSE 0 END) * 100.0 /
      NULLIF(SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END), 0) AS dup_block_rate,
    SUM(CASE WHEN is_fs_check = 1 AND is_payment_fraud_block = 1 THEN customer_count ELSE 0 END) * 100.0 /
      NULLIF(SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END), 0) AS pf_block_rate,
    SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END) AS volume
  FROM payments_hf.payments_p0_metrics_checkout_funnel
  CROSS JOIN weeks w
  WHERE hellofresh_week = w.affected_week
    AND country IN (SELECT country FROM countries)
    AND is_different_checkout = FALSE
  GROUP BY country
),
prev AS (
  SELECT 
    country,
    SUM(CASE WHEN is_fs_check = 1 AND NOT is_fraud_service_block THEN customer_count ELSE 0 END) * 100.0 /
      NULLIF(SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END), 0) AS far,
    SUM(CASE WHEN is_fs_check = 1 AND is_duplicate_at_pre_checkout = 1 THEN customer_count ELSE 0 END) * 100.0 /
      NULLIF(SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END), 0) AS dup_rate,
    SUM(CASE WHEN is_fs_check = 1 AND is_voucher_fraud_block = 1 THEN customer_count ELSE 0 END) * 100.0 /
      NULLIF(SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END), 0) AS dup_block_rate,
    SUM(CASE WHEN is_fs_check = 1 AND is_payment_fraud_block = 1 THEN customer_count ELSE 0 END) * 100.0 /
      NULLIF(SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END), 0) AS pf_block_rate,
    SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END) AS volume
  FROM payments_hf.payments_p0_metrics_checkout_funnel
  CROSS JOIN weeks w
  WHERE hellofresh_week = w.prev_week
    AND country IN (SELECT country FROM countries)
    AND is_different_checkout = FALSE
  GROUP BY country
),
combined AS (
  SELECT 
    c.country,
    ROUND(p.far, 1) as prev_far,
    ROUND(c.far, 1) as curr_far,
    ROUND(c.far, 2) as far_pct,
    ROUND((c.far - p.far) / NULLIF(p.far, 0) * 100, 2) as far_delta,
    ROUND(c.dup_rate, 2) as dup_rate_pct,
    ROUND((c.dup_rate - p.dup_rate) / NULLIF(p.dup_rate, 0) * 100, 2) as dup_rate_delta,
    ROUND(c.dup_block_rate, 2) as dup_block_pct,
    ROUND((c.dup_block_rate - p.dup_block_rate) / NULLIF(p.dup_block_rate, 0) * 100, 2) as dup_block_delta,
    ROUND(c.pf_block_rate, 2) as pf_block_pct,
    ROUND((c.pf_block_rate - p.pf_block_rate) / NULLIF(p.pf_block_rate, 0) * 100, 2) as pf_block_delta,
    c.volume,
    ABS(c.volume * (c.far - p.far) / 100) as contribution
  FROM curr c
  JOIN prev p ON c.country = p.country
),
ranked AS (
  SELECT *,
    ROW_NUMBER() OVER (ORDER BY contribution DESC) as rank_contribution,
    ROW_NUMBER() OVER (ORDER BY ABS(far_delta) DESC) as rank_change
  FROM combined
),
top_countries AS (
  SELECT * FROM ranked
  WHERE rank_contribution <= 4 OR rank_change <= 4
  ORDER BY rank_contribution
  LIMIT 8
)
SELECT 
  country, 
  prev_far,
  curr_far,
  far_pct,
  far_delta,
  dup_rate_pct,
  dup_rate_delta,
  dup_block_pct,
  dup_block_delta,
  pf_block_pct,
  pf_block_delta,
  volume,
  CASE WHEN ABS(far_delta) > 2.5 THEN '⚠️' ELSE '' END as flag
FROM top_countries
ORDER BY far_delta ASC

```

</details>

<details>
<summary>L1b: Channel Category Scan</summary>

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
  SELECT 
    category,
    SUM(CASE WHEN is_fs_check = 1 AND NOT is_fraud_service_block THEN customer_count ELSE 0 END) * 100.0 /
      NULLIF(SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END), 0) AS far,
    SUM(CASE WHEN is_fs_check = 1 AND is_duplicate_at_pre_checkout = 1 THEN customer_count ELSE 0 END) * 100.0 /
      NULLIF(SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END), 0) AS dup_rate,
    SUM(CASE WHEN is_fs_check = 1 AND is_voucher_fraud_block = 1 THEN customer_count ELSE 0 END) * 100.0 /
      NULLIF(SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END), 0) AS dup_block_rate,
    SUM(CASE WHEN is_fs_check = 1 AND is_payment_fraud_block = 1 THEN customer_count ELSE 0 END) * 100.0 /
      NULLIF(SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END), 0) AS pf_block_rate,
    SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END) AS volume
  FROM payments_hf.payments_p0_metrics_checkout_funnel
  CROSS JOIN weeks w
  WHERE hellofresh_week = w.affected_week
    AND country IN (SELECT country FROM countries)
    AND is_different_checkout = FALSE
  GROUP BY category
),
prev AS (
  SELECT 
    category,
    SUM(CASE WHEN is_fs_check = 1 AND NOT is_fraud_service_block THEN customer_count ELSE 0 END) * 100.0 /
      NULLIF(SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END), 0) AS far,
    SUM(CASE WHEN is_fs_check = 1 AND is_duplicate_at_pre_checkout = 1 THEN customer_count ELSE 0 END) * 100.0 /
      NULLIF(SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END), 0) AS dup_rate,
    SUM(CASE WHEN is_fs_check = 1 AND is_voucher_fraud_block = 1 THEN customer_count ELSE 0 END) * 100.0 /
      NULLIF(SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END), 0) AS dup_block_rate,
    SUM(CASE WHEN is_fs_check = 1 AND is_payment_fraud_block = 1 THEN customer_count ELSE 0 END) * 100.0 /
      NULLIF(SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END), 0) AS pf_block_rate,
    SUM(CASE WHEN is_fs_check = 1 THEN customer_count ELSE 0 END) AS volume
  FROM payments_hf.payments_p0_metrics_checkout_funnel
  CROSS JOIN weeks w
  WHERE hellofresh_week = w.prev_week
    AND country IN (SELECT country FROM countries)
    AND is_different_checkout = FALSE
  GROUP BY category
)
SELECT 
  c.category,
  ROUND(p.far, 1) as prev_far,
  ROUND(c.far, 1) as curr_far,
  ROUND(c.far, 2) as far_pct,
  ROUND((c.far - p.far) / NULLIF(p.far, 0) * 100, 2) as far_delta,
  ROUND(c.dup_rate, 2) as dup_rate_pct,
  ROUND((c.dup_rate - p.dup_rate) / NULLIF(p.dup_rate, 0) * 100, 2) as dup_rate_delta,
  ROUND(c.dup_block_rate, 2) as dup_block_pct,
  ROUND((c.dup_block_rate - p.dup_block_rate) / NULLIF(p.dup_block_rate, 0) * 100, 2) as dup_block_delta,
  ROUND(c.pf_block_rate, 2) as pf_block_pct,
  ROUND((c.pf_block_rate - p.pf_block_rate) / NULLIF(p.pf_block_rate, 0) * 100, 2) as pf_block_delta,
  c.volume,
  CASE WHEN ABS((c.far - p.far) / NULLIF(p.far, 0) * 100) > 2.5 THEN '⚠️' ELSE '' END as flag
FROM curr c
JOIN prev p ON c.category = p.category
ORDER BY c.category

```

</details>

---

*Report: 2026-04-09*
