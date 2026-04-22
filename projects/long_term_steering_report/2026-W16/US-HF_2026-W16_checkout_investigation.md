# PCR Investigation: US-HF 2026-W16

**Metric:** Payment Conversion Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 26.24% → 25.83% (-0.41pp)  
**Volume:** 55,957 payment visits  
**Threshold:** +0.20pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined by -0.41pp (26.24% → 25.83%) in US-HF for 2026-W16, driven primarily by a significant drop in Fraud Service approval rates despite a 5.9% increase in payment visit volume.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | vs threshold ±0.20pp | -0.17pp | ✅ |
| Click Submit Form | vs threshold ±0.20pp | -0.24pp | ⚠️ |
| FE Validation Passed | vs threshold ±0.20pp | +0.10pp | ✅ |
| Enter Fraud Service | vs threshold ±0.20pp | -0.08pp | ✅ |
| Approved by Fraud Service | vs threshold ±0.20pp | -1.04pp | ⚠️ |
| Call to PVS | vs threshold ±0.20pp | +0.44pp | ⚠️ |
| Successful Checkout | vs threshold ±0.20pp | -0.16pp | ✅ |

**Key Findings:**
- **Fraud Service approval rate dropped significantly (-1.04pp)**, declining from 93.04% to 91.99% in GA data, representing the largest conversion drop in the funnel
- **Braintree_ApplePay experienced a notable decline (-2.14pp)** in success rate (75.34% → 73.20%) with increased volume (+648 attempts), contributing meaningfully to overall PCR decline
- **Adyen_CreditCard gap to Fraud Service improved dramatically** (-203 transactions skipped), reducing the gap percentage from 77.4% to 33.6% of total gap
- **Backend PVS Success rate declined (-0.27pp)** from 93.02% to 92.75%, indicating downstream payment processing issues
- **Click Submit Form conversion weakened (-0.24pp)**, suggesting potential user experience friction at the form submission stage

**Action:** **Investigate** - The -1.04pp drop in Fraud Service approval rate exceeds threshold significantly and warrants immediate investigation into fraud rule changes or model updates deployed in W16. Additionally, review Braintree_ApplePay configuration for potential issues causing the -2.14pp decline.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 52,863 | 55,957 | 3,094 | 5.9% | - | - | - |
| Select Payment Method | 19,711 | 20,767 | 1,056 | 5.4% | 37.29% | 37.11% | -0.17pp |
| Click Submit Form | 17,360 | 18,240 | 880 | 5.1% | 88.07% | 87.83% | -0.24pp |
| FE Validation Passed | 16,321 | 17,167 | 846 | 5.2% | 94.01% | 94.12% | +0.10pp |
| Enter Fraud Service | 15,998 | 16,814 | 816 | 5.1% | 98.02% | 97.94% | -0.08pp |
| Approved by Fraud Service | 14,884 | 15,468 | 584 | 3.9% | 93.04% | 91.99% | -1.04pp |
| Call to PVS | 14,895 | 15,548 | 653 | 4.4% | 100.07% | 100.52% | +0.44pp |
| **Successful Checkout** | 13,872 | 14,455 | 583 | 4.2% | 93.13% | 92.97% | -0.16pp |
| **PCR Rate** | | | | | 26.24% | 25.83% | **-0.41pp** |

### Waterfall Backend

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 57,223 | 59,150 | 1,927 | 3.4% | - | - | - |
| Checkout Attempt | 20,476 | 20,703 | 227 | 1.1% | 35.78% | 35.00% | -0.78pp |
| Enter Fraud Service | 20,167 | 20,593 | 426 | 2.1% | 98.49% | 99.47% | +0.98pp |
| Approved by Fraud Service | 18,051 | 18,536 | 485 | 2.7% | 89.51% | 90.01% | +0.50pp |
| PVS Attempt | 17,669 | 18,142 | 473 | 2.7% | 97.88% | 97.87% | -0.01pp |
| PVS Success | 16,435 | 16,826 | 391 | 2.4% | 93.02% | 92.75% | -0.27pp |
| **Successful Checkout** | 15,942 | 16,293 | 351 | 2.2% | 97.00% | 96.83% | -0.17pp |
| **PCR Rate** | | | | | 27.86% | 27.55% | **-0.31pp** |

### Payment Method Breakdown

| Payment Method | 2026-W15 Attempt | 2026-W15 Success | 2026-W15 Rate | 2026-W16 Attempt | 2026-W16 Success | 2026-W16 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 11,650 | 9,367 | 80.40% | 11,305 | 9,241 | 81.74% | +1.34pp |
| Braintree_ApplePay | 6,740 | 5,078 | 75.34% | 7,388 | 5,408 | 73.20% | -2.14pp |
| Braintree_Paypal | 1,586 | 1,371 | 86.44% | 1,655 | 1,421 | 85.86% | -0.58pp |
| Braintree_CreditCard | 167 | 126 | 75.45% | 264 | 222 | 84.09% | +8.64pp |
|  | 93 | 0 | 0.00% | 54 | 1 | 1.85% | +1.85pp |
| Adyen_CreditCard | 240 | 0 | 0.00% | 37 | 0 | 0.00% | +0.00pp |
| CreditCard | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (1 countries in US-HF)

| Country | Volume | PCR 2026-W15 | PCR 2026-W16 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| US | 55,957 | 26.24% | 25.83% | -0.41pp | 1 | 1 |

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



## Fraud Analysis

**Include reason:** Approved Δ (-1.04pp) meets threshold (+0.20pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W15 | 2026-W15 % | 2026-W16 | 2026-W16 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 20,476 | - | 20,703 | - | 227 | 1.1% |
| Enter Fraud Service | 20,167 | - | 20,593 | - | 426 | 2.1% |
| **Gap (Skipped)** | **309** | **1.51%** | **110** | **0.53%** | **-199** | **-0.98pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W15 Gap | 2026-W15 % | 2026-W16 Gap | 2026-W16 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| ProcessOut_CreditCard | 36 | 11.6% | 39 | 35.5% | +3 | +23.84pp |
| Adyen_CreditCard | 240 | 77.4% | 37 | 33.6% | -203 | -43.78pp |
| Braintree_ApplePay | 26 | 8.4% | 27 | 24.5% | +1 | +16.16pp |
| Braintree_Paypal | 6 | 1.9% | 6 | 5.5% | 0 | +3.52pp |
| Braintree_CreditCard | 2 | 0.6% | 1 | 0.9% | -1 | +0.26pp |
| **Total** | **310** | **100%** | **110** | **100%** | **-200** | - |

*% of Gap = Payment Method Gap / Total Gap*

---


---

*Report: 2026-04-22*
