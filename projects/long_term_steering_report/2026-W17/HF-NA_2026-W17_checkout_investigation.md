# PCR Investigation: HF-NA 2026-W17

**Metric:** Payment Conversion Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 27.55% → 27.26% (-0.29pp)  
**Volume:** 54,647 payment visits  
**Threshold:** +0.15pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined by -0.29pp (27.55% → 27.26%) in HF-NA for 2026-W17, with payment visits dropping 23.3% (71,281 → 54,647).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | GA: Step conversion change | -0.57pp | ⚠️ |
| Click Submit Form | GA: Step conversion change | +0.15pp | ✅ |
| FE Validation Passed | GA: Step conversion change | +0.17pp | ⚠️ |
| Enter Fraud Service | GA: Step conversion change | +0.02pp | ✅ |
| Approved by Fraud Service | GA: Step conversion change | +0.88pp | ✅ |
| Call to PVS | GA: Step conversion change | -0.75pp | ⚠️ |
| Successful Checkout | GA: Step conversion change | -0.21pp | ⚠️ |

**Key Findings:**
- **Select Payment Method** is the primary negative driver at -0.57pp, indicating reduced user engagement at the first conversion step
- **Call to PVS** shows a significant gap with -0.75pp drop, contributing to the overall PCR decline
- **US market underperformed** with PCR dropping -0.79pp (25.83% → 25.04%), while **CA improved** +0.91pp (33.82% → 34.73%)
- **Fraud approval rates improved** significantly (+0.88pp in GA, +0.99pp in Backend), with Adyen_CreditCard gap decreasing by 42 cases
- **PVS failures** remain dominated by "Blocked Verification: Payment method blocked due to business reasons" at 56.2% of all failures

**Action:** Monitor - The PCR decline (-0.29pp) is modest and partially offset by improved fraud approval rates. Focus monitoring on US market Select Payment Method conversion and PVS call gap issues.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 71,281 | 54,647 | -16,634 | -23.3% | - | - | - |
| Select Payment Method | 28,700 | 21,689 | -7,011 | -24.4% | 40.26% | 39.69% | -0.57pp |
| Click Submit Form | 24,573 | 18,603 | -5,970 | -24.3% | 85.62% | 85.77% | +0.15pp |
| FE Validation Passed | 23,114 | 17,531 | -5,583 | -24.2% | 94.06% | 94.24% | +0.17pp |
| Enter Fraud Service | 22,598 | 17,144 | -5,454 | -24.1% | 97.77% | 97.79% | +0.02pp |
| Approved by Fraud Service | 20,843 | 15,964 | -4,879 | -23.4% | 92.23% | 93.12% | +0.88pp |
| Call to PVS | 20,847 | 15,847 | -5,000 | -24.0% | 100.02% | 99.27% | -0.75pp |
| **Successful Checkout** | 19,638 | 14,895 | -4,743 | -24.2% | 94.20% | 93.99% | -0.21pp |
| **PCR Rate** | | | | | 27.55% | 27.26% | **-0.29pp** |

### Waterfall Backend

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 64,488 | 66,966 | 2,478 | 3.8% | - | - | - |
| Checkout Attempt | 27,682 | 24,139 | -3,543 | -12.8% | 42.93% | 36.05% | -6.88pp |
| Enter Fraud Service | 27,529 | 24,035 | -3,494 | -12.7% | 99.45% | 99.57% | +0.12pp |
| Approved by Fraud Service | 24,837 | 21,923 | -2,914 | -11.7% | 90.22% | 91.21% | +0.99pp |
| PVS Attempt | 23,369 | 20,363 | -3,006 | -12.9% | 94.09% | 92.88% | -1.21pp |
| PVS Success | 21,934 | 19,130 | -2,804 | -12.8% | 93.86% | 93.94% | +0.09pp |
| **Successful Checkout** | 18,883 | 19,694 | 811 | 4.3% | 86.09% | 102.95% | +16.86pp |
| **PCR Rate** | | | | | 29.28% | 29.41% | **+0.13pp** |

### Payment Method Breakdown

| Payment Method | 2026-W16 Attempt | 2026-W16 Success | 2026-W16 Rate | 2026-W17 Attempt | 2026-W17 Success | 2026-W17 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 15,360 | 10,779 | 70.18% | 13,389 | 11,150 | 83.28% | +13.10pp |
| Braintree_ApplePay | 9,005 | 5,766 | 64.03% | 7,646 | 5,930 | 77.56% | +13.53pp |
| Braintree_Paypal | 2,334 | 1,706 | 73.09% | 2,006 | 1,704 | 84.95% | +11.85pp |
| Adyen_CreditCard | 665 | 429 | 64.51% | 761 | 678 | 89.09% | +24.58pp |
| Braintree_CreditCard | 264 | 202 | 76.52% | 277 | 231 | 83.39% | +6.88pp |
|  | 54 | 1 | 1.85% | 59 | 0 | 0.00% | -1.85pp |
| Braintree_Venmo | 0 | 0 | 0.00% | 1 | 1 | 100.00% | +100.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (2 countries in HF-NA)

