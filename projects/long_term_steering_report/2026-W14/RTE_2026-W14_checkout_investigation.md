# PCR Investigation: RTE 2026-W14

**Metric:** Payment Conversion Rate (PCR)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 37.81% → 39.36% (+1.56pp)  
**Volume:** ~63K payment visits

---

## Executive Summary

**Overall:** Payment Conversion Rate improved by +1.56pp from 37.81% to 39.36% during 2026-W14, despite a 10.4% decrease in payment visit volume.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | 48.18% → 49.94% | +1.76pp | ✅ |
| Click Submit Form | 89.19% → 90.09% | +0.90pp | ✅ |
| FE Validation Passed | 97.61% → 97.15% | -0.46pp | ⚠️ |
| Enter Fraud Service | 97.99% → 97.78% | -0.21pp | ⚠️ |
| Approved by Fraud Service | 96.11% → 95.98% | -0.13pp | ⚠️ |
| Call to PVS | 99.89% → 99.80% | -0.09pp | ⚠️ |
| Successful Checkout | 95.83% → 96.15% | +0.32pp | ✅ |

**Key Findings:**
- Early funnel performance drove the PCR improvement, with Select Payment Method (+1.76pp) and Click Submit Form (+0.90pp) showing strong gains
- Mid-funnel steps experienced slight degradation, particularly FE Validation (-0.46pp) and fraud service approval rates (-0.13pp)
- Final checkout success rate improved (+0.32pp), offsetting mid-funnel losses and contributing to overall PCR gains
- Payment volume decreased significantly (-10.4% to ~63K visits) but conversion quality improved across the funnel
- Backend data shows similar patterns with checkout attempt rate improving (+1.97pp) and PVS success rate remaining stable (+0.01pp)

**Action:** Monitor

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
| **Successful Checkout** | 42,106 | 39,663 | -2,443 | -5.8% | 101.31% | 102.55% | +1.25pp |

---

## Payment Method Breakdown

| Payment Method | 2026-W13 Attempt | 2026-W13 Success | 2026-W13 Rate | 2026-W14 Attempt | 2026-W14 Success | 2026-W14 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 17,491 | 16,287 | 93.12% | 17,123 | 15,983 | 93.34% | +0.23pp |
| Braintree_ApplePay | 11,367 | 10,474 | 92.14% | 10,528 | 9,741 | 92.52% | +0.38pp |
| Adyen_CreditCard | 9,936 | 9,165 | 92.24% | 9,248 | 8,450 | 91.37% | -0.87pp |
| Braintree_Paypal | 5,297 | 4,964 | 93.71% | 4,880 | 4,523 | 92.68% | -1.03pp |
| Adyen_IDeal | 809 | 756 | 93.45% | 676 | 610 | 90.24% | -3.21pp |
| Adyen_Klarna | 378 | 347 | 91.80% | 297 | 273 | 91.92% | +0.12pp |
| Braintree_CreditCard | 125 | 105 | 84.00% | 91 | 76 | 83.52% | -0.48pp |
| Braintree_Venmo | 4 | 4 | 100.00% | 6 | 6 | 100.00% | +0.00pp |
|  | 4 | 4 | 100.00% | 1 | 1 | 100.00% | +0.00pp |

---

## Conclusion

The PCR improvement of +1.56pp represents a positive trend driven primarily by enhanced early-funnel performance, with users more likely to select payment methods and submit forms. While mid-funnel conversion rates showed minor degradation, particularly in validation and fraud processing, the strong early-funnel gains and improved final checkout success resulted in net positive performance despite reduced traffic volume.

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
