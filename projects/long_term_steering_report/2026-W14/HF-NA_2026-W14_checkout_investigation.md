# PCR Investigation: HF-NA 2026-W14

**Metric:** Payment Conversion Rate (PCR)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 28.63% → 27.95% (-0.68pp)  
**Volume:** ~59K payment visits

---

## Executive Summary

**Overall:** Payment Conversion Rate declined from 28.63% to 27.95%, a decrease of 0.68 percentage points during week 2026-W14.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Volume down, conversion down | -0.34pp | ⚠️ |
| Click Submit Form | Volume down, conversion down | -0.41pp | ⚠️ |
| FE Validation Passed | Volume down, conversion down | -0.67pp | ⚠️ |
| Enter Fraud Service | Volume down, minor conversion drop | -0.15pp | ⚠️ |
| Approved by Fraud Service | Volume down, conversion down | -0.33pp | ⚠️ |
| Call to PVS | Volume down, conversion down | -0.18pp | ⚠️ |
| Successful Checkout | Volume down, conversion improved | +0.28pp | ✅ |

**Key Findings:**
- Frontend validation showed the largest conversion drop at -0.67pp, indicating potential issues with form validation processes
- Payment volume declined across all funnel steps with Select Payment Method showing -135 fewer conversions
- Individual payment methods showed mixed performance: Adyen_CreditCard improved significantly (+5.74pp) while Braintree_Paypal declined (-0.33pp)
- Backend data shows checkout attempts dropped by 4.0% while fraud service approval rates actually improved (+1.55pp)
- The final checkout step performed better than previous week (+0.28pp conversion), suggesting the issue is in user engagement rather than payment processing

**Action:** Investigate - Focus on frontend validation issues and user drop-off patterns in early funnel steps.

---

---

## Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 59,286 | 59,447 | 161 | 0.3% | - | - | - |
| Select Payment Method | 24,367 | 24,232 | -135 | -0.6% | 41.10% | 40.76% | -0.34pp |
| Click Submit Form | 20,847 | 20,633 | -214 | -1.0% | 85.55% | 85.15% | -0.41pp |
| FE Validation Passed | 19,788 | 19,446 | -342 | -1.7% | 94.92% | 94.25% | -0.67pp |
| Enter Fraud Service | 19,364 | 19,001 | -363 | -1.9% | 97.86% | 97.71% | -0.15pp |
| Approved by Fraud Service | 18,111 | 17,708 | -403 | -2.2% | 93.53% | 93.20% | -0.33pp |
| Call to PVS | 18,097 | 17,662 | -435 | -2.4% | 99.92% | 99.74% | -0.18pp |
| **Successful Checkout** | 16,975 | 16,617 | -358 | -2.1% | 93.80% | 94.08% | +0.28pp |
| **PCR Rate** | | | | | 28.63% | 27.95% | **-0.68pp** |

---

## Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 65,957 | 65,294 | -663 | -1.0% | - | - | - |
| Checkout Attempt | 24,928 | 23,935 | -993 | -4.0% | 37.79% | 36.66% | -1.14pp |
| Enter Fraud Service | 24,773 | 23,622 | -1,151 | -4.6% | 99.38% | 98.69% | -0.69pp |
| Approved by Fraud Service | 22,212 | 21,545 | -667 | -3.0% | 89.66% | 91.21% | +1.55pp |
| PVS Attempt | 20,751 | 20,221 | -530 | -2.6% | 93.42% | 93.85% | +0.43pp |
| PVS Success | 19,490 | 19,033 | -457 | -2.3% | 93.92% | 94.12% | +0.20pp |
| **Successful Checkout** | 20,997 | 20,515 | -482 | -2.3% | 107.73% | 107.79% | +0.05pp |

---

## Payment Method Breakdown

| Payment Method | 2026-W13 Attempt | 2026-W13 Success | 2026-W13 Rate | 2026-W14 Attempt | 2026-W14 Success | 2026-W14 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 14,991 | 12,309 | 82.11% | 13,953 | 11,693 | 83.80% | +1.69pp |
| Braintree_ApplePay | 7,428 | 6,470 | 87.10% | 7,371 | 6,504 | 88.24% | +1.13pp |
| Braintree_Paypal | 1,961 | 1,709 | 87.15% | 2,071 | 1,798 | 86.82% | -0.33pp |
| Adyen_CreditCard | 130 | 122 | 93.85% | 241 | 240 | 99.59% | +5.74pp |
| Braintree_CreditCard | 281 | 257 | 91.46% | 178 | 160 | 89.89% | -1.57pp |
|  | 136 | 129 | 94.85% | 120 | 119 | 99.17% | +4.31pp |
| Braintree_Venmo | 0 | 0 | 0.00% | 1 | 1 | 100.00% | +100.00pp |
| ApplePay | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |
| CreditCard | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |
| NoPayment | 1 | 1 | 100.00% | 0 | 0 | 0.00% | -100.00pp |

---

## Conclusion

The 0.68pp decline in PCR appears driven primarily by frontend user experience issues, particularly in form validation and early funnel engagement, rather than payment processing problems. While backend systems showed improved fraud approval rates and final checkout conversion increased, the significant drop-off in frontend validation (-0.67pp) and reduced user engagement at payment method selection warrant immediate investigation into potential UI/UX issues or technical problems affecting user experience.

---

## SQL Queries

<details>
<summary>Waterfall GA</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'HF-NA' as cluster
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
  SELECT '2026-W14' as affected_week, 'HF-NA' as cluster
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
