# PCR Investigation: HF-INTL 2026-W14

**Metric:** Payment Conversion Rate  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 34.88% → 36.04% (+1.16pp)  
**Volume:** 62,654 payment visits  
**Threshold:** +0.58pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** PCR improved significantly from 34.88% to 36.04% (+1.16pp) in 2026-W14, exceeding the threshold of +0.58pp, driven primarily by improvements in early funnel stages and payment verification success.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ≥ threshold? | +0.42pp | ✅ |
| Click Submit Form | ≥ threshold? | +0.59pp | ⚠️ |
| FE Validation Passed | ≥ threshold? | +0.68pp | ⚠️ |
| Enter Fraud Service | ≥ threshold? | +0.40pp | ✅ |
| Approved by Fraud Service | ≥ threshold? | -0.21pp | ✅ |
| Call to PVS | ≥ threshold? | -0.03pp | ✅ |
| Successful Checkout (PVS Success) | ≥ threshold? | +0.85pp | ⚠️ |

**Key Findings:**
- FR showed the largest contribution to improvement with PCR increasing +3.10pp, driven by Select Payment Method conversion (+2.98pp GA, +3.77pp Backend Checkout Attempt)
- DK demonstrated strong performance with +5.89pp PCR improvement despite lower volume, with Select Payment Method (+4.17pp) as the key driver
- FE Validation recovery rate improved from 56.10% to 57.57% (+1.47pp), with APPLEPAY_DISMISSED remaining the dominant error type (76.8%)
- PVS failures decreased significantly (-512 total failures), with "Failed Verification: Insufficient Funds" dropping notably (-132 count, -4.31pp share)
- Braintree_ApplePay showed meaningful improvement (+1.70pp) while ProcessOut_ApplePay declined (-1.20pp)

**Action:** Monitor - The positive trend across multiple funnel stages and countries suggests organic improvement; continue tracking FR and DK performance while monitoring ApplePay payment method divergence.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 82,373 | 62,654 | -19,719 | -23.9% | - | - | - |
| Select Payment Method | 45,198 | 34,643 | -10,555 | -23.4% | 54.87% | 55.29% | +0.42pp |
| Click Submit Form | 36,437 | 28,132 | -8,305 | -22.8% | 80.62% | 81.21% | +0.59pp |
| FE Validation Passed | 33,860 | 26,334 | -7,526 | -22.2% | 92.93% | 93.61% | +0.68pp |
| Enter Fraud Service | 32,610 | 25,466 | -7,144 | -21.9% | 96.31% | 96.70% | +0.40pp |
| Approved by Fraud Service | 30,636 | 23,871 | -6,765 | -22.1% | 93.95% | 93.74% | -0.21pp |
| Call to PVS | 30,582 | 23,821 | -6,761 | -22.1% | 99.82% | 99.79% | -0.03pp |
| **Successful Checkout** | 28,731 | 22,581 | -6,150 | -21.4% | 93.95% | 94.79% | +0.85pp |
| **PCR Rate** | | | | | 34.88% | 36.04% | **+1.16pp** |

### Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 106,120 | 81,560 | -24,560 | -23.1% | - | - | - |
| Checkout Attempt | 47,601 | 37,841 | -9,760 | -20.5% | 44.86% | 46.40% | +1.54pp |
| Enter Fraud Service | 46,295 | 36,671 | -9,624 | -20.8% | 97.26% | 96.91% | -0.35pp |
| Approved by Fraud Service | 42,663 | 33,636 | -9,027 | -21.2% | 92.15% | 91.72% | -0.43pp |
| PVS Attempt | 39,598 | 31,465 | -8,133 | -20.5% | 92.82% | 93.55% | +0.73pp |
| PVS Success | 37,702 | 30,206 | -7,496 | -19.9% | 95.21% | 96.00% | +0.79pp |
| **Successful Checkout** | 41,021 | 32,545 | -8,476 | -20.7% | 108.80% | 107.74% | -1.06pp |
| **PCR Rate** | | | | | 38.66% | 39.90% | **+1.25pp** |

### Payment Method Breakdown

