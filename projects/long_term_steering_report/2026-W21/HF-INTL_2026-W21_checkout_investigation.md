# PCR Investigation: HF-INTL 2026-W21

**Metric:** Payment Conversion Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 35.47% → 34.93% (-0.54pp)  
**Volume:** 61,290 payment visits  
**Threshold:** +0.27pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined by -0.54pp (35.47% → 34.93%) on 61,290 payment visits in 2026-W21, driven primarily by degradation in the Click Submit Form and Successful Checkout steps.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ≥ -0.27pp | -0.17pp | ✅ |
| Click Submit Form | ≥ -0.27pp | -1.03pp | ⚠️ |
| FE Validation Passed | ≥ -0.27pp | -0.03pp | ✅ |
| Enter Fraud Service | ≥ -0.27pp | -0.20pp | ✅ |
| Approved by Fraud Service | ≥ -0.27pp | +0.49pp | ✅ |
| Call to PVS | ≥ -0.27pp | +0.82pp | ✅ |
| Successful Checkout | ≥ -0.27pp | -0.99pp | ⚠️ |

**Key Findings:**
- **Click Submit Form** conversion dropped -1.03pp (81.65% → 80.62%), indicating increased user abandonment at the payment form submission stage
- **Successful Checkout** conversion declined -0.99pp (94.44% → 93.45%), the largest negative contributor to PCR degradation
- **DE** (largest volume market at 11,548 visits) saw -1.49pp PCR decline, with Successful Checkout dropping -3.67pp in GA waterfall
- **Adyen_Sepa** gap to fraud service increased significantly (+447 transactions), with 89.8% of checkout attempts failing to reach fraud service in W21
- **PVS failure reasons** shifted: "Cancelled: Cancelled" increased +72 cases (+4.89pp share), while "Customer abandoned payment after 60 minutes" decreased -167 cases

**Action:** Investigate — Focus on DE market Successful Checkout degradation and Adyen_Sepa integration issues causing pre-fraud service drops.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 68,137 | 61,290 | -6,847 | -10.0% | - | - | - |
| Select Payment Method | 37,270 | 33,422 | -3,848 | -10.3% | 54.70% | 54.53% | -0.17pp |
| Click Submit Form | 30,432 | 26,945 | -3,487 | -11.5% | 81.65% | 80.62% | -1.03pp |
| FE Validation Passed | 28,484 | 25,213 | -3,271 | -11.5% | 93.60% | 93.57% | -0.03pp |
| Enter Fraud Service | 27,507 | 24,298 | -3,209 | -11.7% | 96.57% | 96.37% | -0.20pp |
| Approved by Fraud Service | 25,931 | 23,024 | -2,907 | -11.2% | 94.27% | 94.76% | +0.49pp |
| Call to PVS | 25,592 | 22,911 | -2,681 | -10.5% | 98.69% | 99.51% | +0.82pp |
| **Successful Checkout** | 24,168 | 21,410 | -2,758 | -11.4% | 94.44% | 93.45% | -0.99pp |
| **PCR Rate** | | | | | 35.47% | 34.93% | **-0.54pp** |

### Waterfall Backend

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 82,697 | 74,901 | -7,796 | -9.4% | - | - | - |
| Checkout Attempt | 39,231 | 34,915 | -4,316 | -11.0% | 47.44% | 46.61% | -0.82pp |
| Enter Fraud Service | 38,026 | 33,327 | -4,699 | -12.4% | 96.93% | 95.45% | -1.48pp |
| Approved by Fraud Service | 35,012 | 30,985 | -4,027 | -11.5% | 92.07% | 92.97% | +0.90pp |
| PVS Attempt | 31,674 | 28,205 | -3,469 | -11.0% | 90.47% | 91.03% | +0.56pp |
| PVS Success | 29,614 | 26,435 | -3,179 | -10.7% | 93.50% | 93.72% | +0.23pp |
| **Successful Checkout** | 32,207 | 28,793 | -3,414 | -10.6% | 108.76% | 108.92% | +0.16pp |
| **PCR Rate** | | | | | 38.95% | 38.44% | **-0.50pp** |

### Payment Method Breakdown

