# PCR Investigation: HF-INTL 2026-W16

**Metric:** Payment Conversion Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 37.75% → 37.09% (-0.66pp)  
**Volume:** 76,258 payment visits  
**Threshold:** +0.33pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined from 37.75% to 37.09% (-0.66pp) on 76,258 payment visits in HF-INTL during 2026-W16.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ≥ -0.33pp | -1.27pp | ⚠️ |
| Click Submit Form | ≥ -0.33pp | +0.13pp | ✅ |
| FE Validation Passed | ≥ -0.33pp | -0.44pp | ⚠️ |
| Enter Fraud Service | ≥ -0.33pp | -0.40pp | ⚠️ |
| Approved by Fraud Service | ≥ -0.33pp | +0.05pp | ✅ |
| Call to PVS | ≥ -0.33pp | -0.19pp | ✅ |
| Successful Checkout | ≥ -0.33pp | +1.28pp | ✅ |

**Key Findings:**
- **Select Payment Method is the primary driver** of PCR decline (-1.27pp), with significant drops in IE (-7.09pp), GB (-1.80pp), and FR (-1.55pp)
- **Fraud Service gap widened** from 2.31% to 3.16% (+0.85pp) of checkout attempts, driven almost entirely by Adyen_Sepa (83.5% of gap) which has 0.17% success rate
- **FE Validation recovery rate declined** (-0.99pp), with APPLEPAY_DISMISSED remaining the dominant error type (75.2% of errors)
- **FR shows fraud approval decline** (-1.94pp in backend), while IE experienced largest country-level PCR drop (-5.14pp)
- **PVS performance improved** (+1.28pp GA, +1.01pp backend) with total failures decreasing from 1,143 to 809 (-334)

**Action:** Investigate - Focus on Select Payment Method drop-off across GB, FR, and IE; assess Adyen_Sepa integration issues causing fraud service gap; review Apple Pay dismissal patterns

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 69,804 | 76,258 | 6,454 | 9.2% | - | - | - |
| Select Payment Method | 40,026 | 42,759 | 2,733 | 6.8% | 57.34% | 56.07% | -1.27pp |
| Click Submit Form | 32,523 | 34,798 | 2,275 | 7.0% | 81.25% | 81.38% | +0.13pp |
| FE Validation Passed | 30,521 | 32,502 | 1,981 | 6.5% | 93.84% | 93.40% | -0.44pp |
| Enter Fraud Service | 29,497 | 31,281 | 1,784 | 6.0% | 96.64% | 96.24% | -0.40pp |
| Approved by Fraud Service | 27,779 | 29,475 | 1,696 | 6.1% | 94.18% | 94.23% | +0.05pp |
| Call to PVS | 27,746 | 29,384 | 1,638 | 5.9% | 99.88% | 99.69% | -0.19pp |
| **Successful Checkout** | 26,353 | 28,286 | 1,933 | 7.3% | 94.98% | 96.26% | +1.28pp |
| **PCR Rate** | | | | | 37.75% | 37.09% | **-0.66pp** |

### Waterfall Backend

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 90,874 | 96,797 | 5,923 | 6.5% | - | - | - |
| Checkout Attempt | 43,442 | 45,804 | 2,362 | 5.4% | 47.80% | 47.32% | -0.49pp |
| Enter Fraud Service | 42,437 | 44,356 | 1,919 | 4.5% | 97.69% | 96.84% | -0.85pp |
| Approved by Fraud Service | 39,153 | 40,911 | 1,758 | 4.5% | 92.26% | 92.23% | -0.03pp |
| PVS Attempt | 36,514 | 37,314 | 800 | 2.2% | 93.26% | 91.21% | -2.05pp |
| PVS Success | 35,098 | 36,244 | 1,146 | 3.3% | 96.12% | 97.13% | +1.01pp |
| **Successful Checkout** | 37,822 | 39,285 | 1,463 | 3.9% | 107.76% | 108.39% | +0.63pp |
| **PCR Rate** | | | | | 41.62% | 40.58% | **-1.04pp** |

### Payment Method Breakdown

