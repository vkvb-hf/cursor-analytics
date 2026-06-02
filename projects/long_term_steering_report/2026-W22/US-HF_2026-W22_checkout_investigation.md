# PCR Investigation: US-HF 2026-W22

**Metric:** Payment Conversion Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 25.15% → 26.16% (+1.01pp)  
**Volume:** 43,571 payment visits  
**Threshold:** +0.51pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate improved from 25.15% to 26.16% (+1.01pp) in US-HF for 2026-W22, with 43,571 payment visits processed.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Above threshold | +1.20pp | ⚠️ |
| Click Submit Form | Below threshold | +0.40pp | ✅ |
| FE Validation Passed | Below threshold | +0.25pp | ✅ |
| Enter Fraud Service | Below threshold | -0.17pp | ✅ |
| Approved by Fraud Service | Above threshold | +0.68pp | ⚠️ |
| Call to PVS | Below threshold | +0.09pp | ✅ |
| Successful Checkout | Below threshold | -0.50pp | ✅ |

**Key Findings:**
- **Select Payment Method** was the primary driver of improvement, with conversion increasing from 37.47% to 38.67% (+1.20pp), contributing most significantly to the overall PCR gain
- **Fraud Service approval rate** improved by +0.68pp (93.95% → 94.63%), exceeding the investigation threshold of +0.51pp
- **Backend data anomaly detected:** Payment Method Listed shows 0 records for 2026-W22, indicating a potential logging/tracking issue rather than actual operational failure
- **Fraud gap increased significantly:** Gap between Checkout Attempt and Enter Fraud Service grew from 0.43% to 1.34% (+0.91pp), driven primarily by Adyen_CreditCard which accounted for 69.6% of the gap in W22 (up from 1.0%)
- **Successful Checkout conversion declined** slightly by -0.50pp (90.79% → 90.29%) at the PVS stage, partially offsetting upstream gains

**Action:** Investigate - Backend data collection issue requires immediate attention (Payment Method Listed = 0). Additionally, investigate the Adyen_CreditCard fraud service gap increase (+166 transactions skipping fraud check).

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 43,129 | 43,571 | 442 | 1.0% | - | - | - |
| Select Payment Method | 16,160 | 16,847 | 687 | 4.3% | 37.47% | 38.67% | +1.20pp |
| Click Submit Form | 14,067 | 14,732 | 665 | 4.7% | 87.05% | 87.45% | +0.40pp |
| FE Validation Passed | 13,167 | 13,826 | 659 | 5.0% | 93.60% | 93.85% | +0.25pp |
| Enter Fraud Service | 12,748 | 13,362 | 614 | 4.8% | 96.82% | 96.64% | -0.17pp |
| Approved by Fraud Service | 11,977 | 12,645 | 668 | 5.6% | 93.95% | 94.63% | +0.68pp |
| Call to PVS | 11,946 | 12,624 | 678 | 5.7% | 99.74% | 99.83% | +0.09pp |
| **Successful Checkout** | 10,846 | 11,398 | 552 | 5.1% | 90.79% | 90.29% | -0.50pp |
| **PCR Rate** | | | | | 25.15% | 26.16% | **+1.01pp** |

### Waterfall Backend

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 46,653 | 0 | -46,653 | -100.0% | - | - | - |
| Checkout Attempt | 15,926 | 14,945 | -981 | -6.2% | 34.14% | 0.00% | -34.14pp |
| Enter Fraud Service | 15,858 | 14,745 | -1,113 | -7.0% | 99.57% | 98.66% | -0.91pp |
| Approved by Fraud Service | 14,707 | 13,754 | -953 | -6.5% | 92.74% | 93.28% | +0.54pp |
| PVS Attempt | 14,320 | 13,392 | -928 | -6.5% | 97.37% | 97.37% | -0.00pp |
| PVS Success | 12,997 | 12,102 | -895 | -6.9% | 90.76% | 90.37% | -0.39pp |
| **Successful Checkout** | 12,237 | 0 | -12,237 | -100.0% | 94.15% | 0.00% | -94.15pp |
| **PCR Rate** | | | | | 26.23% | 0.00% | **-26.23pp** |

### Payment Method Breakdown

