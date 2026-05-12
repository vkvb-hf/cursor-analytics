# PCR Investigation: US-HF 2026-W19

**Metric:** Payment Conversion Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 23.37% → 23.95% (+0.57pp)  
**Volume:** 51,440 payment visits  
**Threshold:** +0.29pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate improved by +0.57pp (23.37% → 23.95%) in US-HF for 2026-W19, driven primarily by increased user engagement at the payment method selection stage, despite headwinds from PVS failures and fraud service gaps.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Rate change vs threshold | +1.07pp | ✅ Improved |
| Click Submit Form | Rate change vs threshold | +0.45pp | ✅ Improved |
| FE Validation Passed | Rate change vs threshold | -0.37pp | ⚠️ Exceeds threshold |
| Enter Fraud Service | Rate change vs threshold | -0.33pp | ⚠️ Exceeds threshold |
| Approved by Fraud Service | Rate change vs threshold | -0.10pp | ✅ Within threshold |
| Call to PVS | Rate change vs threshold | +0.71pp | ✅ Improved |
| Successful Checkout | Rate change vs threshold | -0.91pp | ⚠️ Exceeds threshold |

**Key Findings:**
- **PVS Success rate dropped significantly (-1.53pp)** in backend data, with "Insufficient Funds" declines increasing by 139 cases (+5.53pp share), becoming the fastest-growing decline reason
- **Fraud service gap widened (+0.43pp)** with Adyen_CreditCard accounting for 57.9% of skipped transactions (143 of 247 gaps), up from 55.6%
- **ProcessOut_CreditCard success rate declined (-1.89pp)** despite being the highest volume payment method (10,651 attempts), potentially masking overall PCR gains
- **FE Validation recovery rate decreased (-1.17pp)** to 71.61%, with "terms_not_accepted" errors affecting 51.8% of users experiencing errors
- **Braintree_Paypal showed strong improvement (+2.22pp)** in success rate, reaching 83.51%

**Action:** **Investigate** - The PVS failure increase (+239 cases) and Adyen_CreditCard fraud service gap require immediate attention. Recommend reviewing Adyen integration logs and coordinating with payment processor on increased "Insufficient Funds" declines.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 54,042 | 51,440 | -2,602 | -4.8% | - | - | - |
| Select Payment Method | 18,879 | 18,520 | -359 | -1.9% | 34.93% | 36.00% | +1.07pp |
| Click Submit Form | 16,481 | 16,251 | -230 | -1.4% | 87.30% | 87.75% | +0.45pp |
| FE Validation Passed | 15,487 | 15,211 | -276 | -1.8% | 93.97% | 93.60% | -0.37pp |
| Enter Fraud Service | 14,996 | 14,678 | -318 | -2.1% | 96.83% | 96.50% | -0.33pp |
| Approved by Fraud Service | 14,290 | 13,973 | -317 | -2.2% | 95.29% | 95.20% | -0.10pp |
| Call to PVS | 13,876 | 13,667 | -209 | -1.5% | 97.10% | 97.81% | +0.71pp |
| **Successful Checkout** | 12,632 | 12,318 | -314 | -2.5% | 91.03% | 90.13% | -0.91pp |
| **PCR Rate** | | | | | 23.37% | 23.95% | **+0.57pp** |

### Waterfall Backend

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 58,098 | 56,039 | -2,059 | -3.5% | - | - | - |
| Checkout Attempt | 18,914 | 18,985 | 71 | 0.4% | 32.56% | 33.88% | +1.32pp |
| Enter Fraud Service | 18,752 | 18,741 | -11 | -0.1% | 99.14% | 98.71% | -0.43pp |
| Approved by Fraud Service | 17,404 | 17,218 | -186 | -1.1% | 92.81% | 91.87% | -0.94pp |
| PVS Attempt | 16,396 | 16,324 | -72 | -0.4% | 94.21% | 94.81% | +0.60pp |
| PVS Success | 14,942 | 14,627 | -315 | -2.1% | 91.13% | 89.60% | -1.53pp |
| **Successful Checkout** | 14,591 | 14,496 | -95 | -0.7% | 97.65% | 99.10% | +1.45pp |
| **PCR Rate** | | | | | 25.11% | 25.87% | **+0.75pp** |

