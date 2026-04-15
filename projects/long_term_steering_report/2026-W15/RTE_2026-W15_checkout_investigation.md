# PCR Investigation: RTE 2026-W15

**Metric:** Payment Conversion Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 39.36% → 45.59% (+6.23pp)  
**Volume:** 61,475 payment visits  
**Threshold:** +3.11pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate improved significantly from 39.36% to 45.59% (+6.23pp) in 2026-W15, exceeding the threshold of +3.11pp, driven primarily by a substantial increase in the Select Payment Method step.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Δ > 3.11pp | +6.32pp | ⚠️ |
| Click Submit Form | Δ > 3.11pp | +1.52pp | ✅ |
| FE Validation Passed | Δ > 3.11pp | +0.36pp | ✅ |
| Enter Fraud Service | Δ > 3.11pp | +0.17pp | ✅ |
| Approved by Fraud Service | Δ > 3.11pp | +0.09pp | ✅ |
| Call to PVS | Δ > 3.11pp | +0.07pp | ✅ |
| Successful Checkout | Δ > 3.11pp | +0.39pp | ✅ |

**Key Findings:**
- The Select Payment Method step is the primary driver of the PCR improvement, with conversion jumping from 49.93% to 56.25% (+6.32pp) at the global level
- All four analyzed countries (TV, CF, YE, FJ) show significant improvements in Select Payment Method conversion: TV +14.30pp, CF +12.81pp, YE +12.38pp, FJ +3.64pp
- Payment method performance is generally stable, with Braintree_ApplePay (+2.16pp), Adyen_IDeal (+2.28pp), and Adyen_Klarna (+2.06pp) showing notable improvements
- Backend waterfall shows minimal change in PCR (+0.68pp), suggesting the improvement is concentrated in the front-end user experience rather than backend processing
- Total payment visits decreased slightly (-3.0%) while successful checkouts increased (+12.4%), indicating improved conversion efficiency

**Action:** Monitor – The improvement appears to be a positive trend driven by improved user engagement at the payment method selection step. Investigate what changes may have been deployed affecting the payment selection UI/UX to document and potentially replicate this success.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 63,361 | 61,475 | -1,886 | -3.0% | - | - | - |
| Select Payment Method | 31,637 | 34,578 | 2,941 | 9.3% | 49.93% | 56.25% | +6.32pp |
| Click Submit Form | 28,501 | 31,675 | 3,174 | 11.1% | 90.09% | 91.60% | +1.52pp |
| FE Validation Passed | 27,689 | 30,888 | 3,199 | 11.6% | 97.15% | 97.52% | +0.36pp |
| Enter Fraud Service | 27,074 | 30,253 | 3,179 | 11.7% | 97.78% | 97.94% | +0.17pp |
| Approved by Fraud Service | 26,000 | 29,079 | 3,079 | 11.8% | 96.03% | 96.12% | +0.09pp |
| Call to PVS | 25,936 | 29,029 | 3,093 | 11.9% | 99.75% | 99.83% | +0.07pp |
| **Successful Checkout** | 24,939 | 28,026 | 3,087 | 12.4% | 96.16% | 96.54% | +0.39pp |
| **PCR Rate** | | | | | 39.36% | 45.59% | **+6.23pp** |

### Waterfall Backend

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 110,209 | 120,531 | 10,322 | 9.4% | - | - | - |
| Checkout Attempt | 42,850 | 47,320 | 4,470 | 10.4% | 38.88% | 39.26% | +0.38pp |
| Enter Fraud Service | 42,766 | 47,248 | 4,482 | 10.5% | 99.80% | 99.85% | +0.04pp |
| Approved by Fraud Service | 40,642 | 44,906 | 4,264 | 10.5% | 95.03% | 95.04% | +0.01pp |
| PVS Attempt | 39,914 | 44,168 | 4,254 | 10.7% | 98.21% | 98.36% | +0.15pp |
| PVS Success | 38,675 | 42,939 | 4,264 | 11.0% | 96.90% | 97.22% | +0.32pp |
| **Successful Checkout** | 38,814 | 43,273 | 4,459 | 11.5% | 100.36% | 100.78% | +0.42pp |
| **PCR Rate** | | | | | 35.22% | 35.90% | **+0.68pp** |

### Payment Method Breakdown

