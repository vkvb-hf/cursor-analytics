# Fraud Investigation: RTE 2026-W14

**Metric:** Fraud Approval Rate  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 94.14% → 94.72% (+0.61%)  
**Volume:** 42,650 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) for RTE cluster improved slightly from 94.14% to 94.72% (+0.61%) in 2026-W14, a change that is not statistically significant and falls within normal weekly fluctuation observed in the 8-week trend (range: 93.82% - 94.95%).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | FAR within normal range (93.82%-94.95%) | +0.61% | ✅ |
| L1: Country Scan | 2 countries exceed ±2.5% threshold (TO, TK) | TO: -4.22%, TK: +5.01% | ⚠️ |
| L1: Channel Scan | Both categories within threshold | Paid: +1.00%, Referral: -1.15% | ✅ |
| L2: TO Deep-Dive | Paid channel duplicate spike | Dup Rate: +122.15% | ⚠️ |
| L2: TK Deep-Dive | Duplicate rate improvement | Dup Rate: -37.46% | ✅ |

**Key Findings:**
- **TO experienced a -4.22% FAR decline** driven by a significant spike in duplicate detection (+70.52%) and blocking (+71.26%) in the Paid channel, with only 579 customers affected (1.4% of total volume)
- **TK showed a +5.01% FAR improvement** due to decreased duplicate activity (Dup Rate -37.46%, Dup Block -30.58%), though this represents only 336 customers (0.8% of total volume)
- **FJ dominates cluster volume** at 29,804 customers (69.9% of total) with stable FAR improvement of +1.11%
- **Referral channel shows elevated duplicate rates** (22.61%) compared to Paid (12.52%), consistent with expected voucher abuse patterns
- **Payment Fraud Block rates remain negligible** across all countries (≤0.29%), indicating no payment fraud concerns

**Action:** **Monitor** - The overall FAR change is not significant and the flagged countries (TO, TK) represent <2.5% of total volume combined. Continue standard monitoring; no investigation required unless patterns persist in W15.

---

---

## L0: 8-Week Trend (RTE)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W14 | 94.72% | 14.31% | 4.46% | 0.20% | 42,650 | +0.61% ← REPORTED CHANGE |
| 2026-W13 | 94.14% | 14.50% | 4.06% | 0.26% | 43,962 | +0.34% |
| 2026-W12 | 93.82% | 14.53% | 4.28% | 0.22% | 45,581 | -0.63% |
| 2026-W11 | 94.41% | 14.54% | 3.91% | 0.21% | 48,713 | -0.57% |
| 2026-W10 | 94.95% | 13.98% | 3.74% | 0.16% | 50,499 | +0.53% |
| 2026-W09 | 94.45% | 14.28% | 4.09% | 0.22% | 51,707 | +0.43% |
| 2026-W08 | 94.05% | 14.98% | 4.35% | 0.12% | 48,963 | -0.20% |
| 2026-W07 | 94.25% | 14.89% | 4.17% | 0.12% | 50,465 | - |

---

## L1: Country Breakdown

| Country | Curr vs Prev | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|---------|--------------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| TO | 92.5→88.6 | 88.60% | -4.22% | 11.92% | +70.52% | 10.88% | +71.26% | 0.00% | - | 579 | ⚠️ |
| TT | 91.3→89.3 | 89.32% | -2.14% | 10.56% | +23.82% | 8.73% | +35.38% | 0.00% | - | 871 |  |
| CF | 94.1→93.5 | 93.52% | -0.66% | 13.48% | +0.04% | 5.38% | +21.34% | 0.00% | - | 6,632 |  |
| YE | 94.0→93.5 | 93.50% | -0.54% | 18.29% | -1.41% | 6.09% | +26.28% | 0.00% | - | 3,418 |  |
| FJ | 94.5→95.5 | 95.51% | +1.11% | 14.45% | -2.85% | 3.69% | +2.93% | 0.29% | -21.21% | 29,804 |  |
| TV | 90.9→93.1 | 93.08% | +2.38% | 8.21% | +5.30% | 6.15% | -5.23% | 0.00% | -100.00% | 390 |  |
| TK | 88.4→92.9 | 92.86% | +5.01% | 7.44% | -37.46% | 6.25% | -30.58% | 0.00% | - | 336 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TO, TK

---

## L1: Channel Category Scan

**Note:** Fraud rates vary significantly by channel - Paid channels typically have higher duplicate rates due to voucher abuse.

| Category | Curr vs Prev | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|--------------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 96.6→97.6 | 97.60% | +1.00% | 12.52% | -4.75% | 1.60% | +3.56% | 0.21% | -20.74% | 35,066 |  |
| Referral | 82.3→81.4 | 81.40% | -1.15% | 22.61% | +8.01% | 17.67% | +10.48% | 0.16% | -19.34% | 7,584 |  |

---

## L2: TO Deep-Dive

### Channel Category

**Note:** Channel mix shifts can significantly impact country-level FAR.

| Category | Curr vs Prev | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|--------------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 95.1→91.2 | 91.20% | -4.09% | 9.49% | +122.15% | 8.10% | +113.35% | 0.00% | - | 432 | ⚠️ |
| Referral | 81.9→81.0 | 80.95% | -1.20% | 19.05% | +5.44% | 19.05% | +13.55% | 0.00% | - | 147 |  |

### Payment Method (Payment Fraud Block Rate)

| Payment Method | Curr vs Prev | PF Block % | Δ % | Volume | Flag |
|----------------|--------------|------------|-----|--------|------|
| Others | 0.00→0.00 | 0.00% | - | 505 |  |

**Root Cause:** Dup Rate ↑ + Dup Block ↑

---

## L2: TK Deep-Dive

### Channel Category

**Note:** Channel mix shifts can significantly impact country-level FAR.

| Category | Curr vs Prev | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|--------------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 90.2→93.5 | 93.48% | +3.63% | 6.88% | -32.54% | 5.43% | -21.68% | 0.00% | - | 276 | ⚠️ |
| Referral | 81.8→90.0 | 90.00% | +10.00% | 10.00% | -45.00% | 10.00% | -40.00% | 0.00% | - | 60 | ⚠️ |

### Payment Method (Payment Fraud Block Rate)

| Payment Method | Curr vs Prev | PF Block % | Δ % | Volume | Flag |
|----------------|--------------|------------|-----|--------|------|
| Others | 0.00→0.00 | 0.00% | - | 324 |  |

**Root Cause:** Dup Rate ↓ + Dup Block ↓

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| TO | ↓ -4.22% | Paid -4.1% | +70.5% | +71.3% | +0.0% | Dup Rate ↑ + Dup Block ↑ |
| TK | ↑ +5.01% | Paid +3.6% | -37.5% | -30.6% | +0.0% | Dup Rate ↓ + Dup Block ↓ |

---

## SQL Queries

<details>
<summary>L0: 8-Week Trend</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'RTE' as cluster
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
