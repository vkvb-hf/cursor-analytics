# PCR Investigation: US-HF 2026-W15

**Metric:** Payment Conversion Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 26.41% → 26.24% (-0.17pp)  
**Volume:** 52,863 payment visits  
**Threshold:** +0.08pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined by -0.17pp (26.41% → 26.24%) on 52,863 payment visits in US-HF during 2026-W15, with the primary driver being a significant drop in Fraud Service approval rates.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ≥ threshold | +0.10pp | ✅ |
| Click Submit Form | < threshold | -0.25pp | ⚠️ |
| FE Validation Passed | < threshold | -0.57pp | ⚠️ |
| Enter Fraud Service | < threshold | -0.09pp | ⚠️ |
| Approved by Fraud Service | < threshold | -0.71pp | ⚠️ |
| Call to PVS | ≥ threshold | +0.36pp | ✅ |
| Successful Checkout | ≥ threshold | +0.44pp | ✅ |

**Key Findings:**
- **Fraud Service approval is the primary bottleneck:** GA waterfall shows -0.71pp decline, while backend data reveals a more severe -2.40pp drop in Fraud Service approval rate (91.91% → 89.51%)
- **FE Validation recovery rate declined:** Customer recovery rate dropped -1.88pp (74.36% → 72.48%), with APPLEPAY_DISMISSED errors increasing share by +1.55pp to 52.4% of all errors
- **ProcessOut_CreditCard and Braintree_ApplePay both underperforming:** ProcessOut_CreditCard declined -2.10pp (82.50% → 80.40%) and Braintree_ApplePay declined -2.66pp (78.00% → 75.34%)
- **Braintree_CreditCard experienced severe decline:** Success rate dropped -13.31pp (88.76% → 75.45%), though on relatively low volume (167 attempts)
- **Adyen_CreditCard continues to show 0% success rate** with 240 attempts, contributing entirely to the Fraud Service gap

**Action:** **Investigate** - Priority focus on Fraud Service configuration/rules changes affecting ProcessOut_CreditCard and Braintree_ApplePay in US; secondary investigation into Adyen_CreditCard integration failure and elevated APPLEPAY_DISMISSED errors.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 44,056 | 52,863 | 8,807 | 20.0% | - | - | - |
| Select Payment Method | 16,381 | 19,711 | 3,330 | 20.3% | 37.18% | 37.29% | +0.10pp |
| Click Submit Form | 14,468 | 17,360 | 2,892 | 20.0% | 88.32% | 88.07% | -0.25pp |
| FE Validation Passed | 13,684 | 16,321 | 2,637 | 19.3% | 94.58% | 94.01% | -0.57pp |
| Enter Fraud Service | 13,426 | 15,998 | 2,572 | 19.2% | 98.11% | 98.02% | -0.09pp |
| Approved by Fraud Service | 12,583 | 14,880 | 2,297 | 18.3% | 93.72% | 93.01% | -0.71pp |
| Call to PVS | 12,551 | 14,895 | 2,344 | 18.7% | 99.75% | 100.10% | +0.36pp |
| **Successful Checkout** | 11,634 | 13,872 | 2,238 | 19.2% | 92.69% | 93.13% | +0.44pp |
| **PCR Rate** | | | | | 26.41% | 26.24% | **-0.17pp** |

### Waterfall Backend

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 47,792 | 57,223 | 9,431 | 19.7% | - | - | - |
| Checkout Attempt | 16,949 | 20,476 | 3,527 | 20.8% | 35.46% | 35.78% | +0.32pp |
| Enter Fraud Service | 16,671 | 20,167 | 3,496 | 21.0% | 98.36% | 98.49% | +0.13pp |
| Approved by Fraud Service | 15,322 | 18,051 | 2,729 | 17.8% | 91.91% | 89.51% | -2.40pp |
| PVS Attempt | 14,911 | 17,669 | 2,758 | 18.5% | 97.32% | 97.88% | +0.57pp |
| PVS Success | 13,845 | 16,435 | 2,590 | 18.7% | 92.85% | 93.02% | +0.17pp |
| **Successful Checkout** | 13,514 | 15,942 | 2,428 | 18.0% | 97.61% | 97.00% | -0.61pp |
| **PCR Rate** | | | | | 28.28% | 27.86% | **-0.42pp** |

