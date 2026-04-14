# PCR Investigation: RTE 2026-W15

**Metric:** Payment Conversion Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 39.36% → 45.60% (+6.24pp)  
**Volume:** 61,443 payment visits  
**Threshold:** +3.12pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate improved significantly from 39.36% to 45.60% (+6.24pp) in 2026-W15, exceeding the threshold of +3.12pp, driven primarily by substantial gains at the Select Payment Method step across all analyzed countries.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Δ > threshold | +6.34pp | ⚠️ |
| Click Submit Form | Δ > threshold | +1.51pp | ✅ |
| FE Validation Passed | Δ < threshold | +0.39pp | ✅ |
| Enter Fraud Service | Δ < threshold | +0.17pp | ✅ |
| Approved by Fraud Service | Δ < threshold | +0.06pp | ✅ |
| Call to PVS | Δ < threshold | +0.09pp | ✅ |
| Successful Checkout | Δ < threshold | +0.36pp | ✅ |

**Key Findings:**
- **Select Payment Method is the primary driver:** GA waterfall shows +6.34pp improvement at this step, accounting for the majority of the overall PCR gain
- **Consistent pattern across all countries:** TV (+14.35pp), CF (+12.83pp), YE (+12.41pp), and FJ (+3.66pp) all show Select Payment Method as the key driver in GA waterfall
- **Braintree_ApplePay and Adyen_CreditCard showed notable improvements:** +2.16pp and +1.10pp respectively in success rates
- **TV showed the largest PCR increase (+13.65pp)** despite small volume (511 visits), while FJ contributed most volume (40,918 visits) with +3.52pp improvement
- **Backend waterfall shows smaller gains (+0.68pp PCR)** compared to GA waterfall (+6.24pp), suggesting improvement concentrated in front-end user experience

**Action:** **Monitor** - The improvement appears to be a positive systemic change in the Select Payment Method step across multiple countries. Investigate what UX or technical changes were deployed in W15 that improved payment method selection rates. Continue monitoring to confirm the improvement is sustained.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 63,361 | 61,443 | -1,918 | -3.0% | - | - | - |
| Select Payment Method | 31,637 | 34,572 | 2,935 | 9.3% | 49.93% | 56.27% | +6.34pp |
| Click Submit Form | 28,501 | 31,667 | 3,166 | 11.1% | 90.09% | 91.60% | +1.51pp |
| FE Validation Passed | 27,689 | 30,888 | 3,199 | 11.6% | 97.15% | 97.54% | +0.39pp |
| Enter Fraud Service | 27,074 | 30,254 | 3,180 | 11.7% | 97.78% | 97.95% | +0.17pp |
| Approved by Fraud Service | 26,000 | 29,073 | 3,073 | 11.8% | 96.03% | 96.10% | +0.06pp |
| Call to PVS | 25,936 | 29,029 | 3,093 | 11.9% | 99.75% | 99.85% | +0.09pp |
| **Successful Checkout** | 24,939 | 28,019 | 3,080 | 12.4% | 96.16% | 96.52% | +0.36pp |
| **PCR Rate** | | | | | 39.36% | 45.60% | **+6.24pp** |

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
| FJ | 40,918 | 39.94% | 43.46% | +3.52pp | 1 | 7 |
| CF | 11,794 | 40.23% | 52.43% | +12.20pp | 2 | 3 |
| YE | 4,876 | 37.72% | 50.57% | +12.85pp | 3 | 2 |
| TV | 511 | 39.58% | 53.23% | +13.65pp | 5 | 1 |

---

### TV

#### Waterfall GA

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 518 | 511 | -7 | -1.35pp | - | - | - |
| Select Payment Method | 319 | 388 | +69 | +21.63pp | 61.58% | 75.93% | +14.35pp |
| Click Submit Form | 284 | 359 | +75 | +26.41pp | 89.03% | 92.53% | +3.50pp |
| FE Validation Passed | 279 | 354 | +75 | +26.88pp | 98.24% | 98.61% | +0.37pp |
| Enter Fraud Service | 277 | 351 | +74 | +26.71pp | 99.28% | 99.15% | -0.13pp |
| Approved by Fraud Service | 264 | 340 | +76 | +28.79pp | 95.31% | 96.87% | +1.56pp |
| Call to PVS | 264 | 342 | +78 | +29.55pp | 100.00% | 100.59% | +0.59pp |
| **Successful Checkout** | 205 | 272 | +67 | +32.68pp | 77.65% | 79.53% | +1.88pp |
| **PCR Rate** | | | | | 39.58% | 53.23% | **+13.65pp** |

