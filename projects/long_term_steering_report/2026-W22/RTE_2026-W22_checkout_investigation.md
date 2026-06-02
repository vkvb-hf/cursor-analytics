# PCR Investigation: RTE 2026-W22

**Metric:** Payment Conversion Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 38.53% → 38.72% (+0.20pp)  
**Volume:** 59,729 payment visits  
**Threshold:** +0.10pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate improved slightly from 38.53% to 38.72% (+0.20pp) on 59,729 payment visits, exceeding the +0.10pp threshold.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Volume & Rate | +0.55pp | ✅ |
| Click Submit Form | Conversion | -0.35pp | ⚠️ |
| FE Validation Passed | Conversion | -0.20pp | ⚠️ |
| Enter Fraud Service | Conversion | -0.02pp | ✅ |
| Approved by Fraud Service | Conversion | +0.27pp | ✅ |
| Call to PVS | Conversion | +0.00pp | ✅ |
| Successful Checkout | Conversion | -0.29pp | ⚠️ |

**Key Findings:**
- **Fraud approval improvement drove gains:** Approved by Fraud Service conversion increased +0.27pp globally, with TZ showing exceptional improvement (+6.51pp), contributing most significantly to the overall PCR lift
- **Payment method selection improved:** Select Payment Method conversion rose +0.55pp (48.64% → 49.19%), indicating better top-of-funnel engagement
- **PVS Success declined:** Successful Checkout step showed -0.29pp conversion decline, with "Cancelled: Cancelled" errors increasing +4.93pp share and "Blocked Verification" up +2.33pp share
- **FE Validation slight degradation:** FE Validation Passed dropped -0.20pp with recovery rate declining from 67.68% to 67.45%; APPLEPAY_DISMISSED errors increased to 95.8% share (+1.06pp)
- **Backend data anomaly:** Backend waterfall shows 0 values for 2026-W22 Successful Checkout and Payment Method Listed, suggesting potential data collection issues requiring investigation

**Action:** **Monitor** - The positive PCR movement is within expected variance. Investigate backend data integrity issues showing zero values in 2026-W22. Monitor PVS "Cancelled" and "Blocked Verification" error increases for potential emerging patterns.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 59,713 | 59,729 | 16 | 0.0% | - | - | - |
| Select Payment Method | 29,044 | 29,382 | 338 | 1.2% | 48.64% | 49.19% | +0.55pp |
| Click Submit Form | 26,126 | 26,328 | 202 | 0.8% | 89.95% | 89.61% | -0.35pp |
| FE Validation Passed | 25,481 | 25,625 | 144 | 0.6% | 97.53% | 97.33% | -0.20pp |
| Enter Fraud Service | 24,982 | 25,119 | 137 | 0.5% | 98.04% | 98.03% | -0.02pp |
| Approved by Fraud Service | 23,917 | 24,117 | 200 | 0.8% | 95.74% | 96.01% | +0.27pp |
| Call to PVS | 23,879 | 24,079 | 200 | 0.8% | 99.84% | 99.84% | +0.00pp |
| **Successful Checkout** | 23,005 | 23,129 | 124 | 0.5% | 96.34% | 96.05% | -0.29pp |
| **PCR Rate** | | | | | 38.53% | 38.72% | **+0.20pp** |

### Waterfall Backend

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 100,611 | 0 | -100,611 | -100.0% | - | - | - |
| Checkout Attempt | 38,141 | 33,715 | -4,426 | -11.6% | 37.91% | 0.00% | -37.91pp |
| Enter Fraud Service | 38,097 | 33,668 | -4,429 | -11.6% | 99.88% | 99.86% | -0.02pp |
| Approved by Fraud Service | 36,078 | 31,944 | -4,134 | -11.5% | 94.70% | 94.88% | +0.18pp |
| PVS Attempt | 35,603 | 31,528 | -4,075 | -11.4% | 98.68% | 98.70% | +0.01pp |
| PVS Success | 34,624 | 30,590 | -4,034 | -11.7% | 97.25% | 97.02% | -0.23pp |
| **Successful Checkout** | 34,248 | 0 | -34,248 | -100.0% | 98.91% | 0.00% | -98.91pp |
| **PCR Rate** | | | | | 34.04% | 0.00% | **-34.04pp** |