| Payment Method | 2026-W20 Attempt | 2026-W20 Success | 2026-W20 Rate | 2026-W21 Attempt | 2026-W21 Success | 2026-W21 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 12,671 | 10,979 | 86.65% | 10,902 | 9,571 | 87.79% | +1.14pp |
| Braintree_ApplePay | 10,994 | 7,961 | 72.41% | 9,293 | 6,889 | 74.13% | +1.72pp |
| Braintree_Paypal | 6,971 | 6,309 | 90.50% | 5,993 | 5,543 | 92.49% | +1.99pp |
| Adyen_Klarna | 2,078 | 1,923 | 92.54% | 2,250 | 2,113 | 93.91% | +1.37pp |
| ProcessOut_ApplePay | 1,623 | 1,444 | 88.97% | 1,546 | 1,387 | 89.72% | +0.74pp |
| Adyen_Sepa | 957 | 3 | 0.31% | 1,404 | 2 | 0.14% | -0.17pp |
| Adyen_CreditCard | 1,555 | 1,507 | 96.91% | 1,377 | 1,345 | 97.68% | +0.76pp |
| Adyen_IDeal | 1,195 | 1,079 | 90.29% | 1,016 | 937 | 92.22% | +1.93pp |
| Adyen_BcmcMobile | 733 | 687 | 93.72% | 707 | 660 | 93.35% | -0.37pp |
| ProcessOut_Mobilepay | 228 | 213 | 93.42% | 219 | 210 | 95.89% | +2.47pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (4 countries in HF-INTL)

| Country | Volume | PCR 2026-W20 | PCR 2026-W21 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| DE | 11,548 | 35.20% | 33.71% | -1.49pp | 1 | 5 |
| AU | 8,104 | 34.83% | 33.61% | -1.22pp | 2 | 6 |
| NO | 899 | 44.50% | 47.72% | +3.22pp | 5 | 1 |
| CH | 351 | 23.92% | 26.78% | +2.86pp | 12 | 2 |

---

### NO

#### Waterfall GA

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 737 | 899 | +162 | +21.98pp | - | - | - |
| Select Payment Method | 431 | 539 | +108 | +25.06pp | 58.48% | 59.96% | +1.48pp |
| Click Submit Form | 368 | 465 | +97 | +26.36pp | 85.38% | 86.27% | +0.89pp |
| FE Validation Passed | 348 | 451 | +103 | +29.60pp | 94.57% | 96.99% | +2.42pp |
| Enter Fraud Service | 341 | 443 | +102 | +29.91pp | 97.99% | 98.23% | +0.24pp |
| Approved by Fraud Service | 333 | 437 | +104 | +31.23pp | 97.65% | 98.65% | +0.99pp |
| Call to PVS | 330 | 438 | +108 | +32.73pp | 99.10% | 100.23% | +1.13pp |
| **Successful Checkout** | 328 | 429 | +101 | +30.79pp | 99.39% | 97.95% | -1.45pp |
| **PCR Rate** | | | | | 44.50% | 47.72% | **+3.21pp** |

**Key Driver:** FE Validation Passed (+2.42pp)

#### Waterfall Backend

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 1,000 | 1,118 | +118 | +11.80pp | - | - | - |
| Checkout Attempt | 471 | 568 | +97 | +20.59pp | 47.10% | 50.81% | +3.71pp |
| Enter Fraud Service | 467 | 562 | +95 | +20.34pp | 99.15% | 98.94% | -0.21pp |
| Approved by Fraud Service | 456 | 552 | +96 | +21.05pp | 97.64% | 98.22% | +0.58pp |
| PVS Attempt | 376 | 509 | +133 | +35.37pp | 82.46% | 92.21% | +9.75pp |
| PVS Success | 354 | 482 | +128 | +36.16pp | 94.15% | 94.70% | +0.55pp |
| **Successful Checkout** | 449 | 547 | +98 | +21.83pp | 126.84% | 113.49% | -13.35pp |

**Key Driver:** Successful Checkout (-13.35pp)

---

### CH

