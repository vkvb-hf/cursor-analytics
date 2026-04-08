# PCR Investigation: US-HF 2026-W14

**Metric:** Payment Conversion Rate (PCR)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 26.77% → 26.41% (-0.37pp)  
**Volume:** ~44K payment visits

---

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate (PCR) for US-HF declined by -0.37pp week-over-week (26.77% → 26.41%) on approximately 44K payment visits.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Entry rate | -0.42pp | ⚠️ |
| Click Submit Form | Form engagement | +0.02pp | ✅ |
| FE Validation Passed | Validation | -0.41pp | ⚠️ |
| Enter Fraud Service | Fraud routing | +0.12pp | ✅ |
| Approved by Fraud Service | Fraud approval | -0.00pp | ✅ |
| Call to PVS | PVS routing | -0.24pp | ⚠️ |
| Successful Checkout | Final conversion | +0.26pp | ✅ |

**Key Findings:**
- **Select Payment Method is the primary driver** of the PCR decline, with conversion dropping -0.42pp (37.60% → 37.18%), indicating fewer visitors are initiating the payment process
- **FE Validation recovery rate decreased by -1.31pp** (75.67% → 74.36%), with "terms_not_accepted" remaining the dominant error type at 51.6% of errors
- **Backend data shows a significant -0.99pp drop in Checkout Attempt rate** (36.46% → 35.46%), corroborating the top-of-funnel issue
- **ProcessOut_CreditCard and Braintree_ApplePay both improved** their success rates (+3.21pp and +2.28pp respectively), partially offsetting upstream losses
- **Fraud Service approval improved significantly in backend data** (+2.75pp), and PVS failures decreased by 55 cases week-over-week

**Action:** **Investigate** - The consistent decline at the Select Payment Method step across both GA and Backend waterfalls suggests a user experience or technical issue at the payment method selection stage. Recommend reviewing any recent UI/UX changes, page load performance, and A/B test exposure during W14.

---

---

## Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 44,370 | 44,056 | -314 | -0.7% | - | - | - |
| Select Payment Method | 16,684 | 16,381 | -303 | -1.8% | 37.60% | 37.18% | -0.42pp |
| Click Submit Form | 14,732 | 14,468 | -264 | -1.8% | 88.30% | 88.32% | +0.02pp |
| FE Validation Passed | 13,994 | 13,684 | -310 | -2.2% | 94.99% | 94.58% | -0.41pp |
| Enter Fraud Service | 13,714 | 13,426 | -288 | -2.1% | 98.00% | 98.11% | +0.12pp |
| Approved by Fraud Service | 12,848 | 12,578 | -270 | -2.1% | 93.69% | 93.68% | -0.00pp |
| Call to PVS | 12,852 | 12,552 | -300 | -2.3% | 100.03% | 99.79% | -0.24pp |
| **Successful Checkout** | 11,879 | 11,634 | -245 | -2.1% | 92.43% | 92.69% | +0.26pp |
| **PCR Rate** | | | | | 26.77% | 26.41% | **-0.37pp** |

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

**Include reason:** FE Validation Passed Δ Conv (-0.41pp) meets threshold (+0.18pp)

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

**Include reason:** PVS Success Δ Conv (+0.26pp) meets threshold (+0.18pp)

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
## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (1 countries in US-HF)

| Country | Volume | PCR 2026-W13 | PCR 2026-W14 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| US | 44,056 | 26.77% | 26.41% | -0.36pp | 1 | 1 |

---

### US

#### Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 44,370 | 44,056 | -314 | -0.71pp | - | - | - |
| Select Payment Method | 16,684 | 16,381 | -303 | -1.82pp | 37.60% | 37.18% | -0.42pp |
| Click Submit Form | 14,732 | 14,468 | -264 | -1.79pp | 88.30% | 88.32% | +0.02pp |
| FE Validation Passed | 13,994 | 13,684 | -310 | -2.22pp | 94.99% | 94.58% | -0.41pp |
| Enter Fraud Service | 13,714 | 13,426 | -288 | -2.10pp | 98.00% | 98.11% | +0.12pp |
| Approved by Fraud Service | 12,848 | 12,578 | -270 | -2.10pp | 93.69% | 93.68% | -0.00pp |
| Call to PVS | 12,852 | 12,552 | -300 | -2.33pp | 100.03% | 99.79% | -0.24pp |
| **Successful Checkout** | 11,879 | 11,634 | -245 | -2.06pp | 92.43% | 92.69% | +0.26pp |
| **PCR Rate** | | | | | 26.77% | 26.41% | **-0.37pp** |

