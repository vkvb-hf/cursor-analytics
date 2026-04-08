# PCR Investigation: RTE 2026-W14

**Metric:** Payment Conversion Rate (PCR)  
**Period:** 2026-W13 → 2026-W14  
**Observation:**  
GA: 37.81% → 39.36% (+1.56pp, 4.1% change)  
Backend: 33.67% → 35.22% (+1.55pp, 4.6% change)  
**Volume:** ~63K payment visits

---

## Executive Summary

## Executive Summary

**Overall:** PCR improved in 2026-W14, with GA increasing +1.56pp (37.81% → 39.36%) and Backend increasing +1.55pp (33.67% → 35.22%), despite a -10.4% decrease in payment visit volume (~63K visits).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | GA entry rate | +1.76pp | ✅ |
| Click Submit Form | Form submission | +0.90pp | ✅ |
| FE Validation Passed | Frontend validation | -0.46pp | ⚠️ |
| Enter Fraud Service | Fraud check entry | -0.21pp | ✅ |
| Approved by Fraud Service | Fraud approval | -0.12pp | ✅ |
| Call to PVS | PVS routing | -0.09pp | ✅ |
| Successful Checkout (GA) | Final conversion | +0.32pp | ✅ |
| PVS Attempt (Backend) | PVS attempt rate | -1.25pp | ⚠️ |
| PVS Success (Backend) | PVS success rate | +0.01pp | ✅ |

**Key Findings:**
- Top-of-funnel improvement drove PCR gains: Select Payment Method conversion increased +1.76pp and Click Submit Form improved +0.90pp
- Backend PVS Attempt rate dropped -1.25pp (99.46% → 98.21%), indicating potential routing issues between fraud approval and payment verification
- Adyen_IDeal showed the largest payment method decline at -3.21pp (93.45% → 90.24%), though on relatively low volume (676 attempts)
- Braintree_ApplePay declined -1.71pp (87.23% → 85.51%) on significant volume (~10.5K attempts), warranting attention
- ProcessOut_CreditCard, the highest-volume method (~17K attempts), remained stable with slight improvement (+0.30pp)

**Action:** Monitor — Overall PCR improvement is positive. Investigate the Backend PVS Attempt drop (-1.25pp) and Braintree_ApplePay decline (-1.71pp) if trends persist in W15.

---

---

## Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 70,720 | 63,359 | -7,361 | -10.4% | - | - | - |
| Select Payment Method | 34,070 | 31,640 | -2,430 | -7.1% | 48.18% | 49.94% | +1.76pp |
| Click Submit Form | 30,387 | 28,506 | -1,881 | -6.2% | 89.19% | 90.09% | +0.90pp |
| FE Validation Passed | 29,662 | 27,695 | -1,967 | -6.6% | 97.61% | 97.15% | -0.46pp |
| Enter Fraud Service | 29,066 | 27,080 | -1,986 | -6.8% | 97.99% | 97.78% | -0.21pp |
| Approved by Fraud Service | 27,934 | 25,992 | -1,942 | -7.0% | 96.11% | 95.98% | -0.12pp |
| Call to PVS | 27,902 | 25,940 | -1,962 | -7.0% | 99.89% | 99.80% | -0.09pp |
| **Successful Checkout** | 26,738 | 24,941 | -1,797 | -6.7% | 95.83% | 96.15% | +0.32pp |
| **PCR Rate** | | | | | 37.81% | 39.36% | **+1.56pp** |

---

## Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 123,045 | 110,209 | -12,836 | -10.4% | - | - | - |
| Checkout Attempt | 45,411 | 42,850 | -2,561 | -5.6% | 36.91% | 38.88% | +1.97pp |
| Enter Fraud Service | 45,337 | 42,766 | -2,571 | -5.7% | 99.84% | 99.80% | -0.03pp |
| Approved by Fraud Service | 43,132 | 40,642 | -2,490 | -5.8% | 95.14% | 95.03% | -0.10pp |
| PVS Attempt | 42,897 | 39,914 | -2,983 | -7.0% | 99.46% | 98.21% | -1.25pp |
| PVS Success | 41,563 | 38,675 | -2,888 | -6.9% | 96.89% | 96.90% | +0.01pp |
| **Successful Checkout** | 41,426 | 38,814 | -2,612 | -6.3% | 99.67% | 100.36% | +0.69pp |
| **PCR Rate** | | | | | 33.67% | 35.22% | **+1.55pp** |

---

## Payment Method Breakdown

| Payment Method | 2026-W13 Attempt | 2026-W13 Success | 2026-W13 Rate | 2026-W14 Attempt | 2026-W14 Success | 2026-W14 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 17,491 | 16,234 | 92.81% | 17,123 | 15,943 | 93.11% | +0.30pp |
| Braintree_ApplePay | 11,367 | 9,915 | 87.23% | 10,528 | 9,003 | 85.51% | -1.71pp |
| Adyen_CreditCard | 9,936 | 9,111 | 91.70% | 9,248 | 8,384 | 90.66% | -1.04pp |
| Braintree_Paypal | 5,297 | 4,954 | 93.52% | 4,880 | 4,520 | 92.62% | -0.90pp |
| Adyen_IDeal | 809 | 756 | 93.45% | 676 | 610 | 90.24% | -3.21pp |
| Adyen_Klarna | 378 | 347 | 91.80% | 297 | 273 | 91.92% | +0.12pp |
| Braintree_CreditCard | 125 | 105 | 84.00% | 91 | 75 | 82.42% | -1.58pp |
| Braintree_Venmo | 4 | 4 | 100.00% | 6 | 6 | 100.00% | +0.00pp |
|  | 4 | 0 | 0.00% | 1 | 0 | 0.00% | +0.00pp |

---

## Conclusion

The PCR improvement of +1.55-1.56pp in W14 is primarily driven by stronger top-of-funnel engagement, with more users selecting payment methods and completing form submissions. While overall performance is positive, the Backend PVS Attempt rate decline (-1.25pp) and underperformance of Braintree_ApplePay (-1.71pp) should be monitored in the coming week to ensure these do not develop into larger issues.

---

## SQL Queries

<details>
<summary>Waterfall GA</summary>

```sql

WITH params AS (
  SELECT '2026-W14' as affected_week, 'RTE' as cluster
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
  SELECT '2026-W14' as affected_week, 'RTE' as cluster
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
  SUM(CASE WHEN event_payment_method_listed = 1 AND event_checkout_success = 1 THEN 1 ELSE 0 END) AS checkout_success
FROM spark_catalog.payments_hf.checkout_funnel_backend f
JOIN week_dates wd ON f.event_date BETWEEN wd.start_date AND wd.end_date
WHERE f.event_date BETWEEN (SELECT min_date FROM date_range) AND (SELECT max_date FROM date_range)
  AND f.country IN (SELECT country FROM countries)
GROUP BY 1, 2
ORDER BY hellofresh_week, checkout_attempt DESC

```

</details>


---

*Report: 2026-04-08*
