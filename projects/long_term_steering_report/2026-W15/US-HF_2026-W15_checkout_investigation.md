# PCR Investigation: US-HF 2026-W15

**Metric:** Payment Conversion Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 26.41% → 26.23% (-0.17pp)  
**Volume:** 52,854 payment visits  
**Threshold:** +0.09pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** PCR declined by -0.17pp (26.41% → 26.23%) on 52,854 payment visits in US-HF during 2026-W15, driven primarily by Fraud Service approval rate degradation.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | GA step-rate | +0.09pp | ✅ |
| Click Submit Form | GA step-rate | -0.23pp | ⚠️ |
| FE Validation Passed | GA step-rate | -0.55pp | ⚠️ |
| Enter Fraud Service | GA step-rate | -0.10pp | ⚠️ |
| Approved by Fraud Service | GA step-rate | -0.73pp | ⚠️ |
| Call to PVS | GA step-rate | +0.37pp | ✅ |
| Successful Checkout | GA step-rate | +0.42pp | ✅ |

**Key Findings:**
- **Fraud Service approval rate is the primary driver:** Backend data shows a significant -2.40pp decline (91.91% → 89.51%) in Fraud Service approvals, indicating stricter fraud rules or increased flagging
- **FE Validation recovery rate declined:** Recovery rate dropped -1.88pp (74.36% → 72.48%), with APPLEPAY_DISMISSED errors increasing by +1.53pp share and terms_not_accepted up +0.57pp
- **Payment method performance degraded:** ProcessOut_CreditCard declined -2.10pp (82.50% → 80.40%) and Braintree_ApplePay declined -2.66pp (78.00% → 75.34%), affecting the two highest-volume payment methods
- **Braintree_CreditCard experienced severe decline:** Rate dropped -13.31pp (88.76% → 75.45%), though volume is relatively low (167 attempts)
- **PVS failures increased:** Total PVS failures rose from 934 to 1,102 (+168), with "Insufficient Funds" errors increasing +1.41pp in share

**Action:** Investigate — Prioritize review of Fraud Service rule changes impacting approval rates in US, and coordinate with Fraud team to assess if recent model updates are causing increased false positives.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 44,056 | 52,854 | 8,798 | 20.0% | - | - | - |
| Select Payment Method | 16,381 | 19,701 | 3,320 | 20.3% | 37.18% | 37.27% | +0.09pp |
| Click Submit Form | 14,468 | 17,354 | 2,886 | 19.9% | 88.32% | 88.09% | -0.23pp |
| FE Validation Passed | 13,684 | 16,318 | 2,634 | 19.2% | 94.58% | 94.03% | -0.55pp |
| Enter Fraud Service | 13,426 | 15,994 | 2,568 | 19.1% | 98.11% | 98.01% | -0.10pp |
| Approved by Fraud Service | 12,580 | 14,870 | 2,290 | 18.2% | 93.70% | 92.97% | -0.73pp |
| Call to PVS | 12,551 | 14,891 | 2,340 | 18.6% | 99.77% | 100.14% | +0.37pp |
| **Successful Checkout** | 11,634 | 13,865 | 2,231 | 19.2% | 92.69% | 93.11% | +0.42pp |
| **PCR Rate** | | | | | 26.41% | 26.23% | **-0.17pp** |

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
| US | 52,854 | 26.41% | 26.23% | -0.18pp | 1 | 1 |

---

### US

#### Waterfall GA

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 44,056 | 52,854 | +8,798 | +19.97pp | - | - | - |
| Select Payment Method | 16,381 | 19,701 | +3,320 | +20.27pp | 37.18% | 37.27% | +0.09pp |
| Click Submit Form | 14,468 | 17,354 | +2,886 | +19.95pp | 88.32% | 88.09% | -0.23pp |
| FE Validation Passed | 13,684 | 16,318 | +2,634 | +19.25pp | 94.58% | 94.03% | -0.55pp |
| Enter Fraud Service | 13,426 | 15,994 | +2,568 | +19.13pp | 98.11% | 98.01% | -0.10pp |
| Approved by Fraud Service | 12,580 | 14,870 | +2,290 | +18.20pp | 93.70% | 92.97% | -0.73pp |
| Call to PVS | 12,551 | 14,891 | +2,340 | +18.64pp | 99.77% | 100.14% | +0.37pp |
| **Successful Checkout** | 11,634 | 13,865 | +2,231 | +19.18pp | 92.69% | 93.11% | +0.42pp |
| **PCR Rate** | | | | | 26.41% | 26.23% | **-0.17pp** |

**Key Driver:** Approved by Fraud Service (-0.73pp)

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

**Include reason:** FE Validation Passed Δ Conv (-0.55pp) meets threshold (+0.09pp)

### Recovery Rate

| Metric | 2026-W14 | 2026-W15 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 3,553 | 4,357 | 804 |
| Error → Passed | 2,642 | 3,158 | 516 |
| **Recovery Rate** | **74.36%** | **72.48%** | **-1.88pp** |

### Error Type Distribution

| Error Type | 2026-W14 | 2026-W14 % | 2026-W15 | 2026-W15 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 1,805 | 50.8% | 2,280 | 52.3% | +1.53pp |
| terms_not_accepted | 1,834 | 51.6% | 2,274 | 52.2% | +0.57pp |
| PAYPAL_POPUP_CLOSED | 254 | 7.1% | 308 | 7.1% | -0.08pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 223 | 6.3% | 231 | 5.3% | -0.97pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 113 | 3.2% | 146 | 3.4% | +0.17pp |
| CC_TOKENISE_ERR | 108 | 3.0% | 114 | 2.6% | -0.42pp |
| PAYPAL_TOKENISE_ERR | 23 | 0.6% | 38 | 0.9% | +0.22pp |
| APPLEPAY_MERCHANT_VALIDATION_ERR | 0 | 0.0% | 1 | 0.0% | +0.02pp |
| CC_NO_PREPAID_ERR | 2 | 0.1% | 0 | 0.0% | -0.06pp |
| EXPRESS_CHECKOUT_APPLEPAY_TOKENISE_ERR | 1 | 0.0% | 0 | 0.0% | -0.03pp |


---

## Fraud Analysis

**Include reason:** Enter FS Δ (-0.10pp) meets threshold (+0.09pp)

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

**Include reason:** PVS Success Δ Conv (+0.42pp) meets threshold (+0.09pp)

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

*Report: 2026-04-14*
