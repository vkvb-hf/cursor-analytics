# PCR Investigation: WL 2026-W14

**Metric:** Payment Conversion Rate (PCR)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 30.03% → 29.88% (-0.15pp)  
**Volume:** ~35K payment visits

---

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined from 30.03% to 29.88% (-0.15pp) week-over-week, with payment visits decreasing by 8.1% (~3,110 fewer visits).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ≥-0.07pp | -0.26pp | ⚠️ |
| Click Submit Form | ≥-0.07pp | +0.09pp | ✅ |
| FE Validation Passed | ≥-0.07pp | +0.21pp | ✅ |
| Enter Fraud Service | ≥-0.07pp | +0.20pp | ✅ |
| Approved by Fraud Service | ≥-0.07pp | -0.11pp | ⚠️ |
| Call to PVS | ≥-0.07pp | -0.53pp | ⚠️ |
| Successful Checkout | ≥-0.07pp | +0.25pp | ✅ |

**Key Findings:**
- **Call to PVS shows significant drop (-0.53pp):** Backend data confirms a severe PVS Attempt decline (-9.71pp from 98.79% to 89.07%), indicating a critical issue between fraud approval and payment verification service calls.
- **Country KN is the primary driver:** KN experienced a -3.75pp PCR decline with Select Payment Method dropping -3.26pp, contributing most to the overall degradation.
- **Braintree_CreditCard shows notable decline:** Success rate dropped -2.58pp (90.20% → 87.62%), the largest negative change among major payment methods.
- **Braintree_Paypal also underperforming:** Success rate declined -1.73pp (92.11% → 90.38%), with increased "CVC Declined" errors (+5.58pp share) in PVS failures.
- **Positive offset from GN and ER:** Both countries improved PCR (+4.30pp and +2.04pp respectively), partially offsetting KN's decline through better Select Payment Method conversion.

**Action:** **Investigate** - Priority investigation needed for (1) the Call to PVS / PVS Attempt gap showing -9.71pp backend drop, and (2) KN market's Select Payment Method degradation (-3.26pp). Check for technical issues with PVS connectivity and any payment method availability changes in KN.

---

---

## Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 38,531 | 35,421 | -3,110 | -8.1% | - | - | - |
| Select Payment Method | 15,773 | 14,407 | -1,366 | -8.7% | 40.94% | 40.67% | -0.26pp |
| Click Submit Form | 13,947 | 12,752 | -1,195 | -8.6% | 88.42% | 88.51% | +0.09pp |
| FE Validation Passed | 13,240 | 12,132 | -1,108 | -8.4% | 94.93% | 95.14% | +0.21pp |
| Enter Fraud Service | 12,710 | 11,671 | -1,039 | -8.2% | 96.00% | 96.20% | +0.20pp |
| Approved by Fraud Service | 12,028 | 11,032 | -996 | -8.3% | 94.63% | 94.52% | -0.11pp |
| Call to PVS | 12,004 | 10,952 | -1,052 | -8.8% | 99.80% | 99.27% | -0.53pp |
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

**Include reason:** FE Validation Passed Δ Conv (+0.21pp) meets threshold (+0.07pp)

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

**Include reason:** Enter FS Δ (+0.20pp) meets threshold (+0.07pp)

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

**Include reason:** PVS Success Δ Conv (+0.25pp) meets threshold (+0.07pp)

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
## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (3 countries in WL)

| Country | Volume | PCR 2026-W13 | PCR 2026-W14 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| KN | 7,671 | 27.15% | 23.40% | -3.75pp | 1 | 2 |
| ER | 6,075 | 27.87% | 29.91% | +2.04pp | 2 | 3 |
| GN | 2,321 | 32.80% | 37.10% | +4.30pp | 3 | 1 |

---

### ER

#### Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 7,041 | 6,075 | -966 | -13.72pp | - | - | - |
| Select Payment Method | 2,919 | 2,616 | -303 | -10.38pp | 41.46% | 43.06% | +1.60pp |
| Click Submit Form | 2,509 | 2,287 | -222 | -8.85pp | 85.95% | 87.42% | +1.47pp |
| FE Validation Passed | 2,262 | 2,071 | -191 | -8.44pp | 90.16% | 90.56% | +0.40pp |
| Enter Fraud Service | 2,207 | 2,031 | -176 | -7.97pp | 97.57% | 98.07% | +0.50pp |
| Approved by Fraud Service | 2,103 | 1,937 | -166 | -7.89pp | 95.29% | 95.37% | +0.08pp |
| Call to PVS | 2,098 | 1,931 | -167 | -7.96pp | 99.76% | 99.69% | -0.07pp |
| **Successful Checkout** | 1,962 | 1,817 | -145 | -7.39pp | 93.52% | 94.10% | +0.58pp |
| **PCR Rate** | | | | | 27.87% | 29.91% | **+2.04pp** |

**Key Driver:** Select Payment Method (+1.60pp)

#### Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 8,743 | 7,976 | -767 | -8.77pp | - | - | - |
| Checkout Attempt | 2,707 | 2,496 | -211 | -7.79pp | 30.96% | 31.29% | +0.33pp |
| Enter Fraud Service | 2,706 | 2,496 | -210 | -7.76pp | 99.96% | 100.00% | +0.04pp |
| Approved by Fraud Service | 2,550 | 2,353 | -197 | -7.73pp | 94.24% | 94.27% | +0.04pp |
| PVS Attempt | 2,545 | 2,344 | -201 | -7.90pp | 99.80% | 99.62% | -0.19pp |
| PVS Success | 2,408 | 2,224 | -184 | -7.64pp | 94.62% | 94.88% | +0.26pp |
| **Successful Checkout** | 2,414 | 2,232 | -182 | -7.54pp | 100.25% | 100.36% | +0.11pp |

**Key Driver:** Checkout Attempt (+0.33pp)

---

### GN

#### Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 2,988 | 2,321 | -667 | -22.32pp | - | - | - |
| Select Payment Method | 1,682 | 1,401 | -281 | -16.71pp | 56.29% | 60.36% | +4.07pp |
| Click Submit Form | 1,480 | 1,243 | -237 | -16.01pp | 87.99% | 88.72% | +0.73pp |
| FE Validation Passed | 1,182 | 1,005 | -177 | -14.97pp | 79.86% | 80.85% | +0.99pp |
| Enter Fraud Service | 1,089 | 933 | -156 | -14.33pp | 92.13% | 92.84% | +0.70pp |
| Approved by Fraud Service | 1,027 | 888 | -139 | -13.53pp | 94.31% | 95.18% | +0.87pp |
| Call to PVS | 1,020 | 886 | -134 | -13.14pp | 99.32% | 99.77% | +0.46pp |
| **Successful Checkout** | 980 | 861 | -119 | -12.14pp | 96.08% | 97.18% | +1.10pp |
| **PCR Rate** | | | | | 32.80% | 37.10% | **+4.30pp** |

**Key Driver:** Select Payment Method (+4.07pp)

#### Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 3,823 | 3,125 | -698 | -18.26pp | - | - | - |
| Checkout Attempt | 1,446 | 1,217 | -229 | -15.84pp | 37.82% | 38.94% | +1.12pp |
| Enter Fraud Service | 1,439 | 1,212 | -227 | -15.77pp | 99.52% | 99.59% | +0.07pp |
| Approved by Fraud Service | 1,337 | 1,142 | -195 | -14.58pp | 92.91% | 94.22% | +1.31pp |
| PVS Attempt | 1,214 | 1,013 | -201 | -16.56pp | 90.80% | 88.70% | -2.10pp |
| PVS Success | 1,170 | 987 | -183 | -15.64pp | 96.38% | 97.43% | +1.06pp |
| **Successful Checkout** | 1,313 | 1,125 | -188 | -14.32pp | 112.22% | 113.98% | +1.76pp |

**Key Driver:** PVS Attempt (-2.10pp)

---

### KN

#### Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 8,310 | 7,671 | -639 | -7.69pp | - | - | - |
| Select Payment Method | 2,861 | 2,391 | -470 | -16.43pp | 34.43% | 31.17% | -3.26pp |
| Click Submit Form | 2,467 | 2,019 | -448 | -18.16pp | 86.23% | 84.44% | -1.79pp |
| FE Validation Passed | 2,531 | 2,086 | -445 | -17.58pp | 102.59% | 103.32% | +0.72pp |
| Enter Fraud Service | 2,460 | 2,016 | -444 | -18.05pp | 97.19% | 96.64% | -0.55pp |
| Approved by Fraud Service | 2,316 | 1,862 | -454 | -19.60pp | 94.15% | 92.36% | -1.79pp |
| Call to PVS | 2,319 | 1,864 | -455 | -19.62pp | 100.13% | 100.11% | -0.02pp |
| **Successful Checkout** | 2,256 | 1,795 | -461 | -20.43pp | 97.28% | 96.30% | -0.99pp |
| **PCR Rate** | | | | | 27.15% | 23.40% | **-3.75pp** |

**Key Driver:** Select Payment Method (-3.26pp)

#### Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 10,002 | 9,345 | -657 | -6.57pp | - | - | - |
| Checkout Attempt | 2,809 | 2,357 | -452 | -16.09pp | 28.08% | 25.22% | -2.86pp |
| Enter Fraud Service | 2,786 | 2,327 | -459 | -16.48pp | 99.18% | 98.73% | -0.45pp |
| Approved by Fraud Service | 2,590 | 2,101 | -489 | -18.88pp | 92.96% | 90.29% | -2.68pp |
| PVS Attempt | 2,592 | 2,100 | -492 | -18.98pp | 100.08% | 99.95% | -0.12pp |
| PVS Success | 2,557 | 2,068 | -489 | -19.12pp | 98.65% | 98.48% | -0.17pp |
| **Successful Checkout** | 2,557 | 2,070 | -487 | -19.05pp | 100.00% | 100.10% | +0.10pp |

**Key Driver:** Checkout Attempt (-2.86pp)

---

## Conclusion

The -0.15pp PCR decline is primarily driven by two issues: a significant backend gap between fraud approval and PVS attempt (-9.71pp), and poor performance in the KN market where Select Payment Method conversion dropped -3.26pp. While improvements in GN (+4.30pp) and ER (+2.04pp) provided partial offset, the PVS connectivity issue requires immediate technical investigation as it represents a systemic problem affecting checkout completion across all markets.

---

## SQL Queries

<details>
<summary>Waterfall GA (cluster/country)</summary>

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
<summary>Backend Combined (cluster/country)</summary>

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
<summary>Country PCR Summary</summary>

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
