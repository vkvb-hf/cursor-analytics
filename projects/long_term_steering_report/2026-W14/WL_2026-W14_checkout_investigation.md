# PCR Investigation: WL 2026-W14

**Metric:** Payment Conversion Rate (PCR)  
**Period:** 2026-W13 → 2026-W14  
**Observation:**  
GA: 30.03% → 29.88% (-0.15pp, -0.5% change)  
Backend: 29.06% → 28.33% (-0.73pp, -2.5% change)  
**Volume:** ~35K payment visits

---

## Executive Summary

## Executive Summary

**Overall:** PCR declined in W14, with GA showing a minor drop of -0.15pp (30.03% → 29.88%) while Backend experienced a more significant decline of -0.73pp (29.06% → 28.33%) on ~35K payment visits.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | GA entry rate | -0.26pp | ⚠️ |
| Click Submit Form | Form submission | +0.09pp | ✅ |
| FE Validation Passed | Client validation | +0.21pp | ✅ |
| Enter Fraud Service | Fraud check entry | +0.21pp | ✅ |
| Approved by Fraud Service | Fraud approval | -0.11pp | ✅ |
| Call to PVS | PVS routing | -0.52pp | ⚠️ |
| PVS Attempt (Backend) | PVS attempt rate | -9.71pp | ⚠️ |
| PVS Success | Payment verification | -0.05pp | ✅ |
| Successful Checkout | Final conversion | +0.25pp | ✅ |

**Key Findings:**
- **Critical Backend Issue:** PVS Attempt rate dropped significantly by -9.71pp (98.79% → 89.07%), indicating a major gap between fraud approval and payment verification attempts
- **Braintree_CreditCard degradation:** Success rate declined -2.58pp (90.20% → 87.62%), the largest drop among high-volume payment methods
- **Braintree_Paypal decline:** Conversion dropped -1.73pp (92.11% → 90.38%) with increased "Funding Instrument Declined" errors
- **CVC-related failures increased:** "Failed Verification: Refused(CVC Declined)" errors jumped from 10 to 21 (+11), suggesting potential card validation issues
- **Volume decline:** Overall payment visits dropped -8.1% (38,531 → 35,420), reducing the absolute impact of rate changes

**Action:** **Investigate** — The -9.71pp drop in Backend PVS Attempt rate requires immediate investigation to identify why approved fraud checks are not proceeding to payment verification. Additionally, review Braintree_CreditCard processor performance and the spike in CVC decline errors.

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
| **Successful Checkout** | 13,390 | 12,368 | -1,022 | -7.6% | 101.39% | 112.08% | +10.69pp |
| **PCR Rate** | | | | | 29.06% | 28.33% | **-0.73pp** |

---

## Payment Method Breakdown

| Payment Method | 2026-W13 Attempt | 2026-W13 Success | 2026-W13 Rate | 2026-W14 Attempt | 2026-W14 Success | 2026-W14 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 4,073 | 3,675 | 90.23% | 3,917 | 3,516 | 89.76% | -0.47pp |
| Braintree_ApplePay | 4,162 | 3,839 | 92.24% | 3,733 | 3,417 | 91.53% | -0.70pp |
| Adyen_CreditCard | 2,682 | 2,377 | 88.63% | 2,796 | 2,510 | 89.77% | +1.14pp |
| Braintree_Paypal | 1,850 | 1,704 | 92.11% | 1,663 | 1,503 | 90.38% | -1.73pp |
| Braintree_CreditCard | 1,602 | 1,445 | 90.20% | 1,317 | 1,154 | 87.62% | -2.58pp |
| ProcessOut_ApplePay | 411 | 349 | 84.91% | 283 | 265 | 93.64% | +8.72pp |
|  | 0 | 0 | 0.00% | 2 | 2 | 100.00% | +100.00pp |
| Braintree_Venmo | 1 | 1 | 100.00% | 1 | 1 | 100.00% | +0.00pp |
| NoPayment | 1 | 0 | 0.00% | 1 | 0 | 0.00% | +0.00pp |
| CreditCard | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |

---

## FE Validation Errors

*Included because FE Validation Passed Δ Conv (+0.21pp) meets threshold (+0.07pp)*

| Error Type | 2026-W13 | 2026-W14 | Δ |
| ---------- | ----------- | --------------- | - |
| APPLEPAY_DISMISSED | 1,409 | 1,217 | -192 |
| terms_not_accepted | 808 | 751 | -57 |
| PAYPAL_POPUP_CLOSED | 283 | 263 | -20 |
| CC_TOKENISE_ERR | 40 | 30 | -10 |
| PAYPAL_TOKENISE_ERR | 32 | 27 | -5 |
| VENMO_TOKENISE_ERR | 0 | 1 | +1 |

---

## Fraud Analysis

*Included because Enter FS Δ (+0.21pp) meets threshold (+0.07pp)*

**Gap (Checkout Attempt → Enter Fraud Service):**

| Week | Checkout Attempt | Enter FS | Gap | Gap % |
| ---- | ---------------- | -------- | --- | ----- |
| 2026-W13 | 14,782 | 14,732 | 50 | 0.34% |
| 2026-W14 | 13,713 | 13,666 | 47 | 0.34% |
| **Δ** | -1,069 | -1,066 | -3 | +0.00pp |


---

## Payment Verification Errors

*Included because PVS Success Δ Conv (+0.25pp) meets threshold (+0.07pp)*

| Decline Reason | 2026-W13 | 2026-W14 | Δ |
| -------------- | ----------- | --------------- | - |
| Failed Verification: Insufficient Funds | 62 | 42 | -20 |
| Blocked Verification: Payment method is blocked due to business reasons | 38 | 40 | +2 |
| Failed Verification: Refused(CVC Declined) | 10 | 21 | +11 |
| Failed Verification: Card Issuer Declined CVV | 25 | 21 | -4 |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 29 | 20 | -9 |
| Failed Verification: Refused(FRAUD) | 20 | 16 | -4 |
| Failed Verification: Cannot Authorize at this time (Policy) | 14 | 16 | +2 |
| Failed Verification: Declined - Call Issuer | 12 | 15 | +3 |
| Failed Verification: Processor Declined | 12 | 14 | +2 |
| Failed Verification: Refused(Refused) | 14 | 9 | -5 |

---
## Conclusion

The PCR decline in W14 is primarily driven by a significant Backend issue where the PVS Attempt rate dropped by 9.71pp, indicating a substantial number of transactions are failing to reach payment verification after fraud approval. While the GA funnel shows relatively stable performance with only minor drops at entry (-0.26pp) and PVS routing (-0.52pp), the Backend data reveals a systemic issue that warrants immediate technical investigation. The combination of this routing gap and payment method-specific declines (particularly Braintree_CreditCard at -2.58pp) suggests both infrastructure and processor-level issues need to be addressed.

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
