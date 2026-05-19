# PCR Investigation: HF-INTL 2026-W20

**Metric:** Payment Conversion Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 36.32% → 35.47% (-0.85pp)  
**Volume:** 68,135 payment visits  
**Threshold:** +0.43pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined from 36.32% to 35.47% (-0.85pp) on 68,135 payment visits in W20, driven primarily by fraud service approval degradation and payment method-specific issues with Braintree_ApplePay.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Rate vs W19 | -0.52pp | ⚠️ |
| Click Submit Form | Rate vs W19 | -0.40pp | ✅ |
| FE Validation Passed | Rate vs W19 | -0.49pp | ⚠️ |
| Enter Fraud Service | Rate vs W19 | +0.77pp | ✅ |
| Approved by Fraud Service | Rate vs W19 | -0.92pp | ⚠️ |
| Call to PVS | Rate vs W19 | -0.84pp | ⚠️ |
| Successful Checkout | Rate vs W19 | +0.55pp | ✅ |

**Key Findings:**
- **Braintree_ApplePay critical decline:** Success rate dropped from 85.18% to 72.41% (-12.77pp), the largest payment method degradation, requiring immediate investigation
- **Fraud Service approval degradation:** Approved by Fraud Service conversion fell -0.92pp at L0 level, with NZ showing -2.69pp (GA) and -2.97pp (Backend) drops
- **FR driving overall decline:** FR is the top contributor with PCR dropping -1.94pp, primarily due to Select Payment Method step (-1.52pp)
- **FE Validation recovery rate worsening:** Recovery rate decreased from 60.51% to 59.10% (-1.41pp), with APPLEPAY_DISMISSED errors remaining dominant at 75%+ of all errors
- **PVS abandonment spike:** "Customer abandoned payment after 60 minutes" errors increased significantly (+123 count, +8.43pp share), suggesting potential UX or processing delays

**Action:** Investigate - Prioritize Braintree_ApplePay integration issues and fraud service rule changes affecting NZ and GB markets

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 69,612 | 68,135 | -1,477 | -2.1% | - | - | - |
| Select Payment Method | 38,440 | 37,268 | -1,172 | -3.0% | 55.22% | 54.70% | -0.52pp |
| Click Submit Form | 31,541 | 30,430 | -1,111 | -3.5% | 82.05% | 81.65% | -0.40pp |
| FE Validation Passed | 29,676 | 28,482 | -1,194 | -4.0% | 94.09% | 93.60% | -0.49pp |
| Enter Fraud Service | 28,429 | 27,505 | -924 | -3.3% | 95.80% | 96.57% | +0.77pp |
| Approved by Fraud Service | 27,052 | 25,921 | -1,131 | -4.2% | 95.16% | 94.24% | -0.92pp |
| Call to PVS | 26,933 | 25,590 | -1,343 | -5.0% | 99.56% | 98.72% | -0.84pp |
| **Successful Checkout** | 25,285 | 24,166 | -1,119 | -4.4% | 93.88% | 94.44% | +0.55pp |
| **PCR Rate** | | | | | 36.32% | 35.47% | **-0.85pp** |

### Waterfall Backend

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 86,756 | 82,697 | -4,059 | -4.7% | - | - | - |
| Checkout Attempt | 40,870 | 39,231 | -1,639 | -4.0% | 47.11% | 47.44% | +0.33pp |
| Enter Fraud Service | 39,734 | 38,026 | -1,708 | -4.3% | 97.22% | 96.93% | -0.29pp |
| Approved by Fraud Service | 36,775 | 35,012 | -1,763 | -4.8% | 92.55% | 92.07% | -0.48pp |
| PVS Attempt | 33,686 | 31,674 | -2,012 | -6.0% | 91.60% | 90.47% | -1.13pp |
| PVS Success | 31,310 | 29,614 | -1,696 | -5.4% | 92.95% | 93.50% | +0.55pp |
| **Successful Checkout** | 35,454 | 32,207 | -3,247 | -9.2% | 113.24% | 108.76% | -4.48pp |
| **PCR Rate** | | | | | 40.87% | 38.95% | **-1.92pp** |

### Payment Method Breakdown

