# PCR Investigation: RTE 2026-W21

**Metric:** Payment Conversion Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 39.29% → 38.53% (-0.76pp)  
**Volume:** 59,717 payment visits  
**Threshold:** +0.38pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined from 39.29% to 38.53% (-0.76pp) on 59,717 payment visits in 2026-W21, driven primarily by upstream funnel drop-off at Select Payment Method and degraded Fraud Service approval rates.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Visits → Select | -1.40pp | ⚠️ |
| Click Submit Form | Select → Submit | +0.16pp | ✅ |
| FE Validation Passed | Submit → Validated | -0.41pp | ⚠️ |
| Enter Fraud Service | Validated → Fraud | +0.11pp | ✅ |
| Approved by Fraud Service | Fraud → Approved | -0.40pp | ⚠️ |
| Call to PVS | Approved → PVS | +0.77pp | ✅ |
| Successful Checkout | PVS → Success | +0.62pp | ✅ |

**Key Findings:**
- **Select Payment Method** is the largest conversion drop (-1.40pp), with FJ showing -1.98pp and TT showing -6.03pp at this step
- **Braintree_ApplePay** success rate collapsed from 92.03% to 83.12% (-8.91pp), representing the most significant payment method degradation
- **FE Validation errors** show APPLEPAY_DISMISSED increased from 84.2% to 94.8% of errors (+10.55pp share), with new Apple Pay address validation errors emerging (APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR +5.07pp, APPLEPAY_ADDRESS_EMPTY_NAME_ERR +2.62pp)
- **Fraud Service approval** declined -0.40pp overall, with TT experiencing severe degradation (-5.41pp GA, -4.86pp Backend)
- **Recovery rate** for FE validation errors dropped from 71.79% to 67.71% (-4.09pp), indicating customers are less able to overcome validation issues

**Action:** **Investigate** - Immediate investigation required into Braintree_ApplePay integration issues, focusing on the surge in Apple Pay dismissals and new address validation errors. Coordinate with Braintree technical team to identify root cause.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 63,829 | 59,717 | -4,112 | -6.4% | - | - | - |
| Select Payment Method | 31,940 | 29,048 | -2,892 | -9.1% | 50.04% | 48.64% | -1.40pp |
| Click Submit Form | 28,678 | 26,128 | -2,550 | -8.9% | 89.79% | 89.95% | +0.16pp |
| FE Validation Passed | 28,089 | 25,485 | -2,604 | -9.3% | 97.95% | 97.54% | -0.41pp |
| Enter Fraud Service | 27,508 | 24,985 | -2,523 | -9.2% | 97.93% | 98.04% | +0.11pp |
| Approved by Fraud Service | 26,436 | 23,911 | -2,525 | -9.6% | 96.10% | 95.70% | -0.40pp |
| Call to PVS | 26,200 | 23,881 | -2,319 | -8.9% | 99.11% | 99.87% | +0.77pp |
| **Successful Checkout** | 25,079 | 23,007 | -2,072 | -8.3% | 95.72% | 96.34% | +0.62pp |
| **PCR Rate** | | | | | 39.29% | 38.53% | **-0.76pp** |

### Waterfall Backend

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 109,196 | 100,611 | -8,585 | -7.9% | - | - | - |
| Checkout Attempt | 41,865 | 38,141 | -3,724 | -8.9% | 38.34% | 37.91% | -0.43pp |
| Enter Fraud Service | 41,795 | 38,097 | -3,698 | -8.8% | 99.83% | 99.88% | +0.05pp |
| Approved by Fraud Service | 39,708 | 36,078 | -3,630 | -9.1% | 95.01% | 94.70% | -0.31pp |
| PVS Attempt | 38,879 | 35,603 | -3,276 | -8.4% | 97.91% | 98.68% | +0.77pp |
| PVS Success | 37,515 | 34,623 | -2,892 | -7.7% | 96.49% | 97.25% | +0.76pp |
| **Successful Checkout** | 38,272 | 34,248 | -4,024 | -10.5% | 102.02% | 98.92% | -3.10pp |
| **PCR Rate** | | | | | 35.05% | 34.04% | **-1.01pp** |

### Payment Method Breakdown

