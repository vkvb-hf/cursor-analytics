# PCR Investigation: HF-INTL 2026-W14

**Metric:** Payment Conversion Rate (PCR)  
**Period:** 2026-W13 → 2026-W14  
**Observation:**  
GA: 34.88% → 36.04% (+1.16pp, 3.3% change)  
Backend: 38.66% → 39.90% (+1.25pp, 3.2% change)  
**Volume:** ~62K payment visits

---

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate (PCR) improved week-over-week, with GA increasing by +1.16pp (34.88% → 36.04%) and Backend increasing by +1.25pp (38.66% → 39.90%), despite a significant -23.9% drop in payment visit volume.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | GA step conversion | +0.42pp | ✅ |
| Click Submit Form | GA step conversion | +0.59pp | ✅ |
| FE Validation Passed | GA step conversion | +0.68pp | ✅ |
| Enter Fraud Service | GA step conversion | +0.40pp | ✅ |
| Approved by Fraud Service | GA step conversion | -0.24pp | ⚠️ |
| Call to PVS | GA step conversion | -0.01pp | ✅ |
| Successful Checkout | GA step conversion | +0.85pp | ✅ |
| Checkout Attempt | Backend step conversion | +1.54pp | ✅ |
| Enter Fraud Service | Backend step conversion | -0.35pp | ⚠️ |
| Approved by Fraud Service | Backend step conversion | -0.43pp | ⚠️ |
| PVS Attempt | Backend step conversion | +0.73pp | ✅ |
| PVS Success | Backend step conversion | +0.79pp | ✅ |

**Key Findings:**
- **Braintree ApplePay showed strongest improvement** among payment methods with +1.70pp gain (83.73% → 85.43%), contributing positively to overall PCR
- **FE Validation recovery rate improved by +1.47pp** (56.10% → 57.57%), indicating customers are more successfully recovering from frontend errors
- **PVS failures decreased significantly** from 1,522 to 1,010 (-512 failures), with "Insufficient Funds" declines dropping by -4.31pp share
- **Fraud Service approval rates slightly declined** in both GA (-0.24pp) and Backend (-0.43pp) waterfalls, warranting monitoring
- **APPLEPAY_DISMISSED remains the dominant FE error** at 76.8% of all errors, though this is expected user behavior

**Action:** Monitor — The PCR improvement is healthy across most funnel steps. Continue observing fraud service approval trends and maintain current configurations.

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
| **Successful Checkout** | 41,021 | 32,545 | -8,476 | -20.7% | 108.80% | 107.74% | -1.06pp |
| **PCR Rate** | | | | | 38.66% | 39.90% | **+1.25pp** |

---

## Payment Method Breakdown

| Payment Method | 2026-W13 Attempt | 2026-W13 Success | 2026-W13 Rate | 2026-W14 Attempt | 2026-W14 Success | 2026-W14 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 17,791 | 15,715 | 88.33% | 14,680 | 12,973 | 88.37% | +0.04pp |
| Braintree_ApplePay | 13,360 | 11,186 | 83.73% | 10,592 | 9,049 | 85.43% | +1.70pp |
| Braintree_Paypal | 9,125 | 8,314 | 91.11% | 7,030 | 6,377 | 90.71% | -0.40pp |
| Adyen_Klarna | 2,195 | 2,082 | 94.85% | 1,481 | 1,394 | 94.13% | -0.73pp |
| Adyen_IDeal | 1,887 | 1,732 | 91.79% | 1,322 | 1,218 | 92.13% | +0.35pp |
| ProcessOut_ApplePay | 1,558 | 1,429 | 91.72% | 1,213 | 1,098 | 90.52% | -1.20pp |
| Adyen_Sepa | 984 | 2 | 0.20% | 1,024 | 3 | 0.29% | +0.09pp |
| Adyen_BcmcMobile | 475 | 460 | 96.84% | 384 | 368 | 95.83% | -1.01pp |
| Adyen_CreditCard | 116 | 100 | 86.21% | 69 | 63 | 91.30% | +5.10pp |
| NoPayment | 105 | 0 | 0.00% | 42 | 0 | 0.00% | +0.00pp |

---

## FE Validation Errors

*Included because FE Validation Passed Δ Conv (+0.68pp) meets threshold (+0.58pp)*

### Recovery Rate

| Metric | 2026-W13 | 2026-W14 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 6,594 | 4,801 | -1,793 |
| Error → Passed | 3,699 | 2,764 | -935 |
| **Recovery Rate** | **56.10%** | **57.57%** | **+1.47pp** |

*Recovery Rate = Customers who had error but still passed / Customers with FE Error*

### Error Type Distribution