### Payment Method Breakdown

| Payment Method | 2026-W21 Attempt | 2026-W21 Success | 2026-W21 Rate | 2026-W22 Attempt | 2026-W22 Success | 2026-W22 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 15,302 | 14,169 | 92.60% | 13,454 | 0 | 0.00% | -92.60pp |
| Braintree_ApplePay | 9,142 | 7,599 | 83.12% | 8,158 | 0 | 0.00% | -83.12pp |
| Adyen_CreditCard | 8,279 | 7,482 | 90.37% | 7,365 | 0 | 0.00% | -90.37pp |
| Braintree_Paypal | 4,342 | 4,042 | 93.09% | 3,773 | 0 | 0.00% | -93.09pp |
| Adyen_IDeal | 474 | 435 | 91.77% | 422 | 0 | 0.00% | -91.77pp |
| Adyen_Klarna | 270 | 240 | 88.89% | 262 | 0 | 0.00% | -88.89pp |
| Adyen_BcmcMobile | 213 | 195 | 91.55% | 200 | 0 | 0.00% | -91.55pp |
| Braintree_CreditCard | 115 | 86 | 74.78% | 80 | 0 | 0.00% | -74.78pp |
| paypal | 1 | 0 | 0.00% | 1 | 0 | 0.00% | +0.00pp |
| mc | 2 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (3 countries in RTE)

| Country | Volume | PCR 2026-W21 | PCR 2026-W22 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| TZ | 957 | 25.31% | 28.11% | +2.80pp | 1 | 1 |
| YE | 5,642 | 37.01% | 37.38% | +0.37pp | 2 | 6 |
| TO | 585 | 34.95% | 37.61% | +2.66pp | 4 | 2 |

---

### TZ

#### Waterfall GA

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 960 | 957 | -3 | -0.31pp | - | - | - |
| Select Payment Method | 468 | 504 | +36 | +7.69pp | 48.75% | 52.66% | +3.91pp |
| Click Submit Form | 331 | 331 | 0 | +0.00pp | 70.73% | 65.67% | -5.05pp |
| FE Validation Passed | 300 | 306 | +6 | +2.00pp | 90.63% | 92.45% | +1.81pp |
| Enter Fraud Service | 280 | 287 | +7 | +2.50pp | 93.33% | 93.79% | +0.46pp |
| Approved by Fraud Service | 253 | 278 | +25 | +9.88pp | 90.36% | 96.86% | +6.51pp |
| Call to PVS | 253 | 278 | +25 | +9.88pp | 100.00% | 100.00% | +0.00pp |
| **Successful Checkout** | 243 | 269 | +26 | +10.70pp | 96.05% | 96.76% | +0.72pp |
| **PCR Rate** | | | | | 25.31% | 28.11% | **+2.80pp** |

**Key Driver:** Approved by Fraud Service (+6.51pp)

#### Waterfall Backend

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 1,407 | 0 | -1,407 | -100.00pp | - | - | - |
| Checkout Attempt | 422 | 374 | -48 | -11.37pp | 29.99% | 0.00% | -29.99pp |
| Enter Fraud Service | 422 | 373 | -49 | -11.61pp | 100.00% | 99.73% | -0.27pp |
| Approved by Fraud Service | 371 | 352 | -19 | -5.12pp | 87.91% | 94.37% | +6.46pp |
| PVS Attempt | 371 | 351 | -20 | -5.39pp | 100.00% | 99.72% | -0.28pp |
| PVS Success | 358 | 343 | -15 | -4.19pp | 96.50% | 97.72% | +1.22pp |
| **Successful Checkout** | 360 | 343 | -17 | -4.72pp | 100.56% | 100.00% | -0.56pp |

**Key Driver:** Checkout Attempt (-29.99pp)

---

### TO

