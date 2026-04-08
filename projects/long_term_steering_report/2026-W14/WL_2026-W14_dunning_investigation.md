# Dunning Ship Rate Investigation: WL 2026-W14

**Metric:** Ship Rate (Good Customers)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 29.38% → 28.34% (-3.54pp, -1.04pppp)  
**Volume:** 8,055 orders  
**Significance:** Significant

---

## Executive Summary

## Executive Summary

**Overall:** Ship Rate for WL cluster declined from 29.38% to 28.34% (-1.04pp, -3.54% relative change) in 2026-W14, flagged as significant with 8,055 orders.

**Funnel Analysis:**

| Step | Check | Δ Value | Result |
| ---- | ----- | ------- | ------ |
| Payday Phase | Mid-Cycle → Mid-Cycle | No change | ✅ |
| Pre-Dunning AR | 91.18% → 90.71% | -0.47pp | ✅ |
| Discount % | 16.34% → 15.45% | -0.89pp | ✅ |
| PC2 | 47.52% → 47.03% | -0.49pp | ✅ |
| Mix Shift (Simpson's) | AO volume drop 59.6% | High-SR market shrink | ⚠️ |

**Key Findings:**
- **Simpson's Paradox confirmed:** AO (highest SR market at 72.58%) lost 59.6% of volume (1,228 → 496 orders), removing high-converting orders from the mix and dragging down the aggregate rate
- **All individual countries improved or held steady:** ER +2.93pp, CK +4.18pp, AO +5.32pp, CG +2.81pp, GN +0.97pp — only KN showed slight decline (-1.04pp) and MR remained near zero
- **MR anomaly:** Ship Rate dropped from 0.07% to 0.00% with PC2 showing NaN values, indicating potential data quality issues or operational changes in this market
- **KN volume increased 17.4%** while SR declined 1.04pp, partially offsetting positive mix effects with lower-converting volume
- **Discount rates decreased across most markets** (WL -5.45pp overall), which per the decision framework should support higher Ship Rate — yet aggregate declined due to mix shift

**Action:** Monitor — The aggregate decline is driven by Simpson's Paradox (AO volume collapse), not deteriorating country performance. Investigate the root cause of AO's 60% volume drop and MR's data anomalies before escalating.

---

---

## WL (Cluster)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
| ---- | ------------ | ------ | --------- | ---- | -------------- | ---- | ---------- | ------ | --- | ----- |
| 2026-W13 | Mid-Cycle | 8,702 | 29.38% | - | 91.18% | - | 16.34% | - | 47.52% | - |
| 2026-W14 | Mid-Cycle | 8,055 | 28.34% | -3.54pp | 90.71% | -0.52pp | 15.45% | -5.45pp | 47.03% | -1.03pp |

---

## ER (Rank: #1 by contribution, #3 by change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
| ---- | ------------ | ------ | --------- | ---- | -------------- | ---- | ---------- | ------ | --- | ----- |
| 2026-W13 | Mid-Cycle | 2,563 | 23.64% | - | 89.92% | - | 18.54% | - | 41.5% | - |
| 2026-W14 | Mid-Cycle | 2,559 | 26.57% | +12.39pp | 89.23% | -0.77pp | 19.47% | +5.02pp | 43.85% | +5.66pp |

---

## CK (Rank: #2 by contribution, #4 by change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
| ---- | ------------ | ------ | --------- | ---- | -------------- | ---- | ---------- | ------ | --- | ----- |
| 2026-W13 | Mid-Cycle | 1,441 | 43.58% | - | 94.15% | - | 26.77% | - | 47.97% | - |
| 2026-W14 | Mid-Cycle | 1,497 | 47.76% | +9.59pp | 93.82% | -0.35pp | 25.26% | -5.64pp | 47.84% | -0.27pp |

---

## AO (Rank: #3 by contribution, #5 by change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
| ---- | ------------ | ------ | --------- | ---- | -------------- | ---- | ---------- | ------ | --- | ----- |
| 2026-W13 | Mid-Cycle | 1,228 | 67.26% | - | 87.96% | - | 16.55% | - | 37.55% | - |
| 2026-W14 | Mid-Cycle | 496 | 72.58% | +7.91pp | 85.22% | -3.12pp | 13.65% | -17.52pp | 43.32% | +15.37pp |

---

## CG (Rank: #4 by contribution, #2 by change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
| ---- | ------------ | ------ | --------- | ---- | -------------- | ---- | ---------- | ------ | --- | ----- |
| 2026-W13 | Mid-Cycle | 798 | 21.93% | - | 96.76% | - | 20.81% | - | 51.84% | - |
| 2026-W14 | Mid-Cycle | 780 | 24.74% | +12.81pp | 96.91% | +0.16pp | 17.64% | -15.23pp | 51.87% | +0.06pp |

---

## KN (Rank: #5 by contribution, #6 by change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
| ---- | ------------ | ------ | --------- | ---- | -------------- | ---- | ---------- | ------ | --- | ----- |
| 2026-W13 | Mid-Cycle | 570 | 16.14% | - | 87.61% | - | 11.62% | - | 87.12% | - |
| 2026-W14 | Mid-Cycle | 669 | 15.10% | -6.44pp | 88.22% | +0.70pp | 11.34% | -2.41pp | 47.34% | -45.66pp |

---

## GN (Rank: #6 by contribution, #7 by change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
| ---- | ------------ | ------ | --------- | ---- | -------------- | ---- | ---------- | ------ | --- | ----- |
| 2026-W13 | Mid-Cycle | 635 | 36.06% | - | 93.50% | - | 23.17% | - | 50.2% | - |
| 2026-W14 | Mid-Cycle | 632 | 37.03% | +2.69pp | 92.33% | -1.25pp | 22.96% | -0.91pp | 50.58% | +0.76pp |

---

## MR (Rank: #7 by contribution, #1 by change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
| ---- | ------------ | ------ | --------- | ---- | -------------- | ---- | ---------- | ------ | --- | ----- |
| 2026-W13 | Mid-Cycle | 1,467 | 0.07% | - | 79.88% | - | 9.47% | - | 42.03% | - |
| 2026-W14 | Mid-Cycle | 1,422 | 0.00% | -100.00pp | 80.33% | +0.56pp | 8.14% | -14.04pp | nan% | nanpp |


## Mix Shift Analysis (Simpson's Paradox Check)

| Country | SR Tier | Prev Volume | Curr Volume | Volume Δ | Prev SR | Curr SR | SR Δ |
| ------- | ------- | ----------- | ----------- | -------- | ------- | ------- | ---- |
| ER  | Low | 2,563 | 2,559 | -0.2% | 23.64% | 26.57% | +2.93pp |
| MR  | Low | 1,467 | 1,422 | -3.1% | 0.07% | 0.00% | +0.00pp |
| CK  | Medium | 1,441 | 1,497 | +3.9% | 43.58% | 47.76% | +4.18pp |
| AO ⚠️ | High | 1,228 | 496 | -59.6% | 67.26% | 72.58% | +5.32pp |
| CG  | Low | 798 | 780 | -2.3% | 21.93% | 24.74% | +2.81pp |
| GN  | Medium | 635 | 632 | -0.5% | 36.06% | 37.03% | +0.97pp |
| KN  | Low | 570 | 669 | +17.4% | 16.14% | 15.10% | -1.04pp |

*High-SR markets (>50%) with volume drop >30% indicate Simpson's Paradox*

---
## Decision Framework

**How Ship Rate relates to other metrics:**

| Metric | Relationship | If metric ↑ | If metric ↓ |
| ------ | ------------ | ----------- | ----------- |
| Pre-Dunning AR | Positive | Ship Rate ↑ | Ship Rate ↓ |
| Discount % | Negative | Ship Rate ↓ | Ship Rate ↑ |
| PC2 | Positive | Ship Rate ↑ | Ship Rate ↓ |

**Payday Cycle (for HF-INTL):**
- Phase transition: Mid-Cycle → Mid-Cycle
- Pre-Payday → Payday: Expected SR ↓
- Payday → Post-Payday: Expected SR ↑
- Post-Payday → Mid-Cycle: Expected SR →

---

## Conclusion

The 1.04pp decline in WL Ship Rate is a **compositional artifact**, not a performance issue. The high-converting AO market experienced a 59.6% volume reduction, while lower-converting markets (ER, KN) maintained or increased volume, shifting the mix toward lower Ship Rate segments. Underlying country-level performance actually improved across 5 of 7 markets, indicating healthy dunning execution. Priority should be understanding why AO eligible orders dropped so dramatically and resolving the MR data quality issue (NaN PC2).

---

## SQL Queries

<details>
<summary>Cluster Query</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'WL' as cluster, 'cluster' as level
),
date_lkup AS (
  SELECT hellofresh_week, ROW_NUMBER() OVER (ORDER BY hellofresh_week ASC) AS row_num
  FROM dimensions.date_dimension GROUP BY hellofresh_week
),
weeks AS (
  SELECT curr.hellofresh_week as affected_week, prev.hellofresh_week as prev_week
  FROM date_lkup curr JOIN date_lkup prev ON curr.row_num = prev.row_num + 1
  WHERE curr.hellofresh_week = (SELECT affected_week FROM params)
),
payday_phases AS (
  SELECT hellofresh_week,
    CASE WHEN SUM(CASE WHEN day_of_month BETWEEN 8 AND 15 THEN 1 ELSE 0 END) >= 4 THEN 1 ELSE 0 END as is_payday
  FROM dimensions.date_dimension GROUP BY hellofresh_week
),
payday_with_context AS (
  SELECT hellofresh_week, is_payday,
    LEAD(is_payday) OVER (ORDER BY hellofresh_week) as next_is_payday,
    LAG(is_payday) OVER (ORDER BY hellofresh_week) as prev_is_payday
  FROM payday_phases
),
payday_labeled AS (
  SELECT hellofresh_week,
    CASE WHEN is_payday = 1 THEN 'Payday' WHEN next_is_payday = 1 THEN 'Pre-Payday'
         WHEN prev_is_payday = 1 THEN 'Post-Payday' ELSE 'Mid-Cycle' END as payday_phase
  FROM payday_with_context
),
countries AS (
  SELECT business_unit as country FROM payments_hf.business_units
  WHERE ARRAY_CONTAINS(reporting_cluster_array, (SELECT cluster FROM params))
),
base_data AS (
  SELECT hellofresh_delivery_week as week,
    CASE WHEN (SELECT level FROM params) = 'cluster' THEN (SELECT cluster FROM params) ELSE country END as group_key,
    SUM(CASE WHEN dunning_execution = 'shipped' THEN order_nr ELSE 0 END) as shipped,
    SUM(order_nr) as eligible,
    SUM(CAST(discount_amount_incl_vat_eur AS DOUBLE)) as discount_sum,
    SUM(CAST(grand_total_eur AS DOUBLE) + CAST(discount_amount_incl_vat_eur AS DOUBLE)) as total_sum,
    SUM(CASE WHEN dunning_execution = 'shipped' THEN profit_margin_week_eur ELSE 0 END) as profit_margin_shipped,
    SUM(CASE WHEN dunning_execution = 'shipped' THEN gross_revenue_week_eur ELSE 0 END) as gross_revenue_shipped
  FROM payments_hf.dunning_dashboard CROSS JOIN weeks w
  WHERE hellofresh_delivery_week IN (w.prev_week, w.affected_week)
    AND country IN (SELECT country FROM countries) AND product_type = 'mealbox'
    AND NOT (RIGHT(COALESCE(last_10_order_statuses, ''), 2) = 'ff')
  GROUP BY hellofresh_delivery_week, 
    CASE WHEN (SELECT level FROM params) = 'cluster' THEN (SELECT cluster FROM params) ELSE country END
),
pre_dunning_ar AS (
  SELECT hellofresh_week as week,
    CASE WHEN (SELECT level FROM params) = 'cluster' THEN (SELECT cluster FROM params) ELSE country END as group_key,
    ROUND(SUM(`2_PreDunningAR`) * 100.0 / NULLIF(SUM(order_count), 0), 2) as pre_dunning_ar
  FROM payments_hf.payments_p0_metrics_box_candidates CROSS JOIN weeks w
  WHERE hellofresh_week IN (w.prev_week, w.affected_week) AND country IN (SELECT country FROM countries)
  GROUP BY hellofresh_week, CASE WHEN (SELECT level FROM params) = 'cluster' THEN (SELECT cluster FROM params) ELSE country END
),
combined AS (
  SELECT b.week, b.group_key, b.eligible as volume,
    ROUND(b.shipped * 100.0 / NULLIF(b.eligible, 0), 2) as ship_rate, p.pre_dunning_ar,
    ROUND(b.discount_sum * 100.0 / NULLIF(b.total_sum, 0), 2) as discount_pct,
    ROUND(b.profit_margin_shipped * 100.0 / NULLIF(b.gross_revenue_shipped, 0), 2) as pc2
  FROM base_data b LEFT JOIN pre_dunning_ar p ON b.week = p.week AND b.group_key = p.group_key
),
with_deltas AS (
  SELECT 
    c.*,
    prev.ship_rate as prev_ship_rate,
    prev.pre_dunning_ar as prev_pre_dunning_ar,
    prev.discount_pct as prev_discount_pct,
    prev.pc2 as prev_pc2,
    prev.volume as prev_volume,
    ABS(c.volume * (c.ship_rate - COALESCE(prev.ship_rate, c.ship_rate)) / 100) as contribution,
    ABS((c.ship_rate - COALESCE(prev.ship_rate, c.ship_rate)) / NULLIF(prev.ship_rate, 0) * 100) as abs_delta_sr
  FROM combined c
  CROSS JOIN weeks w
  LEFT JOIN combined prev ON c.week = w.affected_week AND prev.week = w.prev_week AND c.group_key = prev.group_key
),
ranked AS (
  SELECT 
    group_key,
    SUM(contribution) as total_contribution,
    MAX(abs_delta_sr) as max_abs_delta,
    ROW_NUMBER() OVER (ORDER BY SUM(contribution) DESC) as rank_contribution,
    ROW_NUMBER() OVER (ORDER BY MAX(abs_delta_sr) DESC) as rank_change
  FROM with_deltas
  WHERE week = (SELECT affected_week FROM weeks)
  GROUP BY group_key
)
SELECT c.group_key, c.week, pp.payday_phase, CAST(c.volume AS INT) as volume,
  c.ship_rate, c.prev_ship_rate, c.pre_dunning_ar, c.prev_pre_dunning_ar,
  c.discount_pct, c.prev_discount_pct, c.pc2, c.prev_pc2,
  COALESCE(r.rank_contribution, 999) as rank_contribution,
  COALESCE(r.rank_change, 999) as rank_change
