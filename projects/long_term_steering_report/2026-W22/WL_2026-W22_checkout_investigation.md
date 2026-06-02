# PCR Investigation: WL 2026-W22

**Metric:** Payment Conversion Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 28.66% → 29.39% (+0.73pp)  
**Volume:** 41,496 payment visits  
**Threshold:** +0.37pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate improved from 28.66% to 29.39% (+0.73pp) on 41,496 payment visits in 2026-W22, driven primarily by improved fraud approval rates and frontend validation performance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | vs threshold ±0.37pp | +0.28pp | ✅ |
| Click Submit Form | vs threshold ±0.37pp | +0.27pp | ✅ |
| FE Validation Passed | vs threshold ±0.37pp | +0.78pp | ⚠️ |
| Enter Fraud Service | vs threshold ±0.37pp | -0.03pp | ✅ |
| Approved by Fraud Service | vs threshold ±0.37pp | +0.89pp | ⚠️ |
| Call to PVS | vs threshold ±0.37pp | -0.36pp | ✅ |
| Successful Checkout | vs threshold ±0.37pp | +0.14pp | ✅ |

**Key Findings:**
- Fraud Service approval rate improved significantly (+0.89pp), exceeding the threshold; gap between Checkout Attempt and Enter Fraud Service decreased from 0.76% to 0.62% (-0.14pp)
- FE Validation Passed conversion improved by +0.78pp, with stable recovery rate (59.09% → 58.98%) and consistent error type distribution led by APPLEPAY_DISMISSED (64%)
- KN showed strong improvement (+3.98pp PCR) driven by Select Payment Method conversion (+3.44pp), while CK declined (-4.15pp PCR) due to Select Payment Method drop (-4.78pp)
- Backend Waterfall data shows critical data quality issues with "Payment Method Listed" and "Successful Checkout" reporting 0 values in 2026-W22, resulting in anomalous metrics (e.g., -100% changes, 0% PCR)
- Payment volume increased 9.4% week-over-week (37,939 → 41,496 visits) with proportional increases across funnel steps

**Action:** Investigate - Backend data pipeline issue requires immediate attention; "Payment Method Listed" and "Successful Checkout" metrics showing zero values indicate logging or data collection failure that must be resolved to ensure accurate monitoring.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 37,939 | 41,496 | 3,557 | 9.4% | - | - | - |
| Select Payment Method | 14,736 | 16,232 | 1,496 | 10.2% | 38.84% | 39.12% | +0.28pp |
| Click Submit Form | 12,957 | 14,316 | 1,359 | 10.5% | 87.93% | 88.20% | +0.27pp |
| FE Validation Passed | 12,421 | 13,836 | 1,415 | 11.4% | 95.86% | 96.65% | +0.78pp |
| Enter Fraud Service | 11,996 | 13,359 | 1,363 | 11.4% | 96.58% | 96.55% | -0.03pp |
| Approved by Fraud Service | 11,340 | 12,748 | 1,408 | 12.4% | 94.53% | 95.43% | +0.89pp |
| Call to PVS | 11,206 | 12,551 | 1,345 | 12.0% | 98.82% | 98.45% | -0.36pp |
| **Successful Checkout** | 10,873 | 12,196 | 1,323 | 12.2% | 97.03% | 97.17% | +0.14pp |
| **PCR Rate** | | | | | 28.66% | 29.39% | **+0.73pp** |

### Waterfall Backend

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 44,630 | 0 | -44,630 | -100.0% | - | - | - |
| Checkout Attempt | 13,459 | 13,154 | -305 | -2.3% | 30.16% | 0.00% | -30.16pp |
| Enter Fraud Service | 13,357 | 13,073 | -284 | -2.1% | 99.24% | 99.38% | +0.14pp |
| Approved by Fraud Service | 12,470 | 12,356 | -114 | -0.9% | 93.36% | 94.52% | +1.16pp |
| PVS Attempt | 9,450 | 9,304 | -146 | -1.5% | 75.78% | 75.30% | -0.48pp |
| PVS Success | 9,153 | 9,038 | -115 | -1.3% | 96.86% | 97.14% | +0.28pp |
| **Successful Checkout** | 12,082 | 0 | -12,082 | -100.0% | 132.00% | 0.00% | -132.00pp |
| **PCR Rate** | | | | | 27.07% | 0.00% | **-27.07pp** |

