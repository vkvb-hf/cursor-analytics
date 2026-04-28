# PCR Investigation: WL 2026-W17

**Metric:** Payment Conversion Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 35.83% → 32.05% (-3.78pp)  
**Volume:** 29,176 payment visits  
**Threshold:** +1.89pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined significantly from 35.83% to 32.05% (-3.78pp) in 2026-W17, with payment visits decreasing by 7.2% (29,176 visits).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | >1.89pp threshold | -3.27pp | ⚠️ |
| Click Submit Form | >1.89pp threshold | -2.31pp | ⚠️ |
| FE Validation Passed | Within threshold | +1.15pp | ✅ |
| Enter Fraud Service | Within threshold | -0.21pp | ✅ |
| Approved by Fraud Service | Within threshold | -1.12pp | ✅ |
| Call to PVS | Within threshold | -0.07pp | ✅ |
| Successful Checkout | Within threshold | -1.02pp | ✅ |

**Key Findings:**
- **Select Payment Method is the primary driver** of PCR decline across all analyzed countries: CG (-14.37pp), GN (-13.84pp), and ER (-7.69pp)
- **CG experienced the largest PCR drop** (-12.90pp, from 47.43% to 34.53%) despite a 7.48% increase in payment visits
- **Backend data shows contradictory trends**: Backend PCR remained stable (-0.13pp) while GA shows -3.78pp decline, and all payment methods show improved success rates (+9.33pp to +12.42pp)
- **Click Submit Form shows secondary degradation** (-2.31pp overall), with CG (-4.11pp), GN (-3.87pp), and ER (-4.16pp) all experiencing drops
- **Payment Method Listed increased 14.5%** in backend while Checkout Attempts remained flat (-0.2%), indicating users are seeing payment options but not initiating checkout

**Action:** **Investigate** - The significant drop in Select Payment Method conversion across all countries suggests a potential UI/UX issue, page load problem, or A/B test affecting the payment method selection step. Cross-reference with deployment logs and investigate the discrepancy between GA and Backend tracking.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 31,447 | 29,176 | -2,271 | -7.2% | - | - | - |
| Select Payment Method | 14,664 | 12,651 | -2,013 | -13.7% | 46.63% | 43.36% | -3.27pp |
| Click Submit Form | 13,440 | 11,303 | -2,137 | -15.9% | 91.65% | 89.34% | -2.31pp |
| FE Validation Passed | 12,772 | 10,871 | -1,901 | -14.9% | 95.03% | 96.18% | +1.15pp |
| Enter Fraud Service | 12,363 | 10,500 | -1,863 | -15.1% | 96.80% | 96.59% | -0.21pp |
| Approved by Fraud Service | 11,661 | 9,786 | -1,875 | -16.1% | 94.32% | 93.20% | -1.12pp |
| Call to PVS | 11,526 | 9,666 | -1,860 | -16.1% | 98.84% | 98.77% | -0.07pp |
| **Successful Checkout** | 11,269 | 9,352 | -1,917 | -17.0% | 97.77% | 96.75% | -1.02pp |
| **PCR Rate** | | | | | 35.83% | 32.05% | **-3.78pp** |

### Waterfall Backend

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 37,760 | 43,233 | 5,473 | 14.5% | - | - | - |
| Checkout Attempt | 14,419 | 14,388 | -31 | -0.2% | 38.19% | 33.28% | -4.91pp |
| Enter Fraud Service | 14,379 | 14,296 | -83 | -0.6% | 99.72% | 99.36% | -0.36pp |
| Approved by Fraud Service | 13,410 | 13,187 | -223 | -1.7% | 93.26% | 92.24% | -1.02pp |
| PVS Attempt | 11,024 | 10,957 | -67 | -0.6% | 82.21% | 83.09% | +0.88pp |
| PVS Success | 10,758 | 10,631 | -127 | -1.2% | 97.59% | 97.02% | -0.56pp |
| **Successful Checkout** | 11,173 | 12,736 | 1,563 | 14.0% | 103.86% | 119.80% | +15.94pp |
| **PCR Rate** | | | | | 29.59% | 29.46% | **-0.13pp** |

### Payment Method Breakdown

