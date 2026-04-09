# PCR Investigation: HF-NA 2026-W14

**Metric:** Payment Conversion Rate  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 28.63% → 27.96% (-0.68pp)  
**Volume:** 59,454 payment visits  
**Threshold:** +0.34pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined by -0.68pp (28.63% → 27.96%) in 2026-W14, driven primarily by drops in FE Validation Passed and early funnel engagement.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Δ ≥ -0.34pp? | -0.34pp | ⚠️ |
| Click Submit Form | Δ ≥ -0.34pp? | -0.40pp | ⚠️ |
| FE Validation Passed | Δ ≥ -0.34pp? | -0.68pp | ⚠️ |
| Enter Fraud Service | Δ ≥ -0.34pp? | -0.15pp | ✅ |
| Approved by Fraud Service | Δ ≥ -0.34pp? | -0.33pp | ✅ |
| Call to PVS | Δ ≥ -0.34pp? | -0.19pp | ✅ |
| Successful Checkout | Δ ≥ -0.34pp? | +0.29pp | ✅ |

**Key Findings:**
- **FE Validation Passed is the largest single-step drop** at -0.68pp, with recovery rate declining from 72.25% to 70.06% (-2.19pp)
- **Canada drove the majority of PCR decline** with -1.77pp drop (34.16% → 32.39%), significantly worse than US at -0.36pp
- **APPLEPAY_DISMISSED errors increased** from 54.6% to 56.9% of FE errors (+2.33pp share), while terms_not_accepted decreased (-4.41pp share)
- **Backend shows Checkout Attempt drop of -1.14pp** (37.79% → 36.66%), indicating users are abandoning before attempting payment
- **Payment method performance improved** for top processors: ProcessOut_CreditCard (+1.69pp) and Braintree_ApplePay (+1.61pp), indicating the issue is upstream in the funnel

**Action:** **Investigate** - Focus on the FE Validation step, specifically the increase in APPLEPAY_DISMISSED errors and the significant drop in Canada's FE Validation Passed rate (-1.30pp). Review any recent changes to Apple Pay implementation or frontend validation logic deployed in W14.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 59,286 | 59,454 | 168 | 0.3% | - | - | - |
| Select Payment Method | 24,367 | 24,236 | -131 | -0.5% | 41.10% | 40.76% | -0.34pp |
| Click Submit Form | 20,847 | 20,638 | -209 | -1.0% | 85.55% | 85.15% | -0.40pp |
| FE Validation Passed | 19,788 | 19,450 | -338 | -1.7% | 94.92% | 94.24% | -0.68pp |
| Enter Fraud Service | 19,364 | 19,005 | -359 | -1.9% | 97.86% | 97.71% | -0.15pp |
| Approved by Fraud Service | 18,112 | 17,714 | -398 | -2.2% | 93.53% | 93.21% | -0.33pp |
| Call to PVS | 18,097 | 17,665 | -432 | -2.4% | 99.92% | 99.72% | -0.19pp |
| **Successful Checkout** | 16,975 | 16,621 | -354 | -2.1% | 93.80% | 94.09% | +0.29pp |
| **PCR Rate** | | | | | 28.63% | 27.96% | **-0.68pp** |

### Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 65,957 | 65,294 | -663 | -1.0% | - | - | - |
| Checkout Attempt | 24,928 | 23,935 | -993 | -4.0% | 37.79% | 36.66% | -1.14pp |
| Enter Fraud Service | 24,773 | 23,622 | -1,151 | -4.6% | 99.38% | 98.69% | -0.69pp |
| Approved by Fraud Service | 22,212 | 21,545 | -667 | -3.0% | 89.66% | 91.21% | +1.55pp |
| PVS Attempt | 20,751 | 20,221 | -530 | -2.6% | 93.42% | 93.85% | +0.43pp |
| PVS Success | 19,490 | 19,033 | -457 | -2.3% | 93.92% | 94.12% | +0.20pp |
| **Successful Checkout** | 20,042 | 19,496 | -546 | -2.7% | 102.83% | 102.43% | -0.40pp |
| **PCR Rate** | | | | | 30.39% | 29.86% | **-0.53pp** |

### Payment Method Breakdown

