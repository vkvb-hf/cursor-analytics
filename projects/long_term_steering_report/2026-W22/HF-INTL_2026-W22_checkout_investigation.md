# PCR Investigation: HF-INTL 2026-W22

**Metric:** Payment Conversion Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 34.93% → 36.88% (+1.95pp)  
**Volume:** 59,503 payment visits  
**Threshold:** +0.98pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate improved significantly from 34.93% to 36.88% (+1.95pp) in HF-INTL during 2026-W22, driven primarily by gains in the early funnel stages.

**Funnel Analysis (GA):**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ≥ ±0.98pp | +1.77pp | ⚠️ |
| Click Submit Form | ≥ ±0.98pp | +0.72pp | ✅ |
| FE Validation Passed | ≥ ±0.98pp | +0.71pp | ✅ |
| Enter Fraud Service | ≥ ±0.98pp | +0.17pp | ✅ |
| Approved by Fraud Service | ≥ ±0.98pp | +0.18pp | ✅ |
| Call to PVS | ≥ ±0.98pp | +0.11pp | ✅ |
| Successful Checkout | ≥ ±0.98pp | +0.12pp | ✅ |

**Key Findings:**
- **IE showed exceptional improvement** (+10.86pp PCR), driven by Click Submit Form (+7.70pp) and Select Payment Method (+6.54pp), contributing most significantly to the overall gain
- **Select Payment Method** was the primary driver of overall improvement at +1.77pp, exceeding the threshold across the cluster
- **Backend data anomaly detected:** Payment Method Listed and Successful Checkout show 0 values for 2026-W22, indicating a potential logging or data pipeline issue rather than actual payment failures
- **NO experienced a decline** (-2.45pp PCR) despite increased volume (+39.82%), primarily due to Click Submit Form drop (-5.65pp)
- **FR improved moderately** (+2.44pp PCR) with Select Payment Method (+3.07pp) as the key driver

**Action:** Investigate — The backend data shows critical anomalies (0 values across all payment methods for 2026-W22) that require immediate investigation of the data pipeline. The GA data indicates genuine funnel improvements, but backend discrepancies must be resolved to confirm the actual payment success rates.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 61,296 | 59,503 | -1,793 | -2.9% | - | - | - |
| Select Payment Method | 33,424 | 33,501 | 77 | 0.2% | 54.53% | 56.30% | +1.77pp |
| Click Submit Form | 26,947 | 27,251 | 304 | 1.1% | 80.62% | 81.34% | +0.72pp |
| FE Validation Passed | 25,215 | 25,692 | 477 | 1.9% | 93.57% | 94.28% | +0.71pp |
| Enter Fraud Service | 24,300 | 24,803 | 503 | 2.1% | 96.37% | 96.54% | +0.17pp |
| Approved by Fraud Service | 23,040 | 23,561 | 521 | 2.3% | 94.81% | 94.99% | +0.18pp |
| Call to PVS | 22,912 | 23,455 | 543 | 2.4% | 99.44% | 99.55% | +0.11pp |
| **Successful Checkout** | 21,411 | 21,946 | 535 | 2.5% | 93.45% | 93.57% | +0.12pp |
| **PCR Rate** | | | | | 34.93% | 36.88% | **+1.95pp** |

### Waterfall Backend

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 74,901 | 0 | -74,901 | -100.0% | - | - | - |
| Checkout Attempt | 34,915 | 31,534 | -3,381 | -9.7% | 46.61% | 0.00% | -46.61pp |
| Enter Fraud Service | 33,327 | 30,612 | -2,715 | -8.1% | 95.45% | 97.08% | +1.62pp |
| Approved by Fraud Service | 30,985 | 28,543 | -2,442 | -7.9% | 92.97% | 93.24% | +0.27pp |
| PVS Attempt | 28,205 | 25,404 | -2,801 | -9.9% | 91.03% | 89.00% | -2.03pp |
| PVS Success | 26,435 | 24,006 | -2,429 | -9.2% | 93.72% | 94.50% | +0.77pp |
| **Successful Checkout** | 28,793 | 0 | -28,793 | -100.0% | 108.92% | 0.00% | -108.92pp |
| **PCR Rate** | | | | | 38.44% | 0.00% | **-38.44pp** |

