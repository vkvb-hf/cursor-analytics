# PCR Investigation: WL 2026-W19

**Metric:** Payment Conversion Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 29.75% → 29.33% (-0.42pp)  
**Volume:** 39,753 payment visits  
**Threshold:** +0.21pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined from 29.75% to 29.33% (-0.42pp) in 2026-W19, driven primarily by frontend validation failures and reduced form submission rates.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Rate change vs threshold | -0.09pp | ✅ |
| Click Submit Form | Rate change vs threshold | -0.45pp | ⚠️ |
| FE Validation Passed | Rate change vs threshold | -0.58pp | ⚠️ |
| Enter Fraud Service | Rate change vs threshold | +0.14pp | ✅ |
| Approved by Fraud Service | Rate change vs threshold | +0.05pp | ✅ |
| Call to PVS | Rate change vs threshold | +0.08pp | ✅ |
| Successful Checkout | Rate change vs threshold | -0.35pp | ⚠️ |

**Key Findings:**
- FE Validation Passed showed the largest conversion drop (-0.58pp), with recovery rate declining from 63.05% to 59.98% (-3.07pp)
- APPLEPAY_DISMISSED errors increased from 60.7% to 63.7% of all FE errors, becoming the dominant error type
- GN experienced the largest PCR decline (-4.06pp), driven by FE Validation issues (-3.29pp) and reduced form submissions (-2.79pp)
- KN showed significant deterioration at Select Payment Method (-2.69pp), contributing to a -3.00pp PCR decline
- MR was the sole positive performer (+3.46pp PCR improvement), with Select Payment Method improving by +3.14pp
- Braintree_CreditCard payment method showed notable decline (-3.28pp success rate)

**Action:** Investigate - Focus on FE validation issues, particularly APPLEPAY_DISMISSED errors and the declining recovery rate. Priority investigation needed for GN and KN markets.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 37,719 | 39,753 | 2,034 | 5.4% | - | - | - |
| Select Payment Method | 15,172 | 15,956 | 784 | 5.2% | 40.22% | 40.14% | -0.09pp |
| Click Submit Form | 13,481 | 14,106 | 625 | 4.6% | 88.85% | 88.41% | -0.45pp |
| FE Validation Passed | 12,989 | 13,509 | 520 | 4.0% | 96.35% | 95.77% | -0.58pp |
| Enter Fraud Service | 12,433 | 12,949 | 516 | 4.2% | 95.72% | 95.85% | +0.14pp |
| Approved by Fraud Service | 11,778 | 12,273 | 495 | 4.2% | 94.73% | 94.78% | +0.05pp |
| Call to PVS | 11,649 | 12,149 | 500 | 4.3% | 98.90% | 98.99% | +0.08pp |
| **Successful Checkout** | 11,220 | 11,659 | 439 | 3.9% | 96.32% | 95.97% | -0.35pp |
| **PCR Rate** | | | | | 29.75% | 29.33% | **-0.42pp** |

### Waterfall Backend

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 44,387 | 46,798 | 2,411 | 5.4% | - | - | - |
| Checkout Attempt | 14,203 | 14,652 | 449 | 3.2% | 32.00% | 31.31% | -0.69pp |
| Enter Fraud Service | 14,119 | 14,541 | 422 | 3.0% | 99.41% | 99.24% | -0.17pp |
| Approved by Fraud Service | 13,132 | 13,543 | 411 | 3.1% | 93.01% | 93.14% | +0.13pp |
| PVS Attempt | 10,753 | 10,480 | -273 | -2.5% | 81.88% | 77.38% | -4.50pp |
| PVS Success | 10,325 | 9,985 | -340 | -3.3% | 96.02% | 95.28% | -0.74pp |
| **Successful Checkout** | 12,656 | 13,026 | 370 | 2.9% | 122.58% | 130.46% | +7.88pp |
| **PCR Rate** | | | | | 28.51% | 27.83% | **-0.68pp** |

### Payment Method Breakdown

| Payment Method | 2026-W18 Attempt | 2026-W18 Success | 2026-W18 Rate | 2026-W19 Attempt | 2026-W19 Success | 2026-W19 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 3,942 | 3,463 | 87.85% | 4,246 | 3,703 | 87.21% | -0.64pp |
| Braintree_ApplePay | 4,128 | 3,756 | 90.99% | 4,130 | 3,746 | 90.70% | -0.29pp |
| Adyen_CreditCard | 2,644 | 2,323 | 87.86% | 2,709 | 2,434 | 89.85% | +1.99pp |
| Braintree_Paypal | 1,677 | 1,517 | 90.46% | 1,841 | 1,677 | 91.09% | +0.63pp |
| Braintree_CreditCard | 1,522 | 1,333 | 87.58% | 1,478 | 1,246 | 84.30% | -3.28pp |
| ProcessOut_ApplePay | 287 | 264 | 91.99% | 245 | 219 | 89.39% | -2.60pp |
| NoPayment | 3 | 0 | 0.00% | 2 | 0 | 0.00% | +0.00pp |
| Braintree_Venmo | 0 | 0 | 0.00% | 1 | 1 | 100.00% | +100.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (3 countries in WL)