| Payment Method | 2026-W16 Attempt | 2026-W16 Success | 2026-W16 Rate | 2026-W17 Attempt | 2026-W17 Success | 2026-W17 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| Braintree_ApplePay | 4,252 | 3,340 | 78.55% | 4,095 | 3,684 | 89.96% | +11.41pp |
| ProcessOut_CreditCard | 4,032 | 3,087 | 76.56% | 3,893 | 3,417 | 87.77% | +11.21pp |
| Adyen_CreditCard | 2,766 | 2,146 | 77.58% | 2,743 | 2,384 | 86.91% | +9.33pp |
| Braintree_Paypal | 1,713 | 1,336 | 77.99% | 1,742 | 1,575 | 90.41% | +12.42pp |
| Braintree_CreditCard | 1,288 | 974 | 75.62% | 1,518 | 1,326 | 87.35% | +11.73pp |
| ProcessOut_ApplePay | 366 | 289 | 78.96% | 390 | 347 | 88.97% | +10.01pp |
| NoPayment | 1 | 0 | 0.00% | 4 | 0 | 0.00% | +0.00pp |
|  | 0 | 0 | 0.00% | 2 | 2 | 100.00% | +100.00pp |
| Braintree_Venmo | 1 | 1 | 100.00% | 1 | 1 | 100.00% | +0.00pp |
| CreditCard | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (3 countries in WL)

| Country | Volume | PCR 2026-W16 | PCR 2026-W17 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| CG | 4,165 | 47.43% | 34.53% | -12.90pp | 1 | 1 |
| ER | 4,734 | 40.71% | 31.94% | -8.77pp | 2 | 3 |
| GN | 2,325 | 50.25% | 39.40% | -10.85pp | 4 | 2 |

---

### ER

#### Waterfall GA

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 4,399 | 4,734 | +335 | +7.62pp | - | - | - |
| Select Payment Method | 2,352 | 2,167 | -185 | -7.87pp | 53.47% | 45.78% | -7.69pp |
| Click Submit Form | 2,186 | 1,924 | -262 | -11.99pp | 92.94% | 88.79% | -4.16pp |
| FE Validation Passed | 2,007 | 1,767 | -240 | -11.96pp | 91.81% | 91.84% | +0.03pp |
| Enter Fraud Service | 1,956 | 1,726 | -230 | -11.76pp | 97.46% | 97.68% | +0.22pp |
| Approved by Fraud Service | 1,864 | 1,610 | -254 | -13.63pp | 95.30% | 93.28% | -2.02pp |
| Call to PVS | 1,863 | 1,610 | -253 | -13.58pp | 99.95% | 100.00% | +0.05pp |
| **Successful Checkout** | 1,791 | 1,512 | -279 | -15.58pp | 96.14% | 93.91% | -2.22pp |
| **PCR Rate** | | | | | 40.71% | 31.94% | **-8.77pp** |

**Key Driver:** Select Payment Method (-7.69pp)

#### Waterfall Backend

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 6,413 | 7,418 | +1,005 | +15.67pp | - | - | - |
| Checkout Attempt | 2,420 | 2,424 | +4 | +0.17pp | 37.74% | 32.68% | -5.06pp |
| Enter Fraud Service | 2,418 | 2,424 | +6 | +0.25pp | 99.92% | 100.00% | +0.08pp |
| Approved by Fraud Service | 2,281 | 2,235 | -46 | -2.02pp | 94.33% | 92.20% | -2.13pp |
| PVS Attempt | 2,278 | 2,232 | -46 | -2.02pp | 99.87% | 99.87% | -0.00pp |
| PVS Success | 2,198 | 2,112 | -86 | -3.91pp | 96.49% | 94.62% | -1.86pp |
| **Successful Checkout** | 2,201 | 2,115 | -86 | -3.91pp | 100.14% | 100.14% | +0.01pp |

**Key Driver:** Checkout Attempt (-5.06pp)

---

### GN

