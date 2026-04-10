# PCR Investigation: RTE 2026-W12

**Metric:** Payment Conversion Rate  
**Period:** 2026-W11 → 2026-W12  
**Observation:** 44.03% → 38.63% (-5.41pp)  
**Volume:** 71,217 payment visits  
**Threshold:** +2.70pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined significantly from 44.03% to 38.63% (-5.41pp) in 2026-W12, exceeding the threshold of 2.70pp, with the primary degradation occurring at the Select Payment Method step.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | >2.70pp drop | -7.30pp | ⚠️ |
| Click Submit Form | Within threshold | +0.57pp | ✅ |
| FE Validation Passed | Within threshold | +0.43pp | ✅ |
| Enter Fraud Service | Within threshold | -0.16pp | ✅ |
| Approved by Fraud Service | Within threshold | -0.28pp | ✅ |
| Call to PVS | Within threshold | -0.04pp | ✅ |
| Successful Checkout | Within threshold | -0.13pp | ✅ |

**Key Findings:**
- The Select Payment Method step is the dominant driver of PCR decline, dropping -7.30pp globally (57.55% → 50.25%), indicating users are abandoning before selecting a payment option
- All four analyzed countries (FJ, CF, TZ, TV) show consistent degradation at Select Payment Method: FJ (-7.81pp), CF (-6.50pp), TZ (-9.59pp), TV (-11.79pp)
- Payment method mix shifted significantly: Braintree_CreditCard volume dropped from 15,448 to 4,329 attempts (-72%), while ProcessOut_CreditCard increased from 5,365 to 14,520 attempts (+171%)
- Despite volume increase (+5.8% payment visits), absolute successful checkouts decreased by 2,129 transactions
- Backend funnel shows smaller degradation (-0.69pp PCR) compared to GA (-5.41pp), suggesting the issue is primarily in the frontend user experience before checkout attempt

**Action:** **Investigate** - The consistent and severe drop at Select Payment Method across all countries indicates a potential frontend issue, UI/UX change, or payment method availability problem that requires immediate investigation. Review any deployments or configuration changes affecting the payment selection interface in W12.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 67,310 | 71,217 | 3,907 | 5.8% | - | - | - |
| Select Payment Method | 38,734 | 35,784 | -2,950 | -7.6% | 57.55% | 50.25% | -7.30pp |
| Click Submit Form | 33,728 | 31,362 | -2,366 | -7.0% | 87.08% | 87.64% | +0.57pp |
| FE Validation Passed | 32,812 | 30,646 | -2,166 | -6.6% | 97.28% | 97.72% | +0.43pp |
| Enter Fraud Service | 32,237 | 30,059 | -2,178 | -6.8% | 98.25% | 98.08% | -0.16pp |
| Approved by Fraud Service | 30,980 | 28,804 | -2,176 | -7.0% | 96.10% | 95.82% | -0.28pp |
| Call to PVS | 30,942 | 28,757 | -2,185 | -7.1% | 99.88% | 99.84% | -0.04pp |
| **Successful Checkout** | 29,638 | 27,509 | -2,129 | -7.2% | 95.79% | 95.66% | -0.13pp |
| **PCR Rate** | | | | | 44.03% | 38.63% | **-5.41pp** |

### Waterfall Backend

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 134,739 | 128,098 | -6,641 | -4.9% | - | - | - |
| Checkout Attempt | 49,986 | 46,864 | -3,122 | -6.2% | 37.10% | 36.58% | -0.51pp |
| Enter Fraud Service | 49,925 | 46,775 | -3,150 | -6.3% | 99.88% | 99.81% | -0.07pp |
| Approved by Fraud Service | 47,556 | 44,337 | -3,219 | -6.8% | 95.25% | 94.79% | -0.47pp |
| PVS Attempt | 47,403 | 44,209 | -3,194 | -6.7% | 99.68% | 99.71% | +0.03pp |
| PVS Success | 45,974 | 42,831 | -3,143 | -6.8% | 96.99% | 96.88% | -0.10pp |
| **Successful Checkout** | 46,328 | 43,161 | -3,167 | -6.8% | 100.77% | 100.77% | +0.00pp |
| **PCR Rate** | | | | | 34.38% | 33.69% | **-0.69pp** |

### Payment Method Breakdown

