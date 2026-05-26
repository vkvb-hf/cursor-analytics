# PCR Investigation: HF-NA 2026-W21

**Metric:** Payment Conversion Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 25.93% → 27.38% (+1.45pp)  
**Volume:** 56,777 payment visits  
**Threshold:** +0.73pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate improved significantly from 25.93% to 27.38% (+1.45pp) in 2026-W21, exceeding the threshold of +0.73pp, driven primarily by improvements in payment method selection and successful checkout steps.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ≥ threshold | +1.73pp | ✅ |
| Click Submit Form | < threshold | -1.01pp | ⚠️ |
| FE Validation Passed | < threshold | +0.23pp | ✅ |
| Enter Fraud Service | < threshold | -0.30pp | ✅ |
| Approved by Fraud Service | < threshold | -0.53pp | ✅ |
| Call to PVS | ≥ threshold | +1.38pp | ✅ |
| Successful Checkout | ≥ threshold | +1.43pp | ✅ |

**Key Findings:**
- ProcessOut_CreditCard success rate improved significantly from 79.83% to 83.54% (+3.71pp), representing the largest volume payment method with 12,075 attempts
- Adyen_CreditCard showed exceptional improvement from 79.58% to 92.13% (+12.55pp), though with lower volume (699 attempts)
- PVS failures decreased substantially from 1,567 to 1,243 (-324 failures), with "Insufficient Funds" declines dropping by 198 cases (-8.33pp share)
- US showed strong improvement in Call to PVS step (+1.66pp) and PVS Success (+1.61pp in backend)
- CA experienced growth in payment visits (+632) while maintaining conversion improvements, with PVS Attempt improving +4.01pp in backend

**Action:** Monitor - The positive trend across multiple funnel steps and payment methods suggests healthy performance. Continue monitoring the Click Submit Form step (-1.01pp) to ensure the slight decline does not worsen.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 62,102 | 56,777 | -5,325 | -8.6% | - | - | - |
| Select Payment Method | 24,394 | 23,285 | -1,109 | -4.5% | 39.28% | 41.01% | +1.73pp |
| Click Submit Form | 20,946 | 19,759 | -1,187 | -5.7% | 85.87% | 84.86% | -1.01pp |
| FE Validation Passed | 19,550 | 18,488 | -1,062 | -5.4% | 93.34% | 93.57% | +0.23pp |
| Enter Fraud Service | 18,986 | 17,899 | -1,087 | -5.7% | 97.12% | 96.81% | -0.30pp |
| Approved by Fraud Service | 17,953 | 16,830 | -1,123 | -6.3% | 94.56% | 94.03% | -0.53pp |
| Call to PVS | 17,620 | 16,750 | -870 | -4.9% | 98.15% | 99.52% | +1.38pp |
| **Successful Checkout** | 16,100 | 15,544 | -556 | -3.5% | 91.37% | 92.80% | +1.43pp |
| **PCR Rate** | | | | | 25.93% | 27.38% | **+1.45pp** |

### Waterfall Backend

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 65,525 | 60,874 | -4,651 | -7.1% | - | - | - |
| Checkout Attempt | 23,339 | 21,892 | -1,447 | -6.2% | 35.62% | 35.96% | +0.34pp |
| Enter Fraud Service | 23,112 | 21,785 | -1,327 | -5.7% | 99.03% | 99.51% | +0.48pp |
| Approved by Fraud Service | 21,459 | 20,192 | -1,267 | -5.9% | 92.85% | 92.69% | -0.16pp |
| PVS Attempt | 19,621 | 18,838 | -783 | -4.0% | 91.43% | 93.29% | +1.86pp |
| PVS Success | 17,792 | 17,395 | -397 | -2.2% | 90.68% | 92.34% | +1.66pp |
| **Successful Checkout** | 17,775 | 17,327 | -448 | -2.5% | 99.90% | 99.61% | -0.30pp |
| **PCR Rate** | | | | | 27.13% | 28.46% | **+1.34pp** |

### Payment Method Breakdown

