# Fraud Investigation: HF-INTL 2026-W14

**Metric:** Fraud Approval Rate  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 91.79% → 91.70% (-0.10%)  
**Volume:** 37,558 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate for HF-INTL declined marginally from 91.79% to 91.70% (-0.10%) in 2026-W14, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | FAR within normal range (91.58%-92.37%) | -0.10% | ✅ |
| L1: Country Scan | 2 countries exceed ±2.5% threshold (NZ, LU) | NZ +4.56%, LU +4.71% | ⚠️ |
| L1: Channel Scan | Both Paid and Referral within threshold | Paid +0.77%, Referral +0.18% | ✅ |
| L2: NZ Deep-Dive | Referral channel spike (+24.38%) | Dup Rate ↓, Dup Block ↓, PF Block ↓ | ⚠️ |
| L2: LU Deep-Dive | Referral channel spike (+90.38%) on low volume (13) | Root cause unclear | ⚠️ |

**Key Findings:**
- Volume decreased significantly by 19.6% (46,689 → 37,558 customers), contributing to metric volatility
- NZ saw a +4.56% FAR improvement driven by Referral channel (+24.38%), with decreases across all block types: Dup Rate (-7.76%), Dup Block (-15.82%), and PF Block (-11.39%)
- LU shows a +4.71% FAR increase but on very low volume (77 total, 13 Referral), making this statistically unreliable
- CH and AT showed notable FAR declines (-2.47% and -2.24% respectively), with AT experiencing a +21.46% increase in Duplicate Rate and +73.96% increase in Dup Block Rate
- Duplicate Block Rate increased cluster-wide from 6.61% to 7.42% (+0.81pp), the highest in the 8-week period

**Action:** Monitor — The overall change is not significant and within normal operating range. Continue monitoring NZ and AT trends next week; LU volume too low for actionable conclusions.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W14 | 91.70% | 30.22% | 7.42% | 0.25% | 37,558 | -0.10% ← REPORTED CHANGE |
| 2026-W13 | 91.79% | 30.52% | 6.61% | 0.27% | 46,689 | -0.17% |
| 2026-W12 | 91.94% | 30.60% | 6.86% | 0.20% | 44,707 | +0.25% |
| 2026-W11 | 91.72% | 29.91% | 7.11% | 0.15% | 49,927 | -0.70% |
| 2026-W10 | 92.36% | 29.84% | 6.44% | 0.22% | 52,844 | -0.01% |
| 2026-W09 | 92.37% | 29.17% | 6.28% | 0.37% | 54,963 | +0.86% |
| 2026-W08 | 91.58% | 29.98% | 7.05% | 0.26% | 54,577 | -0.44% |
| 2026-W07 | 91.99% | 29.94% | 6.76% | 0.16% | 54,624 | - |

---

## L1: Country Breakdown

| Country | Curr vs Prev | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|---------|--------------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| CH | 92.9→90.6 | 90.60% | -2.47% | 11.11% | -3.17% | 4.27% | +160.68% | 0.00% | -100.00% | 117 |  |
| AT | 92.9→90.8 | 90.79% | -2.24% | 23.10% | +21.46% | 7.75% | +73.96% | 0.00% | -100.00% | 619 |  |
| FR | 88.8→88.0 | 87.97% | -0.93% | 25.90% | +0.83% | 11.26% | +17.99% | 0.17% | -15.51% | 9,239 |  |
| GB | 92.4→92.7 | 92.73% | +0.39% | 39.58% | -1.89% | 6.53% | +3.94% | 0.37% | +54.66% | 8,861 |  |
| AU | 91.9→92.5 | 92.46% | +0.58% | 36.22% | +2.06% | 6.45% | -2.50% | 0.40% | +1.72% | 3,009 |  |
| NZ | 85.6→89.5 | 89.51% | +4.56% | 35.97% | -7.76% | 7.77% | -15.82% | 1.63% | -11.39% | 734 | ⚠️ |
| LU | 93.0→97.4 | 97.40% | +4.71% | 9.09% | - | 0.00% | - | 0.00% | - | 77 | ⚠️ |

**Countries exceeding ±2.5% threshold:** NZ, LU

---

## L1: Channel Category Scan

**Note:** Fraud rates vary significantly by channel - Paid channels typically have higher duplicate rates due to voucher abuse.

| Category | Curr vs Prev | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|--------------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 96.9→97.6 | 97.60% | +0.77% | 30.16% | -2.11% | 1.48% | -9.88% | 0.25% | -14.75% | 27,353 |  |
| Referral | 75.7→75.9 | 75.88% | +0.18% | 30.39% | +2.58% | 23.32% | +4.48% | 0.24% | +19.34% | 10,205 |  |

---

## L2: NZ Deep-Dive

### Channel Category

**Note:** Channel mix shifts can significantly impact country-level FAR.

| Category | Curr vs Prev | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|--------------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 94.5→96.7 | 96.75% | +2.40% | 35.44% | -4.78% | 0.18% | -61.78% | 1.99% | +5.09% | 553 |  |
| Referral | 54.2→67.4 | 67.40% | +24.38% | 37.57% | -16.98% | 30.94% | -23.08% | 0.55% | -67.04% | 181 | ⚠️ |

### Payment Method (Payment Fraud Block Rate)

| Payment Method | Curr vs Prev | PF Block % | Δ % | Volume | Flag |
|----------------|--------------|------------|-----|--------|------|
| Others | 1.96→1.70 | 1.70% | -13.09% | 706 | ⚠️ |

**Root Cause:** Dup Rate ↓ + Dup Block ↓ + PF Block ↓

---

## L2: LU Deep-Dive

### Channel Category

**Note:** Channel mix shifts can significantly impact country-level FAR.

| Category | Curr vs Prev | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|--------------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 98.7→100.0 | 100.00% | +1.32% | 10.94% | - | 0.00% | - | 0.00% | - | 64 |  |
| Referral | 44.4→84.6 | 84.62% | +90.38% | 0.00% | - | 0.00% | - | 0.00% | - | 13 | ⚠️ |

### Payment Method (Payment Fraud Block Rate)

| Payment Method | Curr vs Prev | PF Block % | Δ % | Volume | Flag |
|----------------|--------------|------------|-----|--------|------|

**Root Cause:** Requires investigation

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| NZ | ↑ +4.56% | Referral +24.4% | -7.8% | -15.8% | -11.4% | Dup Rate ↓ + Dup Block ↓ + PF Block ↓ |
| LU | ↑ +4.71% | Referral +90.4% | +0.0% | +0.0% | +0.0% | Requires investigation |

---

## SQL Queries

<details>
<summary>L0: 8-Week Trend</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'HF-INTL' as cluster
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

*Report: 2026-04-08*
