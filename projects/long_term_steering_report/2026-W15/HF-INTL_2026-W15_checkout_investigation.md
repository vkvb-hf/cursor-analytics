# PCR Investigation: HF-INTL 2026-W15

**Metric:** Payment Conversion Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 36.04% → 37.75% (+1.71pp)  
**Volume:** 69,804 payment visits  
**Threshold:** +0.86pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate improved by +1.71pp (36.04% → 37.75%) on 69,804 payment visits in 2026-W15, exceeding the significance threshold of +0.86pp.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Above threshold | +2.05pp | ✅ |
| Click Submit Form | Within normal range | +0.05pp | ✅ |
| FE Validation Passed | Within normal range | +0.24pp | ✅ |
| Enter Fraud Service | Within normal range | -0.06pp | ✅ |
| Approved by Fraud Service | Within normal range | +0.31pp | ✅ |
| Call to PVS | Within normal range | +0.24pp | ✅ |
| Successful Checkout | Within normal range | +0.18pp | ✅ |

**Key Findings:**
- Select Payment Method conversion was the primary driver of improvement, increasing +2.05pp (55.29% → 57.34%) at the cluster level
- GB and NO showed the strongest improvements: GB +2.46pp driven by Select Payment Method (+2.69pp), NO +5.83pp driven by Click Submit Form (+3.04pp) and Checkout Attempt (+6.87pp in backend)
- LU experienced a significant decline of -17.90pp, primarily due to Select Payment Method drop (-11.63pp), though volume is minimal (73 visits)
- Braintree_Paypal showed notable improvement (+0.92pp) while ProcessOut_CreditCard improved +0.58pp on the highest volume
- Backend data confirms the trend with Checkout Attempt improving +1.41pp (46.40% → 47.80%)

**Action:** Monitor — Positive trend driven by early-funnel improvements in Select Payment Method. Continue monitoring GB and NO performance while tracking LU for potential data quality issues given low volume.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 62,655 | 69,804 | 7,149 | 11.4% | - | - | - |
| Select Payment Method | 34,644 | 40,026 | 5,382 | 15.5% | 55.29% | 57.34% | +2.05pp |
| Click Submit Form | 28,133 | 32,523 | 4,390 | 15.6% | 81.21% | 81.25% | +0.05pp |
| FE Validation Passed | 26,335 | 30,521 | 4,186 | 15.9% | 93.61% | 93.84% | +0.24pp |
| Enter Fraud Service | 25,467 | 29,497 | 4,030 | 15.8% | 96.70% | 96.64% | -0.06pp |
| Approved by Fraud Service | 23,887 | 27,757 | 3,870 | 16.2% | 93.80% | 94.10% | +0.31pp |
| Call to PVS | 23,823 | 27,749 | 3,926 | 16.5% | 99.73% | 99.97% | +0.24pp |
| **Successful Checkout** | 22,582 | 26,353 | 3,771 | 16.7% | 94.79% | 94.97% | +0.18pp |
| **PCR Rate** | | | | | 36.04% | 37.75% | **+1.71pp** |

### Waterfall Backend

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 81,560 | 90,874 | 9,314 | 11.4% | - | - | - |
| Checkout Attempt | 37,841 | 43,442 | 5,601 | 14.8% | 46.40% | 47.80% | +1.41pp |
| Enter Fraud Service | 36,671 | 42,437 | 5,766 | 15.7% | 96.91% | 97.69% | +0.78pp |
| Approved by Fraud Service | 33,636 | 39,153 | 5,517 | 16.4% | 91.72% | 92.26% | +0.54pp |
| PVS Attempt | 31,465 | 36,514 | 5,049 | 16.0% | 93.55% | 93.26% | -0.29pp |
| PVS Success | 30,206 | 35,098 | 4,892 | 16.2% | 96.00% | 96.12% | +0.12pp |
| **Successful Checkout** | 32,545 | 37,822 | 5,277 | 16.2% | 107.74% | 107.76% | +0.02pp |
| **PCR Rate** | | | | | 39.90% | 41.62% | **+1.72pp** |

### Payment Method Breakdown

| Payment Method | 2026-W14 Attempt | 2026-W14 Success | 2026-W14 Rate | 2026-W15 Attempt | 2026-W15 Success | 2026-W15 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 14,680 | 12,973 | 88.37% | 16,221 | 14,429 | 88.95% | +0.58pp |
| Braintree_ApplePay | 10,592 | 9,049 | 85.43% | 12,470 | 10,644 | 85.36% | -0.08pp |
| Braintree_Paypal | 7,030 | 6,377 | 90.71% | 8,604 | 7,884 | 91.63% | +0.92pp |
| Adyen_Klarna | 1,481 | 1,394 | 94.13% | 2,047 | 1,935 | 94.53% | +0.40pp |
| ProcessOut_ApplePay | 1,213 | 1,098 | 90.52% | 1,474 | 1,342 | 91.04% | +0.53pp |
| Adyen_IDeal | 1,322 | 1,218 | 92.13% | 1,257 | 1,151 | 91.57% | -0.57pp |
| Adyen_Sepa | 1,024 | 3 | 0.29% | 835 | 0 | 0.00% | -0.29pp |
| Adyen_BcmcMobile | 384 | 368 | 95.83% | 388 | 370 | 95.36% | -0.47pp |
| Adyen_CreditCard | 69 | 63 | 91.30% | 74 | 63 | 85.14% | -6.17pp |
| NoPayment | 42 | 0 | 0.00% | 60 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (4 countries in HF-INTL)

