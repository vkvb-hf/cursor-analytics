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

**Overall:** PCR declined in W14, with GA showing -0.15pp (29.88%) and Backend showing -0.73pp (28.33%), on reduced volume of ~35K payment visits (-8.1% WoW).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Threshold ±0.07pp | -0.26pp | ⚠️ |
| Click Submit Form | Threshold ±0.07pp | +0.09pp | ⚠️ |
| FE Validation Passed | Threshold ±0.07pp | +0.21pp | ✅ |
| Enter Fraud Service | Threshold ±0.07pp | +0.21pp | ✅ |
| Approved by Fraud Service | Threshold ±0.07pp | -0.11pp | ⚠️ |
| Call to PVS | Threshold ±0.07pp | -0.52pp | ⚠️ |
| Successful Checkout | Threshold ±0.07pp | +0.25pp | ✅ |

**Key Findings:**
- **Call to PVS drop (-0.52pp):** The largest GA funnel degradation occurred between Fraud Approval and PVS call, with Backend showing a severe -9.71pp drop in PVS Attempt rate (98.79% → 89.07%), indicating a potential system issue routing approved transactions to payment verification.
- **Braintree_CreditCard underperformance:** Success rate dropped -2.58pp (90.20% → 87.62%), the worst decline among major payment methods.
- **Braintree_Paypal decline:** Success rate fell -1.73pp (92.11% → 90.38%), with PayPal-related FE errors (PAYPAL_POPUP_CLOSED) increasing slightly (+0.63pp share).
- **CVC-related PVS failures increased:** "Refused(CVC Declined)" errors rose from 10 to 21 cases (+5.58pp share), suggesting potential card validation issues.
- **Volume decline across all steps:** Payment visits dropped -8.1% WoW, though conversion rates within most steps remained stable or improved slightly.

**Action:** **Investigate** - The significant gap between Backend Fraud Approval and PVS Attempt (-9.71pp) requires immediate technical investigation to identify why approved transactions are not reaching payment verification. Additionally, review Braintree_CreditCard processor performance and the increase in CVC decline errors.

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

### Recovery Rate

| Metric | 2026-W13 | 2026-W14 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 2,068 | 1,837 | -231 |
| Error → Passed | 1,209 | 1,079 | -130 |
| **Recovery Rate** | **58.46%** | **58.74%** | **+0.27pp** |

*Recovery Rate = Customers who had error but still passed / Customers with FE Error*

### Error Type Distribution

| Error Type | 2026-W13 | 2026-W13 % | 2026-W14 | 2026-W14 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 1,409 | 68.1% | 1,217 | 66.2% | -1.88pp |
| terms_not_accepted | 808 | 39.1% | 751 | 40.9% | +1.81pp |
| PAYPAL_POPUP_CLOSED | 283 | 13.7% | 263 | 14.3% | +0.63pp |
| CC_TOKENISE_ERR | 40 | 1.9% | 30 | 1.6% | -0.30pp |
| PAYPAL_TOKENISE_ERR | 32 | 1.5% | 27 | 1.5% | -0.08pp |
| VENMO_TOKENISE_ERR | 0 | 0.0% | 1 | 0.1% | +0.05pp |

*% of Errors = Error Type Count / Customers with FE Error (can exceed 100% as customers may have multiple error types)*

---

## Fraud Analysis

*Included because Enter FS Δ (+0.21pp) meets threshold (+0.07pp)*

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W13 | 2026-W13 % | 2026-W14 | 2026-W14 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 14,782 | - | 13,713 | - | -1,069 | -7.2% |
| Enter Fraud Service | 14,732 | - | 13,666 | - | -1,066 | -7.2% |
| **Gap (Skipped)** | **50** | **0.34%** | **47** | **0.34%** | **-3** | **+0.00pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W13 Gap | 2026-W13 % | 2026-W14 Gap | 2026-W14 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Braintree_CreditCard | 16 | 32.7% | 19 | 41.3% | +3 | +8.65pp |
| Braintree_ApplePay | 8 | 16.3% | 9 | 19.6% | +1 | +3.24pp |
| Adyen_CreditCard | 8 | 16.3% | 7 | 15.2% | -1 | -1.11pp |
| Braintree_Paypal | 10 | 20.4% | 6 | 13.0% | -4 | -7.36pp |
| ProcessOut_CreditCard | 7 | 14.3% | 5 | 10.9% | -2 | -3.42pp |
| **Total** | **49** | **100%** | **46** | **100%** | **-3** | - |

*% of Gap = Payment Method Gap / Total Gap*

---

## Payment Verification Errors

*Included because PVS Success Δ Conv (+0.25pp) meets threshold (+0.07pp)*

| Decline Reason | 2026-W13 | 2026-W13 % | 2026-W14 | 2026-W14 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Failed Verification: Insufficient Funds | 62 | 26.3% | 42 | 19.6% | -20 | -6.65pp |
| Blocked Verification: Payment method is blocked due to business reasons | 38 | 16.1% | 40 | 18.7% | +2 | +2.59pp |
| Failed Verification: Refused(CVC Declined) | 10 | 4.2% | 21 | 9.8% | +11 | +5.58pp |
| Failed Verification: Card Issuer Declined CVV | 25 | 10.6% | 21 | 9.8% | -4 | -0.78pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 29 | 12.3% | 20 | 9.3% | -9 | -2.94pp |
| Failed Verification: Refused(FRAUD) | 20 | 8.5% | 16 | 7.5% | -4 | -1.00pp |
| Failed Verification: Cannot Authorize at this time (Policy) | 14 | 5.9% | 16 | 7.5% | +2 | +1.54pp |
| Failed Verification: Declined - Call Issuer | 12 | 5.1% | 15 | 7.0% | +3 | +1.92pp |
| Failed Verification: Processor Declined | 12 | 5.1% | 14 | 6.5% | +2 | +1.46pp |
| Failed Verification: Refused(Refused) | 14 | 5.9% | 9 | 4.2% | -5 | -1.73pp |
| **Total PVS Failures** | **236** | **100%** | **214** | **100%** | **-22** | - |

---
## Conclusion

The W14 PCR decline is primarily driven by a significant Backend funnel gap between Fraud Service approval and PVS attempt, where conversion dropped -9.71pp, suggesting a technical routing issue that prevented approved transactions from proceeding to payment verification. While GA-level step conversions show relatively minor fluctuations, the Backend data reveals the core problem requiring engineering investigation. Secondary concerns include degraded performance on Braintree_CreditCard (-2.58pp) and increased CVC-related payment verification failures.

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
<summary>FE Recovery Rate</summary>

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