| Payment Method | 2026-W15 Attempt | 2026-W15 Success | 2026-W15 Rate | 2026-W16 Attempt | 2026-W16 Success | 2026-W16 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 16,221 | 14,429 | 88.95% | 16,099 | 14,117 | 87.69% | -1.26pp |
| Braintree_ApplePay | 12,470 | 10,644 | 85.36% | 13,355 | 11,236 | 84.13% | -1.22pp |
| Braintree_Paypal | 8,604 | 7,884 | 91.63% | 9,604 | 8,794 | 91.57% | -0.07pp |
| ProcessOut_ApplePay | 1,474 | 1,342 | 91.04% | 1,544 | 1,419 | 91.90% | +0.86pp |
| Adyen_CreditCard | 74 | 63 | 85.14% | 1,347 | 1,321 | 98.07% | +12.93pp |
| Adyen_IDeal | 1,257 | 1,151 | 91.57% | 1,238 | 1,146 | 92.57% | +1.00pp |
| Adyen_Sepa | 835 | 0 | 0.00% | 1,197 | 2 | 0.17% | +0.17pp |
| Adyen_Klarna | 2,047 | 1,935 | 94.53% | 1,152 | 1,094 | 94.97% | +0.44pp |
| Adyen_BcmcMobile | 388 | 370 | 95.36% | 171 | 154 | 90.06% | -5.30pp |
| NoPayment | 60 | 0 | 0.00% | 89 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (4 countries in HF-INTL)

| Country | Volume | PCR 2026-W15 | PCR 2026-W16 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| GB | 22,126 | 40.92% | 39.64% | -1.28pp | 1 | 11 |
| FR | 14,757 | 31.52% | 29.71% | -1.81pp | 2 | 7 |
| IE | 3,148 | 39.48% | 34.34% | -5.14pp | 3 | 2 |
| LU | 91 | 39.73% | 57.14% | +17.41pp | 10 | 1 |

---

### FR

#### Waterfall GA

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 15,455 | 14,757 | -698 | -4.52pp | - | - | - |
| Select Payment Method | 7,615 | 7,043 | -572 | -7.51pp | 49.27% | 47.73% | -1.55pp |
| Click Submit Form | 6,089 | 5,617 | -472 | -7.75pp | 79.96% | 79.75% | -0.21pp |
| FE Validation Passed | 5,687 | 5,221 | -466 | -8.19pp | 93.40% | 92.95% | -0.45pp |
| Enter Fraud Service | 5,491 | 5,024 | -467 | -8.50pp | 96.55% | 96.23% | -0.33pp |
| Approved by Fraud Service | 4,995 | 4,502 | -493 | -9.87pp | 90.97% | 89.61% | -1.36pp |
| Call to PVS | 5,007 | 4,506 | -501 | -10.01pp | 100.24% | 100.09% | -0.15pp |
| **Successful Checkout** | 4,871 | 4,385 | -486 | -9.98pp | 97.28% | 97.31% | +0.03pp |
| **PCR Rate** | | | | | 31.52% | 29.71% | **-1.80pp** |

**Key Driver:** Select Payment Method (-1.55pp)

#### Waterfall Backend

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 20,551 | 19,157 | -1,394 | -6.78pp | - | - | - |
| Checkout Attempt | 8,469 | 7,674 | -795 | -9.39pp | 41.21% | 40.06% | -1.15pp |
| Enter Fraud Service | 8,455 | 7,650 | -805 | -9.52pp | 99.83% | 99.69% | -0.15pp |
| Approved by Fraud Service | 7,408 | 6,554 | -854 | -11.53pp | 87.62% | 85.67% | -1.94pp |
| PVS Attempt | 7,408 | 6,547 | -861 | -11.62pp | 100.00% | 99.89% | -0.11pp |
| PVS Success | 7,290 | 6,428 | -862 | -11.82pp | 98.41% | 98.18% | -0.22pp |
| **Successful Checkout** | 7,315 | 6,447 | -868 | -11.87pp | 100.34% | 100.30% | -0.05pp |

**Key Driver:** Approved by Fraud Service (-1.94pp)

---

### IE

#### Waterfall GA

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 2,548 | 3,148 | +600 | +23.55pp | - | - | - |
| Select Payment Method | 1,526 | 1,662 | +136 | +8.91pp | 59.89% | 52.80% | -7.09pp |
| Click Submit Form | 1,236 | 1,348 | +112 | +9.06pp | 81.00% | 81.11% | +0.11pp |
| FE Validation Passed | 1,144 | 1,251 | +107 | +9.35pp | 92.56% | 92.80% | +0.25pp |
| Enter Fraud Service | 1,113 | 1,207 | +94 | +8.45pp | 97.29% | 96.48% | -0.81pp |
| Approved by Fraud Service | 1,034 | 1,118 | +84 | +8.12pp | 92.90% | 92.63% | -0.28pp |
| Call to PVS | 1,039 | 1,121 | +82 | +7.89pp | 100.48% | 100.27% | -0.22pp |
| **Successful Checkout** | 1,006 | 1,081 | +75 | +7.46pp | 96.82% | 96.43% | -0.39pp |
| **PCR Rate** | | | | | 39.48% | 34.34% | **-5.14pp** |