| Payment Method | 2026-W20 Attempt | 2026-W20 Success | 2026-W20 Rate | 2026-W21 Attempt | 2026-W21 Success | 2026-W21 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 16,871 | 15,584 | 92.37% | 15,302 | 14,169 | 92.60% | +0.22pp |
| Braintree_ApplePay | 9,776 | 8,997 | 92.03% | 9,142 | 7,599 | 83.12% | -8.91pp |
| Adyen_CreditCard | 9,102 | 8,057 | 88.52% | 8,279 | 7,482 | 90.37% | +1.85pp |
| Braintree_Paypal | 4,945 | 4,547 | 91.95% | 4,342 | 4,042 | 93.09% | +1.14pp |
| Adyen_IDeal | 771 | 721 | 93.51% | 474 | 435 | 91.77% | -1.74pp |
| Adyen_Klarna | 287 | 271 | 94.43% | 270 | 240 | 88.89% | -5.54pp |
| Adyen_BcmcMobile | 3 | 1 | 33.33% | 213 | 195 | 91.55% | +58.22pp |
| Braintree_CreditCard | 105 | 90 | 85.71% | 115 | 86 | 74.78% | -10.93pp |
| mc | 1 | 0 | 0.00% | 2 | 0 | 0.00% | +0.00pp |
| paypal | 0 | 0 | 0.00% | 1 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (4 countries in RTE)

| Country | Volume | PCR 2026-W20 | PCR 2026-W21 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| FJ | 39,125 | 40.43% | 38.54% | -1.89pp | 1 | 4 |
| YE | 5,743 | 34.45% | 37.02% | +2.57pp | 2 | 3 |
| TT | 1,113 | 31.74% | 25.97% | -5.77pp | 3 | 1 |
| TO | 658 | 29.18% | 34.95% | +5.77pp | 4 | 2 |

---

### TT

#### Waterfall GA

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 1,591 | 1,113 | -478 | -30.04pp | - | - | - |
| Select Payment Method | 855 | 531 | -324 | -37.89pp | 53.74% | 47.71% | -6.03pp |
| Click Submit Form | 781 | 474 | -307 | -39.31pp | 91.35% | 89.27% | -2.08pp |
| FE Validation Passed | 786 | 482 | -304 | -38.68pp | 100.64% | 101.69% | +1.05pp |
| Enter Fraud Service | 782 | 479 | -303 | -38.75pp | 99.49% | 99.38% | -0.11pp |
| Approved by Fraud Service | 759 | 439 | -320 | -42.16pp | 97.06% | 91.65% | -5.41pp |
| Call to PVS | 748 | 438 | -310 | -41.44pp | 98.55% | 99.77% | +1.22pp |
| **Successful Checkout** | 505 | 289 | -216 | -42.77pp | 67.51% | 65.98% | -1.53pp |
| **PCR Rate** | | | | | 31.74% | 25.97% | **-5.78pp** |

**Key Driver:** Select Payment Method (-6.03pp)

#### Waterfall Backend

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 2,098 | 1,475 | -623 | -29.69pp | - | - | - |
| Checkout Attempt | 1,018 | 643 | -375 | -36.84pp | 48.52% | 43.59% | -4.93pp |
| Enter Fraud Service | 1,017 | 643 | -374 | -36.77pp | 99.90% | 100.00% | +0.10pp |
| Approved by Fraud Service | 962 | 577 | -385 | -40.02pp | 94.59% | 89.74% | -4.86pp |
| PVS Attempt | 949 | 578 | -371 | -39.09pp | 98.65% | 100.17% | +1.52pp |
| PVS Success | 762 | 467 | -295 | -38.71pp | 80.30% | 80.80% | +0.50pp |
| **Successful Checkout** | 944 | 576 | -368 | -38.98pp | 123.88% | 123.34% | -0.54pp |

**Key Driver:** Checkout Attempt (-4.93pp)

---

### TO

#### Waterfall GA

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 970 | 658 | -312 | -32.16pp | - | - | - |
| Select Payment Method | 450 | 369 | -81 | -18.00pp | 46.39% | 56.08% | +9.69pp |
| Click Submit Form | 363 | 317 | -46 | -12.67pp | 80.67% | 85.91% | +5.24pp |
| FE Validation Passed | 344 | 314 | -30 | -8.72pp | 94.77% | 99.05% | +4.29pp |
| Enter Fraud Service | 324 | 307 | -17 | -5.25pp | 94.19% | 97.77% | +3.58pp |
| Approved by Fraud Service | 311 | 283 | -28 | -9.00pp | 95.99% | 92.18% | -3.81pp |
| Call to PVS | 308 | 285 | -23 | -7.47pp | 99.04% | 100.71% | +1.67pp |
| **Successful Checkout** | 283 | 230 | -53 | -18.73pp | 91.88% | 80.70% | -11.18pp |
| **PCR Rate** | | | | | 29.18% | 34.95% | **+5.78pp** |

**Key Driver:** Successful Checkout (-11.18pp)