| Payment Method | 2026-W13 Attempt | 2026-W13 Success | 2026-W13 Rate | 2026-W14 Attempt | 2026-W14 Success | 2026-W14 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 14,991 | 12,281 | 81.92% | 13,953 | 11,666 | 83.61% | +1.69pp |
| Braintree_ApplePay | 7,428 | 5,796 | 78.03% | 7,371 | 5,870 | 79.64% | +1.61pp |
| Braintree_Paypal | 1,961 | 1,707 | 87.05% | 2,071 | 1,793 | 86.58% | -0.47pp |
| Adyen_CreditCard | 130 | 5 | 3.85% | 241 | 7 | 2.90% | -0.94pp |
| Braintree_CreditCard | 281 | 253 | 90.04% | 178 | 158 | 88.76% | -1.27pp |
|  | 136 | 0 | 0.00% | 120 | 1 | 0.83% | +0.83pp |
| Braintree_Venmo | 0 | 0 | 0.00% | 1 | 1 | 100.00% | +100.00pp |
| ApplePay | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |
| CreditCard | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |
| NoPayment | 1 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (2 countries in HF-NA)

| Country | Volume | PCR 2026-W13 | PCR 2026-W14 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| CA | 15,398 | 34.16% | 32.39% | -1.77pp | 1 | 1 |
| US | 44,056 | 26.77% | 26.41% | -0.36pp | 2 | 2 |

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

### CA

#### Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 14,916 | 15,398 | +482 | +3.23pp | - | - | - |
| Select Payment Method | 7,683 | 7,855 | +172 | +2.24pp | 51.51% | 51.01% | -0.50pp |
| Click Submit Form | 6,115 | 6,170 | +55 | +0.90pp | 79.59% | 78.55% | -1.04pp |
| FE Validation Passed | 5,794 | 5,766 | -28 | -0.48pp | 94.75% | 93.45% | -1.30pp |
| Enter Fraud Service | 5,650 | 5,579 | -71 | -1.26pp | 97.51% | 96.76% | -0.76pp |
| Approved by Fraud Service | 5,264 | 5,136 | -128 | -2.43pp | 93.17% | 92.06% | -1.11pp |
| Call to PVS | 5,245 | 5,113 | -132 | -2.52pp | 99.64% | 99.55% | -0.09pp |
| **Successful Checkout** | 5,096 | 4,987 | -109 | -2.14pp | 97.16% | 97.54% | +0.38pp |
| **PCR Rate** | | | | | 34.16% | 32.39% | **-1.78pp** |

**Key Driver:** FE Validation Passed (-1.30pp)

#### Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 17,128 | 17,502 | +374 | +2.18pp | - | - | - |
| Checkout Attempt | 7,126 | 6,986 | -140 | -1.96pp | 41.60% | 39.92% | -1.69pp |
| Enter Fraud Service | 7,126 | 6,951 | -175 | -2.46pp | 100.00% | 99.50% | -0.50pp |
| Approved by Fraud Service | 6,479 | 6,223 | -256 | -3.95pp | 90.92% | 89.53% | -1.39pp |
| PVS Attempt | 5,390 | 5,310 | -80 | -1.48pp | 83.19% | 85.33% | +2.14pp |
| PVS Success | 5,271 | 5,188 | -83 | -1.57pp | 97.79% | 97.70% | -0.09pp |
| **Successful Checkout** | 6,306 | 6,094 | -212 | -3.36pp | 119.64% | 117.46% | -2.17pp |

**Key Driver:** Successful Checkout (-2.17pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (-0.68pp) meets threshold (+0.34pp)

### Recovery Rate

| Metric | 2026-W13 | 2026-W14 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 4,587 | 4,519 | -68 |
| Error → Passed | 3,314 | 3,166 | -148 |
| **Recovery Rate** | **72.25%** | **70.06%** | **-2.19pp** |

### Error Type Distribution

| Error Type | 2026-W13 | 2026-W13 % | 2026-W14 | 2026-W14 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 2,505 | 54.6% | 2,573 | 56.9% | +2.33pp |
| terms_not_accepted | 2,064 | 45.0% | 1,834 | 40.6% | -4.41pp |
| PAYPAL_POPUP_CLOSED | 455 | 9.9% | 421 | 9.3% | -0.60pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 293 | 6.4% | 280 | 6.2% | -0.19pp |
| CC_TOKENISE_ERR | 158 | 3.4% | 149 | 3.3% | -0.15pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 123 | 2.7% | 120 | 2.7% | -0.03pp |
| PAYPAL_TOKENISE_ERR | 39 | 0.9% | 33 | 0.7% | -0.12pp |
| CC_NO_PREPAID_ERR | 2 | 0.0% | 2 | 0.0% | +0.00pp |
| EXPRESS_CHECKOUT_APPLEPAY_TOKENISE_ERR | 0 | 0.0% | 1 | 0.0% | +0.02pp |


---


---

*Report: 2026-04-09*