| Payment Method | 2026-W20 Attempt | 2026-W20 Success | 2026-W20 Rate | 2026-W21 Attempt | 2026-W21 Success | 2026-W21 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 12,623 | 10,077 | 79.83% | 12,075 | 10,087 | 83.54% | +3.71pp |
| Braintree_ApplePay | 7,426 | 5,006 | 67.41% | 6,787 | 4,684 | 69.01% | +1.60pp |
| Braintree_Paypal | 2,067 | 1,752 | 84.76% | 1,998 | 1,698 | 84.98% | +0.22pp |
| Adyen_CreditCard | 901 | 717 | 79.58% | 699 | 644 | 92.13% | +12.55pp |
| Braintree_CreditCard | 259 | 222 | 85.71% | 247 | 212 | 85.83% | +0.12pp |
| visa | 25 | 0 | 0.00% | 30 | 1 | 3.33% | +3.33pp |
| NoPayment | 12 | 0 | 0.00% | 21 | 0 | 0.00% | +0.00pp |
| mc | 8 | 0 | 0.00% | 13 | 0 | 0.00% | +0.00pp |
| amex | 4 | 0 | 0.00% | 10 | 0 | 0.00% | +0.00pp |
| paypal | 10 | 0 | 0.00% | 10 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (2 countries in HF-NA)

| Country | Volume | PCR 2026-W20 | PCR 2026-W21 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| US | 43,124 | 23.88% | 25.15% | +1.27pp | 1 | 1 |
| CA | 13,653 | 33.64% | 34.42% | +0.78pp | 2 | 2 |

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

### CA

#### Waterfall GA

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 13,021 | 13,653 | +632 | +4.85pp | - | - | - |
| Select Payment Method | 6,673 | 7,126 | +453 | +6.79pp | 51.25% | 52.19% | +0.95pp |
| Click Submit Form | 5,402 | 5,693 | +291 | +5.39pp | 80.95% | 79.89% | -1.06pp |
| FE Validation Passed | 5,054 | 5,322 | +268 | +5.30pp | 93.56% | 93.48% | -0.07pp |
| Enter Fraud Service | 4,910 | 5,152 | +242 | +4.93pp | 97.15% | 96.81% | -0.35pp |
| Approved by Fraud Service | 4,601 | 4,858 | +257 | +5.59pp | 93.71% | 94.29% | +0.59pp |
| Call to PVS | 4,519 | 4,804 | +285 | +6.31pp | 98.22% | 98.89% | +0.67pp |
| **Successful Checkout** | 4,380 | 4,699 | +319 | +7.28pp | 96.92% | 97.81% | +0.89pp |
| **PCR Rate** | | | | | 33.64% | 34.42% | **+0.78pp** |

**Key Driver:** Click Submit Form (-1.06pp)

#### Waterfall Backend

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 13,462 | 14,221 | +759 | +5.64pp | - | - | - |
| Checkout Attempt | 5,749 | 5,966 | +217 | +3.77pp | 42.71% | 41.95% | -0.75pp |
| Enter Fraud Service | 5,679 | 5,927 | +248 | +4.37pp | 98.78% | 99.35% | +0.56pp |
| Approved by Fraud Service | 5,209 | 5,485 | +276 | +5.30pp | 91.72% | 92.54% | +0.82pp |
| PVS Attempt | 4,082 | 4,518 | +436 | +10.68pp | 78.36% | 82.37% | +4.01pp |
| PVS Success | 3,939 | 4,398 | +459 | +11.65pp | 96.50% | 97.34% | +0.85pp |
| **Successful Checkout** | 5,039 | 5,356 | +317 | +6.29pp | 127.93% | 121.78% | -6.14pp |

**Key Driver:** Successful Checkout (-6.14pp)

---



## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (+1.43pp) meets threshold (+0.73pp)

| Decline Reason | 2026-W20 | 2026-W20 % | 2026-W21 | 2026-W21 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Blocked Verification: Payment method is blocked due to business reasons | 690 | 44.0% | 640 | 51.5% | -50 | +7.46pp |
| Failed Verification: Insufficient Funds | 457 | 29.2% | 259 | 20.8% | -198 | -8.33pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 117 | 7.5% | 104 | 8.4% | -13 | +0.90pp |
| Failed Verification: Issuer or Cardholder has put a restriction on the card | 79 | 5.0% | 58 | 4.7% | -21 | -0.38pp |
| Failed Verification: Cannot Authorize at this time (Policy) | 36 | 2.3% | 33 | 2.7% | -3 | +0.36pp |
| Failed Verification: Card Issuer Declined CVV | 42 | 2.7% | 31 | 2.5% | -11 | -0.19pp |
| Failed Verification: Declined | 52 | 3.3% | 31 | 2.5% | -21 | -0.82pp |
| Failed Verification: Processor Declined - Fraud Suspected | 40 | 2.6% | 31 | 2.5% | -9 | -0.06pp |
| Failed Verification: Processor Declined | 32 | 2.0% | 29 | 2.3% | -3 | +0.29pp |
| Failed Verification: Closed Card | 22 | 1.4% | 27 | 2.2% | +5 | +0.77pp |
| **Total PVS Failures** | **1,567** | **100%** | **1,243** | **100%** | **-324** | - |

---


---

*Report: 2026-05-26*