#### Waterfall GA

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 439 | 351 | -88 | -20.05pp | - | - | - |
| Select Payment Method | 180 | 151 | -29 | -16.11pp | 41.00% | 43.02% | +2.02pp |
| Click Submit Form | 126 | 115 | -11 | -8.73pp | 70.00% | 76.16% | +6.16pp |
| FE Validation Passed | 119 | 110 | -9 | -7.56pp | 94.44% | 95.65% | +1.21pp |
| Enter Fraud Service | 112 | 107 | -5 | -4.46pp | 94.12% | 97.27% | +3.16pp |
| Approved by Fraud Service | 112 | 104 | -8 | -7.14pp | 100.00% | 97.20% | -2.80pp |
| Call to PVS | 112 | 103 | -9 | -8.04pp | 100.00% | 99.04% | -0.96pp |
| **Successful Checkout** | 105 | 94 | -11 | -10.48pp | 93.75% | 91.26% | -2.49pp |
| **PCR Rate** | | | | | 23.92% | 26.78% | **+2.86pp** |

**Key Driver:** Click Submit Form (+6.16pp)

#### Waterfall Backend

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 643 | 508 | -135 | -21.00pp | - | - | - |
| Checkout Attempt | 140 | 110 | -30 | -21.43pp | 21.77% | 21.65% | -0.12pp |
| Enter Fraud Service | 135 | 108 | -27 | -20.00pp | 96.43% | 98.18% | +1.75pp |
| Approved by Fraud Service | 134 | 105 | -29 | -21.64pp | 99.26% | 97.22% | -2.04pp |
| PVS Attempt | 134 | 106 | -28 | -20.90pp | 100.00% | 100.95% | +0.95pp |
| PVS Success | 125 | 96 | -29 | -23.20pp | 93.28% | 90.57% | -2.72pp |
| **Successful Checkout** | 128 | 103 | -25 | -19.53pp | 102.40% | 107.29% | +4.89pp |

**Key Driver:** Successful Checkout (+4.89pp)

---

### AU

#### Waterfall GA

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 8,218 | 8,104 | -114 | -1.39pp | - | - | - |
| Select Payment Method | 4,326 | 4,127 | -199 | -4.60pp | 52.64% | 50.93% | -1.72pp |
| Click Submit Form | 3,654 | 3,428 | -226 | -6.19pp | 84.47% | 83.06% | -1.40pp |
| FE Validation Passed | 3,346 | 3,147 | -199 | -5.95pp | 91.57% | 91.80% | +0.23pp |
| Enter Fraud Service | 3,236 | 3,051 | -185 | -5.72pp | 96.71% | 96.95% | +0.24pp |
| Approved by Fraud Service | 3,063 | 2,843 | -220 | -7.18pp | 94.65% | 93.18% | -1.47pp |
| Call to PVS | 2,957 | 2,809 | -148 | -5.01pp | 96.54% | 98.80% | +2.26pp |
| **Successful Checkout** | 2,862 | 2,724 | -138 | -4.82pp | 96.79% | 96.97% | +0.19pp |
| **PCR Rate** | | | | | 34.83% | 33.61% | **-1.21pp** |

**Key Driver:** Call to PVS (+2.26pp)

#### Waterfall Backend

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 9,056 | 8,965 | -91 | -1.00pp | - | - | - |
| Checkout Attempt | 3,752 | 3,559 | -193 | -5.14pp | 41.43% | 39.70% | -1.73pp |
| Enter Fraud Service | 3,728 | 3,535 | -193 | -5.18pp | 99.36% | 99.33% | -0.03pp |
| Approved by Fraud Service | 3,467 | 3,239 | -228 | -6.58pp | 93.00% | 91.63% | -1.37pp |
| PVS Attempt | 2,992 | 2,907 | -85 | -2.84pp | 86.30% | 89.75% | +3.45pp |
| PVS Success | 2,845 | 2,820 | -25 | -0.88pp | 95.09% | 97.01% | +1.92pp |
| **Successful Checkout** | 3,305 | 3,166 | -139 | -4.21pp | 116.17% | 112.27% | -3.90pp |

**Key Driver:** Successful Checkout (-3.90pp)

---

### DE

