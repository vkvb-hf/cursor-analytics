# PCR Investigation: RTE 2026-W13

**Metric:** Payment Conversion Rate  
**Period:** 2026-W12 → 2026-W13  
**Observation:** 38.63% → 37.81% (-0.82pp)  
**Volume:** 70,721 payment visits  
**Threshold:** +0.41pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined by -0.82pp (38.63% → 37.81%) in 2026-W13, driven primarily by a significant drop in the "Select Payment Method" step across major markets.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ⚠️ | -2.07pp | Exceeds threshold |
| Click Submit Form | ✅ | +1.55pp | Improved |
| FE Validation Passed | ✅ | -0.10pp | Within threshold |
| Enter Fraud Service | ✅ | -0.09pp | Within threshold |
| Approved by Fraud Service | ✅ | +0.29pp | Improved |
| Call to PVS | ✅ | +0.04pp | Within threshold |
| Successful Checkout | ✅ | +0.17pp | Improved |

**Key Findings:**
- **Primary driver:** "Select Payment Method" conversion dropped -2.07pp (50.25% → 48.18%), accounting for the majority of the PCR decline
- **Payment method degradation:** Braintree_ApplePay success rate fell -4.40pp (91.63% → 87.23%), and Braintree_CreditCard crashed -8.72pp (92.72% → 84.00%) with volume dropping from 4,329 to just 125 attempts
- **Geographic impact:** FJ (largest market) saw "Select Payment Method" drop -2.82pp; CF experienced -1.78pp decline at the same step
- **Positive outlier:** TO showed strong improvement with PCR +9.21pp, driven by "Select Payment Method" increasing +9.15pp
- **Backend stable:** Backend PCR remained nearly flat at -0.03pp, indicating the issue is concentrated in the frontend/user selection phase

**Action:** **Investigate** - The significant drop in "Select Payment Method" conversion combined with Braintree payment method degradation (especially the near-complete volume loss for Braintree_CreditCard) warrants immediate investigation into potential UI/UX changes, payment method availability issues, or Braintree integration problems.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 71,217 | 70,721 | -496 | -0.7% | - | - | - |
| Select Payment Method | 35,784 | 34,071 | -1,713 | -4.8% | 50.25% | 48.18% | -2.07pp |
| Click Submit Form | 31,362 | 30,388 | -974 | -3.1% | 87.64% | 89.19% | +1.55pp |
| FE Validation Passed | 30,646 | 29,663 | -983 | -3.2% | 97.72% | 97.61% | -0.10pp |
| Enter Fraud Service | 30,059 | 29,067 | -992 | -3.3% | 98.08% | 97.99% | -0.09pp |
| Approved by Fraud Service | 28,804 | 27,937 | -867 | -3.0% | 95.82% | 96.11% | +0.29pp |
| Call to PVS | 28,757 | 27,903 | -854 | -3.0% | 99.84% | 99.88% | +0.04pp |
| **Successful Checkout** | 27,509 | 26,739 | -770 | -2.8% | 95.66% | 95.83% | +0.17pp |
| **PCR Rate** | | | | | 38.63% | 37.81% | **-0.82pp** |

### Waterfall Backend

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 128,098 | 123,045 | -5,053 | -3.9% | - | - | - |
| Checkout Attempt | 46,864 | 45,411 | -1,453 | -3.1% | 36.58% | 36.91% | +0.32pp |
| Enter Fraud Service | 46,775 | 45,337 | -1,438 | -3.1% | 99.81% | 99.84% | +0.03pp |
| Approved by Fraud Service | 44,337 | 43,132 | -1,205 | -2.7% | 94.79% | 95.14% | +0.35pp |
| PVS Attempt | 44,209 | 42,897 | -1,312 | -3.0% | 99.71% | 99.46% | -0.26pp |
| PVS Success | 42,831 | 41,563 | -1,268 | -3.0% | 96.88% | 96.89% | +0.01pp |
| **Successful Checkout** | 43,161 | 41,426 | -1,735 | -4.0% | 100.77% | 99.67% | -1.10pp |
| **PCR Rate** | | | | | 33.69% | 33.67% | **-0.03pp** |

### Payment Method Breakdown

