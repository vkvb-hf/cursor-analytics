# PCR Investigation: US-HF 2026-W20

**Metric:** Payment Conversion Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 23.95% → 23.88% (-0.07pp)  
**Volume:** 49,081 payment visits  
**Threshold:** +0.03pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined slightly from 23.95% to 23.88% (-0.07pp) in US-HF for 2026-W20, with payment visits down 4.6% (49,081 visits).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Within threshold | +0.10pp | ✅ |
| Click Submit Form | Within threshold | -0.03pp | ✅ |
| FE Validation Passed | Exceeds threshold | -0.34pp | ⚠️ |
| Enter Fraud Service | Exceeds threshold | +0.61pp | ✅ |
| Approved by Fraud Service | Exceeds threshold | -0.41pp | ⚠️ |
| Call to PVS | Exceeds threshold | +0.38pp | ✅ |
| Successful Checkout | Exceeds threshold | -0.67pp | ⚠️ |

**Key Findings:**
- **Braintree_ApplePay experienced severe degradation:** Success rate dropped from 74.41% to 65.67% (-8.74pp), making it the primary driver of PCR decline despite representing ~35% of payment attempts
- **Successful Checkout step shows largest impact:** GA funnel shows -0.67pp conversion drop at final checkout, while Backend shows -4.99pp drop from PVS Success to Successful Checkout
- **FE Validation errors increased:** "terms_not_accepted" errors rose from 51.8% to 55.5% (+3.76pp) of error share, though overall recovery rate improved slightly (+0.60pp)
- **Fraud service approval declined:** -0.41pp drop in approval rate despite improved entry rate (+0.61pp), indicating stricter fraud filtering
- **Adyen_CreditCard and legacy payment methods remain non-functional:** 0% success rate persists for Adyen_CreditCard (84 attempts) and direct card brand entries (visa, paypal, mc, amex)

**Action:** **Investigate** - Prioritize root cause analysis for Braintree_ApplePay's -8.74pp success rate decline, as this single payment method is driving the majority of the PCR degradation.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 51,443 | 49,081 | -2,362 | -4.6% | - | - | - |
| Select Payment Method | 18,523 | 17,721 | -802 | -4.3% | 36.01% | 36.11% | +0.10pp |
| Click Submit Form | 16,253 | 15,544 | -709 | -4.4% | 87.74% | 87.72% | -0.03pp |
| FE Validation Passed | 15,213 | 14,496 | -717 | -4.7% | 93.60% | 93.26% | -0.34pp |
| Enter Fraud Service | 14,680 | 14,076 | -604 | -4.1% | 96.50% | 97.10% | +0.61pp |
| Approved by Fraud Service | 13,982 | 13,349 | -633 | -4.5% | 95.25% | 94.84% | -0.41pp |
| Call to PVS | 13,669 | 13,101 | -568 | -4.2% | 97.76% | 98.14% | +0.38pp |
| **Successful Checkout** | 12,320 | 11,720 | -600 | -4.9% | 90.13% | 89.46% | -0.67pp |
| **PCR Rate** | | | | | 23.95% | 23.88% | **-0.07pp** |

### Waterfall Backend

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 56,039 | 52,063 | -3,976 | -7.1% | - | - | - |
| Checkout Attempt | 18,985 | 17,590 | -1,395 | -7.3% | 33.88% | 33.79% | -0.09pp |
| Enter Fraud Service | 18,741 | 17,433 | -1,308 | -7.0% | 98.71% | 99.11% | +0.39pp |
| Approved by Fraud Service | 17,218 | 16,250 | -968 | -5.6% | 91.87% | 93.21% | +1.34pp |
| PVS Attempt | 16,324 | 15,539 | -785 | -4.8% | 94.81% | 95.62% | +0.82pp |
| PVS Success | 14,627 | 13,853 | -774 | -5.3% | 89.60% | 89.15% | -0.45pp |
| **Successful Checkout** | 14,496 | 13,037 | -1,459 | -10.1% | 99.10% | 94.11% | -4.99pp |
| **PCR Rate** | | | | | 25.87% | 25.04% | **-0.83pp** |

