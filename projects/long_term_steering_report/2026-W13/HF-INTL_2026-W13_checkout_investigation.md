# PCR Investigation: HF-INTL 2026-W13

**Metric:** Payment Conversion Rate  
**Period:** 2026-W12 → 2026-W13  
**Observation:** 34.47% → 34.88% (+0.41pp)  
**Volume:** 82,373 payment visits  
**Threshold:** +0.20pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate improved from 34.47% to 34.88% (+0.41pp) on 82,373 payment visits, exceeding the +0.20pp threshold for investigation.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Volume & Rate | +1.00pp | ✅ |
| Click Submit Form | Rate | +0.38pp | ✅ |
| FE Validation Passed | Rate | -0.10pp | ✅ |
| Enter Fraud Service | Rate | +0.18pp | ✅ |
| Approved by Fraud Service | Rate | -0.09pp | ✅ |
| Call to PVS | Rate | +0.26pp | ✅ |
| Successful Checkout | Rate | -1.30pp | ⚠️ |

**Key Findings:**
- The +1.00pp improvement in Select Payment Method was the primary driver of overall PCR gains, with GB contributing +0.88pp at this step
- Successful Checkout conversion dropped -1.30pp despite upstream improvements, driven by a 75% increase in PVS failures (872 → 1,530 total failures)
- DE experienced a significant -6.63pp drop at Successful Checkout despite +6.57% volume growth, with PVS Success falling -6.06pp in backend data
- "Refused: Refused" errors increased by +132 cases (+7.10pp share), and "Cancelled: Cancelled" rose by +154 cases (+5.87pp share)
- Adyen_IDeal (-2.63pp) and Adyen_Klarna (-1.92pp) showed notable conversion declines, while Adyen_CreditCard dropped -11.25pp on reduced volume (906 → 116 attempts)

**Action:** Investigate — The -1.30pp Successful Checkout degradation and 75% increase in PVS failures require immediate investigation, particularly the surge in "Refused" and "Cancelled" errors. Focus analysis on DE payment processing issues and Adyen payment method performance.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 80,204 | 82,373 | 2,169 | 2.7% | - | - | - |
| Select Payment Method | 43,208 | 45,198 | 1,990 | 4.6% | 53.87% | 54.87% | +1.00pp |
| Click Submit Form | 34,670 | 36,437 | 1,767 | 5.1% | 80.24% | 80.62% | +0.38pp |
| FE Validation Passed | 32,251 | 33,860 | 1,609 | 5.0% | 93.02% | 92.93% | -0.10pp |
| Enter Fraud Service | 31,002 | 32,610 | 1,608 | 5.2% | 96.13% | 96.31% | +0.18pp |
| Approved by Fraud Service | 29,153 | 30,636 | 1,483 | 5.1% | 94.04% | 93.95% | -0.09pp |
| Call to PVS | 29,026 | 30,582 | 1,556 | 5.4% | 99.56% | 99.82% | +0.26pp |
| **Successful Checkout** | 27,647 | 28,731 | 1,084 | 3.9% | 95.25% | 93.95% | -1.30pp |
| **PCR Rate** | | | | | 34.47% | 34.88% | **+0.41pp** |

### Waterfall Backend

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 103,212 | 106,120 | 2,908 | 2.8% | - | - | - |
| Checkout Attempt | 45,460 | 47,601 | 2,141 | 4.7% | 44.05% | 44.86% | +0.81pp |
| Enter Fraud Service | 44,204 | 46,295 | 2,091 | 4.7% | 97.24% | 97.26% | +0.02pp |
| Approved by Fraud Service | 40,666 | 42,663 | 1,997 | 4.9% | 92.00% | 92.15% | +0.16pp |
| PVS Attempt | 38,136 | 39,598 | 1,462 | 3.8% | 93.78% | 92.82% | -0.96pp |
| PVS Success | 36,870 | 37,702 | 832 | 2.3% | 96.68% | 95.21% | -1.47pp |
| **Successful Checkout** | 39,131 | 41,021 | 1,890 | 4.8% | 106.13% | 108.80% | +2.67pp |
| **PCR Rate** | | | | | 37.91% | 38.66% | **+0.74pp** |

