# PCR Investigation: HF-INTL 2026-W14

**Metric:** Payment Conversion Rate (PCR)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 34.88% → 36.04% (+1.16pp)  
**Volume:** ~62K payment visits

---

## Executive Summary

**Overall:** Payment Conversion Rate improved from 34.88% to 36.04%, representing a +1.16pp increase during week 2026-W14 despite a 23.9% decline in payment visit volume.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ✅ | +0.42pp | Improved conversion |
| Click Submit Form | ✅ | +0.59pp | Improved conversion |
| FE Validation Passed | ✅ | +0.68pp | Improved conversion |
| Enter Fraud Service | ✅ | +0.40pp | Improved conversion |
| Approved by Fraud Service | ⚠️ | -0.24pp | Slight decline |
| Call to PVS | ✅ | -0.01pp | Stable |
| Successful Checkout | ✅ | +0.85pp | Strong improvement |

**Key Findings:**
- Frontend validation performance improved significantly (+0.68pp), indicating better user experience or form optimization
- Successful checkout conversion showed the strongest improvement (+0.85pp), driving overall PCR gains
- Fraud service approval rate declined slightly (-0.24pp), though this was offset by improvements elsewhere
- Braintree ApplePay showed notable improvement (+1.10pp rate increase) while ProcessOut ApplePay declined (-1.33pp)
- Backend data shows checkout attempt rate improved from 44.86% to 46.40% (+1.54pp), supporting the positive trend

**Action:** Monitor - The improvements appear consistent across most funnel steps with strong positive impact on overall PCR.

---

---

## Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 82,373 | 62,648 | -19,725 | -23.9% | - | - | - |
| Select Payment Method | 45,198 | 34,641 | -10,557 | -23.4% | 54.87% | 55.29% | +0.42pp |
| Click Submit Form | 36,437 | 28,131 | -8,306 | -22.8% | 80.62% | 81.21% | +0.59pp |
| FE Validation Passed | 33,860 | 26,333 | -7,527 | -22.2% | 92.93% | 93.61% | +0.68pp |
| Enter Fraud Service | 32,610 | 25,466 | -7,144 | -21.9% | 96.31% | 96.71% | +0.40pp |
| Approved by Fraud Service | 30,635 | 23,863 | -6,772 | -22.1% | 93.94% | 93.71% | -0.24pp |
| Call to PVS | 30,583 | 23,821 | -6,762 | -22.1% | 99.83% | 99.82% | -0.01pp |
| **Successful Checkout** | 28,731 | 22,580 | -6,151 | -21.4% | 93.94% | 94.79% | +0.85pp |
| **PCR Rate** | | | | | 34.88% | 36.04% | **+1.16pp** |

---

## Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 106,120 | 81,560 | -24,560 | -23.1% | - | - | - |
| Checkout Attempt | 47,601 | 37,841 | -9,760 | -20.5% | 44.86% | 46.40% | +1.54pp |
| Enter Fraud Service | 46,295 | 36,671 | -9,624 | -20.8% | 97.26% | 96.91% | -0.35pp |
| Approved by Fraud Service | 42,663 | 33,636 | -9,027 | -21.2% | 92.15% | 91.72% | -0.43pp |
| PVS Attempt | 39,598 | 31,465 | -8,133 | -20.5% | 92.82% | 93.55% | +0.73pp |
| PVS Success | 37,702 | 30,206 | -7,496 | -19.9% | 95.21% | 96.00% | +0.79pp |
| **Successful Checkout** | 42,869 | 34,145 | -8,724 | -20.4% | 113.70% | 113.04% | -0.66pp |

---

## Payment Method Breakdown

| Payment Method | 2026-W13 Attempt | 2026-W13 Success | 2026-W13 Rate | 2026-W14 Attempt | 2026-W14 Success | 2026-W14 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 17,791 | 15,721 | 88.36% | 14,680 | 12,978 | 88.41% | +0.04pp |
| Braintree_ApplePay | 13,360 | 11,935 | 89.33% | 10,592 | 9,579 | 90.44% | +1.10pp |
| Braintree_Paypal | 9,125 | 8,317 | 91.15% | 7,030 | 6,381 | 90.77% | -0.38pp |
| Adyen_Klarna | 2,195 | 2,082 | 94.85% | 1,481 | 1,395 | 94.19% | -0.66pp |
| Adyen_IDeal | 1,887 | 1,733 | 91.84% | 1,322 | 1,218 | 92.13% | +0.29pp |
| ProcessOut_ApplePay | 1,558 | 1,431 | 91.85% | 1,213 | 1,098 | 90.52% | -1.33pp |
| Adyen_Sepa | 984 | 977 | 99.29% | 1,024 | 1,019 | 99.51% | +0.22pp |
| Adyen_BcmcMobile | 475 | 460 | 96.84% | 384 | 368 | 95.83% | -1.01pp |
| Adyen_CreditCard | 116 | 103 | 88.79% | 69 | 63 | 91.30% | +2.51pp |
| NoPayment | 105 | 105 | 100.00% | 42 | 42 | 100.00% | +0.00pp |

