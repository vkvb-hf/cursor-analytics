# PCR Investigation: RTE 2026-W20

**Metric:** Payment Conversion Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 38.59% → 39.29% (+0.70pp)  
**Volume:** 63,830 payment visits  
**Threshold:** +0.35pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate improved by +0.70pp (38.59% → 39.29%) on 63,830 payment visits, exceeding the monitoring threshold of +0.35pp.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ≥ threshold | +0.83pp | ✅ |
| Click Submit Form | ≥ threshold | +0.44pp | ✅ |
| FE Validation Passed | < threshold | +0.06pp | ✅ |
| Enter Fraud Service | ≥ threshold | +0.42pp | ⚠️ |
| Approved by Fraud Service | negative | -0.23pp | ⚠️ |
| Call to PVS | negative | -0.37pp | ⚠️ |
| Successful Checkout | negative | -0.23pp | ⚠️ |

**Key Findings:**
- The PCR improvement is primarily driven by early-funnel gains: Select Payment Method (+0.83pp) and Click Submit Form (+0.44pp) conversion improvements offset downstream friction
- TV showed the largest absolute change (+3.88pp), driven by Select Payment Method (+5.59pp) and Fraud Service approval (+3.78pp in backend)
- YE contributed significantly with +2.05pp improvement, primarily from Select Payment Method (+2.26pp GA) and Checkout Attempt (+3.58pp backend)
- Braintree_ApplePay (-1.06pp) and Adyen_CreditCard (-1.04pp) showed declining success rates despite overall PCR improvement
- Fraud Service gap increased slightly (+0.03pp), with Braintree_ApplePay showing new gap occurrences (0 → 5 cases)

**Action:** Monitor — The positive PCR trend is healthy, but watch downstream conversion decline at Call to PVS (-0.37pp) and payment method performance degradation for Braintree_ApplePay and Adyen_CreditCard.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 65,184 | 63,830 | -1,354 | -2.1% | - | - | - |
| Select Payment Method | 32,074 | 31,940 | -134 | -0.4% | 49.21% | 50.04% | +0.83pp |
| Click Submit Form | 28,657 | 28,678 | 21 | 0.1% | 89.35% | 89.79% | +0.44pp |
| FE Validation Passed | 28,051 | 28,089 | 38 | 0.1% | 97.89% | 97.95% | +0.06pp |
| Enter Fraud Service | 27,354 | 27,508 | 154 | 0.6% | 97.52% | 97.93% | +0.42pp |
| Approved by Fraud Service | 26,335 | 26,419 | 84 | 0.3% | 96.27% | 96.04% | -0.23pp |
| Call to PVS | 26,214 | 26,200 | -14 | -0.1% | 99.54% | 99.17% | -0.37pp |
| **Successful Checkout** | 25,153 | 25,079 | -74 | -0.3% | 95.95% | 95.72% | -0.23pp |
| **PCR Rate** | | | | | 38.59% | 39.29% | **+0.70pp** |

### Waterfall Backend

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 111,336 | 109,196 | -2,140 | -1.9% | - | - | - |
| Checkout Attempt | 41,790 | 41,865 | 75 | 0.2% | 37.54% | 38.34% | +0.80pp |
| Enter Fraud Service | 41,733 | 41,795 | 62 | 0.1% | 99.86% | 99.83% | -0.03pp |
| Approved by Fraud Service | 39,469 | 39,708 | 239 | 0.6% | 94.58% | 95.01% | +0.43pp |
| PVS Attempt | 38,661 | 38,879 | 218 | 0.6% | 97.95% | 97.91% | -0.04pp |
| PVS Success | 37,371 | 37,515 | 144 | 0.4% | 96.66% | 96.49% | -0.17pp |
| **Successful Checkout** | 38,363 | 38,272 | -91 | -0.2% | 102.65% | 102.02% | -0.64pp |
| **PCR Rate** | | | | | 34.46% | 35.05% | **+0.59pp** |

