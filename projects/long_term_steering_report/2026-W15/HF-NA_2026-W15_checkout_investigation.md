# PCR Investigation: HF-NA 2026-W15

**Metric:** Payment Conversion Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 27.96% → 27.99% (+0.03pp)  
**Volume:** 69,100 payment visits  
**Threshold:** +0.02pp (0.5 × |Overall PCR Δ|)

## Executive Summary

**Overall:** Payment Conversion Rate showed minimal improvement from 27.96% to 27.99% (+0.03pp) with volume increasing 16.2% to 69,100 payment visits.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ≥ threshold | +0.05pp | ✅ |
| Click Submit Form | ≥ threshold | +0.19pp | ✅ |
| FE Validation Passed | < threshold | -0.38pp | ⚠️ |
| Enter Fraud Service | ≥ threshold | +0.02pp | ✅ |
| Approved by Fraud Service | < threshold | -0.21pp | ⚠️ |
| Call to PVS | ≥ threshold | +0.28pp | ✅ |
| Successful Checkout | ≥ threshold | +0.09pp | ✅ |

**Key Findings:**
- CA drove positive performance with PCR improving +1.29pp (32.39% → 33.68%), primarily from Select Payment Method gains (+1.29pp) and Fraud Service approval improvements (+1.63pp in backend)
- US showed PCR decline of -0.17pp, with Fraud Service approval being the key driver (-0.71pp GA, -2.40pp backend)
- FE Validation recovery rate declined from 70.06% to 68.93% (-1.13pp), with "terms_not_accepted" errors increasing share (+1.28pp)
- Braintree_ApplePay conversion rate dropped -2.14pp (79.64% → 77.50%) and Braintree_CreditCard experienced significant decline of -13.31pp (88.76% → 75.45%)
- PVS failures increased by 186 cases (+19%), with "Insufficient Funds" errors growing in share (+2.26pp)

**Action:** Monitor - The overall PCR change is marginal (+0.03pp), but investigate the Fraud Service approval decline in US (-2.40pp backend) and monitor the Braintree_CreditCard conversion drop given its severity despite low volume.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 59,454 | 69,100 | 9,646 | 16.2% | - | - | - |
| Select Payment Method | 24,236 | 28,203 | 3,967 | 16.4% | 40.76% | 40.81% | +0.05pp |
| Click Submit Form | 20,638 | 24,069 | 3,431 | 16.6% | 85.15% | 85.34% | +0.19pp |
| FE Validation Passed | 19,450 | 22,592 | 3,142 | 16.2% | 94.24% | 93.86% | -0.38pp |
| Enter Fraud Service | 19,005 | 22,079 | 3,074 | 16.2% | 97.71% | 97.73% | +0.02pp |
| Approved by Fraud Service | 17,723 | 20,543 | 2,820 | 15.9% | 93.25% | 93.04% | -0.21pp |
| Call to PVS | 17,664 | 20,533 | 2,869 | 16.2% | 99.67% | 99.95% | +0.28pp |
| **Successful Checkout** | 16,621 | 19,340 | 2,719 | 16.4% | 94.10% | 94.19% | +0.09pp |
| **PCR Rate** | | | | | 27.96% | 27.99% | **+0.03pp** |

### Waterfall Backend

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 65,294 | 75,644 | 10,350 | 15.9% | - | - | - |
| Checkout Attempt | 23,935 | 28,054 | 4,119 | 17.2% | 36.66% | 37.09% | +0.43pp |
| Enter Fraud Service | 23,622 | 27,711 | 4,089 | 17.3% | 98.69% | 98.78% | +0.09pp |
| Approved by Fraud Service | 21,545 | 24,928 | 3,383 | 15.7% | 91.21% | 89.96% | -1.25pp |
| PVS Attempt | 20,221 | 23,512 | 3,291 | 16.3% | 93.85% | 94.32% | +0.46pp |
| PVS Success | 19,033 | 22,120 | 3,087 | 16.2% | 94.12% | 94.08% | -0.05pp |
| **Successful Checkout** | 19,496 | 22,541 | 3,045 | 15.6% | 102.43% | 101.90% | -0.53pp |
| **PCR Rate** | | | | | 29.86% | 29.80% | **-0.06pp** |