#### Waterfall GA

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 12,027 | 11,548 | -479 | -3.98pp | - | - | - |
| Select Payment Method | 7,127 | 6,931 | -196 | -2.75pp | 59.26% | 60.02% | +0.76pp |
| Click Submit Form | 5,586 | 5,282 | -304 | -5.44pp | 78.38% | 76.21% | -2.17pp |
| FE Validation Passed | 5,345 | 5,052 | -293 | -5.48pp | 95.69% | 95.65% | -0.04pp |
| Enter Fraud Service | 5,035 | 4,756 | -279 | -5.54pp | 94.20% | 94.14% | -0.06pp |
| Approved by Fraud Service | 4,807 | 4,585 | -222 | -4.62pp | 95.47% | 96.40% | +0.93pp |
| Call to PVS | 4,755 | 4,561 | -194 | -4.08pp | 98.92% | 99.48% | +0.56pp |
| **Successful Checkout** | 4,233 | 3,893 | -340 | -8.03pp | 89.02% | 85.35% | -3.67pp |
| **PCR Rate** | | | | | 35.20% | 33.71% | **-1.48pp** |

**Key Driver:** Successful Checkout (-3.67pp)

#### Waterfall Backend

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 15,561 | 14,658 | -903 | -5.80pp | - | - | - |
| Checkout Attempt | 7,561 | 6,935 | -626 | -8.28pp | 48.59% | 47.31% | -1.28pp |
| Enter Fraud Service | 7,529 | 6,901 | -628 | -8.34pp | 99.58% | 99.51% | -0.07pp |
| Approved by Fraud Service | 7,031 | 6,538 | -493 | -7.01pp | 93.39% | 94.74% | +1.35pp |
| PVS Attempt | 6,914 | 6,480 | -434 | -6.28pp | 98.34% | 99.11% | +0.78pp |
| PVS Success | 6,269 | 5,697 | -572 | -9.12pp | 90.67% | 87.92% | -2.75pp |
| **Successful Checkout** | 6,877 | 6,449 | -428 | -6.22pp | 109.70% | 113.20% | +3.50pp |

**Key Driver:** Successful Checkout (+3.50pp)

---



## Fraud Analysis

**Include reason:** Approved Δ (+0.49pp) meets threshold (+0.27pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W20 | 2026-W20 % | 2026-W21 | 2026-W21 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 39,231 | - | 34,915 | - | -4,316 | -11.0% |
| Enter Fraud Service | 38,026 | - | 33,327 | - | -4,699 | -12.4% |
| **Gap (Skipped)** | **1,205** | **3.07%** | **1,588** | **4.55%** | **383** | **+1.48pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W20 Gap | 2026-W20 % | 2026-W21 Gap | 2026-W21 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Adyen_Sepa | 957 | 80.7% | 1,404 | 89.8% | +447 | +9.14pp |
| NoPayment | 120 | 10.1% | 70 | 4.5% | -50 | -5.64pp |
| Braintree_ApplePay | 49 | 4.1% | 43 | 2.8% | -6 | -1.38pp |
| ProcessOut_CreditCard | 36 | 3.0% | 27 | 1.7% | -9 | -1.31pp |
| Braintree_Paypal | 24 | 2.0% | 19 | 1.2% | -5 | -0.81pp |
| **Total** | **1,186** | **100%** | **1,563** | **100%** | **377** | - |

*% of Gap = Payment Method Gap / Total Gap*

---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (-0.99pp) meets threshold (+0.27pp)

| Decline Reason | 2026-W20 | 2026-W20 % | 2026-W21 | 2026-W21 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| RedirectShopper | 368 | 25.6% | 409 | 28.3% | +41 | +2.68pp |
| Cancelled: Cancelled | 225 | 15.7% | 297 | 20.6% | +72 | +4.89pp |
| Refused: Refused | 134 | 9.3% | 182 | 12.6% | +48 | +3.26pp |
| Failed Verification: Insufficient Funds | 141 | 9.8% | 173 | 12.0% | +32 | +2.15pp |
| Pending | 128 | 8.9% | 133 | 9.2% | +5 | +0.29pp |
| Verified | 68 | 4.7% | 71 | 4.9% | +3 | +0.18pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 77 | 5.4% | 69 | 4.8% | -8 | -0.59pp |
| CHARGE_STATE_FAILURE: Customer abandoned payment after 60 minutes | 207 | 14.4% | 40 | 2.8% | -167 | -11.65pp |
| Failed Verification: Declined | 55 | 3.8% | 39 | 2.7% | -16 | -1.13pp |
| Failed Verification: 200 OK: 05 : Do not honor | 33 | 2.3% | 32 | 2.2% | -1 | -0.08pp |
| **Total PVS Failures** | **1,436** | **100%** | **1,445** | **100%** | **+9** | - |

---


---

*Report: 2026-05-26*
