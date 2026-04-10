# PCR Investigation: HF-NA 2026-W13

**Metric:** Payment Conversion Rate  
**Period:** 2026-W12 → 2026-W13  
**Observation:** 28.35% → 28.63% (+0.28pp)  
**Volume:** 59,286 payment visits  
**Threshold:** +0.14pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate improved by +0.28pp (28.35% → 28.63%) in HF-NA during 2026-W13, driven primarily by a significant uplift in the Click Submit Form step (+2.55pp), despite a 4.1% decrease in payment visit volume.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Below threshold | -1.05pp | ⚠️ |
| Click Submit Form | Above threshold | +2.55pp | ✅ |
| FE Validation Passed | Above threshold | +0.93pp | ✅ |
| Enter Fraud Service | Below threshold | +0.07pp | ✅ |
| Approved by Fraud Service | Below threshold | -0.38pp | ⚠️ |
| Call to PVS | Above threshold | +0.52pp | ✅ |
| Successful Checkout | Below threshold | -0.62pp | ⚠️ |

**Key Findings:**
- **Click Submit Form conversion surged +2.55pp** at the cluster level, with US showing an even stronger improvement of +4.21pp, indicating improved form submission behavior
- **Adyen_CreditCard experienced a catastrophic decline** from 90.66% to 3.85% success rate (-86.82pp), with 123 transactions now skipping fraud service entry (up from 10), suggesting a critical integration failure
- **Braintree_CreditCard volume dropped 91%** (3,268 → 281 attempts) but success rate improved significantly (+7.23pp), indicating a potential traffic routing change to ProcessOut_CreditCard (which increased from 11,105 to 14,991 attempts)
- **FE Validation recovery rate improved +2.06pp** (70.19% → 72.25%), with CC_NO_PREPAID_ERR nearly eliminated (250 → 2 occurrences, -5.01pp share)
- **PVS blocked verifications increased** (+56 counts, +2.83pp share), becoming the dominant decline reason at 53.5% of all PVS failures

**Action:** **Investigate** — The Adyen_CreditCard integration failure requires immediate attention as it shows near-complete payment failure (3.85% success rate) and a significant increase in fraud service bypass. Additionally, confirm the traffic migration from Braintree_CreditCard to ProcessOut_CreditCard was intentional.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 61,825 | 59,286 | -2,539 | -4.1% | - | - | - |
| Select Payment Method | 26,062 | 24,367 | -1,695 | -6.5% | 42.15% | 41.10% | -1.05pp |
| Click Submit Form | 21,633 | 20,847 | -786 | -3.6% | 83.01% | 85.55% | +2.55pp |
| FE Validation Passed | 20,333 | 19,788 | -545 | -2.7% | 93.99% | 94.92% | +0.93pp |
| Enter Fraud Service | 19,884 | 19,364 | -520 | -2.6% | 97.79% | 97.86% | +0.07pp |
| Approved by Fraud Service | 18,674 | 18,112 | -562 | -3.0% | 93.91% | 93.53% | -0.38pp |
| Call to PVS | 18,562 | 18,097 | -465 | -2.5% | 99.40% | 99.92% | +0.52pp |
| **Successful Checkout** | 17,527 | 16,975 | -552 | -3.1% | 94.42% | 93.80% | -0.62pp |
| **PCR Rate** | | | | | 28.35% | 28.63% | **+0.28pp** |

### Waterfall Backend

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 68,668 | 65,957 | -2,711 | -3.9% | - | - | - |
| Checkout Attempt | 25,136 | 24,928 | -208 | -0.8% | 36.61% | 37.79% | +1.19pp |
| Enter Fraud Service | 25,260 | 24,773 | -487 | -1.9% | 100.49% | 99.38% | -1.12pp |
| Approved by Fraud Service | 22,879 | 22,212 | -667 | -2.9% | 90.57% | 89.66% | -0.91pp |
| PVS Attempt | 21,127 | 20,751 | -376 | -1.8% | 92.34% | 93.42% | +1.08pp |
| PVS Success | 19,899 | 19,490 | -409 | -2.1% | 94.19% | 93.92% | -0.26pp |
| **Successful Checkout** | 20,526 | 20,042 | -484 | -2.4% | 103.15% | 102.83% | -0.32pp |
| **PCR Rate** | | | | | 29.89% | 30.39% | **+0.49pp** |

### Payment Method Breakdown

