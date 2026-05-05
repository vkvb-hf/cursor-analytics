# PCR Investigation: HF-INTL 2026-W18

**Metric:** Payment Conversion Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 36.00% → 36.49% (+0.49pp)  
**Volume:** 70,952 payment visits  
**Threshold:** +0.25pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate improved from 36.00% to 36.49% (+0.49pp) on 70,952 payment visits, exceeding the monitoring threshold of +0.25pp.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ≥-0.25pp | +0.28pp | ✅ |
| Click Submit Form | ≥-0.25pp | +1.12pp | ✅ |
| FE Validation Passed | ≥-0.25pp | +0.64pp | ✅ |
| Enter Fraud Service | ≥-0.25pp | -0.45pp | ⚠️ |
| Approved by Fraud Service | ≥-0.25pp | +0.29pp | ✅ |
| Call to PVS | ≥-0.25pp | +0.01pp | ✅ |
| Successful Checkout | ≥-0.25pp | -1.00pp | ⚠️ |

**Key Findings:**
- **PVS failures nearly doubled:** Total PVS failures increased from 806 to 1,494 (+688), with a new error "CHARGE_STATE_FAILURE: No action was initiated on the transaction yet" appearing (226 occurrences, 15.1% of failures) and "Cancelled: Cancelled" rising significantly (+132 occurrences)
- **NO experienced significant PCR decline:** NO dropped -4.32pp (47.70% → 43.38%), primarily driven by Select Payment Method conversion falling -5.09pp
- **DE and FR drove overall improvement:** DE contributed +1.91pp and FR contributed +1.68pp to PCR, with both showing strong improvements in Click Submit Form conversion (+2.81pp and +1.80pp respectively)
- **Fraud service entry rate declined:** Enter Fraud Service conversion dropped -0.45pp, though the gap (skipped transactions) actually decreased by 191 transactions, largely due to reduced Adyen_Sepa volume (-202 skipped)
- **ProcessOut_Mobilepay showed massive improvement:** Conversion rate jumped from 33.33% to 96.25% (+62.92pp), though on small volume (3 → 240 attempts)

**Action:** Investigate - The new PVS error type "CHARGE_STATE_FAILURE: No action was initiated" requires immediate investigation as it represents a significant new failure mode; also monitor NO for continued Select Payment Method degradation.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 72,694 | 70,952 | -1,742 | -2.4% | - | - | - |
| Select Payment Method | 39,985 | 39,223 | -762 | -1.9% | 55.00% | 55.28% | +0.28pp |
| Click Submit Form | 32,467 | 32,287 | -180 | -0.6% | 81.20% | 82.32% | +1.12pp |
| FE Validation Passed | 30,332 | 30,369 | 37 | 0.1% | 93.42% | 94.06% | +0.64pp |
| Enter Fraud Service | 29,093 | 28,993 | -100 | -0.3% | 95.92% | 95.47% | -0.45pp |
| Approved by Fraud Service | 27,503 | 27,493 | -10 | -0.0% | 94.53% | 94.83% | +0.29pp |
| Call to PVS | 27,333 | 27,327 | -6 | -0.0% | 99.38% | 99.40% | +0.01pp |
| **Successful Checkout** | 26,170 | 25,891 | -279 | -1.1% | 95.75% | 94.75% | -1.00pp |
| **PCR Rate** | | | | | 36.00% | 36.49% | **+0.49pp** |

### Waterfall Backend

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 90,855 | 88,569 | -2,286 | -2.5% | - | - | - |
| Checkout Attempt | 42,480 | 42,247 | -233 | -0.5% | 46.76% | 47.70% | +0.94pp |
| Enter Fraud Service | 40,922 | 40,880 | -42 | -0.1% | 96.33% | 96.76% | +0.43pp |
| Approved by Fraud Service | 37,878 | 37,737 | -141 | -0.4% | 92.56% | 92.31% | -0.25pp |
| PVS Attempt | 34,080 | 34,181 | 101 | 0.3% | 89.97% | 90.58% | +0.60pp |
| PVS Success | 32,944 | 32,190 | -754 | -2.3% | 96.67% | 94.18% | -2.49pp |
| **Successful Checkout** | 36,198 | 36,169 | -29 | -0.1% | 109.88% | 112.36% | +2.48pp |
| **PCR Rate** | | | | | 39.84% | 40.84% | **+1.00pp** |

### Payment Method Breakdown

