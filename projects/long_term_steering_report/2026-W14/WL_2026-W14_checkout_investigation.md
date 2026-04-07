# PCR Investigation: WL 2026-W14

**Metric:** Payment Conversion Rate (PCR)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 30.03% → 29.88% (-0.15pp)  
**Volume:** ~35K payment visits

---

## Executive Summary

**Overall:** Payment Conversion Rate declined from 30.03% to 29.88% (-0.15pp) during week 2026-W14, representing a minor decrease despite reduced payment visit volumes.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | 40.94% → 40.67% | -0.26pp | ⚠️ |
| Click Submit Form | 88.42% → 88.51% | +0.09pp | ✅ |
| FE Validation Passed | 94.93% → 95.14% | +0.21pp | ✅ |
| Enter Fraud Service | 96.00% → 96.21% | +0.21pp | ✅ |
| Approved by Fraud Service | 94.63% → 94.52% | -0.11pp | ⚠️ |
| Call to PVS | 99.81% → 99.28% | -0.52pp | ⚠️ |
| Successful Checkout | 96.39% → 96.64% | +0.25pp | ✅ |

**Key Findings:**
- Payment visits decreased significantly by 8.1% (38,531 → 35,420), indicating reduced traffic volume
- Backend data shows a concerning drop in PVS Attempt conversion (98.79% → 89.07%, -9.71pp), suggesting payment processing issues
- Payment method performance was mixed: ProcessOut_ApplePay improved dramatically (+8.72pp) while Braintree_CreditCard declined (-2.50pp)
- The largest conversion drop occurred at "Call to PVS" step (-0.52pp), aligning with backend PVS processing issues
- Despite individual step challenges, the final checkout success rate improved (+0.25pp), partially offsetting earlier funnel losses

**Action:** Investigate - Focus on PVS processing issues and payment method routing optimization.

---

---

## Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 38,531 | 35,420 | -3,111 | -8.1% | - | - | - |
| Select Payment Method | 15,773 | 14,406 | -1,367 | -8.7% | 40.94% | 40.67% | -0.26pp |
| Click Submit Form | 13,947 | 12,751 | -1,196 | -8.6% | 88.42% | 88.51% | +0.09pp |
| FE Validation Passed | 13,240 | 12,131 | -1,109 | -8.4% | 94.93% | 95.14% | +0.21pp |
| Enter Fraud Service | 12,710 | 11,671 | -1,039 | -8.2% | 96.00% | 96.21% | +0.21pp |
| Approved by Fraud Service | 12,027 | 11,031 | -996 | -8.3% | 94.63% | 94.52% | -0.11pp |
| Call to PVS | 12,004 | 10,952 | -1,052 | -8.8% | 99.81% | 99.28% | -0.52pp |
| **Successful Checkout** | 11,571 | 10,584 | -987 | -8.5% | 96.39% | 96.64% | +0.25pp |
| **PCR Rate** | | | | | 30.03% | 29.88% | **-0.15pp** |

---

## Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 46,082 | 43,656 | -2,426 | -5.3% | - | - | - |
| Checkout Attempt | 14,782 | 13,713 | -1,069 | -7.2% | 32.08% | 31.41% | -0.67pp |
| Enter Fraud Service | 14,732 | 13,666 | -1,066 | -7.2% | 99.66% | 99.66% | -0.00pp |
| Approved by Fraud Service | 13,771 | 12,768 | -1,003 | -7.3% | 93.48% | 93.43% | -0.05pp |
| PVS Attempt | 13,604 | 11,373 | -2,231 | -16.4% | 98.79% | 89.07% | -9.71pp |
| PVS Success | 13,206 | 11,035 | -2,171 | -16.4% | 97.07% | 97.03% | -0.05pp |
| **Successful Checkout** | 13,396 | 12,378 | -1,018 | -7.6% | 101.44% | 112.17% | +10.73pp |

---

## Payment Method Breakdown

| Payment Method | 2026-W13 Attempt | 2026-W13 Success | 2026-W13 Rate | 2026-W14 Attempt | 2026-W14 Success | 2026-W14 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 4,073 | 3,676 | 90.25% | 3,917 | 3,517 | 89.79% | -0.46pp |
| Braintree_ApplePay | 4,162 | 3,839 | 92.24% | 3,733 | 3,417 | 91.53% | -0.70pp |
| Adyen_CreditCard | 2,682 | 2,381 | 88.78% | 2,796 | 2,515 | 89.95% | +1.17pp |
| Braintree_Paypal | 1,850 | 1,704 | 92.11% | 1,663 | 1,505 | 90.50% | -1.61pp |
| Braintree_CreditCard | 1,602 | 1,445 | 90.20% | 1,317 | 1,155 | 87.70% | -2.50pp |
| ProcessOut_ApplePay | 411 | 349 | 84.91% | 283 | 265 | 93.64% | +8.72pp |
|  | 0 | 0 | 0.00% | 2 | 2 | 100.00% | +100.00pp |
| Braintree_Venmo | 1 | 1 | 100.00% | 1 | 1 | 100.00% | +0.00pp |
| NoPayment | 1 | 1 | 100.00% | 1 | 1 | 100.00% | +0.00pp |
| CreditCard | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |

---

## Conclusion

The 0.15pp decline in PCR appears to be primarily driven by payment processing issues, particularly around PVS attempts which showed a significant 9.71pp conversion drop in the backend data. While some funnel steps improved and checkout success rates remained strong, the combination of reduced traffic volume and payment processing challenges warrants investigation into the underlying technical systems and payment method routing logic.

---

## SQL Queries

<details>
<summary>Waterfall GA</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'WL' as cluster
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
  SELECT '2026-W14' as affected_week, 'WL' as cluster
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
