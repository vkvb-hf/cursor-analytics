# PCR Investigation: HF-NA 2026-W19

**Metric:** Payment Conversion Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 25.22% → 25.81% (+0.59pp)  
**Volume:** 65,553 payment visits  
**Threshold:** +0.30pp (0.5 × |Overall PCR Δ|)

## Executive Summary

**Overall:** Payment Conversion Rate improved by +0.59pp (25.22% → 25.81%) in HF-NA during 2026-W19, driven primarily by early funnel improvements in payment method selection despite downstream PVS challenges.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Above threshold | +0.79pp | ✅ |
| Click Submit Form | Above threshold | +0.85pp | ✅ |
| FE Validation Passed | Within threshold | -0.27pp | ✅ |
| Enter Fraud Service | Within threshold | -0.12pp | ✅ |
| Approved by Fraud Service | Within threshold | +0.06pp | ✅ |
| Call to PVS | Above threshold | +0.52pp | ✅ |
| Successful Checkout | Below threshold | -0.85pp | ⚠️ |

**Key Findings:**
- Early funnel strength: Select Payment Method (+0.79pp) and Click Submit Form (+0.85pp) drove overall PCR improvement, offsetting downstream losses
- PVS Success declined significantly in Backend data (-1.43pp), with "Insufficient Funds" errors increasing by +138 cases (+4.82pp share), indicating potential economic or card funding issues
- CA outperformed US with +0.82pp PCR improvement vs +0.58pp, primarily driven by Click Submit Form (+1.60pp) gains
- US experienced notable PVS Success degradation (-1.53pp in Backend), contributing to the regional PVS challenges
- ProcessOut_CreditCard, the dominant payment method (55% of volume), declined by -1.27pp in success rate, while Braintree_Paypal improved by +2.54pp

**Action:** Monitor - The positive PCR trend is healthy, but the increasing "Insufficient Funds" errors (+138 cases) and PVS Success decline warrant continued observation. If PVS degradation persists next week, escalate to Payment Operations.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 69,233 | 65,553 | -3,680 | -5.3% | - | - | - |
| Select Payment Method | 26,381 | 25,496 | -885 | -3.4% | 38.10% | 38.89% | +0.79pp |
| Click Submit Form | 22,453 | 21,916 | -537 | -2.4% | 85.11% | 85.96% | +0.85pp |
| FE Validation Passed | 21,110 | 20,547 | -563 | -2.7% | 94.02% | 93.75% | -0.27pp |
| Enter Fraud Service | 20,403 | 19,835 | -568 | -2.8% | 96.65% | 96.53% | -0.12pp |
| Approved by Fraud Service | 19,351 | 18,824 | -527 | -2.7% | 94.84% | 94.90% | +0.06pp |
| Call to PVS | 18,838 | 18,423 | -415 | -2.2% | 97.35% | 97.87% | +0.52pp |
| **Successful Checkout** | 17,463 | 16,922 | -541 | -3.1% | 92.70% | 91.85% | -0.85pp |
| **PCR Rate** | | | | | 25.22% | 25.81% | **+0.59pp** |

### Waterfall Backend

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 74,056 | 70,781 | -3,275 | -4.4% | - | - | - |
| Checkout Attempt | 25,307 | 25,004 | -303 | -1.2% | 34.17% | 35.33% | +1.15pp |
| Enter Fraud Service | 25,100 | 24,725 | -375 | -1.5% | 99.18% | 98.88% | -0.30pp |
| Approved by Fraud Service | 23,155 | 22,692 | -463 | -2.0% | 92.25% | 91.78% | -0.47pp |
| PVS Attempt | 21,205 | 20,728 | -477 | -2.2% | 91.58% | 91.34% | -0.23pp |
| PVS Success | 19,605 | 18,867 | -738 | -3.8% | 92.45% | 91.02% | -1.43pp |
| **Successful Checkout** | 19,995 | 19,648 | -347 | -1.7% | 101.99% | 104.14% | +2.15pp |
| **PCR Rate** | | | | | 27.00% | 27.76% | **+0.76pp** |

