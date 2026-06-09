# PCR Investigation: RTE 2026-W23

**Metric:** Payment Conversion Rate  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 38.71% → 39.81% (+1.10pp)  
**Volume:** 58,387 payment visits  
**Threshold:** +0.55pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate improved from 38.71% to 39.81% (+1.10pp) in week 2026-W23, driven primarily by improved FE Validation pass rates and consistent gains across all major payment methods.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Above threshold | +0.87pp | ✅ |
| Click Submit Form | Within normal range | +0.06pp | ✅ |
| FE Validation Passed | Above threshold | +0.87pp | ✅ |
| Enter Fraud Service | Within normal range | +0.12pp | ✅ |
| Approved by Fraud Service | Within normal range | +0.07pp | ✅ |
| Call to PVS | Minor decline | -0.13pp | ⚠️ |
| Successful Checkout | Within normal range | +0.03pp | ✅ |

**Key Findings:**
- FE Validation Passed conversion improved by +0.87pp, with APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR decreasing significantly (-4.41pp in error share), suggesting a fix to Apple Pay address validation
- All payment methods showed substantial success rate improvements: Braintree_ApplePay (+19.53pp), ProcessOut_CreditCard (+12.94pp), Braintree_Paypal (+12.71pp), Adyen_CreditCard (+12.56pp)
- FJ (largest market with 39,127 visits) improved +1.52pp, primarily driven by FE Validation Passed (+1.39pp)
- TV showed significant decline (-6.25pp) driven by Call to PVS step (-3.33pp), but low volume (488 visits) limits overall impact
- Error recovery rate improved from 67.44% to 69.99% (+2.55pp), indicating better user experience after encountering FE errors

**Action:** Monitor - The improvement appears to be driven by a systematic fix to FE validation (particularly Apple Pay address validation). Continue monitoring to confirm stability, but investigate the TV decline in PVS call rates if it persists.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 59,729 | 58,387 | -1,342 | -2.2% | - | - | - |
| Select Payment Method | 29,381 | 29,228 | -153 | -0.5% | 49.19% | 50.06% | +0.87pp |
| Click Submit Form | 26,324 | 26,204 | -120 | -0.5% | 89.60% | 89.65% | +0.06pp |
| FE Validation Passed | 25,623 | 25,734 | 111 | 0.4% | 97.34% | 98.21% | +0.87pp |
| Enter Fraud Service | 25,117 | 25,257 | 140 | 0.6% | 98.03% | 98.15% | +0.12pp |
| Approved by Fraud Service | 24,124 | 24,276 | 152 | 0.6% | 96.05% | 96.12% | +0.07pp |
| Call to PVS | 23,036 | 23,149 | 113 | 0.5% | 95.49% | 95.36% | -0.13pp |
| **Successful Checkout** | 23,124 | 23,244 | 120 | 0.5% | 100.38% | 100.41% | +0.03pp |
| **PCR Rate** | | | | | 38.71% | 39.81% | **+1.10pp** |

### Waterfall Backend

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 84,796 | 100,318 | 15,522 | 18.3% | - | - | - |
| Checkout Attempt | 37,438 | 38,824 | 1,386 | 3.7% | 44.15% | 38.70% | -5.45pp |
| Enter Fraud Service | 37,386 | 38,780 | 1,394 | 3.7% | 99.86% | 99.89% | +0.03pp |
| Approved by Fraud Service | 35,492 | 36,898 | 1,406 | 4.0% | 94.93% | 95.15% | +0.21pp |
| PVS Attempt | 35,018 | 36,387 | 1,369 | 3.9% | 98.66% | 98.62% | -0.05pp |
| PVS Success | 33,969 | 35,334 | 1,365 | 4.0% | 97.00% | 97.11% | +0.10pp |
| **Successful Checkout** | 29,112 | 35,809 | 6,697 | 23.0% | 85.70% | 101.34% | +15.64pp |
| **PCR Rate** | | | | | 34.33% | 35.70% | **+1.36pp** |

