# PCR Investigation: HF-NA 2026-W12

**Metric:** Payment Conversion Rate  
**Period:** 2026-W11 → 2026-W12  
**Observation:** 27.80% → 28.35% (+0.55pp)  
**Volume:** 61,825 payment visits  
**Threshold:** +0.27pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate improved by +0.55pp (27.80% → 28.35%) in 2026-W12, driven primarily by gains in frontend form submission and validation steps, despite an overall decline in payment visit volume (-7.8%).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | vs threshold ±0.27pp | -0.73pp | ⚠️ |
| Click Submit Form | vs threshold ±0.27pp | +1.58pp | ⚠️ |
| FE Validation Passed | vs threshold ±0.27pp | +1.38pp | ⚠️ |
| Enter Fraud Service | vs threshold ±0.27pp | +0.16pp | ✅ |
| Approved by Fraud Service | vs threshold ±0.27pp | +0.15pp | ✅ |
| Call to PVS | vs threshold ±0.27pp | -0.04pp | ✅ |
| Successful Checkout | vs threshold ±0.27pp | -0.02pp | ✅ |

**Key Findings:**
- **Click Submit Form** conversion improved significantly (+1.58pp), indicating users who select a payment method are more likely to proceed with submission
- **FE Validation Passed** improved by +1.38pp, supported by a higher error recovery rate (66.60% → 70.19%, +3.59pp) and a notable decrease in CC_NO_PREPAID_ERR occurrences (-3.13pp share reduction)
- **Canada outperformed US** with +1.19pp PCR improvement vs +0.34pp, driven by FE Validation gains (+1.46pp) in Canada
- **Select Payment Method declined** (-0.73pp), suggesting fewer visitors are initiating the payment flow despite better downstream conversion
- **ProcessOut_CreditCard** increased its volume share and improved success rate (+0.53pp to 83.25%), while Braintree_CreditCard declined in both volume and rate (-1.78pp)

**Action:** Monitor — The overall PCR improvement is positive and driven by legitimate funnel improvements. Continue tracking the Select Payment Method decline and Braintree_CreditCard performance to ensure they don't offset future gains.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 67,040 | 61,825 | -5,215 | -7.8% | - | - | - |
| Select Payment Method | 28,750 | 26,062 | -2,688 | -9.3% | 42.88% | 42.15% | -0.73pp |
| Click Submit Form | 23,411 | 21,633 | -1,778 | -7.6% | 81.43% | 83.01% | +1.58pp |
| FE Validation Passed | 21,680 | 20,333 | -1,347 | -6.2% | 92.61% | 93.99% | +1.38pp |
| Enter Fraud Service | 21,166 | 19,884 | -1,282 | -6.1% | 97.63% | 97.79% | +0.16pp |
| Approved by Fraud Service | 19,846 | 18,674 | -1,172 | -5.9% | 93.76% | 93.91% | +0.15pp |
| Call to PVS | 19,734 | 18,562 | -1,172 | -5.9% | 99.44% | 99.40% | -0.04pp |
| **Successful Checkout** | 18,638 | 17,527 | -1,111 | -6.0% | 94.45% | 94.42% | -0.02pp |
| **PCR Rate** | | | | | 27.80% | 28.35% | **+0.55pp** |

### Waterfall Backend

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 75,949 | 68,668 | -7,281 | -9.6% | - | - | - |
| Checkout Attempt | 27,130 | 25,136 | -1,994 | -7.3% | 35.72% | 36.61% | +0.88pp |
| Enter Fraud Service | 27,070 | 25,260 | -1,810 | -6.7% | 99.78% | 100.49% | +0.71pp |
| Approved by Fraud Service | 24,491 | 22,879 | -1,612 | -6.6% | 90.47% | 90.57% | +0.10pp |
| PVS Attempt | 22,919 | 21,127 | -1,792 | -7.8% | 93.58% | 92.34% | -1.24pp |
| PVS Success | 21,580 | 19,899 | -1,681 | -7.8% | 94.16% | 94.19% | +0.03pp |
| **Successful Checkout** | 22,221 | 20,526 | -1,695 | -7.6% | 102.97% | 103.15% | +0.18pp |
| **PCR Rate** | | | | | 29.26% | 29.89% | **+0.63pp** |

### Payment Method Breakdown

