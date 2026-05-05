# PCR Investigation: HF-NA 2026-W18

**Metric:** Payment Conversion Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 27.42% → 25.22% (-2.20pp)  
**Volume:** 69,229 payment visits  
**Threshold:** +1.10pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined significantly from 27.42% to 25.22% (-2.20pp) in 2026-W18, with volume increasing by 10.2% to 69,229 payment visits.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Δ ≥ -1.10pp | -1.68pp | ⚠️ |
| Click Submit Form | Δ ≥ -1.10pp | -0.78pp | ✅ |
| FE Validation Passed | Δ ≥ -1.10pp | -0.29pp | ✅ |
| Enter Fraud Service | Δ ≥ -1.10pp | -1.09pp | ✅ |
| Approved by Fraud Service | Δ ≥ -1.10pp | +1.56pp | ✅ |
| Call to PVS | Δ ≥ -1.10pp | -1.84pp | ⚠️ |
| Successful Checkout | Δ ≥ -1.10pp | -1.41pp | ⚠️ |

**Key Findings:**
- **Call to PVS step shows critical degradation:** US experienced -2.64pp drop (GA) and -2.90pp in PVS Attempt (Backend), indicating payment verification service connectivity or routing issues
- **Adyen_CreditCard suffered severe decline:** Success rate dropped -10.43pp (89.09% → 78.66%), and fraud service skip gap increased from 23 to 99 transactions (+76 count, +25.71pp share of gap)
- **PVS failures increased 30%:** Total failures rose from 1,053 to 1,368 (+315), with "Insufficient Funds" errors jumping +128 count (+5.29pp share)
- **CA showed upstream degradation:** Select Payment Method conversion dropped -3.20pp (52.58% → 49.38%), suggesting payment page rendering or loading issues
- **ProcessOut_CreditCard declined -3.02pp:** As the highest volume payment method (13,963 attempts), this contributed significantly to overall PCR drop

**Action:** **Investigate** - Prioritize root cause analysis on PVS connectivity issues affecting US market and Adyen_CreditCard integration failures. Review recent deployments or configuration changes impacting payment verification routing.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 62,814 | 69,229 | 6,415 | 10.2% | - | - | - |
| Select Payment Method | 24,989 | 26,378 | 1,389 | 5.6% | 39.78% | 38.10% | -1.68pp |
| Click Submit Form | 21,463 | 22,450 | 987 | 4.6% | 85.89% | 85.11% | -0.78pp |
| FE Validation Passed | 20,241 | 21,107 | 866 | 4.3% | 94.31% | 94.02% | -0.29pp |
| Enter Fraud Service | 19,784 | 20,400 | 616 | 3.1% | 97.74% | 96.65% | -1.09pp |
| Approved by Fraud Service | 18,451 | 19,344 | 893 | 4.8% | 93.26% | 94.82% | +1.56pp |
| Call to PVS | 18,306 | 18,836 | 530 | 2.9% | 99.21% | 97.37% | -1.84pp |
| **Successful Checkout** | 17,226 | 17,460 | 234 | 1.4% | 94.10% | 92.69% | -1.41pp |
| **PCR Rate** | | | | | 27.42% | 25.22% | **-2.20pp** |

### Waterfall Backend

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 66,966 | 74,056 | 7,090 | 10.6% | - | - | - |
| Checkout Attempt | 24,139 | 25,307 | 1,168 | 4.8% | 36.05% | 34.17% | -1.87pp |
| Enter Fraud Service | 24,035 | 25,100 | 1,065 | 4.4% | 99.57% | 99.18% | -0.39pp |
| Approved by Fraud Service | 21,923 | 23,155 | 1,232 | 5.6% | 91.21% | 92.25% | +1.04pp |
| PVS Attempt | 20,363 | 21,205 | 842 | 4.1% | 92.88% | 91.58% | -1.31pp |
| PVS Success | 19,130 | 19,605 | 475 | 2.5% | 93.94% | 92.45% | -1.49pp |
| **Successful Checkout** | 19,694 | 19,995 | 301 | 1.5% | 102.95% | 101.99% | -0.96pp |
| **PCR Rate** | | | | | 29.41% | 27.00% | **-2.41pp** |

### Payment Method Breakdown