### Payment Method Breakdown

| Payment Method | 2026-W14 Attempt | 2026-W14 Success | 2026-W14 Rate | 2026-W15 Attempt | 2026-W15 Success | 2026-W15 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 13,953 | 11,666 | 83.61% | 16,642 | 13,764 | 82.71% | -0.90pp |
| Braintree_ApplePay | 7,371 | 5,870 | 79.64% | 8,572 | 6,643 | 77.50% | -2.14pp |
| Braintree_Paypal | 2,071 | 1,793 | 86.58% | 2,309 | 2,000 | 86.62% | +0.04pp |
| Adyen_CreditCard | 241 | 7 | 2.90% | 271 | 8 | 2.95% | +0.05pp |
| Braintree_CreditCard | 178 | 158 | 88.76% | 167 | 126 | 75.45% | -13.31pp |
|  | 120 | 1 | 0.83% | 93 | 0 | 0.00% | -0.83pp |
| Braintree_Venmo | 1 | 1 | 100.00% | 0 | 0 | 0.00% | -100.00pp |
| CreditCard | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (2 countries in HF-NA)

| Country | Volume | PCR 2026-W14 | PCR 2026-W15 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| CA | 16,237 | 32.39% | 33.68% | +1.29pp | 1 | 1 |
| US | 52,863 | 26.41% | 26.24% | -0.17pp | 2 | 2 |

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

### CA

#### Waterfall GA

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 15,398 | 16,237 | +839 | +5.45pp | - | - | - |
| Select Payment Method | 7,855 | 8,492 | +637 | +8.11pp | 51.01% | 52.30% | +1.29pp |
| Click Submit Form | 6,170 | 6,709 | +539 | +8.74pp | 78.55% | 79.00% | +0.46pp |
| FE Validation Passed | 5,766 | 6,271 | +505 | +8.76pp | 93.45% | 93.47% | +0.02pp |
| Enter Fraud Service | 5,579 | 6,081 | +502 | +9.00pp | 96.76% | 96.97% | +0.21pp |
| Approved by Fraud Service | 5,140 | 5,663 | +523 | +10.18pp | 92.13% | 93.13% | +0.99pp |
| Call to PVS | 5,113 | 5,638 | +525 | +10.27pp | 99.47% | 99.56% | +0.08pp |
| **Successful Checkout** | 4,987 | 5,468 | +481 | +9.65pp | 97.54% | 96.98% | -0.55pp |
| **PCR Rate** | | | | | 32.39% | 33.68% | **+1.29pp** |

**Key Driver:** Select Payment Method (+1.29pp)

#### Waterfall Backend

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 17,502 | 18,421 | +919 | +5.25pp | - | - | - |
| Checkout Attempt | 6,986 | 7,578 | +592 | +8.47pp | 39.92% | 41.14% | +1.22pp |
| Enter Fraud Service | 6,951 | 7,544 | +593 | +8.53pp | 99.50% | 99.55% | +0.05pp |
| Approved by Fraud Service | 6,223 | 6,877 | +654 | +10.51pp | 89.53% | 91.16% | +1.63pp |
| PVS Attempt | 5,310 | 5,843 | +533 | +10.04pp | 85.33% | 84.96% | -0.36pp |
| PVS Success | 5,188 | 5,685 | +497 | +9.58pp | 97.70% | 97.30% | -0.41pp |
| **Successful Checkout** | 6,094 | 6,723 | +629 | +10.32pp | 117.46% | 118.26% | +0.80pp |

