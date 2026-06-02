# PCR Investigation: HF-NA 2026-W22

**Metric:** Payment Conversion Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 27.38% → 27.90% (+0.52pp)  
**Volume:** 57,737 payment visits  
**Threshold:** +0.26pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate improved from 27.38% to 27.90% (+0.52pp) on 57,737 payment visits in HF-NA during 2026-W22.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ≥ threshold? | +0.88pp | ✅ |
| Click Submit Form | ≥ threshold? | -0.19pp | ✅ |
| FE Validation Passed | ≥ threshold? | +0.39pp | ⚠️ |
| Enter Fraud Service | ≥ threshold? | -0.24pp | ✅ |
| Approved by Fraud Service | ≥ threshold? | +0.61pp | ⚠️ |
| Call to PVS | ≥ threshold? | -0.08pp | ✅ |
| Successful Checkout | ≥ threshold? | -0.69pp | ⚠️ |

**Key Findings:**
- **US drove the improvement:** US PCR increased +1.01pp (25.15% → 26.16%) with Select Payment Method conversion up +1.20pp, offsetting CA's decline of -1.18pp
- **Backend data anomaly:** Backend waterfall shows Payment Method Listed dropped to 0 in 2026-W22 and Successful Checkout showing 0, indicating a critical data collection issue that requires immediate investigation
- **Fraud service gap increased:** Gap between Checkout Attempt and Enter Fraud Service grew from 0.49% to 1.23% (+0.74pp), with Adyen_CreditCard accounting for 60.3% of the gap in W22 (up from 8.6%)
- **FE validation recovery improved:** Recovery rate increased from 67.52% to 69.77% (+2.25pp), with terms_not_accepted errors rising slightly (+1.21pp share)
- **CA Click Submit Form declined:** CA saw -1.61pp drop in Click Submit Form conversion (79.89% → 78.29%), contributing to the country's overall PCR decline

**Action:** **Investigate** — Critical backend data logging issue (0 values for Payment Method Listed and Successful Checkout) requires immediate technical investigation. Additionally, the increasing fraud service gap for Adyen_CreditCard should be reviewed with the payments team.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 56,784 | 57,737 | 953 | 1.7% | - | - | - |
| Select Payment Method | 23,287 | 24,184 | 897 | 3.9% | 41.01% | 41.89% | +0.88pp |
| Click Submit Form | 19,761 | 20,476 | 715 | 3.6% | 84.86% | 84.67% | -0.19pp |
| FE Validation Passed | 18,490 | 19,239 | 749 | 4.1% | 93.57% | 93.96% | +0.39pp |
| Enter Fraud Service | 17,901 | 18,580 | 679 | 3.8% | 96.81% | 96.57% | -0.24pp |
| Approved by Fraud Service | 16,842 | 17,595 | 753 | 4.5% | 94.08% | 94.70% | +0.61pp |
| Call to PVS | 16,751 | 17,486 | 735 | 4.4% | 99.46% | 99.38% | -0.08pp |
| **Successful Checkout** | 15,546 | 16,107 | 561 | 3.6% | 92.81% | 92.11% | -0.69pp |
| **PCR Rate** | | | | | 27.38% | 27.90% | **+0.52pp** |

### Waterfall Backend

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 60,874 | 0 | -60,874 | -100.0% | - | - | - |
| Checkout Attempt | 21,892 | 20,302 | -1,590 | -7.3% | 35.96% | 0.00% | -35.96pp |
| Enter Fraud Service | 21,785 | 20,052 | -1,733 | -8.0% | 99.51% | 98.77% | -0.74pp |
| Approved by Fraud Service | 20,192 | 18,680 | -1,512 | -7.5% | 92.69% | 93.16% | +0.47pp |
| PVS Attempt | 18,838 | 17,447 | -1,391 | -7.4% | 93.29% | 93.40% | +0.10pp |
| PVS Success | 17,395 | 16,034 | -1,361 | -7.8% | 92.34% | 91.90% | -0.44pp |
| **Successful Checkout** | 17,327 | 0 | -17,327 | -100.0% | 99.61% | 0.00% | -99.61pp |
| **PCR Rate** | | | | | 28.46% | 0.00% | **-28.46pp** |

### Payment Method Breakdown

