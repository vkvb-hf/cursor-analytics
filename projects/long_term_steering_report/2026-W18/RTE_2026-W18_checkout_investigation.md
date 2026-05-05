# PCR Investigation: RTE 2026-W18

**Metric:** Payment Conversion Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 39.46% → 37.88% (-1.57pp)  
**Volume:** 67,115 payment visits  
**Threshold:** +0.79pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined by -1.57pp (39.46% → 37.88%) in 2026-W18, driven primarily by upstream funnel drop-off at the payment method selection stage and downstream PVS success issues.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Δ > 0.79pp | -1.44pp | ⚠️ |
| Click Submit Form | Δ > 0.79pp | -0.66pp | ✅ |
| FE Validation Passed | Δ > 0.79pp | +0.16pp | ✅ |
| Enter Fraud Service | Δ > 0.79pp | -0.58pp | ✅ |
| Approved by Fraud Service | Δ > 0.79pp | +0.83pp | ⚠️ |
| Call to PVS | Δ > 0.79pp | -0.04pp | ✅ |
| Successful Checkout | Δ > 0.79pp | -0.75pp | ✅ |

**Key Findings:**
- **Select Payment Method** is the primary drop-off point in GA waterfall (-1.44pp), with YE showing the most severe decline (-5.54pp) and FJ contributing the largest absolute volume impact (-1.37pp)
- **YE** experienced the largest country-level PCR decline (-6.32pp), with issues across multiple funnel stages including checkout attempt (-2.90pp in backend) and successful checkout (-2.55pp in GA)
- **TV** showed significant PVS Success degradation (-3.39pp in backend) despite relatively small volume (561 visits), indicating potential payment processor issues
- **Fraud Service approval improved** (+0.83pp), meeting the threshold—this is a positive signal but warrants monitoring
- **Adyen_CreditCard** showed slight success rate decline (-0.45pp) and contributed 68.2% of the fraud service gap in W18

**Action:** Investigate — Focus on YE and TV markets to identify root cause of payment method selection drop-off and PVS success failures. Review any recent changes to payment page UX or PSP configurations in these regions.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 67,161 | 67,115 | -46 | -0.1% | - | - | - |
| Select Payment Method | 33,444 | 32,454 | -990 | -3.0% | 49.80% | 48.36% | -1.44pp |
| Click Submit Form | 30,142 | 29,035 | -1,107 | -3.7% | 90.13% | 89.47% | -0.66pp |
| FE Validation Passed | 29,453 | 28,419 | -1,034 | -3.5% | 97.71% | 97.88% | +0.16pp |
| Enter Fraud Service | 28,841 | 27,663 | -1,178 | -4.1% | 97.92% | 97.34% | -0.58pp |
| Approved by Fraud Service | 27,537 | 26,642 | -895 | -3.3% | 95.48% | 96.31% | +0.83pp |
| Call to PVS | 27,452 | 26,548 | -904 | -3.3% | 99.69% | 99.65% | -0.04pp |
| **Successful Checkout** | 26,499 | 25,426 | -1,073 | -4.0% | 96.53% | 95.77% | -0.75pp |
| **PCR Rate** | | | | | 39.46% | 37.88% | **-1.57pp** |

### Waterfall Backend

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 125,985 | 117,564 | -8,421 | -6.7% | - | - | - |
| Checkout Attempt | 45,942 | 43,278 | -2,664 | -5.8% | 36.47% | 36.81% | +0.35pp |
| Enter Fraud Service | 45,857 | 43,213 | -2,644 | -5.8% | 99.81% | 99.85% | +0.03pp |
| Approved by Fraud Service | 43,257 | 40,887 | -2,370 | -5.5% | 94.33% | 94.62% | +0.29pp |
| PVS Attempt | 42,589 | 40,202 | -2,387 | -5.6% | 98.46% | 98.32% | -0.13pp |
| PVS Success | 41,333 | 38,801 | -2,532 | -6.1% | 97.05% | 96.52% | -0.54pp |
| **Successful Checkout** | 42,145 | 39,682 | -2,463 | -5.8% | 101.96% | 102.27% | +0.31pp |
| **PCR Rate** | | | | | 33.45% | 33.75% | **+0.30pp** |

### Payment Method Breakdown