### Payment Method Breakdown

| Payment Method | 2026-W19 Attempt | 2026-W19 Success | 2026-W19 Rate | 2026-W20 Attempt | 2026-W20 Success | 2026-W20 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 16,932 | 15,593 | 92.09% | 16,871 | 15,584 | 92.37% | +0.28pp |
| Braintree_ApplePay | 9,221 | 8,584 | 93.09% | 9,776 | 8,997 | 92.03% | -1.06pp |
| Adyen_CreditCard | 9,613 | 8,609 | 89.56% | 9,102 | 8,057 | 88.52% | -1.04pp |
| Braintree_Paypal | 4,821 | 4,473 | 92.78% | 4,945 | 4,547 | 91.95% | -0.83pp |
| Adyen_IDeal | 668 | 626 | 93.71% | 771 | 721 | 93.51% | -0.20pp |
| Adyen_Klarna | 325 | 302 | 92.92% | 287 | 271 | 94.43% | +1.50pp |
| Braintree_CreditCard | 204 | 173 | 84.80% | 105 | 90 | 85.71% | +0.91pp |
| Braintree_Venmo | 3 | 3 | 100.00% | 4 | 4 | 100.00% | +0.00pp |
| Adyen_BcmcMobile | 0 | 0 | 0.00% | 3 | 1 | 33.33% | +33.33pp |
| mc | 1 | 0 | 0.00% | 1 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (4 countries in RTE)

| Country | Volume | PCR 2026-W19 | PCR 2026-W20 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| FJ | 40,715 | 39.63% | 40.42% | +0.79pp | 1 | 6 |
| YE | 6,352 | 32.40% | 34.45% | +2.05pp | 2 | 5 |
| TT | 1,591 | 28.35% | 31.74% | +3.39pp | 3 | 2 |
| TV | 506 | 38.02% | 41.90% | +3.88pp | 5 | 1 |

---

### TT

#### Waterfall GA

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 1,372 | 1,591 | +219 | +15.96pp | - | - | - |
| Select Payment Method | 726 | 855 | +129 | +17.77pp | 52.92% | 53.74% | +0.82pp |
| Click Submit Form | 656 | 781 | +125 | +19.05pp | 90.36% | 91.35% | +0.99pp |
| FE Validation Passed | 660 | 786 | +126 | +19.09pp | 100.61% | 100.64% | +0.03pp |
| Enter Fraud Service | 652 | 782 | +130 | +19.94pp | 98.79% | 99.49% | +0.70pp |
| Approved by Fraud Service | 628 | 759 | +131 | +20.86pp | 96.32% | 97.06% | +0.74pp |
| Call to PVS | 628 | 748 | +120 | +19.11pp | 100.00% | 98.55% | -1.45pp |
| **Successful Checkout** | 389 | 505 | +116 | +29.82pp | 61.94% | 67.51% | +5.57pp |
| **PCR Rate** | | | | | 28.35% | 31.74% | **+3.39pp** |

**Key Driver:** Successful Checkout (+5.57pp)

#### Waterfall Backend

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 1,907 | 2,098 | +191 | +10.02pp | - | - | - |
| Checkout Attempt | 879 | 1,018 | +139 | +15.81pp | 46.09% | 48.52% | +2.43pp |
| Enter Fraud Service | 878 | 1,017 | +139 | +15.83pp | 99.89% | 99.90% | +0.02pp |
| Approved by Fraud Service | 823 | 962 | +139 | +16.89pp | 93.74% | 94.59% | +0.86pp |
| PVS Attempt | 824 | 949 | +125 | +15.17pp | 100.12% | 98.65% | -1.47pp |
| PVS Success | 622 | 762 | +140 | +22.51pp | 75.49% | 80.30% | +4.81pp |
| **Successful Checkout** | 820 | 944 | +124 | +15.12pp | 131.83% | 123.88% | -7.95pp |

