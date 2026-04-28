# PCR Investigation: HF-INTL 2026-W17

**Metric:** Payment Conversion Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 37.09% → 36.09% (-1.00pp)  
**Volume:** 61,868 payment visits  
**Threshold:** +0.50pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined by -1.00pp (from 37.09% to 36.09%) on 61,868 payment visits in 2026-W17, breaching the monitoring threshold.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Δ ≥ ±0.50pp | -1.03pp | ⚠️ |
| Click Submit Form | Δ ≥ ±0.50pp | -0.22pp | ✅ |
| FE Validation Passed | Δ ≥ ±0.50pp | +0.06pp | ✅ |
| Enter Fraud Service | Δ ≥ ±0.50pp | -0.30pp | ✅ |
| Approved by Fraud Service | Δ ≥ ±0.50pp | +0.32pp | ✅ |
| Call to PVS | Δ ≥ ±0.50pp | -0.19pp | ✅ |
| Successful Checkout | Δ ≥ ±0.50pp | -0.49pp | ✅ |

**Key Findings:**
- **Primary bottleneck at Select Payment Method:** GA funnel shows -1.03pp drop at payment method selection, accounting for the majority of the PCR decline
- **NL experienced severe degradation:** PCR dropped -6.44pp driven by Select Payment Method conversion falling -9.26pp (from 64.96% to 55.70%)
- **GB showed strong improvement:** PCR increased +2.06pp with Click Submit Form improving +1.98pp, partially offsetting overall decline
- **Backend Checkout Attempt rates declined significantly across markets:** DE (-9.08pp), NL (-11.12pp), and NO (-8.35pp) all showed major drops in checkout attempt conversion from payment method listing
- **All payment methods improved success rates:** Despite overall PCR decline, individual payment method success rates increased (e.g., Braintree_Paypal +12.04pp, Adyen_CreditCard +21.11pp), indicating the issue is upstream user engagement

**Action:** **Investigate** — Focus on NL market to understand the -9.26pp drop in Select Payment Method conversion; review any UI/UX changes, payment method availability, or technical issues affecting the payment selection step across HF-INTL.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 76,262 | 61,868 | -14,394 | -18.9% | - | - | - |
| Select Payment Method | 42,762 | 34,053 | -8,709 | -20.4% | 56.07% | 55.04% | -1.03pp |
| Click Submit Form | 34,800 | 27,637 | -7,163 | -20.6% | 81.38% | 81.16% | -0.22pp |
| FE Validation Passed | 32,504 | 25,830 | -6,674 | -20.5% | 93.40% | 93.46% | +0.06pp |
| Enter Fraud Service | 31,283 | 24,782 | -6,501 | -20.8% | 96.24% | 95.94% | -0.30pp |
| Approved by Fraud Service | 29,488 | 23,439 | -6,049 | -20.5% | 94.26% | 94.58% | +0.32pp |
| Call to PVS | 29,383 | 23,310 | -6,073 | -20.7% | 99.64% | 99.45% | -0.19pp |
| **Successful Checkout** | 28,287 | 22,327 | -5,960 | -21.1% | 96.27% | 95.78% | -0.49pp |
| **PCR Rate** | | | | | 37.09% | 36.09% | **-1.00pp** |

### Waterfall Backend

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 83,606 | 90,856 | 7,250 | 8.7% | - | - | - |
| Checkout Attempt | 45,804 | 42,480 | -3,324 | -7.3% | 54.79% | 46.76% | -8.03pp |
| Enter Fraud Service | 44,356 | 40,922 | -3,434 | -7.7% | 96.84% | 96.33% | -0.51pp |
| Approved by Fraud Service | 40,911 | 37,878 | -3,033 | -7.4% | 92.23% | 92.56% | +0.33pp |
| PVS Attempt | 37,314 | 34,080 | -3,234 | -8.7% | 91.21% | 89.97% | -1.23pp |
| PVS Success | 36,244 | 32,944 | -3,300 | -9.1% | 97.13% | 96.67% | -0.47pp |
| **Successful Checkout** | 34,049 | 36,198 | 2,149 | 6.3% | 93.94% | 109.88% | +15.93pp |
| **PCR Rate** | | | | | 40.73% | 39.84% | **-0.88pp** |

### Payment Method Breakdown