| Payment Method | 2026-W17 Attempt | 2026-W17 Success | 2026-W17 Rate | 2026-W18 Attempt | 2026-W18 Success | 2026-W18 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 13,389 | 11,150 | 83.28% | 13,963 | 11,207 | 80.26% | -3.02pp |
| Braintree_ApplePay | 7,646 | 5,930 | 77.56% | 8,075 | 6,159 | 76.27% | -1.28pp |
| Braintree_Paypal | 2,006 | 1,704 | 84.95% | 2,176 | 1,796 | 82.54% | -2.41pp |
| Adyen_CreditCard | 761 | 678 | 89.09% | 717 | 564 | 78.66% | -10.43pp |
| Braintree_CreditCard | 277 | 231 | 83.39% | 312 | 266 | 85.26% | +1.86pp |
|  | 59 | 0 | 0.00% | 52 | 0 | 0.00% | +0.00pp |
| NoPayment | 0 | 0 | 0.00% | 9 | 0 | 0.00% | +0.00pp |
| Braintree_Venmo | 1 | 1 | 100.00% | 3 | 3 | 100.00% | +0.00pp |
| CreditCard | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (2 countries in HF-NA)

| Country | Volume | PCR 2026-W17 | PCR 2026-W18 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| US | 54,039 | 25.39% | 23.37% | -2.02pp | 1 | 2 |
| CA | 15,190 | 34.22% | 31.80% | -2.42pp | 2 | 1 |

---

### US

#### Waterfall GA

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 48,356 | 54,039 | +5,683 | +11.75pp | - | - | - |
| Select Payment Method | 17,387 | 18,877 | +1,490 | +8.57pp | 35.96% | 34.93% | -1.02pp |
| Click Submit Form | 15,354 | 16,479 | +1,125 | +7.33pp | 88.31% | 87.30% | -1.01pp |
| FE Validation Passed | 14,479 | 15,485 | +1,006 | +6.95pp | 94.30% | 93.97% | -0.33pp |
| Enter Fraud Service | 14,193 | 14,994 | +801 | +5.64pp | 98.02% | 96.83% | -1.20pp |
| Approved by Fraud Service | 13,279 | 14,285 | +1,006 | +7.58pp | 93.56% | 95.27% | +1.71pp |
| Call to PVS | 13,247 | 13,874 | +627 | +4.73pp | 99.76% | 97.12% | -2.64pp |
| **Successful Checkout** | 12,278 | 12,630 | +352 | +2.87pp | 92.69% | 91.03% | -1.65pp |
| **PCR Rate** | | | | | 25.39% | 23.37% | **-2.02pp** |

**Key Driver:** Call to PVS (-2.64pp)

#### Waterfall Backend

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 51,507 | 58,098 | +6,591 | +12.80pp | - | - | - |
| Checkout Attempt | 17,450 | 18,914 | +1,464 | +8.39pp | 33.88% | 32.56% | -1.32pp |
| Enter Fraud Service | 17,390 | 18,752 | +1,362 | +7.83pp | 99.66% | 99.14% | -0.51pp |
| Approved by Fraud Service | 15,957 | 17,404 | +1,447 | +9.07pp | 91.76% | 92.81% | +1.05pp |
| PVS Attempt | 15,496 | 16,396 | +900 | +5.81pp | 97.11% | 94.21% | -2.90pp |
| PVS Success | 14,360 | 14,942 | +582 | +4.05pp | 92.67% | 91.13% | -1.54pp |
| **Successful Checkout** | 14,742 | 15,428 | +686 | +4.65pp | 102.66% | 103.25% | +0.59pp |

**Key Driver:** PVS Attempt (-2.90pp)

---

### CA

#### Waterfall GA

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 14,458 | 15,190 | +732 | +5.06pp | - | - | - |
| Select Payment Method | 7,602 | 7,501 | -101 | -1.33pp | 52.58% | 49.38% | -3.20pp |
| Click Submit Form | 6,109 | 5,971 | -138 | -2.26pp | 80.36% | 79.60% | -0.76pp |
| FE Validation Passed | 5,762 | 5,622 | -140 | -2.43pp | 94.32% | 94.16% | -0.16pp |
| Enter Fraud Service | 5,591 | 5,406 | -185 | -3.31pp | 97.03% | 96.16% | -0.87pp |
| Approved by Fraud Service | 5,172 | 5,059 | -113 | -2.18pp | 92.51% | 93.58% | +1.08pp |
| Call to PVS | 5,059 | 4,962 | -97 | -1.92pp | 97.82% | 98.08% | +0.27pp |
| **Successful Checkout** | 4,948 | 4,830 | -118 | -2.38pp | 97.81% | 97.34% | -0.47pp |
| **PCR Rate** | | | | | 34.22% | 31.80% | **-2.43pp** |

