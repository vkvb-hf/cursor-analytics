# PCR Investigation: WL 2026-W13

**Metric:** Payment Conversion Rate  
**Period:** 2026-W12 → 2026-W13  
**Observation:** 30.34% → 30.03% (-0.31pp)  
**Volume:** 38,531 payment visits  
**Threshold:** +0.15pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined by -0.31pp (30.34% → 30.03%) in 2026-W13, driven primarily by a significant drop in the Select Payment Method step (-0.49pp) and Fraud Service approval rate (-0.27pp).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Rate vs Prior Week | -0.49pp | ⚠️ |
| Click Submit Form | Rate vs Prior Week | +0.26pp | ✅ |
| FE Validation Passed | Rate vs Prior Week | +0.24pp | ✅ |
| Enter Fraud Service | Rate vs Prior Week | -0.22pp | ⚠️ |
| Approved by Fraud Service | Rate vs Prior Week | -0.27pp | ⚠️ |
| Call to PVS | Rate vs Prior Week | -0.04pp | ✅ |
| Successful Checkout | Rate vs Prior Week | +0.18pp | ✅ |

**Key Findings:**
- **GN country experienced severe PCR decline (-4.57pp)**, with Select Payment Method conversion dropping -3.90pp and FE Validation Passed dropping -3.79pp, making it the largest negative contributor
- **ProcessOut_CreditCard success rate declined -1.62pp** (91.85% → 90.23%), while ProcessOut_ApplePay dropped -3.29pp (88.21% → 84.91%), indicating potential issues with ProcessOut gateway
- **Fraud Service entry gap increased +0.12pp** (0.22% → 0.34%), with Braintree_CreditCard showing the largest increase in skipped transactions (+10 count, +12.65pp share)
- **CG country showed positive improvement (+1.68pp)** driven by Select Payment Method (+2.24pp), partially offsetting overall decline
- **PVS failures decreased by 18 total**, with "Insufficient Funds" declines dropping from 85 to 62 (-23 count), contributing to the +0.18pp improvement in Successful Checkout conversion

**Action:** Investigate — Focus on GN country's significant conversion drop at Select Payment Method and FE Validation steps, and examine ProcessOut gateway performance degradation across both CreditCard and ApplePay methods.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 40,203 | 38,531 | -1,672 | -4.2% | - | - | - |
| Select Payment Method | 16,655 | 15,773 | -882 | -5.3% | 41.43% | 40.94% | -0.49pp |
| Click Submit Form | 14,684 | 13,947 | -737 | -5.0% | 88.17% | 88.42% | +0.26pp |
| FE Validation Passed | 13,905 | 13,240 | -665 | -4.8% | 94.69% | 94.93% | +0.24pp |
| Enter Fraud Service | 13,379 | 12,710 | -669 | -5.0% | 96.22% | 96.00% | -0.22pp |
| Approved by Fraud Service | 12,697 | 12,028 | -669 | -5.3% | 94.90% | 94.63% | -0.27pp |
| Call to PVS | 12,677 | 12,004 | -673 | -5.3% | 99.84% | 99.80% | -0.04pp |
| **Successful Checkout** | 12,197 | 11,571 | -626 | -5.1% | 96.21% | 96.39% | +0.18pp |
| **PCR Rate** | | | | | 30.34% | 30.03% | **-0.31pp** |

### Waterfall Backend

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 48,081 | 46,082 | -1,999 | -4.2% | - | - | - |
| Checkout Attempt | 15,454 | 14,782 | -672 | -4.3% | 32.14% | 32.08% | -0.06pp |
| Enter Fraud Service | 15,420 | 14,732 | -688 | -4.5% | 99.78% | 99.66% | -0.12pp |
| Approved by Fraud Service | 14,468 | 13,771 | -697 | -4.8% | 93.83% | 93.48% | -0.35pp |
| PVS Attempt | 14,412 | 13,604 | -808 | -5.6% | 99.61% | 98.79% | -0.83pp |
| PVS Success | 13,963 | 13,206 | -757 | -5.4% | 96.88% | 97.07% | +0.19pp |
| **Successful Checkout** | 14,025 | 13,390 | -635 | -4.5% | 100.44% | 101.39% | +0.95pp |
| **PCR Rate** | | | | | 29.17% | 29.06% | **-0.11pp** |

### Payment Method Breakdown