### Payment Method Breakdown

| Payment Method | 2026-W21 Attempt | 2026-W21 Success | 2026-W21 Rate | 2026-W22 Attempt | 2026-W22 Success | 2026-W22 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| Braintree_ApplePay | 3,718 | 3,373 | 90.72% | 3,708 | 0 | 0.00% | -90.72pp |
| ProcessOut_CreditCard | 3,808 | 3,405 | 89.42% | 3,567 | 0 | 0.00% | -89.42pp |
| Adyen_CreditCard | 2,419 | 2,200 | 90.95% | 2,568 | 0 | 0.00% | -90.95pp |
| Braintree_Paypal | 1,727 | 1,596 | 92.41% | 1,566 | 0 | 0.00% | -92.41pp |
| Braintree_CreditCard | 1,470 | 1,245 | 84.69% | 1,461 | 0 | 0.00% | -84.69pp |
| ProcessOut_ApplePay | 314 | 263 | 83.76% | 281 | 0 | 0.00% | -83.76pp |
| NoPayment | 3 | 0 | 0.00% | 3 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (2 countries in WL)

| Country | Volume | PCR 2026-W21 | PCR 2026-W22 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| KN | 8,500 | 23.95% | 27.93% | +3.98pp | 1 | 2 |
| CK | 5,609 | 46.14% | 41.99% | -4.15pp | 2 | 1 |

---

### KN

#### Waterfall GA

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 8,110 | 8,500 | +390 | +4.81pp | - | - | - |
| Select Payment Method | 2,692 | 3,114 | +422 | +15.68pp | 33.19% | 36.64% | +3.44pp |
| Click Submit Form | 2,256 | 2,657 | +401 | +17.77pp | 83.80% | 85.32% | +1.52pp |
| FE Validation Passed | 2,317 | 2,741 | +424 | +18.30pp | 102.70% | 103.16% | +0.46pp |
| Enter Fraud Service | 2,180 | 2,633 | +453 | +20.78pp | 94.09% | 96.06% | +1.97pp |
| Approved by Fraud Service | 2,013 | 2,465 | +452 | +22.45pp | 92.34% | 93.62% | +1.28pp |
| Call to PVS | 2,014 | 2,463 | +449 | +22.29pp | 100.05% | 99.92% | -0.13pp |
| **Successful Checkout** | 1,942 | 2,374 | +432 | +22.25pp | 96.43% | 96.39% | -0.04pp |
| **PCR Rate** | | | | | 23.95% | 27.93% | **+3.98pp** |

**Key Driver:** Select Payment Method (+3.44pp)

#### Waterfall Backend

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 9,904 | 0 | -9,904 | -100.00pp | - | - | - |
| Checkout Attempt | 2,546 | 2,665 | +119 | +4.67pp | 25.71% | 0.00% | -25.71pp |
| Enter Fraud Service | 2,466 | 2,602 | +136 | +5.52pp | 96.86% | 97.64% | +0.78pp |
| Approved by Fraud Service | 2,221 | 2,383 | +162 | +7.29pp | 90.06% | 91.58% | +1.52pp |
| PVS Attempt | 2,220 | 2,379 | +159 | +7.16pp | 99.95% | 99.83% | -0.12pp |
| PVS Success | 2,172 | 2,331 | +159 | +7.32pp | 97.84% | 97.98% | +0.14pp |
| **Successful Checkout** | 2,172 | 2,331 | +159 | +7.32pp | 100.00% | 100.00% | +0.00pp |

**Key Driver:** Checkout Attempt (-25.71pp)

---

### CK