| Payment Method | 2026-W11 Attempt | 2026-W11 Success | 2026-W11 Rate | 2026-W12 Attempt | 2026-W12 Success | 2026-W12 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 5,365 | 4,958 | 92.41% | 14,520 | 13,475 | 92.80% | +0.39pp |
| Braintree_ApplePay | 11,787 | 10,871 | 92.23% | 11,001 | 10,080 | 91.63% | -0.60pp |
| Adyen_CreditCard | 10,448 | 9,473 | 90.67% | 10,383 | 9,471 | 91.22% | +0.55pp |
| Braintree_Paypal | 5,683 | 5,338 | 93.93% | 5,386 | 4,967 | 92.22% | -1.71pp |
| Braintree_CreditCard | 15,448 | 14,515 | 93.96% | 4,329 | 4,014 | 92.72% | -1.24pp |
| Adyen_IDeal | 841 | 786 | 93.46% | 803 | 736 | 91.66% | -1.80pp |
| Adyen_Klarna | 403 | 381 | 94.54% | 434 | 414 | 95.39% | +0.85pp |
|  | 5 | 0 | 0.00% | 4 | 0 | 0.00% | +0.00pp |
| Braintree_Venmo | 6 | 6 | 100.00% | 4 | 4 | 100.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (4 countries in RTE)

| Country | Volume | PCR 2026-W11 | PCR 2026-W12 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| FJ | 46,294 | 43.70% | 38.44% | -5.26pp | 1 | 5 |
| CF | 13,036 | 47.88% | 41.74% | -6.14pp | 2 | 4 |
| TZ | 1,443 | 34.31% | 22.52% | -11.79pp | 4 | 2 |
| TV | 743 | 49.05% | 35.80% | -13.25pp | 5 | 1 |

---

### TZ

#### Waterfall GA

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 1,189 | 1,443 | +254 | +21.36pp | - | - | - |
| Select Payment Method | 690 | 699 | +9 | +1.30pp | 58.03% | 48.44% | -9.59pp |
| Click Submit Form | 514 | 462 | -52 | -10.12pp | 74.49% | 66.09% | -8.40pp |
| FE Validation Passed | 483 | 416 | -67 | -13.87pp | 93.97% | 90.04% | -3.93pp |
| Enter Fraud Service | 449 | 375 | -74 | -16.48pp | 92.96% | 90.14% | -2.82pp |
| Approved by Fraud Service | 428 | 344 | -84 | -19.63pp | 95.32% | 91.73% | -3.59pp |
| Call to PVS | 432 | 343 | -89 | -20.60pp | 100.93% | 99.71% | -1.23pp |
| **Successful Checkout** | 408 | 325 | -83 | -20.34pp | 94.44% | 94.75% | +0.31pp |
| **PCR Rate** | | | | | 34.31% | 22.52% | **-11.79pp** |

**Key Driver:** Select Payment Method (-9.59pp)

#### Waterfall Backend

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 1,941 | 1,974 | +33 | +1.70pp | - | - | - |
| Checkout Attempt | 667 | 602 | -65 | -9.75pp | 34.36% | 30.50% | -3.87pp |
| Enter Fraud Service | 666 | 602 | -64 | -9.61pp | 99.85% | 100.00% | +0.15pp |
| Approved by Fraud Service | 614 | 531 | -83 | -13.52pp | 92.19% | 88.21% | -3.99pp |
| PVS Attempt | 613 | 530 | -83 | -13.54pp | 99.84% | 99.81% | -0.03pp |
| PVS Success | 593 | 515 | -78 | -13.15pp | 96.74% | 97.17% | +0.43pp |
| **Successful Checkout** | 596 | 518 | -78 | -13.09pp | 100.51% | 100.58% | +0.08pp |

**Key Driver:** Approved by Fraud Service (-3.99pp)

---

### TV

#### Waterfall GA

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 681 | 743 | +62 | +9.10pp | - | - | - |
| Select Payment Method | 468 | 423 | -45 | -9.62pp | 68.72% | 56.93% | -11.79pp |
| Click Submit Form | 432 | 375 | -57 | -13.19pp | 92.31% | 88.65% | -3.66pp |
| FE Validation Passed | 428 | 373 | -55 | -12.85pp | 99.07% | 99.47% | +0.39pp |
| Enter Fraud Service | 428 | 370 | -58 | -13.55pp | 100.00% | 99.20% | -0.80pp |
| Approved by Fraud Service | 411 | 353 | -58 | -14.11pp | 96.03% | 95.41% | -0.62pp |
| Call to PVS | 410 | 354 | -56 | -13.66pp | 99.76% | 100.28% | +0.53pp |
| **Successful Checkout** | 334 | 266 | -68 | -20.36pp | 81.46% | 75.14% | -6.32pp |
| **PCR Rate** | | | | | 49.05% | 35.80% | **-13.24pp** |

**Key Driver:** Select Payment Method (-11.79pp)

#### Waterfall Backend

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 982 | 957 | -25 | -2.55pp | - | - | - |
| Checkout Attempt | 549 | 530 | -19 | -3.46pp | 55.91% | 55.38% | -0.52pp |
| Enter Fraud Service | 549 | 530 | -19 | -3.46pp | 100.00% | 100.00% | +0.00pp |
| Approved by Fraud Service | 523 | 494 | -29 | -5.54pp | 95.26% | 93.21% | -2.06pp |
| PVS Attempt | 520 | 493 | -27 | -5.19pp | 99.43% | 99.80% | +0.37pp |
| PVS Success | 444 | 403 | -41 | -9.23pp | 85.38% | 81.74% | -3.64pp |
| **Successful Checkout** | 519 | 488 | -31 | -5.97pp | 116.89% | 121.09% | +4.20pp |