**Key Driver:** Select Payment Method (+14.35pp)

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
| Payment Visits | 12,912 | 11,794 | -1,118 | -8.66pp | - | - | - |
| Select Payment Method | 6,510 | 7,460 | +950 | +14.59pp | 50.42% | 63.25% | +12.83pp |
| Click Submit Form | 5,852 | 6,906 | +1,054 | +18.01pp | 89.89% | 92.57% | +2.68pp |
| FE Validation Passed | 5,784 | 6,848 | +1,064 | +18.40pp | 98.84% | 99.16% | +0.32pp |
| Enter Fraud Service | 5,639 | 6,676 | +1,037 | +18.39pp | 97.49% | 97.49% | -0.00pp |
| Approved by Fraud Service | 5,375 | 6,377 | +1,002 | +18.64pp | 95.32% | 95.52% | +0.20pp |
| Call to PVS | 5,339 | 6,346 | +1,007 | +18.86pp | 99.33% | 99.51% | +0.18pp |
| **Successful Checkout** | 5,194 | 6,184 | +990 | +19.06pp | 97.28% | 97.45% | +0.16pp |
| **PCR Rate** | | | | | 40.23% | 52.43% | **+12.21pp** |

**Key Driver:** Select Payment Method (+12.83pp)

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
| Payment Visits | 5,231 | 4,876 | -355 | -6.79pp | - | - | - |
| Select Payment Method | 2,625 | 3,052 | +427 | +16.27pp | 50.18% | 62.59% | +12.41pp |
| Click Submit Form | 2,357 | 2,810 | +453 | +19.22pp | 89.79% | 92.07% | +2.28pp |
| FE Validation Passed | 2,324 | 2,780 | +456 | +19.62pp | 98.60% | 98.93% | +0.33pp |
| Enter Fraud Service | 2,208 | 2,655 | +447 | +20.24pp | 95.01% | 95.50% | +0.49pp |
| Approved by Fraud Service | 2,082 | 2,560 | +478 | +22.96pp | 94.29% | 96.42% | +2.13pp |
| Call to PVS | 2,065 | 2,548 | +483 | +23.39pp | 99.18% | 99.53% | +0.35pp |
| **Successful Checkout** | 1,973 | 2,466 | +493 | +24.99pp | 95.54% | 96.78% | +1.24pp |
| **PCR Rate** | | | | | 37.72% | 50.57% | **+12.86pp** |

**Key Driver:** Select Payment Method (+12.41pp)

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
| Payment Visits | 40,637 | 40,918 | +281 | +0.69pp | - | - | - |
| Select Payment Method | 19,973 | 21,608 | +1,635 | +8.19pp | 49.15% | 52.81% | +3.66pp |
| Click Submit Form | 18,161 | 19,777 | +1,616 | +8.90pp | 90.93% | 91.53% | +0.60pp |
| FE Validation Passed | 17,530 | 19,167 | +1,637 | +9.34pp | 96.53% | 96.92% | +0.39pp |
| Enter Fraud Service | 17,246 | 18,896 | +1,650 | +9.57pp | 98.38% | 98.59% | +0.21pp |
| Approved by Fraud Service | 16,698 | 18,230 | +1,532 | +9.17pp | 96.82% | 96.48% | -0.35pp |
| Call to PVS | 16,683 | 18,229 | +1,546 | +9.27pp | 99.91% | 99.99% | +0.08pp |
| **Successful Checkout** | 16,232 | 17,782 | +1,550 | +9.55pp | 97.30% | 97.55% | +0.25pp |
| **PCR Rate** | | | | | 39.94% | 43.46% | **+3.51pp** |

**Key Driver:** Select Payment Method (+3.66pp)

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

*Report: 2026-04-14*
