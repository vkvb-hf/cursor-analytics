# PCR Investigation: US-HF 2026-W14

**Metric:** Payment Conversion Rate (PCR)  
**Period:** 2026-W13 → 2026-W14  
**Observation:**  
GA: 26.77% → 26.40% (-0.37pp, -1.4% change)  
Backend: 28.36% → 28.28% (-0.09pp, -0.3% change)  
**Volume:** ~44K payment visits

---

## Executive Summary

## Executive Summary

**Overall:** PCR declined by -0.37pp (26.77% → 26.40%) in GA tracking, while Backend showed a minimal decline of -0.09pp (28.36% → 28.28%), indicating the drop is primarily driven by upper-funnel behavior captured in GA.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | GA entry rate | -0.42pp | ⚠️ |
| Click Submit Form | Click-through | +0.02pp | ✅ |
| FE Validation Passed | Validation rate | -0.41pp | ⚠️ |
| Enter Fraud Service | Routing | +0.11pp | ✅ |
| Approved by Fraud Service | Fraud approval | -0.00pp | ✅ |
| Call to PVS | PVS routing | -0.23pp | ⚠️ |
| Successful Checkout | Final conversion | +0.26pp | ✅ |

**Key Findings:**
- **Select Payment Method drop (-0.42pp):** Entry rate to payment selection declined from 37.60% to 37.18%, contributing to overall volume reduction
- **FE Validation degradation (-0.41pp, -1.31pp recovery rate):** Recovery rate dropped from 75.67% to 74.36%; "terms_not_accepted" errors decreased (-4.50pp share) while "APPLEPAY_DISMISSED" remained stable (50.8%)
- **ProcessOut_CreditCard improved significantly (+3.21pp):** Success rate increased from 79.29% to 82.50%, partially offsetting other declines
- **Backend Checkout Attempt drop (-0.99pp):** Checkout attempt rate declined from 36.46% to 35.46%, indicating pre-checkout abandonment
- **Fraud Service approval improved in Backend (+2.75pp):** Approval rate increased from 89.15% to 91.91%, a positive signal

**Action:** **Monitor** - The decline is modest (-0.37pp) with compensating improvements in payment method success rates and fraud approval. Continue tracking FE validation recovery rate and Select Payment Method entry rate for sustained degradation.

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
| **Successful Checkout** | 13,849 | 13,514 | -335 | -2.4% | 97.40% | 97.61% | +0.21pp |
| **PCR Rate** | | | | | 28.36% | 28.28% | **-0.09pp** |

---

## Payment Method Breakdown

| Payment Method | 2026-W13 Attempt | 2026-W13 Success | 2026-W13 Rate | 2026-W14 Attempt | 2026-W14 Success | 2026-W14 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 10,229 | 8,111 | 79.29% | 9,309 | 7,680 | 82.50% | +3.21pp |
| Braintree_ApplePay | 5,750 | 4,354 | 75.72% | 5,745 | 4,481 | 78.00% | +2.28pp |
| Braintree_Paypal | 1,298 | 1,131 | 87.13% | 1,384 | 1,193 | 86.20% | -0.93pp |
| Adyen_CreditCard | 108 | 0 | 0.00% | 212 | 0 | 0.00% | +0.00pp |
| Braintree_CreditCard | 281 | 253 | 90.04% | 178 | 158 | 88.76% | -1.27pp |
|  | 136 | 0 | 0.00% | 120 | 1 | 0.83% | +0.83pp |
| Braintree_Venmo | 0 | 0 | 0.00% | 1 | 1 | 100.00% | +100.00pp |

---

## FE Validation Errors

*Included because FE Validation Passed Δ Conv (-0.41pp) meets threshold (+0.18pp)*

### Recovery Rate

| Metric | 2026-W13 | 2026-W14 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 3,678 | 3,553 | -125 |
| Error → Passed | 2,783 | 2,642 | -141 |
| **Recovery Rate** | **75.67%** | **74.36%** | **-1.31pp** |

*Recovery Rate = Customers who had error but still passed / Customers with FE Error*

### Error Type Distribution

| Error Type | 2026-W13 | 2026-W13 % | 2026-W14 | 2026-W14 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| terms_not_accepted | 2,064 | 56.1% | 1,834 | 51.6% | -4.50pp |
| APPLEPAY_DISMISSED | 1,840 | 50.0% | 1,805 | 50.8% | +0.77pp |
| PAYPAL_POPUP_CLOSED | 273 | 7.4% | 254 | 7.1% | -0.27pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 235 | 6.4% | 223 | 6.3% | -0.11pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 102 | 2.8% | 113 | 3.2% | +0.41pp |
| CC_TOKENISE_ERR | 102 | 2.8% | 108 | 3.0% | +0.27pp |
| PAYPAL_TOKENISE_ERR | 24 | 0.7% | 23 | 0.6% | -0.01pp |
| CC_NO_PREPAID_ERR | 2 | 0.1% | 2 | 0.1% | +0.00pp |
| EXPRESS_CHECKOUT_APPLEPAY_TOKENISE_ERR | 0 | 0.0% | 1 | 0.0% | +0.03pp |

*% of Errors = Error Type Count / Customers with FE Error (can exceed 100% as customers may have multiple error types)*

---

## Payment Verification Errors

*Included because PVS Success Δ Conv (+0.26pp) meets threshold (+0.18pp)*

| Decline Reason | 2026-W13 | 2026-W13 % | 2026-W14 | 2026-W14 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Blocked Verification: Payment method is blocked due to business reasons | 570 | 56.3% | 534 | 55.7% | -36 | -0.53pp |
| Failed Verification: Insufficient Funds | 166 | 16.4% | 158 | 16.5% | -8 | +0.11pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 64 | 6.3% | 52 | 5.4% | -12 | -0.89pp |
| Failed Verification: Declined - Call Issuer | 36 | 3.6% | 42 | 4.4% | +6 | +0.83pp |
| Failed Verification: Card Issuer Declined CVV | 37 | 3.7% | 34 | 3.5% | -3 | -0.10pp |
| Failed Verification: Issuer or Cardholder has put a restriction on the card | 36 | 3.6% | 33 | 3.4% | -3 | -0.11pp |
| Failed Verification: Cannot Authorize at this time (Policy) | 28 | 2.8% | 29 | 3.0% | +1 | +0.26pp |
| Failed Verification: Processor Declined - Fraud Suspected | 18 | 1.8% | 27 | 2.8% | +9 | +1.04pp |
| Failed Verification: Card Not Activated | 38 | 3.8% | 25 | 2.6% | -13 | -1.14pp |
| Failed Verification: Processor Declined | 20 | 2.0% | 24 | 2.5% | +4 | +0.53pp |
| **Total PVS Failures** | **1,013** | **100%** | **958** | **100%** | **-55** | - |

---
## Conclusion

The PCR decline in W14 is driven primarily by upper-funnel drop-off at payment method selection (-0.42pp) and FE validation (-0.41pp), with a notable decrease in validation recovery rate (-1.31pp). However, downstream performance remains healthy with ProcessOut_CreditCard (+3.21pp) and ApplePay (+2.28pp) showing improved success rates, and the final checkout step converting better (+0.26pp). No immediate escalation is required, but the FE validation recovery rate trend should be monitored in the coming weeks.

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