| Payment Method | 2026-W12 Attempt | 2026-W12 Success | 2026-W12 Rate | 2026-W13 Attempt | 2026-W13 Success | 2026-W13 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 11,105 | 9,245 | 83.25% | 14,991 | 12,281 | 81.92% | -1.33pp |
| Braintree_ApplePay | 7,668 | 5,972 | 77.88% | 7,428 | 5,796 | 78.03% | +0.15pp |
| Braintree_Paypal | 2,086 | 1,796 | 86.10% | 1,961 | 1,707 | 87.05% | +0.95pp |
| Braintree_CreditCard | 3,268 | 2,706 | 82.80% | 281 | 253 | 90.04% | +7.23pp |
|  | 119 | 0 | 0.00% | 136 | 0 | 0.00% | +0.00pp |
| Adyen_CreditCard | 889 | 806 | 90.66% | 130 | 5 | 3.85% | -86.82pp |
| NoPayment | 0 | 0 | 0.00% | 1 | 0 | 0.00% | +0.00pp |
| ApplePay | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |
| Braintree_Venmo | 1 | 1 | 100.00% | 0 | 0 | 0.00% | -100.00pp |
| CreditCard | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (2 countries in HF-NA)

| Country | Volume | PCR 2026-W12 | PCR 2026-W13 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| US | 44,370 | 26.18% | 26.77% | +0.59pp | 1 | 2 |
| CA | 14,916 | 34.89% | 34.16% | -0.73pp | 2 | 1 |

---

### US

#### Waterfall GA

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 46,444 | 44,370 | -2,074 | -4.47pp | - | - | - |
| Select Payment Method | 18,056 | 16,684 | -1,372 | -7.60pp | 38.88% | 37.60% | -1.27pp |
| Click Submit Form | 15,184 | 14,732 | -452 | -2.98pp | 84.09% | 88.30% | +4.21pp |
| FE Validation Passed | 14,250 | 13,994 | -256 | -1.80pp | 93.85% | 94.99% | +1.14pp |
| Enter Fraud Service | 13,938 | 13,714 | -224 | -1.61pp | 97.81% | 98.00% | +0.19pp |
| Approved by Fraud Service | 13,102 | 12,848 | -254 | -1.94pp | 94.00% | 93.69% | -0.32pp |
| Call to PVS | 13,082 | 12,852 | -230 | -1.76pp | 99.85% | 100.03% | +0.18pp |
| **Successful Checkout** | 12,160 | 11,879 | -281 | -2.31pp | 92.95% | 92.43% | -0.52pp |
| **PCR Rate** | | | | | 26.18% | 26.77% | **+0.59pp** |

**Key Driver:** Click Submit Form (+4.21pp)

#### Waterfall Backend

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 50,863 | 48,829 | -2,034 | -4.00pp | - | - | - |
| Checkout Attempt | 17,752 | 17,802 | +50 | +0.28pp | 34.90% | 36.46% | +1.56pp |
| Enter Fraud Service | 17,717 | 17,647 | -70 | -0.40pp | 99.80% | 99.13% | -0.67pp |
| Approved by Fraud Service | 15,978 | 15,733 | -245 | -1.53pp | 90.18% | 89.15% | -1.03pp |
| PVS Attempt | 15,651 | 15,361 | -290 | -1.85pp | 97.95% | 97.64% | -0.32pp |
| PVS Success | 14,543 | 14,219 | -324 | -2.23pp | 92.92% | 92.57% | -0.35pp |
| **Successful Checkout** | 14,855 | 14,691 | -164 | -1.10pp | 102.15% | 103.32% | +1.17pp |

**Key Driver:** Checkout Attempt (+1.56pp)

---

### CA

#### Waterfall GA

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 15,381 | 14,916 | -465 | -3.02pp | - | - | - |
| Select Payment Method | 8,006 | 7,683 | -323 | -4.03pp | 52.05% | 51.51% | -0.54pp |
| Click Submit Form | 6,449 | 6,115 | -334 | -5.18pp | 80.55% | 79.59% | -0.96pp |
| FE Validation Passed | 6,083 | 5,794 | -289 | -4.75pp | 94.32% | 94.75% | +0.43pp |
| Enter Fraud Service | 5,946 | 5,650 | -296 | -4.98pp | 97.75% | 97.51% | -0.23pp |
| Approved by Fraud Service | 5,572 | 5,264 | -308 | -5.53pp | 93.71% | 93.17% | -0.54pp |
| Call to PVS | 5,480 | 5,245 | -235 | -4.29pp | 98.35% | 99.64% | +1.29pp |
| **Successful Checkout** | 5,367 | 5,096 | -271 | -5.05pp | 97.94% | 97.16% | -0.78pp |
| **PCR Rate** | | | | | 34.89% | 34.16% | **-0.73pp** |

**Key Driver:** Call to PVS (+1.29pp)

#### Waterfall Backend

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 17,805 | 17,128 | -677 | -3.80pp | - | - | - |
| Checkout Attempt | 7,384 | 7,126 | -258 | -3.49pp | 41.47% | 41.60% | +0.13pp |
| Enter Fraud Service | 7,543 | 7,126 | -417 | -5.53pp | 102.15% | 100.00% | -2.15pp |
| Approved by Fraud Service | 6,901 | 6,479 | -422 | -6.12pp | 91.49% | 90.92% | -0.57pp |
| PVS Attempt | 5,476 | 5,390 | -86 | -1.57pp | 79.35% | 83.19% | +3.84pp |
| PVS Success | 5,356 | 5,271 | -85 | -1.59pp | 97.81% | 97.79% | -0.02pp |
| **Successful Checkout** | 6,520 | 6,306 | -214 | -3.28pp | 121.73% | 119.64% | -2.10pp |

