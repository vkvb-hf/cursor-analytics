# PCR Investigation: HF-INTL 2026-W12

**Metric:** Payment Conversion Rate  
**Period:** 2026-W11 → 2026-W12  
**Observation:** 35.24% → 34.47% (-0.77pp)  
**Volume:** 80,204 payment visits  
**Threshold:** +0.39pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined from 35.24% to 34.47% (-0.77pp) on 80,204 payment visits in 2026-W12, driven primarily by drops in the Select Payment Method and Successful Checkout steps.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Δ > 0.39pp threshold | -0.96pp | ⚠️ |
| Click Submit Form | Within threshold | -0.13pp | ✅ |
| FE Validation Passed | Positive improvement | +0.73pp | ✅ |
| Enter Fraud Service | Within threshold | -0.20pp | ✅ |
| Approved by Fraud Service | Stable | +0.03pp | ✅ |
| Call to PVS | Stable | +0.09pp | ✅ |
| Successful Checkout | Δ > 0.39pp threshold | -0.93pp | ⚠️ |

**Key Findings:**
- **GB is the largest contributor to decline:** -1.86pp PCR drop with Select Payment Method conversion falling -2.41pp, indicating potential UX or payment option visibility issues
- **Braintree_ApplePay underperformed:** Success rate dropped -0.99pp (84.46% → 83.47%), contributing to overall decline given its high volume (12,342 attempts)
- **PVS "Pending" errors surged:** Increased from 6 to 58 cases (+5.80pp share), suggesting potential PSP processing delays
- **ES market effectively ceased operations:** Volume dropped from 257 to 1 payment visit with 0% conversion, requiring business clarification
- **FE Validation showed positive recovery:** Recovery rate improved +1.82pp (55.37% → 57.19%) with APPLEPAY_DISMISSED errors decreasing in share

**Action:** Investigate — Focus on GB market's Select Payment Method drop and Braintree_ApplePay performance; clarify ES market status with business team; monitor PVS "Pending" error trend with PSP.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 87,588 | 80,204 | -7,384 | -8.4% | - | - | - |
| Select Payment Method | 48,027 | 43,208 | -4,819 | -10.0% | 54.83% | 53.87% | -0.96pp |
| Click Submit Form | 38,598 | 34,670 | -3,928 | -10.2% | 80.37% | 80.24% | -0.13pp |
| FE Validation Passed | 35,624 | 32,251 | -3,373 | -9.5% | 92.29% | 93.02% | +0.73pp |
| Enter Fraud Service | 34,317 | 31,002 | -3,315 | -9.7% | 96.33% | 96.13% | -0.20pp |
| Approved by Fraud Service | 32,260 | 29,153 | -3,107 | -9.6% | 94.01% | 94.04% | +0.03pp |
| Call to PVS | 32,092 | 29,026 | -3,066 | -9.6% | 99.48% | 99.56% | +0.09pp |
| **Successful Checkout** | 30,867 | 27,647 | -3,220 | -10.4% | 96.18% | 95.25% | -0.93pp |
| **PCR Rate** | | | | | 35.24% | 34.47% | **-0.77pp** |

### Waterfall Backend

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 114,917 | 103,212 | -11,705 | -10.2% | - | - | - |
| Checkout Attempt | 50,688 | 45,460 | -5,228 | -10.3% | 44.11% | 44.05% | -0.06pp |
| Enter Fraud Service | 49,586 | 44,204 | -5,382 | -10.9% | 97.83% | 97.24% | -0.59pp |
| Approved by Fraud Service | 45,457 | 40,666 | -4,791 | -10.5% | 91.67% | 92.00% | +0.32pp |
| PVS Attempt | 42,932 | 38,136 | -4,796 | -11.2% | 94.45% | 93.78% | -0.67pp |
| PVS Success | 41,730 | 36,870 | -4,860 | -11.6% | 97.20% | 96.68% | -0.52pp |
| **Successful Checkout** | 43,935 | 39,131 | -4,804 | -10.9% | 105.28% | 106.13% | +0.85pp |
| **PCR Rate** | | | | | 38.23% | 37.91% | **-0.32pp** |

### Payment Method Breakdown