### Payment Method Breakdown

| Payment Method | 2026-W12 Attempt | 2026-W12 Success | 2026-W12 Rate | 2026-W13 Attempt | 2026-W13 Success | 2026-W13 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 16,784 | 14,775 | 88.03% | 17,791 | 15,715 | 88.33% | +0.30pp |
| Braintree_ApplePay | 12,342 | 10,302 | 83.47% | 13,360 | 11,186 | 83.73% | +0.26pp |
| Braintree_Paypal | 9,374 | 8,559 | 91.31% | 9,125 | 8,314 | 91.11% | -0.19pp |
| Adyen_Klarna | 1,022 | 989 | 96.77% | 2,195 | 2,082 | 94.85% | -1.92pp |
| Adyen_IDeal | 1,772 | 1,673 | 94.41% | 1,887 | 1,732 | 91.79% | -2.63pp |
| ProcessOut_ApplePay | 1,847 | 1,692 | 91.61% | 1,558 | 1,429 | 91.72% | +0.11pp |
| Adyen_Sepa | 1,092 | 1 | 0.09% | 984 | 2 | 0.20% | +0.11pp |
| Adyen_BcmcMobile | 279 | 257 | 92.11% | 475 | 460 | 96.84% | +4.73pp |
| Adyen_CreditCard | 906 | 883 | 97.46% | 116 | 100 | 86.21% | -11.25pp |
| NoPayment | 39 | 0 | 0.00% | 105 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (4 countries in HF-INTL)

| Country | Volume | PCR 2026-W12 | PCR 2026-W13 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| GB | 20,468 | 37.26% | 38.73% | +1.47pp | 1 | 8 |
| DE | 15,048 | 36.70% | 34.92% | -1.78pp | 2 | 7 |
| NO | 1,096 | 49.14% | 45.16% | -3.98pp | 8 | 2 |
| CH | 500 | 20.00% | 24.60% | +4.60pp | 11 | 1 |

---

### NO

#### Waterfall GA

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 1,221 | 1,096 | -125 | -10.24pp | - | - | - |
| Select Payment Method | 764 | 674 | -90 | -11.78pp | 62.57% | 61.50% | -1.08pp |
| Click Submit Form | 661 | 571 | -90 | -13.62pp | 86.52% | 84.72% | -1.80pp |
| FE Validation Passed | 652 | 554 | -98 | -15.03pp | 98.64% | 97.02% | -1.62pp |
| Enter Fraud Service | 645 | 537 | -108 | -16.74pp | 98.93% | 96.93% | -1.99pp |
| Approved by Fraud Service | 616 | 506 | -110 | -17.86pp | 95.50% | 94.23% | -1.28pp |
| Call to PVS | 607 | 508 | -99 | -16.31pp | 98.54% | 100.40% | +1.86pp |
| **Successful Checkout** | 600 | 495 | -105 | -17.50pp | 98.85% | 97.44% | -1.41pp |
| **PCR Rate** | | | | | 49.14% | 45.16% | **-3.98pp** |

**Key Driver:** Enter Fraud Service (-1.99pp)

#### Waterfall Backend

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 1,637 | 1,465 | -172 | -10.51pp | - | - | - |
| Checkout Attempt | 885 | 718 | -167 | -18.87pp | 54.06% | 49.01% | -5.05pp |
| Enter Fraud Service | 884 | 716 | -168 | -19.00pp | 99.89% | 99.72% | -0.17pp |
| Approved by Fraud Service | 823 | 666 | -157 | -19.08pp | 93.10% | 93.02% | -0.08pp |
| PVS Attempt | 738 | 540 | -198 | -26.83pp | 89.67% | 81.08% | -8.59pp |
| PVS Success | 720 | 522 | -198 | -27.50pp | 97.56% | 96.67% | -0.89pp |
| **Successful Checkout** | 813 | 653 | -160 | -19.68pp | 112.92% | 125.10% | +12.18pp |

