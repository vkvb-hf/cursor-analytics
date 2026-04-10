# PCR Investigation: WL 2026-W12

**Metric:** Payment Conversion Rate  
**Period:** 2026-W11 → 2026-W12  
**Observation:** 34.47% → 30.34% (-4.13pp)  
**Volume:** 40,203 payment visits  
**Threshold:** +2.07pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined significantly from 34.47% to 30.34% (-4.13pp) in 2026-W12, despite a 4.0% increase in payment visits volume (40,203 visits).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | >2.07pp threshold | -3.98pp | ⚠️ |
| Click Submit Form | >2.07pp threshold | -2.31pp | ⚠️ |
| FE Validation Passed | Within threshold | +0.15pp | ✅ |
| Enter Fraud Service | Within threshold | -0.23pp | ✅ |
| Approved by Fraud Service | Within threshold | -0.87pp | ✅ |
| Call to PVS | Within threshold | +0.04pp | ✅ |
| Successful Checkout | Within threshold | -0.04pp | ✅ |

**Key Findings:**
- **Select Payment Method is the primary bottleneck:** Conversion dropped -3.98pp at the global level, with country-level drops of -7.86pp (CG), -8.75pp (GN), and -5.91pp (ER) — all significantly exceeding the 2.07pp threshold
- **Click Submit Form shows secondary degradation:** -2.31pp globally, with CG experiencing the largest drop at -4.52pp and ER at -4.21pp
- **All major payment methods declined:** Adyen_CreditCard (-2.08pp), ProcessOut_ApplePay (-2.86pp), Braintree_ApplePay (-1.88pp), and Braintree_Paypal (-1.54pp) all showed decreased success rates
- **Backend data confirms frontend issues:** Checkout Attempt conversion dropped across all analyzed countries (CG: -0.74pp, ER: -1.50pp, GN: -0.69pp), indicating users are abandoning before initiating checkout
- **CG had the highest impact:** With -7.57pp PCR decline on 6,419 visits, CG contributed the most to the overall degradation

**Action:** **Investigate** — The consistent pattern of degradation at the Select Payment Method and Click Submit Form steps across all top countries suggests a potential UX/UI issue, page load problem, or payment method display issue introduced in W12 that requires immediate investigation.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 38,660 | 40,203 | 1,543 | 4.0% | - | - | - |
| Select Payment Method | 17,556 | 16,655 | -901 | -5.1% | 45.41% | 41.43% | -3.98pp |
| Click Submit Form | 15,884 | 14,684 | -1,200 | -7.6% | 90.48% | 88.17% | -2.31pp |
| FE Validation Passed | 15,017 | 13,905 | -1,112 | -7.4% | 94.54% | 94.69% | +0.15pp |
| Enter Fraud Service | 14,484 | 13,379 | -1,105 | -7.6% | 96.45% | 96.22% | -0.23pp |
| Approved by Fraud Service | 13,871 | 12,697 | -1,174 | -8.5% | 95.77% | 94.90% | -0.87pp |
| Call to PVS | 13,844 | 12,677 | -1,167 | -8.4% | 99.81% | 99.84% | +0.04pp |
| **Successful Checkout** | 13,326 | 12,197 | -1,129 | -8.5% | 96.26% | 96.21% | -0.04pp |
| **PCR Rate** | | | | | 34.47% | 30.34% | **-4.13pp** |

### Waterfall Backend

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 51,052 | 48,081 | -2,971 | -5.8% | - | - | - |
| Checkout Attempt | 16,808 | 15,454 | -1,354 | -8.1% | 32.92% | 32.14% | -0.78pp |
| Enter Fraud Service | 16,769 | 15,420 | -1,349 | -8.0% | 99.77% | 99.78% | +0.01pp |
| Approved by Fraud Service | 15,912 | 14,468 | -1,444 | -9.1% | 94.89% | 93.83% | -1.06pp |
| PVS Attempt | 15,835 | 14,412 | -1,423 | -9.0% | 99.52% | 99.61% | +0.10pp |
| PVS Success | 15,352 | 13,963 | -1,389 | -9.0% | 96.95% | 96.88% | -0.07pp |
| **Successful Checkout** | 15,455 | 14,025 | -1,430 | -9.3% | 100.67% | 100.44% | -0.23pp |
| **PCR Rate** | | | | | 30.27% | 29.17% | **-1.10pp** |