| Payment Method | 2026-W21 Attempt | 2026-W21 Success | 2026-W21 Rate | 2026-W22 Attempt | 2026-W22 Success | 2026-W22 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 12,075 | 10,087 | 83.54% | 11,002 | 0 | 0.00% | -83.54pp |
| Braintree_ApplePay | 6,787 | 4,684 | 69.01% | 6,384 | 0 | 0.00% | -69.01pp |
| Braintree_Paypal | 1,998 | 1,698 | 84.98% | 1,778 | 0 | 0.00% | -84.98pp |
| Adyen_CreditCard | 699 | 644 | 92.13% | 824 | 0 | 0.00% | -92.13pp |
| Braintree_CreditCard | 247 | 212 | 85.83% | 212 | 0 | 0.00% | -85.83pp |
| NoPayment | 21 | 0 | 0.00% | 33 | 0 | 0.00% | +0.00pp |
| visa | 30 | 1 | 3.33% | 32 | 0 | 0.00% | -3.33pp |
| mc | 13 | 0 | 0.00% | 22 | 0 | 0.00% | +0.00pp |
| paypal | 10 | 0 | 0.00% | 11 | 0 | 0.00% | +0.00pp |
| amex | 10 | 0 | 0.00% | 2 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (2 countries in HF-NA)

| Country | Volume | PCR 2026-W21 | PCR 2026-W22 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| US | 43,571 | 25.15% | 26.16% | +1.01pp | 1 | 2 |
| CA | 14,166 | 34.42% | 33.24% | -1.18pp | 2 | 1 |

---

### US

#### Waterfall GA

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 43,129 | 43,571 | +442 | +1.02pp | - | - | - |
| Select Payment Method | 16,160 | 16,847 | +687 | +4.25pp | 37.47% | 38.67% | +1.20pp |
| Click Submit Form | 14,067 | 14,732 | +665 | +4.73pp | 87.05% | 87.45% | +0.40pp |
| FE Validation Passed | 13,167 | 13,826 | +659 | +5.00pp | 93.60% | 93.85% | +0.25pp |
| Enter Fraud Service | 12,748 | 13,362 | +614 | +4.82pp | 96.82% | 96.64% | -0.17pp |
| Approved by Fraud Service | 11,977 | 12,645 | +668 | +5.58pp | 93.95% | 94.63% | +0.68pp |
| Call to PVS | 11,946 | 12,624 | +678 | +5.68pp | 99.74% | 99.83% | +0.09pp |
| **Successful Checkout** | 10,846 | 11,398 | +552 | +5.09pp | 90.79% | 90.29% | -0.50pp |
| **PCR Rate** | | | | | 25.15% | 26.16% | **+1.01pp** |

**Key Driver:** Select Payment Method (+1.20pp)

#### Waterfall Backend

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 46,653 | 0 | -46,653 | -100.00pp | - | - | - |
| Checkout Attempt | 15,926 | 14,945 | -981 | -6.16pp | 34.14% | 0.00% | -34.14pp |
| Enter Fraud Service | 15,858 | 14,745 | -1,113 | -7.02pp | 99.57% | 98.66% | -0.91pp |
| Approved by Fraud Service | 14,707 | 13,754 | -953 | -6.48pp | 92.74% | 93.28% | +0.54pp |
| PVS Attempt | 14,320 | 13,392 | -928 | -6.48pp | 97.37% | 97.37% | -0.00pp |
| PVS Success | 12,997 | 12,102 | -895 | -6.89pp | 90.76% | 90.37% | -0.39pp |
| **Successful Checkout** | 13,335 | 12,602 | -733 | -5.50pp | 102.60% | 104.13% | +1.53pp |

**Key Driver:** Checkout Attempt (-34.14pp)

---

### CA

#### Waterfall GA

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 13,655 | 14,166 | +511 | +3.74pp | - | - | - |
| Select Payment Method | 7,127 | 7,337 | +210 | +2.95pp | 52.19% | 51.79% | -0.40pp |
| Click Submit Form | 5,694 | 5,744 | +50 | +0.88pp | 79.89% | 78.29% | -1.61pp |
| FE Validation Passed | 5,323 | 5,413 | +90 | +1.69pp | 93.48% | 94.24% | +0.75pp |
| Enter Fraud Service | 5,153 | 5,218 | +65 | +1.26pp | 96.81% | 96.40% | -0.41pp |
| Approved by Fraud Service | 4,865 | 4,950 | +85 | +1.75pp | 94.41% | 94.86% | +0.45pp |
| Call to PVS | 4,805 | 4,862 | +57 | +1.19pp | 98.77% | 98.22% | -0.54pp |
| **Successful Checkout** | 4,700 | 4,709 | +9 | +0.19pp | 97.81% | 96.85% | -0.96pp |
| **PCR Rate** | | | | | 34.42% | 33.24% | **-1.18pp** |

**Key Driver:** Click Submit Form (-1.61pp)

