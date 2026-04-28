# PCR Investigation: RTE 2026-W17

**Metric:** Payment Conversion Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 48.92% → 40.13% (-8.79pp)  
**Volume:** 56,341 payment visits  
**Threshold:** +4.39pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined significantly from 48.92% to 40.13% (-8.79pp) in 2026-W17, driven primarily by a substantial drop in the Select Payment Method step across all analyzed countries.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Δ > 4.39pp | -9.27pp | ⚠️ |
| Click Submit Form | Δ > 4.39pp | -2.54pp | ✅ |
| FE Validation Passed | Δ > 4.39pp | +0.18pp | ✅ |
| Enter Fraud Service | Δ > 4.39pp | +0.06pp | ✅ |
| Approved by Fraud Service | Δ > 4.39pp | -0.46pp | ✅ |
| Call to PVS | Δ > 4.39pp | +0.01pp | ✅ |
| Successful Checkout | Δ > 4.39pp | +0.07pp | ✅ |

**Key Findings:**
- Select Payment Method is the primary bottleneck, dropping from 59.68% to 50.41% (-9.27pp) at the global level, exceeding the threshold significantly
- TT experienced the most severe decline with PCR dropping -18.51pp, driven by Select Payment Method conversion falling -20.35pp (72.21% → 51.86%)
- All four analyzed countries (FJ, CF, TT, TK) show consistent pattern: Select Payment Method is the key driver with declines ranging from -8.68pp to -20.35pp
- Backend data shows Payment Method Listed increased +21.2% while Checkout Attempt conversion dropped -9.20pp, indicating users are viewing payment options but not proceeding
- All payment methods show improved success rates (+10.50pp to +12.80pp) once users attempt checkout, confirming the issue is upstream at payment method selection

**Action:** Investigate - Urgent investigation required into Select Payment Method step. Focus on UI/UX changes, payment method availability, or technical issues preventing users from selecting payment methods. Prioritize TT and TK markets given their disproportionate impact.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 56,976 | 56,341 | -635 | -1.1% | - | - | - |
| Select Payment Method | 34,002 | 28,402 | -5,600 | -16.5% | 59.68% | 50.41% | -9.27pp |
| Click Submit Form | 31,624 | 25,693 | -5,931 | -18.8% | 93.01% | 90.46% | -2.54pp |
| FE Validation Passed | 30,859 | 25,119 | -5,740 | -18.6% | 97.58% | 97.77% | +0.18pp |
| Enter Fraud Service | 30,212 | 24,607 | -5,605 | -18.6% | 97.90% | 97.96% | +0.06pp |
| Approved by Fraud Service | 28,945 | 23,461 | -5,484 | -18.9% | 95.81% | 95.34% | -0.46pp |
| Call to PVS | 28,875 | 23,406 | -5,469 | -18.9% | 99.76% | 99.77% | +0.01pp |
| **Successful Checkout** | 27,872 | 22,609 | -5,263 | -18.9% | 96.53% | 96.59% | +0.07pp |
| **PCR Rate** | | | | | 48.92% | 40.13% | **-8.79pp** |

### Waterfall Backend

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 103,973 | 125,985 | 22,012 | 21.2% | - | - | - |
| Checkout Attempt | 47,481 | 45,942 | -1,539 | -3.2% | 45.67% | 36.47% | -9.20pp |
| Enter Fraud Service | 47,408 | 45,857 | -1,551 | -3.3% | 99.85% | 99.81% | -0.03pp |
| Approved by Fraud Service | 44,921 | 43,257 | -1,664 | -3.7% | 94.75% | 94.33% | -0.42pp |
| PVS Attempt | 44,111 | 42,589 | -1,522 | -3.5% | 98.20% | 98.46% | +0.26pp |
| PVS Success | 42,878 | 41,333 | -1,545 | -3.6% | 97.20% | 97.05% | -0.15pp |
| **Successful Checkout** | 37,717 | 42,145 | 4,428 | 11.7% | 87.96% | 101.96% | +14.00pp |
| **PCR Rate** | | | | | 36.28% | 33.45% | **-2.82pp** |

### Payment Method Breakdown

| Payment Method | 2026-W16 Attempt | 2026-W16 Success | 2026-W16 Rate | 2026-W17 Attempt | 2026-W17 Success | 2026-W17 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 18,972 | 15,100 | 79.59% | 18,689 | 17,267 | 92.39% | +12.80pp |
| Braintree_ApplePay | 10,851 | 8,619 | 79.43% | 10,861 | 9,956 | 91.67% | +12.24pp |
| Adyen_CreditCard | 10,595 | 8,335 | 78.67% | 9,814 | 8,863 | 90.31% | +11.64pp |
| Braintree_Paypal | 5,531 | 4,435 | 80.18% | 5,526 | 5,099 | 92.27% | +12.09pp |
| Adyen_IDeal | 1,060 | 863 | 81.42% | 622 | 575 | 92.44% | +11.03pp |
| Adyen_Klarna | 343 | 279 | 81.34% | 316 | 296 | 93.67% | +12.33pp |
| Braintree_CreditCard | 123 | 83 | 67.48% | 109 | 85 | 77.98% | +10.50pp |
| Braintree_Venmo | 3 | 3 | 100.00% | 4 | 4 | 100.00% | +0.00pp |
|  | 3 | 0 | 0.00% | 1 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (4 countries in RTE)

