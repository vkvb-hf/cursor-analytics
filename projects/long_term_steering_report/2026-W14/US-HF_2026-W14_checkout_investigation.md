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

**Overall:** PCR declined modestly in 2026-W14, with GA showing -0.37pp (26.77% → 26.40%) and Backend showing -0.09pp (28.36% → 28.28%) on ~44K payment visits.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | GA entry rate | -0.42pp | ⚠️ |
| Click Submit Form | Click-through | +0.02pp | ✅ |
| FE Validation Passed | Validation rate | -0.41pp | ⚠️ |
| Enter Fraud Service | Handoff rate | +0.11pp | ✅ |
| Approved by Fraud Service | Approval rate | -0.00pp | ✅ |
| Call to PVS | PVS call rate | -0.23pp | ⚠️ |
| Successful Checkout | Final conversion | +0.26pp | ✅ |
| Backend: Checkout Attempt | Entry rate | -0.99pp | ⚠️ |
| Backend: Fraud Approval | Approval rate | +2.75pp | ✅ |

**Key Findings:**
- **Top-of-funnel weakness:** Select Payment Method conversion dropped -0.42pp (37.60% → 37.18%), contributing most to the GA PCR decline
- **FE Validation errors improved:** Despite -0.41pp conversion drop, "terms_not_accepted" errors decreased significantly (-230), suggesting the issue may be volume-related rather than error-driven
- **Payment method performance improved:** ProcessOut_CreditCard success rate increased +3.21pp (79.29% → 82.50%) and Braintree_ApplePay improved +2.28pp (75.72% → 78.00%)
- **Backend fraud approval strengthened:** +2.75pp improvement (89.15% → 91.91%) indicates healthier traffic quality or improved fraud model performance
- **PVS errors declined:** Most decline reasons showed decreases, including "Blocked Verification" (-36) and "Insufficient Funds" (-8), though "Fraud Suspected" increased (+9)

**Action:** **Monitor** — The decline is minor (-0.37pp GA) and partially offset by improvements in payment method success rates and fraud approval. No escalation needed unless the top-of-funnel drop persists in W15.

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

| Error Type | 2026-W13 | 2026-W14 | Δ |
| ---------- | ----------- | --------------- | - |
| terms_not_accepted | 2,064 | 1,834 | -230 |
| APPLEPAY_DISMISSED | 1,840 | 1,805 | -35 |
| PAYPAL_POPUP_CLOSED | 273 | 254 | -19 |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 235 | 223 | -12 |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 102 | 113 | +11 |
| CC_TOKENISE_ERR | 102 | 108 | +6 |
| PAYPAL_TOKENISE_ERR | 24 | 23 | -1 |
| CC_NO_PREPAID_ERR | 2 | 2 | 0 |
| EXPRESS_CHECKOUT_APPLEPAY_TOKENISE_ERR | 0 | 1 | +1 |

---

## Payment Verification Errors

*Included because PVS Success Δ Conv (+0.26pp) meets threshold (+0.18pp)*

| Decline Reason | 2026-W13 | 2026-W14 | Δ |
| -------------- | ----------- | --------------- | - |
| Blocked Verification: Payment method is blocked due to business reasons | 570 | 534 | -36 |
| Failed Verification: Insufficient Funds | 166 | 158 | -8 |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 64 | 52 | -12 |
| Failed Verification: Declined - Call Issuer | 36 | 42 | +6 |
| Failed Verification: Card Issuer Declined CVV | 37 | 34 | -3 |
| Failed Verification: Issuer or Cardholder has put a restriction on the card | 36 | 33 | -3 |
| Failed Verification: Cannot Authorize at this time (Policy) | 28 | 29 | +1 |
| Failed Verification: Processor Declined - Fraud Suspected | 18 | 27 | +9 |
| Failed Verification: Card Not Activated | 38 | 25 | -13 |
| Failed Verification: Processor Declined | 20 | 24 | +4 |

---
## Conclusion

The PCR decline in 2026-W14 was driven primarily by reduced top-of-funnel engagement (Select Payment Method -0.42pp) and FE validation pass rate (-0.41pp), while downstream metrics showed stability or improvement. Payment processor performance was notably stronger, with ProcessOut_CreditCard and ApplePay both showing meaningful gains. Given the modest overall impact and positive signals in conversion quality metrics, continued monitoring is recommended with attention to whether the top-of-funnel softness persists.

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