**Key Driver:** Select Payment Method (-0.42pp)

#### Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 48,829 | 47,792 | -1,037 | -2.12pp | - | - | - |
| Checkout Attempt | 17,802 | 16,949 | -853 | -4.79pp | 36.46% | 35.46% | -0.99pp |
| Enter Fraud Service | 17,647 | 16,671 | -976 | -5.53pp | 99.13% | 98.36% | -0.77pp |
| Approved by Fraud Service | 15,733 | 15,322 | -411 | -2.61pp | 89.15% | 91.91% | +2.75pp |
| PVS Attempt | 15,361 | 14,911 | -450 | -2.93pp | 97.64% | 97.32% | -0.32pp |
| PVS Success | 14,219 | 13,845 | -374 | -2.63pp | 92.57% | 92.85% | +0.29pp |
| **Successful Checkout** | 14,691 | 14,421 | -270 | -1.84pp | 103.32% | 104.16% | +0.84pp |

**Key Driver:** Approved by Fraud Service (+2.75pp)

---

## Conclusion

The -0.37pp PCR decline in US-HF for 2026-W14 is primarily driven by reduced conversion at the payment method selection stage (-0.42pp) and decreased FE validation recovery rates (-1.31pp). While downstream metrics including payment method success rates and PVS performance showed improvement, these gains were insufficient to offset the top-of-funnel losses. Investigation should focus on identifying any changes to the payment selection experience or technical issues that may be preventing users from initiating checkout.

---

## SQL Queries

<details>
<summary>Waterfall GA (cluster/country)</summary>

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
<summary>Backend Combined (cluster/country)</summary>

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
<summary>Country PCR Summary</summary>

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
),
base_data AS (
  SELECT
    d.iso_year_week AS hellofresh_week,
    f.country,
    SUM(is_pay_visit) AS payment_visits,
    SUM(is_success) AS successful_checkout
  FROM spark_catalog.payments_hf.fact_payment_conversion_rate f
  JOIN dimensions.date_dimension d ON f.date_string_backwards = d.date_string_backwards
  CROSS JOIN weeks w
  WHERE d.iso_year_week IN (w.affected_week, w.prev_week)
    AND f.country IN (SELECT country FROM countries)
  GROUP BY 1, 2
),
with_pcr AS (
  SELECT
    hellofresh_week,
    country,
    payment_visits,
    successful_checkout,
    ROUND(successful_checkout * 100.0 / NULLIF(payment_visits, 0), 2) AS pcr
  FROM base_data
),
with_delta AS (
  SELECT
    curr.country,
    curr.payment_visits AS curr_volume,
    prev.payment_visits AS prev_volume,
    curr.pcr AS curr_pcr,
    prev.pcr AS prev_pcr,
    ROUND(curr.pcr - prev.pcr, 2) AS delta_pcr_pp,
    ABS(curr.pcr - prev.pcr) AS abs_delta_pcr,
    curr.payment_visits * ABS(curr.pcr - prev.pcr) AS contribution
  FROM with_pcr curr
  CROSS JOIN weeks w
  JOIN with_pcr prev ON curr.country = prev.country 
    AND curr.hellofresh_week = w.affected_week 
    AND prev.hellofresh_week = w.prev_week
),
ranked AS (
  SELECT
    country,
    prev_volume,
    curr_volume,
    prev_pcr,
    curr_pcr,
    delta_pcr_pp,
    contribution,
    ROW_NUMBER() OVER (ORDER BY contribution DESC) AS rank_contribution,
    ROW_NUMBER() OVER (ORDER BY abs_delta_pcr DESC) AS rank_change
  FROM with_delta
)
SELECT
  country,
  prev_volume,
  curr_volume,
  prev_pcr,
  curr_pcr,
  delta_pcr_pp,
  rank_contribution,
  rank_change
FROM ranked
ORDER BY rank_contribution

```

</details>

<details>
<summary>FE Validation Recovery Rate</summary>

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