| Payment Method | 2026-W17 Attempt | 2026-W17 Success | 2026-W17 Rate | 2026-W18 Attempt | 2026-W18 Success | 2026-W18 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 13,554 | 11,768 | 86.82% | 13,625 | 11,801 | 86.61% | -0.21pp |
| Braintree_ApplePay | 12,455 | 10,503 | 84.33% | 12,090 | 10,209 | 84.44% | +0.11pp |
| Braintree_Paypal | 9,178 | 8,424 | 91.78% | 8,048 | 7,349 | 91.31% | -0.47pp |
| Adyen_Klarna | 846 | 802 | 94.80% | 1,773 | 1,659 | 93.57% | -1.23pp |
| ProcessOut_ApplePay | 1,486 | 1,334 | 89.77% | 1,540 | 1,363 | 88.51% | -1.26pp |
| Adyen_CreditCard | 1,729 | 1,691 | 97.80% | 1,524 | 1,485 | 97.44% | -0.36pp |
| Adyen_IDeal | 1,129 | 1,025 | 90.79% | 1,390 | 1,268 | 91.22% | +0.43pp |
| Adyen_Sepa | 1,321 | 3 | 0.23% | 1,118 | 2 | 0.18% | -0.05pp |
| Adyen_BcmcMobile | 688 | 647 | 94.04% | 698 | 666 | 95.42% | +1.37pp |
| ProcessOut_Mobilepay | 3 | 1 | 33.33% | 240 | 231 | 96.25% | +62.92pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (4 countries in HF-INTL)

| Country | Volume | PCR 2026-W17 | PCR 2026-W18 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| DE | 13,595 | 35.24% | 37.15% | +1.91pp | 1 | 6 |
| FR | 15,417 | 27.66% | 29.34% | +1.68pp | 2 | 8 |
| DK | 1,705 | 45.49% | 49.15% | +3.66pp | 4 | 2 |
| NO | 1,268 | 47.70% | 43.38% | -4.32pp | 6 | 1 |

---

### NO

#### Waterfall GA

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 1,195 | 1,268 | +73 | +6.11pp | - | - | - |
| Select Payment Method | 745 | 726 | -19 | -2.55pp | 62.34% | 57.26% | -5.09pp |
| Click Submit Form | 639 | 601 | -38 | -5.95pp | 85.77% | 82.78% | -2.99pp |
| FE Validation Passed | 616 | 588 | -28 | -4.55pp | 96.40% | 97.84% | +1.44pp |
| Enter Fraud Service | 607 | 570 | -37 | -6.10pp | 98.54% | 96.94% | -1.60pp |
| Approved by Fraud Service | 586 | 563 | -23 | -3.92pp | 96.54% | 98.77% | +2.23pp |
| Call to PVS | 579 | 561 | -18 | -3.11pp | 98.81% | 99.64% | +0.84pp |
| **Successful Checkout** | 570 | 550 | -20 | -3.51pp | 98.45% | 98.04% | -0.41pp |
| **PCR Rate** | | | | | 47.70% | 43.38% | **-4.32pp** |

**Key Driver:** Select Payment Method (-5.09pp)

#### Waterfall Backend

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 1,572 | 1,598 | +26 | +1.65pp | - | - | - |
| Checkout Attempt | 804 | 784 | -20 | -2.49pp | 51.15% | 49.06% | -2.08pp |
| Enter Fraud Service | 800 | 778 | -22 | -2.75pp | 99.50% | 99.23% | -0.27pp |
| Approved by Fraud Service | 762 | 764 | +2 | +0.26pp | 95.25% | 98.20% | +2.95pp |
| PVS Attempt | 627 | 734 | +107 | +17.07pp | 82.28% | 96.07% | +13.79pp |
| PVS Success | 618 | 703 | +85 | +13.75pp | 98.56% | 95.78% | -2.79pp |
| **Successful Checkout** | 750 | 755 | +5 | +0.67pp | 121.36% | 107.40% | -13.96pp |

**Key Driver:** Successful Checkout (-13.96pp)

---

### FR

#### Waterfall GA

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 14,484 | 15,417 | +933 | +6.44pp | - | - | - |
| Select Payment Method | 6,581 | 7,216 | +635 | +9.65pp | 45.44% | 46.81% | +1.37pp |
| Click Submit Form | 5,172 | 5,801 | +629 | +12.16pp | 78.59% | 80.39% | +1.80pp |
| FE Validation Passed | 4,783 | 5,382 | +599 | +12.52pp | 92.48% | 92.78% | +0.30pp |
| Enter Fraud Service | 4,574 | 5,098 | +524 | +11.46pp | 95.63% | 94.72% | -0.91pp |
| Approved by Fraud Service | 4,149 | 4,670 | +521 | +12.56pp | 90.71% | 91.60% | +0.90pp |
| Call to PVS | 4,150 | 4,662 | +512 | +12.34pp | 100.02% | 99.83% | -0.20pp |
| **Successful Checkout** | 4,006 | 4,524 | +518 | +12.93pp | 96.53% | 97.04% | +0.51pp |
| **PCR Rate** | | | | | 27.66% | 29.34% | **+1.69pp** |