| Error Type | 2026-W13 | 2026-W13 % | 2026-W14 | 2026-W14 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 4,957 | 75.2% | 3,689 | 76.8% | +1.66pp |
| PAYPAL_POPUP_CLOSED | 1,434 | 21.7% | 910 | 19.0% | -2.79pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 329 | 5.0% | 255 | 5.3% | +0.32pp |
| PAYPAL_TOKENISE_ERR | 170 | 2.6% | 106 | 2.2% | -0.37pp |
| CC_TOKENISE_ERR | 122 | 1.9% | 102 | 2.1% | +0.27pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 150 | 2.3% | 98 | 2.0% | -0.23pp |
| APPLEPAY_TOKENISE_ERR | 0 | 0.0% | 6 | 0.1% | +0.12pp |
| APPLEPAY_MERCHANT_VALIDATION_ERR | 2 | 0.0% | 1 | 0.0% | -0.01pp |

*% of Errors = Error Type Count / Customers with FE Error (can exceed 100% as customers may have multiple error types)*

---

## Payment Verification Errors

*Included because PVS Success Δ Conv (+0.85pp) meets threshold (+0.58pp)*

| Decline Reason | 2026-W13 | 2026-W13 % | 2026-W14 | 2026-W14 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| RedirectShopper | 455 | 29.9% | 325 | 32.2% | -130 | +2.28pp |
| Cancelled: Cancelled | 239 | 15.7% | 192 | 19.0% | -47 | +3.31pp |
| Failed Verification: Insufficient Funds | 263 | 17.3% | 131 | 13.0% | -132 | -4.31pp |
| Failed Verification: Declined | 130 | 8.5% | 90 | 8.9% | -40 | +0.37pp |
| Pending | 128 | 8.4% | 88 | 8.7% | -40 | +0.30pp |
| Refused: Refused | 163 | 10.7% | 83 | 8.2% | -80 | -2.49pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 103 | 6.8% | 58 | 5.7% | -45 | -1.02pp |
| Failed Verification: Security | 25 | 1.6% | 24 | 2.4% | -1 | +0.73pp |
| Failed Verification: OK: 83 : Fraud/Security | 11 | 0.7% | 10 | 1.0% | -1 | +0.27pp |
| Blocked Verification: Payment method is blocked due to business reasons | 5 | 0.3% | 9 | 0.9% | +4 | +0.56pp |
| **Total PVS Failures** | **1,522** | **100%** | **1,010** | **100%** | **-512** | - |

---
## Conclusion

The PCR improvement in W14 reflects genuine funnel health gains across multiple steps, particularly in checkout initiation (+1.54pp backend), PVS success (+0.79pp), and FE validation recovery (+1.47pp). The volume decrease (-23.9% payment visits) did not negatively impact conversion quality, suggesting higher-intent traffic or improved user experience. The slight decline in fraud service approval rates (-0.24pp to -0.43pp) should be monitored but does not currently require intervention.

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
  SUM(CASE WHEN event_payment_method_listed = 1 AND event_checkout_success = 1 THEN 1 ELSE 0 END) AS checkout_success
FROM spark_catalog.payments_hf.checkout_funnel_backend f
JOIN week_dates wd ON f.event_date BETWEEN wd.start_date AND wd.end_date
WHERE f.event_date BETWEEN (SELECT min_date FROM date_range) AND (SELECT max_date FROM date_range)
  AND f.country IN (SELECT country FROM countries)
GROUP BY 1, 2
ORDER BY hellofresh_week, checkout_attempt DESC

```

</details>

<details>
<summary>FE Recovery Rate</summary>

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
  SUM(is_click) AS click_submit,
  SUM(CASE WHEN is_click = 1 AND is_fe_validation_error = 1 THEN 1 ELSE 0 END) AS customers_with_fe_error,
  SUM(CASE WHEN is_click = 1 AND is_fe_validation_error = 1 AND is_fe_validation_passed = 1 THEN 1 ELSE 0 END) AS error_then_passed,
  SUM(CASE WHEN is_click = 1 AND is_fe_validation_error = 1 AND is_fe_validation_passed = 0 THEN 1 ELSE 0 END) AS error_not_passed
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
<summary>FE Validation Errors</summary>

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
  iso_year_week AS hellofresh_week,
  label_error,
  SUM(errors) AS errors
FROM payments_hf.dash_ga_error
CROSS JOIN weeks w
WHERE iso_year_week IN (w.affected_week, w.prev_week)
  AND country IN (SELECT country FROM countries)
  AND event_action = 'PaymentFormFEValidationError'
GROUP BY 1, 2
ORDER BY hellofresh_week, errors DESC

```

</details>

<details>
<summary>PVS Decline Reasons</summary>

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
  pvs_last_payload.decline_response AS decline_reason,
  COUNT(*) AS customers
FROM spark_catalog.payments_hf.checkout_funnel_backend f
JOIN week_dates wd ON f.event_date BETWEEN wd.start_date AND wd.end_date
WHERE f.event_date BETWEEN (SELECT min_date FROM date_range) AND (SELECT max_date FROM date_range)
  AND f.country IN (SELECT country FROM countries)
  AND event_payment_verification_attempt = 1
  AND event_payment_verification_success = 0
  AND pvs_last_payload.decline_response IS NOT NULL
GROUP BY 1, 2
ORDER BY hellofresh_week, customers DESC

```

</details>


---

*Report: 2026-04-08*
