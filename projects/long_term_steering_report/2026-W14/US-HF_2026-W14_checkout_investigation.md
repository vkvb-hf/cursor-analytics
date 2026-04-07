# PCR Investigation: US-HF 2026-W14

**Metric:** Payment Conversion Rate (PCR)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 26.77% → 26.40% (-0.37pp)  
**Volume:** ~44K payment visits

---

## Executive Summary

**Overall:** Payment Conversion Rate declined by 0.37pp from 26.77% to 26.40% in 2026-W14, representing a moderate deterioration in payment performance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | GA | -0.42pp | ⚠️ |
| Click Submit Form | GA | +0.02pp | ✅ |
| FE Validation Passed | GA | -0.41pp | ⚠️ |
| Enter Fraud Service | GA | +0.11pp | ✅ |
| Approved by Fraud Service | GA | -0.00pp | ✅ |
| Call to PVS | GA | -0.23pp | ⚠️ |
| Successful Checkout | GA | +0.26pp | ✅ |
| Checkout Attempt | Backend | -0.99pp | ⚠️ |
| Enter Fraud Service | Backend | -0.77pp | ⚠️ |
| Approved by Fraud Service | Backend | +2.75pp | ✅ |

**Key Findings:**
- Early funnel shows weakness with Select Payment Method conversion declining 0.42pp (37.60% → 37.18%) in GA flow
- Backend checkout attempts dropped significantly by 0.99pp (36.46% → 35.46%), indicating user engagement issues
- Fraud service approval rates improved substantially by 2.75pp (89.15% → 91.91%) in backend flow, suggesting better fraud detection accuracy
- ProcessOut_CreditCard and Braintree_ApplePay both showed strong improvements (+3.23pp and +1.80pp respectively), while Braintree_Paypal declined slightly (-0.87pp)
- Overall payment volumes decreased across both GA (-319 visits, -0.7%) and backend (-853 attempts, -4.8%) flows

**Action:** Investigate - Focus on early funnel optimization, particularly payment method selection and initial checkout attempt conversion issues.

---

---

## Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 44,370 | 44,051 | -319 | -0.7% | - | - | - |
| Select Payment Method | 16,684 | 16,377 | -307 | -1.8% | 37.60% | 37.18% | -0.42pp |
| Click Submit Form | 14,732 | 14,464 | -268 | -1.8% | 88.30% | 88.32% | +0.02pp |
| FE Validation Passed | 13,994 | 13,680 | -314 | -2.2% | 94.99% | 94.58% | -0.41pp |
| Enter Fraud Service | 13,714 | 13,422 | -292 | -2.1% | 98.00% | 98.11% | +0.11pp |
| Approved by Fraud Service | 12,847 | 12,573 | -274 | -2.1% | 93.68% | 93.67% | -0.00pp |
| Call to PVS | 12,852 | 12,549 | -303 | -2.4% | 100.04% | 99.81% | -0.23pp |
| **Successful Checkout** | 11,879 | 11,631 | -248 | -2.1% | 92.43% | 92.68% | +0.26pp |
| **PCR Rate** | | | | | 26.77% | 26.40% | **-0.37pp** |

---

## Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 48,829 | 47,792 | -1,037 | -2.1% | - | - | - |
| Checkout Attempt | 17,802 | 16,949 | -853 | -4.8% | 36.46% | 35.46% | -0.99pp |
| Enter Fraud Service | 17,647 | 16,671 | -976 | -5.5% | 99.13% | 98.36% | -0.77pp |
| Approved by Fraud Service | 15,733 | 15,322 | -411 | -2.6% | 89.15% | 91.91% | +2.75pp |
| PVS Attempt | 15,361 | 14,911 | -450 | -2.9% | 97.64% | 97.32% | -0.32pp |
| PVS Success | 14,219 | 13,845 | -374 | -2.6% | 92.57% | 92.85% | +0.29pp |
| **Successful Checkout** | 14,691 | 14,421 | -270 | -1.8% | 103.32% | 104.16% | +0.84pp |

---

## Payment Method Breakdown

| Payment Method | 2026-W13 Attempt | 2026-W13 Success | 2026-W13 Rate | 2026-W14 Attempt | 2026-W14 Success | 2026-W14 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 10,229 | 8,131 | 79.49% | 9,309 | 7,700 | 82.72% | +3.23pp |
| Braintree_ApplePay | 5,750 | 4,934 | 85.81% | 5,745 | 5,033 | 87.61% | +1.80pp |
| Braintree_Paypal | 1,298 | 1,133 | 87.29% | 1,384 | 1,196 | 86.42% | -0.87pp |
| Adyen_CreditCard | 108 | 107 | 99.07% | 212 | 212 | 100.00% | +0.93pp |
| Braintree_CreditCard | 281 | 257 | 91.46% | 178 | 160 | 89.89% | -1.57pp |
|  | 136 | 129 | 94.85% | 120 | 119 | 99.17% | +4.31pp |
| Braintree_Venmo | 0 | 0 | 0.00% | 1 | 1 | 100.00% | +100.00pp |

---

## Conclusion

The 0.37pp decline in PCR appears to be driven primarily by reduced user engagement in the early stages of the payment funnel, with Select Payment Method and Checkout Attempt conversions showing notable deterioration. While fraud service improvements and strong performance from major payment methods (ProcessOut_CreditCard, Braintree_ApplePay) provide positive signals, the overall trend requires investigation into user experience factors affecting initial payment engagement.

---

## SQL Queries

<details>
<summary>Waterfall GA</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'US-HF' as cluster
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
  SELECT '2026-W14' as affected_week, 'US-HF' as cluster
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
