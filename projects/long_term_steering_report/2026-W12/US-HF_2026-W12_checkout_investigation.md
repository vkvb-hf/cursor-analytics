# PCR Investigation: US-HF 2026-W12

**Metric:** Payment Conversion Rate  
**Period:** 2026-W11 → 2026-W12  
**Observation:** 25.84% → 26.18% (+0.34pp)  
**Volume:** 46,444 payment visits  
**Threshold:** +0.17pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate improved by +0.34pp (25.84% → 26.18%) in US-HF during 2026-W12, exceeding the significance threshold of +0.17pp, driven primarily by improved form submission and frontend validation performance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Above threshold | -1.18pp | ⚠️ |
| Click Submit Form | Above threshold | +2.25pp | ✅ |
| FE Validation Passed | Above threshold | +1.35pp | ✅ |
| Enter Fraud Service | Below threshold | +0.06pp | ✅ |
| Approved by Fraud Service | Below threshold | +0.11pp | ✅ |
| Call to PVS | Below threshold | -0.10pp | ✅ |
| Successful Checkout | Below threshold | +0.04pp | ✅ |

**Key Findings:**
- **Click Submit Form conversion increased significantly (+2.25pp)**, representing the largest positive driver of PCR improvement, with conversion rising from 81.84% to 84.09%
- **FE Validation recovery rate improved by +3.36pp** (69.81% → 73.17%), with fewer customers encountering errors (4,604 → 4,003) and more successfully recovering
- **ProcessOut_CreditCard showed strong performance gains (+2.88pp)** with increased volume (5,554 → 6,991 attempts) and improved success rate (78.61% → 81.49%)
- **Select Payment Method conversion declined (-1.18pp)**, partially offsetting gains, with conversion dropping from 40.06% to 38.88%
- **CC_NO_PREPAID_ERR reduced significantly (-3.96pp share)**, dropping from 470 to 250 occurrences, contributing to improved FE validation performance

**Action:** Monitor - The PCR improvement is positive and driven by identifiable improvements in form submission and validation steps. Continue monitoring the Select Payment Method drop-off and ProcessOut_CreditCard performance trends.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 50,340 | 46,444 | -3,896 | -7.7% | - | - | - |
| Select Payment Method | 20,164 | 18,056 | -2,108 | -10.5% | 40.06% | 38.88% | -1.18pp |
| Click Submit Form | 16,503 | 15,184 | -1,319 | -8.0% | 81.84% | 84.09% | +2.25pp |
| FE Validation Passed | 15,265 | 14,250 | -1,015 | -6.6% | 92.50% | 93.85% | +1.35pp |
| Enter Fraud Service | 14,921 | 13,938 | -983 | -6.6% | 97.75% | 97.81% | +0.06pp |
| Approved by Fraud Service | 14,010 | 13,102 | -908 | -6.5% | 93.89% | 94.00% | +0.11pp |
| Call to PVS | 14,003 | 13,082 | -921 | -6.6% | 99.95% | 99.85% | -0.10pp |
| **Successful Checkout** | 13,010 | 12,160 | -850 | -6.5% | 92.91% | 92.95% | +0.04pp |
| **PCR Rate** | | | | | 25.84% | 26.18% | **+0.34pp** |

### Waterfall Backend

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 56,242 | 50,863 | -5,379 | -9.6% | - | - | - |
| Checkout Attempt | 19,306 | 17,752 | -1,554 | -8.0% | 34.33% | 34.90% | +0.57pp |
| Enter Fraud Service | 19,240 | 17,717 | -1,523 | -7.9% | 99.66% | 99.80% | +0.14pp |
| Approved by Fraud Service | 17,321 | 15,978 | -1,343 | -7.8% | 90.03% | 90.18% | +0.16pp |
| PVS Attempt | 16,952 | 15,651 | -1,301 | -7.7% | 97.87% | 97.95% | +0.08pp |
| PVS Success | 15,766 | 14,543 | -1,223 | -7.8% | 93.00% | 92.92% | -0.08pp |
| **Successful Checkout** | 15,363 | 14,106 | -1,257 | -8.2% | 97.44% | 97.00% | -0.45pp |
| **PCR Rate** | | | | | 27.32% | 27.73% | **+0.42pp** |

### Payment Method Breakdown