| Payment Method | 2026-W17 Attempt | 2026-W17 Success | 2026-W17 Rate | 2026-W18 Attempt | 2026-W18 Success | 2026-W18 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 18,689 | 17,267 | 92.39% | 17,733 | 16,355 | 92.23% | -0.16pp |
| Braintree_ApplePay | 10,861 | 9,956 | 91.67% | 9,801 | 9,003 | 91.86% | +0.19pp |
| Adyen_CreditCard | 9,814 | 8,863 | 90.31% | 9,721 | 8,735 | 89.86% | -0.45pp |
| Braintree_Paypal | 5,526 | 5,099 | 92.27% | 4,901 | 4,551 | 92.86% | +0.59pp |
| Adyen_IDeal | 622 | 575 | 92.44% | 710 | 657 | 92.54% | +0.09pp |
| Adyen_Klarna | 316 | 296 | 93.67% | 300 | 284 | 94.67% | +1.00pp |
| Braintree_CreditCard | 109 | 85 | 77.98% | 97 | 86 | 88.66% | +10.68pp |
| Braintree_Venmo | 4 | 4 | 100.00% | 11 | 11 | 100.00% | +0.00pp |
|  | 1 | 0 | 0.00% | 4 | 0 | 0.00% | +0.00pp |
| CreditCard | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (3 countries in RTE)

| Country | Volume | PCR 2026-W17 | PCR 2026-W18 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| FJ | 42,819 | 39.57% | 38.35% | -1.22pp | 1 | 5 |
| YE | 6,775 | 39.07% | 32.75% | -6.32pp | 2 | 1 |
| TV | 561 | 44.18% | 39.22% | -4.96pp | 4 | 2 |

---

### TV

#### Waterfall GA

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 550 | 561 | +11 | +2.00pp | - | - | - |
| Select Payment Method | 352 | 339 | -13 | -3.69pp | 64.00% | 60.43% | -3.57pp |
| Click Submit Form | 321 | 300 | -21 | -6.54pp | 91.19% | 88.50% | -2.70pp |
| FE Validation Passed | 313 | 298 | -15 | -4.79pp | 97.51% | 99.33% | +1.83pp |
| Enter Fraud Service | 309 | 296 | -13 | -4.21pp | 98.72% | 99.33% | +0.61pp |
| Approved by Fraud Service | 294 | 286 | -8 | -2.72pp | 95.15% | 96.62% | +1.48pp |
| Call to PVS | 294 | 284 | -10 | -3.40pp | 100.00% | 99.30% | -0.70pp |
| **Successful Checkout** | 243 | 220 | -23 | -9.47pp | 82.65% | 77.46% | -5.19pp |
| **PCR Rate** | | | | | 44.18% | 39.22% | **-4.97pp** |

**Key Driver:** Successful Checkout (-5.19pp)

#### Waterfall Backend

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 813 | 814 | +1 | +0.12pp | - | - | - |
| Checkout Attempt | 414 | 398 | -16 | -3.86pp | 50.92% | 48.89% | -2.03pp |
| Enter Fraud Service | 413 | 398 | -15 | -3.63pp | 99.76% | 100.00% | +0.24pp |
| Approved by Fraud Service | 390 | 373 | -17 | -4.36pp | 94.43% | 93.72% | -0.71pp |
| PVS Attempt | 388 | 371 | -17 | -4.38pp | 99.49% | 99.46% | -0.02pp |
| PVS Success | 329 | 302 | -27 | -8.21pp | 84.79% | 81.40% | -3.39pp |
| **Successful Checkout** | 386 | 369 | -17 | -4.40pp | 117.33% | 122.19% | +4.86pp |

**Key Driver:** Successful Checkout (+4.86pp)

---

### YE

#### Waterfall GA

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 6,276 | 6,775 | +499 | +7.95pp | - | - | - |
| Select Payment Method | 3,098 | 2,969 | -129 | -4.16pp | 49.36% | 43.82% | -5.54pp |
| Click Submit Form | 2,826 | 2,631 | -195 | -6.90pp | 91.22% | 88.62% | -2.60pp |
| FE Validation Passed | 2,781 | 2,595 | -186 | -6.69pp | 98.41% | 98.63% | +0.22pp |
| Enter Fraud Service | 2,656 | 2,446 | -210 | -7.91pp | 95.51% | 94.26% | -1.25pp |
| Approved by Fraud Service | 2,529 | 2,349 | -180 | -7.12pp | 95.22% | 96.03% | +0.82pp |
| Call to PVS | 2,517 | 2,339 | -178 | -7.07pp | 99.53% | 99.57% | +0.05pp |
| **Successful Checkout** | 2,452 | 2,219 | -233 | -9.50pp | 97.42% | 94.87% | -2.55pp |
| **PCR Rate** | | | | | 39.07% | 32.75% | **-6.32pp** |

**Key Driver:** Select Payment Method (-5.54pp)