### Payment Method Breakdown

| Payment Method | 2026-W18 Attempt | 2026-W18 Success | 2026-W18 Rate | 2026-W19 Attempt | 2026-W19 Success | 2026-W19 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 13,963 | 11,207 | 80.26% | 13,865 | 10,952 | 78.99% | -1.27pp |
| Braintree_ApplePay | 8,075 | 6,159 | 76.27% | 7,715 | 5,910 | 76.60% | +0.33pp |
| Braintree_Paypal | 2,176 | 1,796 | 82.54% | 2,064 | 1,756 | 85.08% | +2.54pp |
| Adyen_CreditCard | 717 | 564 | 78.66% | 909 | 687 | 75.58% | -3.08pp |
| Braintree_CreditCard | 312 | 266 | 85.26% | 398 | 341 | 85.68% | +0.42pp |
| visa | 0 | 0 | 0.00% | 19 | 0 | 0.00% | +0.00pp |
| paypal | 0 | 0 | 0.00% | 9 | 0 | 0.00% | +0.00pp |
| mc | 0 | 0 | 0.00% | 8 | 2 | 25.00% | +25.00pp |
|  | 52 | 0 | 0.00% | 7 | 0 | 0.00% | +0.00pp |
| NoPayment | 9 | 0 | 0.00% | 7 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (2 countries in HF-NA)

| Country | Volume | PCR 2026-W18 | PCR 2026-W19 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| US | 51,440 | 23.37% | 23.95% | +0.58pp | 1 | 2 |
| CA | 14,113 | 31.80% | 32.62% | +0.82pp | 2 | 1 |

---

### US

#### Waterfall GA

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 54,042 | 51,440 | -2,602 | -4.81pp | - | - | - |
| Select Payment Method | 18,879 | 18,520 | -359 | -1.90pp | 34.93% | 36.00% | +1.07pp |
| Click Submit Form | 16,481 | 16,251 | -230 | -1.40pp | 87.30% | 87.75% | +0.45pp |
| FE Validation Passed | 15,487 | 15,211 | -276 | -1.78pp | 93.97% | 93.60% | -0.37pp |
| Enter Fraud Service | 14,996 | 14,678 | -318 | -2.12pp | 96.83% | 96.50% | -0.33pp |
| Approved by Fraud Service | 14,290 | 13,973 | -317 | -2.22pp | 95.29% | 95.20% | -0.10pp |
| Call to PVS | 13,876 | 13,667 | -209 | -1.51pp | 97.10% | 97.81% | +0.71pp |
| **Successful Checkout** | 12,632 | 12,318 | -314 | -2.49pp | 91.03% | 90.13% | -0.91pp |
| **PCR Rate** | | | | | 23.37% | 23.95% | **+0.57pp** |

**Key Driver:** Select Payment Method (+1.07pp)

#### Waterfall Backend

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 58,098 | 56,039 | -2,059 | -3.54pp | - | - | - |
| Checkout Attempt | 18,914 | 18,985 | +71 | +0.38pp | 32.56% | 33.88% | +1.32pp |
| Enter Fraud Service | 18,752 | 18,741 | -11 | -0.06pp | 99.14% | 98.71% | -0.43pp |
| Approved by Fraud Service | 17,404 | 17,218 | -186 | -1.07pp | 92.81% | 91.87% | -0.94pp |
| PVS Attempt | 16,396 | 16,324 | -72 | -0.44pp | 94.21% | 94.81% | +0.60pp |
| PVS Success | 14,942 | 14,627 | -315 | -2.11pp | 91.13% | 89.60% | -1.53pp |
| **Successful Checkout** | 15,428 | 15,313 | -115 | -0.75pp | 103.25% | 104.69% | +1.44pp |