**Key Driver:** Select Payment Method (-3.20pp)

#### Waterfall Backend

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 15,459 | 15,958 | +499 | +3.23pp | - | - | - |
| Checkout Attempt | 6,689 | 6,393 | -296 | -4.43pp | 43.27% | 40.06% | -3.21pp |
| Enter Fraud Service | 6,645 | 6,348 | -297 | -4.47pp | 99.34% | 99.30% | -0.05pp |
| Approved by Fraud Service | 5,966 | 5,751 | -215 | -3.60pp | 89.78% | 90.60% | +0.81pp |
| PVS Attempt | 4,867 | 4,809 | -58 | -1.19pp | 81.58% | 83.62% | +2.04pp |
| PVS Success | 4,770 | 4,663 | -107 | -2.24pp | 98.01% | 96.96% | -1.04pp |
| **Successful Checkout** | 5,791 | 5,505 | -286 | -4.94pp | 121.40% | 118.06% | -3.35pp |

**Key Driver:** Successful Checkout (-3.35pp)

---



## Fraud Analysis

**Include reason:** Approved Δ (+1.56pp) meets threshold (+1.10pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W17 | 2026-W17 % | 2026-W18 | 2026-W18 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 24,139 | - | 25,307 | - | 1,168 | 4.8% |
| Enter Fraud Service | 24,035 | - | 25,100 | - | 1,065 | 4.4% |
| **Gap (Skipped)** | **104** | **0.43%** | **207** | **0.82%** | **103** | **+0.39pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W17 Gap | 2026-W17 % | 2026-W18 Gap | 2026-W18 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Adyen_CreditCard | 23 | 22.1% | 99 | 47.8% | +76 | +25.71pp |
| ProcessOut_CreditCard | 42 | 40.4% | 57 | 27.5% | +15 | -12.85pp |
| Braintree_ApplePay | 28 | 26.9% | 28 | 13.5% | 0 | -13.40pp |
| Braintree_Paypal | 11 | 10.6% | 14 | 6.8% | +3 | -3.81pp |
| NoPayment | 0 | 0.0% | 9 | 4.3% | +9 | +4.35pp |
| **Total** | **104** | **100%** | **207** | **100%** | **103** | - |

*% of Gap = Payment Method Gap / Total Gap*

---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (-1.41pp) meets threshold (+1.10pp)

| Decline Reason | 2026-W17 | 2026-W17 % | 2026-W18 | 2026-W18 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Blocked Verification: Payment method is blocked due to business reasons | 593 | 56.3% | 678 | 49.6% | +85 | -6.75pp |
| Failed Verification: Insufficient Funds | 186 | 17.7% | 314 | 23.0% | +128 | +5.29pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 76 | 7.2% | 117 | 8.6% | +41 | +1.34pp |
| Failed Verification: Issuer or Cardholder has put a restriction on the card | 49 | 4.7% | 54 | 3.9% | +5 | -0.71pp |
| Failed Verification: Card Issuer Declined CVV | 28 | 2.7% | 52 | 3.8% | +24 | +1.14pp |
| Failed Verification: Declined - Call Issuer | 31 | 2.9% | 40 | 2.9% | +9 | -0.02pp |
| Failed Verification: Cannot Authorize at this time (Policy) | 17 | 1.6% | 33 | 2.4% | +16 | +0.80pp |
| Failed Verification: Processor Declined - Fraud Suspected | 21 | 2.0% | 30 | 2.2% | +9 | +0.20pp |
| Failed Verification: Declined | 32 | 3.0% | 27 | 2.0% | -5 | -1.07pp |
| Failed Verification: Closed Card | 20 | 1.9% | 23 | 1.7% | +3 | -0.22pp |
| **Total PVS Failures** | **1,053** | **100%** | **1,368** | **100%** | **+315** | - |

---


---

*Report: 2026-05-05*