### Payment Method Breakdown

| Payment Method | 2026-W18 Attempt | 2026-W18 Success | 2026-W18 Rate | 2026-W19 Attempt | 2026-W19 Success | 2026-W19 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 10,449 | 8,291 | 79.35% | 10,651 | 8,250 | 77.46% | -1.89pp |
| Braintree_ApplePay | 6,474 | 4,784 | 73.90% | 6,225 | 4,632 | 74.41% | +0.51pp |
| Braintree_Paypal | 1,534 | 1,247 | 81.29% | 1,522 | 1,271 | 83.51% | +2.22pp |
| Braintree_CreditCard | 312 | 266 | 85.26% | 398 | 341 | 85.68% | +0.42pp |
| Adyen_CreditCard | 90 | 0 | 0.00% | 143 | 0 | 0.00% | +0.00pp |
| visa | 0 | 0 | 0.00% | 19 | 0 | 0.00% | +0.00pp |
| paypal | 0 | 0 | 0.00% | 9 | 0 | 0.00% | +0.00pp |
| mc | 0 | 0 | 0.00% | 8 | 2 | 25.00% | +25.00pp |
|  | 52 | 0 | 0.00% | 7 | 0 | 0.00% | +0.00pp |
| amex | 0 | 0 | 0.00% | 3 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (1 countries in US-HF)

| Country | Volume | PCR 2026-W18 | PCR 2026-W19 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| US | 51,440 | 23.37% | 23.95% | +0.58pp | 1 | 1 |

---

### US

#### Waterfall GA

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 54,042 | 51,440 | -2,602 | -4.81pp | - | - | - |
| Select Payment Method | 18,879 | 18,520 | -359 | -1.90pp | 34.93% | 36.00% | +1.07pp |
| Click Submit Form | 16,481 | 16,251 | -230 | -1.40pp | 87.30% | 87.75% | +0.45pp |
| FE Validation Passed | 15,487 | 15,211 | -276 | -1.78pp | 93.97% | 93.60% | -0.37pp |
| Enter Fraud Service | 14,996 | 14,678 | -318 | -2.12pp | 96.83% | 96.50% | -0.33pp |
| Approved by Fraud Service | 14,290 | 13,973 | -317 | -2.22pp | 95.29% | 95.20% | -0.10pp |
| Call to PVS | 13,876 | 13,667 | -209 | -1.51pp | 97.10% | 97.81% | +0.71pp |
| **Successful Checkout** | 12,632 | 12,318 | -314 | -2.49pp | 91.03% | 90.13% | -0.91pp |
| **PCR Rate** | | | | | 23.37% | 23.95% | **+0.57pp** |

**Key Driver:** Select Payment Method (+1.07pp)

#### Waterfall Backend

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 58,098 | 56,039 | -2,059 | -3.54pp | - | - | - |
| Checkout Attempt | 18,914 | 18,985 | +71 | +0.38pp | 32.56% | 33.88% | +1.32pp |
| Enter Fraud Service | 18,752 | 18,741 | -11 | -0.06pp | 99.14% | 98.71% | -0.43pp |
| Approved by Fraud Service | 17,404 | 17,218 | -186 | -1.07pp | 92.81% | 91.87% | -0.94pp |
| PVS Attempt | 16,396 | 16,324 | -72 | -0.44pp | 94.21% | 94.81% | +0.60pp |
| PVS Success | 14,942 | 14,627 | -315 | -2.11pp | 91.13% | 89.60% | -1.53pp |
| **Successful Checkout** | 15,428 | 15,313 | -115 | -0.75pp | 103.25% | 104.69% | +1.44pp |

