# PCR Investigation: US-HF 2026-W21

**Metric:** Payment Conversion Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 23.88% → 25.15% (+1.27pp)  
**Volume:** 43,124 payment visits  
**Threshold:** +0.63pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate improved significantly from 23.88% to 25.15% (+1.27pp) in US-HF for 2026-W21, driven primarily by improvements in PVS-related steps despite a 12.1% decrease in payment visit volume.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ≥ threshold? | +1.37pp | ✅ |
| Click Submit Form | ≥ threshold? | -0.67pp | ⚠️ |
| FE Validation Passed | ≥ threshold? | +0.34pp | ✅ |
| Enter Fraud Service | ≥ threshold? | -0.29pp | ✅ |
| Approved by Fraud Service | ≥ threshold? | -0.94pp | ⚠️ |
| Call to PVS | ≥ threshold? | +1.66pp | ✅ |
| Successful Checkout | ≥ threshold? | +1.32pp | ✅ |

**Key Findings:**
- **PVS performance significantly improved:** Call to PVS conversion increased +1.66pp (GA) and PVS Attempt +1.74pp (Backend), indicating better payment processor reliability
- **Insufficient Funds declines dropped substantially:** Failed Verification due to Insufficient Funds decreased by 202 cases (-9.04pp share), contributing to higher PVS success rates
- **ProcessOut_CreditCard success rate improved:** The primary payment method saw a +3.46pp increase in success rate (78.77% → 82.23%), driving overall PCR improvement
- **Fraud Service approval slightly declined:** Approved by Fraud Service dropped -0.94pp, exceeding the threshold, though this was offset by downstream improvements
- **Adyen_CreditCard fraud gap resolved:** Gap between Checkout Attempt and Enter Fraud Service for Adyen_CreditCard dropped from 84 to 1 case (-83 count)

**Action:** Monitor - The PCR improvement is healthy and driven by legitimate PVS and payment method performance gains. Continue monitoring Fraud Service approval rates to ensure the -0.94pp decline does not worsen.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 49,081 | 43,124 | -5,957 | -12.1% | - | - | - |
| Select Payment Method | 17,721 | 16,159 | -1,562 | -8.8% | 36.11% | 37.47% | +1.37pp |
| Click Submit Form | 15,544 | 14,066 | -1,478 | -9.5% | 87.72% | 87.05% | -0.67pp |
| FE Validation Passed | 14,496 | 13,166 | -1,330 | -9.2% | 93.26% | 93.60% | +0.34pp |
| Enter Fraud Service | 14,076 | 12,747 | -1,329 | -9.4% | 97.10% | 96.82% | -0.29pp |
| Approved by Fraud Service | 13,352 | 11,972 | -1,380 | -10.3% | 94.86% | 93.92% | -0.94pp |
| Call to PVS | 13,101 | 11,946 | -1,155 | -8.8% | 98.12% | 99.78% | +1.66pp |
| **Successful Checkout** | 11,720 | 10,845 | -875 | -7.5% | 89.46% | 90.78% | +1.32pp |
| **PCR Rate** | | | | | 23.88% | 25.15% | **+1.27pp** |

### Waterfall Backend

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 52,063 | 46,653 | -5,410 | -10.4% | - | - | - |
| Checkout Attempt | 17,590 | 15,926 | -1,664 | -9.5% | 33.79% | 34.14% | +0.35pp |
| Enter Fraud Service | 17,433 | 15,858 | -1,575 | -9.0% | 99.11% | 99.57% | +0.47pp |
| Approved by Fraud Service | 16,250 | 14,707 | -1,543 | -9.5% | 93.21% | 92.74% | -0.47pp |
| PVS Attempt | 15,539 | 14,320 | -1,219 | -7.8% | 95.62% | 97.37% | +1.74pp |
| PVS Success | 13,853 | 12,997 | -856 | -6.2% | 89.15% | 90.76% | +1.61pp |
| **Successful Checkout** | 13,037 | 12,237 | -800 | -6.1% | 94.11% | 94.15% | +0.04pp |
| **PCR Rate** | | | | | 25.04% | 26.23% | **+1.19pp** |

### Payment Method Breakdown

| Payment Method | 2026-W20 Attempt | 2026-W20 Success | 2026-W20 Rate | 2026-W21 Attempt | 2026-W21 Success | 2026-W21 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 9,675 | 7,621 | 78.77% | 8,937 | 7,349 | 82.23% | +3.46pp |
| Braintree_ApplePay | 6,059 | 3,979 | 65.67% | 5,360 | 3,571 | 66.62% | +0.95pp |
| Braintree_Paypal | 1,462 | 1,214 | 83.04% | 1,316 | 1,103 | 83.81% | +0.78pp |
| Braintree_CreditCard | 259 | 222 | 85.71% | 247 | 212 | 85.83% | +0.12pp |
| visa | 25 | 0 | 0.00% | 30 | 1 | 3.33% | +3.33pp |
| mc | 8 | 0 | 0.00% | 13 | 0 | 0.00% | +0.00pp |
| amex | 4 | 0 | 0.00% | 10 | 0 | 0.00% | +0.00pp |
| paypal | 10 | 0 | 0.00% | 10 | 0 | 0.00% | +0.00pp |
| Adyen_CreditCard | 84 | 0 | 0.00% | 1 | 0 | 0.00% | +0.00pp |
| Braintree_Venmo | 1 | 1 | 100.00% | 1 | 1 | 100.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (1 countries in US-HF)