#### Waterfall Backend

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 1,370 | 999 | -371 | -27.08pp | - | - | - |
| Checkout Attempt | 442 | 410 | -32 | -7.24pp | 32.26% | 41.04% | +8.78pp |
| Enter Fraud Service | 442 | 410 | -32 | -7.24pp | 100.00% | 100.00% | +0.00pp |
| Approved by Fraud Service | 404 | 374 | -30 | -7.43pp | 91.40% | 91.22% | -0.18pp |
| PVS Attempt | 403 | 374 | -29 | -7.20pp | 99.75% | 100.00% | +0.25pp |
| PVS Success | 374 | 324 | -50 | -13.37pp | 92.80% | 86.63% | -6.17pp |
| **Successful Checkout** | 398 | 374 | -24 | -6.03pp | 106.42% | 115.43% | +9.01pp |

**Key Driver:** Successful Checkout (+9.01pp)

---

### YE

#### Waterfall GA

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 6,352 | 5,743 | -609 | -9.59pp | - | - | - |
| Select Payment Method | 2,947 | 2,777 | -170 | -5.77pp | 46.39% | 48.35% | +1.96pp |
| Click Submit Form | 2,625 | 2,480 | -145 | -5.52pp | 89.07% | 89.31% | +0.23pp |
| FE Validation Passed | 2,602 | 2,451 | -151 | -5.80pp | 99.12% | 98.83% | -0.29pp |
| Enter Fraud Service | 2,477 | 2,341 | -136 | -5.49pp | 95.20% | 95.51% | +0.32pp |
| Approved by Fraud Service | 2,336 | 2,211 | -125 | -5.35pp | 94.31% | 94.45% | +0.14pp |
| Call to PVS | 2,286 | 2,209 | -77 | -3.37pp | 97.86% | 99.91% | +2.05pp |
| **Successful Checkout** | 2,188 | 2,126 | -62 | -2.83pp | 95.71% | 96.24% | +0.53pp |
| **PCR Rate** | | | | | 34.45% | 37.02% | **+2.57pp** |

**Key Driver:** Call to PVS (+2.05pp)

#### Waterfall Backend

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 9,441 | 8,406 | -1,035 | -10.96pp | - | - | - |
| Checkout Attempt | 3,768 | 3,480 | -288 | -7.64pp | 39.91% | 41.40% | +1.49pp |
| Enter Fraud Service | 3,763 | 3,479 | -284 | -7.55pp | 99.87% | 99.97% | +0.10pp |
| Approved by Fraud Service | 3,505 | 3,234 | -271 | -7.73pp | 93.14% | 92.96% | -0.19pp |
| PVS Attempt | 3,220 | 3,092 | -128 | -3.98pp | 91.87% | 95.61% | +3.74pp |
| PVS Success | 3,117 | 3,005 | -112 | -3.59pp | 96.80% | 97.19% | +0.39pp |
| **Successful Checkout** | 3,383 | 3,164 | -219 | -6.47pp | 108.53% | 105.29% | -3.24pp |

**Key Driver:** PVS Attempt (+3.74pp)

---

### FJ

#### Waterfall GA

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 40,714 | 39,125 | -1,589 | -3.90pp | - | - | - |
| Select Payment Method | 20,263 | 18,697 | -1,566 | -7.73pp | 49.77% | 47.79% | -1.98pp |
| Click Submit Form | 18,360 | 16,866 | -1,494 | -8.14pp | 90.61% | 90.21% | -0.40pp |
| FE Validation Passed | 17,896 | 16,337 | -1,559 | -8.71pp | 97.47% | 96.86% | -0.61pp |
| Enter Fraud Service | 17,638 | 16,105 | -1,533 | -8.69pp | 98.56% | 98.58% | +0.02pp |
| Approved by Fraud Service | 17,066 | 15,510 | -1,556 | -9.12pp | 96.76% | 96.31% | -0.45pp |
| Call to PVS | 16,950 | 15,499 | -1,451 | -8.56pp | 99.32% | 99.93% | +0.61pp |
| **Successful Checkout** | 16,459 | 15,078 | -1,381 | -8.39pp | 97.10% | 97.28% | +0.18pp |
| **PCR Rate** | | | | | 40.43% | 38.54% | **-1.89pp** |

**Key Driver:** Select Payment Method (-1.98pp)

#### Waterfall Backend

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 79,119 | 74,143 | -4,976 | -6.29pp | - | - | - |
| Checkout Attempt | 29,074 | 26,729 | -2,345 | -8.07pp | 36.75% | 36.05% | -0.70pp |
| Enter Fraud Service | 29,056 | 26,714 | -2,342 | -8.06pp | 99.94% | 99.94% | +0.01pp |
| Approved by Fraud Service | 27,841 | 25,524 | -2,317 | -8.32pp | 95.82% | 95.55% | -0.27pp |
| PVS Attempt | 27,653 | 25,459 | -2,194 | -7.93pp | 99.32% | 99.75% | +0.42pp |
| PVS Success | 26,876 | 24,880 | -1,996 | -7.43pp | 97.19% | 97.73% | +0.54pp |
| **Successful Checkout** | 26,952 | 24,952 | -2,000 | -7.42pp | 100.28% | 100.29% | +0.01pp |