| Payment Method | 2026-W19 Attempt | 2026-W19 Success | 2026-W19 Rate | 2026-W20 Attempt | 2026-W20 Success | 2026-W20 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 13,184 | 11,590 | 87.91% | 12,671 | 10,979 | 86.65% | -1.26pp |
| Braintree_ApplePay | 11,993 | 10,216 | 85.18% | 10,994 | 7,961 | 72.41% | -12.77pp |
| Braintree_Paypal | 7,478 | 6,872 | 91.90% | 6,971 | 6,309 | 90.50% | -1.39pp |
| Adyen_Klarna | 1,768 | 1,645 | 93.04% | 2,078 | 1,923 | 92.54% | -0.50pp |
| ProcessOut_ApplePay | 1,384 | 1,249 | 90.25% | 1,623 | 1,444 | 88.97% | -1.27pp |
| Adyen_CreditCard | 1,481 | 1,450 | 97.91% | 1,555 | 1,507 | 96.91% | -0.99pp |
| Adyen_IDeal | 1,386 | 1,256 | 90.62% | 1,195 | 1,079 | 90.29% | -0.33pp |
| Adyen_Sepa | 929 | 3 | 0.32% | 957 | 3 | 0.31% | -0.01pp |
| Adyen_BcmcMobile | 770 | 732 | 95.06% | 733 | 687 | 93.72% | -1.34pp |
| ProcessOut_Mobilepay | 285 | 273 | 95.79% | 228 | 213 | 93.42% | -2.37pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (4 countries in HF-INTL)

| Country | Volume | PCR 2026-W19 | PCR 2026-W20 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| FR | 16,121 | 30.72% | 28.78% | -1.94pp | 1 | 5 |
| GB | 17,085 | 41.11% | 40.47% | -0.64pp | 2 | 13 |
| NZ | 2,461 | 32.79% | 30.48% | -2.31pp | 6 | 2 |
| LU | 102 | 47.31% | 58.82% | +11.51pp | 11 | 1 |

---

### FR

#### Waterfall GA

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 15,961 | 16,121 | +160 | +1.00pp | - | - | - |
| Select Payment Method | 7,717 | 7,550 | -167 | -2.16pp | 48.35% | 46.83% | -1.52pp |
| Click Submit Form | 6,143 | 5,916 | -227 | -3.70pp | 79.60% | 78.36% | -1.25pp |
| FE Validation Passed | 5,763 | 5,479 | -284 | -4.93pp | 93.81% | 92.61% | -1.20pp |
| Enter Fraud Service | 5,439 | 5,246 | -193 | -3.55pp | 94.38% | 95.75% | +1.37pp |
| Approved by Fraud Service | 5,013 | 4,769 | -244 | -4.87pp | 92.17% | 90.91% | -1.26pp |
| Call to PVS | 5,034 | 4,757 | -277 | -5.50pp | 100.42% | 99.75% | -0.67pp |
| **Successful Checkout** | 4,903 | 4,639 | -264 | -5.38pp | 97.40% | 97.52% | +0.12pp |
| **PCR Rate** | | | | | 30.72% | 28.78% | **-1.94pp** |

**Key Driver:** Select Payment Method (-1.52pp)

#### Waterfall Backend

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 20,010 | 19,560 | -450 | -2.25pp | - | - | - |
| Checkout Attempt | 8,020 | 7,694 | -326 | -4.06pp | 40.08% | 39.34% | -0.74pp |
| Enter Fraud Service | 7,996 | 7,673 | -323 | -4.04pp | 99.70% | 99.73% | +0.03pp |
| Approved by Fraud Service | 7,048 | 6,723 | -325 | -4.61pp | 88.14% | 87.62% | -0.53pp |
| PVS Attempt | 7,051 | 6,690 | -361 | -5.12pp | 100.04% | 99.51% | -0.53pp |
| PVS Success | 6,566 | 6,260 | -306 | -4.66pp | 93.12% | 93.57% | +0.45pp |
| **Successful Checkout** | 6,959 | 6,590 | -369 | -5.30pp | 105.99% | 105.27% | -0.71pp |

**Key Driver:** Checkout Attempt (-0.74pp)

---

### NZ

#### Waterfall GA

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 2,205 | 2,461 | +256 | +11.61pp | - | - | - |
| Select Payment Method | 1,141 | 1,271 | +130 | +11.39pp | 51.75% | 51.65% | -0.10pp |
| Click Submit Form | 891 | 973 | +82 | +9.20pp | 78.09% | 76.55% | -1.54pp |
| FE Validation Passed | 832 | 896 | +64 | +7.69pp | 93.38% | 92.09% | -1.29pp |
| Enter Fraud Service | 804 | 873 | +69 | +8.58pp | 96.63% | 97.43% | +0.80pp |
| Approved by Fraud Service | 751 | 792 | +41 | +5.46pp | 93.41% | 90.72% | -2.69pp |
| Call to PVS | 751 | 779 | +28 | +3.73pp | 100.00% | 98.36% | -1.64pp |
| **Successful Checkout** | 723 | 750 | +27 | +3.73pp | 96.27% | 96.28% | +0.01pp |
| **PCR Rate** | | | | | 32.79% | 30.48% | **-2.31pp** |