| Country | Volume | PCR 2026-W20 | PCR 2026-W21 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| US | 43,124 | 23.88% | 25.15% | +1.27pp | 1 | 1 |

---

### US

#### Waterfall GA

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 49,081 | 43,124 | -5,957 | -12.14pp | - | - | - |
| Select Payment Method | 17,721 | 16,159 | -1,562 | -8.81pp | 36.11% | 37.47% | +1.37pp |
| Click Submit Form | 15,544 | 14,066 | -1,478 | -9.51pp | 87.72% | 87.05% | -0.67pp |
| FE Validation Passed | 14,496 | 13,166 | -1,330 | -9.17pp | 93.26% | 93.60% | +0.34pp |
| Enter Fraud Service | 14,076 | 12,747 | -1,329 | -9.44pp | 97.10% | 96.82% | -0.29pp |
| Approved by Fraud Service | 13,352 | 11,972 | -1,380 | -10.34pp | 94.86% | 93.92% | -0.94pp |
| Call to PVS | 13,101 | 11,946 | -1,155 | -8.82pp | 98.12% | 99.78% | +1.66pp |
| **Successful Checkout** | 11,720 | 10,845 | -875 | -7.47pp | 89.46% | 90.78% | +1.32pp |
| **PCR Rate** | | | | | 23.88% | 25.15% | **+1.27pp** |

**Key Driver:** Call to PVS (+1.66pp)

#### Waterfall Backend

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 52,063 | 46,653 | -5,410 | -10.39pp | - | - | - |
| Checkout Attempt | 17,590 | 15,926 | -1,664 | -9.46pp | 33.79% | 34.14% | +0.35pp |
| Enter Fraud Service | 17,433 | 15,858 | -1,575 | -9.03pp | 99.11% | 99.57% | +0.47pp |
| Approved by Fraud Service | 16,250 | 14,707 | -1,543 | -9.50pp | 93.21% | 92.74% | -0.47pp |
| PVS Attempt | 15,539 | 14,320 | -1,219 | -7.84pp | 95.62% | 97.37% | +1.74pp |
| PVS Success | 13,853 | 12,997 | -856 | -6.18pp | 89.15% | 90.76% | +1.61pp |
| **Successful Checkout** | 14,296 | 13,335 | -961 | -6.72pp | 103.20% | 102.60% | -0.60pp |

**Key Driver:** PVS Attempt (+1.74pp)

---



## Fraud Analysis

**Include reason:** Approved Δ (-0.94pp) meets threshold (+0.63pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W20 | 2026-W20 % | 2026-W21 | 2026-W21 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 17,590 | - | 15,926 | - | -1,664 | -9.5% |
| Enter Fraud Service | 17,433 | - | 15,858 | - | -1,575 | -9.0% |
| **Gap (Skipped)** | **157** | **0.89%** | **68** | **0.43%** | **-89** | **-0.47pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W20 Gap | 2026-W20 % | 2026-W21 Gap | 2026-W21 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| ProcessOut_CreditCard | 43 | 26.9% | 60 | 58.8% | +17 | +31.95pp |
| Braintree_ApplePay | 20 | 12.5% | 31 | 30.4% | +11 | +17.89pp |
| Braintree_Paypal | 10 | 6.2% | 7 | 6.9% | -3 | +0.61pp |
| Braintree_CreditCard | 3 | 1.9% | 3 | 2.9% | 0 | +1.07pp |
| Adyen_CreditCard | 84 | 52.5% | 1 | 1.0% | -83 | -51.52pp |
| **Total** | **160** | **100%** | **102** | **100%** | **-58** | - |

*% of Gap = Payment Method Gap / Total Gap*

---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (+1.32pp) meets threshold (+0.63pp)

| Decline Reason | 2026-W20 | 2026-W20 % | 2026-W21 | 2026-W21 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Blocked Verification: Payment method is blocked due to business reasons | 690 | 45.3% | 640 | 53.4% | -50 | +8.10pp |
| Failed Verification: Insufficient Funds | 439 | 28.8% | 237 | 19.8% | -202 | -9.04pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 101 | 6.6% | 89 | 7.4% | -12 | +0.80pp |
| Failed Verification: Issuer or Cardholder has put a restriction on the card | 79 | 5.2% | 57 | 4.8% | -22 | -0.43pp |
| Failed Verification: Cannot Authorize at this time (Policy) | 36 | 2.4% | 31 | 2.6% | -5 | +0.22pp |
| Failed Verification: Card Issuer Declined CVV | 42 | 2.8% | 31 | 2.6% | -11 | -0.17pp |
| Failed Verification: Processor Declined - Fraud Suspected | 39 | 2.6% | 30 | 2.5% | -9 | -0.06pp |
| Failed Verification: Processor Declined | 31 | 2.0% | 29 | 2.4% | -2 | +0.38pp |
| Failed Verification: Declined | 45 | 3.0% | 28 | 2.3% | -17 | -0.62pp |
| Failed Verification: Closed Card | 22 | 1.4% | 27 | 2.3% | +5 | +0.81pp |
| **Total PVS Failures** | **1,524** | **100%** | **1,199** | **100%** | **-325** | - |

---


---

*Report: 2026-05-26*