| Payment Method | 2026-W14 Attempt | 2026-W14 Success | 2026-W14 Rate | 2026-W15 Attempt | 2026-W15 Success | 2026-W15 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 17,123 | 15,943 | 93.11% | 18,823 | 17,485 | 92.89% | -0.22pp |
| Braintree_ApplePay | 10,528 | 9,003 | 85.51% | 11,163 | 9,787 | 87.67% | +2.16pp |
| Adyen_CreditCard | 9,248 | 8,384 | 90.66% | 10,764 | 9,877 | 91.76% | +1.10pp |
| Braintree_Paypal | 4,880 | 4,520 | 92.62% | 5,437 | 5,099 | 93.78% | +1.16pp |
| Adyen_IDeal | 676 | 610 | 90.24% | 628 | 581 | 92.52% | +2.28pp |
| Adyen_Klarna | 297 | 273 | 91.92% | 382 | 359 | 93.98% | +2.06pp |
| Braintree_CreditCard | 91 | 75 | 82.42% | 116 | 82 | 70.69% | -11.73pp |
| Braintree_Venmo | 6 | 6 | 100.00% | 4 | 3 | 75.00% | -25.00pp |
|  | 1 | 0 | 0.00% | 3 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (4 countries in RTE)

| Country | Volume | PCR 2026-W14 | PCR 2026-W15 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| CF | 11,806 | 40.23% | 52.41% | +12.18pp | 1 | 3 |
| FJ | 40,934 | 39.94% | 43.45% | +3.51pp | 2 | 7 |
| YE | 4,880 | 37.72% | 50.53% | +12.81pp | 3 | 2 |
| TV | 510 | 39.58% | 53.33% | +13.75pp | 5 | 1 |

---

### TV

#### Waterfall GA

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 518 | 510 | -8 | -1.54pp | - | - | - |
| Select Payment Method | 319 | 387 | +68 | +21.32pp | 61.58% | 75.88% | +14.30pp |
| Click Submit Form | 284 | 358 | +74 | +26.06pp | 89.03% | 92.51% | +3.48pp |
| FE Validation Passed | 279 | 353 | +74 | +26.52pp | 98.24% | 98.60% | +0.36pp |
| Enter Fraud Service | 277 | 350 | +73 | +26.35pp | 99.28% | 99.15% | -0.13pp |
| Approved by Fraud Service | 264 | 340 | +76 | +28.79pp | 95.31% | 97.14% | +1.84pp |
| Call to PVS | 264 | 342 | +78 | +29.55pp | 100.00% | 100.59% | +0.59pp |
| **Successful Checkout** | 205 | 272 | +67 | +32.68pp | 77.65% | 79.53% | +1.88pp |
| **PCR Rate** | | | | | 39.58% | 53.33% | **+13.76pp** |

**Key Driver:** Select Payment Method (+14.30pp)

#### Waterfall Backend

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 691 | 821 | +130 | +18.81pp | - | - | - |
| Checkout Attempt | 390 | 495 | +105 | +26.92pp | 56.44% | 60.29% | +3.85pp |
| Enter Fraud Service | 390 | 495 | +105 | +26.92pp | 100.00% | 100.00% | +0.00pp |
| Approved by Fraud Service | 364 | 476 | +112 | +30.77pp | 93.33% | 96.16% | +2.83pp |
| PVS Attempt | 363 | 476 | +113 | +31.13pp | 99.73% | 100.00% | +0.27pp |
| PVS Success | 307 | 400 | +93 | +30.29pp | 84.57% | 84.03% | -0.54pp |
| **Successful Checkout** | 362 | 475 | +113 | +31.22pp | 117.92% | 118.75% | +0.83pp |

**Key Driver:** Checkout Attempt (+3.85pp)

---

### CF

#### Waterfall GA

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 12,912 | 11,806 | -1,106 | -8.57pp | - | - | - |
| Select Payment Method | 6,510 | 7,465 | +955 | +14.67pp | 50.42% | 63.23% | +12.81pp |
| Click Submit Form | 5,852 | 6,910 | +1,058 | +18.08pp | 89.89% | 92.57% | +2.67pp |
| FE Validation Passed | 5,784 | 6,852 | +1,068 | +18.46pp | 98.84% | 99.16% | +0.32pp |
| Enter Fraud Service | 5,639 | 6,680 | +1,041 | +18.46pp | 97.49% | 97.49% | -0.00pp |
| Approved by Fraud Service | 5,375 | 6,383 | +1,008 | +18.75pp | 95.32% | 95.55% | +0.24pp |
| Call to PVS | 5,339 | 6,349 | +1,010 | +18.92pp | 99.33% | 99.47% | +0.14pp |
| **Successful Checkout** | 5,194 | 6,188 | +994 | +19.14pp | 97.28% | 97.46% | +0.18pp |
| **PCR Rate** | | | | | 40.23% | 52.41% | **+12.19pp** |

**Key Driver:** Select Payment Method (+12.81pp)

#### Waterfall Backend

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 15,500 | 16,978 | +1,478 | +9.54pp | - | - | - |
| Checkout Attempt | 6,695 | 7,874 | +1,179 | +17.61pp | 43.19% | 46.38% | +3.18pp |
| Enter Fraud Service | 6,633 | 7,837 | +1,204 | +18.15pp | 99.07% | 99.53% | +0.46pp |
| Approved by Fraud Service | 6,238 | 7,385 | +1,147 | +18.39pp | 94.04% | 94.23% | +0.19pp |
| PVS Attempt | 5,813 | 6,939 | +1,126 | +19.37pp | 93.19% | 93.96% | +0.77pp |
| PVS Success | 5,696 | 6,815 | +1,119 | +19.65pp | 97.99% | 98.21% | +0.23pp |
| **Successful Checkout** | 6,165 | 7,276 | +1,111 | +18.02pp | 108.23% | 106.76% | -1.47pp |