| Payment Method | 2026-W12 Attempt | 2026-W12 Success | 2026-W12 Rate | 2026-W13 Attempt | 2026-W13 Success | 2026-W13 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 14,520 | 13,475 | 92.80% | 17,491 | 16,234 | 92.81% | +0.01pp |
| Braintree_ApplePay | 11,001 | 10,080 | 91.63% | 11,367 | 9,915 | 87.23% | -4.40pp |
| Adyen_CreditCard | 10,383 | 9,471 | 91.22% | 9,936 | 9,111 | 91.70% | +0.48pp |
| Braintree_Paypal | 5,386 | 4,967 | 92.22% | 5,297 | 4,954 | 93.52% | +1.30pp |
| Adyen_IDeal | 803 | 736 | 91.66% | 809 | 756 | 93.45% | +1.79pp |
| Adyen_Klarna | 434 | 414 | 95.39% | 378 | 347 | 91.80% | -3.59pp |
| Braintree_CreditCard | 4,329 | 4,014 | 92.72% | 125 | 105 | 84.00% | -8.72pp |
|  | 4 | 0 | 0.00% | 4 | 0 | 0.00% | +0.00pp |
| Braintree_Venmo | 4 | 4 | 100.00% | 4 | 4 | 100.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (4 countries in RTE)

| Country | Volume | PCR 2026-W12 | PCR 2026-W13 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| FJ | 45,842 | 38.44% | 37.43% | -1.01pp | 1 | 8 |
| CF | 13,359 | 41.74% | 40.21% | -1.53pp | 2 | 7 |
| TO | 1,246 | 35.65% | 44.86% | +9.21pp | 4 | 1 |
| TV | 653 | 35.80% | 39.82% | +4.02pp | 7 | 2 |

---

### TV

#### Waterfall GA

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 743 | 653 | -90 | -12.11pp | - | - | - |
| Select Payment Method | 423 | 392 | -31 | -7.33pp | 56.93% | 60.03% | +3.10pp |
| Click Submit Form | 375 | 348 | -27 | -7.20pp | 88.65% | 88.78% | +0.12pp |
| FE Validation Passed | 373 | 348 | -25 | -6.70pp | 99.47% | 100.00% | +0.53pp |
| Enter Fraud Service | 370 | 347 | -23 | -6.22pp | 99.20% | 99.71% | +0.52pp |
| Approved by Fraud Service | 353 | 331 | -22 | -6.23pp | 95.41% | 95.39% | -0.02pp |
| Call to PVS | 354 | 332 | -22 | -6.21pp | 100.28% | 100.30% | +0.02pp |
| **Successful Checkout** | 266 | 260 | -6 | -2.26pp | 75.14% | 78.31% | +3.17pp |
| **PCR Rate** | | | | | 35.80% | 39.82% | **+4.02pp** |

**Key Driver:** Successful Checkout (+3.17pp)

#### Waterfall Backend

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 957 | 831 | -126 | -13.17pp | - | - | - |
| Checkout Attempt | 530 | 463 | -67 | -12.64pp | 55.38% | 55.72% | +0.33pp |
| Enter Fraud Service | 530 | 462 | -68 | -12.83pp | 100.00% | 99.78% | -0.22pp |
| Approved by Fraud Service | 494 | 431 | -63 | -12.75pp | 93.21% | 93.29% | +0.08pp |
| PVS Attempt | 493 | 433 | -60 | -12.17pp | 99.80% | 100.46% | +0.67pp |
| PVS Success | 403 | 374 | -29 | -7.20pp | 81.74% | 86.37% | +4.63pp |
| **Successful Checkout** | 488 | 431 | -57 | -11.68pp | 121.09% | 115.24% | -5.85pp |

**Key Driver:** Successful Checkout (-5.85pp)

---

### CF

#### Waterfall GA

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 13,036 | 13,359 | +323 | +2.48pp | - | - | - |
| Select Payment Method | 6,673 | 6,601 | -72 | -1.08pp | 51.19% | 49.41% | -1.78pp |
| Click Submit Form | 6,048 | 5,942 | -106 | -1.75pp | 90.63% | 90.02% | -0.62pp |
| FE Validation Passed | 5,980 | 5,901 | -79 | -1.32pp | 98.88% | 99.31% | +0.43pp |
| Enter Fraud Service | 5,857 | 5,781 | -76 | -1.30pp | 97.94% | 97.97% | +0.02pp |
| Approved by Fraud Service | 5,591 | 5,537 | -54 | -0.97pp | 95.46% | 95.78% | +0.32pp |
| Call to PVS | 5,586 | 5,541 | -45 | -0.81pp | 99.91% | 100.07% | +0.16pp |
| **Successful Checkout** | 5,441 | 5,371 | -70 | -1.29pp | 97.40% | 96.93% | -0.47pp |
| **PCR Rate** | | | | | 41.74% | 40.21% | **-1.53pp** |

**Key Driver:** Select Payment Method (-1.78pp)

