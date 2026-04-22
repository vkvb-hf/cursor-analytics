# PCR Investigation: RTE 2026-W16

**Metric:** Payment Conversion Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 45.59% → 48.92% (+3.33pp)  
**Volume:** 56,978 payment visits  
**Threshold:** +1.66pp (0.5 × |Overall PCR Δ|)

## Executive Summary

**Overall:** Payment Conversion Rate improved significantly from 45.59% to 48.92% (+3.33pp), exceeding the threshold of +1.66pp, driven primarily by increased conversion at the Select Payment Method step.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | \|+3.43pp\| > 1.66pp | +3.43pp | ⚠️ |
| Click Submit Form | \|+1.40pp\| < 1.66pp | +1.40pp | ✅ |
| FE Validation Passed | \|+0.07pp\| < 1.66pp | +0.07pp | ✅ |
| Enter Fraud Service | \|-0.04pp\| < 1.66pp | -0.04pp | ✅ |
| Approved by Fraud Service | \|-0.40pp\| < 1.66pp | -0.40pp | ✅ |
| Call to PVS | \|+0.03pp\| < 1.66pp | +0.03pp | ✅ |
| Successful Checkout | \|-0.02pp\| < 1.66pp | -0.02pp | ✅ |

**Key Findings:**
- Select Payment Method conversion improved +3.43pp (56.25% → 59.68%), representing the primary driver of PCR improvement across all analyzed countries
- FJ contributed the largest volume impact with +5.15pp PCR improvement driven by Select Payment Method (+5.41pp), despite a -11.63% reduction in payment visits
- TT showed the highest PCR improvement (+10.94pp) with Select Payment Method conversion increasing +7.11pp and strong volume growth (+40.81%)
- Braintree_ApplePay success rate improved +4.34pp (87.67% → 92.01%), the largest gain among major payment methods
- YE was the only analyzed country showing PCR decline (-3.60pp), driven by Select Payment Method conversion drop (-4.09pp)

**Action:** Monitor — The PCR improvement is positive and primarily driven by upstream funnel improvements at the Select Payment Method step. Investigate the root cause of improvements in FJ and TT to determine if changes can be replicated, and monitor YE for continued decline.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 61,475 | 56,978 | -4,497 | -7.3% | - | - | - |
| Select Payment Method | 34,579 | 34,002 | -577 | -1.7% | 56.25% | 59.68% | +3.43pp |
| Click Submit Form | 31,676 | 31,624 | -52 | -0.2% | 91.60% | 93.01% | +1.40pp |
| FE Validation Passed | 30,889 | 30,859 | -30 | -0.1% | 97.52% | 97.58% | +0.07pp |
| Enter Fraud Service | 30,254 | 30,212 | -42 | -0.1% | 97.94% | 97.90% | -0.04pp |
| Approved by Fraud Service | 29,090 | 28,928 | -162 | -0.6% | 96.15% | 95.75% | -0.40pp |
| Call to PVS | 29,029 | 28,875 | -154 | -0.5% | 99.79% | 99.82% | +0.03pp |
| **Successful Checkout** | 28,027 | 27,872 | -155 | -0.6% | 96.55% | 96.53% | -0.02pp |
| **PCR Rate** | | | | | 45.59% | 48.92% | **+3.33pp** |

### Waterfall Backend

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 120,531 | 120,654 | 123 | 0.1% | - | - | - |
| Checkout Attempt | 47,320 | 47,481 | 161 | 0.3% | 39.26% | 39.35% | +0.09pp |
| Enter Fraud Service | 47,248 | 47,408 | 160 | 0.3% | 99.85% | 99.85% | -0.00pp |
| Approved by Fraud Service | 44,906 | 44,921 | 15 | 0.0% | 95.04% | 94.75% | -0.29pp |
| PVS Attempt | 44,168 | 44,111 | -57 | -0.1% | 98.36% | 98.20% | -0.16pp |
| PVS Success | 42,939 | 42,878 | -61 | -0.1% | 97.22% | 97.20% | -0.01pp |
| **Successful Checkout** | 43,273 | 43,889 | 616 | 1.4% | 100.78% | 102.36% | +1.58pp |
| **PCR Rate** | | | | | 35.90% | 36.38% | **+0.47pp** |