### Payment Method Breakdown

| Payment Method | 2026-W19 Attempt | 2026-W19 Success | 2026-W19 Rate | 2026-W20 Attempt | 2026-W20 Success | 2026-W20 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 10,651 | 8,250 | 77.46% | 9,675 | 7,621 | 78.77% | +1.31pp |
| Braintree_ApplePay | 6,225 | 4,632 | 74.41% | 6,059 | 3,979 | 65.67% | -8.74pp |
| Braintree_Paypal | 1,522 | 1,271 | 83.51% | 1,462 | 1,214 | 83.04% | -0.47pp |
| Braintree_CreditCard | 398 | 341 | 85.68% | 259 | 222 | 85.71% | +0.04pp |
| Adyen_CreditCard | 143 | 0 | 0.00% | 84 | 0 | 0.00% | +0.00pp |
| visa | 19 | 0 | 0.00% | 25 | 0 | 0.00% | +0.00pp |
| paypal | 9 | 0 | 0.00% | 10 | 0 | 0.00% | +0.00pp |
| mc | 8 | 2 | 25.00% | 8 | 0 | 0.00% | -25.00pp |
| amex | 3 | 0 | 0.00% | 4 | 0 | 0.00% | +0.00pp |
| discover | 0 | 0 | 0.00% | 3 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (1 countries in US-HF)

| Country | Volume | PCR 2026-W19 | PCR 2026-W20 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| US | 49,081 | 23.95% | 23.88% | -0.07pp | 1 | 1 |

---

### US

#### Waterfall GA

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 51,443 | 49,081 | -2,362 | -4.59pp | - | - | - |
| Select Payment Method | 18,523 | 17,721 | -802 | -4.33pp | 36.01% | 36.11% | +0.10pp |
| Click Submit Form | 16,253 | 15,544 | -709 | -4.36pp | 87.74% | 87.72% | -0.03pp |
| FE Validation Passed | 15,213 | 14,496 | -717 | -4.71pp | 93.60% | 93.26% | -0.34pp |
| Enter Fraud Service | 14,680 | 14,076 | -604 | -4.11pp | 96.50% | 97.10% | +0.61pp |
| Approved by Fraud Service | 13,982 | 13,349 | -633 | -4.53pp | 95.25% | 94.84% | -0.41pp |
| Call to PVS | 13,669 | 13,101 | -568 | -4.16pp | 97.76% | 98.14% | +0.38pp |
| **Successful Checkout** | 12,320 | 11,720 | -600 | -4.87pp | 90.13% | 89.46% | -0.67pp |
| **PCR Rate** | | | | | 23.95% | 23.88% | **-0.07pp** |

**Key Driver:** Successful Checkout (-0.67pp)

#### Waterfall Backend

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 56,039 | 52,063 | -3,976 | -7.10pp | - | - | - |
| Checkout Attempt | 18,985 | 17,590 | -1,395 | -7.35pp | 33.88% | 33.79% | -0.09pp |
| Enter Fraud Service | 18,741 | 17,433 | -1,308 | -6.98pp | 98.71% | 99.11% | +0.39pp |
| Approved by Fraud Service | 17,218 | 16,250 | -968 | -5.62pp | 91.87% | 93.21% | +1.34pp |
| PVS Attempt | 16,324 | 15,539 | -785 | -4.81pp | 94.81% | 95.62% | +0.82pp |
| PVS Success | 14,627 | 13,853 | -774 | -5.29pp | 89.60% | 89.15% | -0.45pp |
| **Successful Checkout** | 15,313 | 14,296 | -1,017 | -6.64pp | 104.69% | 103.20% | -1.49pp |