### Payment Method Breakdown

| Payment Method | 2026-W22 Attempt | 2026-W22 Success | 2026-W22 Rate | 2026-W23 Attempt | 2026-W23 Success | 2026-W23 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 14,987 | 12,031 | 80.28% | 16,454 | 15,338 | 93.22% | +12.94pp |
| Braintree_ApplePay | 9,057 | 6,557 | 72.40% | 8,890 | 8,172 | 91.92% | +19.53pp |
| Adyen_CreditCard | 8,143 | 6,299 | 77.35% | 8,051 | 7,239 | 89.91% | +12.56pp |
| Braintree_Paypal | 4,170 | 3,381 | 81.08% | 4,266 | 4,001 | 93.79% | +12.71pp |
| Adyen_IDeal | 473 | 365 | 77.17% | 507 | 465 | 91.72% | +14.55pp |
| Adyen_Klarna | 288 | 237 | 82.29% | 274 | 254 | 92.70% | +10.41pp |
| Adyen_BcmcMobile | 224 | 174 | 77.68% | 268 | 252 | 94.03% | +16.35pp |
| Braintree_CreditCard | 95 | 68 | 71.58% | 113 | 88 | 77.88% | +6.30pp |
| mc | 0 | 0 | 0.00% | 1 | 0 | 0.00% | +0.00pp |
| paypal | 1 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (4 countries in RTE)

| Country | Volume | PCR 2026-W22 | PCR 2026-W23 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| FJ | 39,127 | 38.54% | 40.06% | +1.52pp | 1 | 4 |
| CF | 10,215 | 41.64% | 42.58% | +0.94pp | 2 | 7 |
| TV | 488 | 44.98% | 38.73% | -6.25pp | 3 | 1 |
| TK | 440 | 39.76% | 43.86% | +4.10pp | 4 | 2 |

---

### TV

#### Waterfall GA

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 658 | 488 | -170 | -25.84pp | - | - | - |
| Select Payment Method | 425 | 301 | -124 | -29.18pp | 64.59% | 61.68% | -2.91pp |
| Click Submit Form | 379 | 266 | -113 | -29.82pp | 89.18% | 88.37% | -0.80pp |
| FE Validation Passed | 379 | 262 | -117 | -30.87pp | 100.00% | 98.50% | -1.50pp |
| Enter Fraud Service | 379 | 260 | -119 | -31.40pp | 100.00% | 99.24% | -0.76pp |
| Approved by Fraud Service | 368 | 246 | -122 | -33.15pp | 97.10% | 94.62% | -2.48pp |
| Call to PVS | 295 | 189 | -106 | -35.93pp | 80.16% | 76.83% | -3.33pp |
| **Successful Checkout** | 296 | 189 | -107 | -36.15pp | 100.34% | 100.00% | -0.34pp |
| **PCR Rate** | | | | | 44.98% | 38.73% | **-6.26pp** |

**Key Driver:** Call to PVS (-3.33pp)

#### Waterfall Backend

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 756 | 685 | -71 | -9.39pp | - | - | - |
| Checkout Attempt | 470 | 340 | -130 | -27.66pp | 62.17% | 49.64% | -12.53pp |
| Enter Fraud Service | 470 | 340 | -130 | -27.66pp | 100.00% | 100.00% | +0.00pp |
| Approved by Fraud Service | 451 | 320 | -131 | -29.05pp | 95.96% | 94.12% | -1.84pp |
| PVS Attempt | 451 | 320 | -131 | -29.05pp | 100.00% | 100.00% | +0.00pp |
| PVS Success | 374 | 259 | -115 | -30.75pp | 82.93% | 80.94% | -1.99pp |
| **Successful Checkout** | 450 | 320 | -130 | -28.89pp | 120.32% | 123.55% | +3.23pp |