#### Waterfall GA

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 658 | 585 | -73 | -11.09pp | - | - | - |
| Select Payment Method | 369 | 336 | -33 | -8.94pp | 56.08% | 57.44% | +1.36pp |
| Click Submit Form | 317 | 299 | -18 | -5.68pp | 85.91% | 88.99% | +3.08pp |
| FE Validation Passed | 314 | 289 | -25 | -7.96pp | 99.05% | 96.66% | -2.40pp |
| Enter Fraud Service | 307 | 287 | -20 | -6.51pp | 97.77% | 99.31% | +1.54pp |
| Approved by Fraud Service | 283 | 267 | -16 | -5.65pp | 92.18% | 93.03% | +0.85pp |
| Call to PVS | 285 | 269 | -16 | -5.61pp | 100.71% | 100.75% | +0.04pp |
| **Successful Checkout** | 230 | 220 | -10 | -4.35pp | 80.70% | 81.78% | +1.08pp |
| **PCR Rate** | | | | | 34.95% | 37.61% | **+2.65pp** |

**Key Driver:** Click Submit Form (+3.08pp)

#### Waterfall Backend

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 999 | 0 | -999 | -100.00pp | - | - | - |
| Checkout Attempt | 410 | 358 | -52 | -12.68pp | 41.04% | 0.00% | -41.04pp |
| Enter Fraud Service | 410 | 357 | -53 | -12.93pp | 100.00% | 99.72% | -0.28pp |
| Approved by Fraud Service | 374 | 321 | -53 | -14.17pp | 91.22% | 89.92% | -1.30pp |
| PVS Attempt | 374 | 320 | -54 | -14.44pp | 100.00% | 99.69% | -0.31pp |
| PVS Success | 324 | 282 | -42 | -12.96pp | 86.63% | 88.12% | +1.49pp |
| **Successful Checkout** | 374 | 314 | -60 | -16.04pp | 115.43% | 111.35% | -4.08pp |

**Key Driver:** Checkout Attempt (-41.04pp)

---

### YE

#### Waterfall GA

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 5,744 | 5,642 | -102 | -1.78pp | - | - | - |
| Select Payment Method | 2,777 | 2,759 | -18 | -0.65pp | 48.35% | 48.90% | +0.55pp |
| Click Submit Form | 2,480 | 2,459 | -21 | -0.85pp | 89.31% | 89.13% | -0.18pp |
| FE Validation Passed | 2,451 | 2,433 | -18 | -0.73pp | 98.83% | 98.94% | +0.11pp |
| Enter Fraud Service | 2,341 | 2,343 | +2 | +0.09pp | 95.51% | 96.30% | +0.79pp |
| Approved by Fraud Service | 2,212 | 2,195 | -17 | -0.77pp | 94.49% | 93.68% | -0.81pp |
| Call to PVS | 2,209 | 2,192 | -17 | -0.77pp | 99.86% | 99.86% | -0.00pp |
| **Successful Checkout** | 2,126 | 2,109 | -17 | -0.80pp | 96.24% | 96.21% | -0.03pp |
| **PCR Rate** | | | | | 37.01% | 37.38% | **+0.37pp** |

**Key Driver:** Approved by Fraud Service (-0.81pp)

#### Waterfall Backend

| Funnel Step | 2026-W21 | 2026-W22 | Δ Count | Δ % | 2026-W21 Conv | 2026-W22 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 8,406 | 0 | -8,406 | -100.00pp | - | - | - |
| Checkout Attempt | 3,480 | 3,176 | -304 | -8.74pp | 41.40% | 0.00% | -41.40pp |
| Enter Fraud Service | 3,479 | 3,175 | -304 | -8.74pp | 99.97% | 99.97% | -0.00pp |
| Approved by Fraud Service | 3,234 | 2,926 | -308 | -9.52pp | 92.96% | 92.16% | -0.80pp |
| PVS Attempt | 3,092 | 2,785 | -307 | -9.93pp | 95.61% | 95.18% | -0.43pp |
| PVS Success | 3,005 | 2,722 | -283 | -9.42pp | 97.19% | 97.74% | +0.55pp |
| **Successful Checkout** | 3,164 | 2,877 | -287 | -9.07pp | 105.29% | 105.69% | +0.40pp |