**Key Driver:** Approved by Fraud Service (-2.69pp)

#### Waterfall Backend

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 2,523 | 2,721 | +198 | +7.85pp | - | - | - |
| Checkout Attempt | 914 | 991 | +77 | +8.42pp | 36.23% | 36.42% | +0.19pp |
| Enter Fraud Service | 910 | 989 | +79 | +8.68pp | 99.56% | 99.80% | +0.24pp |
| Approved by Fraud Service | 822 | 864 | +42 | +5.11pp | 90.33% | 87.36% | -2.97pp |
| PVS Attempt | 795 | 832 | +37 | +4.65pp | 96.72% | 96.30% | -0.42pp |
| PVS Success | 731 | 770 | +39 | +5.34pp | 91.95% | 92.55% | +0.60pp |
| **Successful Checkout** | 795 | 827 | +32 | +4.03pp | 108.76% | 107.40% | -1.35pp |

**Key Driver:** Approved by Fraud Service (-2.97pp)

---

### LU

#### Waterfall GA

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 93 | 102 | +9 | +9.68pp | - | - | - |
| Select Payment Method | 60 | 77 | +17 | +28.33pp | 64.52% | 75.49% | +10.97pp |
| Click Submit Form | 52 | 72 | +20 | +38.46pp | 86.67% | 93.51% | +6.84pp |
| FE Validation Passed | 50 | 65 | +15 | +30.00pp | 96.15% | 90.28% | -5.88pp |
| Enter Fraud Service | 49 | 64 | +15 | +30.61pp | 98.00% | 98.46% | +0.46pp |
| Approved by Fraud Service | 47 | 64 | +17 | +36.17pp | 95.92% | 100.00% | +4.08pp |
| Call to PVS | 45 | 64 | +19 | +42.22pp | 95.74% | 100.00% | +4.26pp |
| **Successful Checkout** | 44 | 60 | +16 | +36.36pp | 97.78% | 93.75% | -4.03pp |
| **PCR Rate** | | | | | 47.31% | 58.82% | **+11.51pp** |

**Key Driver:** Select Payment Method (+10.97pp)

#### Waterfall Backend

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 288 | 264 | -24 | -8.33pp | - | - | - |
| Checkout Attempt | 69 | 84 | +15 | +21.74pp | 23.96% | 31.82% | +7.86pp |
| Enter Fraud Service | 63 | 70 | +7 | +11.11pp | 91.30% | 83.33% | -7.97pp |
| Approved by Fraud Service | 60 | 70 | +10 | +16.67pp | 95.24% | 100.00% | +4.76pp |
| PVS Attempt | 57 | 70 | +13 | +22.81pp | 95.00% | 100.00% | +5.00pp |
| PVS Success | 55 | 66 | +11 | +20.00pp | 96.49% | 94.29% | -2.21pp |
| **Successful Checkout** | 59 | 82 | +23 | +38.98pp | 107.27% | 124.24% | +16.97pp |

**Key Driver:** Successful Checkout (+16.97pp)

---

### GB

#### Waterfall GA

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 18,714 | 17,085 | -1,629 | -8.70pp | - | - | - |
| Select Payment Method | 10,912 | 9,984 | -928 | -8.50pp | 58.31% | 58.44% | +0.13pp |
| Click Submit Form | 9,146 | 8,336 | -810 | -8.86pp | 83.82% | 83.49% | -0.32pp |
| FE Validation Passed | 8,480 | 7,715 | -765 | -9.02pp | 92.72% | 92.55% | -0.17pp |
| Enter Fraud Service | 8,207 | 7,529 | -678 | -8.26pp | 96.78% | 97.59% | +0.81pp |
| Approved by Fraud Service | 7,890 | 7,138 | -752 | -9.53pp | 96.14% | 94.81% | -1.33pp |
| Call to PVS | 7,838 | 7,051 | -787 | -10.04pp | 99.34% | 98.78% | -0.56pp |
| **Successful Checkout** | 7,693 | 6,915 | -778 | -10.11pp | 98.15% | 98.07% | -0.08pp |
| **PCR Rate** | | | | | 41.11% | 40.47% | **-0.63pp** |

**Key Driver:** Approved by Fraud Service (-1.33pp)