**Key Driver:** Checkout Attempt (-0.70pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (-0.41pp) meets threshold (+0.38pp)

### Recovery Rate

| Metric | 2026-W20 | 2026-W21 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 3,283 | 2,945 | -338 |
| Error → Passed | 2,357 | 1,994 | -363 |
| **Recovery Rate** | **71.79%** | **67.71%** | **-4.09pp** |

### Error Type Distribution

| Error Type | 2026-W20 | 2026-W20 % | 2026-W21 | 2026-W21 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 2,765 | 84.2% | 2,791 | 94.8% | +10.55pp |
| terms_not_accepted | 1,723 | 52.5% | 1,326 | 45.0% | -7.46pp |
| PAYPAL_POPUP_CLOSED | 812 | 24.7% | 694 | 23.6% | -1.17pp |
| CC_TOKENISE_ERR | 197 | 6.0% | 184 | 6.2% | +0.25pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 4 | 0.1% | 153 | 5.2% | +5.07pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 2 | 0.1% | 79 | 2.7% | +2.62pp |
| PAYPAL_TOKENISE_ERR | 89 | 2.7% | 78 | 2.6% | -0.06pp |
| APPLEPAY_TOKENISE_ERR | 0 | 0.0% | 1 | 0.0% | +0.03pp |
| VENMO_TOKENISE_ERR | 1 | 0.0% | 0 | 0.0% | -0.03pp |


---

## Fraud Analysis

**Include reason:** Approved Δ (-0.40pp) meets threshold (+0.38pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W20 | 2026-W20 % | 2026-W21 | 2026-W21 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 41,865 | - | 38,141 | - | -3,724 | -8.9% |
| Enter Fraud Service | 41,795 | - | 38,097 | - | -3,698 | -8.8% |
| **Gap (Skipped)** | **70** | **0.17%** | **44** | **0.12%** | **-26** | **-0.05pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W20 Gap | 2026-W20 % | 2026-W21 Gap | 2026-W21 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Adyen_CreditCard | 46 | 65.7% | 29 | 65.9% | -17 | +0.19pp |
| ProcessOut_CreditCard | 12 | 17.1% | 7 | 15.9% | -5 | -1.23pp |
| Braintree_ApplePay | 5 | 7.1% | 5 | 11.4% | 0 | +4.22pp |
| Braintree_Paypal | 5 | 7.1% | 2 | 4.5% | -3 | -2.60pp |
| Braintree_CreditCard | 0 | 0.0% | 1 | 2.3% | +1 | +2.27pp |
| Adyen_Klarna | 2 | 2.9% | 0 | 0.0% | -2 | -2.86pp |
| **Total** | **70** | **100%** | **44** | **100%** | **-26** | - |

*% of Gap = Payment Method Gap / Total Gap*

---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (+0.62pp) meets threshold (+0.38pp)

| Decline Reason | 2026-W20 | 2026-W20 % | 2026-W21 | 2026-W21 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Failed Verification: Insufficient Funds | 217 | 27.4% | 123 | 20.1% | -94 | -7.37pp |
| RedirectShopper | 168 | 21.2% | 115 | 18.8% | -53 | -2.48pp |
| Blocked Verification: Payment method is blocked due to business reasons | 109 | 13.8% | 89 | 14.5% | -20 | +0.74pp |
| Failed Verification: Card Issuer Declined CVV | 51 | 6.4% | 52 | 8.5% | +1 | +2.04pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 64 | 8.1% | 50 | 8.2% | -14 | +0.07pp |
| Failed Verification: Declined | 44 | 5.6% | 40 | 6.5% | -4 | +0.96pp |
| Pending | 2 | 0.3% | 39 | 6.4% | +37 | +6.11pp |
| Failed Verification: Declined - Call Issuer | 45 | 5.7% | 36 | 5.9% | -9 | +0.18pp |
| Failed Verification: Refused(CVC Declined) | 42 | 5.3% | 35 | 5.7% | -7 | +0.40pp |
| Failed Verification: Issuer or Cardholder has put a restriction on the card | 49 | 6.2% | 34 | 5.5% | -15 | -0.65pp |
| **Total PVS Failures** | **791** | **100%** | **613** | **100%** | **-178** | - |

---


---

*Report: 2026-05-26*