| Payment Method | 2026-W11 Attempt | 2026-W11 Success | 2026-W11 Rate | 2026-W12 Attempt | 2026-W12 Success | 2026-W12 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 10,007 | 8,278 | 82.72% | 11,105 | 9,245 | 83.25% | +0.53pp |
| Braintree_ApplePay | 8,301 | 6,499 | 78.29% | 7,668 | 5,972 | 77.88% | -0.41pp |
| Braintree_CreditCard | 5,630 | 4,762 | 84.58% | 3,268 | 2,706 | 82.80% | -1.78pp |
| Braintree_Paypal | 2,253 | 1,938 | 86.02% | 2,086 | 1,796 | 86.10% | +0.08pp |
| Adyen_CreditCard | 845 | 743 | 87.93% | 889 | 806 | 90.66% | +2.73pp |
|  | 93 | 0 | 0.00% | 119 | 0 | 0.00% | +0.00pp |
| Braintree_Venmo | 1 | 1 | 100.00% | 1 | 1 | 100.00% | +0.00pp |
| ApplePay | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |
| CreditCard | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |
| Paypal | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (2 countries in HF-NA)

| Country | Volume | PCR 2026-W11 | PCR 2026-W12 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| CA | 15,381 | 33.70% | 34.89% | +1.19pp | 1 | 1 |
| US | 46,444 | 25.84% | 26.18% | +0.34pp | 2 | 2 |

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

### CA

#### Waterfall GA

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 16,700 | 15,381 | -1,319 | -7.90pp | - | - | - |
| Select Payment Method | 8,586 | 8,006 | -580 | -6.76pp | 51.41% | 52.05% | +0.64pp |
| Click Submit Form | 6,908 | 6,449 | -459 | -6.64pp | 80.46% | 80.55% | +0.10pp |
| FE Validation Passed | 6,415 | 6,083 | -332 | -5.18pp | 92.86% | 94.32% | +1.46pp |
| Enter Fraud Service | 6,245 | 5,946 | -299 | -4.79pp | 97.35% | 97.75% | +0.40pp |
| Approved by Fraud Service | 5,836 | 5,572 | -264 | -4.52pp | 93.45% | 93.71% | +0.26pp |
| Call to PVS | 5,731 | 5,480 | -251 | -4.38pp | 98.20% | 98.35% | +0.15pp |
| **Successful Checkout** | 5,628 | 5,367 | -261 | -4.64pp | 98.20% | 97.94% | -0.26pp |
| **PCR Rate** | | | | | 33.70% | 34.89% | **+1.19pp** |

**Key Driver:** FE Validation Passed (+1.46pp)

#### Waterfall Backend

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 19,707 | 17,805 | -1,902 | -9.65pp | - | - | - |
| Checkout Attempt | 7,824 | 7,384 | -440 | -5.62pp | 39.70% | 41.47% | +1.77pp |
| Enter Fraud Service | 7,830 | 7,543 | -287 | -3.67pp | 100.08% | 102.15% | +2.08pp |
| Approved by Fraud Service | 7,170 | 6,901 | -269 | -3.75pp | 91.57% | 91.49% | -0.08pp |
| PVS Attempt | 5,967 | 5,476 | -491 | -8.23pp | 83.22% | 79.35% | -3.87pp |
| PVS Success | 5,814 | 5,356 | -458 | -7.88pp | 97.44% | 97.81% | +0.37pp |
| **Successful Checkout** | 6,973 | 6,520 | -453 | -6.50pp | 119.93% | 121.73% | +1.80pp |

**Key Driver:** PVS Attempt (-3.87pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (+1.38pp) meets threshold (+0.27pp)

### Recovery Rate

| Metric | 2026-W11 | 2026-W12 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 5,743 | 4,948 | -795 |
| Error → Passed | 3,825 | 3,473 | -352 |
| **Recovery Rate** | **66.60%** | **70.19%** | **+3.59pp** |

### Error Type Distribution

| Error Type | 2026-W11 | 2026-W11 % | 2026-W12 | 2026-W12 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 3,085 | 53.7% | 2,657 | 53.7% | -0.02pp |
| terms_not_accepted | 2,323 | 40.4% | 2,074 | 41.9% | +1.47pp |
| PAYPAL_POPUP_CLOSED | 570 | 9.9% | 450 | 9.1% | -0.83pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 311 | 5.4% | 277 | 5.6% | +0.18pp |
| CC_NO_PREPAID_ERR | 470 | 8.2% | 250 | 5.1% | -3.13pp |
| CC_TOKENISE_ERR | 130 | 2.3% | 133 | 2.7% | +0.42pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 139 | 2.4% | 126 | 2.5% | +0.13pp |
| PAYPAL_TOKENISE_ERR | 49 | 0.9% | 53 | 1.1% | +0.22pp |
| APPLEPAY_MERCHANT_VALIDATION_ERR | 1 | 0.0% | 5 | 0.1% | +0.08pp |
| VENMO_TOKENISE_ERR | 0 | 0.0% | 1 | 0.0% | +0.02pp |


---


---

*Report: 2026-04-10*