| Payment Method | 2026-W16 Attempt | 2026-W16 Success | 2026-W16 Rate | 2026-W17 Attempt | 2026-W17 Success | 2026-W17 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 16,099 | 12,234 | 75.99% | 13,554 | 11,768 | 86.82% | +10.83pp |
| Braintree_ApplePay | 13,355 | 9,766 | 73.13% | 12,455 | 10,503 | 84.33% | +11.20pp |
| Braintree_Paypal | 9,604 | 7,659 | 79.75% | 9,178 | 8,424 | 91.78% | +12.04pp |
| Adyen_CreditCard | 1,347 | 1,033 | 76.69% | 1,729 | 1,691 | 97.80% | +21.11pp |
| ProcessOut_ApplePay | 1,544 | 1,238 | 80.18% | 1,486 | 1,334 | 89.77% | +9.59pp |
| Adyen_Sepa | 1,197 | 2 | 0.17% | 1,321 | 3 | 0.23% | +0.06pp |
| Adyen_IDeal | 1,238 | 1,003 | 81.02% | 1,129 | 1,025 | 90.79% | +9.77pp |
| Adyen_Klarna | 1,152 | 965 | 83.77% | 846 | 802 | 94.80% | +11.03pp |
| Adyen_BcmcMobile | 171 | 148 | 86.55% | 688 | 647 | 94.04% | +7.49pp |
| NoPayment | 89 | 0 | 0.00% | 91 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (4 countries in HF-INTL)

| Country | Volume | PCR 2026-W16 | PCR 2026-W17 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| GB | 15,984 | 39.64% | 41.70% | +2.06pp | 1 | 7 |
| DE | 14,584 | 36.95% | 34.94% | -2.01pp | 2 | 8 |
| NL | 1,815 | 42.36% | 35.92% | -6.44pp | 4 | 1 |
| NO | 961 | 45.73% | 50.57% | +4.84pp | 8 | 2 |

---

### NO

#### Waterfall GA

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 1,535 | 961 | -574 | -37.39pp | - | - | - |
| Select Payment Method | 942 | 623 | -319 | -33.86pp | 61.37% | 64.83% | +3.46pp |
| Click Submit Form | 792 | 540 | -252 | -31.82pp | 84.08% | 86.68% | +2.60pp |
| FE Validation Passed | 764 | 522 | -242 | -31.68pp | 96.46% | 96.67% | +0.20pp |
| Enter Fraud Service | 736 | 517 | -219 | -29.76pp | 96.34% | 99.04% | +2.71pp |
| Approved by Fraud Service | 714 | 501 | -213 | -29.83pp | 97.01% | 96.91% | -0.11pp |
| Call to PVS | 711 | 495 | -216 | -30.38pp | 99.58% | 98.80% | -0.78pp |
| **Successful Checkout** | 702 | 486 | -216 | -30.77pp | 98.73% | 98.18% | -0.55pp |
| **PCR Rate** | | | | | 45.73% | 50.57% | **+4.84pp** |

**Key Driver:** Select Payment Method (+3.46pp)

#### Waterfall Backend

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 1,744 | 1,573 | -171 | -9.81pp | - | - | - |
| Checkout Attempt | 1,037 | 804 | -233 | -22.47pp | 59.46% | 51.11% | -8.35pp |
| Enter Fraud Service | 1,032 | 800 | -232 | -22.48pp | 99.52% | 99.50% | -0.02pp |
| Approved by Fraud Service | 993 | 762 | -231 | -23.26pp | 96.22% | 95.25% | -0.97pp |
| PVS Attempt | 909 | 627 | -282 | -31.02pp | 91.54% | 82.28% | -9.26pp |
| PVS Success | 901 | 618 | -283 | -31.41pp | 99.12% | 98.56% | -0.56pp |
| **Successful Checkout** | 986 | 750 | -236 | -23.94pp | 109.43% | 121.36% | +11.93pp |

**Key Driver:** Successful Checkout (+11.93pp)

---

### NL

#### Waterfall GA

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 1,995 | 1,815 | -180 | -9.02pp | - | - | - |
| Select Payment Method | 1,296 | 1,011 | -285 | -21.99pp | 64.96% | 55.70% | -9.26pp |
| Click Submit Form | 1,172 | 879 | -293 | -25.00pp | 90.43% | 86.94% | -3.49pp |
| FE Validation Passed | 1,166 | 875 | -291 | -24.96pp | 99.49% | 99.54% | +0.06pp |
| Enter Fraud Service | 1,153 | 868 | -285 | -24.72pp | 98.89% | 99.20% | +0.31pp |
| Approved by Fraud Service | 1,069 | 814 | -255 | -23.85pp | 92.71% | 93.78% | +1.06pp |
| Call to PVS | 1,070 | 815 | -255 | -23.83pp | 100.09% | 100.12% | +0.03pp |
| **Successful Checkout** | 845 | 652 | -193 | -22.84pp | 78.97% | 80.00% | +1.03pp |
| **PCR Rate** | | | | | 42.36% | 35.92% | **-6.43pp** |

**Key Driver:** Select Payment Method (-9.26pp)

#### Waterfall Backend

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 2,588 | 2,867 | +279 | +10.78pp | - | - | - |
| Checkout Attempt | 1,760 | 1,631 | -129 | -7.33pp | 68.01% | 56.89% | -11.12pp |
| Enter Fraud Service | 1,755 | 1,512 | -243 | -13.85pp | 99.72% | 92.70% | -7.01pp |
| Approved by Fraud Service | 1,606 | 1,379 | -227 | -14.13pp | 91.51% | 91.20% | -0.31pp |
| PVS Attempt | 1,604 | 1,371 | -233 | -14.53pp | 99.88% | 99.42% | -0.46pp |
| PVS Success | 1,432 | 1,226 | -206 | -14.39pp | 89.28% | 89.42% | +0.15pp |
| **Successful Checkout** | 1,601 | 1,483 | -118 | -7.37pp | 111.80% | 120.96% | +9.16pp |