---

## Conclusion

The PCR improvement of +1.16pp is primarily driven by enhanced frontend validation performance and successful checkout conversion, with most funnel steps showing positive momentum. While payment visit volume decreased significantly (-23.9%), the quality of conversion improved across the customer journey, suggesting successful optimization efforts or favorable user behavior changes during this period.

---

## SQL Queries

<details>
<summary>Waterfall GA</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'HF-INTL' as cluster
),
weeks AS (
  SELECT 
    (SELECT affected_week FROM params) as affected_week,
    LAG(iso_year_week) OVER (ORDER BY iso_year_week) as prev_week
  FROM (SELECT DISTINCT iso_year_week FROM dimensions.date_dimension)
  WHERE iso_year_week <= (SELECT affected_week FROM params)
  QUALIFY iso_year_week = (SELECT affected_week FROM params)
),
countries AS (
  SELECT business_unit as country
  FROM payments_hf.business_units
  WHERE ARRAY_CONTAINS(reporting_cluster_array, (SELECT cluster FROM params))
)
SELECT
  d.iso_year_week AS hellofresh_week,
  SUM(is_pay_visit) AS payment_visits,
  SUM(is_select) AS select_payment_method,
  SUM(is_click) AS click_submit_form,
  SUM(CASE WHEN is_fs_check = 1 THEN 1 WHEN is_click = 1 AND is_fe_validation_error = 0 THEN 1 ELSE is_fe_validation_passed END) AS fe_validation_passed,
  SUM(is_fs_check) AS enter_fraud_service,
  SUM(CASE WHEN is_fs_check = 1 AND is_voucher_fraud_block = 0 AND is_payment_fraud_block = 0 THEN 1 ELSE 0 END) AS approved_by_fraud_service,
  SUM(is_pvs) AS call_to_pvs,
  SUM(is_success) AS successful_checkout
FROM spark_catalog.payments_hf.fact_payment_conversion_rate f
JOIN dimensions.date_dimension d ON f.date_string_backwards = d.date_string_backwards
CROSS JOIN weeks w
WHERE d.iso_year_week IN (w.affected_week, w.prev_week)
  AND f.country IN (SELECT country FROM countries)
GROUP BY 1
ORDER BY hellofresh_week

```

</details>

<details>
<summary>Backend Combined</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'HF-INTL' as cluster
),
week_dates AS (
  SELECT 
    MIN(date_string_backwards) as start_date,
    MAX(date_string_backwards) as end_date,
    iso_year_week
  FROM dimensions.date_dimension
  WHERE iso_year_week IN (
    (SELECT affected_week FROM params),
    (SELECT MAX(iso_year_week) FROM dimensions.date_dimension 
     WHERE iso_year_week < (SELECT affected_week FROM params))
  )
  GROUP BY iso_year_week
),
date_range AS (
  SELECT MIN(start_date) as min_date, MAX(end_date) as max_date
  FROM week_dates
),
countries AS (
  SELECT business_unit as country
  FROM payments_hf.business_units
  WHERE ARRAY_CONTAINS(reporting_cluster_array, (SELECT cluster FROM params))
)
SELECT
  wd.iso_year_week AS hellofresh_week,
  f.payment_method,
  SUM(event_payment_method_listed) AS payment_method_listed,
  SUM(event_checkout_attempt) AS checkout_attempt,
  SUM(event_attempted_fraud_check) AS enter_fraud_service,
  SUM(CASE WHEN event_attempted_fraud_check = 1 AND event_fs_blocked = 0 THEN 1 ELSE 0 END) AS approved_by_fraud_service,
  SUM(event_payment_verification_attempt) AS pvs_attempt,
  SUM(event_payment_verification_success) AS pvs_success,
  SUM(event_checkout_success) AS checkout_success
FROM spark_catalog.payments_hf.checkout_funnel_backend f
JOIN week_dates wd ON f.event_date BETWEEN wd.start_date AND wd.end_date
WHERE f.event_date BETWEEN (SELECT min_date FROM date_range) AND (SELECT max_date FROM date_range)
  AND f.country IN (SELECT country FROM countries)
GROUP BY 1, 2
ORDER BY hellofresh_week, checkout_attempt DESC

```

</details>

---

*Report: 2026-04-07*