**Key Driver:** PVS Success (-1.53pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (-0.37pp) meets threshold (+0.29pp)

### Recovery Rate

| Metric | 2026-W18 | 2026-W19 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 4,298 | 4,251 | -47 |
| Error → Passed | 3,128 | 3,044 | -84 |
| **Recovery Rate** | **72.78%** | **71.61%** | **-1.17pp** |

### Error Type Distribution

| Error Type | 2026-W18 | 2026-W18 % | 2026-W19 | 2026-W19 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 2,298 | 53.5% | 2,248 | 52.9% | -0.59pp |
| terms_not_accepted | 2,274 | 52.9% | 2,201 | 51.8% | -1.13pp |
| PAYPAL_POPUP_CLOSED | 315 | 7.3% | 313 | 7.4% | +0.03pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 251 | 5.8% | 219 | 5.2% | -0.69pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 154 | 3.6% | 137 | 3.2% | -0.36pp |
| CC_TOKENISE_ERR | 127 | 3.0% | 123 | 2.9% | -0.06pp |
| PAYPAL_TOKENISE_ERR | 30 | 0.7% | 36 | 0.8% | +0.15pp |
| CC_NO_PREPAID_ERR | 6 | 0.1% | 7 | 0.2% | +0.03pp |
| APPLEPAY_MERCHANT_VALIDATION_ERR | 2 | 0.0% | 2 | 0.0% | +0.00pp |


---

## Fraud Analysis

**Include reason:** Enter FS Δ (-0.33pp) meets threshold (+0.29pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W18 | 2026-W18 % | 2026-W19 | 2026-W19 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 18,914 | - | 18,985 | - | 71 | 0.4% |
| Enter Fraud Service | 18,752 | - | 18,741 | - | -11 | -0.1% |
| **Gap (Skipped)** | **162** | **0.86%** | **244** | **1.29%** | **82** | **+0.43pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W18 Gap | 2026-W18 % | 2026-W19 Gap | 2026-W19 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Adyen_CreditCard | 90 | 55.6% | 143 | 57.9% | +53 | +2.34pp |
| ProcessOut_CreditCard | 44 | 27.2% | 66 | 26.7% | +22 | -0.44pp |
| Braintree_ApplePay | 19 | 11.7% | 27 | 10.9% | +8 | -0.80pp |
| Braintree_Paypal | 8 | 4.9% | 10 | 4.0% | +2 | -0.89pp |
| Braintree_CreditCard | 1 | 0.6% | 1 | 0.4% | 0 | -0.21pp |
| **Total** | **162** | **100%** | **247** | **100%** | **85** | - |

*% of Gap = Payment Method Gap / Total Gap*

---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (-0.91pp) meets threshold (+0.29pp)

| Decline Reason | 2026-W18 | 2026-W18 % | 2026-W19 | 2026-W19 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Blocked Verification: Payment method is blocked due to business reasons | 678 | 51.6% | 736 | 47.4% | +58 | -4.20pp |
| Failed Verification: Insufficient Funds | 292 | 22.2% | 431 | 27.7% | +139 | +5.53pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 97 | 7.4% | 97 | 6.2% | 0 | -1.13pp |
| Failed Verification: Issuer or Cardholder has put a restriction on the card | 54 | 4.1% | 76 | 4.9% | +22 | +0.78pp |
| Failed Verification: Declined - Call Issuer | 39 | 3.0% | 44 | 2.8% | +5 | -0.13pp |
| Failed Verification: Card Issuer Declined CVV | 52 | 4.0% | 43 | 2.8% | -9 | -1.19pp |
| Failed Verification: Processor Declined - Fraud Suspected | 29 | 2.2% | 39 | 2.5% | +10 | +0.30pp |
| Failed Verification: Processor Declined | 20 | 1.5% | 34 | 2.2% | +14 | +0.67pp |
| Failed Verification: Declined | 23 | 1.7% | 32 | 2.1% | +9 | +0.31pp |
| Failed Verification: Cannot Authorize at this time (Policy) | 31 | 2.4% | 22 | 1.4% | -9 | -0.94pp |
| **Total PVS Failures** | **1,315** | **100%** | **1,554** | **100%** | **+239** | - |

---


---

*Report: 2026-05-12*
