# PCR Investigation: US-HF 2026-W18

**Metric:** Payment Conversion Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 25.39% → 23.37% (-2.02pp)  
**Volume:** 54,039 payment visits  
**Threshold:** +1.01pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined by -2.02pp (25.39% → 23.37%) in US-HF for 2026-W18, with volume increasing by 11.8% to 54,039 payment visits.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ≥ ±1.01pp threshold | -1.02pp | ⚠️ |
| Click Submit Form | ≥ ±1.01pp threshold | -1.01pp | ⚠️ |
| FE Validation Passed | ≥ ±1.01pp threshold | -0.33pp | ✅ |
| Enter Fraud Service | ≥ ±1.01pp threshold | -1.20pp | ⚠️ |
| Approved by Fraud Service | ≥ ±1.01pp threshold | +1.71pp | ✅ |
| Call to PVS | ≥ ±1.01pp threshold | -2.64pp | ⚠️ |
| Successful Checkout | ≥ ±1.01pp threshold | -1.65pp | ⚠️ |

**Key Findings:**
- **PVS Routing Gap:** Call to PVS step showed the largest conversion drop (-2.64pp GA, -2.90pp Backend), with 411 fewer transactions reaching PVS than approved by Fraud Service in W18
- **Adyen Integration Issue:** 90 new Adyen_CreditCard checkout attempts in W18 had 0% success rate and 100% skipped fraud service entry, indicating a potential integration or configuration problem
- **ProcessOut_CreditCard Performance Decline:** The primary payment method (55% of attempts) dropped -3.97pp in success rate (83.32% → 79.35%)
- **Insufficient Funds Increase:** PVS failures due to "Insufficient Funds" increased by +118 cases (+5.11pp share), suggesting potential customer base or economic factors
- **Fraud Service Approval Improved:** Despite overall decline, fraud service approval rate improved +1.71pp (93.56% → 95.27%)

**Action:** **Investigate** - Priority focus on (1) Adyen_CreditCard integration causing 100% fraud service bypass, (2) PVS routing gap causing -2.64pp drop post-fraud approval, and (3) ProcessOut_CreditCard success rate decline of -3.97pp

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 48,356 | 54,039 | 5,683 | 11.8% | - | - | - |
| Select Payment Method | 17,387 | 18,877 | 1,490 | 8.6% | 35.96% | 34.93% | -1.02pp |
| Click Submit Form | 15,354 | 16,479 | 1,125 | 7.3% | 88.31% | 87.30% | -1.01pp |
| FE Validation Passed | 14,479 | 15,485 | 1,006 | 6.9% | 94.30% | 93.97% | -0.33pp |
| Enter Fraud Service | 14,193 | 14,994 | 801 | 5.6% | 98.02% | 96.83% | -1.20pp |
| Approved by Fraud Service | 13,279 | 14,285 | 1,006 | 7.6% | 93.56% | 95.27% | +1.71pp |
| Call to PVS | 13,247 | 13,874 | 627 | 4.7% | 99.76% | 97.12% | -2.64pp |
| **Successful Checkout** | 12,278 | 12,630 | 352 | 2.9% | 92.69% | 91.03% | -1.65pp |
| **PCR Rate** | | | | | 25.39% | 23.37% | **-2.02pp** |

### Waterfall Backend

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 51,507 | 58,098 | 6,591 | 12.8% | - | - | - |
| Checkout Attempt | 17,450 | 18,914 | 1,464 | 8.4% | 33.88% | 32.56% | -1.32pp |
| Enter Fraud Service | 17,390 | 18,752 | 1,362 | 7.8% | 99.66% | 99.14% | -0.51pp |
| Approved by Fraud Service | 15,957 | 17,404 | 1,447 | 9.1% | 91.76% | 92.81% | +1.05pp |
| PVS Attempt | 15,496 | 16,396 | 900 | 5.8% | 97.11% | 94.21% | -2.90pp |
| PVS Success | 14,360 | 14,942 | 582 | 4.1% | 92.67% | 91.13% | -1.54pp |
| **Successful Checkout** | 14,039 | 14,591 | 552 | 3.9% | 97.76% | 97.65% | -0.11pp |
| **PCR Rate** | | | | | 27.26% | 25.11% | **-2.14pp** |