#### Waterfall Backend

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 15,185 | 15,488 | +303 | +2.00pp | - | - | - |
| Checkout Attempt | 6,895 | 6,875 | -20 | -0.29pp | 45.41% | 44.39% | -1.02pp |
| Enter Fraud Service | 6,845 | 6,831 | -14 | -0.20pp | 99.27% | 99.36% | +0.09pp |
| Approved by Fraud Service | 6,457 | 6,481 | +24 | +0.37pp | 94.33% | 94.88% | +0.54pp |
| PVS Attempt | 6,436 | 6,455 | +19 | +0.30pp | 99.67% | 99.60% | -0.08pp |
| PVS Success | 6,327 | 6,333 | +6 | +0.09pp | 98.31% | 98.11% | -0.20pp |
| **Successful Checkout** | 6,387 | 6,404 | +17 | +0.27pp | 100.95% | 101.12% | +0.17pp |

**Key Driver:** Checkout Attempt (-1.02pp)

---

### FJ

#### Waterfall GA

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 46,294 | 45,842 | -452 | -0.98pp | - | - | - |
| Select Payment Method | 22,980 | 21,465 | -1,515 | -6.59pp | 49.64% | 46.82% | -2.82pp |
| Click Submit Form | 19,973 | 19,217 | -756 | -3.79pp | 86.91% | 89.53% | +2.61pp |
| FE Validation Passed | 19,448 | 18,659 | -789 | -4.06pp | 97.37% | 97.10% | -0.28pp |
| Enter Fraud Service | 19,161 | 18,366 | -795 | -4.15pp | 98.52% | 98.43% | -0.09pp |
| Approved by Fraud Service | 18,463 | 17,731 | -732 | -3.96pp | 96.36% | 96.54% | +0.19pp |
| Call to PVS | 18,425 | 17,701 | -724 | -3.93pp | 99.79% | 99.83% | +0.04pp |
| **Successful Checkout** | 17,794 | 17,158 | -636 | -3.57pp | 96.58% | 96.93% | +0.36pp |
| **PCR Rate** | | | | | 38.44% | 37.43% | **-1.01pp** |

**Key Driver:** Select Payment Method (-2.82pp)

#### Waterfall Backend

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 95,268 | 90,783 | -4,485 | -4.71pp | - | - | - |
| Checkout Attempt | 32,366 | 31,262 | -1,104 | -3.41pp | 33.97% | 34.44% | +0.46pp |
| Enter Fraud Service | 32,330 | 31,237 | -1,093 | -3.38pp | 99.89% | 99.92% | +0.03pp |
| Approved by Fraud Service | 30,813 | 29,838 | -975 | -3.16pp | 95.31% | 95.52% | +0.21pp |
| PVS Attempt | 30,714 | 29,723 | -991 | -3.23pp | 99.68% | 99.61% | -0.06pp |
| PVS Success | 29,887 | 28,937 | -950 | -3.18pp | 97.31% | 97.36% | +0.05pp |
| **Successful Checkout** | 29,963 | 29,029 | -934 | -3.12pp | 100.25% | 100.32% | +0.06pp |

**Key Driver:** Checkout Attempt (+0.46pp)

---

### TO

#### Waterfall GA

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 1,122 | 1,246 | +124 | +11.05pp | - | - | - |
| Select Payment Method | 570 | 747 | +177 | +31.05pp | 50.80% | 59.95% | +9.15pp |
| Click Submit Form | 489 | 658 | +169 | +34.56pp | 85.79% | 88.09% | +2.30pp |
| FE Validation Passed | 465 | 626 | +161 | +34.62pp | 95.09% | 95.14% | +0.04pp |
| Enter Fraud Service | 447 | 614 | +167 | +37.36pp | 96.13% | 98.08% | +1.95pp |
| Approved by Fraud Service | 418 | 580 | +162 | +38.76pp | 93.51% | 94.46% | +0.95pp |
| Call to PVS | 420 | 580 | +160 | +38.10pp | 100.48% | 100.00% | -0.48pp |
| **Successful Checkout** | 400 | 559 | +159 | +39.75pp | 95.24% | 96.38% | +1.14pp |
| **PCR Rate** | | | | | 35.65% | 44.86% | **+9.21pp** |

**Key Driver:** Select Payment Method (+9.15pp)

#### Waterfall Backend

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 1,487 | 1,617 | +130 | +8.74pp | - | - | - |
| Checkout Attempt | 617 | 787 | +170 | +27.55pp | 41.49% | 48.67% | +7.18pp |
| Enter Fraud Service | 617 | 787 | +170 | +27.55pp | 100.00% | 100.00% | +0.00pp |
| Approved by Fraud Service | 569 | 731 | +162 | +28.47pp | 92.22% | 92.88% | +0.66pp |
| PVS Attempt | 569 | 731 | +162 | +28.47pp | 100.00% | 100.00% | +0.00pp |
| PVS Success | 548 | 710 | +162 | +29.56pp | 96.31% | 97.13% | +0.82pp |
| **Successful Checkout** | 557 | 716 | +159 | +28.55pp | 101.64% | 100.85% | -0.80pp |

**Key Driver:** Checkout Attempt (+7.18pp)

---





---

*Report: 2026-04-10*