| Payment Method | 2026-W11 Attempt | 2026-W11 Success | 2026-W11 Rate | 2026-W12 Attempt | 2026-W12 Success | 2026-W12 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 18,708 | 16,465 | 88.01% | 16,784 | 14,775 | 88.03% | +0.02pp |
| Braintree_ApplePay | 14,070 | 11,883 | 84.46% | 12,342 | 10,302 | 83.47% | -0.99pp |
| Braintree_Paypal | 10,572 | 9,582 | 90.64% | 9,374 | 8,559 | 91.31% | +0.67pp |
| ProcessOut_ApplePay | 2,030 | 1,881 | 92.66% | 1,847 | 1,692 | 91.61% | -1.05pp |
| Adyen_IDeal | 1,950 | 1,809 | 92.77% | 1,772 | 1,673 | 94.41% | +1.64pp |
| Adyen_Sepa | 926 | 7 | 0.76% | 1,092 | 1 | 0.09% | -0.66pp |
| Adyen_Klarna | 1,086 | 1,045 | 96.22% | 1,022 | 989 | 96.77% | +0.55pp |
| Adyen_CreditCard | 1,277 | 1,244 | 97.42% | 906 | 883 | 97.46% | +0.05pp |
| Adyen_BcmcMobile | 19 | 19 | 100.00% | 279 | 257 | 92.11% | -7.89pp |
| NoPayment | 17 | 0 | 0.00% | 39 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (4 countries in HF-INTL)

| Country | Volume | PCR 2026-W11 | PCR 2026-W12 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| GB | 18,635 | 39.12% | 37.26% | -1.86pp | 1 | 7 |
| FR | 20,406 | 29.26% | 28.38% | -0.88pp | 2 | 10 |
| LU | 70 | 31.65% | 47.14% | +15.49pp | 11 | 2 |
| ES | 1 | 32.68% | 0.00% | -32.68pp | 15 | 1 |

---

### FR

#### Waterfall GA

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 23,301 | 20,406 | -2,895 | -12.42pp | - | - | - |
| Select Payment Method | 10,892 | 9,344 | -1,548 | -14.21pp | 46.74% | 45.79% | -0.95pp |
| Click Submit Form | 8,614 | 7,330 | -1,284 | -14.91pp | 79.09% | 78.45% | -0.64pp |
| FE Validation Passed | 7,949 | 6,846 | -1,103 | -13.88pp | 92.28% | 93.40% | +1.12pp |
| Enter Fraud Service | 7,647 | 6,575 | -1,072 | -14.02pp | 96.20% | 96.04% | -0.16pp |
| Approved by Fraud Service | 7,037 | 6,006 | -1,031 | -14.65pp | 92.02% | 91.35% | -0.68pp |
| Call to PVS | 7,022 | 6,002 | -1,020 | -14.53pp | 99.79% | 99.93% | +0.15pp |
| **Successful Checkout** | 6,818 | 5,791 | -1,027 | -15.06pp | 97.09% | 96.48% | -0.61pp |
| **PCR Rate** | | | | | 29.26% | 28.38% | **-0.88pp** |

**Key Driver:** FE Validation Passed (+1.12pp)

#### Waterfall Backend

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 30,939 | 27,180 | -3,759 | -12.15pp | - | - | - |
| Checkout Attempt | 11,559 | 9,998 | -1,561 | -13.50pp | 37.36% | 36.78% | -0.58pp |
| Enter Fraud Service | 11,545 | 9,980 | -1,565 | -13.56pp | 99.88% | 99.82% | -0.06pp |
| Approved by Fraud Service | 10,270 | 8,852 | -1,418 | -13.81pp | 88.96% | 88.70% | -0.26pp |
| PVS Attempt | 10,262 | 8,848 | -1,414 | -13.78pp | 99.92% | 99.95% | +0.03pp |
| PVS Success | 10,082 | 8,652 | -1,430 | -14.18pp | 98.25% | 97.78% | -0.46pp |
| **Successful Checkout** | 10,133 | 8,690 | -1,443 | -14.24pp | 100.51% | 100.44% | -0.07pp |

**Key Driver:** Checkout Attempt (-0.58pp)

---

### LU