| Payment Method | 2026-W13 Attempt | 2026-W13 Success | 2026-W13 Rate | 2026-W14 Attempt | 2026-W14 Success | 2026-W14 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 17,791 | 15,715 | 88.33% | 14,680 | 12,973 | 88.37% | +0.04pp |
| Braintree_ApplePay | 13,360 | 11,186 | 83.73% | 10,592 | 9,049 | 85.43% | +1.70pp |
| Braintree_Paypal | 9,125 | 8,314 | 91.11% | 7,030 | 6,377 | 90.71% | -0.40pp |
| Adyen_Klarna | 2,195 | 2,082 | 94.85% | 1,481 | 1,394 | 94.13% | -0.73pp |
| Adyen_IDeal | 1,887 | 1,732 | 91.79% | 1,322 | 1,218 | 92.13% | +0.35pp |
| ProcessOut_ApplePay | 1,558 | 1,429 | 91.72% | 1,213 | 1,098 | 90.52% | -1.20pp |
| Adyen_Sepa | 984 | 2 | 0.20% | 1,024 | 3 | 0.29% | +0.09pp |
| Adyen_BcmcMobile | 475 | 460 | 96.84% | 384 | 368 | 95.83% | -1.01pp |
| Adyen_CreditCard | 116 | 100 | 86.21% | 69 | 63 | 91.30% | +5.10pp |
| NoPayment | 105 | 0 | 0.00% | 42 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (4 countries in HF-INTL)

| Country | Volume | PCR 2026-W13 | PCR 2026-W14 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| FR | 16,752 | 29.08% | 32.18% | +3.10pp | 1 | 3 |
| AU | 6,338 | 34.87% | 36.48% | +1.61pp | 2 | 6 |
| DK | 1,407 | 42.72% | 48.61% | +5.89pp | 4 | 2 |
| LU | 59 | 49.41% | 57.63% | +8.22pp | 12 | 1 |

---

### FR

#### Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 21,892 | 16,752 | -5,140 | -23.48pp | - | - | - |
| Select Payment Method | 10,249 | 8,342 | -1,907 | -18.61pp | 46.82% | 49.80% | +2.98pp |
| Click Submit Form | 8,054 | 6,662 | -1,392 | -17.28pp | 78.58% | 79.86% | +1.28pp |
| FE Validation Passed | 7,496 | 6,272 | -1,224 | -16.33pp | 93.07% | 94.15% | +1.07pp |
| Enter Fraud Service | 7,205 | 6,071 | -1,134 | -15.74pp | 96.12% | 96.80% | +0.68pp |
| Approved by Fraud Service | 6,575 | 5,535 | -1,040 | -15.82pp | 91.26% | 91.17% | -0.08pp |
| Call to PVS | 6,581 | 5,544 | -1,037 | -15.76pp | 100.09% | 100.16% | +0.07pp |
| **Successful Checkout** | 6,367 | 5,391 | -976 | -15.33pp | 96.75% | 97.24% | +0.49pp |
| **PCR Rate** | | | | | 29.08% | 32.18% | **+3.10pp** |

**Key Driver:** Select Payment Method (+2.98pp)

#### Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 29,173 | 22,499 | -6,674 | -22.88pp | - | - | - |
| Checkout Attempt | 10,942 | 9,288 | -1,654 | -15.12pp | 37.51% | 41.28% | +3.77pp |
| Enter Fraud Service | 10,913 | 9,274 | -1,639 | -15.02pp | 99.73% | 99.85% | +0.11pp |
| Approved by Fraud Service | 9,699 | 8,163 | -1,536 | -15.84pp | 88.88% | 88.02% | -0.86pp |
| PVS Attempt | 9,691 | 8,159 | -1,532 | -15.81pp | 99.92% | 99.95% | +0.03pp |
| PVS Success | 9,459 | 8,029 | -1,430 | -15.12pp | 97.61% | 98.41% | +0.80pp |
| **Successful Checkout** | 9,497 | 8,058 | -1,439 | -15.15pp | 100.40% | 100.36% | -0.04pp |

**Key Driver:** Checkout Attempt (+3.77pp)

---

### AU

#### Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 8,615 | 6,338 | -2,277 | -26.43pp | - | - | - |
| Select Payment Method | 4,489 | 3,376 | -1,113 | -24.79pp | 52.11% | 53.27% | +1.16pp |
| Click Submit Form | 3,772 | 2,841 | -931 | -24.68pp | 84.03% | 84.15% | +0.13pp |
| FE Validation Passed | 3,402 | 2,603 | -799 | -23.49pp | 90.19% | 91.62% | +1.43pp |
| Enter Fraud Service | 3,300 | 2,534 | -766 | -23.21pp | 97.00% | 97.35% | +0.35pp |
| Approved by Fraud Service | 3,099 | 2,388 | -711 | -22.94pp | 93.91% | 94.24% | +0.33pp |
| Call to PVS | 3,094 | 2,377 | -717 | -23.17pp | 99.84% | 99.54% | -0.30pp |
| **Successful Checkout** | 3,004 | 2,312 | -692 | -23.04pp | 97.09% | 97.27% | +0.17pp |
| **PCR Rate** | | | | | 34.87% | 36.48% | **+1.61pp** |

**Key Driver:** FE Validation Passed (+1.43pp)

#### Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 9,530 | 7,185 | -2,345 | -24.61pp | - | - | - |
| Checkout Attempt | 3,886 | 3,029 | -857 | -22.05pp | 40.78% | 42.16% | +1.38pp |
| Enter Fraud Service | 3,864 | 3,015 | -849 | -21.97pp | 99.43% | 99.54% | +0.10pp |
| Approved by Fraud Service | 3,573 | 2,794 | -779 | -21.80pp | 92.47% | 92.67% | +0.20pp |
| PVS Attempt | 3,140 | 2,464 | -676 | -21.53pp | 87.88% | 88.19% | +0.31pp |
| PVS Success | 3,062 | 2,401 | -661 | -21.59pp | 97.52% | 97.44% | -0.07pp |
| **Successful Checkout** | 3,498 | 2,725 | -773 | -22.10pp | 114.24% | 113.49% | -0.74pp |

**Key Driver:** Checkout Attempt (+1.38pp)

---

### LU

#### Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 85 | 59 | -26 | -30.59pp | - | - | - |
| Select Payment Method | 53 | 40 | -13 | -24.53pp | 62.35% | 67.80% | +5.44pp |
| Click Submit Form | 51 | 37 | -14 | -27.45pp | 96.23% | 92.50% | -3.73pp |
| FE Validation Passed | 48 | 35 | -13 | -27.08pp | 94.12% | 94.59% | +0.48pp |
| Enter Fraud Service | 45 | 35 | -10 | -22.22pp | 93.75% | 100.00% | +6.25pp |
| Approved by Fraud Service | 45 | 35 | -10 | -22.22pp | 100.00% | 100.00% | +0.00pp |
| Call to PVS | 44 | 35 | -9 | -20.45pp | 97.78% | 100.00% | +2.22pp |
| **Successful Checkout** | 42 | 34 | -8 | -19.05pp | 95.45% | 97.14% | +1.69pp |
| **PCR Rate** | | | | | 49.41% | 57.63% | **+8.22pp** |

**Key Driver:** Enter Fraud Service (+6.25pp)

#### Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 282 | 256 | -26 | -9.22pp | - | - | - |
| Checkout Attempt | 86 | 75 | -11 | -12.79pp | 30.50% | 29.30% | -1.20pp |
| Enter Fraud Service | 65 | 62 | -3 | -4.62pp | 75.58% | 82.67% | +7.09pp |
| Approved by Fraud Service | 65 | 62 | -3 | -4.62pp | 100.00% | 100.00% | +0.00pp |
| PVS Attempt | 64 | 61 | -3 | -4.69pp | 98.46% | 98.39% | -0.07pp |
| PVS Success | 62 | 60 | -2 | -3.23pp | 96.88% | 98.36% | +1.49pp |
| **Successful Checkout** | 81 | 73 | -8 | -9.88pp | 130.65% | 121.67% | -8.98pp |

**Key Driver:** Successful Checkout (-8.98pp)

---

### DK

#### Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 1,573 | 1,407 | -166 | -10.55pp | - | - | - |
| Select Payment Method | 1,002 | 955 | -47 | -4.69pp | 63.70% | 67.87% | +4.17pp |
| Click Submit Form | 848 | 820 | -28 | -3.30pp | 84.63% | 85.86% | +1.23pp |
| FE Validation Passed | 791 | 778 | -13 | -1.64pp | 93.28% | 94.88% | +1.60pp |
| Enter Fraud Service | 768 | 759 | -9 | -1.17pp | 97.09% | 97.56% | +0.47pp |
| Approved by Fraud Service | 698 | 696 | -2 | -0.29pp | 90.89% | 91.70% | +0.81pp |
| Call to PVS | 694 | 695 | +1 | +0.14pp | 99.43% | 99.86% | +0.43pp |
| **Successful Checkout** | 672 | 684 | +12 | +1.79pp | 96.83% | 98.42% | +1.59pp |
| **PCR Rate** | | | | | 42.72% | 48.61% | **+5.89pp** |

**Key Driver:** Select Payment Method (+4.17pp)

#### Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 2,170 | 1,976 | -194 | -8.94pp | - | - | - |
| Checkout Attempt | 1,115 | 1,111 | -4 | -0.36pp | 51.38% | 56.22% | +4.84pp |
| Enter Fraud Service | 1,106 | 1,107 | +1 | +0.09pp | 99.19% | 99.64% | +0.45pp |
| Approved by Fraud Service | 991 | 984 | -7 | -0.71pp | 89.60% | 88.89% | -0.71pp |
| PVS Attempt | 961 | 966 | +5 | +0.52pp | 96.97% | 98.17% | +1.20pp |
| PVS Success | 944 | 957 | +13 | +1.38pp | 98.23% | 99.07% | +0.84pp |
| **Successful Checkout** | 972 | 976 | +4 | +0.41pp | 102.97% | 101.99% | -0.98pp |

**Key Driver:** Checkout Attempt (+4.84pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (+0.68pp) meets threshold (+0.58pp)

### Recovery Rate

| Metric | 2026-W13 | 2026-W14 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 6,594 | 4,801 | -1,793 |
| Error → Passed | 3,699 | 2,764 | -935 |
| **Recovery Rate** | **56.10%** | **57.57%** | **+1.47pp** |

### Error Type Distribution

| Error Type | 2026-W13 | 2026-W13 % | 2026-W14 | 2026-W14 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 4,957 | 75.2% | 3,689 | 76.8% | +1.66pp |
| PAYPAL_POPUP_CLOSED | 1,434 | 21.7% | 910 | 19.0% | -2.79pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 329 | 5.0% | 255 | 5.3% | +0.32pp |
| PAYPAL_TOKENISE_ERR | 170 | 2.6% | 106 | 2.2% | -0.37pp |
| CC_TOKENISE_ERR | 122 | 1.9% | 102 | 2.1% | +0.27pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 150 | 2.3% | 98 | 2.0% | -0.23pp |
| APPLEPAY_TOKENISE_ERR | 0 | 0.0% | 6 | 0.1% | +0.12pp |
| APPLEPAY_MERCHANT_VALIDATION_ERR | 2 | 0.0% | 1 | 0.0% | -0.01pp |


---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (+0.85pp) meets threshold (+0.58pp)

| Decline Reason | 2026-W13 | 2026-W13 % | 2026-W14 | 2026-W14 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| RedirectShopper | 455 | 29.9% | 325 | 32.2% | -130 | +2.28pp |
| Cancelled: Cancelled | 239 | 15.7% | 192 | 19.0% | -47 | +3.31pp |
| Failed Verification: Insufficient Funds | 263 | 17.3% | 131 | 13.0% | -132 | -4.31pp |
| Failed Verification: Declined | 130 | 8.5% | 90 | 8.9% | -40 | +0.37pp |
| Pending | 128 | 8.4% | 88 | 8.7% | -40 | +0.30pp |
| Refused: Refused | 163 | 10.7% | 83 | 8.2% | -80 | -2.49pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 103 | 6.8% | 58 | 5.7% | -45 | -1.02pp |
| Failed Verification: Security | 25 | 1.6% | 24 | 2.4% | -1 | +0.73pp |
| Failed Verification: OK: 83 : Fraud/Security | 11 | 0.7% | 10 | 1.0% | -1 | +0.27pp |
| Blocked Verification: Payment method is blocked due to business reasons | 5 | 0.3% | 9 | 0.9% | +4 | +0.56pp |
| **Total PVS Failures** | **1,522** | **100%** | **1,010** | **100%** | **-512** | - |

---


---

*Report: 2026-04-10*