### Payment Method Breakdown

| Payment Method | 2026-W15 Attempt | 2026-W15 Success | 2026-W15 Rate | 2026-W16 Attempt | 2026-W16 Success | 2026-W16 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 18,823 | 17,485 | 92.89% | 18,972 | 17,585 | 92.69% | -0.20pp |
| Braintree_ApplePay | 11,163 | 9,787 | 87.67% | 10,851 | 9,984 | 92.01% | +4.34pp |
| Adyen_CreditCard | 10,764 | 9,877 | 91.76% | 10,595 | 9,736 | 91.89% | +0.13pp |
| Braintree_Paypal | 5,437 | 5,099 | 93.78% | 5,531 | 5,158 | 93.26% | -0.53pp |
| Adyen_IDeal | 628 | 581 | 92.52% | 1,060 | 1,009 | 95.19% | +2.67pp |
| Adyen_Klarna | 382 | 359 | 93.98% | 343 | 323 | 94.17% | +0.19pp |
| Braintree_CreditCard | 116 | 82 | 70.69% | 123 | 91 | 73.98% | +3.29pp |
|  | 3 | 0 | 0.00% | 3 | 0 | 0.00% | +0.00pp |
| Braintree_Venmo | 4 | 3 | 75.00% | 3 | 3 | 100.00% | +25.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (3 countries in RTE)

| Country | Volume | PCR 2026-W15 | PCR 2026-W16 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| FJ | 36,172 | 43.45% | 48.60% | +5.15pp | 1 | 2 |
| YE | 5,201 | 50.53% | 46.93% | -3.60pp | 2 | 3 |
| TT | 1,432 | 35.50% | 46.44% | +10.94pp | 3 | 1 |

---

### TT

#### Waterfall GA

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 1,017 | 1,432 | +415 | +40.81pp | - | - | - |
| Select Payment Method | 662 | 1,034 | +372 | +56.19pp | 65.09% | 72.21% | +7.11pp |
| Click Submit Form | 623 | 1,000 | +377 | +60.51pp | 94.11% | 96.71% | +2.60pp |
| FE Validation Passed | 626 | 1,000 | +374 | +59.74pp | 100.48% | 100.00% | -0.48pp |
| Enter Fraud Service | 624 | 995 | +371 | +59.46pp | 99.68% | 99.50% | -0.18pp |
| Approved by Fraud Service | 574 | 955 | +381 | +66.38pp | 91.99% | 95.98% | +3.99pp |
| Call to PVS | 574 | 957 | +383 | +66.72pp | 100.00% | 100.21% | +0.21pp |
| **Successful Checkout** | 361 | 665 | +304 | +84.21pp | 62.89% | 69.49% | +6.60pp |
| **PCR Rate** | | | | | 35.50% | 46.44% | **+10.94pp** |

**Key Driver:** Select Payment Method (+7.11pp)

#### Waterfall Backend

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 1,822 | 2,361 | +539 | +29.58pp | - | - | - |
| Checkout Attempt | 860 | 1,297 | +437 | +50.81pp | 47.20% | 54.93% | +7.73pp |
| Enter Fraud Service | 860 | 1,297 | +437 | +50.81pp | 100.00% | 100.00% | +0.00pp |
| Approved by Fraud Service | 786 | 1,224 | +438 | +55.73pp | 91.40% | 94.37% | +2.98pp |
| PVS Attempt | 788 | 1,223 | +435 | +55.20pp | 100.25% | 99.92% | -0.34pp |
| PVS Success | 588 | 985 | +397 | +67.52pp | 74.62% | 80.54% | +5.92pp |
| **Successful Checkout** | 785 | 1,221 | +436 | +55.54pp | 133.50% | 123.96% | -9.54pp |

**Key Driver:** Successful Checkout (-9.54pp)

---

### YE

