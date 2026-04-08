# Dunning Ship Rate Investigation: US-HF 2026-W14

**Metric:** Ship Rate (Good Customers)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 45.08% → 47.79% (+6.01pp, +2.71pppp)  
**Volume:** 13,814 orders  
**Significance:** Significant

---

## Executive Summary

## Executive Summary

**Overall:** Ship Rate for US-HF improved significantly in 2026-W14, increasing from 45.08% to 47.79% (+2.71pp, representing a +6.01% relative change) on stable volume of ~13,814 orders.

**Funnel Analysis:**

| Step | Check | Δ Value | Result |
| ---- | ----- | ------- | ------ |
| Pre-Dunning AR | 92.85% → 92.79% | -0.06pp | ✅ Stable |
| Discount % | 16.31% → 14.58% | -1.73pp (-10.61% relative) | ✅ Favorable |
| PC2 (Margin) | 51.11% → 52.82% | +1.71pp (+3.35% relative) | ✅ Improved |
| Ship Rate | 45.08% → 47.79% | +2.71pp (+6.01% relative) | ✅ Improved |

**Key Findings:**
- **Discount reduction drove improvement:** Discount % decreased significantly by 1.73pp (10.61% relative decline), which has a negative relationship with Ship Rate—lower discounts correlate with higher ship rates
- **No Simpson's Paradox detected:** US is the sole market in this cluster, with stable volume (+0.0% change) and Medium SR tier, indicating genuine performance improvement rather than mix shift
- **Margin improved alongside Ship Rate:** PC2 increased by +1.71pp to 52.82%, suggesting shipped orders maintained healthy profitability
- **Pre-Dunning AR remained stable:** Near-flat change (-0.06pp) indicates consistent upstream payment authorization performance
- **Payday phase unchanged:** Both weeks were Mid-Cycle, eliminating payday timing as a factor in the improvement

**Action:** **Monitor** — This is a positive, significant improvement driven by favorable discount dynamics with no signs of mix shift distortion. Continue tracking to confirm the trend sustains into W15.

---

---

## US-HF (Cluster)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
| ---- | ------------ | ------ | --------- | ---- | -------------- | ---- | ---------- | ------ | --- | ----- |
| 2026-W13 | Mid-Cycle | 13,817 | 45.08% | - | 92.85% | - | 16.31% | - | 51.11% | - |
| 2026-W14 | Mid-Cycle | 13,814 | 47.79% | +6.01pp | 92.79% | -0.06pp | 14.58% | -10.61pp | 52.82% | +3.35pp |

---

## US (Rank: #1 by contribution, #1 by change)

| Week | Payday Phase | Volume | Ship Rate | Δ SR | Pre-Dunning AR | Δ AR | Discount % | Δ Disc | PC2 | Δ PC2 |
| ---- | ------------ | ------ | --------- | ---- | -------------- | ---- | ---------- | ------ | --- | ----- |
| 2026-W13 | Mid-Cycle | 13,817 | 45.08% | - | 92.85% | - | 16.31% | - | 51.11% | - |
| 2026-W14 | Mid-Cycle | 13,814 | 47.79% | +6.01pp | 92.79% | -0.06pp | 14.58% | -10.61pp | 52.82% | +3.35pp |


## Mix Shift Analysis (Simpson's Paradox Check)

| Country | SR Tier | Prev Volume | Curr Volume | Volume Δ | Prev SR | Curr SR | SR Δ |
| ------- | ------- | ----------- | ----------- | -------- | ------- | ------- | ---- |
| US  | Medium | 13,817 | 13,814 | +0.0% | 45.08% | 47.79% | +2.71pp |

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

The +2.71pp Ship Rate improvement in US-HF during 2026-W14 represents genuine operational performance gains, primarily driven by a substantial reduction in discount rates (-1.73pp) while maintaining stable pre-dunning authorization and improving profit margins. With no evidence of Simpson's Paradox and consistent payday phase timing, this improvement reflects real underlying improvement in customer payment behavior. Continued monitoring is recommended to validate trend persistence.

---

## SQL Queries

<details>
<summary>Cluster Query</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'US-HF' as cluster, 'cluster' as level
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
  SELECT '2026-W14' as affected_week, 'US-HF' as cluster, 'country' as level
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
  SELECT '2026-W14' as affected_week, 'US-HF' as cluster
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