### Payment Method Breakdown

| Payment Method | 2026-W11 Attempt | 2026-W11 Success | 2026-W11 Rate | 2026-W12 Attempt | 2026-W12 Success | 2026-W12 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| Braintree_ApplePay | 4,757 | 4,409 | 92.68% | 4,458 | 4,048 | 90.80% | -1.88pp |
| ProcessOut_CreditCard | 4,652 | 4,284 | 92.09% | 4,391 | 4,033 | 91.85% | -0.24pp |
| Adyen_CreditCard | 3,538 | 3,230 | 91.29% | 3,042 | 2,714 | 89.22% | -2.08pp |
| Braintree_Paypal | 2,007 | 1,873 | 93.32% | 1,899 | 1,743 | 91.79% | -1.54pp |
| Braintree_CreditCard | 1,448 | 1,292 | 89.23% | 1,270 | 1,143 | 90.00% | +0.77pp |
| ProcessOut_ApplePay | 403 | 367 | 91.07% | 390 | 344 | 88.21% | -2.86pp |
| NoPayment | 3 | 0 | 0.00% | 4 | 0 | 0.00% | +0.00pp |
| CreditCard | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (3 countries in WL)

| Country | Volume | PCR 2026-W11 | PCR 2026-W12 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| CG | 6,419 | 38.26% | 30.69% | -7.57pp | 1 | 1 |
| ER | 8,303 | 33.31% | 27.51% | -5.80pp | 2 | 3 |
| GN | 3,243 | 43.34% | 37.37% | -5.97pp | 5 | 2 |

---

### ER

#### Waterfall GA

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 6,469 | 8,303 | +1,834 | +28.35pp | - | - | - |
| Select Payment Method | 3,039 | 3,410 | +371 | +12.21pp | 46.98% | 41.07% | -5.91pp |
| Click Submit Form | 2,731 | 2,921 | +190 | +6.96pp | 89.87% | 85.66% | -4.21pp |
| FE Validation Passed | 2,476 | 2,628 | +152 | +6.14pp | 90.66% | 89.97% | -0.69pp |
| Enter Fraud Service | 2,414 | 2,551 | +137 | +5.68pp | 97.50% | 97.07% | -0.43pp |
| Approved by Fraud Service | 2,311 | 2,455 | +144 | +6.23pp | 95.73% | 96.24% | +0.50pp |
| Call to PVS | 2,306 | 2,444 | +138 | +5.98pp | 99.78% | 99.55% | -0.23pp |
| **Successful Checkout** | 2,155 | 2,284 | +129 | +5.99pp | 93.45% | 93.45% | +0.00pp |
| **PCR Rate** | | | | | 33.31% | 27.51% | **-5.80pp** |

**Key Driver:** Select Payment Method (-5.91pp)

#### Waterfall Backend

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 9,471 | 10,247 | +776 | +8.19pp | - | - | - |
| Checkout Attempt | 2,934 | 3,021 | +87 | +2.97pp | 30.98% | 29.48% | -1.50pp |
| Enter Fraud Service | 2,930 | 3,018 | +88 | +3.00pp | 99.86% | 99.90% | +0.04pp |
| Approved by Fraud Service | 2,784 | 2,873 | +89 | +3.20pp | 95.02% | 95.20% | +0.18pp |
| PVS Attempt | 2,780 | 2,856 | +76 | +2.73pp | 99.86% | 99.41% | -0.45pp |
| PVS Success | 2,623 | 2,695 | +72 | +2.74pp | 94.35% | 94.36% | +0.01pp |
| **Successful Checkout** | 2,628 | 2,707 | +79 | +3.01pp | 100.19% | 100.45% | +0.25pp |

**Key Driver:** Checkout Attempt (-1.50pp)

---

### GN