FROM with_deltas c
CROSS JOIN weeks w
JOIN payday_labeled pp ON c.week = pp.hellofresh_week
LEFT JOIN ranked r ON c.group_key = r.group_key
ORDER BY COALESCE(r.rank_contribution, 999), c.week

```

</details>

<details>
<summary>Country Query</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'WL' as cluster, 'country' as level
),
date_lkup AS (
  SELECT hellofresh_week, ROW_NUMBER() OVER (ORDER BY hellofresh_week ASC) AS row_num
  FROM dimensions.date_dimension GROUP BY hellofresh_week
),
weeks AS (
  SELECT curr.hellofresh_week as affected_week, prev.hellofresh_week as prev_week
  FROM date_lkup curr JOIN date_lkup prev ON curr.row_num = prev.row_num + 1
  WHERE curr.hellofresh_week = (SELECT affected_week FROM params)
),
payday_phases AS (
  SELECT hellofresh_week,
    CASE WHEN SUM(CASE WHEN day_of_month BETWEEN 8 AND 15 THEN 1 ELSE 0 END) >= 4 THEN 1 ELSE 0 END as is_payday
  FROM dimensions.date_dimension GROUP BY hellofresh_week
),
payday_with_context AS (
  SELECT hellofresh_week, is_payday,
    LEAD(is_payday) OVER (ORDER BY hellofresh_week) as next_is_payday,
    LAG(is_payday) OVER (ORDER BY hellofresh_week) as prev_is_payday
  FROM payday_phases
),
payday_labeled AS (
  SELECT hellofresh_week,
    CASE WHEN is_payday = 1 THEN 'Payday' WHEN next_is_payday = 1 THEN 'Pre-Payday'
         WHEN prev_is_payday = 1 THEN 'Post-Payday' ELSE 'Mid-Cycle' END as payday_phase
  FROM payday_with_context
),
countries AS (
  SELECT business_unit as country FROM payments_hf.business_units
  WHERE ARRAY_CONTAINS(reporting_cluster_array, (SELECT cluster FROM params))
),
base_data AS (
  SELECT hellofresh_delivery_week as week,
    CASE WHEN (SELECT level FROM params) = 'cluster' THEN (SELECT cluster FROM params) ELSE country END as group_key,
    SUM(CASE WHEN dunning_execution = 'shipped' THEN order_nr ELSE 0 END) as shipped,
    SUM(order_nr) as eligible,
    SUM(CAST(discount_amount_incl_vat_eur AS DOUBLE)) as discount_sum,
    SUM(CAST(grand_total_eur AS DOUBLE) + CAST(discount_amount_incl_vat_eur AS DOUBLE)) as total_sum,
    SUM(CASE WHEN dunning_execution = 'shipped' THEN profit_margin_week_eur ELSE 0 END) as profit_margin_shipped,
    SUM(CASE WHEN dunning_execution = 'shipped' THEN gross_revenue_week_eur ELSE 0 END) as gross_revenue_shipped
  FROM payments_hf.dunning_dashboard CROSS JOIN weeks w
  WHERE hellofresh_delivery_week IN (w.prev_week, w.affected_week)
    AND country IN (SELECT country FROM countries) AND product_type = 'mealbox'
    AND NOT (RIGHT(COALESCE(last_10_order_statuses, ''), 2) = 'ff')
  GROUP BY hellofresh_delivery_week, 
    CASE WHEN (SELECT level FROM params) = 'cluster' THEN (SELECT cluster FROM params) ELSE country END
),
pre_dunning_ar AS (
  SELECT hellofresh_week as week,
    CASE WHEN (SELECT level FROM params) = 'cluster' THEN (SELECT cluster FROM params) ELSE country END as group_key,
    ROUND(SUM(`2_PreDunningAR`) * 100.0 / NULLIF(SUM(order_count), 0), 2) as pre_dunning_ar
  FROM payments_hf.payments_p0_metrics_box_candidates CROSS JOIN weeks w
  WHERE hellofresh_week IN (w.prev_week, w.affected_week) AND country IN (SELECT country FROM countries)
  GROUP BY hellofresh_week, CASE WHEN (SELECT level FROM params) = 'cluster' THEN (SELECT cluster FROM params) ELSE country END
),
combined AS (
  SELECT b.week, b.group_key, b.eligible as volume,
    ROUND(b.shipped * 100.0 / NULLIF(b.eligible, 0), 2) as ship_rate, p.pre_dunning_ar,
    ROUND(b.discount_sum * 100.0 / NULLIF(b.total_sum, 0), 2) as discount_pct,
    ROUND(b.profit_margin_shipped * 100.0 / NULLIF(b.gross_revenue_shipped, 0), 2) as pc2
  FROM base_data b LEFT JOIN pre_dunning_ar p ON b.week = p.week AND b.group_key = p.group_key
),
with_deltas AS (
  SELECT 
    c.*,
    prev.ship_rate as prev_ship_rate,
    prev.pre_dunning_ar as prev_pre_dunning_ar,
    prev.discount_pct as prev_discount_pct,
    prev.pc2 as prev_pc2,
    prev.volume as prev_volume,
    ABS(c.volume * (c.ship_rate - COALESCE(prev.ship_rate, c.ship_rate)) / 100) as contribution,
    ABS((c.ship_rate - COALESCE(prev.ship_rate, c.ship_rate)) / NULLIF(prev.ship_rate, 0) * 100) as abs_delta_sr
  FROM combined c
  CROSS JOIN weeks w
  LEFT JOIN combined prev ON c.week = w.affected_week AND prev.week = w.prev_week AND c.group_key = prev.group_key
),
ranked AS (
  SELECT 
    group_key,
    SUM(contribution) as total_contribution,
    MAX(abs_delta_sr) as max_abs_delta,
    ROW_NUMBER() OVER (ORDER BY SUM(contribution) DESC) as rank_contribution,
    ROW_NUMBER() OVER (ORDER BY MAX(abs_delta_sr) DESC) as rank_change
  FROM with_deltas
  WHERE week = (SELECT affected_week FROM weeks)
  GROUP BY group_key
)
SELECT c.group_key, c.week, pp.payday_phase, CAST(c.volume AS INT) as volume,
  c.ship_rate, c.prev_ship_rate, c.pre_dunning_ar, c.prev_pre_dunning_ar,
  c.discount_pct, c.prev_discount_pct, c.pc2, c.prev_pc2,
  COALESCE(r.rank_contribution, 999) as rank_contribution,
  COALESCE(r.rank_change, 999) as rank_change
FROM with_deltas c
CROSS JOIN weeks w
JOIN payday_labeled pp ON c.week = pp.hellofresh_week
LEFT JOIN ranked r ON c.group_key = r.group_key
ORDER BY COALESCE(r.rank_contribution, 999), c.week

```