**Key Driver:** Successful Checkout (-1.49pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (-0.34pp) meets threshold (+0.03pp)

### Recovery Rate

| Metric | 2026-W19 | 2026-W20 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 4,252 | 4,247 | -5 |
| Error → Passed | 3,045 | 3,067 | 22 |
| **Recovery Rate** | **71.61%** | **72.22%** | **+0.60pp** |

### Error Type Distribution

| Error Type | 2026-W19 | 2026-W19 % | 2026-W20 | 2026-W20 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| terms_not_accepted | 2,202 | 51.8% | 2,359 | 55.5% | +3.76pp |
| APPLEPAY_DISMISSED | 2,248 | 52.9% | 2,180 | 51.3% | -1.54pp |
| PAYPAL_POPUP_CLOSED | 313 | 7.4% | 336 | 7.9% | +0.55pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 219 | 5.2% | 227 | 5.3% | +0.19pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 137 | 3.2% | 119 | 2.8% | -0.42pp |
| CC_TOKENISE_ERR | 123 | 2.9% | 114 | 2.7% | -0.21pp |
| PAYPAL_TOKENISE_ERR | 36 | 0.8% | 40 | 0.9% | +0.10pp |
| CC_NO_PREPAID_ERR | 7 | 0.2% | 8 | 0.2% | +0.02pp |
| APPLEPAY_MERCHANT_VALIDATION_ERR | 2 | 0.0% | 3 | 0.1% | +0.02pp |


---

## Fraud Analysis

**Include reason:** Enter FS Δ (+0.61pp) meets threshold (+0.03pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W19 | 2026-W19 % | 2026-W20 | 2026-W20 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 18,985 | - | 17,590 | - | -1,395 | -7.3% |
| Enter Fraud Service | 18,741 | - | 17,433 | - | -1,308 | -7.0% |
| **Gap (Skipped)** | **244** | **1.29%** | **157** | **0.89%** | **-87** | **-0.39pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W19 Gap | 2026-W19 % | 2026-W20 Gap | 2026-W20 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Adyen_CreditCard | 143 | 57.9% | 84 | 52.5% | -59 | -5.39pp |
| ProcessOut_CreditCard | 66 | 26.7% | 43 | 26.9% | -23 | +0.15pp |
| Braintree_ApplePay | 27 | 10.9% | 20 | 12.5% | -7 | +1.57pp |
| Braintree_Paypal | 10 | 4.0% | 10 | 6.2% | 0 | +2.20pp |
| Braintree_CreditCard | 1 | 0.4% | 3 | 1.9% | +2 | +1.47pp |
| **Total** | **247** | **100%** | **160** | **100%** | **-87** | - |

*% of Gap = Payment Method Gap / Total Gap*

---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (-0.67pp) meets threshold (+0.03pp)

| Decline Reason | 2026-W19 | 2026-W19 % | 2026-W20 | 2026-W20 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Blocked Verification: Payment method is blocked due to business reasons | 736 | 47.4% | 690 | 44.6% | -46 | -2.73pp |
| Failed Verification: Insufficient Funds | 431 | 27.7% | 439 | 28.4% | +8 | +0.66pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 97 | 6.2% | 101 | 6.5% | +4 | +0.29pp |
| Failed Verification: Issuer or Cardholder has put a restriction on the card | 76 | 4.9% | 79 | 5.1% | +3 | +0.22pp |
| Failed Verification: Declined | 32 | 2.1% | 45 | 2.9% | +13 | +0.85pp |
| Failed Verification: Declined - Call Issuer | 44 | 2.8% | 44 | 2.8% | 0 | +0.01pp |
| Failed Verification: Card Issuer Declined CVV | 43 | 2.8% | 42 | 2.7% | -1 | -0.05pp |
| Failed Verification: Processor Declined - Fraud Suspected | 39 | 2.5% | 39 | 2.5% | 0 | +0.01pp |
| Failed Verification: Cannot Authorize at this time (Policy) | 22 | 1.4% | 36 | 2.3% | +14 | +0.91pp |
| Failed Verification: Processor Declined | 34 | 2.2% | 31 | 2.0% | -3 | -0.18pp |
| **Total PVS Failures** | **1,554** | **100%** | **1,546** | **100%** | **-8** | - |

---


---

*Report: 2026-05-19*