**Key Driver:** Successful Checkout (-7.95pp)

---

### TV

#### Waterfall GA

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 605 | 506 | -99 | -16.36pp | - | - | - |
| Select Payment Method | 350 | 321 | -29 | -8.29pp | 57.85% | 63.44% | +5.59pp |
| Click Submit Form | 313 | 278 | -35 | -11.18pp | 89.43% | 86.60% | -2.82pp |
| FE Validation Passed | 309 | 278 | -31 | -10.03pp | 98.72% | 100.00% | +1.28pp |
| Enter Fraud Service | 307 | 276 | -31 | -10.10pp | 99.35% | 99.28% | -0.07pp |
| Approved by Fraud Service | 287 | 264 | -23 | -8.01pp | 93.49% | 95.65% | +2.17pp |
| Call to PVS | 288 | 264 | -24 | -8.33pp | 100.35% | 100.00% | -0.35pp |
| **Successful Checkout** | 230 | 212 | -18 | -7.83pp | 79.86% | 80.30% | +0.44pp |
| **PCR Rate** | | | | | 38.02% | 41.90% | **+3.88pp** |

**Key Driver:** Select Payment Method (+5.59pp)

#### Waterfall Backend

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 926 | 759 | -167 | -18.03pp | - | - | - |
| Checkout Attempt | 414 | 350 | -64 | -15.46pp | 44.71% | 46.11% | +1.40pp |
| Enter Fraud Service | 414 | 349 | -65 | -15.70pp | 100.00% | 99.71% | -0.29pp |
| Approved by Fraud Service | 377 | 331 | -46 | -12.20pp | 91.06% | 94.84% | +3.78pp |
| PVS Attempt | 377 | 329 | -48 | -12.73pp | 100.00% | 99.40% | -0.60pp |
| PVS Success | 321 | 278 | -43 | -13.40pp | 85.15% | 84.50% | -0.65pp |
| **Successful Checkout** | 377 | 328 | -49 | -13.00pp | 117.45% | 117.99% | +0.54pp |

**Key Driver:** Approved by Fraud Service (+3.78pp)

---

### YE

#### Waterfall GA

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 6,623 | 6,352 | -271 | -4.09pp | - | - | - |
| Select Payment Method | 2,923 | 2,947 | +24 | +0.82pp | 44.13% | 46.39% | +2.26pp |
| Click Submit Form | 2,570 | 2,625 | +55 | +2.14pp | 87.92% | 89.07% | +1.15pp |
| FE Validation Passed | 2,536 | 2,602 | +66 | +2.60pp | 98.68% | 99.12% | +0.45pp |
| Enter Fraud Service | 2,402 | 2,477 | +75 | +3.12pp | 94.72% | 95.20% | +0.48pp |
| Approved by Fraud Service | 2,283 | 2,335 | +52 | +2.28pp | 95.05% | 94.27% | -0.78pp |
| Call to PVS | 2,270 | 2,286 | +16 | +0.70pp | 99.43% | 97.90% | -1.53pp |
| **Successful Checkout** | 2,146 | 2,188 | +42 | +1.96pp | 94.54% | 95.71% | +1.18pp |
| **PCR Rate** | | | | | 32.40% | 34.45% | **+2.04pp** |

**Key Driver:** Select Payment Method (+2.26pp)

#### Waterfall Backend

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 10,028 | 9,441 | -587 | -5.85pp | - | - | - |
| Checkout Attempt | 3,643 | 3,768 | +125 | +3.43pp | 36.33% | 39.91% | +3.58pp |
| Enter Fraud Service | 3,640 | 3,763 | +123 | +3.38pp | 99.92% | 99.87% | -0.05pp |
| Approved by Fraud Service | 3,363 | 3,505 | +142 | +4.22pp | 92.39% | 93.14% | +0.75pp |
| PVS Attempt | 3,125 | 3,220 | +95 | +3.04pp | 92.92% | 91.87% | -1.05pp |
| PVS Success | 2,997 | 3,117 | +120 | +4.00pp | 95.90% | 96.80% | +0.90pp |
| **Successful Checkout** | 3,250 | 3,383 | +133 | +4.09pp | 108.44% | 108.53% | +0.09pp |