**Key Driver:** Checkout Attempt (-12.53pp)

---

### TK

#### Waterfall GA

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 581 | 440 | -141 | -24.27pp | - | - | - |
| Select Payment Method | 304 | 239 | -65 | -21.38pp | 52.32% | 54.32% | +1.99pp |
| Click Submit Form | 277 | 216 | -61 | -22.02pp | 91.12% | 90.38% | -0.74pp |
| FE Validation Passed | 258 | 208 | -50 | -19.38pp | 93.14% | 96.30% | +3.16pp |
| Enter Fraud Service | 249 | 206 | -43 | -17.27pp | 96.51% | 99.04% | +2.53pp |
| Approved by Fraud Service | 237 | 196 | -41 | -17.30pp | 95.18% | 95.15% | -0.04pp |
| Call to PVS | 231 | 193 | -38 | -16.45pp | 97.47% | 98.47% | +1.00pp |
| **Successful Checkout** | 231 | 193 | -38 | -16.45pp | 100.00% | 100.00% | +0.00pp |
| **PCR Rate** | | | | | 39.76% | 43.86% | **+4.10pp** |

**Key Driver:** FE Validation Passed (+3.16pp)

#### Waterfall Backend

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 717 | 669 | -48 | -6.69pp | - | - | - |
| Checkout Attempt | 321 | 290 | -31 | -9.66pp | 44.77% | 43.35% | -1.42pp |
| Enter Fraud Service | 321 | 290 | -31 | -9.66pp | 100.00% | 100.00% | +0.00pp |
| Approved by Fraud Service | 301 | 268 | -33 | -10.96pp | 93.77% | 92.41% | -1.36pp |
| PVS Attempt | 301 | 267 | -34 | -11.30pp | 100.00% | 99.63% | -0.37pp |
| PVS Success | 297 | 266 | -31 | -10.44pp | 98.67% | 99.63% | +0.95pp |
| **Successful Checkout** | 299 | 267 | -32 | -10.70pp | 100.67% | 100.38% | -0.30pp |

**Key Driver:** Checkout Attempt (-1.42pp)

---

### CF

#### Waterfall GA

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 11,033 | 10,215 | -818 | -7.41pp | - | - | - |
| Select Payment Method | 5,666 | 5,374 | -292 | -5.15pp | 51.36% | 52.61% | +1.25pp |
| Click Submit Form | 5,154 | 4,872 | -282 | -5.47pp | 90.96% | 90.66% | -0.30pp |
| FE Validation Passed | 5,115 | 4,829 | -286 | -5.59pp | 99.24% | 99.12% | -0.13pp |
| Enter Fraud Service | 4,986 | 4,740 | -246 | -4.93pp | 97.48% | 98.16% | +0.68pp |
| Approved by Fraud Service | 4,746 | 4,502 | -244 | -5.14pp | 95.19% | 94.98% | -0.21pp |
| Call to PVS | 4,587 | 4,342 | -245 | -5.34pp | 96.65% | 96.45% | -0.20pp |
| **Successful Checkout** | 4,594 | 4,350 | -244 | -5.31pp | 100.15% | 100.18% | +0.03pp |
| **PCR Rate** | | | | | 41.64% | 42.58% | **+0.95pp** |

**Key Driver:** Select Payment Method (+1.25pp)

#### Waterfall Backend

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 10,687 | 11,764 | +1,077 | +10.08pp | - | - | - |
| Checkout Attempt | 5,675 | 5,545 | -130 | -2.29pp | 53.10% | 47.14% | -5.97pp |
| Enter Fraud Service | 5,641 | 5,516 | -125 | -2.22pp | 99.40% | 99.48% | +0.08pp |
| Approved by Fraud Service | 5,255 | 5,142 | -113 | -2.15pp | 93.16% | 93.22% | +0.06pp |
| PVS Attempt | 5,010 | 4,869 | -141 | -2.81pp | 95.34% | 94.69% | -0.65pp |
| PVS Success | 4,916 | 4,778 | -138 | -2.81pp | 98.12% | 98.13% | +0.01pp |
| **Successful Checkout** | 5,179 | 5,066 | -113 | -2.18pp | 105.35% | 106.03% | +0.68pp |