| Country | Volume | PCR 2026-W16 | PCR 2026-W17 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| US | 42,133 | 25.83% | 25.04% | -0.79pp | 1 | 2 |
| CA | 12,514 | 33.82% | 34.73% | +0.91pp | 2 | 1 |

---

### US

#### Waterfall GA

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 55,957 | 42,133 | -13,824 | -24.70pp | - | - | - |
| Select Payment Method | 20,767 | 15,040 | -5,727 | -27.58pp | 37.11% | 35.70% | -1.42pp |
| Click Submit Form | 18,240 | 13,235 | -5,005 | -27.44pp | 87.83% | 88.00% | +0.17pp |
| FE Validation Passed | 17,167 | 12,466 | -4,701 | -27.38pp | 94.12% | 94.19% | +0.07pp |
| Enter Fraud Service | 16,814 | 12,220 | -4,594 | -27.32pp | 97.94% | 98.03% | +0.08pp |
| Approved by Fraud Service | 15,472 | 11,423 | -4,049 | -26.17pp | 92.02% | 93.48% | +1.46pp |
| Call to PVS | 15,548 | 11,401 | -4,147 | -26.67pp | 100.49% | 99.81% | -0.68pp |
| **Successful Checkout** | 14,455 | 10,549 | -3,906 | -27.02pp | 92.97% | 92.53% | -0.44pp |
| **PCR Rate** | | | | | 25.83% | 25.04% | **-0.79pp** |

**Key Driver:** Approved by Fraud Service (+1.46pp)

#### Waterfall Backend

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 50,112 | 51,507 | +1,395 | +2.78pp | - | - | - |
| Checkout Attempt | 20,703 | 17,450 | -3,253 | -15.71pp | 41.31% | 33.88% | -7.43pp |
| Enter Fraud Service | 20,593 | 17,390 | -3,203 | -15.55pp | 99.47% | 99.66% | +0.19pp |
| Approved by Fraud Service | 18,536 | 15,957 | -2,579 | -13.91pp | 90.01% | 91.76% | +1.75pp |
| PVS Attempt | 18,142 | 15,496 | -2,646 | -14.58pp | 97.87% | 97.11% | -0.76pp |
| PVS Success | 16,826 | 14,360 | -2,466 | -14.66pp | 92.75% | 92.67% | -0.08pp |
| **Successful Checkout** | 17,245 | 14,742 | -2,503 | -14.51pp | 102.49% | 102.66% | +0.17pp |

**Key Driver:** Checkout Attempt (-7.43pp)

---

### CA

#### Waterfall GA

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 15,324 | 12,514 | -2,810 | -18.34pp | - | - | - |
| Select Payment Method | 7,933 | 6,649 | -1,284 | -16.19pp | 51.77% | 53.13% | +1.36pp |
| Click Submit Form | 6,333 | 5,368 | -965 | -15.24pp | 79.83% | 80.73% | +0.90pp |
| FE Validation Passed | 5,947 | 5,065 | -882 | -14.83pp | 93.90% | 94.36% | +0.45pp |
| Enter Fraud Service | 5,784 | 4,924 | -860 | -14.87pp | 97.26% | 97.22% | -0.04pp |
| Approved by Fraud Service | 5,371 | 4,541 | -830 | -15.45pp | 92.86% | 92.22% | -0.64pp |
| Call to PVS | 5,299 | 4,446 | -853 | -16.10pp | 98.66% | 97.91% | -0.75pp |
| **Successful Checkout** | 5,183 | 4,346 | -837 | -16.15pp | 97.81% | 97.75% | -0.06pp |
| **PCR Rate** | | | | | 33.82% | 34.73% | **+0.91pp** |

**Key Driver:** Select Payment Method (+1.36pp)

#### Waterfall Backend

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 14,376 | 15,459 | +1,083 | +7.53pp | - | - | - |
| Checkout Attempt | 6,979 | 6,689 | -290 | -4.16pp | 48.55% | 43.27% | -5.28pp |
| Enter Fraud Service | 6,936 | 6,645 | -291 | -4.20pp | 99.38% | 99.34% | -0.04pp |
| Approved by Fraud Service | 6,301 | 5,966 | -335 | -5.32pp | 90.84% | 89.78% | -1.06pp |
| PVS Attempt | 5,227 | 4,867 | -360 | -6.89pp | 82.96% | 81.58% | -1.38pp |
| PVS Success | 5,108 | 4,770 | -338 | -6.62pp | 97.72% | 98.01% | +0.28pp |
| **Successful Checkout** | 6,140 | 5,791 | -349 | -5.68pp | 120.20% | 121.40% | +1.20pp |