**Key Driver:** PVS Attempt (+3.84pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (+0.93pp) meets threshold (+0.14pp)

### Recovery Rate

| Metric | 2026-W12 | 2026-W13 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 4,948 | 4,587 | -361 |
| Error → Passed | 3,473 | 3,314 | -159 |
| **Recovery Rate** | **70.19%** | **72.25%** | **+2.06pp** |

### Error Type Distribution

| Error Type | 2026-W12 | 2026-W12 % | 2026-W13 | 2026-W13 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 2,657 | 53.7% | 2,505 | 54.6% | +0.91pp |
| terms_not_accepted | 2,074 | 41.9% | 2,064 | 45.0% | +3.08pp |
| PAYPAL_POPUP_CLOSED | 450 | 9.1% | 455 | 9.9% | +0.82pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 277 | 5.6% | 293 | 6.4% | +0.79pp |
| CC_TOKENISE_ERR | 133 | 2.7% | 158 | 3.4% | +0.76pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 126 | 2.5% | 123 | 2.7% | +0.14pp |
| PAYPAL_TOKENISE_ERR | 53 | 1.1% | 39 | 0.9% | -0.22pp |
| CC_NO_PREPAID_ERR | 250 | 5.1% | 2 | 0.0% | -5.01pp |
| APPLEPAY_MERCHANT_VALIDATION_ERR | 5 | 0.1% | 0 | 0.0% | -0.10pp |
| VENMO_TOKENISE_ERR | 1 | 0.0% | 0 | 0.0% | -0.02pp |


---

## Fraud Analysis

**Include reason:** Approved Δ (-0.38pp) meets threshold (+0.14pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W12 | 2026-W12 % | 2026-W13 | 2026-W13 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 25,136 | - | 24,928 | - | -208 | -0.8% |
| Enter Fraud Service | 25,260 | - | 24,773 | - | -487 | -1.9% |
| **Gap (Skipped)** | **-124** | **-0.49%** | **155** | **0.62%** | **279** | **+1.12pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W12 Gap | 2026-W12 % | 2026-W13 Gap | 2026-W13 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Adyen_CreditCard | 10 | 18.5% | 123 | 65.8% | +113 | +47.26pp |
| ProcessOut_CreditCard | 21 | 38.9% | 37 | 19.8% | +16 | -19.10pp |
| Braintree_ApplePay | 9 | 16.7% | 21 | 11.2% | +12 | -5.44pp |
| Braintree_Paypal | 10 | 18.5% | 5 | 2.7% | -5 | -15.84pp |
| NoPayment | 0 | 0.0% | 1 | 0.5% | +1 | +0.53pp |
| Braintree_CreditCard | 4 | 7.4% | 0 | 0.0% | -4 | -7.41pp |
| **Total** | **54** | **100%** | **187** | **100%** | **133** | - |

*% of Gap = Payment Method Gap / Total Gap*

---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (-0.62pp) meets threshold (+0.14pp)

| Decline Reason | 2026-W12 | 2026-W12 % | 2026-W13 | 2026-W13 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Blocked Verification: Payment method is blocked due to business reasons | 514 | 50.7% | 570 | 53.5% | +56 | +2.83pp |
| Failed Verification: Insufficient Funds | 217 | 21.4% | 184 | 17.3% | -33 | -4.12pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 77 | 7.6% | 83 | 7.8% | +6 | +0.20pp |
| Failed Verification: Card Not Activated | 43 | 4.2% | 38 | 3.6% | -5 | -0.67pp |
| Failed Verification: Card Issuer Declined CVV | 48 | 4.7% | 37 | 3.5% | -11 | -1.26pp |
| Failed Verification: Issuer or Cardholder has put a restriction on the card | 19 | 1.9% | 36 | 3.4% | +17 | +1.51pp |
| Failed Verification: Declined - Call Issuer | 22 | 2.2% | 36 | 3.4% | +14 | +1.21pp |
| Failed Verification: Closed Card | 28 | 2.8% | 33 | 3.1% | +5 | +0.34pp |
| Failed Verification: Cannot Authorize at this time (Policy) | 19 | 1.9% | 28 | 2.6% | +9 | +0.76pp |
| Failed Verification: Processor Declined | 27 | 2.7% | 20 | 1.9% | -7 | -0.78pp |
| **Total PVS Failures** | **1,014** | **100%** | **1,065** | **100%** | **+51** | - |

---


---

*Report: 2026-04-10*