#### Waterfall GA

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 4,880 | 5,201 | +321 | +6.58pp | - | - | - |
| Select Payment Method | 3,053 | 3,041 | -12 | -0.39pp | 62.56% | 58.47% | -4.09pp |
| Click Submit Form | 2,811 | 2,839 | +28 | +1.00pp | 92.07% | 93.36% | +1.28pp |
| FE Validation Passed | 2,781 | 2,789 | +8 | +0.29pp | 98.93% | 98.24% | -0.69pp |
| Enter Fraud Service | 2,655 | 2,661 | +6 | +0.23pp | 95.47% | 95.41% | -0.06pp |
| Approved by Fraud Service | 2,559 | 2,532 | -27 | -1.06pp | 96.38% | 95.15% | -1.23pp |
| Call to PVS | 2,547 | 2,528 | -19 | -0.75pp | 99.53% | 99.84% | +0.31pp |
| **Successful Checkout** | 2,466 | 2,441 | -25 | -1.01pp | 96.82% | 96.56% | -0.26pp |
| **PCR Rate** | | | | | 50.53% | 46.93% | **-3.60pp** |

**Key Driver:** Select Payment Method (-4.09pp)

#### Waterfall Backend

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 9,611 | 10,426 | +815 | +8.48pp | - | - | - |
| Checkout Attempt | 4,055 | 4,195 | +140 | +3.45pp | 42.19% | 40.24% | -1.96pp |
| Enter Fraud Service | 4,051 | 4,193 | +142 | +3.51pp | 99.90% | 99.95% | +0.05pp |
| Approved by Fraud Service | 3,862 | 3,962 | +100 | +2.59pp | 95.33% | 94.49% | -0.84pp |
| PVS Attempt | 3,655 | 3,713 | +58 | +1.59pp | 94.64% | 93.72% | -0.92pp |
| PVS Success | 3,559 | 3,609 | +50 | +1.40pp | 97.37% | 97.20% | -0.17pp |
| **Successful Checkout** | 3,774 | 3,878 | +104 | +2.76pp | 106.04% | 107.45% | +1.41pp |

**Key Driver:** Checkout Attempt (-1.96pp)

---

### FJ

#### Waterfall GA

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 40,932 | 36,172 | -4,760 | -11.63pp | - | - | - |
| Select Payment Method | 21,607 | 21,050 | -557 | -2.58pp | 52.79% | 58.19% | +5.41pp |
| Click Submit Form | 19,780 | 19,628 | -152 | -0.77pp | 91.54% | 93.24% | +1.70pp |
| FE Validation Passed | 19,162 | 19,081 | -81 | -0.42pp | 96.88% | 97.21% | +0.34pp |
| Enter Fraud Service | 18,891 | 18,778 | -113 | -0.60pp | 98.59% | 98.41% | -0.17pp |
| Approved by Fraud Service | 18,239 | 18,023 | -216 | -1.18pp | 96.55% | 95.98% | -0.57pp |
| Call to PVS | 18,225 | 17,998 | -227 | -1.25pp | 99.92% | 99.86% | -0.06pp |
| **Successful Checkout** | 17,784 | 17,581 | -203 | -1.14pp | 97.58% | 97.68% | +0.10pp |
| **PCR Rate** | | | | | 43.45% | 48.60% | **+5.16pp** |

**Key Driver:** Select Payment Method (+5.41pp)

#### Waterfall Backend

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 87,260 | 86,777 | -483 | -0.55pp | - | - | - |
| Checkout Attempt | 32,538 | 32,488 | -50 | -0.15pp | 37.29% | 37.44% | +0.15pp |
| Enter Fraud Service | 32,509 | 32,472 | -37 | -0.11pp | 99.91% | 99.95% | +0.04pp |
| Approved by Fraud Service | 31,016 | 30,882 | -134 | -0.43pp | 95.41% | 95.10% | -0.30pp |
| PVS Attempt | 30,930 | 30,779 | -151 | -0.49pp | 99.72% | 99.67% | -0.06pp |
| PVS Success | 30,227 | 30,067 | -160 | -0.53pp | 97.73% | 97.69% | -0.04pp |
| **Successful Checkout** | 30,296 | 30,170 | -126 | -0.42pp | 100.23% | 100.34% | +0.11pp |

**Key Driver:** Approved by Fraud Service (-0.30pp)

---





---

*Report: 2026-04-22*