**Key Driver:** Successful Checkout (+12.18pp)

---

### CH

#### Waterfall GA

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 570 | 500 | -70 | -12.28pp | - | - | - |
| Select Payment Method | 220 | 200 | -20 | -9.09pp | 38.60% | 40.00% | +1.40pp |
| Click Submit Form | 151 | 150 | -1 | -0.66pp | 68.64% | 75.00% | +6.36pp |
| FE Validation Passed | 131 | 140 | +9 | +6.87pp | 86.75% | 93.33% | +6.58pp |
| Enter Fraud Service | 123 | 135 | +12 | +9.76pp | 93.89% | 96.43% | +2.54pp |
| Approved by Fraud Service | 119 | 131 | +12 | +10.08pp | 96.75% | 97.04% | +0.29pp |
| Call to PVS | 118 | 131 | +13 | +11.02pp | 99.16% | 100.00% | +0.84pp |
| **Successful Checkout** | 114 | 123 | +9 | +7.89pp | 96.61% | 93.89% | -2.72pp |
| **PCR Rate** | | | | | 20.00% | 24.60% | **+4.60pp** |

**Key Driver:** FE Validation Passed (+6.58pp)

#### Waterfall Backend

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 830 | 745 | -85 | -10.24pp | - | - | - |
| Checkout Attempt | 175 | 181 | +6 | +3.43pp | 21.08% | 24.30% | +3.21pp |
| Enter Fraud Service | 171 | 177 | +6 | +3.51pp | 97.71% | 97.79% | +0.08pp |
| Approved by Fraud Service | 160 | 172 | +12 | +7.50pp | 93.57% | 97.18% | +3.61pp |
| PVS Attempt | 159 | 172 | +13 | +8.18pp | 99.38% | 100.00% | +0.62pp |
| PVS Success | 150 | 165 | +15 | +10.00pp | 94.34% | 95.93% | +1.59pp |
| **Successful Checkout** | 152 | 166 | +14 | +9.21pp | 101.33% | 100.61% | -0.73pp |

**Key Driver:** Approved by Fraud Service (+3.61pp)

---

### DE

#### Waterfall GA

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 14,120 | 15,048 | +928 | +6.57pp | - | - | - |
| Select Payment Method | 8,401 | 9,083 | +682 | +8.12pp | 59.50% | 60.36% | +0.86pp |
| Click Submit Form | 6,531 | 6,999 | +468 | +7.17pp | 77.74% | 77.06% | -0.68pp |
| FE Validation Passed | 6,135 | 6,635 | +500 | +8.15pp | 93.94% | 94.80% | +0.86pp |
| Enter Fraud Service | 5,673 | 6,177 | +504 | +8.88pp | 92.47% | 93.10% | +0.63pp |
| Approved by Fraud Service | 5,441 | 5,927 | +486 | +8.93pp | 95.91% | 95.95% | +0.04pp |
| Call to PVS | 5,415 | 5,900 | +485 | +8.96pp | 99.52% | 99.54% | +0.02pp |
| **Successful Checkout** | 5,182 | 5,255 | +73 | +1.41pp | 95.70% | 89.07% | -6.63pp |
| **PCR Rate** | | | | | 36.70% | 34.92% | **-1.78pp** |

**Key Driver:** Successful Checkout (-6.63pp)

#### Waterfall Backend

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 19,088 | 20,193 | +1,105 | +5.79pp | - | - | - |
| Checkout Attempt | 8,704 | 9,329 | +625 | +7.18pp | 45.60% | 46.20% | +0.60pp |
| Enter Fraud Service | 8,675 | 9,285 | +610 | +7.03pp | 99.67% | 99.53% | -0.14pp |
| Approved by Fraud Service | 8,132 | 8,753 | +621 | +7.64pp | 93.74% | 94.27% | +0.53pp |
| PVS Attempt | 8,070 | 8,690 | +620 | +7.68pp | 99.24% | 99.28% | +0.04pp |
| PVS Success | 7,835 | 7,910 | +75 | +0.96pp | 97.09% | 91.02% | -6.06pp |
| **Successful Checkout** | 7,897 | 8,508 | +611 | +7.74pp | 100.79% | 107.56% | +6.77pp |