### Payment Method Breakdown

| Payment Method | 2026-W14 Attempt | 2026-W14 Success | 2026-W14 Rate | 2026-W15 Attempt | 2026-W15 Success | 2026-W15 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 9,309 | 7,680 | 82.50% | 11,650 | 9,367 | 80.40% | -2.10pp |
| Braintree_ApplePay | 5,745 | 4,481 | 78.00% | 6,740 | 5,078 | 75.34% | -2.66pp |
| Braintree_Paypal | 1,384 | 1,193 | 86.20% | 1,586 | 1,371 | 86.44% | +0.24pp |
| Adyen_CreditCard | 212 | 0 | 0.00% | 240 | 0 | 0.00% | +0.00pp |
| Braintree_CreditCard | 178 | 158 | 88.76% | 167 | 126 | 75.45% | -13.31pp |
|  | 120 | 1 | 0.83% | 93 | 0 | 0.00% | -0.83pp |
| Braintree_Venmo | 1 | 1 | 100.00% | 0 | 0 | 0.00% | -100.00pp |
| CreditCard | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (1 countries in US-HF)

| Country | Volume | PCR 2026-W14 | PCR 2026-W15 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| US | 52,863 | 26.41% | 26.24% | -0.17pp | 1 | 1 |

---

### US

#### Waterfall GA

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 44,056 | 52,863 | +8,807 | +19.99pp | - | - | - |
| Select Payment Method | 16,381 | 19,711 | +3,330 | +20.33pp | 37.18% | 37.29% | +0.10pp |
| Click Submit Form | 14,468 | 17,360 | +2,892 | +19.99pp | 88.32% | 88.07% | -0.25pp |
| FE Validation Passed | 13,684 | 16,321 | +2,637 | +19.27pp | 94.58% | 94.01% | -0.57pp |
| Enter Fraud Service | 13,426 | 15,998 | +2,572 | +19.16pp | 98.11% | 98.02% | -0.09pp |
| Approved by Fraud Service | 12,583 | 14,880 | +2,297 | +18.25pp | 93.72% | 93.01% | -0.71pp |
| Call to PVS | 12,551 | 14,895 | +2,344 | +18.68pp | 99.75% | 100.10% | +0.36pp |
| **Successful Checkout** | 11,634 | 13,872 | +2,238 | +19.24pp | 92.69% | 93.13% | +0.44pp |
| **PCR Rate** | | | | | 26.41% | 26.24% | **-0.17pp** |

**Key Driver:** Approved by Fraud Service (-0.71pp)

#### Waterfall Backend

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 47,792 | 57,223 | +9,431 | +19.73pp | - | - | - |
| Checkout Attempt | 16,949 | 20,476 | +3,527 | +20.81pp | 35.46% | 35.78% | +0.32pp |
| Enter Fraud Service | 16,671 | 20,167 | +3,496 | +20.97pp | 98.36% | 98.49% | +0.13pp |
| Approved by Fraud Service | 15,322 | 18,051 | +2,729 | +17.81pp | 91.91% | 89.51% | -2.40pp |
| PVS Attempt | 14,911 | 17,669 | +2,758 | +18.50pp | 97.32% | 97.88% | +0.57pp |
| PVS Success | 13,845 | 16,435 | +2,590 | +18.71pp | 92.85% | 93.02% | +0.17pp |
| **Successful Checkout** | 14,421 | 17,039 | +2,618 | +18.15pp | 104.16% | 103.68% | -0.49pp |