**Key Driver:** Checkout Attempt (+3.18pp)

---

### YE

#### Waterfall GA

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 5,231 | 4,880 | -351 | -6.71pp | - | - | - |
| Select Payment Method | 2,625 | 3,053 | +428 | +16.30pp | 50.18% | 62.56% | +12.38pp |
| Click Submit Form | 2,357 | 2,811 | +454 | +19.26pp | 89.79% | 92.07% | +2.28pp |
| FE Validation Passed | 2,324 | 2,781 | +457 | +19.66pp | 98.60% | 98.93% | +0.33pp |
| Enter Fraud Service | 2,208 | 2,655 | +447 | +20.24pp | 95.01% | 95.47% | +0.46pp |
| Approved by Fraud Service | 2,082 | 2,560 | +478 | +22.96pp | 94.29% | 96.42% | +2.13pp |
| Call to PVS | 2,065 | 2,548 | +483 | +23.39pp | 99.18% | 99.53% | +0.35pp |
| **Successful Checkout** | 1,973 | 2,466 | +493 | +24.99pp | 95.54% | 96.78% | +1.24pp |
| **PCR Rate** | | | | | 37.72% | 50.53% | **+12.82pp** |

**Key Driver:** Select Payment Method (+12.38pp)

#### Waterfall Backend

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 8,323 | 9,611 | +1,288 | +15.48pp | - | - | - |
| Checkout Attempt | 3,422 | 4,055 | +633 | +18.50pp | 41.11% | 42.19% | +1.08pp |
| Enter Fraud Service | 3,420 | 4,051 | +631 | +18.45pp | 99.94% | 99.90% | -0.04pp |
| Approved by Fraud Service | 3,205 | 3,862 | +657 | +20.50pp | 93.71% | 95.33% | +1.62pp |
| PVS Attempt | 3,000 | 3,655 | +655 | +21.83pp | 93.60% | 94.64% | +1.04pp |
| PVS Success | 2,899 | 3,559 | +660 | +22.77pp | 96.63% | 97.37% | +0.74pp |
| **Successful Checkout** | 3,110 | 3,774 | +664 | +21.35pp | 107.28% | 106.04% | -1.24pp |

**Key Driver:** Approved by Fraud Service (+1.62pp)

---

### FJ

#### Waterfall GA

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 40,637 | 40,934 | +297 | +0.73pp | - | - | - |
| Select Payment Method | 19,973 | 21,608 | +1,635 | +8.19pp | 49.15% | 52.79% | +3.64pp |
| Click Submit Form | 18,161 | 19,781 | +1,620 | +8.92pp | 90.93% | 91.54% | +0.62pp |
| FE Validation Passed | 17,530 | 19,163 | +1,633 | +9.32pp | 96.53% | 96.88% | +0.35pp |
| Enter Fraud Service | 17,246 | 18,892 | +1,646 | +9.54pp | 98.38% | 98.59% | +0.21pp |
| Approved by Fraud Service | 16,698 | 18,230 | +1,532 | +9.17pp | 96.82% | 96.50% | -0.33pp |
| Call to PVS | 16,683 | 18,226 | +1,543 | +9.25pp | 99.91% | 99.98% | +0.07pp |
| **Successful Checkout** | 16,232 | 17,785 | +1,553 | +9.57pp | 97.30% | 97.58% | +0.28pp |
| **PCR Rate** | | | | | 39.94% | 43.45% | **+3.50pp** |

**Key Driver:** Select Payment Method (+3.64pp)

#### Waterfall Backend

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 79,968 | 87,260 | +7,292 | +9.12pp | - | - | - |
| Checkout Attempt | 29,929 | 32,538 | +2,609 | +8.72pp | 37.43% | 37.29% | -0.14pp |
| Enter Fraud Service | 29,910 | 32,509 | +2,599 | +8.69pp | 99.94% | 99.91% | -0.03pp |
| Approved by Fraud Service | 28,651 | 31,016 | +2,365 | +8.25pp | 95.79% | 95.41% | -0.38pp |
| PVS Attempt | 28,555 | 30,930 | +2,375 | +8.32pp | 99.66% | 99.72% | +0.06pp |
| PVS Success | 27,820 | 30,227 | +2,407 | +8.65pp | 97.43% | 97.73% | +0.30pp |
| **Successful Checkout** | 27,885 | 30,296 | +2,411 | +8.65pp | 100.23% | 100.23% | -0.01pp |

**Key Driver:** Approved by Fraud Service (-0.38pp)

---





---

*Report: 2026-04-15*