#### Waterfall GA

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 79 | 70 | -9 | -11.39pp | - | - | - |
| Select Payment Method | 45 | 45 | 0 | +0.00pp | 56.96% | 64.29% | +7.32pp |
| Click Submit Form | 36 | 38 | +2 | +5.56pp | 80.00% | 84.44% | +4.44pp |
| FE Validation Passed | 35 | 34 | -1 | -2.86pp | 97.22% | 89.47% | -7.75pp |
| Enter Fraud Service | 32 | 34 | +2 | +6.25pp | 91.43% | 100.00% | +8.57pp |
| Approved by Fraud Service | 31 | 34 | +3 | +9.68pp | 96.88% | 100.00% | +3.12pp |
| Call to PVS | 27 | 33 | +6 | +22.22pp | 87.10% | 97.06% | +9.96pp |
| **Successful Checkout** | 25 | 33 | +8 | +32.00pp | 92.59% | 100.00% | +7.41pp |
| **PCR Rate** | | | | | 31.65% | 47.14% | **+15.50pp** |

**Key Driver:** Call to PVS (+9.96pp)

#### Waterfall Backend

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 296 | 269 | -27 | -9.12pp | - | - | - |
| Checkout Attempt | 103 | 74 | -29 | -28.16pp | 34.80% | 27.51% | -7.29pp |
| Enter Fraud Service | 75 | 55 | -20 | -26.67pp | 72.82% | 74.32% | +1.51pp |
| Approved by Fraud Service | 73 | 55 | -18 | -24.66pp | 97.33% | 100.00% | +2.67pp |
| PVS Attempt | 69 | 53 | -16 | -23.19pp | 94.52% | 96.36% | +1.84pp |
| PVS Success | 66 | 53 | -13 | -19.70pp | 95.65% | 100.00% | +4.35pp |
| **Successful Checkout** | 93 | 71 | -22 | -23.66pp | 140.91% | 133.96% | -6.95pp |

**Key Driver:** Checkout Attempt (-7.29pp)

---

### GB

#### Waterfall GA

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 19,814 | 18,635 | -1,179 | -5.95pp | - | - | - |
| Select Payment Method | 11,782 | 10,631 | -1,151 | -9.77pp | 59.46% | 57.05% | -2.41pp |
| Click Submit Form | 9,617 | 8,583 | -1,034 | -10.75pp | 81.62% | 80.74% | -0.89pp |
| FE Validation Passed | 8,686 | 7,772 | -914 | -10.52pp | 90.32% | 90.55% | +0.23pp |
| Enter Fraud Service | 8,486 | 7,562 | -924 | -10.89pp | 97.70% | 97.30% | -0.40pp |
| Approved by Fraud Service | 7,955 | 7,113 | -842 | -10.58pp | 93.74% | 94.06% | +0.32pp |
| Call to PVS | 7,897 | 7,079 | -818 | -10.36pp | 99.27% | 99.52% | +0.25pp |
| **Successful Checkout** | 7,752 | 6,943 | -809 | -10.44pp | 98.16% | 98.08% | -0.09pp |
| **PCR Rate** | | | | | 39.12% | 37.26% | **-1.87pp** |

**Key Driver:** Select Payment Method (-2.41pp)

#### Waterfall Backend

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 25,018 | 22,638 | -2,380 | -9.51pp | - | - | - |
| Checkout Attempt | 12,055 | 10,604 | -1,451 | -12.04pp | 48.19% | 46.84% | -1.34pp |
| Enter Fraud Service | 12,035 | 10,558 | -1,477 | -12.27pp | 99.83% | 99.57% | -0.27pp |
| Approved by Fraud Service | 10,945 | 9,718 | -1,227 | -11.21pp | 90.94% | 92.04% | +1.10pp |
| PVS Attempt | 9,421 | 8,285 | -1,136 | -12.06pp | 86.08% | 85.25% | -0.82pp |
| PVS Success | 9,231 | 8,134 | -1,097 | -11.88pp | 97.98% | 98.18% | +0.19pp |
| **Successful Checkout** | 10,774 | 9,583 | -1,191 | -11.05pp | 116.72% | 117.81% | +1.10pp |

**Key Driver:** Checkout Attempt (-1.34pp)

---

### ES

#### Waterfall GA

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 257 | 1 | -256 | -99.61pp | - | - | - |
| Select Payment Method | 127 | 0 | -127 | -100.00pp | 49.42% | 0.00% | -49.42pp |
| Click Submit Form | 106 | 0 | -106 | -100.00pp | 83.46% | 0.00% | -83.46pp |
| FE Validation Passed | 98 | 0 | -98 | -100.00pp | 92.45% | 0.00% | -92.45pp |
| Enter Fraud Service | 93 | 0 | -93 | -100.00pp | 94.90% | 0.00% | -94.90pp |
| Approved by Fraud Service | 85 | 0 | -85 | -100.00pp | 91.40% | 0.00% | -91.40pp |
| Call to PVS | 85 | 0 | -85 | -100.00pp | 100.00% | 0.00% | -100.00pp |
| **Successful Checkout** | 84 | 0 | -84 | -100.00pp | 98.82% | 0.00% | -98.82pp |
| **PCR Rate** | | | | | 32.68% | 0.00% | **-32.68pp** |

