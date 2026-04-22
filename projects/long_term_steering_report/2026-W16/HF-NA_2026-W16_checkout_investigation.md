# PCR Investigation: HF-NA 2026-W16

**Metric:** Payment Conversion Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 27.99% → 27.55% (-0.44pp)  
**Volume:** 71,279 payment visits  
**Threshold:** +0.22pp (0.5 × |Overall PCR Δ|)

## Executive Summary

**Overall:** Payment Conversion Rate declined by -0.44pp (27.99% → 27.55%) in HF-NA during 2026-W16, primarily driven by a significant drop in fraud service approval rates.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Δ ≥ threshold? | -0.55pp | ⚠️ |
| Click Submit Form | Δ ≥ threshold? | +0.28pp | ✅ |
| FE Validation Passed | Δ ≥ threshold? | +0.20pp | ✅ |
| Enter Fraud Service | Δ ≥ threshold? | +0.04pp | ✅ |
| Approved by Fraud Service | Δ ≥ threshold? | -0.88pp | ⚠️ |
| Call to PVS | Δ ≥ threshold? | +0.15pp | ✅ |
| Successful Checkout | Δ ≥ threshold? | +0.01pp | ✅ |

**Key Findings:**
- **Fraud Service Approval** is the primary driver of the decline, dropping -0.88pp (93.08% → 92.20%) at cluster level and -1.04pp in US specifically
- **Braintree_ApplePay** experienced a notable conversion rate decline of -1.75pp (77.50% → 75.75%), representing the largest negative shift among high-volume payment methods
- **Adyen_CreditCard** showed dramatic improvement (+80.06pp), but this appears to be recovery from a previous issue rather than organic growth (2.95% → 83.01%)
- **US** drove the overall decline with -0.41pp drop, while **CA** showed slight improvement (+0.13pp)
- **Gap reduction** before Fraud Service improved significantly (-0.67pp), with Adyen_CreditCard gap decreasing from 262 to 65 transactions

**Action:** Investigate - The -0.88pp decline in Fraud Service approval rate exceeds the threshold and warrants investigation into potential changes in fraud rules or patterns, particularly for US traffic.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 69,100 | 71,279 | 2,179 | 3.2% | - | - | - |
| Select Payment Method | 28,203 | 28,698 | 495 | 1.8% | 40.81% | 40.26% | -0.55pp |
| Click Submit Form | 24,069 | 24,571 | 502 | 2.1% | 85.34% | 85.62% | +0.28pp |
| FE Validation Passed | 22,592 | 23,112 | 520 | 2.3% | 93.86% | 94.06% | +0.20pp |
| Enter Fraud Service | 22,079 | 22,596 | 517 | 2.3% | 97.73% | 97.77% | +0.04pp |
| Approved by Fraud Service | 20,552 | 20,834 | 282 | 1.4% | 93.08% | 92.20% | -0.88pp |
| Call to PVS | 20,533 | 20,845 | 312 | 1.5% | 99.91% | 100.05% | +0.15pp |
| **Successful Checkout** | 19,340 | 19,636 | 296 | 1.5% | 94.19% | 94.20% | +0.01pp |
| **PCR Rate** | | | | | 27.99% | 27.55% | **-0.44pp** |

### Waterfall Backend

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 75,644 | 75,980 | 336 | 0.4% | - | - | - |
| Checkout Attempt | 28,054 | 27,682 | -372 | -1.3% | 37.09% | 36.43% | -0.65pp |
| Enter Fraud Service | 27,711 | 27,529 | -182 | -0.7% | 98.78% | 99.45% | +0.67pp |
| Approved by Fraud Service | 24,928 | 24,837 | -91 | -0.4% | 89.96% | 90.22% | +0.26pp |
| PVS Attempt | 23,512 | 23,369 | -143 | -0.6% | 94.32% | 94.09% | -0.23pp |
| PVS Success | 22,120 | 21,934 | -186 | -0.8% | 94.08% | 93.86% | -0.22pp |
| **Successful Checkout** | 22,541 | 22,314 | -227 | -1.0% | 101.90% | 101.73% | -0.17pp |
| **PCR Rate** | | | | | 29.80% | 29.37% | **-0.43pp** |

### Payment Method Breakdown

| Payment Method | 2026-W15 Attempt | 2026-W15 Success | 2026-W15 Rate | 2026-W16 Attempt | 2026-W16 Success | 2026-W16 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 16,642 | 13,764 | 82.71% | 15,360 | 12,699 | 82.68% | -0.03pp |
| Braintree_ApplePay | 8,572 | 6,643 | 77.50% | 9,005 | 6,821 | 75.75% | -1.75pp |
| Braintree_Paypal | 2,309 | 2,000 | 86.62% | 2,334 | 2,019 | 86.50% | -0.11pp |
| Adyen_CreditCard | 271 | 8 | 2.95% | 665 | 552 | 83.01% | +80.06pp |
| Braintree_CreditCard | 167 | 126 | 75.45% | 264 | 222 | 84.09% | +8.64pp |
|  | 93 | 0 | 0.00% | 54 | 1 | 1.85% | +1.85pp |
| CreditCard | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (2 countries in HF-NA)

| Country | Volume | PCR 2026-W15 | PCR 2026-W16 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| US | 55,957 | 26.24% | 25.83% | -0.41pp | 1 | 1 |
| CA | 15,322 | 33.68% | 33.81% | +0.13pp | 2 | 2 |

---

### US