**Key Driver:** Checkout Attempt (-5.28pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (+0.17pp) meets threshold (+0.15pp)

### Recovery Rate

| Metric | 2026-W16 | 2026-W17 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 5,537 | 4,213 | -1,324 |
| Error → Passed | 3,874 | 2,971 | -903 |
| **Recovery Rate** | **69.97%** | **70.52%** | **+0.55pp** |

### Error Type Distribution

| Error Type | 2026-W16 | 2026-W16 % | 2026-W17 | 2026-W17 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 3,188 | 57.6% | 2,763 | 65.6% | +8.01pp |
| terms_not_accepted | 2,257 | 40.8% | 2,076 | 49.3% | +8.51pp |
| PAYPAL_POPUP_CLOSED | 464 | 8.4% | 418 | 9.9% | +1.54pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 333 | 6.0% | 295 | 7.0% | +0.99pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 205 | 3.7% | 162 | 3.8% | +0.14pp |
| CC_TOKENISE_ERR | 162 | 2.9% | 138 | 3.3% | +0.35pp |
| PAYPAL_TOKENISE_ERR | 46 | 0.8% | 56 | 1.3% | +0.50pp |
| CC_NO_PREPAID_ERR | 9 | 0.2% | 13 | 0.3% | +0.15pp |
| APPLEPAY_MERCHANT_VALIDATION_ERR | 1 | 0.0% | 2 | 0.0% | +0.03pp |
| VENMO_TOKENISE_ERR | 0 | 0.0% | 1 | 0.0% | +0.02pp |


---

## Fraud Analysis

**Include reason:** Approved Δ (+0.88pp) meets threshold (+0.15pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W16 | 2026-W16 % | 2026-W17 | 2026-W17 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 27,682 | - | 24,139 | - | -3,543 | -12.8% |
| Enter Fraud Service | 27,529 | - | 24,035 | - | -3,494 | -12.7% |
| **Gap (Skipped)** | **153** | **0.55%** | **104** | **0.43%** | **-49** | **-0.12pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W16 Gap | 2026-W16 % | 2026-W17 Gap | 2026-W17 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| ProcessOut_CreditCard | 49 | 32.0% | 42 | 40.4% | -7 | +8.36pp |
| Braintree_ApplePay | 29 | 19.0% | 28 | 26.9% | -1 | +7.97pp |
| Adyen_CreditCard | 65 | 42.5% | 23 | 22.1% | -42 | -20.37pp |
| Braintree_Paypal | 9 | 5.9% | 11 | 10.6% | +2 | +4.69pp |
| Braintree_CreditCard | 1 | 0.7% | 0 | 0.0% | -1 | -0.65pp |
| **Total** | **153** | **100%** | **104** | **100%** | **-49** | - |

*% of Gap = Payment Method Gap / Total Gap*

---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (-0.21pp) meets threshold (+0.15pp)

| Decline Reason | 2026-W16 | 2026-W16 % | 2026-W17 | 2026-W17 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Blocked Verification: Payment method is blocked due to business reasons | 665 | 54.0% | 593 | 56.2% | -72 | +2.18pp |
| Failed Verification: Insufficient Funds | 231 | 18.8% | 186 | 17.6% | -45 | -1.14pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 79 | 6.4% | 76 | 7.2% | -3 | +0.78pp |
| Failed Verification: Issuer or Cardholder has put a restriction on the card | 64 | 5.2% | 49 | 4.6% | -15 | -0.55pp |
| Failed Verification: Declined | 28 | 2.3% | 32 | 3.0% | +4 | +0.76pp |
| Failed Verification: Declined - Call Issuer | 39 | 3.2% | 31 | 2.9% | -8 | -0.23pp |
| Failed Verification: Card Issuer Declined CVV | 41 | 3.3% | 28 | 2.7% | -13 | -0.68pp |
| Failed Verification: Processor Declined - Fraud Suspected | 31 | 2.5% | 21 | 2.0% | -10 | -0.53pp |
| Failed Verification: Closed Card | 32 | 2.6% | 20 | 1.9% | -12 | -0.70pp |
| Failed Verification: Processor Declined | 22 | 1.8% | 20 | 1.9% | -2 | +0.11pp |
| **Total PVS Failures** | **1,232** | **100%** | **1,056** | **100%** | **-176** | - |

---


---

*Report: 2026-04-28*