| Country | Volume | PCR 2026-W16 | PCR 2026-W17 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| FJ | 36,785 | 48.61% | 40.20% | -8.41pp | 1 | 6 |
| CF | 10,564 | 52.62% | 42.92% | -9.70pp | 2 | 5 |
| TT | 1,049 | 46.44% | 27.93% | -18.51pp | 4 | 1 |
| TK | 385 | 52.86% | 39.74% | -13.12pp | 6 | 2 |

---

### TT

#### Waterfall GA

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 1,432 | 1,049 | -383 | -26.75pp | - | - | - |
| Select Payment Method | 1,034 | 544 | -490 | -47.39pp | 72.21% | 51.86% | -20.35pp |
| Click Submit Form | 1,000 | 500 | -500 | -50.00pp | 96.71% | 91.91% | -4.80pp |
| FE Validation Passed | 1,000 | 504 | -496 | -49.60pp | 100.00% | 100.80% | +0.80pp |
| Enter Fraud Service | 995 | 502 | -493 | -49.55pp | 99.50% | 99.60% | +0.10pp |
| Approved by Fraud Service | 955 | 480 | -475 | -49.74pp | 95.98% | 95.62% | -0.36pp |
| Call to PVS | 957 | 479 | -478 | -49.95pp | 100.21% | 99.79% | -0.42pp |
| **Successful Checkout** | 665 | 293 | -372 | -55.94pp | 69.49% | 61.17% | -8.32pp |
| **PCR Rate** | | | | | 46.44% | 27.93% | **-18.51pp** |

**Key Driver:** Select Payment Method (-20.35pp)

#### Waterfall Backend

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 2,035 | 1,790 | -245 | -12.04pp | - | - | - |
| Checkout Attempt | 1,297 | 813 | -484 | -37.32pp | 63.73% | 45.42% | -18.32pp |
| Enter Fraud Service | 1,297 | 813 | -484 | -37.32pp | 100.00% | 100.00% | +0.00pp |
| Approved by Fraud Service | 1,224 | 749 | -475 | -38.81pp | 94.37% | 92.13% | -2.24pp |
| PVS Attempt | 1,223 | 745 | -478 | -39.08pp | 99.92% | 99.47% | -0.45pp |
| PVS Success | 985 | 570 | -415 | -42.13pp | 80.54% | 76.51% | -4.03pp |
| **Successful Checkout** | 1,221 | 744 | -477 | -39.07pp | 123.96% | 130.53% | +6.57pp |

**Key Driver:** Checkout Attempt (-18.32pp)

---

### TK

#### Waterfall GA

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 454 | 385 | -69 | -15.20pp | - | - | - |
| Select Payment Method | 306 | 202 | -104 | -33.99pp | 67.40% | 52.47% | -14.93pp |
| Click Submit Form | 282 | 186 | -96 | -34.04pp | 92.16% | 92.08% | -0.08pp |
| FE Validation Passed | 268 | 173 | -95 | -35.45pp | 95.04% | 93.01% | -2.02pp |
| Enter Fraud Service | 258 | 171 | -87 | -33.72pp | 96.27% | 98.84% | +2.58pp |
| Approved by Fraud Service | 244 | 155 | -89 | -36.48pp | 94.57% | 90.64% | -3.93pp |
| Call to PVS | 243 | 155 | -88 | -36.21pp | 99.59% | 100.00% | +0.41pp |
| **Successful Checkout** | 240 | 153 | -87 | -36.25pp | 98.77% | 98.71% | -0.06pp |
| **PCR Rate** | | | | | 52.86% | 39.74% | **-13.12pp** |

**Key Driver:** Select Payment Method (-14.93pp)

#### Waterfall Backend

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 721 | 792 | +71 | +9.85pp | - | - | - |
| Checkout Attempt | 375 | 318 | -57 | -15.20pp | 52.01% | 40.15% | -11.86pp |
| Enter Fraud Service | 374 | 318 | -56 | -14.97pp | 99.73% | 100.00% | +0.27pp |
| Approved by Fraud Service | 340 | 277 | -63 | -18.53pp | 90.91% | 87.11% | -3.80pp |
| PVS Attempt | 340 | 277 | -63 | -18.53pp | 100.00% | 100.00% | +0.00pp |
| PVS Success | 340 | 274 | -66 | -19.41pp | 100.00% | 98.92% | -1.08pp |
| **Successful Checkout** | 340 | 276 | -64 | -18.82pp | 100.00% | 100.73% | +0.73pp |