### Payment Method Breakdown

| Payment Method | 2026-W17 Attempt | 2026-W17 Success | 2026-W17 Rate | 2026-W18 Attempt | 2026-W18 Success | 2026-W18 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 9,759 | 8,131 | 83.32% | 10,449 | 8,291 | 79.35% | -3.97pp |
| Braintree_ApplePay | 5,994 | 4,531 | 75.59% | 6,474 | 4,784 | 73.90% | -1.70pp |
| Braintree_Paypal | 1,360 | 1,145 | 84.19% | 1,534 | 1,247 | 81.29% | -2.90pp |
| Braintree_CreditCard | 277 | 231 | 83.39% | 312 | 266 | 85.26% | +1.86pp |
| Adyen_CreditCard | 0 | 0 | 0.00% | 90 | 0 | 0.00% | +0.00pp |
|  | 59 | 0 | 0.00% | 52 | 0 | 0.00% | +0.00pp |
| Braintree_Venmo | 1 | 1 | 100.00% | 3 | 3 | 100.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (1 countries in US-HF)

| Country | Volume | PCR 2026-W17 | PCR 2026-W18 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| US | 54,039 | 25.39% | 23.37% | -2.02pp | 1 | 1 |

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



## Fraud Analysis

**Include reason:** Enter FS Δ (-1.20pp) meets threshold (+1.01pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W17 | 2026-W17 % | 2026-W18 | 2026-W18 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 17,450 | - | 18,914 | - | 1,464 | 8.4% |
| Enter Fraud Service | 17,390 | - | 18,752 | - | 1,362 | 7.8% |
| **Gap (Skipped)** | **60** | **0.34%** | **162** | **0.86%** | **102** | **+0.51pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W17 Gap | 2026-W17 % | 2026-W18 Gap | 2026-W18 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Adyen_CreditCard | 0 | 0.0% | 90 | 55.6% | +90 | +55.56pp |
| ProcessOut_CreditCard | 32 | 53.3% | 44 | 27.2% | +12 | -26.17pp |
| Braintree_ApplePay | 20 | 33.3% | 19 | 11.7% | -1 | -21.60pp |
| Braintree_Paypal | 8 | 13.3% | 8 | 4.9% | 0 | -8.40pp |
| Braintree_CreditCard | 0 | 0.0% | 1 | 0.6% | +1 | +0.62pp |
| **Total** | **60** | **100%** | **162** | **100%** | **102** | - |

*% of Gap = Payment Method Gap / Total Gap*

---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (-1.65pp) meets threshold (+1.01pp)

| Decline Reason | 2026-W17 | 2026-W17 % | 2026-W18 | 2026-W18 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Blocked Verification: Payment method is blocked due to business reasons | 593 | 58.1% | 678 | 51.5% | +85 | -6.66pp |
| Failed Verification: Insufficient Funds | 174 | 17.1% | 292 | 22.2% | +118 | +5.11pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 62 | 6.1% | 97 | 7.4% | +35 | +1.29pp |
| Failed Verification: Issuer or Cardholder has put a restriction on the card | 48 | 4.7% | 54 | 4.1% | +6 | -0.61pp |
| Failed Verification: Card Issuer Declined CVV | 28 | 2.7% | 52 | 3.9% | +24 | +1.20pp |
| Failed Verification: Declined - Call Issuer | 30 | 2.9% | 39 | 3.0% | +9 | +0.02pp |
| Failed Verification: Cannot Authorize at this time (Policy) | 17 | 1.7% | 31 | 2.4% | +14 | +0.69pp |
| Failed Verification: Processor Declined - Fraud Suspected | 21 | 2.1% | 29 | 2.2% | +8 | +0.14pp |
| Failed Verification: Declined | 27 | 2.6% | 23 | 1.7% | -4 | -0.90pp |
| Failed Verification: Closed Card | 20 | 2.0% | 22 | 1.7% | +2 | -0.29pp |
| **Total PVS Failures** | **1,020** | **100%** | **1,317** | **100%** | **+297** | - |

---


---

*Report: 2026-05-05*