| Country | Volume | PCR 2026-W14 | PCR 2026-W15 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| GB | 17,250 | 38.46% | 40.92% | +2.46pp | 1 | 5 |
| DE | 14,039 | 35.69% | 36.90% | +1.21pp | 2 | 11 |
| NO | 1,679 | 42.23% | 48.06% | +5.83pp | 5 | 2 |
| LU | 73 | 57.63% | 39.73% | -17.90pp | 11 | 1 |

---

### NO

#### Waterfall GA

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 708 | 1,679 | +971 | +137.15pp | - | - | - |
| Select Payment Method | 432 | 1,052 | +620 | +143.52pp | 61.02% | 62.66% | +1.64pp |
| Click Submit Form | 354 | 894 | +540 | +152.54pp | 81.94% | 84.98% | +3.04pp |
| FE Validation Passed | 339 | 877 | +538 | +158.70pp | 95.76% | 98.10% | +2.34pp |
| Enter Fraud Service | 328 | 858 | +530 | +161.59pp | 96.76% | 97.83% | +1.08pp |
| Approved by Fraud Service | 308 | 826 | +518 | +168.18pp | 93.90% | 96.27% | +2.37pp |
| Call to PVS | 306 | 826 | +520 | +169.93pp | 99.35% | 100.00% | +0.65pp |
| **Successful Checkout** | 299 | 807 | +508 | +169.90pp | 97.71% | 97.70% | -0.01pp |
| **PCR Rate** | | | | | 42.23% | 48.06% | **+5.83pp** |

**Key Driver:** Click Submit Form (+3.04pp)

#### Waterfall Backend

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 1,017 | 2,244 | +1,227 | +120.65pp | - | - | - |
| Checkout Attempt | 484 | 1,222 | +738 | +152.48pp | 47.59% | 54.46% | +6.87pp |
| Enter Fraud Service | 481 | 1,218 | +737 | +153.22pp | 99.38% | 99.67% | +0.29pp |
| Approved by Fraud Service | 448 | 1,155 | +707 | +157.81pp | 93.14% | 94.83% | +1.69pp |
| PVS Attempt | 415 | 1,030 | +615 | +148.19pp | 92.63% | 89.18% | -3.46pp |
| PVS Success | 405 | 1,004 | +599 | +147.90pp | 97.59% | 97.48% | -0.11pp |
| **Successful Checkout** | 438 | 1,129 | +691 | +157.76pp | 108.15% | 112.45% | +4.30pp |

**Key Driver:** Checkout Attempt (+6.87pp)

---

### DE

#### Waterfall GA

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 11,201 | 14,039 | +2,838 | +25.34pp | - | - | - |
| Select Payment Method | 6,594 | 8,621 | +2,027 | +30.74pp | 58.87% | 61.41% | +2.54pp |
| Click Submit Form | 5,180 | 6,654 | +1,474 | +28.46pp | 78.56% | 77.18% | -1.37pp |
| FE Validation Passed | 4,939 | 6,360 | +1,421 | +28.77pp | 95.35% | 95.58% | +0.23pp |
| Enter Fraud Service | 4,630 | 5,984 | +1,354 | +29.24pp | 93.74% | 94.09% | +0.34pp |
| Approved by Fraud Service | 4,417 | 5,742 | +1,325 | +30.00pp | 95.40% | 95.96% | +0.56pp |
| Call to PVS | 4,376 | 5,719 | +1,343 | +30.69pp | 99.07% | 99.60% | +0.53pp |
| **Successful Checkout** | 3,998 | 5,180 | +1,182 | +29.56pp | 91.36% | 90.58% | -0.79pp |
| **PCR Rate** | | | | | 35.69% | 36.90% | **+1.20pp** |

**Key Driver:** Select Payment Method (+2.54pp)