**Key Driver:** Checkout Attempt (-11.86pp)

---

### CF

#### Waterfall GA

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 11,194 | 10,564 | -630 | -5.63pp | - | - | - |
| Select Payment Method | 6,974 | 5,582 | -1,392 | -19.96pp | 62.30% | 52.84% | -9.46pp |
| Click Submit Form | 6,512 | 5,108 | -1,404 | -21.56pp | 93.38% | 91.51% | -1.87pp |
| FE Validation Passed | 6,440 | 5,071 | -1,369 | -21.26pp | 98.89% | 99.28% | +0.38pp |
| Enter Fraud Service | 6,300 | 4,950 | -1,350 | -21.43pp | 97.83% | 97.61% | -0.21pp |
| Approved by Fraud Service | 6,038 | 4,669 | -1,369 | -22.67pp | 95.84% | 94.32% | -1.52pp |
| Call to PVS | 6,010 | 4,641 | -1,369 | -22.78pp | 99.54% | 99.40% | -0.14pp |
| **Successful Checkout** | 5,890 | 4,534 | -1,356 | -23.02pp | 98.00% | 97.69% | -0.31pp |
| **PCR Rate** | | | | | 52.62% | 42.92% | **-9.70pp** |

**Key Driver:** Select Payment Method (-9.46pp)

#### Waterfall Backend

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 13,713 | 14,971 | +1,258 | +9.17pp | - | - | - |
| Checkout Attempt | 7,471 | 6,838 | -633 | -8.47pp | 54.48% | 45.67% | -8.81pp |
| Enter Fraud Service | 7,417 | 6,777 | -640 | -8.63pp | 99.28% | 99.11% | -0.17pp |
| Approved by Fraud Service | 7,002 | 6,282 | -720 | -10.28pp | 94.40% | 92.70% | -1.71pp |
| PVS Attempt | 6,546 | 5,929 | -617 | -9.43pp | 93.49% | 94.38% | +0.89pp |
| PVS Success | 6,455 | 5,812 | -643 | -9.96pp | 98.61% | 98.03% | -0.58pp |
| **Successful Checkout** | 6,951 | 6,195 | -756 | -10.88pp | 107.68% | 106.59% | -1.09pp |

**Key Driver:** Checkout Attempt (-8.81pp)

---

### FJ

#### Waterfall GA

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 36,171 | 36,785 | +614 | +1.70pp | - | - | - |
| Select Payment Method | 21,050 | 18,215 | -2,835 | -13.47pp | 58.20% | 49.52% | -8.68pp |
| Click Submit Form | 19,628 | 16,524 | -3,104 | -15.81pp | 93.24% | 90.72% | -2.53pp |
| FE Validation Passed | 19,081 | 16,082 | -2,999 | -15.72pp | 97.21% | 97.33% | +0.11pp |
| Enter Fraud Service | 18,778 | 15,836 | -2,942 | -15.67pp | 98.41% | 98.47% | +0.06pp |
| Approved by Fraud Service | 18,033 | 15,183 | -2,850 | -15.80pp | 96.03% | 95.88% | -0.16pp |
| Call to PVS | 17,998 | 15,167 | -2,831 | -15.73pp | 99.81% | 99.89% | +0.09pp |
| **Successful Checkout** | 17,581 | 14,789 | -2,792 | -15.88pp | 97.68% | 97.51% | -0.18pp |
| **PCR Rate** | | | | | 48.61% | 40.20% | **-8.40pp** |

**Key Driver:** Select Payment Method (-8.68pp)

#### Waterfall Backend

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 75,018 | 94,197 | +19,179 | +25.57pp | - | - | - |
| Checkout Attempt | 32,488 | 32,501 | +13 | +0.04pp | 43.31% | 34.50% | -8.80pp |
| Enter Fraud Service | 32,472 | 32,480 | +8 | +0.02pp | 99.95% | 99.94% | -0.02pp |
| Approved by Fraud Service | 30,882 | 30,814 | -68 | -0.22pp | 95.10% | 94.87% | -0.23pp |
| PVS Attempt | 30,779 | 30,705 | -74 | -0.24pp | 99.67% | 99.65% | -0.02pp |
| PVS Success | 30,067 | 29,921 | -146 | -0.49pp | 97.69% | 97.45% | -0.24pp |
| **Successful Checkout** | 30,170 | 30,059 | -111 | -0.37pp | 100.34% | 100.46% | +0.12pp |

**Key Driver:** Checkout Attempt (-8.80pp)

---





---

*Report: 2026-04-28*