**Key Driver:** Select Payment Method (-7.09pp)

#### Waterfall Backend

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 3,467 | 3,924 | +457 | +13.18pp | - | - | - |
| Checkout Attempt | 1,598 | 1,674 | +76 | +4.76pp | 46.09% | 42.66% | -3.43pp |
| Enter Fraud Service | 1,596 | 1,667 | +71 | +4.45pp | 99.87% | 99.58% | -0.29pp |
| Approved by Fraud Service | 1,460 | 1,509 | +49 | +3.36pp | 91.48% | 90.52% | -0.96pp |
| PVS Attempt | 1,282 | 1,394 | +112 | +8.74pp | 87.81% | 92.38% | +4.57pp |
| PVS Success | 1,255 | 1,364 | +109 | +8.69pp | 97.89% | 97.85% | -0.05pp |
| **Successful Checkout** | 1,436 | 1,477 | +41 | +2.86pp | 114.42% | 108.28% | -6.14pp |

**Key Driver:** Successful Checkout (-6.14pp)

---

### LU

#### Waterfall GA

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 73 | 91 | +18 | +24.66pp | - | - | - |
| Select Payment Method | 41 | 61 | +20 | +48.78pp | 56.16% | 67.03% | +10.87pp |
| Click Submit Form | 34 | 57 | +23 | +67.65pp | 82.93% | 93.44% | +10.52pp |
| FE Validation Passed | 31 | 57 | +26 | +83.87pp | 91.18% | 100.00% | +8.82pp |
| Enter Fraud Service | 31 | 56 | +25 | +80.65pp | 100.00% | 98.25% | -1.75pp |
| Approved by Fraud Service | 31 | 54 | +23 | +74.19pp | 100.00% | 96.43% | -3.57pp |
| Call to PVS | 30 | 53 | +23 | +76.67pp | 96.77% | 98.15% | +1.37pp |
| **Successful Checkout** | 29 | 52 | +23 | +79.31pp | 96.67% | 98.11% | +1.45pp |
| **PCR Rate** | | | | | 39.73% | 57.14% | **+17.42pp** |

**Key Driver:** Select Payment Method (+10.87pp)

#### Waterfall Backend

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 279 | 299 | +20 | +7.17pp | - | - | - |
| Checkout Attempt | 72 | 103 | +31 | +43.06pp | 25.81% | 34.45% | +8.64pp |
| Enter Fraud Service | 66 | 92 | +26 | +39.39pp | 91.67% | 89.32% | -2.35pp |
| Approved by Fraud Service | 65 | 86 | +21 | +32.31pp | 98.48% | 93.48% | -5.01pp |
| PVS Attempt | 63 | 84 | +21 | +33.33pp | 96.92% | 97.67% | +0.75pp |
| PVS Success | 63 | 82 | +19 | +30.16pp | 100.00% | 97.62% | -2.38pp |
| **Successful Checkout** | 69 | 94 | +25 | +36.23pp | 109.52% | 114.63% | +5.11pp |

**Key Driver:** Checkout Attempt (+8.64pp)

---

### GB

#### Waterfall GA

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 17,250 | 22,126 | +4,876 | +28.27pp | - | - | - |
| Select Payment Method | 10,303 | 12,816 | +2,513 | +24.39pp | 59.73% | 57.92% | -1.80pp |
| Click Submit Form | 8,447 | 10,564 | +2,117 | +25.06pp | 81.99% | 82.43% | +0.44pp |
| FE Validation Passed | 7,720 | 9,682 | +1,962 | +25.41pp | 91.39% | 91.65% | +0.26pp |
| Enter Fraud Service | 7,537 | 9,435 | +1,898 | +25.18pp | 97.63% | 97.45% | -0.18pp |
| Approved by Fraud Service | 7,176 | 8,990 | +1,814 | +25.28pp | 95.21% | 95.28% | +0.07pp |
| Call to PVS | 7,176 | 8,940 | +1,764 | +24.58pp | 100.00% | 99.44% | -0.56pp |
| **Successful Checkout** | 7,059 | 8,771 | +1,712 | +24.25pp | 98.37% | 98.11% | -0.26pp |
| **PCR Rate** | | | | | 40.92% | 39.64% | **-1.28pp** |

**Key Driver:** Select Payment Method (-1.80pp)