**Key Driver:** Checkout Attempt (-41.40pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (-0.20pp) meets threshold (+0.10pp)

### Recovery Rate

| Metric | 2026-W21 | 2026-W22 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 2,946 | 3,051 | 105 |
| Error → Passed | 1,994 | 2,058 | 64 |
| **Recovery Rate** | **67.68%** | **67.45%** | **-0.23pp** |

### Error Type Distribution

| Error Type | 2026-W21 | 2026-W21 % | 2026-W22 | 2026-W22 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 2,792 | 94.8% | 2,924 | 95.8% | +1.06pp |
| terms_not_accepted | 1,325 | 45.0% | 1,238 | 40.6% | -4.40pp |
| PAYPAL_POPUP_CLOSED | 694 | 23.6% | 739 | 24.2% | +0.66pp |
| CC_TOKENISE_ERR | 184 | 6.2% | 176 | 5.8% | -0.48pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 153 | 5.2% | 157 | 5.1% | -0.05pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 79 | 2.7% | 93 | 3.0% | +0.37pp |
| PAYPAL_TOKENISE_ERR | 78 | 2.6% | 64 | 2.1% | -0.55pp |
| APPLEPAY_TOKENISE_ERR | 1 | 0.0% | 1 | 0.0% | -0.00pp |


---

## Fraud Analysis

**Include reason:** Approved Δ (+0.27pp) meets threshold (+0.10pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W21 | 2026-W21 % | 2026-W22 | 2026-W22 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 38,141 | - | 33,715 | - | -4,426 | -11.6% |
| Enter Fraud Service | 38,097 | - | 33,668 | - | -4,429 | -11.6% |
| **Gap (Skipped)** | **44** | **0.12%** | **47** | **0.14%** | **3** | **+0.02pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W21 Gap | 2026-W21 % | 2026-W22 Gap | 2026-W22 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Adyen_CreditCard | 29 | 65.9% | 31 | 66.0% | +2 | +0.05pp |
| Braintree_ApplePay | 5 | 11.4% | 7 | 14.9% | +2 | +3.53pp |
| ProcessOut_CreditCard | 7 | 15.9% | 6 | 12.8% | -1 | -3.14pp |
| Braintree_Paypal | 2 | 4.5% | 2 | 4.3% | 0 | -0.29pp |
| Adyen_BcmcMobile | 0 | 0.0% | 1 | 2.1% | +1 | +2.13pp |
| Braintree_CreditCard | 1 | 2.3% | 0 | 0.0% | -1 | -2.27pp |
| **Total** | **44** | **100%** | **47** | **100%** | **3** | - |

*% of Gap = Payment Method Gap / Total Gap*

---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (-0.29pp) meets threshold (+0.10pp)

| Decline Reason | 2026-W21 | 2026-W21 % | 2026-W22 | 2026-W22 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Failed Verification: Insufficient Funds | 123 | 21.1% | 113 | 18.6% | -10 | -2.51pp |
| Blocked Verification: Payment method is blocked due to business reasons | 89 | 15.3% | 107 | 17.6% | +18 | +2.33pp |
| RedirectShopper | 115 | 19.7% | 98 | 16.1% | -17 | -3.61pp |
| Cancelled: Cancelled | 24 | 4.1% | 55 | 9.0% | +31 | +4.93pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 50 | 8.6% | 48 | 7.9% | -2 | -0.68pp |
| Failed Verification: Card Issuer Declined CVV | 52 | 8.9% | 42 | 6.9% | -10 | -2.01pp |
| Failed Verification: Processor Declined - Fraud Suspected | 29 | 5.0% | 40 | 6.6% | +11 | +1.60pp |
| Failed Verification: Issuer or Cardholder has put a restriction on the card | 34 | 5.8% | 37 | 6.1% | +3 | +0.25pp |
| Failed Verification: Processor Declined | 31 | 5.3% | 35 | 5.8% | +4 | +0.44pp |
| Failed Verification: Declined - Call Issuer | 36 | 6.2% | 33 | 5.4% | -3 | -0.75pp |
| **Total PVS Failures** | **583** | **100%** | **608** | **100%** | **+25** | - |

---


---

*Report: 2026-06-02*
