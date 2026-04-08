# PCR Investigation: HF-INTL 2026-W14

**Metric:** Payment Conversion Rate (PCR)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 34.88% → 36.04% (+1.16pp)  
**Volume:** ~62K payment visits

---

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate (PCR) for HF-INTL improved from 34.88% to 36.04% (+1.16pp) in 2026-W14, driven by broad improvements across most funnel steps despite a 23.9% decrease in payment visit volume.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ≥0pp | +0.42pp | ✅ |
| Click Submit Form | ≥0pp | +0.59pp | ✅ |
| FE Validation Passed | ≥0pp | +0.68pp | ✅ |
| Enter Fraud Service | ≥0pp | +0.40pp | ✅ |
| Approved by Fraud Service | ≥0pp | -0.23pp | ⚠️ |
| Call to PVS | ≥0pp | -0.01pp | ⚠️ |
| Successful Checkout | ≥0pp | +0.85pp | ✅ |

**Key Findings:**
- **France drove the largest contribution** to PCR improvement (+3.10pp), with Select Payment Method conversion increasing by +2.98pp in GA waterfall
- **FE Validation recovery rate improved** from 56.10% to 57.57% (+1.47pp), with APPLEPAY_DISMISSED remaining the dominant error type (76.8% of errors)
- **PVS Success rate improved significantly** (+0.85pp in GA), with "Failed Verification: Insufficient Funds" declining from 17.3% to 13.0% of PVS failures (-4.31pp share)
- **Braintree_ApplePay showed notable improvement** (+1.70pp success rate), while ProcessOut_ApplePay declined (-1.20pp)
- **Fraud Service approval rate slightly declined** (-0.23pp in GA, -0.43pp in Backend), representing the only meaningful negative trend in the funnel

**Action:** Monitor - The overall improvement is positive and broad-based. Continue monitoring Fraud Service approval rates and ProcessOut_ApplePay performance for potential degradation trends.

---

---

## Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 82,373 | 62,654 | -19,719 | -23.9% | - | - | - |
| Select Payment Method | 45,198 | 34,643 | -10,555 | -23.4% | 54.87% | 55.29% | +0.42pp |
| Click Submit Form | 36,437 | 28,132 | -8,305 | -22.8% | 80.62% | 81.21% | +0.59pp |
| FE Validation Passed | 33,860 | 26,334 | -7,526 | -22.2% | 92.93% | 93.61% | +0.68pp |
| Enter Fraud Service | 32,610 | 25,466 | -7,144 | -21.9% | 96.31% | 96.70% | +0.40pp |
| Approved by Fraud Service | 30,635 | 23,864 | -6,771 | -22.1% | 93.94% | 93.71% | -0.23pp |
| Call to PVS | 30,583 | 23,821 | -6,762 | -22.1% | 99.83% | 99.82% | -0.01pp |
| **Successful Checkout** | 28,731 | 22,581 | -6,150 | -21.4% | 93.94% | 94.79% | +0.85pp |
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

**Include reason:** FE Validation Passed Δ Conv (+0.68pp) meets threshold (+0.58pp)

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

**Include reason:** PVS Success Δ Conv (+0.85pp) meets threshold (+0.58pp)

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
## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (4 countries in HF-INTL)

| Country | Volume | PCR 2026-W13 | PCR 2026-W14 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| FR | 16,752 | 29.08% | 32.18% | +3.10pp | 1 | 3 |
| AU | 6,338 | 34.87% | 36.48% | +1.61pp | 2 | 6 |
| DK | 1,407 | 42.72% | 48.61% | +5.89pp | 4 | 2 |
| LU | 59 | 49.41% | 57.63% | +8.22pp | 12 | 1 |

---

### FR

#### Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 21,892 | 16,752 | -5,140 | -23.48pp | - | - | - |
| Select Payment Method | 10,249 | 8,342 | -1,907 | -18.61pp | 46.82% | 49.80% | +2.98pp |
| Click Submit Form | 8,054 | 6,662 | -1,392 | -17.28pp | 78.58% | 79.86% | +1.28pp |
| FE Validation Passed | 7,496 | 6,272 | -1,224 | -16.33pp | 93.07% | 94.15% | +1.07pp |
| Enter Fraud Service | 7,205 | 6,071 | -1,134 | -15.74pp | 96.12% | 96.80% | +0.68pp |
| Approved by Fraud Service | 6,576 | 5,532 | -1,044 | -15.88pp | 91.27% | 91.12% | -0.15pp |
| Call to PVS | 6,582 | 5,544 | -1,038 | -15.77pp | 100.09% | 100.22% | +0.13pp |
| **Successful Checkout** | 6,367 | 5,391 | -976 | -15.33pp | 96.73% | 97.24% | +0.51pp |
| **PCR Rate** | | | | | 29.08% | 32.18% | **+3.10pp** |

**Key Driver:** Select Payment Method (+2.98pp)

#### Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 29,173 | 22,499 | -6,674 | -22.88pp | - | - | - |
| Checkout Attempt | 10,942 | 9,288 | -1,654 | -15.12pp | 37.51% | 41.28% | +3.77pp |
| Enter Fraud Service | 10,913 | 9,274 | -1,639 | -15.02pp | 99.73% | 99.85% | +0.11pp |
| Approved by Fraud Service | 9,699 | 8,163 | -1,536 | -15.84pp | 88.88% | 88.02% | -0.86pp |
| PVS Attempt | 9,691 | 8,159 | -1,532 | -15.81pp | 99.92% | 99.95% | +0.03pp |
| PVS Success | 9,459 | 8,029 | -1,430 | -15.12pp | 97.61% | 98.41% | +0.80pp |
| **Successful Checkout** | 9,497 | 8,058 | -1,439 | -15.15pp | 100.40% | 100.36% | -0.04pp |

**Key Driver:** Checkout Attempt (+3.77pp)

---

### AU

#### Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 8,615 | 6,338 | -2,277 | -26.43pp | - | - | - |
| Select Payment Method | 4,489 | 3,376 | -1,113 | -24.79pp | 52.11% | 53.27% | +1.16pp |
| Click Submit Form | 3,772 | 2,841 | -931 | -24.68pp | 84.03% | 84.15% | +0.13pp |
| FE Validation Passed | 3,402 | 2,603 | -799 | -23.49pp | 90.19% | 91.62% | +1.43pp |
| Enter Fraud Service | 3,300 | 2,534 | -766 | -23.21pp | 97.00% | 97.35% | +0.35pp |
| Approved by Fraud Service | 3,099 | 2,388 | -711 | -22.94pp | 93.91% | 94.24% | +0.33pp |
| Call to PVS | 3,094 | 2,377 | -717 | -23.17pp | 99.84% | 99.54% | -0.30pp |
| **Successful Checkout** | 3,004 | 2,312 | -692 | -23.04pp | 97.09% | 97.27% | +0.17pp |
| **PCR Rate** | | | | | 34.87% | 36.48% | **+1.61pp** |

**Key Driver:** FE Validation Passed (+1.43pp)

#### Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 9,530 | 7,185 | -2,345 | -24.61pp | - | - | - |
| Checkout Attempt | 3,886 | 3,029 | -857 | -22.05pp | 40.78% | 42.16% | +1.38pp |
| Enter Fraud Service | 3,864 | 3,015 | -849 | -21.97pp | 99.43% | 99.54% | +0.10pp |
| Approved by Fraud Service | 3,573 | 2,794 | -779 | -21.80pp | 92.47% | 92.67% | +0.20pp |
| PVS Attempt | 3,140 | 2,464 | -676 | -21.53pp | 87.88% | 88.19% | +0.31pp |
| PVS Success | 3,062 | 2,401 | -661 | -21.59pp | 97.52% | 97.44% | -0.07pp |
| **Successful Checkout** | 3,498 | 2,725 | -773 | -22.10pp | 114.24% | 113.49% | -0.74pp |

**Key Driver:** Checkout Attempt (+1.38pp)

---

### LU

#### Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 85 | 59 | -26 | -30.59pp | - | - | - |
| Select Payment Method | 53 | 40 | -13 | -24.53pp | 62.35% | 67.80% | +5.44pp |
| Click Submit Form | 51 | 37 | -14 | -27.45pp | 96.23% | 92.50% | -3.73pp |
| FE Validation Passed | 48 | 35 | -13 | -27.08pp | 94.12% | 94.59% | +0.48pp |
| Enter Fraud Service | 45 | 35 | -10 | -22.22pp | 93.75% | 100.00% | +6.25pp |
| Approved by Fraud Service | 45 | 35 | -10 | -22.22pp | 100.00% | 100.00% | +0.00pp |
| Call to PVS | 44 | 35 | -9 | -20.45pp | 97.78% | 100.00% | +2.22pp |
| **Successful Checkout** | 42 | 34 | -8 | -19.05pp | 95.45% | 97.14% | +1.69pp |
| **PCR Rate** | | | | | 49.41% | 57.63% | **+8.22pp** |

**Key Driver:** Enter Fraud Service (+6.25pp)

#### Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 282 | 256 | -26 | -9.22pp | - | - | - |
| Checkout Attempt | 86 | 75 | -11 | -12.79pp | 30.50% | 29.30% | -1.20pp |
| Enter Fraud Service | 65 | 62 | -3 | -4.62pp | 75.58% | 82.67% | +7.09pp |
| Approved by Fraud Service | 65 | 62 | -3 | -4.62pp | 100.00% | 100.00% | +0.00pp |
| PVS Attempt | 64 | 61 | -3 | -4.69pp | 98.46% | 98.39% | -0.07pp |
| PVS Success | 62 | 60 | -2 | -3.23pp | 96.88% | 98.36% | +1.49pp |
| **Successful Checkout** | 81 | 73 | -8 | -9.88pp | 130.65% | 121.67% | -8.98pp |

**Key Driver:** Successful Checkout (-8.98pp)

---

### DK

#### Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 1,573 | 1,407 | -166 | -10.55pp | - | - | - |
| Select Payment Method | 1,002 | 955 | -47 | -4.69pp | 63.70% | 67.87% | +4.17pp |
| Click Submit Form | 848 | 820 | -28 | -3.30pp | 84.63% | 85.86% | +1.23pp |
| FE Validation Passed | 791 | 778 | -13 | -1.64pp | 93.28% | 94.88% | +1.60pp |
| Enter Fraud Service | 768 | 759 | -9 | -1.17pp | 97.09% | 97.56% | +0.47pp |
| Approved by Fraud Service | 698 | 695 | -3 | -0.43pp | 90.89% | 91.57% | +0.68pp |
| Call to PVS | 694 | 695 | +1 | +0.14pp | 99.43% | 100.00% | +0.57pp |
| **Successful Checkout** | 672 | 684 | +12 | +1.79pp | 96.83% | 98.42% | +1.59pp |
| **PCR Rate** | | | | | 42.72% | 48.61% | **+5.89pp** |

**Key Driver:** Select Payment Method (+4.17pp)

#### Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 2,170 | 1,976 | -194 | -8.94pp | - | - | - |
| Checkout Attempt | 1,115 | 1,111 | -4 | -0.36pp | 51.38% | 56.22% | +4.84pp |
| Enter Fraud Service | 1,106 | 1,107 | +1 | +0.09pp | 99.19% | 99.64% | +0.45pp |
| Approved by Fraud Service | 991 | 984 | -7 | -0.71pp | 89.60% | 88.89% | -0.71pp |
| PVS Attempt | 961 | 966 | +5 | +0.52pp | 96.97% | 98.17% | +1.20pp |
| PVS Success | 944 | 957 | +13 | +1.38pp | 98.23% | 99.07% | +0.84pp |
| **Successful Checkout** | 972 | 976 | +4 | +0.41pp | 102.97% | 101.99% | -0.98pp |

**Key Driver:** Checkout Attempt (+4.84pp)

---

## Conclusion

The +1.16pp PCR improvement in 2026-W14 reflects healthy performance across the payment funnel, with gains in early-funnel engagement (Select Payment Method +0.42pp) and late-funnel success (PVS Success +0.85pp) offsetting minor declines in Fraud Service approval. France contributed most significantly to the improvement with a +3.10pp PCR increase driven by better checkout initiation rates. No immediate action is required, though the slight Fraud Service approval decline (-0.23pp) should be monitored for persistence in upcoming weeks.

---

## SQL Queries

<details>
<summary>Waterfall GA (cluster/country)</summary>

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
<summary>Backend Combined (cluster/country)</summary>

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
<summary>Country PCR Summary</summary>

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
