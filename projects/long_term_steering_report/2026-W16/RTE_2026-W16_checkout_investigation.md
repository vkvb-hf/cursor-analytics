# PCR Investigation: RTE 2026-W16

**Metric:** Payment Conversion Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 45.59% → 48.93% (+3.34pp)  
**Volume:** 56,958 payment visits  
**Threshold:** +1.67pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate improved significantly from 45.59% to 48.93% (+3.34pp) in W16, driven primarily by gains in early funnel engagement at the Select Payment Method step.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | >1.67pp threshold | +3.44pp | ⚠️ |
| Click Submit Form | >1.67pp threshold | +1.41pp | ✅ |
| FE Validation Passed | Within threshold | +0.06pp | ✅ |
| Enter Fraud Service | Within threshold | -0.04pp | ✅ |
| Approved by Fraud Service | Within threshold | -0.45pp | ✅ |
| Call to PVS | Within threshold | +0.07pp | ✅ |
| Successful Checkout | Within threshold | -0.02pp | ✅ |

**Key Findings:**
- Select Payment Method conversion improved +3.44pp (56.25% → 59.69%), exceeding the 1.67pp threshold and accounting for the majority of the PCR gain
- FJ drove the largest contribution with +5.17pp PCR improvement (43.45% → 48.62%), primarily from Select Payment Method (+5.42pp)
- TT showed the highest absolute change at +10.94pp PCR improvement, with strong gains at Select Payment Method (+7.11pp) and Successful Checkout (+6.60pp)
- YE was the only country showing decline (-3.56pp), with Select Payment Method dropping -4.07pp
- Braintree_ApplePay showed notable success rate improvement (+4.34pp, from 87.67% to 92.01%)

**Action:** Monitor - The improvement is positive and primarily driven by top-of-funnel engagement gains. Continue monitoring FJ and TT performance while investigating the YE decline in Select Payment Method conversion.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 61,475 | 56,958 | -4,517 | -7.3% | - | - | - |
| Select Payment Method | 34,579 | 33,996 | -583 | -1.7% | 56.25% | 59.69% | +3.44pp |
| Click Submit Form | 31,676 | 31,622 | -54 | -0.2% | 91.60% | 93.02% | +1.41pp |
| FE Validation Passed | 30,889 | 30,856 | -33 | -0.1% | 97.52% | 97.58% | +0.06pp |
| Enter Fraud Service | 30,254 | 30,210 | -44 | -0.1% | 97.94% | 97.91% | -0.04pp |
| Approved by Fraud Service | 29,089 | 28,912 | -177 | -0.6% | 96.15% | 95.70% | -0.45pp |
| Call to PVS | 29,029 | 28,872 | -157 | -0.5% | 99.79% | 99.86% | +0.07pp |
| **Successful Checkout** | 28,027 | 27,871 | -156 | -0.6% | 96.55% | 96.53% | -0.02pp |
| **PCR Rate** | | | | | 45.59% | 48.93% | **+3.34pp** |

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
| FJ | 36,164 | 43.45% | 48.62% | +5.17pp | 1 | 2 |
| YE | 5,197 | 50.53% | 46.97% | -3.56pp | 2 | 3 |
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
| Payment Visits | 4,880 | 5,197 | +317 | +6.50pp | - | - | - |
| Select Payment Method | 3,053 | 3,040 | -13 | -0.43pp | 62.56% | 58.50% | -4.07pp |
| Click Submit Form | 2,811 | 2,839 | +28 | +1.00pp | 92.07% | 93.39% | +1.31pp |
| FE Validation Passed | 2,781 | 2,789 | +8 | +0.29pp | 98.93% | 98.24% | -0.69pp |
| Enter Fraud Service | 2,655 | 2,661 | +6 | +0.23pp | 95.47% | 95.41% | -0.06pp |
| Approved by Fraud Service | 2,559 | 2,532 | -27 | -1.06pp | 96.38% | 95.15% | -1.23pp |
| Call to PVS | 2,547 | 2,528 | -19 | -0.75pp | 99.53% | 99.84% | +0.31pp |
| **Successful Checkout** | 2,466 | 2,441 | -25 | -1.01pp | 96.82% | 96.56% | -0.26pp |
| **PCR Rate** | | | | | 50.53% | 46.97% | **-3.56pp** |

**Key Driver:** Select Payment Method (-4.07pp)

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
| Payment Visits | 40,932 | 36,164 | -4,768 | -11.65pp | - | - | - |
| Select Payment Method | 21,607 | 21,049 | -558 | -2.58pp | 52.79% | 58.20% | +5.42pp |
| Click Submit Form | 19,780 | 19,630 | -150 | -0.76pp | 91.54% | 93.26% | +1.71pp |
| FE Validation Passed | 19,162 | 19,082 | -80 | -0.42pp | 96.88% | 97.21% | +0.33pp |
| Enter Fraud Service | 18,891 | 18,780 | -111 | -0.59pp | 98.59% | 98.42% | -0.17pp |
| Approved by Fraud Service | 18,238 | 18,013 | -225 | -1.23pp | 96.54% | 95.92% | -0.63pp |
| Call to PVS | 18,225 | 17,999 | -226 | -1.24pp | 99.93% | 99.92% | -0.01pp |
| **Successful Checkout** | 17,784 | 17,584 | -200 | -1.12pp | 97.58% | 97.69% | +0.11pp |
| **PCR Rate** | | | | | 43.45% | 48.62% | **+5.18pp** |

**Key Driver:** Select Payment Method (+5.42pp)

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

*Report: 2026-04-21*