**Key Driver:** Successful Checkout (+6.77pp)

---

### GB

#### Waterfall GA

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 18,635 | 20,468 | +1,833 | +9.84pp | - | - | - |
| Select Payment Method | 10,631 | 11,857 | +1,226 | +11.53pp | 57.05% | 57.93% | +0.88pp |
| Click Submit Form | 8,583 | 9,655 | +1,072 | +12.49pp | 80.74% | 81.43% | +0.69pp |
| FE Validation Passed | 7,772 | 8,755 | +983 | +12.65pp | 90.55% | 90.68% | +0.13pp |
| Enter Fraud Service | 7,562 | 8,533 | +971 | +12.84pp | 97.30% | 97.46% | +0.17pp |
| Approved by Fraud Service | 7,113 | 8,076 | +963 | +13.54pp | 94.06% | 94.64% | +0.58pp |
| Call to PVS | 7,079 | 8,064 | +985 | +13.91pp | 99.52% | 99.85% | +0.33pp |
| **Successful Checkout** | 6,943 | 7,927 | +984 | +14.17pp | 98.08% | 98.30% | +0.22pp |
| **PCR Rate** | | | | | 37.26% | 38.73% | **+1.47pp** |

**Key Driver:** Select Payment Method (+0.88pp)

#### Waterfall Backend

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 22,638 | 24,536 | +1,898 | +8.38pp | - | - | - |
| Checkout Attempt | 10,604 | 11,820 | +1,216 | +11.47pp | 46.84% | 48.17% | +1.33pp |
| Enter Fraud Service | 10,558 | 11,658 | +1,100 | +10.42pp | 99.57% | 98.63% | -0.94pp |
| Approved by Fraud Service | 9,718 | 10,822 | +1,104 | +11.36pp | 92.04% | 92.83% | +0.79pp |
| PVS Attempt | 8,285 | 8,901 | +616 | +7.44pp | 85.25% | 82.25% | -3.01pp |
| PVS Success | 8,134 | 8,738 | +604 | +7.43pp | 98.18% | 98.17% | -0.01pp |
| **Successful Checkout** | 9,583 | 10,725 | +1,142 | +11.92pp | 117.81% | 122.74% | +4.93pp |

**Key Driver:** Successful Checkout (+4.93pp)

---



## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (-1.30pp) meets threshold (+0.20pp)

| Decline Reason | 2026-W12 | 2026-W12 % | 2026-W13 | 2026-W13 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| RedirectShopper | 223 | 25.6% | 455 | 29.7% | +232 | +4.17pp |
| Failed Verification: Insufficient Funds | 215 | 24.7% | 263 | 17.2% | +48 | -7.47pp |
| Cancelled: Cancelled | 85 | 9.7% | 239 | 15.6% | +154 | +5.87pp |
| Refused: Refused | 31 | 3.6% | 163 | 10.7% | +132 | +7.10pp |
| Failed Verification: Declined | 110 | 12.6% | 130 | 8.5% | +20 | -4.12pp |
| Pending | 58 | 6.7% | 128 | 8.4% | +70 | +1.71pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 107 | 12.3% | 103 | 6.7% | -4 | -5.54pp |
| Failed Verification: Security | 22 | 2.5% | 25 | 1.6% | +3 | -0.89pp |
| Failed Verification: 200 OK: 05 : Do not honor | 11 | 1.3% | 13 | 0.8% | +2 | -0.41pp |
| Failed Verification: OK: 79 : Life cycle | 10 | 1.1% | 11 | 0.7% | +1 | -0.43pp |
| **Total PVS Failures** | **872** | **100%** | **1,530** | **100%** | **+658** | - |

---


---

*Report: 2026-04-10*