#### Waterfall GA

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 3,020 | 3,243 | +223 | +7.38pp | - | - | - |
| Select Payment Method | 2,082 | 1,952 | -130 | -6.24pp | 68.94% | 60.19% | -8.75pp |
| Click Submit Form | 1,866 | 1,737 | -129 | -6.91pp | 89.63% | 88.99% | -0.64pp |
| FE Validation Passed | 1,539 | 1,453 | -86 | -5.59pp | 82.48% | 83.65% | +1.17pp |
| Enter Fraud Service | 1,429 | 1,330 | -99 | -6.93pp | 92.85% | 91.53% | -1.32pp |
| Approved by Fraud Service | 1,361 | 1,262 | -99 | -7.27pp | 95.24% | 94.89% | -0.35pp |
| Call to PVS | 1,359 | 1,261 | -98 | -7.21pp | 99.85% | 99.92% | +0.07pp |
| **Successful Checkout** | 1,309 | 1,212 | -97 | -7.41pp | 96.32% | 96.11% | -0.21pp |
| **PCR Rate** | | | | | 43.34% | 37.37% | **-5.97pp** |

**Key Driver:** Select Payment Method (-8.75pp)

#### Waterfall Backend

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 4,561 | 4,199 | -362 | -7.94pp | - | - | - |
| Checkout Attempt | 1,891 | 1,712 | -179 | -9.47pp | 41.46% | 40.77% | -0.69pp |
| Enter Fraud Service | 1,887 | 1,708 | -179 | -9.49pp | 99.79% | 99.77% | -0.02pp |
| Approved by Fraud Service | 1,769 | 1,598 | -171 | -9.67pp | 93.75% | 93.56% | -0.19pp |
| PVS Attempt | 1,772 | 1,594 | -178 | -10.05pp | 100.17% | 99.75% | -0.42pp |
| PVS Success | 1,710 | 1,537 | -173 | -10.12pp | 96.50% | 96.42% | -0.08pp |
| **Successful Checkout** | 1,736 | 1,566 | -170 | -9.79pp | 101.52% | 101.89% | +0.37pp |

**Key Driver:** Checkout Attempt (-0.69pp)

---

### CG

#### Waterfall GA

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 5,539 | 6,419 | +880 | +15.89pp | - | - | - |
| Select Payment Method | 2,747 | 2,679 | -68 | -2.48pp | 49.59% | 41.74% | -7.86pp |
| Click Submit Form | 2,500 | 2,317 | -183 | -7.32pp | 91.01% | 86.49% | -4.52pp |
| FE Validation Passed | 2,314 | 2,147 | -167 | -7.22pp | 92.56% | 92.66% | +0.10pp |
| Enter Fraud Service | 2,276 | 2,115 | -161 | -7.07pp | 98.36% | 98.51% | +0.15pp |
| Approved by Fraud Service | 2,185 | 2,032 | -153 | -7.00pp | 96.00% | 96.08% | +0.07pp |
| Call to PVS | 2,177 | 2,033 | -144 | -6.61pp | 99.63% | 100.05% | +0.42pp |
| **Successful Checkout** | 2,119 | 1,970 | -149 | -7.03pp | 97.34% | 96.90% | -0.43pp |
| **PCR Rate** | | | | | 38.26% | 30.69% | **-7.57pp** |

**Key Driver:** Select Payment Method (-7.86pp)

#### Waterfall Backend

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 7,761 | 7,400 | -361 | -4.65pp | - | - | - |
| Checkout Attempt | 2,542 | 2,369 | -173 | -6.81pp | 32.75% | 32.01% | -0.74pp |
| Enter Fraud Service | 2,532 | 2,362 | -170 | -6.71pp | 99.61% | 99.70% | +0.10pp |
| Approved by Fraud Service | 2,420 | 2,247 | -173 | -7.15pp | 95.58% | 95.13% | -0.45pp |
| PVS Attempt | 2,406 | 2,234 | -172 | -7.15pp | 99.42% | 99.42% | -0.00pp |
| PVS Success | 2,346 | 2,176 | -170 | -7.25pp | 97.51% | 97.40% | -0.10pp |
| **Successful Checkout** | 2,353 | 2,185 | -168 | -7.14pp | 100.30% | 100.41% | +0.12pp |

**Key Driver:** Checkout Attempt (-0.74pp)

---





---

*Report: 2026-04-10*