| Payment Method | 2026-W12 Attempt | 2026-W12 Success | 2026-W12 Rate | 2026-W13 Attempt | 2026-W13 Success | 2026-W13 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| Braintree_ApplePay | 4,458 | 4,048 | 90.80% | 4,162 | 3,839 | 92.24% | +1.44pp |
| ProcessOut_CreditCard | 4,391 | 4,033 | 91.85% | 4,073 | 3,675 | 90.23% | -1.62pp |
| Adyen_CreditCard | 3,042 | 2,714 | 89.22% | 2,682 | 2,377 | 88.63% | -0.59pp |
| Braintree_Paypal | 1,899 | 1,743 | 91.79% | 1,850 | 1,704 | 92.11% | +0.32pp |
| Braintree_CreditCard | 1,270 | 1,143 | 90.00% | 1,602 | 1,445 | 90.20% | +0.20pp |
| ProcessOut_ApplePay | 390 | 344 | 88.21% | 411 | 349 | 84.91% | -3.29pp |
| NoPayment | 4 | 0 | 0.00% | 1 | 0 | 0.00% | +0.00pp |
| Braintree_Venmo | 0 | 0 | 0.00% | 1 | 1 | 100.00% | +100.00pp |
| CreditCard | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (2 countries in WL)

| Country | Volume | PCR 2026-W12 | PCR 2026-W13 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| GN | 2,988 | 37.37% | 32.80% | -4.57pp | 1 | 1 |
| CG | 5,715 | 30.69% | 32.37% | +1.68pp | 2 | 2 |

---

### GN

#### Waterfall GA

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 3,243 | 2,988 | -255 | -7.86pp | - | - | - |
| Select Payment Method | 1,952 | 1,682 | -270 | -13.83pp | 60.19% | 56.29% | -3.90pp |
| Click Submit Form | 1,737 | 1,480 | -257 | -14.80pp | 88.99% | 87.99% | -1.00pp |
| FE Validation Passed | 1,453 | 1,182 | -271 | -18.65pp | 83.65% | 79.86% | -3.79pp |
| Enter Fraud Service | 1,330 | 1,089 | -241 | -18.12pp | 91.53% | 92.13% | +0.60pp |
| Approved by Fraud Service | 1,262 | 1,027 | -235 | -18.62pp | 94.89% | 94.31% | -0.58pp |
| Call to PVS | 1,261 | 1,020 | -241 | -19.11pp | 99.92% | 99.32% | -0.60pp |
| **Successful Checkout** | 1,212 | 980 | -232 | -19.14pp | 96.11% | 96.08% | -0.04pp |
| **PCR Rate** | | | | | 37.37% | 32.80% | **-4.57pp** |

**Key Driver:** Select Payment Method (-3.90pp)

#### Waterfall Backend

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 4,199 | 3,823 | -376 | -8.95pp | - | - | - |
| Checkout Attempt | 1,712 | 1,446 | -266 | -15.54pp | 40.77% | 37.82% | -2.95pp |
| Enter Fraud Service | 1,708 | 1,439 | -269 | -15.75pp | 99.77% | 99.52% | -0.25pp |
| Approved by Fraud Service | 1,598 | 1,337 | -261 | -16.33pp | 93.56% | 92.91% | -0.65pp |
| PVS Attempt | 1,594 | 1,214 | -380 | -23.84pp | 99.75% | 90.80% | -8.95pp |
| PVS Success | 1,537 | 1,170 | -367 | -23.88pp | 96.42% | 96.38% | -0.05pp |
| **Successful Checkout** | 1,566 | 1,313 | -253 | -16.16pp | 101.89% | 112.22% | +10.34pp |

**Key Driver:** Successful Checkout (+10.34pp)

---

### CG

#### Waterfall GA

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 6,419 | 5,715 | -704 | -10.97pp | - | - | - |
| Select Payment Method | 2,679 | 2,513 | -166 | -6.20pp | 41.74% | 43.97% | +2.24pp |
| Click Submit Form | 2,317 | 2,185 | -132 | -5.70pp | 86.49% | 86.95% | +0.46pp |
| FE Validation Passed | 2,147 | 2,046 | -101 | -4.70pp | 92.66% | 93.64% | +0.98pp |
| Enter Fraud Service | 2,115 | 2,011 | -104 | -4.92pp | 98.51% | 98.29% | -0.22pp |
| Approved by Fraud Service | 2,032 | 1,908 | -124 | -6.10pp | 96.08% | 94.88% | -1.20pp |
| Call to PVS | 2,033 | 1,896 | -137 | -6.74pp | 100.05% | 99.37% | -0.68pp |
| **Successful Checkout** | 1,970 | 1,850 | -120 | -6.09pp | 96.90% | 97.57% | +0.67pp |
| **PCR Rate** | | | | | 30.69% | 32.37% | **+1.68pp** |

**Key Driver:** Select Payment Method (+2.24pp)