**Key Driver:** Click Submit Form (+1.80pp)

#### Waterfall Backend

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 18,251 | 19,464 | +1,213 | +6.65pp | - | - | - |
| Checkout Attempt | 6,815 | 7,660 | +845 | +12.40pp | 37.34% | 39.35% | +2.01pp |
| Enter Fraud Service | 6,801 | 7,637 | +836 | +12.29pp | 99.79% | 99.70% | -0.09pp |
| Approved by Fraud Service | 5,920 | 6,662 | +742 | +12.53pp | 87.05% | 87.23% | +0.19pp |
| PVS Attempt | 5,901 | 6,626 | +725 | +12.29pp | 99.68% | 99.46% | -0.22pp |
| PVS Success | 5,733 | 6,176 | +443 | +7.73pp | 97.15% | 93.21% | -3.94pp |
| **Successful Checkout** | 5,761 | 6,502 | +741 | +12.86pp | 100.49% | 105.28% | +4.79pp |

**Key Driver:** Successful Checkout (+4.79pp)

---

### DE

#### Waterfall GA

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 17,140 | 13,595 | -3,545 | -20.68pp | - | - | - |
| Select Payment Method | 9,977 | 8,151 | -1,826 | -18.30pp | 58.21% | 59.96% | +1.75pp |
| Click Submit Form | 7,602 | 6,440 | -1,162 | -15.29pp | 76.20% | 79.01% | +2.81pp |
| FE Validation Passed | 7,144 | 6,186 | -958 | -13.41pp | 93.98% | 96.06% | +2.08pp |
| Enter Fraud Service | 6,549 | 5,742 | -807 | -12.32pp | 91.67% | 92.82% | +1.15pp |
| Approved by Fraud Service | 6,339 | 5,573 | -766 | -12.08pp | 96.79% | 97.06% | +0.26pp |
| Call to PVS | 6,295 | 5,540 | -755 | -11.99pp | 99.31% | 99.41% | +0.10pp |
| **Successful Checkout** | 6,040 | 5,050 | -990 | -16.39pp | 95.95% | 91.16% | -4.79pp |
| **PCR Rate** | | | | | 35.24% | 37.15% | **+1.91pp** |

**Key Driver:** Successful Checkout (-4.79pp)

#### Waterfall Backend

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 21,803 | 17,544 | -4,259 | -19.53pp | - | - | - |
| Checkout Attempt | 9,620 | 8,562 | -1,058 | -11.00pp | 44.12% | 48.80% | +4.68pp |
| Enter Fraud Service | 9,582 | 8,509 | -1,073 | -11.20pp | 99.60% | 99.38% | -0.22pp |
| Approved by Fraud Service | 9,114 | 8,104 | -1,010 | -11.08pp | 95.12% | 95.24% | +0.12pp |
| PVS Attempt | 8,900 | 7,628 | -1,272 | -14.29pp | 97.65% | 94.13% | -3.53pp |
| PVS Success | 8,654 | 7,072 | -1,582 | -18.28pp | 97.24% | 92.71% | -4.52pp |
| **Successful Checkout** | 8,841 | 7,904 | -937 | -10.60pp | 102.16% | 111.76% | +9.60pp |

**Key Driver:** Successful Checkout (+9.60pp)

---

### DK

#### Waterfall GA

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 1,620 | 1,705 | +85 | +5.25pp | - | - | - |
| Select Payment Method | 1,000 | 1,068 | +68 | +6.80pp | 61.73% | 62.64% | +0.91pp |
| Click Submit Form | 848 | 944 | +96 | +11.32pp | 84.80% | 88.39% | +3.59pp |
| FE Validation Passed | 797 | 897 | +100 | +12.55pp | 93.99% | 95.02% | +1.04pp |
| Enter Fraud Service | 784 | 870 | +86 | +10.97pp | 98.37% | 96.99% | -1.38pp |
| Approved by Fraud Service | 747 | 849 | +102 | +13.65pp | 95.28% | 97.59% | +2.31pp |
| Call to PVS | 747 | 845 | +98 | +13.12pp | 100.00% | 99.53% | -0.47pp |
| **Successful Checkout** | 737 | 838 | +101 | +13.70pp | 98.66% | 99.17% | +0.51pp |
| **PCR Rate** | | | | | 45.49% | 49.15% | **+3.66pp** |

**Key Driver:** Click Submit Form (+3.59pp)