### Payment Method Breakdown

| Payment Method | 2026-W21 Attempt | 2026-W21 Success | 2026-W21 Rate | 2026-W22 Attempt | 2026-W22 Success | 2026-W22 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 10,902 | 9,571 | 87.79% | 10,163 | 0 | 0.00% | -87.79pp |
| Braintree_ApplePay | 9,293 | 6,889 | 74.13% | 8,878 | 0 | 0.00% | -74.13pp |
| Braintree_Paypal | 5,993 | 5,543 | 92.49% | 5,014 | 0 | 0.00% | -92.49pp |
| Adyen_Klarna | 2,250 | 2,113 | 93.91% | 1,760 | 0 | 0.00% | -93.91pp |
| Adyen_CreditCard | 1,377 | 1,345 | 97.68% | 1,705 | 0 | 0.00% | -97.68pp |
| ProcessOut_ApplePay | 1,546 | 1,387 | 89.72% | 1,311 | 0 | 0.00% | -89.72pp |
| Adyen_IDeal | 1,016 | 937 | 92.22% | 1,017 | 0 | 0.00% | -92.22pp |
| Adyen_Sepa | 1,404 | 2 | 0.14% | 791 | 0 | 0.00% | -0.14pp |
| Adyen_BcmcMobile | 707 | 660 | 93.35% | 717 | 0 | 0.00% | -93.35pp |
| ProcessOut_Mobilepay | 219 | 210 | 95.89% | 60 | 0 | 0.00% | -95.89pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (3 countries in HF-INTL)

| Country | Volume | PCR 2026-W21 | PCR 2026-W22 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| IE | 2,983 | 36.27% | 47.13% | +10.86pp | 1 | 1 |
| FR | 12,593 | 28.89% | 31.33% | +2.44pp | 2 | 4 |
| NO | 1,257 | 47.72% | 45.27% | -2.45pp | 6 | 2 |

---

### NO

#### Waterfall GA

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 899 | 1,257 | +358 | +39.82pp | - | - | - |
| Select Payment Method | 539 | 769 | +230 | +42.67pp | 59.96% | 61.18% | +1.22pp |
| Click Submit Form | 465 | 620 | +155 | +33.33pp | 86.27% | 80.62% | -5.65pp |
| FE Validation Passed | 451 | 601 | +150 | +33.26pp | 96.99% | 96.94% | -0.05pp |
| Enter Fraud Service | 443 | 587 | +144 | +32.51pp | 98.23% | 97.67% | -0.56pp |
| Approved by Fraud Service | 437 | 579 | +142 | +32.49pp | 98.65% | 98.64% | -0.01pp |
| Call to PVS | 438 | 578 | +140 | +31.96pp | 100.23% | 99.83% | -0.40pp |
| **Successful Checkout** | 429 | 569 | +140 | +32.63pp | 97.95% | 98.44% | +0.50pp |
| **PCR Rate** | | | | | 47.72% | 45.27% | **-2.45pp** |

**Key Driver:** Click Submit Form (-5.65pp)

#### Waterfall Backend

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 1,118 | 0 | -1,118 | -100.00pp | - | - | - |
| Checkout Attempt | 568 | 648 | +80 | +14.08pp | 50.81% | 0.00% | -50.81pp |
| Enter Fraud Service | 562 | 645 | +83 | +14.77pp | 98.94% | 99.54% | +0.59pp |
| Approved by Fraud Service | 552 | 633 | +81 | +14.67pp | 98.22% | 98.14% | -0.08pp |
| PVS Attempt | 509 | 536 | +27 | +5.30pp | 92.21% | 84.68% | -7.53pp |
| PVS Success | 482 | 520 | +38 | +7.88pp | 94.70% | 97.01% | +2.32pp |
| **Successful Checkout** | 547 | 625 | +78 | +14.26pp | 113.49% | 120.19% | +6.71pp |

**Key Driver:** Checkout Attempt (-50.81pp)

---

### FR