| Payment Method | 2026-W21 Attempt | 2026-W21 Success | 2026-W21 Rate | 2026-W22 Attempt | 2026-W22 Success | 2026-W22 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 8,937 | 7,349 | 82.23% | 8,272 | 0 | 0.00% | -82.23pp |
| Braintree_ApplePay | 5,360 | 3,571 | 66.62% | 5,031 | 0 | 0.00% | -66.62pp |
| Braintree_Paypal | 1,316 | 1,103 | 83.81% | 1,194 | 0 | 0.00% | -83.81pp |
| Braintree_CreditCard | 247 | 212 | 85.83% | 212 | 0 | 0.00% | -85.83pp |
| Adyen_CreditCard | 1 | 0 | 0.00% | 167 | 0 | 0.00% | +0.00pp |
| visa | 30 | 1 | 3.33% | 32 | 0 | 0.00% | -3.33pp |
| mc | 13 | 0 | 0.00% | 22 | 0 | 0.00% | +0.00pp |
| paypal | 10 | 0 | 0.00% | 11 | 0 | 0.00% | +0.00pp |
| amex | 10 | 0 | 0.00% | 2 | 0 | 0.00% | +0.00pp |
| discover | 0 | 0 | 0.00% | 2 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (1 countries in US-HF)

| Country | Volume | PCR 2026-W21 | PCR 2026-W22 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| US | 43,571 | 25.15% | 26.16% | +1.01pp | 1 | 1 |

---

### US

#### Waterfall GA

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 43,129 | 43,571 | +442 | +1.02pp | - | - | - |
| Select Payment Method | 16,160 | 16,847 | +687 | +4.25pp | 37.47% | 38.67% | +1.20pp |
| Click Submit Form | 14,067 | 14,732 | +665 | +4.73pp | 87.05% | 87.45% | +0.40pp |
| FE Validation Passed | 13,167 | 13,826 | +659 | +5.00pp | 93.60% | 93.85% | +0.25pp |
| Enter Fraud Service | 12,748 | 13,362 | +614 | +4.82pp | 96.82% | 96.64% | -0.17pp |
| Approved by Fraud Service | 11,977 | 12,645 | +668 | +5.58pp | 93.95% | 94.63% | +0.68pp |
| Call to PVS | 11,946 | 12,624 | +678 | +5.68pp | 99.74% | 99.83% | +0.09pp |
| **Successful Checkout** | 10,846 | 11,398 | +552 | +5.09pp | 90.79% | 90.29% | -0.50pp |
| **PCR Rate** | | | | | 25.15% | 26.16% | **+1.01pp** |

**Key Driver:** Select Payment Method (+1.20pp)

#### Waterfall Backend

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 46,653 | 0 | -46,653 | -100.00pp | - | - | - |
| Checkout Attempt | 15,926 | 14,945 | -981 | -6.16pp | 34.14% | 0.00% | -34.14pp |
| Enter Fraud Service | 15,858 | 14,745 | -1,113 | -7.02pp | 99.57% | 98.66% | -0.91pp |
| Approved by Fraud Service | 14,707 | 13,754 | -953 | -6.48pp | 92.74% | 93.28% | +0.54pp |
| PVS Attempt | 14,320 | 13,392 | -928 | -6.48pp | 97.37% | 97.37% | -0.00pp |
| PVS Success | 12,997 | 12,102 | -895 | -6.89pp | 90.76% | 90.37% | -0.39pp |
| **Successful Checkout** | 13,335 | 12,602 | -733 | -5.50pp | 102.60% | 104.13% | +1.53pp |

**Key Driver:** Checkout Attempt (-34.14pp)

---



## Fraud Analysis

**Include reason:** Approved Δ (+0.68pp) meets threshold (+0.51pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W21 | 2026-W21 % | 2026-W22 | 2026-W22 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 15,926 | - | 14,945 | - | -981 | -6.2% |
| Enter Fraud Service | 15,858 | - | 14,745 | - | -1,113 | -7.0% |
| **Gap (Skipped)** | **68** | **0.43%** | **200** | **1.34%** | **132** | **+0.91pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W21 Gap | 2026-W21 % | 2026-W22 Gap | 2026-W22 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Adyen_CreditCard | 1 | 1.0% | 167 | 69.6% | +166 | +68.60pp |
| ProcessOut_CreditCard | 60 | 58.8% | 41 | 17.1% | -19 | -41.74pp |
| Braintree_ApplePay | 31 | 30.4% | 22 | 9.2% | -9 | -21.23pp |
| Braintree_Paypal | 7 | 6.9% | 10 | 4.2% | +3 | -2.70pp |
| Braintree_CreditCard | 3 | 2.9% | 0 | 0.0% | -3 | -2.94pp |
| **Total** | **102** | **100%** | **240** | **100%** | **138** | - |

*% of Gap = Payment Method Gap / Total Gap*

---


---

*Report: 2026-06-02*