#### Waterfall GA

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 2,422 | 2,325 | -97 | -4.00pp | - | - | - |
| Select Payment Method | 1,831 | 1,436 | -395 | -21.57pp | 75.60% | 61.76% | -13.84pp |
| Click Submit Form | 1,694 | 1,273 | -421 | -24.85pp | 92.52% | 88.65% | -3.87pp |
| FE Validation Passed | 1,371 | 1,057 | -314 | -22.90pp | 80.93% | 83.03% | +2.10pp |
| Enter Fraud Service | 1,303 | 1,001 | -302 | -23.18pp | 95.04% | 94.70% | -0.34pp |
| Approved by Fraud Service | 1,247 | 947 | -300 | -24.06pp | 95.70% | 94.61% | -1.10pp |
| Call to PVS | 1,243 | 943 | -300 | -24.14pp | 99.68% | 99.58% | -0.10pp |
| **Successful Checkout** | 1,217 | 916 | -301 | -24.73pp | 97.91% | 97.14% | -0.77pp |
| **PCR Rate** | | | | | 50.25% | 39.40% | **-10.85pp** |

**Key Driver:** Select Payment Method (-13.84pp)

#### Waterfall Backend

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 3,511 | 3,706 | +195 | +5.55pp | - | - | - |
| Checkout Attempt | 1,668 | 1,553 | -115 | -6.89pp | 47.51% | 41.91% | -5.60pp |
| Enter Fraud Service | 1,667 | 1,547 | -120 | -7.20pp | 99.94% | 99.61% | -0.33pp |
| Approved by Fraud Service | 1,580 | 1,463 | -117 | -7.41pp | 94.78% | 94.57% | -0.21pp |
| PVS Attempt | 1,329 | 1,218 | -111 | -8.35pp | 84.11% | 83.25% | -0.86pp |
| PVS Success | 1,300 | 1,183 | -117 | -9.00pp | 97.82% | 97.13% | -0.69pp |
| **Successful Checkout** | 1,566 | 1,447 | -119 | -7.60pp | 120.46% | 122.32% | +1.85pp |

**Key Driver:** Checkout Attempt (-5.60pp)

---

### CG

#### Waterfall GA

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 3,875 | 4,165 | +290 | +7.48pp | - | - | - |
| Select Payment Method | 2,360 | 1,938 | -422 | -17.88pp | 60.90% | 46.53% | -14.37pp |
| Click Submit Form | 2,200 | 1,727 | -473 | -21.50pp | 93.22% | 89.11% | -4.11pp |
| FE Validation Passed | 2,057 | 1,627 | -430 | -20.90pp | 93.50% | 94.21% | +0.71pp |
| Enter Fraud Service | 2,022 | 1,604 | -418 | -20.67pp | 98.30% | 98.59% | +0.29pp |
| Approved by Fraud Service | 1,884 | 1,482 | -402 | -21.34pp | 93.18% | 92.39% | -0.78pp |
| Call to PVS | 1,872 | 1,470 | -402 | -21.47pp | 99.36% | 99.19% | -0.17pp |
| **Successful Checkout** | 1,838 | 1,438 | -400 | -21.76pp | 98.18% | 97.82% | -0.36pp |
| **PCR Rate** | | | | | 47.43% | 34.53% | **-12.91pp** |

**Key Driver:** Select Payment Method (-14.37pp)

#### Waterfall Backend

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 5,332 | 6,100 | +768 | +14.40pp | - | - | - |
| Checkout Attempt | 2,257 | 2,158 | -99 | -4.39pp | 42.33% | 35.38% | -6.95pp |
| Enter Fraud Service | 2,254 | 2,152 | -102 | -4.53pp | 99.87% | 99.72% | -0.15pp |
| Approved by Fraud Service | 2,094 | 1,988 | -106 | -5.06pp | 92.90% | 92.38% | -0.52pp |
| PVS Attempt | 2,074 | 1,966 | -108 | -5.21pp | 99.04% | 98.89% | -0.15pp |
| PVS Success | 2,028 | 1,929 | -99 | -4.88pp | 97.78% | 98.12% | +0.34pp |
| **Successful Checkout** | 2,039 | 1,932 | -107 | -5.25pp | 100.54% | 100.16% | -0.39pp |

**Key Driver:** Checkout Attempt (-6.95pp)

---





---

*Report: 2026-04-28*