#### Waterfall Backend

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 22,701 | 20,006 | -2,695 | -11.87pp | - | - | - |
| Checkout Attempt | 11,593 | 10,333 | -1,260 | -10.87pp | 51.07% | 51.65% | +0.58pp |
| Enter Fraud Service | 11,535 | 10,298 | -1,237 | -10.72pp | 99.50% | 99.66% | +0.16pp |
| Approved by Fraud Service | 10,775 | 9,579 | -1,196 | -11.10pp | 93.41% | 93.02% | -0.39pp |
| PVS Attempt | 8,717 | 7,532 | -1,185 | -13.59pp | 80.90% | 78.63% | -2.27pp |
| PVS Success | 8,489 | 7,316 | -1,173 | -13.82pp | 97.38% | 97.13% | -0.25pp |
| **Successful Checkout** | 10,624 | 9,400 | -1,224 | -11.52pp | 125.15% | 128.49% | +3.34pp |

**Key Driver:** Successful Checkout (+3.34pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (-0.49pp) meets threshold (+0.43pp)

### Recovery Rate

| Metric | 2026-W19 | 2026-W20 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 5,234 | 5,274 | 40 |
| Error → Passed | 3,167 | 3,117 | -50 |
| **Recovery Rate** | **60.51%** | **59.10%** | **-1.41pp** |

### Error Type Distribution

| Error Type | 2026-W19 | 2026-W19 % | 2026-W20 | 2026-W20 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 3,928 | 75.0% | 3,968 | 75.2% | +0.19pp |
| PAYPAL_POPUP_CLOSED | 996 | 19.0% | 1,011 | 19.2% | +0.14pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 290 | 5.5% | 292 | 5.5% | -0.00pp |
| PAYPAL_TOKENISE_ERR | 122 | 2.3% | 128 | 2.4% | +0.10pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 128 | 2.4% | 125 | 2.4% | -0.08pp |
| CC_TOKENISE_ERR | 121 | 2.3% | 99 | 1.9% | -0.43pp |
| APPLEPAY_MERCHANT_VALIDATION_ERR | 1 | 0.0% | 5 | 0.1% | +0.08pp |


---

## Fraud Analysis

**Include reason:** Enter FS Δ (+0.77pp) meets threshold (+0.43pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W19 | 2026-W19 % | 2026-W20 | 2026-W20 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 40,870 | - | 39,231 | - | -1,639 | -4.0% |
| Enter Fraud Service | 39,734 | - | 38,026 | - | -1,708 | -4.3% |
| **Gap (Skipped)** | **1,136** | **2.78%** | **1,205** | **3.07%** | **69** | **+0.29pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W19 Gap | 2026-W19 % | 2026-W20 Gap | 2026-W20 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Adyen_Sepa | 928 | 83.9% | 957 | 80.7% | +29 | -3.21pp |
| NoPayment | 40 | 3.6% | 120 | 10.1% | +80 | +6.50pp |
| Braintree_ApplePay | 50 | 4.5% | 49 | 4.1% | -1 | -0.39pp |
| ProcessOut_CreditCard | 49 | 4.4% | 36 | 3.0% | -13 | -1.39pp |
| Braintree_Paypal | 39 | 3.5% | 24 | 2.0% | -15 | -1.50pp |
| **Total** | **1,106** | **100%** | **1,186** | **100%** | **80** | - |

*% of Gap = Payment Method Gap / Total Gap*

---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (+0.55pp) meets threshold (+0.43pp)

| Decline Reason | 2026-W19 | 2026-W19 % | 2026-W20 | 2026-W20 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| RedirectShopper | 517 | 28.1% | 368 | 23.1% | -149 | -4.98pp |
| Cancelled: Cancelled | 384 | 20.8% | 225 | 14.1% | -159 | -6.73pp |
| CHARGE_STATE_FAILURE: Customer abandoned payment after 60 minutes | 84 | 4.6% | 207 | 13.0% | +123 | +8.43pp |
| CHARGE_STATE_FAILURE: No action was initiated on the transaction yet. | 250 | 13.6% | 191 | 12.0% | -59 | -1.59pp |
| Failed Verification: Insufficient Funds | 153 | 8.3% | 141 | 8.8% | -12 | +0.54pp |
| Refused: Refused | 53 | 2.9% | 134 | 8.4% | +81 | +5.53pp |
| Pending | 174 | 9.4% | 128 | 8.0% | -46 | -1.42pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 79 | 4.3% | 77 | 4.8% | -2 | +0.54pp |
| Verified | 86 | 4.7% | 68 | 4.3% | -18 | -0.40pp |
| Failed Verification: Declined | 62 | 3.4% | 55 | 3.5% | -7 | +0.08pp |
| **Total PVS Failures** | **1,842** | **100%** | **1,594** | **100%** | **-248** | - |

---


---

*Report: 2026-05-19*
