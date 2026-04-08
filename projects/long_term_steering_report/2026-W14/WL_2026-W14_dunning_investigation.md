# Dunning Ship Rate Investigation: WL 2026-W14

**Metric:** Ship Rate (Good Customers)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 29.38% → 28.34% (-3.54pp, -1.04pppp)  
**Volume:** 8,055 orders  
**Significance:** Significant

---

## Executive Summary

## Executive Summary

**Overall:** WL cluster Ship Rate declined from 29.38% to 28.34% (-1.04pp, -3.54% relative change) in 2026-W14, driven primarily by Simpson's Paradox from a 59.6% volume collapse in high-performing market AO.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Pre-Dunning AR | 91.18% → 90.71% | -0.47pp | ✅ Minor decline |
| Discount % | 16.34% → 15.45% | -0.89pp | ✅ Favorable (lower discounts) |
| PC2 | 47.52% → 47.03% | -0.49pp | ✅ Stable |
| Payday Phase | Mid-Cycle → Mid-Cycle | No change | ✅ No seasonal impact |
| Mix Shift | AO volume -59.6% | High-SR market | ⚠️ Simpson's Paradox confirmed |

**Key Findings:**
- **Simpson's Paradox identified:** AO (67.26% → 72.58% SR) lost 59.6% of volume (1,228 → 496 orders), removing ~732 high-converting orders from the cluster mix
- **All individual countries improved or held steady:** GN +2.69pp, AO +7.91pp, CG +12.81pp, CK +9.59pp; only KN declined (-6.44pp)
- **KN showed anomalous PC2 drop:** PC2 collapsed from 87.12% to 47.34% (-45.66pp), warranting separate investigation
- **Underlying fundamentals healthy:** Pre-Dunning AR, Discount %, and PC2 all showed stable or improving trends at cluster level
- **Volume redistribution toward lower-SR markets:** KN (low-SR tier at 15.10%) grew +17.4% while AO (high-SR tier) contracted sharply

**Action:** **Monitor** - The cluster-level decline is a compositional artifact (Simpson's Paradox) rather than true performance degradation. Investigate AO's volume collapse separately to understand if this is temporary or structural. Flag KN's PC2 anomaly for review.

---

---

## WL (Cluster)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
| ---- | ------------ | ------ | --------- | ---- | -------------- | ---- | ---------- | ------ | --- | ----- |
| 2026-W13 | Mid-Cycle | 8,702 | 29.38% | - | 91.18% | - | 16.34% | - | 47.52% | - |
| 2026-W14 | Mid-Cycle | 8,055 | 28.34% | -3.54pp | 90.71% | -0.52pp | 15.45% | -5.45pp | 47.03% | -1.03pp |

---

## GN

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
| ---- | ------------ | ------ | --------- | ---- | -------------- | ---- | ---------- | ------ | --- | ----- |
| 2026-W13 | Mid-Cycle | 635 | 36.06% | - | 93.50% | - | 23.17% | - | 50.2% | - |
| 2026-W14 | Mid-Cycle | 632 | 37.03% | +2.69pp | 92.33% | -1.25pp | 22.96% | -0.91pp | 50.58% | +0.76pp |

---

## AO

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
| ---- | ------------ | ------ | --------- | ---- | -------------- | ---- | ---------- | ------ | --- | ----- |
| 2026-W13 | Mid-Cycle | 1,228 | 67.26% | - | 87.96% | - | 16.55% | - | 37.55% | - |
| 2026-W14 | Mid-Cycle | 496 | 72.58% | +7.91pp | 85.22% | -3.12pp | 13.65% | -17.52pp | 43.32% | +15.37pp |

---

## CG

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
| ---- | ------------ | ------ | --------- | ---- | -------------- | ---- | ---------- | ------ | --- | ----- |
| 2026-W13 | Mid-Cycle | 798 | 21.93% | - | 96.76% | - | 20.81% | - | 51.84% | - |
| 2026-W14 | Mid-Cycle | 780 | 24.74% | +12.81pp | 96.91% | +0.16pp | 17.64% | -15.23pp | 51.87% | +0.06pp |

---

## CK

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
| ---- | ------------ | ------ | --------- | ---- | -------------- | ---- | ---------- | ------ | --- | ----- |
| 2026-W13 | Mid-Cycle | 1,441 | 43.58% | - | 94.15% | - | 26.77% | - | 47.97% | - |
| 2026-W14 | Mid-Cycle | 1,497 | 47.76% | +9.59pp | 93.82% | -0.35pp | 25.26% | -5.64pp | 47.84% | -0.27pp |

---

## KN

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
| ---- | ------------ | ------ | --------- | ---- | -------------- | ---- | ---------- | ------ | --- | ----- |
| 2026-W13 | Mid-Cycle | 570 | 16.14% | - | 87.61% | - | 11.62% | - | 87.12% | - |
| 2026-W14 | Mid-Cycle | 669 | 15.10% | -6.44pp | 88.22% | +0.70pp | 11.34% | -2.41pp | 47.34% | -45.66pp |


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

The WL cluster Ship Rate decline of -1.04pp is a statistical artifact caused by Simpson's Paradox: high-performing market AO experienced a 59.6% volume drop while all major countries individually improved their Ship Rates. No operational intervention is required for the cluster metric, but the root cause of AO's volume contraction and KN's dramatic PC2 decline (-45.66pp) should be investigated independently to ensure these do not represent emerging issues.

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
)
SELECT c.group_key, c.week, pp.payday_phase, CAST(c.volume AS INT) as volume,
  c.ship_rate, prev.ship_rate as prev_ship_rate, c.pre_dunning_ar, prev.pre_dunning_ar as prev_pre_dunning_ar,
  c.discount_pct, prev.discount_pct as prev_discount_pct, c.pc2, prev.pc2 as prev_pc2
FROM combined c CROSS JOIN weeks w
LEFT JOIN combined prev ON c.week = w.affected_week AND prev.week = w.prev_week AND c.group_key = prev.group_key
JOIN payday_labeled pp ON c.week = pp.hellofresh_week
ORDER BY c.week

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
)
SELECT c.group_key, c.week, pp.payday_phase, CAST(c.volume AS INT) as volume,
  c.ship_rate, prev.ship_rate as prev_ship_rate, c.pre_dunning_ar, prev.pre_dunning_ar as prev_pre_dunning_ar,
  c.discount_pct, prev.discount_pct as prev_discount_pct, c.pc2, prev.pc2 as prev_pc2
FROM combined c CROSS JOIN weeks w
LEFT JOIN combined prev ON c.week = w.affected_week AND prev.week = w.prev_week AND c.group_key = prev.group_key
JOIN payday_labeled pp ON c.week = pp.hellofresh_week
ORDER BY c.week

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