</details>

<details>
<summary>Mix Shift Query</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'WL' as cluster
),
date_lkup AS (
  SELECT hellofresh_week, ROW_NUMBER() OVER (ORDER BY hellofresh_week ASC) AS row_num
  FROM dimensions.date_dimension
  GROUP BY hellofresh_week
),
weeks AS (
  SELECT curr.hellofresh_week as affected_week, prev.hellofresh_week as prev_week
  FROM date_lkup curr
  JOIN date_lkup prev ON curr.row_num = prev.row_num + 1
  WHERE curr.hellofresh_week = (SELECT affected_week FROM params)
),
countries AS (
  SELECT business_unit as country
  FROM payments_hf.business_units
  WHERE ARRAY_CONTAINS(reporting_cluster_array, (SELECT cluster FROM params))
),
base_data AS (
  SELECT 
    hellofresh_delivery_week as week,
    country,
    SUM(CASE WHEN dunning_execution = 'shipped' THEN order_nr ELSE 0 END) as shipped,
    SUM(order_nr) as eligible
  FROM payments_hf.dunning_dashboard
  CROSS JOIN weeks w
  WHERE hellofresh_delivery_week IN (w.prev_week, w.affected_week)
    AND country IN (SELECT country FROM countries)
    AND product_type = 'mealbox'
    AND NOT (RIGHT(COALESCE(last_10_order_statuses, ''), 2) = 'ff')
  GROUP BY hellofresh_delivery_week, country
)
SELECT 
  country,
  MAX(CASE WHEN week = (SELECT prev_week FROM weeks) THEN eligible END) as prev_volume,
  MAX(CASE WHEN week = (SELECT prev_week FROM weeks) THEN ROUND(shipped * 100.0 / NULLIF(eligible, 0), 2) END) as prev_sr,
  MAX(CASE WHEN week = (SELECT affected_week FROM weeks) THEN eligible END) as curr_volume,
  MAX(CASE WHEN week = (SELECT affected_week FROM weeks) THEN ROUND(shipped * 100.0 / NULLIF(eligible, 0), 2) END) as curr_sr,
  ROUND((MAX(CASE WHEN week = (SELECT affected_week FROM weeks) THEN eligible END) - 
         MAX(CASE WHEN week = (SELECT prev_week FROM weeks) THEN eligible END)) * 100.0 / 
         NULLIF(MAX(CASE WHEN week = (SELECT prev_week FROM weeks) THEN eligible END), 0), 1) as volume_change_pct,
  CASE 
    WHEN MAX(CASE WHEN week = (SELECT prev_week FROM weeks) THEN ROUND(shipped * 100.0 / NULLIF(eligible, 0), 2) END) > 50 THEN 'High'
    WHEN MAX(CASE WHEN week = (SELECT prev_week FROM weeks) THEN ROUND(shipped * 100.0 / NULLIF(eligible, 0), 2) END) > 30 THEN 'Medium'
    ELSE 'Low'
  END as sr_tier
FROM base_data
GROUP BY country
ORDER BY MAX(CASE WHEN week = (SELECT prev_week FROM weeks) THEN eligible END) DESC

```

</details>

---

*Report: 2026-04-08*