**Key Driver:** Approved by Fraud Service (-2.40pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (-0.57pp) meets threshold (+0.08pp)

### Recovery Rate

| Metric | 2026-W14 | 2026-W15 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 3,553 | 4,361 | 808 |
| Error → Passed | 2,642 | 3,161 | 519 |
| **Recovery Rate** | **74.36%** | **72.48%** | **-1.88pp** |

### Error Type Distribution

| Error Type | 2026-W14 | 2026-W14 % | 2026-W15 | 2026-W15 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 1,805 | 50.8% | 2,283 | 52.4% | +1.55pp |
| terms_not_accepted | 1,834 | 51.6% | 2,277 | 52.2% | +0.59pp |
| PAYPAL_POPUP_CLOSED | 254 | 7.1% | 309 | 7.1% | -0.06pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 223 | 6.3% | 231 | 5.3% | -0.98pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 113 | 3.2% | 146 | 3.3% | +0.17pp |
| CC_TOKENISE_ERR | 108 | 3.0% | 114 | 2.6% | -0.43pp |
| PAYPAL_TOKENISE_ERR | 23 | 0.6% | 38 | 0.9% | +0.22pp |
| APPLEPAY_MERCHANT_VALIDATION_ERR | 0 | 0.0% | 1 | 0.0% | +0.02pp |
| CC_NO_PREPAID_ERR | 2 | 0.1% | 0 | 0.0% | -0.06pp |
| EXPRESS_CHECKOUT_APPLEPAY_TOKENISE_ERR | 1 | 0.0% | 0 | 0.0% | -0.03pp |


---

## Fraud Analysis

**Include reason:** Enter FS Δ (-0.09pp) meets threshold (+0.08pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W14 | 2026-W14 % | 2026-W15 | 2026-W15 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 16,949 | - | 20,476 | - | 3,527 | 20.8% |
| Enter Fraud Service | 16,671 | - | 20,167 | - | 3,496 | 21.0% |
| **Gap (Skipped)** | **278** | **1.64%** | **309** | **1.51%** | **31** | **-0.13pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W14 Gap | 2026-W14 % | 2026-W15 Gap | 2026-W15 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Adyen_CreditCard | 212 | 76.3% | 240 | 77.4% | +28 | +1.16pp |
| ProcessOut_CreditCard | 34 | 12.2% | 36 | 11.6% | +2 | -0.62pp |
| Braintree_ApplePay | 23 | 8.3% | 26 | 8.4% | +3 | +0.11pp |
| Braintree_Paypal | 9 | 3.2% | 6 | 1.9% | -3 | -1.30pp |
| Braintree_CreditCard | 0 | 0.0% | 2 | 0.6% | +2 | +0.65pp |
| **Total** | **278** | **100%** | **310** | **100%** | **32** | - |

*% of Gap = Payment Method Gap / Total Gap*

---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (+0.44pp) meets threshold (+0.08pp)

| Decline Reason | 2026-W14 | 2026-W14 % | 2026-W15 | 2026-W15 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Blocked Verification: Payment method is blocked due to business reasons | 534 | 57.2% | 605 | 54.9% | +71 | -2.27pp |
| Failed Verification: Insufficient Funds | 158 | 16.9% | 202 | 18.3% | +44 | +1.41pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 52 | 5.6% | 52 | 4.7% | 0 | -0.85pp |
| Failed Verification: Card Issuer Declined CVV | 34 | 3.6% | 51 | 4.6% | +17 | +0.99pp |
| Failed Verification: Declined - Call Issuer | 42 | 4.5% | 43 | 3.9% | +1 | -0.59pp |
| Failed Verification: Issuer or Cardholder has put a restriction on the card | 33 | 3.5% | 39 | 3.5% | +6 | +0.01pp |
| Failed Verification: Processor Declined - Fraud Suspected | 27 | 2.9% | 33 | 3.0% | +6 | +0.10pp |
| Failed Verification: Processor Declined | 24 | 2.6% | 30 | 2.7% | +6 | +0.15pp |
| Failed Verification: Closed Card | 14 | 1.5% | 24 | 2.2% | +10 | +0.68pp |
| Failed Verification: Declined | 16 | 1.7% | 23 | 2.1% | +7 | +0.37pp |
| **Total PVS Failures** | **934** | **100%** | **1,102** | **100%** | **+168** | - |

---


---

*Report: 2026-04-17*