#### Waterfall Backend

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 21,082 | 26,366 | +5,284 | +25.06pp | - | - | - |
| Checkout Attempt | 10,599 | 13,021 | +2,422 | +22.85pp | 50.28% | 49.39% | -0.89pp |
| Enter Fraud Service | 10,536 | 12,918 | +2,382 | +22.61pp | 99.41% | 99.21% | -0.20pp |
| Approved by Fraud Service | 9,841 | 12,110 | +2,269 | +23.06pp | 93.40% | 93.75% | +0.34pp |
| PVS Attempt | 8,125 | 9,915 | +1,790 | +22.03pp | 82.56% | 81.87% | -0.69pp |
| PVS Success | 7,993 | 9,748 | +1,755 | +21.96pp | 98.38% | 98.32% | -0.06pp |
| **Successful Checkout** | 9,726 | 11,979 | +2,253 | +23.16pp | 121.68% | 122.89% | +1.21pp |

**Key Driver:** Successful Checkout (+1.21pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (-0.44pp) meets threshold (+0.33pp)

### Recovery Rate

| Metric | 2026-W15 | 2026-W16 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 5,532 | 6,044 | 512 |
| Error → Passed | 3,238 | 3,478 | 240 |
| **Recovery Rate** | **58.53%** | **57.54%** | **-0.99pp** |

### Error Type Distribution

| Error Type | 2026-W15 | 2026-W15 % | 2026-W16 | 2026-W16 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 4,220 | 76.3% | 4,548 | 75.2% | -1.04pp |
| PAYPAL_POPUP_CLOSED | 1,089 | 19.7% | 1,268 | 21.0% | +1.29pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 267 | 4.8% | 305 | 5.0% | +0.22pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 134 | 2.4% | 150 | 2.5% | +0.06pp |
| PAYPAL_TOKENISE_ERR | 127 | 2.3% | 126 | 2.1% | -0.21pp |
| CC_TOKENISE_ERR | 114 | 2.1% | 98 | 1.6% | -0.44pp |
| APPLEPAY_MERCHANT_VALIDATION_ERR | 5 | 0.1% | 4 | 0.1% | -0.02pp |
| APPLEPAY_TOKENISE_ERR | 2 | 0.0% | 2 | 0.0% | -0.00pp |


---

## Fraud Analysis

**Include reason:** Enter FS Δ (-0.40pp) meets threshold (+0.33pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W15 | 2026-W15 % | 2026-W16 | 2026-W16 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 43,442 | - | 45,804 | - | 2,362 | 5.4% |
| Enter Fraud Service | 42,437 | - | 44,356 | - | 1,919 | 4.5% |
| **Gap (Skipped)** | **1,005** | **2.31%** | **1,448** | **3.16%** | **443** | **+0.85pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W15 Gap | 2026-W15 % | 2026-W16 Gap | 2026-W16 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Adyen_Sepa | 835 | 84.3% | 1,197 | 83.5% | +362 | -0.87pp |
| NoPayment | 60 | 6.1% | 89 | 6.2% | +29 | +0.15pp |
| Braintree_ApplePay | 42 | 4.2% | 62 | 4.3% | +20 | +0.08pp |
| ProcessOut_CreditCard | 32 | 3.2% | 51 | 3.6% | +19 | +0.32pp |
| Braintree_Paypal | 21 | 2.1% | 35 | 2.4% | +14 | +0.32pp |
| **Total** | **990** | **100%** | **1,434** | **100%** | **444** | - |

*% of Gap = Payment Method Gap / Total Gap*

---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (+1.28pp) meets threshold (+0.33pp)

| Decline Reason | 2026-W15 | 2026-W15 % | 2026-W16 | 2026-W16 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Failed Verification: Insufficient Funds | 171 | 15.0% | 183 | 22.6% | +12 | +7.66pp |
| RedirectShopper | 302 | 26.4% | 182 | 22.5% | -120 | -3.92pp |
| Cancelled: Cancelled | 250 | 21.9% | 109 | 13.5% | -141 | -8.40pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 77 | 6.7% | 92 | 11.4% | +15 | +4.64pp |
| Failed Verification: Declined | 93 | 8.1% | 87 | 10.8% | -6 | +2.62pp |
| Refused: Refused | 121 | 10.6% | 60 | 7.4% | -61 | -3.17pp |
| Pending | 75 | 6.6% | 39 | 4.8% | -36 | -1.74pp |
| Failed Verification: OK: 83 : Fraud/Security | 17 | 1.5% | 22 | 2.7% | +5 | +1.23pp |
| Failed Verification: Security | 27 | 2.4% | 21 | 2.6% | -6 | +0.23pp |
| Blocked Verification: Payment method is blocked due to business reasons | 10 | 0.9% | 14 | 1.7% | +4 | +0.86pp |
| **Total PVS Failures** | **1,143** | **100%** | **809** | **100%** | **-334** | - |

---


---

*Report: 2026-04-22*