#### Waterfall GA

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 52,863 | 55,957 | +3,094 | +5.85pp | - | - | - |
| Select Payment Method | 19,711 | 20,767 | +1,056 | +5.36pp | 37.29% | 37.11% | -0.17pp |
| Click Submit Form | 17,360 | 18,240 | +880 | +5.07pp | 88.07% | 87.83% | -0.24pp |
| FE Validation Passed | 16,321 | 17,167 | +846 | +5.18pp | 94.01% | 94.12% | +0.10pp |
| Enter Fraud Service | 15,998 | 16,814 | +816 | +5.10pp | 98.02% | 97.94% | -0.08pp |
| Approved by Fraud Service | 14,884 | 15,468 | +584 | +3.92pp | 93.04% | 91.99% | -1.04pp |
| Call to PVS | 14,895 | 15,548 | +653 | +4.38pp | 100.07% | 100.52% | +0.44pp |
| **Successful Checkout** | 13,872 | 14,455 | +583 | +4.20pp | 93.13% | 92.97% | -0.16pp |
| **PCR Rate** | | | | | 26.24% | 25.83% | **-0.41pp** |

**Key Driver:** Approved by Fraud Service (-1.04pp)

#### Waterfall Backend

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 57,223 | 59,150 | +1,927 | +3.37pp | - | - | - |
| Checkout Attempt | 20,476 | 20,703 | +227 | +1.11pp | 35.78% | 35.00% | -0.78pp |
| Enter Fraud Service | 20,167 | 20,593 | +426 | +2.11pp | 98.49% | 99.47% | +0.98pp |
| Approved by Fraud Service | 18,051 | 18,536 | +485 | +2.69pp | 89.51% | 90.01% | +0.50pp |
| PVS Attempt | 17,669 | 18,142 | +473 | +2.68pp | 97.88% | 97.87% | -0.01pp |
| PVS Success | 16,435 | 16,826 | +391 | +2.38pp | 93.02% | 92.75% | -0.27pp |
| **Successful Checkout** | 17,039 | 17,245 | +206 | +1.21pp | 103.68% | 102.49% | -1.18pp |

**Key Driver:** Successful Checkout (-1.18pp)

---

### CA

#### Waterfall GA

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 16,237 | 15,322 | -915 | -5.64pp | - | - | - |
| Select Payment Method | 8,492 | 7,931 | -561 | -6.61pp | 52.30% | 51.76% | -0.54pp |
| Click Submit Form | 6,709 | 6,331 | -378 | -5.63pp | 79.00% | 79.83% | +0.82pp |
| FE Validation Passed | 6,271 | 5,945 | -326 | -5.20pp | 93.47% | 93.90% | +0.43pp |
| Enter Fraud Service | 6,081 | 5,782 | -299 | -4.92pp | 96.97% | 97.26% | +0.29pp |
| Approved by Fraud Service | 5,668 | 5,366 | -302 | -5.33pp | 93.21% | 92.81% | -0.40pp |
| Call to PVS | 5,638 | 5,297 | -341 | -6.05pp | 99.47% | 98.71% | -0.76pp |
| **Successful Checkout** | 5,468 | 5,181 | -287 | -5.25pp | 96.98% | 97.81% | +0.83pp |
| **PCR Rate** | | | | | 33.68% | 33.81% | **+0.14pp** |

**Key Driver:** Successful Checkout (+0.83pp)

#### Waterfall Backend

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 18,421 | 16,830 | -1,591 | -8.64pp | - | - | - |
| Checkout Attempt | 7,578 | 6,979 | -599 | -7.90pp | 41.14% | 41.47% | +0.33pp |
| Enter Fraud Service | 7,544 | 6,936 | -608 | -8.06pp | 99.55% | 99.38% | -0.17pp |
| Approved by Fraud Service | 6,877 | 6,301 | -576 | -8.38pp | 91.16% | 90.84% | -0.31pp |
| PVS Attempt | 5,843 | 5,227 | -616 | -10.54pp | 84.96% | 82.96% | -2.01pp |
| PVS Success | 5,685 | 5,108 | -577 | -10.15pp | 97.30% | 97.72% | +0.43pp |
| **Successful Checkout** | 6,723 | 6,140 | -583 | -8.67pp | 118.26% | 120.20% | +1.95pp |

**Key Driver:** PVS Attempt (-2.01pp)

---



## Fraud Analysis

**Include reason:** Approved Δ (-0.88pp) meets threshold (+0.22pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W15 | 2026-W15 % | 2026-W16 | 2026-W16 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 28,054 | - | 27,682 | - | -372 | -1.3% |
| Enter Fraud Service | 27,711 | - | 27,529 | - | -182 | -0.7% |
| **Gap (Skipped)** | **343** | **1.22%** | **153** | **0.55%** | **-190** | **-0.67pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W15 Gap | 2026-W15 % | 2026-W16 Gap | 2026-W16 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Adyen_CreditCard | 262 | 76.2% | 65 | 42.5% | -197 | -33.68pp |
| ProcessOut_CreditCard | 42 | 12.2% | 49 | 32.0% | +7 | +19.82pp |
| Braintree_ApplePay | 29 | 8.4% | 29 | 19.0% | 0 | +10.52pp |
| Braintree_Paypal | 9 | 2.6% | 9 | 5.9% | 0 | +3.27pp |
| Braintree_CreditCard | 2 | 0.6% | 1 | 0.7% | -1 | +0.07pp |
| **Total** | **344** | **100%** | **153** | **100%** | **-191** | - |

*% of Gap = Payment Method Gap / Total Gap*

---


---

*Report: 2026-04-22*