#### Waterfall Backend

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 10,257 | 10,192 | -65 | -0.63pp | - | - | - |
| Checkout Attempt | 4,063 | 3,742 | -321 | -7.90pp | 39.61% | 36.72% | -2.90pp |
| Enter Fraud Service | 4,061 | 3,738 | -323 | -7.95pp | 99.95% | 99.89% | -0.06pp |
| Approved by Fraud Service | 3,848 | 3,499 | -349 | -9.07pp | 94.75% | 93.61% | -1.15pp |
| PVS Attempt | 3,649 | 3,291 | -358 | -9.81pp | 94.83% | 94.06% | -0.77pp |
| PVS Success | 3,559 | 3,167 | -392 | -11.01pp | 97.53% | 96.23% | -1.30pp |
| **Successful Checkout** | 3,767 | 3,391 | -376 | -9.98pp | 105.84% | 107.07% | +1.23pp |

**Key Driver:** Checkout Attempt (-2.90pp)

---

### FJ

#### Waterfall GA

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 44,013 | 42,819 | -1,194 | -2.71pp | - | - | - |
| Select Payment Method | 21,575 | 20,401 | -1,174 | -5.44pp | 49.02% | 47.64% | -1.37pp |
| Click Submit Form | 19,491 | 18,345 | -1,146 | -5.88pp | 90.34% | 89.92% | -0.42pp |
| FE Validation Passed | 18,952 | 17,837 | -1,115 | -5.88pp | 97.23% | 97.23% | -0.00pp |
| Enter Fraud Service | 18,661 | 17,486 | -1,175 | -6.30pp | 98.46% | 98.03% | -0.43pp |
| Approved by Fraud Service | 17,901 | 16,932 | -969 | -5.41pp | 95.93% | 96.83% | +0.90pp |
| Call to PVS | 17,874 | 16,887 | -987 | -5.52pp | 99.85% | 99.73% | -0.11pp |
| **Successful Checkout** | 17,418 | 16,423 | -995 | -5.71pp | 97.45% | 97.25% | -0.20pp |
| **PCR Rate** | | | | | 39.57% | 38.35% | **-1.22pp** |

**Key Driver:** Select Payment Method (-1.37pp)

#### Waterfall Backend

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 94,197 | 85,981 | -8,216 | -8.72pp | - | - | - |
| Checkout Attempt | 32,501 | 30,038 | -2,463 | -7.58pp | 34.50% | 34.94% | +0.43pp |
| Enter Fraud Service | 32,480 | 30,020 | -2,460 | -7.57pp | 99.94% | 99.94% | +0.00pp |
| Approved by Fraud Service | 30,814 | 28,615 | -2,199 | -7.14pp | 94.87% | 95.32% | +0.45pp |
| PVS Attempt | 30,705 | 28,528 | -2,177 | -7.09pp | 99.65% | 99.70% | +0.05pp |
| PVS Success | 29,921 | 27,725 | -2,196 | -7.34pp | 97.45% | 97.19% | -0.26pp |
| **Successful Checkout** | 30,059 | 27,810 | -2,249 | -7.48pp | 100.46% | 100.31% | -0.15pp |

**Key Driver:** Approved by Fraud Service (+0.45pp)

---



## Fraud Analysis

**Include reason:** Approved Δ (+0.83pp) meets threshold (+0.79pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W17 | 2026-W17 % | 2026-W18 | 2026-W18 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 45,942 | - | 43,278 | - | -2,664 | -5.8% |
| Enter Fraud Service | 45,857 | - | 43,213 | - | -2,644 | -5.8% |
| **Gap (Skipped)** | **85** | **0.19%** | **65** | **0.15%** | **-20** | **-0.03pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W17 Gap | 2026-W17 % | 2026-W18 Gap | 2026-W18 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Adyen_CreditCard | 61 | 72.6% | 45 | 68.2% | -16 | -4.44pp |
| ProcessOut_CreditCard | 9 | 10.7% | 9 | 13.6% | 0 | +2.92pp |
| Braintree_ApplePay | 5 | 6.0% | 8 | 12.1% | +3 | +6.17pp |
| Braintree_Paypal | 4 | 4.8% | 3 | 4.5% | -1 | -0.22pp |
| Adyen_IDeal | 0 | 0.0% | 1 | 1.5% | +1 | +1.52pp |
| Braintree_CreditCard | 5 | 6.0% | 0 | 0.0% | -5 | -5.95pp |
| **Total** | **84** | **100%** | **66** | **100%** | **-18** | - |

*% of Gap = Payment Method Gap / Total Gap*

---


---

*Report: 2026-05-05*