| Payment Method | 2026-W11 Attempt | 2026-W11 Success | 2026-W11 Rate | 2026-W12 Attempt | 2026-W12 Success | 2026-W12 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 5,554 | 4,366 | 78.61% | 6,991 | 5,697 | 81.49% | +2.88pp |
| Braintree_ApplePay | 6,491 | 4,940 | 76.11% | 5,978 | 4,515 | 75.53% | -0.58pp |
| Braintree_CreditCard | 5,630 | 4,762 | 84.58% | 3,268 | 2,706 | 82.80% | -1.78pp |
| Braintree_Paypal | 1,524 | 1,294 | 84.91% | 1,395 | 1,187 | 85.09% | +0.18pp |
|  | 93 | 0 | 0.00% | 119 | 0 | 0.00% | +0.00pp |
| Braintree_Venmo | 1 | 1 | 100.00% | 1 | 1 | 100.00% | +0.00pp |
| Adyen_CreditCard | 13 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (1 countries in US-HF)

| Country | Volume | PCR 2026-W11 | PCR 2026-W12 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| US | 46,444 | 25.84% | 26.18% | +0.34pp | 1 | 1 |

---

### US

#### Waterfall GA

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 50,340 | 46,444 | -3,896 | -7.74pp | - | - | - |
| Select Payment Method | 20,164 | 18,056 | -2,108 | -10.45pp | 40.06% | 38.88% | -1.18pp |
| Click Submit Form | 16,503 | 15,184 | -1,319 | -7.99pp | 81.84% | 84.09% | +2.25pp |
| FE Validation Passed | 15,265 | 14,250 | -1,015 | -6.65pp | 92.50% | 93.85% | +1.35pp |
| Enter Fraud Service | 14,921 | 13,938 | -983 | -6.59pp | 97.75% | 97.81% | +0.06pp |
| Approved by Fraud Service | 14,010 | 13,102 | -908 | -6.48pp | 93.89% | 94.00% | +0.11pp |
| Call to PVS | 14,003 | 13,082 | -921 | -6.58pp | 99.95% | 99.85% | -0.10pp |
| **Successful Checkout** | 13,010 | 12,160 | -850 | -6.53pp | 92.91% | 92.95% | +0.04pp |
| **PCR Rate** | | | | | 25.84% | 26.18% | **+0.34pp** |

**Key Driver:** Click Submit Form (+2.25pp)

#### Waterfall Backend

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 56,242 | 50,863 | -5,379 | -9.56pp | - | - | - |
| Checkout Attempt | 19,306 | 17,752 | -1,554 | -8.05pp | 34.33% | 34.90% | +0.57pp |
| Enter Fraud Service | 19,240 | 17,717 | -1,523 | -7.92pp | 99.66% | 99.80% | +0.14pp |
| Approved by Fraud Service | 17,321 | 15,978 | -1,343 | -7.75pp | 90.03% | 90.18% | +0.16pp |
| PVS Attempt | 16,952 | 15,651 | -1,301 | -7.67pp | 97.87% | 97.95% | +0.08pp |
| PVS Success | 15,766 | 14,543 | -1,223 | -7.76pp | 93.00% | 92.92% | -0.08pp |
| **Successful Checkout** | 16,104 | 14,855 | -1,249 | -7.76pp | 102.14% | 102.15% | +0.00pp |

**Key Driver:** Checkout Attempt (+0.57pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (+1.35pp) meets threshold (+0.17pp)

### Recovery Rate

| Metric | 2026-W11 | 2026-W12 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 4,604 | 4,003 | -601 |
| Error → Passed | 3,214 | 2,929 | -285 |
| **Recovery Rate** | **69.81%** | **73.17%** | **+3.36pp** |

### Error Type Distribution

| Error Type | 2026-W11 | 2026-W11 % | 2026-W12 | 2026-W12 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| terms_not_accepted | 2,323 | 50.5% | 2,074 | 51.8% | +1.36pp |
| APPLEPAY_DISMISSED | 2,236 | 48.6% | 1,949 | 48.7% | +0.12pp |
| PAYPAL_POPUP_CLOSED | 336 | 7.3% | 268 | 6.7% | -0.60pp |
| CC_NO_PREPAID_ERR | 470 | 10.2% | 250 | 6.2% | -3.96pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 237 | 5.1% | 213 | 5.3% | +0.17pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 129 | 2.8% | 109 | 2.7% | -0.08pp |
| CC_TOKENISE_ERR | 81 | 1.8% | 91 | 2.3% | +0.51pp |
| PAYPAL_TOKENISE_ERR | 26 | 0.6% | 33 | 0.8% | +0.26pp |
| APPLEPAY_MERCHANT_VALIDATION_ERR | 1 | 0.0% | 3 | 0.1% | +0.05pp |
| VENMO_TOKENISE_ERR | 0 | 0.0% | 1 | 0.0% | +0.02pp |


---


---

*Report: 2026-04-10*