**Key Driver:** Approved by Fraud Service (+1.63pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (-0.38pp) meets threshold (+0.02pp)

### Recovery Rate

| Metric | 2026-W14 | 2026-W15 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 4,519 | 5,439 | 920 |
| Error → Passed | 3,166 | 3,749 | 583 |
| **Recovery Rate** | **70.06%** | **68.93%** | **-1.13pp** |

### Error Type Distribution

| Error Type | 2026-W14 | 2026-W14 % | 2026-W15 | 2026-W15 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 2,573 | 56.9% | 3,097 | 56.9% | +0.00pp |
| terms_not_accepted | 1,834 | 40.6% | 2,277 | 41.9% | +1.28pp |
| PAYPAL_POPUP_CLOSED | 421 | 9.3% | 510 | 9.4% | +0.06pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 280 | 6.2% | 291 | 5.4% | -0.85pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 120 | 2.7% | 172 | 3.2% | +0.51pp |
| CC_TOKENISE_ERR | 149 | 3.3% | 161 | 3.0% | -0.34pp |
| PAYPAL_TOKENISE_ERR | 33 | 0.7% | 59 | 1.1% | +0.35pp |
| APPLEPAY_MERCHANT_VALIDATION_ERR | 0 | 0.0% | 1 | 0.0% | +0.02pp |
| CC_NO_PREPAID_ERR | 2 | 0.0% | 0 | 0.0% | -0.04pp |
| EXPRESS_CHECKOUT_APPLEPAY_TOKENISE_ERR | 1 | 0.0% | 0 | 0.0% | -0.02pp |


---

## Fraud Analysis

**Include reason:** Enter FS Δ (+0.02pp) meets threshold (+0.02pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W14 | 2026-W14 % | 2026-W15 | 2026-W15 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 23,935 | - | 28,054 | - | 4,119 | 17.2% |
| Enter Fraud Service | 23,622 | - | 27,711 | - | 4,089 | 17.3% |
| **Gap (Skipped)** | **313** | **1.31%** | **343** | **1.22%** | **30** | **-0.09pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W14 Gap | 2026-W14 % | 2026-W15 Gap | 2026-W15 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Adyen_CreditCard | 233 | 74.4% | 262 | 76.2% | +29 | +1.72pp |
| ProcessOut_CreditCard | 42 | 13.4% | 42 | 12.2% | 0 | -1.21pp |
| Braintree_ApplePay | 27 | 8.6% | 29 | 8.4% | +2 | -0.20pp |
| Braintree_Paypal | 11 | 3.5% | 9 | 2.6% | -2 | -0.90pp |
| Braintree_CreditCard | 0 | 0.0% | 2 | 0.6% | +2 | +0.58pp |
| **Total** | **313** | **100%** | **344** | **100%** | **31** | - |

*% of Gap = Payment Method Gap / Total Gap*

---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (+0.09pp) meets threshold (+0.02pp)

| Decline Reason | 2026-W14 | 2026-W14 % | 2026-W15 | 2026-W15 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Blocked Verification: Payment method is blocked due to business reasons | 534 | 54.5% | 605 | 51.9% | +71 | -2.61pp |
| Failed Verification: Insufficient Funds | 177 | 18.1% | 237 | 20.3% | +60 | +2.26pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 69 | 7.0% | 71 | 6.1% | +2 | -0.95pp |
| Failed Verification: Card Issuer Declined CVV | 34 | 3.5% | 51 | 4.4% | +17 | +0.90pp |
| Failed Verification: Declined - Call Issuer | 42 | 4.3% | 44 | 3.8% | +2 | -0.51pp |
| Failed Verification: Issuer or Cardholder has put a restriction on the card | 33 | 3.4% | 39 | 3.3% | +6 | -0.02pp |
| Failed Verification: Processor Declined - Fraud Suspected | 30 | 3.1% | 36 | 3.1% | +6 | +0.03pp |
| Failed Verification: Processor Declined | 24 | 2.5% | 30 | 2.6% | +6 | +0.12pp |
| Failed Verification: Declined | 22 | 2.2% | 28 | 2.4% | +6 | +0.16pp |
| Failed Verification: Closed Card | 14 | 1.4% | 24 | 2.1% | +10 | +0.63pp |
| **Total PVS Failures** | **979** | **100%** | **1,165** | **100%** | **+186** | - |

---


---

*Report: 2026-04-17*