**Key Driver:** Checkout Attempt (-5.97pp)

---

### FJ

#### Waterfall GA

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 39,241 | 39,127 | -114 | -0.29pp | - | - | - |
| Select Payment Method | 18,885 | 19,227 | +342 | +1.81pp | 48.13% | 49.14% | +1.01pp |
| Click Submit Form | 16,973 | 17,322 | +349 | +2.06pp | 89.88% | 90.09% | +0.22pp |
| FE Validation Passed | 16,388 | 16,965 | +577 | +3.52pp | 96.55% | 97.94% | +1.39pp |
| Enter Fraud Service | 16,131 | 16,696 | +565 | +3.50pp | 98.43% | 98.41% | -0.02pp |
| Approved by Fraud Service | 15,603 | 16,151 | +548 | +3.51pp | 96.73% | 96.74% | +0.01pp |
| Call to PVS | 15,047 | 15,593 | +546 | +3.63pp | 96.44% | 96.55% | +0.11pp |
| **Successful Checkout** | 15,122 | 15,674 | +552 | +3.65pp | 100.50% | 100.52% | +0.02pp |
| **PCR Rate** | | | | | 38.54% | 40.06% | **+1.52pp** |

**Key Driver:** FE Validation Passed (+1.39pp)

#### Waterfall Backend

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 62,548 | 75,455 | +12,907 | +20.64pp | - | - | - |
| Checkout Attempt | 26,036 | 27,704 | +1,668 | +6.41pp | 41.63% | 36.72% | -4.91pp |
| Enter Fraud Service | 26,022 | 27,691 | +1,669 | +6.41pp | 99.95% | 99.95% | +0.01pp |
| Approved by Fraud Service | 24,948 | 26,569 | +1,621 | +6.50pp | 95.87% | 95.95% | +0.08pp |
| PVS Attempt | 24,878 | 26,504 | +1,626 | +6.54pp | 99.72% | 99.76% | +0.04pp |
| PVS Success | 24,231 | 25,889 | +1,658 | +6.84pp | 97.40% | 97.68% | +0.28pp |
| **Successful Checkout** | 24,303 | 25,968 | +1,665 | +6.85pp | 100.30% | 100.31% | +0.01pp |

**Key Driver:** Checkout Attempt (-4.91pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (+0.87pp) meets threshold (+0.55pp)

### Recovery Rate

| Metric | 2026-W22 | 2026-W23 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 3,050 | 2,589 | -461 |
| Error → Passed | 2,057 | 1,812 | -245 |
| **Recovery Rate** | **67.44%** | **69.99%** | **+2.55pp** |

### Error Type Distribution

| Error Type | 2026-W22 | 2026-W22 % | 2026-W23 | 2026-W23 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 2,924 | 95.9% | 2,481 | 95.8% | -0.04pp |
| terms_not_accepted | 1,238 | 40.6% | 1,044 | 40.3% | -0.27pp |
| PAYPAL_POPUP_CLOSED | 739 | 24.2% | 706 | 27.3% | +3.04pp |
| CC_TOKENISE_ERR | 176 | 5.8% | 192 | 7.4% | +1.65pp |
| PAYPAL_TOKENISE_ERR | 64 | 2.1% | 88 | 3.4% | +1.30pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 157 | 5.1% | 19 | 0.7% | -4.41pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 93 | 3.0% | 15 | 0.6% | -2.47pp |
| APPLEPAY_TOKENISE_ERR | 1 | 0.0% | 0 | 0.0% | -0.03pp |


---


---

*Report: 2026-06-09*