#### Waterfall GA

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 3,921 | 5,609 | +1,688 | +43.05pp | - | - | - |
| Select Payment Method | 2,216 | 2,902 | +686 | +30.96pp | 56.52% | 51.74% | -4.78pp |
| Click Submit Form | 2,048 | 2,659 | +611 | +29.83pp | 92.42% | 91.63% | -0.79pp |
| FE Validation Passed | 1,984 | 2,587 | +603 | +30.39pp | 96.88% | 97.29% | +0.42pp |
| Enter Fraud Service | 1,953 | 2,535 | +582 | +29.80pp | 98.44% | 97.99% | -0.45pp |
| Approved by Fraud Service | 1,875 | 2,446 | +571 | +30.45pp | 96.01% | 96.49% | +0.48pp |
| Call to PVS | 1,874 | 2,442 | +568 | +30.31pp | 99.95% | 99.84% | -0.11pp |
| **Successful Checkout** | 1,809 | 2,355 | +546 | +30.18pp | 96.53% | 96.44% | -0.09pp |
| **PCR Rate** | | | | | 46.14% | 41.99% | **-4.15pp** |

**Key Driver:** Select Payment Method (-4.78pp)

#### Waterfall Backend

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 4,352 | 0 | -4,352 | -100.00pp | - | - | - |
| Checkout Attempt | 2,101 | 2,388 | +287 | +13.66pp | 48.28% | 0.00% | -48.28pp |
| Enter Fraud Service | 2,097 | 2,386 | +289 | +13.78pp | 99.81% | 99.92% | +0.11pp |
| Approved by Fraud Service | 1,995 | 2,285 | +290 | +14.54pp | 95.14% | 95.77% | +0.63pp |
| PVS Attempt | 1,995 | 2,285 | +290 | +14.54pp | 100.00% | 100.00% | +0.00pp |
| PVS Success | 1,934 | 2,219 | +285 | +14.74pp | 96.94% | 97.11% | +0.17pp |
| **Successful Checkout** | 1,949 | 2,232 | +283 | +14.52pp | 100.78% | 100.59% | -0.19pp |

**Key Driver:** Checkout Attempt (-48.28pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (+0.78pp) meets threshold (+0.37pp)

### Recovery Rate

| Metric | 2026-W21 | 2026-W22 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 1,655 | 1,665 | 10 |
| Error → Passed | 978 | 982 | 4 |
| **Recovery Rate** | **59.09%** | **58.98%** | **-0.11pp** |

### Error Type Distribution

| Error Type | 2026-W21 | 2026-W21 % | 2026-W22 | 2026-W22 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 1,064 | 64.3% | 1,065 | 64.0% | -0.33pp |
| terms_not_accepted | 622 | 37.6% | 635 | 38.1% | +0.56pp |
| PAYPAL_POPUP_CLOSED | 259 | 15.6% | 264 | 15.9% | +0.21pp |
| PAYPAL_TOKENISE_ERR | 16 | 1.0% | 19 | 1.1% | +0.17pp |
| CC_TOKENISE_ERR | 19 | 1.1% | 18 | 1.1% | -0.07pp |


---

## Fraud Analysis

**Include reason:** Approved Δ (+0.89pp) meets threshold (+0.37pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W21 | 2026-W21 % | 2026-W22 | 2026-W22 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 13,459 | - | 13,154 | - | -305 | -2.3% |
| Enter Fraud Service | 13,357 | - | 13,073 | - | -284 | -2.1% |
| **Gap (Skipped)** | **102** | **0.76%** | **81** | **0.62%** | **-21** | **-0.14pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W21 Gap | 2026-W21 % | 2026-W22 Gap | 2026-W22 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Braintree_CreditCard | 37 | 37.4% | 29 | 36.7% | -8 | -0.66pp |
| Braintree_ApplePay | 34 | 34.3% | 25 | 31.6% | -9 | -2.70pp |
| Braintree_Paypal | 19 | 19.2% | 16 | 20.3% | -3 | +1.06pp |
| ProcessOut_CreditCard | 5 | 5.1% | 6 | 7.6% | +1 | +2.54pp |
| NoPayment | 0 | 0.0% | 3 | 3.8% | +3 | +3.80pp |
| Adyen_CreditCard | 4 | 4.0% | 0 | 0.0% | -4 | -4.04pp |
| **Total** | **99** | **100%** | **79** | **100%** | **-20** | - |

*% of Gap = Payment Method Gap / Total Gap*

---


---

*Report: 2026-06-02*