#### Waterfall Backend

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 2,277 | 2,324 | +47 | +2.06pp | - | - | - |
| Checkout Attempt | 1,185 | 1,258 | +73 | +6.16pp | 52.04% | 54.13% | +2.09pp |
| Enter Fraud Service | 1,181 | 1,251 | +70 | +5.93pp | 99.66% | 99.44% | -0.22pp |
| Approved by Fraud Service | 1,099 | 1,198 | +99 | +9.01pp | 93.06% | 95.76% | +2.71pp |
| PVS Attempt | 1,081 | 1,138 | +57 | +5.27pp | 98.36% | 94.99% | -3.37pp |
| PVS Success | 1,072 | 1,072 | 0 | +0.00pp | 99.17% | 94.20% | -4.97pp |
| **Successful Checkout** | 1,086 | 1,193 | +107 | +9.85pp | 101.31% | 111.29% | +9.98pp |

**Key Driver:** Successful Checkout (+9.98pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (+0.64pp) meets threshold (+0.25pp)

### Recovery Rate

| Metric | 2026-W17 | 2026-W18 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 5,641 | 5,298 | -343 |
| Error → Passed | 3,263 | 3,156 | -107 |
| **Recovery Rate** | **57.84%** | **59.57%** | **+1.73pp** |

### Error Type Distribution

| Error Type | 2026-W17 | 2026-W17 % | 2026-W18 | 2026-W18 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 4,246 | 75.3% | 4,035 | 76.2% | +0.89pp |
| PAYPAL_POPUP_CLOSED | 1,142 | 20.2% | 996 | 18.8% | -1.45pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 385 | 6.8% | 302 | 5.7% | -1.12pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 144 | 2.6% | 137 | 2.6% | +0.03pp |
| PAYPAL_TOKENISE_ERR | 145 | 2.6% | 124 | 2.3% | -0.23pp |
| CC_TOKENISE_ERR | 79 | 1.4% | 115 | 2.2% | +0.77pp |
| APPLEPAY_TOKENISE_ERR | 0 | 0.0% | 4 | 0.1% | +0.08pp |
| APPLEPAY_MERCHANT_VALIDATION_ERR | 6 | 0.1% | 2 | 0.0% | -0.07pp |
| EXPRESS_CHECKOUT_APPLEPAY_TOKENISE_ERR | 1 | 0.0% | 0 | 0.0% | -0.02pp |


---

## Fraud Analysis

**Include reason:** Enter FS Δ (-0.45pp) meets threshold (+0.25pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W17 | 2026-W17 % | 2026-W18 | 2026-W18 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 42,480 | - | 42,247 | - | -233 | -0.5% |
| Enter Fraud Service | 40,922 | - | 40,880 | - | -42 | -0.1% |
| **Gap (Skipped)** | **1,558** | **3.67%** | **1,367** | **3.24%** | **-191** | **-0.43pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W17 Gap | 2026-W17 % | 2026-W18 Gap | 2026-W18 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Adyen_Sepa | 1,320 | 86.0% | 1,118 | 84.2% | -202 | -1.86pp |
| NoPayment | 91 | 5.9% | 58 | 4.4% | -33 | -1.56pp |
| Braintree_ApplePay | 42 | 2.7% | 56 | 4.2% | +14 | +1.48pp |
| ProcessOut_CreditCard | 42 | 2.7% | 48 | 3.6% | +6 | +0.88pp |
| Braintree_Paypal | 39 | 2.5% | 48 | 3.6% | +9 | +1.07pp |
| **Total** | **1,534** | **100%** | **1,328** | **100%** | **-206** | - |

*% of Gap = Payment Method Gap / Total Gap*

---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (-1.00pp) meets threshold (+0.25pp)

| Decline Reason | 2026-W17 | 2026-W17 % | 2026-W18 | 2026-W18 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| RedirectShopper | 158 | 19.6% | 343 | 23.0% | +185 | +3.36pp |
| CHARGE_STATE_FAILURE: No action was initiated on the transaction yet. | 0 | 0.0% | 226 | 15.1% | +226 | +15.13pp |
| Cancelled: Cancelled | 64 | 7.9% | 196 | 13.1% | +132 | +5.18pp |
| Failed Verification: Insufficient Funds | 201 | 24.9% | 182 | 12.2% | -19 | -12.76pp |
| Pending | 167 | 20.7% | 156 | 10.4% | -11 | -10.28pp |
| Refused: Refused | 22 | 2.7% | 107 | 7.2% | +85 | +4.43pp |
| Verified | 1 | 0.1% | 77 | 5.2% | +76 | +5.03pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 85 | 10.5% | 69 | 4.6% | -16 | -5.93pp |
| Failed Verification: Declined | 105 | 13.0% | 69 | 4.6% | -36 | -8.41pp |
| CHARGE_STATE_FAILURE: The 3DS check has expired | 3 | 0.4% | 69 | 4.6% | +66 | +4.25pp |
| **Total PVS Failures** | **806** | **100%** | **1,494** | **100%** | **+688** | - |

---


---

*Report: 2026-05-05*