#### Waterfall Backend

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 7,400 | 6,538 | -862 | -11.65pp | - | - | - |
| Checkout Attempt | 2,369 | 2,245 | -124 | -5.23pp | 32.01% | 34.34% | +2.32pp |
| Enter Fraud Service | 2,362 | 2,237 | -125 | -5.29pp | 99.70% | 99.64% | -0.06pp |
| Approved by Fraud Service | 2,247 | 2,098 | -149 | -6.63pp | 95.13% | 93.79% | -1.34pp |
| PVS Attempt | 2,234 | 2,077 | -157 | -7.03pp | 99.42% | 99.00% | -0.42pp |
| PVS Success | 2,176 | 2,038 | -138 | -6.34pp | 97.40% | 98.12% | +0.72pp |
| **Successful Checkout** | 2,185 | 2,045 | -140 | -6.41pp | 100.41% | 100.34% | -0.07pp |

**Key Driver:** Checkout Attempt (+2.32pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (+0.24pp) meets threshold (+0.15pp)

### Recovery Rate

| Metric | 2026-W12 | 2026-W13 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 2,295 | 2,068 | -227 |
| Error → Passed | 1,363 | 1,209 | -154 |
| **Recovery Rate** | **59.39%** | **58.46%** | **-0.93pp** |

### Error Type Distribution

| Error Type | 2026-W12 | 2026-W12 % | 2026-W13 | 2026-W13 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 1,547 | 67.4% | 1,409 | 68.1% | +0.73pp |
| terms_not_accepted | 887 | 38.6% | 808 | 39.1% | +0.42pp |
| PAYPAL_POPUP_CLOSED | 376 | 16.4% | 283 | 13.7% | -2.70pp |
| CC_TOKENISE_ERR | 37 | 1.6% | 40 | 1.9% | +0.32pp |
| PAYPAL_TOKENISE_ERR | 30 | 1.3% | 32 | 1.5% | +0.24pp |
| APPLEPAY_TOKENISE_ERR | 1 | 0.0% | 0 | 0.0% | -0.04pp |


---

## Fraud Analysis

**Include reason:** Enter FS Δ (-0.22pp) meets threshold (+0.15pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W12 | 2026-W12 % | 2026-W13 | 2026-W13 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 15,454 | - | 14,782 | - | -672 | -4.3% |
| Enter Fraud Service | 15,420 | - | 14,732 | - | -688 | -4.5% |
| **Gap (Skipped)** | **34** | **0.22%** | **50** | **0.34%** | **16** | **+0.12pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W12 Gap | 2026-W12 % | 2026-W13 Gap | 2026-W13 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Braintree_CreditCard | 6 | 20.0% | 16 | 32.7% | +10 | +12.65pp |
| Braintree_Paypal | 4 | 13.3% | 10 | 20.4% | +6 | +7.07pp |
| Adyen_CreditCard | 5 | 16.7% | 8 | 16.3% | +3 | -0.34pp |
| Braintree_ApplePay | 4 | 13.3% | 8 | 16.3% | +4 | +2.99pp |
| ProcessOut_CreditCard | 11 | 36.7% | 7 | 14.3% | -4 | -22.38pp |
| **Total** | **30** | **100%** | **49** | **100%** | **19** | - |

*% of Gap = Payment Method Gap / Total Gap*

---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (+0.18pp) meets threshold (+0.15pp)

| Decline Reason | 2026-W12 | 2026-W12 % | 2026-W13 | 2026-W13 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Failed Verification: Insufficient Funds | 85 | 32.2% | 62 | 25.2% | -23 | -6.99pp |
| Blocked Verification: Payment method is blocked due to business reasons | 45 | 17.0% | 38 | 15.4% | -7 | -1.60pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 33 | 12.5% | 29 | 11.8% | -4 | -0.71pp |
| Failed Verification: Card Issuer Declined CVV | 16 | 6.1% | 25 | 10.2% | +9 | +4.10pp |
| Failed Verification: Processor Declined - Fraud Suspected | 22 | 8.3% | 20 | 8.1% | -2 | -0.20pp |
| Failed Verification: Refused(FRAUD) | 15 | 5.7% | 20 | 8.1% | +5 | +2.45pp |
| Failed Verification: Refused(Refused) | 12 | 4.5% | 14 | 5.7% | +2 | +1.15pp |
| Failed Verification: Cannot Authorize at this time (Policy) | 10 | 3.8% | 14 | 5.7% | +4 | +1.90pp |
| Failed Verification: Card Not Activated | 11 | 4.2% | 12 | 4.9% | +1 | +0.71pp |
| Failed Verification: Processor Declined | 15 | 5.7% | 12 | 4.9% | -3 | -0.80pp |
| **Total PVS Failures** | **264** | **100%** | **246** | **100%** | **-18** | - |

---


---

*Report: 2026-04-10*