**Key Driver:** Checkout Attempt (-11.12pp)

---

### DE

#### Waterfall GA

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 15,628 | 14,584 | -1,044 | -6.68pp | - | - | - |
| Select Payment Method | 9,331 | 8,466 | -865 | -9.27pp | 59.71% | 58.05% | -1.66pp |
| Click Submit Form | 7,228 | 6,436 | -792 | -10.96pp | 77.46% | 76.02% | -1.44pp |
| FE Validation Passed | 6,840 | 6,052 | -788 | -11.52pp | 94.63% | 94.03% | -0.60pp |
| Enter Fraud Service | 6,301 | 5,548 | -753 | -11.95pp | 92.12% | 91.67% | -0.45pp |
| Approved by Fraud Service | 6,044 | 5,354 | -690 | -11.42pp | 95.92% | 96.50% | +0.58pp |
| Call to PVS | 6,035 | 5,323 | -712 | -11.80pp | 99.85% | 99.42% | -0.43pp |
| **Successful Checkout** | 5,775 | 5,096 | -679 | -11.76pp | 95.69% | 95.74% | +0.04pp |
| **PCR Rate** | | | | | 36.95% | 34.94% | **-2.01pp** |

**Key Driver:** Select Payment Method (-1.66pp)

#### Waterfall Backend

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 18,294 | 21,803 | +3,509 | +19.18pp | - | - | - |
| Checkout Attempt | 9,732 | 9,620 | -112 | -1.15pp | 53.20% | 44.12% | -9.08pp |
| Enter Fraud Service | 9,680 | 9,582 | -98 | -1.01pp | 99.47% | 99.60% | +0.14pp |
| Approved by Fraud Service | 9,147 | 9,114 | -33 | -0.36pp | 94.49% | 95.12% | +0.62pp |
| PVS Attempt | 8,708 | 8,900 | +192 | +2.20pp | 95.20% | 97.65% | +2.45pp |
| PVS Success | 8,441 | 8,654 | +213 | +2.52pp | 96.93% | 97.24% | +0.30pp |
| **Successful Checkout** | 8,940 | 8,841 | -99 | -1.11pp | 105.91% | 102.16% | -3.75pp |

**Key Driver:** Checkout Attempt (-9.08pp)

---

### GB

#### Waterfall GA

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 22,128 | 15,984 | -6,144 | -27.77pp | - | - | - |
| Select Payment Method | 12,818 | 9,393 | -3,425 | -26.72pp | 57.93% | 58.77% | +0.84pp |
| Click Submit Form | 10,565 | 7,928 | -2,637 | -24.96pp | 82.42% | 84.40% | +1.98pp |
| FE Validation Passed | 9,683 | 7,332 | -2,351 | -24.28pp | 91.65% | 92.48% | +0.83pp |
| Enter Fraud Service | 9,436 | 7,166 | -2,270 | -24.06pp | 97.45% | 97.74% | +0.29pp |
| Approved by Fraud Service | 8,993 | 6,834 | -2,159 | -24.01pp | 95.31% | 95.37% | +0.06pp |
| Call to PVS | 8,940 | 6,777 | -2,163 | -24.19pp | 99.41% | 99.17% | -0.24pp |
| **Successful Checkout** | 8,771 | 6,665 | -2,106 | -24.01pp | 98.11% | 98.35% | +0.24pp |
| **PCR Rate** | | | | | 39.64% | 41.70% | **+2.06pp** |

**Key Driver:** Click Submit Form (+1.98pp)

#### Waterfall Backend

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 22,721 | 22,706 | -15 | -0.07pp | - | - | - |
| Checkout Attempt | 13,021 | 11,713 | -1,308 | -10.05pp | 57.31% | 51.59% | -5.72pp |
| Enter Fraud Service | 12,918 | 11,614 | -1,304 | -10.09pp | 99.21% | 99.15% | -0.05pp |
| Approved by Fraud Service | 12,110 | 10,860 | -1,250 | -10.32pp | 93.75% | 93.51% | -0.24pp |
| PVS Attempt | 9,915 | 8,348 | -1,567 | -15.80pp | 81.87% | 76.87% | -5.01pp |
| PVS Success | 9,748 | 8,211 | -1,537 | -15.77pp | 98.32% | 98.36% | +0.04pp |
| **Successful Checkout** | 11,979 | 10,748 | -1,231 | -10.28pp | 122.89% | 130.90% | +8.01pp |

**Key Driver:** Successful Checkout (+8.01pp)

---





---

*Report: 2026-04-28*