#### Waterfall GA

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 13,830 | 12,593 | -1,237 | -8.94pp | - | - | - |
| Select Payment Method | 6,485 | 6,291 | -194 | -2.99pp | 46.89% | 49.96% | +3.07pp |
| Click Submit Form | 5,046 | 4,949 | -97 | -1.92pp | 77.81% | 78.67% | +0.86pp |
| FE Validation Passed | 4,673 | 4,600 | -73 | -1.56pp | 92.61% | 92.95% | +0.34pp |
| Enter Fraud Service | 4,470 | 4,372 | -98 | -2.19pp | 95.66% | 95.04% | -0.61pp |
| Approved by Fraud Service | 4,110 | 4,065 | -45 | -1.09pp | 91.95% | 92.98% | +1.03pp |
| Call to PVS | 4,111 | 4,069 | -42 | -1.02pp | 100.02% | 100.10% | +0.07pp |
| **Successful Checkout** | 3,996 | 3,945 | -51 | -1.28pp | 97.20% | 96.95% | -0.25pp |
| **PCR Rate** | | | | | 28.89% | 31.33% | **+2.43pp** |

**Key Driver:** Select Payment Method (+3.07pp)

#### Waterfall Backend

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 17,083 | 0 | -17,083 | -100.00pp | - | - | - |
| Checkout Attempt | 6,487 | 5,741 | -746 | -11.50pp | 37.97% | 0.00% | -37.97pp |
| Enter Fraud Service | 6,467 | 5,733 | -734 | -11.35pp | 99.69% | 99.86% | +0.17pp |
| Approved by Fraud Service | 5,757 | 5,146 | -611 | -10.61pp | 89.02% | 89.76% | +0.74pp |
| PVS Attempt | 5,750 | 5,143 | -607 | -10.56pp | 99.88% | 99.94% | +0.06pp |
| PVS Success | 5,564 | 5,022 | -542 | -9.74pp | 96.77% | 97.65% | +0.88pp |
| **Successful Checkout** | 5,626 | 5,039 | -587 | -10.43pp | 101.11% | 100.34% | -0.78pp |

**Key Driver:** Checkout Attempt (-37.97pp)

---

### IE

#### Waterfall GA

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 2,804 | 2,983 | +179 | +6.38pp | - | - | - |
| Select Payment Method | 1,536 | 1,829 | +293 | +19.08pp | 54.78% | 61.31% | +6.54pp |
| Click Submit Form | 1,233 | 1,609 | +376 | +30.49pp | 80.27% | 87.97% | +7.70pp |
| FE Validation Passed | 1,133 | 1,542 | +409 | +36.10pp | 91.89% | 95.84% | +3.95pp |
| Enter Fraud Service | 1,086 | 1,494 | +408 | +37.57pp | 95.85% | 96.89% | +1.04pp |
| Approved by Fraud Service | 1,039 | 1,440 | +401 | +38.59pp | 95.67% | 96.39% | +0.71pp |
| Call to PVS | 1,034 | 1,425 | +391 | +37.81pp | 99.52% | 98.96% | -0.56pp |
| **Successful Checkout** | 1,017 | 1,406 | +389 | +38.25pp | 98.36% | 98.67% | +0.31pp |
| **PCR Rate** | | | | | 36.27% | 47.13% | **+10.86pp** |

**Key Driver:** Click Submit Form (+7.70pp)

#### Waterfall Backend

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 3,343 | 0 | -3,343 | -100.00pp | - | - | - |
| Checkout Attempt | 1,455 | 1,782 | +327 | +22.47pp | 43.52% | 0.00% | -43.52pp |
| Enter Fraud Service | 1,455 | 1,776 | +321 | +22.06pp | 100.00% | 99.66% | -0.34pp |
| Approved by Fraud Service | 1,352 | 1,690 | +338 | +25.00pp | 92.92% | 95.16% | +2.24pp |
| PVS Attempt | 1,217 | 926 | -291 | -23.91pp | 90.01% | 54.79% | -35.22pp |
| PVS Success | 1,205 | 911 | -294 | -24.40pp | 99.01% | 98.38% | -0.63pp |
| **Successful Checkout** | 1,332 | 1,670 | +338 | +25.38pp | 110.54% | 183.32% | +72.78pp |

**Key Driver:** Successful Checkout (+72.78pp)

---





---

*Report: 2026-06-02*