**Key Driver:** Call to PVS (-100.00pp)

#### Waterfall Backend

| Funnel Step | 2026-W11 | 2026-W12 | Δ Count | Δ % | 2026-W11 Conv | 2026-W12 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 415 | 0 | -415 | -100.00pp | - | - | - |
| Checkout Attempt | 162 | 0 | -162 | -100.00pp | 39.04% | 0.00% | -39.04pp |
| Enter Fraud Service | 161 | 0 | -161 | -100.00pp | 99.38% | 0.00% | -99.38pp |
| Approved by Fraud Service | 140 | 0 | -140 | -100.00pp | 86.96% | 0.00% | -86.96pp |
| PVS Attempt | 141 | 0 | -141 | -100.00pp | 100.71% | 0.00% | -100.71pp |
| PVS Success | 140 | 0 | -140 | -100.00pp | 99.29% | 0.00% | -99.29pp |
| **Successful Checkout** | 139 | 0 | -139 | -100.00pp | 99.29% | 0.00% | -99.29pp |

**Key Driver:** PVS Attempt (-100.71pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (+0.73pp) meets threshold (+0.39pp)

### Recovery Rate

| Metric | 2026-W11 | 2026-W12 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 7,347 | 6,368 | -979 |
| Error → Passed | 4,068 | 3,642 | -426 |
| **Recovery Rate** | **55.37%** | **57.19%** | **+1.82pp** |

### Error Type Distribution

| Error Type | 2026-W11 | 2026-W11 % | 2026-W12 | 2026-W12 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 5,544 | 75.5% | 4,679 | 73.5% | -1.98pp |
| PAYPAL_POPUP_CLOSED | 1,547 | 21.1% | 1,447 | 22.7% | +1.67pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 339 | 4.6% | 306 | 4.8% | +0.19pp |
| CC_TOKENISE_ERR | 132 | 1.8% | 140 | 2.2% | +0.40pp |
| PAYPAL_TOKENISE_ERR | 174 | 2.4% | 130 | 2.0% | -0.33pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 118 | 1.6% | 122 | 1.9% | +0.31pp |
| APPLEPAY_MERCHANT_VALIDATION_ERR | 3 | 0.0% | 4 | 0.1% | +0.02pp |
| APPLEPAY_TOKENISE_ERR | 2 | 0.0% | 3 | 0.0% | +0.02pp |
| EXPRESS_CHECKOUT_APPLEPAY_TOKENISE_ERR | 1 | 0.0% | 0 | 0.0% | -0.01pp |


---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (-0.93pp) meets threshold (+0.39pp)

| Decline Reason | 2026-W11 | 2026-W11 % | 2026-W12 | 2026-W12 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| RedirectShopper | 231 | 28.8% | 223 | 25.2% | -8 | -3.63pp |
| Failed Verification: Insufficient Funds | 194 | 24.2% | 215 | 24.3% | +21 | +0.08pp |
| Failed Verification: Declined | 113 | 14.1% | 110 | 12.4% | -3 | -1.67pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 95 | 11.8% | 107 | 12.1% | +12 | +0.23pp |
| Cancelled: Cancelled | 96 | 12.0% | 85 | 9.6% | -11 | -2.38pp |
| Pending | 6 | 0.7% | 58 | 6.5% | +52 | +5.80pp |
| Refused: Refused | 23 | 2.9% | 31 | 3.5% | +8 | +0.63pp |
| Failed Verification: Security | 12 | 1.5% | 22 | 2.5% | +10 | +0.99pp |
| CHARGE_STATE_FAILURE: The 3DS check has expired | 32 | 4.0% | 18 | 2.0% | -14 | -1.96pp |
| Refused | 0 | 0.0% | 17 | 1.9% | +17 | +1.92pp |
| **Total PVS Failures** | **802** | **100%** | **886** | **100%** | **+84** | - |

---


---

*Report: 2026-04-10*