| Country | Volume | PCR 2026-W18 | PCR 2026-W19 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| MR | 10,300 | 21.61% | 25.07% | +3.46pp | 1 | 2 |
| KN | 9,112 | 26.63% | 23.63% | -3.00pp | 2 | 3 |
| GN | 3,045 | 38.81% | 34.75% | -4.06pp | 3 | 1 |

---

### GN

#### Waterfall GA

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 2,394 | 3,045 | +651 | +27.19pp | - | - | - |
| Select Payment Method | 1,400 | 1,727 | +327 | +23.36pp | 58.48% | 56.72% | -1.76pp |
| Click Submit Form | 1,247 | 1,490 | +243 | +19.49pp | 89.07% | 86.28% | -2.79pp |
| FE Validation Passed | 1,057 | 1,214 | +157 | +14.85pp | 84.76% | 81.48% | -3.29pp |
| Enter Fraud Service | 1,004 | 1,140 | +136 | +13.55pp | 94.99% | 93.90% | -1.08pp |
| Approved by Fraud Service | 963 | 1,100 | +137 | +14.23pp | 95.92% | 96.49% | +0.57pp |
| Call to PVS | 960 | 1,098 | +138 | +14.37pp | 99.69% | 99.82% | +0.13pp |
| **Successful Checkout** | 929 | 1,058 | +129 | +13.89pp | 96.77% | 96.36% | -0.41pp |
| **PCR Rate** | | | | | 38.81% | 34.75% | **-4.06pp** |

**Key Driver:** FE Validation Passed (-3.29pp)

#### Waterfall Backend

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 3,190 | 3,984 | +794 | +24.89pp | - | - | - |
| Checkout Attempt | 1,336 | 1,478 | +142 | +10.63pp | 41.88% | 37.10% | -4.78pp |
| Enter Fraud Service | 1,332 | 1,470 | +138 | +10.36pp | 99.70% | 99.46% | -0.24pp |
| Approved by Fraud Service | 1,264 | 1,403 | +139 | +11.00pp | 94.89% | 95.44% | +0.55pp |
| PVS Attempt | 1,102 | 1,250 | +148 | +13.43pp | 87.18% | 89.09% | +1.91pp |
| PVS Success | 1,067 | 1,212 | +145 | +13.59pp | 96.82% | 96.96% | +0.14pp |
| **Successful Checkout** | 1,248 | 1,394 | +146 | +11.70pp | 116.96% | 115.02% | -1.95pp |

**Key Driver:** Checkout Attempt (-4.78pp)

---

### KN

#### Waterfall GA

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 8,396 | 9,112 | +716 | +8.53pp | - | - | - |
| Select Payment Method | 2,943 | 2,949 | +6 | +0.20pp | 35.05% | 32.36% | -2.69pp |
| Click Submit Form | 2,572 | 2,533 | -39 | -1.52pp | 87.39% | 85.89% | -1.50pp |
| FE Validation Passed | 2,632 | 2,594 | -38 | -1.44pp | 102.33% | 102.41% | +0.08pp |
| Enter Fraud Service | 2,458 | 2,413 | -45 | -1.83pp | 93.39% | 93.02% | -0.37pp |
| Approved by Fraud Service | 2,310 | 2,258 | -52 | -2.25pp | 93.98% | 93.58% | -0.40pp |
| Call to PVS | 2,307 | 2,256 | -51 | -2.21pp | 99.87% | 99.91% | +0.04pp |
| **Successful Checkout** | 2,236 | 2,153 | -83 | -3.71pp | 96.92% | 95.43% | -1.49pp |
| **PCR Rate** | | | | | 26.63% | 23.63% | **-3.00pp** |

**Key Driver:** Select Payment Method (-2.69pp)

#### Waterfall Backend

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 10,101 | 10,819 | +718 | +7.11pp | - | - | - |
| Checkout Attempt | 2,848 | 2,799 | -49 | -1.72pp | 28.20% | 25.87% | -2.32pp |
| Enter Fraud Service | 2,780 | 2,717 | -63 | -2.27pp | 97.61% | 97.07% | -0.54pp |
| Approved by Fraud Service | 2,537 | 2,459 | -78 | -3.07pp | 91.26% | 90.50% | -0.75pp |
| PVS Attempt | 2,534 | 2,457 | -77 | -3.04pp | 99.88% | 99.92% | +0.04pp |
| PVS Success | 2,472 | 2,370 | -102 | -4.13pp | 97.55% | 96.46% | -1.09pp |
| **Successful Checkout** | 2,472 | 2,372 | -100 | -4.05pp | 100.00% | 100.08% | +0.08pp |

