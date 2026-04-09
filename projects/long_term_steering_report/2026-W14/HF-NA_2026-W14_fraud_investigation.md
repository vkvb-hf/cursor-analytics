# Fraud Investigation: HF-NA 2026-W14

**Metric:** Fraud Approval Rate  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 89.13% → 90.90% (+1.98%)  
**Volume:** 23,540 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) for HF-NA improved significantly in 2026-W14, increasing from 89.13% to 90.90% (+1.98%), driven primarily by a substantial decrease in Payment Fraud (PF) Block rates in the US.

**Funnel Analysis:**

| Step | Check | Δ % | Result |
| ---- | ----- | ------ | ------ |
| L0: Cluster Trend | FAR within 8-week range (88.6%-92.5%) | +1.98% | ✅ |
| L1: Country | US exceeds ±2.5% threshold | +3.30% | ⚠️ |
| L1: Channel | Referral exceeds ±2.5% threshold | +6.81% | ⚠️ |
| L2: US Channel | Referral channel driving change | +16.00% | ⚠️ |
| L2: US Payment | PF Block rate decreased significantly | -74.55% | ⚠️ |

**Key Findings:**
- **US is the primary driver:** US FAR increased +3.30% (88.6% → 91.5%), representing 70.6% of total volume (16,609 of 23,540 customers)
- **PF Block rate collapsed in US:** Payment Fraud Block rate dropped -74.55% (from 3.83% to 0.92% for "Others" payment method), directly improving approval rates
- **Referral channel shows dramatic improvement:** US Referral FAR surged +16.00% (59.8% → 69.4%), with PF Block declining -83.12%
- **Duplicate metrics trending upward:** Duplicate Rate increased +3.68% in US and +17.19% in Referral channel overall, suggesting potential future risk
- **Canada counter-trend:** CA FAR declined -1.20% with Duplicate Block Rate increasing +31.58%, partially offsetting US gains

**Action:** **Investigate** — The -74.55% drop in PF Block rate for US "Others" payment method requires immediate investigation to determine if this reflects a legitimate model/rule change or a potential gap in fraud detection coverage.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W14 | 90.90% | 26.58% | 6.85% | 1.48% | 23,540 | +1.98% ← REPORTED CHANGE |
| 2026-W13 | 89.13% | 26.05% | 6.32% | 3.33% | 24,590 | -1.30% |
| 2026-W12 | 90.31% | 25.61% | 6.09% | 2.50% | 24,841 | +0.05% |
| 2026-W11 | 90.27% | 25.00% | 5.92% | 2.65% | 26,806 | -1.38% |
| 2026-W10 | 91.53% | 25.50% | 5.87% | 1.40% | 27,721 | -0.06% |
| 2026-W09 | 91.58% | 24.92% | 5.85% | 1.27% | 30,559 | +0.03% |
| 2026-W08 | 91.55% | 24.95% | 6.16% | 1.08% | 28,186 | -1.05% |
| 2026-W07 | 92.52% | 23.92% | 5.50% | 0.89% | 30,135 | - |

---

## L1: Country Breakdown

| Country | Curr vs Prev | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|---------|--------------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| CA | 90.4→89.4 | 89.35% | -1.20% | 27.85% | -1.84% | 6.94% | +31.58% | 2.84% | +6.62% | 6,931 |  |
| US | 88.6→91.5 | 91.54% | +3.30% | 26.05% | +3.68% | 6.81% | +1.16% | 0.92% | -74.55% | 16,609 | ⚠️ |

**Countries exceeding ±2.5% threshold:** US

---

## L1: Channel Category Scan

**Note:** Fraud rates vary significantly by channel - Paid channels typically have higher duplicate rates due to voucher abuse.

| Category | Curr vs Prev | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|--------------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 96.0→96.5 | 96.46% | +0.49% | 24.64% | -1.75% | 1.75% | +3.16% | 1.02% | -7.70% | 19,096 |  |
| Referral | 62.7→67.0 | 66.99% | +6.81% | 34.90% | +17.19% | 28.74% | +19.25% | 3.47% | -70.88% | 4,444 | ⚠️ |

---

## L2: US Deep-Dive

### Channel Category

**Note:** Channel mix shifts can significantly impact country-level FAR.

| Category | Curr vs Prev | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|--------------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 96.2→96.5 | 96.46% | +0.31% | 24.60% | +1.33% | 2.27% | +0.81% | 0.54% | +3.85% | 13,594 |  |
| Referral | 59.8→69.4 | 69.35% | +16.00% | 32.60% | +14.92% | 27.30% | +14.46% | 2.59% | -83.12% | 3,015 | ⚠️ |

### Payment Method (Payment Fraud Block Rate)

| Payment Method | Curr vs Prev | PF Block % | Δ % | Volume | Flag |
|----------------|--------------|------------|-----|--------|------|
| Credit Card | 0.00→0.00 | 0.00% | - | 75 |  |
| Others | 3.83→0.95 | 0.95% | -75.09% | 15,404 | ⚠️ |
| Paypal | 0.30→0.46 | 0.46% | +51.22% | 1,090 | ⚠️ |

**Root Cause:** PF Block ↓

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| US | ↑ +3.30% | Referral +16.0% | +3.7% | +1.2% | -74.6% | PF Block ↓ |

---

## SQL Queries

<details>
<summary>L0: 8-Week Trend</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'HF-NA' as cluster
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