**Key Driver:** PVS Success (-1.53pp)

---

### CA

#### Waterfall GA

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 15,191 | 14,113 | -1,078 | -7.10pp | - | - | - |
| Select Payment Method | 7,502 | 6,976 | -526 | -7.01pp | 49.38% | 49.43% | +0.05pp |
| Click Submit Form | 5,972 | 5,665 | -307 | -5.14pp | 79.61% | 81.21% | +1.60pp |
| FE Validation Passed | 5,623 | 5,336 | -287 | -5.10pp | 94.16% | 94.19% | +0.04pp |
| Enter Fraud Service | 5,407 | 5,157 | -250 | -4.62pp | 96.16% | 96.65% | +0.49pp |
| Approved by Fraud Service | 5,061 | 4,851 | -210 | -4.15pp | 93.60% | 94.07% | +0.47pp |
| Call to PVS | 4,962 | 4,756 | -206 | -4.15pp | 98.04% | 98.04% | -0.00pp |
| **Successful Checkout** | 4,831 | 4,604 | -227 | -4.70pp | 97.36% | 96.80% | -0.56pp |
| **PCR Rate** | | | | | 31.80% | 32.62% | **+0.82pp** |

**Key Driver:** Click Submit Form (+1.60pp)

#### Waterfall Backend

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 15,958 | 14,742 | -1,216 | -7.62pp | - | - | - |
| Checkout Attempt | 6,393 | 6,019 | -374 | -5.85pp | 40.06% | 40.83% | +0.77pp |
| Enter Fraud Service | 6,348 | 5,984 | -364 | -5.73pp | 99.30% | 99.42% | +0.12pp |
| Approved by Fraud Service | 5,751 | 5,474 | -277 | -4.82pp | 90.60% | 91.48% | +0.88pp |
| PVS Attempt | 4,809 | 4,404 | -405 | -8.42pp | 83.62% | 80.45% | -3.17pp |
| PVS Success | 4,663 | 4,240 | -423 | -9.07pp | 96.96% | 96.28% | -0.69pp |
| **Successful Checkout** | 5,505 | 5,263 | -242 | -4.40pp | 118.06% | 124.13% | +6.07pp |

**Key Driver:** Successful Checkout (+6.07pp)

---



## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (-0.85pp) meets threshold (+0.30pp)

| Decline Reason | 2026-W18 | 2026-W18 % | 2026-W19 | 2026-W19 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Blocked Verification: Payment method is blocked due to business reasons | 678 | 50.2% | 736 | 45.7% | +58 | -4.51pp |
| Failed Verification: Insufficient Funds | 314 | 23.3% | 452 | 28.1% | +138 | +4.82pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 117 | 8.7% | 112 | 7.0% | -5 | -1.71pp |
| Failed Verification: Issuer or Cardholder has put a restriction on the card | 54 | 4.0% | 76 | 4.7% | +22 | +0.72pp |
| Failed Verification: Declined - Call Issuer | 40 | 3.0% | 44 | 2.7% | +4 | -0.23pp |
| Failed Verification: Card Issuer Declined CVV | 52 | 3.9% | 43 | 2.7% | -9 | -1.18pp |
| Failed Verification: Processor Declined - Fraud Suspected | 30 | 2.2% | 41 | 2.5% | +11 | +0.32pp |
| Failed Verification: Declined | 27 | 2.0% | 37 | 2.3% | +10 | +0.30pp |
| Failed Verification: OK: 51 : Insufficient funds/over credit limit | 17 | 1.3% | 35 | 2.2% | +18 | +0.91pp |
| Failed Verification: Processor Declined | 21 | 1.6% | 34 | 2.1% | +13 | +0.56pp |
| **Total PVS Failures** | **1,350** | **100%** | **1,610** | **100%** | **+260** | - |

---


---

*Report: 2026-05-12*