**Key Driver:** Checkout Attempt (-2.32pp)

---

### MR

#### Waterfall GA

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 9,310 | 10,300 | +990 | +10.63pp | - | - | - |
| Select Payment Method | 2,580 | 3,178 | +598 | +23.18pp | 27.71% | 30.85% | +3.14pp |
| Click Submit Form | 2,290 | 2,861 | +571 | +24.93pp | 88.76% | 90.03% | +1.27pp |
| FE Validation Passed | 2,323 | 2,886 | +563 | +24.24pp | 101.44% | 100.87% | -0.57pp |
| Enter Fraud Service | 2,180 | 2,742 | +562 | +25.78pp | 93.84% | 95.01% | +1.17pp |
| Approved by Fraud Service | 2,101 | 2,682 | +581 | +27.65pp | 96.38% | 97.81% | +1.44pp |
| Call to PVS | 2,005 | 2,578 | +573 | +28.58pp | 95.43% | 96.12% | +0.69pp |
| **Successful Checkout** | 2,012 | 2,582 | +570 | +28.33pp | 100.35% | 100.16% | -0.19pp |
| **PCR Rate** | | | | | 21.61% | 25.07% | **+3.46pp** |

**Key Driver:** Select Payment Method (+3.14pp)

#### Waterfall Backend

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 10,812 | 12,194 | +1,382 | +12.78pp | - | - | - |
| Checkout Attempt | 2,380 | 3,084 | +704 | +29.58pp | 22.01% | 25.29% | +3.28pp |
| Enter Fraud Service | 2,378 | 3,079 | +701 | +29.48pp | 99.92% | 99.84% | -0.08pp |
| Approved by Fraud Service | 2,274 | 2,987 | +713 | +31.35pp | 95.63% | 97.01% | +1.39pp |
| PVS Attempt | 86 | 90 | +4 | +4.65pp | 3.78% | 3.01% | -0.77pp |
| PVS Success | 83 | 88 | +5 | +6.02pp | 96.51% | 97.78% | +1.27pp |
| **Successful Checkout** | 2,187 | 2,880 | +693 | +31.69pp | 2634.94% | 3272.73% | +637.79pp |

**Key Driver:** Successful Checkout (+637.79pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (-0.58pp) meets threshold (+0.21pp)

### Recovery Rate

| Metric | 2026-W18 | 2026-W19 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 1,808 | 1,904 | 96 |
| Error → Passed | 1,140 | 1,142 | 2 |
| **Recovery Rate** | **63.05%** | **59.98%** | **-3.07pp** |

### Error Type Distribution

| Error Type | 2026-W18 | 2026-W18 % | 2026-W19 | 2026-W19 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 1,097 | 60.7% | 1,212 | 63.7% | +2.98pp |
| terms_not_accepted | 826 | 45.7% | 725 | 38.1% | -7.61pp |
| PAYPAL_POPUP_CLOSED | 276 | 15.3% | 293 | 15.4% | +0.12pp |
| PAYPAL_TOKENISE_ERR | 20 | 1.1% | 25 | 1.3% | +0.21pp |
| CC_TOKENISE_ERR | 32 | 1.8% | 23 | 1.2% | -0.56pp |
| VENMO_TOKENISE_ERR | 1 | 0.1% | 0 | 0.0% | -0.06pp |


---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (-0.35pp) meets threshold (+0.21pp)

| Decline Reason | 2026-W18 | 2026-W18 % | 2026-W19 | 2026-W19 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Failed Verification: Insufficient Funds | 71 | 29.3% | 80 | 25.8% | +9 | -3.53pp |
| Blocked Verification: Payment method is blocked due to business reasons | 44 | 18.2% | 63 | 20.3% | +19 | +2.14pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 31 | 12.8% | 32 | 10.3% | +1 | -2.49pp |
| ChallengeShopper | 14 | 5.8% | 25 | 8.1% | +11 | +2.28pp |
| Failed Verification: Refused(Refused) | 10 | 4.1% | 21 | 6.8% | +11 | +2.64pp |
| Failed Verification: Invalid Merchant ID | 14 | 5.8% | 19 | 6.1% | +5 | +0.34pp |
| Failed Verification: Card Issuer Declined CVV | 18 | 7.4% | 18 | 5.8% | 0 | -1.63pp |
| Refused: Refused(3D Not Authenticated) | 14 | 5.8% | 18 | 5.8% | +4 | +0.02pp |
| Failed Verification: Refused(Not enough balance) | 18 | 7.4% | 17 | 5.5% | -1 | -1.95pp |
| Failed Verification: Declined | 8 | 3.3% | 17 | 5.5% | +9 | +2.18pp |
| **Total PVS Failures** | **242** | **100%** | **310** | **100%** | **+68** | - |

---


---

*Report: 2026-05-12*