**Key Driver:** Successful Checkout (+4.20pp)

---

### CF

#### Waterfall GA

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 11,443 | 13,036 | +1,593 | +13.92pp | - | - | - |
| Select Payment Method | 6,601 | 6,673 | +72 | +1.09pp | 57.69% | 51.19% | -6.50pp |
| Click Submit Form | 6,090 | 6,048 | -42 | -0.69pp | 92.26% | 90.63% | -1.62pp |
| FE Validation Passed | 6,021 | 5,980 | -41 | -0.68pp | 98.87% | 98.88% | +0.01pp |
| Enter Fraud Service | 5,912 | 5,857 | -55 | -0.93pp | 98.19% | 97.94% | -0.25pp |
| Approved by Fraud Service | 5,633 | 5,591 | -42 | -0.75pp | 95.28% | 95.46% | +0.18pp |
| Call to PVS | 5,628 | 5,586 | -42 | -0.75pp | 99.91% | 99.91% | -0.00pp |
| **Successful Checkout** | 5,479 | 5,441 | -38 | -0.69pp | 97.35% | 97.40% | +0.05pp |
| **PCR Rate** | | | | | 47.88% | 41.74% | **-6.14pp** |

**Key Driver:** Select Payment Method (-6.50pp)

#### Waterfall Backend

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 15,214 | 15,185 | -29 | -0.19pp | - | - | - |
| Checkout Attempt | 7,033 | 6,895 | -138 | -1.96pp | 46.23% | 45.41% | -0.82pp |
| Enter Fraud Service | 7,000 | 6,845 | -155 | -2.21pp | 99.53% | 99.27% | -0.26pp |
| Approved by Fraud Service | 6,570 | 6,457 | -113 | -1.72pp | 93.86% | 94.33% | +0.47pp |
| PVS Attempt | 6,534 | 6,436 | -98 | -1.50pp | 99.45% | 99.67% | +0.22pp |
| PVS Success | 6,398 | 6,327 | -71 | -1.11pp | 97.92% | 98.31% | +0.39pp |
| **Successful Checkout** | 6,448 | 6,387 | -61 | -0.95pp | 100.78% | 100.95% | +0.17pp |

**Key Driver:** Checkout Attempt (-0.82pp)

---

### FJ

#### Waterfall GA

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 45,252 | 46,294 | +1,042 | +2.30pp | - | - | - |
| Select Payment Method | 25,996 | 22,980 | -3,016 | -11.60pp | 57.45% | 49.64% | -7.81pp |
| Click Submit Form | 22,142 | 19,973 | -2,169 | -9.80pp | 85.17% | 86.91% | +1.74pp |
| FE Validation Passed | 21,449 | 19,448 | -2,001 | -9.33pp | 96.87% | 97.37% | +0.50pp |
| Enter Fraud Service | 21,161 | 19,161 | -2,000 | -9.45pp | 98.66% | 98.52% | -0.13pp |
| Approved by Fraud Service | 20,466 | 18,463 | -2,003 | -9.79pp | 96.72% | 96.36% | -0.36pp |
| Call to PVS | 20,431 | 18,425 | -2,006 | -9.82pp | 99.83% | 99.79% | -0.03pp |
| **Successful Checkout** | 19,777 | 17,794 | -1,983 | -10.03pp | 96.80% | 96.58% | -0.22pp |
| **PCR Rate** | | | | | 43.70% | 38.44% | **-5.27pp** |

**Key Driver:** Select Payment Method (-7.81pp)

#### Waterfall Backend

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 101,601 | 95,268 | -6,333 | -6.23pp | - | - | - |
| Checkout Attempt | 35,271 | 32,366 | -2,905 | -8.24pp | 34.72% | 33.97% | -0.74pp |
| Enter Fraud Service | 35,248 | 32,330 | -2,918 | -8.28pp | 99.93% | 99.89% | -0.05pp |
| Approved by Fraud Service | 33,815 | 30,813 | -3,002 | -8.88pp | 95.93% | 95.31% | -0.63pp |
| PVS Attempt | 33,705 | 30,714 | -2,991 | -8.87pp | 99.67% | 99.68% | +0.00pp |
| PVS Success | 32,888 | 29,887 | -3,001 | -9.12pp | 97.58% | 97.31% | -0.27pp |
| **Successful Checkout** | 32,967 | 29,963 | -3,004 | -9.11pp | 100.24% | 100.25% | +0.01pp |

**Key Driver:** Checkout Attempt (-0.74pp)

---





---

*Report: 2026-04-10*