**Key Driver:** Checkout Attempt (+3.58pp)

---

### FJ

#### Waterfall GA

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 40,463 | 40,715 | +252 | +0.62pp | - | - | - |
| Select Payment Method | 19,835 | 20,263 | +428 | +2.16pp | 49.02% | 49.77% | +0.75pp |
| Click Submit Form | 17,887 | 18,360 | +473 | +2.64pp | 90.18% | 90.61% | +0.43pp |
| FE Validation Passed | 17,434 | 17,896 | +462 | +2.65pp | 97.47% | 97.47% | +0.01pp |
| Enter Fraud Service | 17,097 | 17,638 | +541 | +3.16pp | 98.07% | 98.56% | +0.49pp |
| Approved by Fraud Service | 16,559 | 17,055 | +496 | +3.00pp | 96.85% | 96.69% | -0.16pp |
| Call to PVS | 16,493 | 16,950 | +457 | +2.77pp | 99.60% | 99.38% | -0.22pp |
| **Successful Checkout** | 16,037 | 16,459 | +422 | +2.63pp | 97.24% | 97.10% | -0.13pp |
| **PCR Rate** | | | | | 39.63% | 40.42% | **+0.79pp** |

**Key Driver:** Select Payment Method (+0.75pp)

#### Waterfall Backend

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 79,074 | 79,119 | +45 | +0.06pp | - | - | - |
| Checkout Attempt | 28,520 | 29,074 | +554 | +1.94pp | 36.07% | 36.75% | +0.68pp |
| Enter Fraud Service | 28,506 | 29,056 | +550 | +1.93pp | 99.95% | 99.94% | -0.01pp |
| Approved by Fraud Service | 27,212 | 27,841 | +629 | +2.31pp | 95.46% | 95.82% | +0.36pp |
| PVS Attempt | 27,034 | 27,653 | +619 | +2.29pp | 99.35% | 99.32% | -0.02pp |
| PVS Success | 26,293 | 26,876 | +583 | +2.22pp | 97.26% | 97.19% | -0.07pp |
| **Successful Checkout** | 26,455 | 26,952 | +497 | +1.88pp | 100.62% | 100.28% | -0.33pp |

**Key Driver:** Checkout Attempt (+0.68pp)

---



## Fraud Analysis

**Include reason:** Enter FS Δ (+0.42pp) meets threshold (+0.35pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W19 | 2026-W19 % | 2026-W20 | 2026-W20 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 41,790 | - | 41,865 | - | 75 | 0.2% |
| Enter Fraud Service | 41,733 | - | 41,795 | - | 62 | 0.1% |
| **Gap (Skipped)** | **57** | **0.14%** | **70** | **0.17%** | **13** | **+0.03pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W19 Gap | 2026-W19 % | 2026-W20 Gap | 2026-W20 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Adyen_CreditCard | 41 | 71.9% | 46 | 65.7% | +5 | -6.22pp |
| ProcessOut_CreditCard | 13 | 22.8% | 12 | 17.1% | -1 | -5.66pp |
| Braintree_Paypal | 2 | 3.5% | 5 | 7.1% | +3 | +3.63pp |
| Braintree_ApplePay | 0 | 0.0% | 5 | 7.1% | +5 | +7.14pp |
| Adyen_Klarna | 1 | 1.8% | 2 | 2.9% | +1 | +1.10pp |
| **Total** | **57** | **100%** | **70** | **100%** | **13** | - |

*% of Gap = Payment Method Gap / Total Gap*

---


---

*Report: 2026-05-19*
