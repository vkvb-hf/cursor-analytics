# PCR Investigation: HF-NA 2026-W14

**Metric:** Payment Conversion Rate (PCR)  
**Period:** 2026-W13 → 2026-W14  
**Observation:**  
GA: 28.63% → 27.95% (-0.68pp, -2.4% change)  
Backend: 30.39% → 29.86% (-0.53pp, -1.7% change)  
**Volume:** ~59K payment visits

---

## Executive Summary

## Executive Summary

**Overall:** PCR declined by -0.68pp (GA) and -0.53pp (Backend) in 2026-W14, driven primarily by upper-funnel drop-offs in payment method selection and frontend validation, while downstream conversion steps remained stable or slightly improved.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | >-0.50pp? | -0.34pp | ✅ |
| Click Submit Form | >-0.50pp? | -0.41pp | ✅ |
| FE Validation Passed | >-0.50pp? | -0.67pp | ⚠️ |
| Enter Fraud Service | >-0.50pp? | -0.15pp | ✅ |
| Approved by Fraud Service | >-0.50pp? | -0.33pp | ✅ |
| Call to PVS | >-0.50pp? | -0.18pp | ✅ |
| Successful Checkout | >-0.50pp? | +0.28pp | ✅ |

**Key Findings:**
- **FE Validation Passed** shows the largest conversion drop at -0.67pp, exceeding the threshold and warranting investigation
- **FE Recovery Rate** declined from 72.25% to 70.06% (-2.19pp), meaning fewer customers who encountered errors successfully completed validation
- **APPLEPAY_DISMISSED** errors increased in share (+2.33pp), now representing 56.9% of all FE errors
- **Backend Checkout Attempt** dropped significantly (-1.14pp conversion, -993 attempts), indicating upper-funnel friction
- **ProcessOut_CreditCard** and **Braintree_ApplePay** success rates actually improved (+1.69pp and +1.61pp respectively), suggesting the issue is not with payment processors

**Action:** **Investigate** — Focus on the FE Validation decline and increased APPLEPAY_DISMISSED errors. Review any recent frontend changes affecting Apple Pay user flows and terms acceptance screens.

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
| **Successful Checkout** | 20,042 | 19,496 | -546 | -2.7% | 102.83% | 102.43% | -0.40pp |
| **PCR Rate** | | | | | 30.39% | 29.86% | **-0.53pp** |

---

## Payment Method Breakdown

| Payment Method | 2026-W13 Attempt | 2026-W13 Success | 2026-W13 Rate | 2026-W14 Attempt | 2026-W14 Success | 2026-W14 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 14,991 | 12,281 | 81.92% | 13,953 | 11,666 | 83.61% | +1.69pp |
| Braintree_ApplePay | 7,428 | 5,796 | 78.03% | 7,371 | 5,870 | 79.64% | +1.61pp |
| Braintree_Paypal | 1,961 | 1,707 | 87.05% | 2,071 | 1,793 | 86.58% | -0.47pp |
| Adyen_CreditCard | 130 | 5 | 3.85% | 241 | 7 | 2.90% | -0.94pp |
| Braintree_CreditCard | 281 | 253 | 90.04% | 178 | 158 | 88.76% | -1.27pp |
|  | 136 | 0 | 0.00% | 120 | 1 | 0.83% | +0.83pp |
| Braintree_Venmo | 0 | 0 | 0.00% | 1 | 1 | 100.00% | +100.00pp |
| ApplePay | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |
| CreditCard | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |
| NoPayment | 1 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |

---

## FE Validation Errors

*Included because FE Validation Passed Δ Conv (-0.67pp) meets threshold (+0.34pp)*

### Recovery Rate

| Metric | 2026-W13 | 2026-W14 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 4,587 | 4,519 | -68 |
| Error → Passed | 3,314 | 3,166 | -148 |
| **Recovery Rate** | **72.25%** | **70.06%** | **-2.19pp** |

*Recovery Rate = Customers who had error but still passed / Customers with FE Error*

### Error Type Distribution

| Error Type | 2026-W13 | 2026-W13 % | 2026-W14 | 2026-W14 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 2,505 | 54.6% | 2,573 | 56.9% | +2.33pp |
| terms_not_accepted | 2,064 | 45.0% | 1,834 | 40.6% | -4.41pp |
| PAYPAL_POPUP_CLOSED | 455 | 9.9% | 421 | 9.3% | -0.60pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 293 | 6.4% | 280 | 6.2% | -0.19pp |
| CC_TOKENISE_ERR | 158 | 3.4% | 149 | 3.3% | -0.15pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 123 | 2.7% | 120 | 2.7% | -0.03pp |
| PAYPAL_TOKENISE_ERR | 39 | 0.9% | 33 | 0.7% | -0.12pp |
| CC_NO_PREPAID_ERR | 2 | 0.0% | 2 | 0.0% | +0.00pp |
| EXPRESS_CHECKOUT_APPLEPAY_TOKENISE_ERR | 0 | 0.0% | 1 | 0.0% | +0.02pp |

*% of Errors = Error Type Count / Customers with FE Error (can exceed 100% as customers may have multiple error types)*

---
## Conclusion

The PCR decline in 2026-W14 is primarily attributable to frontend validation issues, with the FE Validation Passed step showing a -0.67pp conversion drop and recovery rates declining by -2.19pp. The increase in APPLEPAY_DISMISSED errors suggests potential UX friction in the Apple Pay flow. Downstream steps from fraud service onward performed normally, indicating the root cause lies in the early checkout experience rather than payment processing infrastructure.

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


---

*Report: 2026-04-08*