#### Waterfall Backend

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 14,221 | 0 | -14,221 | -100.00pp | - | - | - |
| Checkout Attempt | 5,966 | 5,357 | -609 | -10.21pp | 41.95% | 0.00% | -41.95pp |
| Enter Fraud Service | 5,927 | 5,307 | -620 | -10.46pp | 99.35% | 99.07% | -0.28pp |
| Approved by Fraud Service | 5,485 | 4,926 | -559 | -10.19pp | 92.54% | 92.82% | +0.28pp |
| PVS Attempt | 4,518 | 4,055 | -463 | -10.25pp | 82.37% | 82.32% | -0.05pp |
| PVS Success | 4,398 | 3,932 | -466 | -10.60pp | 97.34% | 96.97% | -0.38pp |
| **Successful Checkout** | 5,356 | 4,793 | -563 | -10.51pp | 121.78% | 121.90% | +0.11pp |

**Key Driver:** Checkout Attempt (-41.95pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (+0.39pp) meets threshold (+0.26pp)

### Recovery Rate

| Metric | 2026-W21 | 2026-W22 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 4,486 | 4,701 | 215 |
| Error → Passed | 3,029 | 3,280 | 251 |
| **Recovery Rate** | **67.52%** | **69.77%** | **+2.25pp** |

### Error Type Distribution

| Error Type | 2026-W21 | 2026-W21 % | 2026-W22 | 2026-W22 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 2,600 | 58.0% | 2,740 | 58.3% | +0.33pp |
| terms_not_accepted | 1,819 | 40.5% | 1,963 | 41.8% | +1.21pp |
| PAYPAL_POPUP_CLOSED | 456 | 10.2% | 449 | 9.6% | -0.61pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 256 | 5.7% | 257 | 5.5% | -0.24pp |
| CC_TOKENISE_ERR | 143 | 3.2% | 152 | 3.2% | +0.05pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 97 | 2.2% | 110 | 2.3% | +0.18pp |
| PAYPAL_TOKENISE_ERR | 64 | 1.4% | 45 | 1.0% | -0.47pp |
| CC_NO_PREPAID_ERR | 12 | 0.3% | 9 | 0.2% | -0.08pp |
| APPLEPAY_MERCHANT_VALIDATION_ERR | 1 | 0.0% | 0 | 0.0% | -0.02pp |


---

## Fraud Analysis

**Include reason:** Approved Δ (+0.61pp) meets threshold (+0.26pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W21 | 2026-W21 % | 2026-W22 | 2026-W22 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 21,892 | - | 20,302 | - | -1,590 | -7.3% |
| Enter Fraud Service | 21,785 | - | 20,052 | - | -1,733 | -8.0% |
| **Gap (Skipped)** | **107** | **0.49%** | **250** | **1.23%** | **143** | **+0.74pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W21 Gap | 2026-W21 % | 2026-W22 Gap | 2026-W22 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Adyen_CreditCard | 12 | 8.6% | 176 | 60.3% | +164 | +51.70pp |
| ProcessOut_CreditCard | 66 | 47.1% | 48 | 16.4% | -18 | -30.70pp |
| NoPayment | 21 | 15.0% | 33 | 11.3% | +12 | -3.70pp |
| Braintree_ApplePay | 32 | 22.9% | 23 | 7.9% | -9 | -14.98pp |
| Braintree_Paypal | 9 | 6.4% | 12 | 4.1% | +3 | -2.32pp |
| **Total** | **140** | **100%** | **292** | **100%** | **152** | - |

*% of Gap = Payment Method Gap / Total Gap*

---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (-0.69pp) meets threshold (+0.26pp)

| Decline Reason | 2026-W21 | 2026-W21 % | 2026-W22 | 2026-W22 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Blocked Verification: Payment method is blocked due to business reasons | 640 | 55.0% | 637 | 56.2% | -3 | +1.14pp |
| Failed Verification: Insufficient Funds | 259 | 22.3% | 225 | 19.8% | -34 | -2.43pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 104 | 8.9% | 100 | 8.8% | -4 | -0.12pp |
| Failed Verification: Issuer or Cardholder has put a restriction on the card | 58 | 5.0% | 58 | 5.1% | 0 | +0.13pp |
| Failed Verification: code: 91564 - field: PaymentMethodNonce - Message: Cannot use a payment_method_nonce more than once. | 11 | 0.9% | 25 | 2.2% | +14 | +1.26pp |
| Failed Verification: Declined | 31 | 2.7% | 23 | 2.0% | -8 | -0.64pp |
| Failed Verification: Processor Declined - Fraud Suspected | 31 | 2.7% | 18 | 1.6% | -13 | -1.08pp |
| Failed Verification: Blocked by cardholder/contact cardholder | 0 | 0.0% | 18 | 1.6% | +18 | +1.59pp |
| Failed Verification: Processor Declined | 29 | 2.5% | 15 | 1.3% | -14 | -1.17pp |
| Failed Verification: Closed Account | 0 | 0.0% | 15 | 1.3% | +15 | +1.32pp |
| **Total PVS Failures** | **1,163** | **100%** | **1,134** | **100%** | **-29** | - |

---


---

*Report: 2026-06-02*