#### Waterfall Backend

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 15,216 | 19,227 | +4,011 | +26.36pp | - | - | - |
| Checkout Attempt | 7,189 | 9,186 | +1,997 | +27.78pp | 47.25% | 47.78% | +0.53pp |
| Enter Fraud Service | 7,159 | 9,159 | +2,000 | +27.94pp | 99.58% | 99.71% | +0.12pp |
| Approved by Fraud Service | 6,732 | 8,660 | +1,928 | +28.64pp | 94.04% | 94.55% | +0.52pp |
| PVS Attempt | 6,652 | 8,608 | +1,956 | +29.40pp | 98.81% | 99.40% | +0.59pp |
| PVS Success | 6,183 | 7,996 | +1,813 | +29.32pp | 92.95% | 92.89% | -0.06pp |
| **Successful Checkout** | 6,593 | 8,497 | +1,904 | +28.88pp | 106.63% | 106.27% | -0.37pp |

**Key Driver:** PVS Attempt (+0.59pp)

---

### GB

#### Waterfall GA

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 15,598 | 17,250 | +1,652 | +10.59pp | - | - | - |
| Select Payment Method | 8,896 | 10,303 | +1,407 | +15.82pp | 57.03% | 59.73% | +2.69pp |
| Click Submit Form | 7,243 | 8,447 | +1,204 | +16.62pp | 81.42% | 81.99% | +0.57pp |
| FE Validation Passed | 6,616 | 7,720 | +1,104 | +16.69pp | 91.34% | 91.39% | +0.05pp |
| Enter Fraud Service | 6,450 | 7,537 | +1,087 | +16.85pp | 97.49% | 97.63% | +0.14pp |
| Approved by Fraud Service | 6,103 | 7,174 | +1,071 | +17.55pp | 94.62% | 95.18% | +0.56pp |
| Call to PVS | 6,101 | 7,176 | +1,075 | +17.62pp | 99.97% | 100.03% | +0.06pp |
| **Successful Checkout** | 5,999 | 7,059 | +1,060 | +17.67pp | 98.33% | 98.37% | +0.04pp |
| **PCR Rate** | | | | | 38.46% | 40.92% | **+2.46pp** |

**Key Driver:** Select Payment Method (+2.69pp)

#### Waterfall Backend

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 18,731 | 21,082 | +2,351 | +12.55pp | - | - | - |
| Checkout Attempt | 8,933 | 10,599 | +1,666 | +18.65pp | 47.69% | 50.28% | +2.58pp |
| Enter Fraud Service | 8,884 | 10,536 | +1,652 | +18.60pp | 99.45% | 99.41% | -0.05pp |
| Approved by Fraud Service | 8,247 | 9,841 | +1,594 | +19.33pp | 92.83% | 93.40% | +0.57pp |
| PVS Attempt | 6,795 | 8,125 | +1,330 | +19.57pp | 82.39% | 82.56% | +0.17pp |
| PVS Success | 6,687 | 7,993 | +1,306 | +19.53pp | 98.41% | 98.38% | -0.04pp |
| **Successful Checkout** | 8,151 | 9,726 | +1,575 | +19.32pp | 121.89% | 121.68% | -0.21pp |

**Key Driver:** Checkout Attempt (+2.58pp)

---

### LU

#### Waterfall GA

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 59 | 73 | +14 | +23.73pp | - | - | - |
| Select Payment Method | 40 | 41 | +1 | +2.50pp | 67.80% | 56.16% | -11.63pp |
| Click Submit Form | 37 | 34 | -3 | -8.11pp | 92.50% | 82.93% | -9.57pp |
| FE Validation Passed | 35 | 31 | -4 | -11.43pp | 94.59% | 91.18% | -3.42pp |
| Enter Fraud Service | 35 | 31 | -4 | -11.43pp | 100.00% | 100.00% | +0.00pp |
| Approved by Fraud Service | 35 | 31 | -4 | -11.43pp | 100.00% | 100.00% | +0.00pp |
| Call to PVS | 35 | 30 | -5 | -14.29pp | 100.00% | 96.77% | -3.23pp |
| **Successful Checkout** | 34 | 29 | -5 | -14.71pp | 97.14% | 96.67% | -0.48pp |
| **PCR Rate** | | | | | 57.63% | 39.73% | **-17.90pp** |

**Key Driver:** Select Payment Method (-11.63pp)

#### Waterfall Backend

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 256 | 279 | +23 | +8.98pp | - | - | - |
| Checkout Attempt | 75 | 72 | -3 | -4.00pp | 29.30% | 25.81% | -3.49pp |
| Enter Fraud Service | 62 | 66 | +4 | +6.45pp | 82.67% | 91.67% | +9.00pp |
| Approved by Fraud Service | 62 | 65 | +3 | +4.84pp | 100.00% | 98.48% | -1.52pp |
| PVS Attempt | 61 | 63 | +2 | +3.28pp | 98.39% | 96.92% | -1.46pp |
| PVS Success | 60 | 63 | +3 | +5.00pp | 98.36% | 100.00% | +1.64pp |
| **Successful Checkout** | 73 | 69 | -4 | -5.48pp | 121.67% | 109.52% | -12.14pp |

**Key Driver:** Successful Checkout (-12.14pp)

---





---

*Report: 2026-04-15*
