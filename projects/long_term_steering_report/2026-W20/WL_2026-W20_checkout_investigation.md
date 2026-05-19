# PCR Investigation: WL 2026-W20

**Metric:** Payment Conversion Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 29.33% → 29.38% (+0.05pp)  
**Volume:** 37,426 payment visits  
**Threshold:** +0.03pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate showed a marginal improvement of +0.05pp (29.33% → 29.38%) on 37,426 payment visits, with mixed performance across funnel steps and countries.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ≥ threshold | +0.38pp | ✅ |
| Click Submit Form | ≥ threshold | +0.28pp | ✅ |
| FE Validation Passed | < threshold | -0.76pp | ⚠️ |
| Enter Fraud Service | ≥ threshold | +0.51pp | ✅ |
| Approved by Fraud Service | < threshold | -0.33pp | ⚠️ |
| Call to PVS | < threshold | -0.63pp | ⚠️ |
| Successful Checkout | ≥ threshold | +0.17pp | ✅ |

**Key Findings:**
- **FE Validation degradation (-0.76pp):** Recovery rate dropped from 59.98% to 57.32% (-2.66pp), with APPLEPAY_DISMISSED errors increasing (+0.93pp share) and CC_TOKENISE_ERR growing (+0.51pp share)
- **Country divergence:** AO improved significantly (+4.13pp PCR) driven by Select Payment Method (+5.66pp), while MR declined sharply (-2.05pp PCR) with the same step being the key driver (-2.05pp)
- **Call to PVS gap (-0.63pp):** Notable decline in the handoff between Fraud Service approval and PVS calls, particularly impacting MR (-1.07pp) and AO (-3.10pp)
- **Payment method performance mixed:** Adyen_CreditCard declined -1.87pp and ProcessOut_ApplePay dropped -3.96pp, while ProcessOut_CreditCard improved +0.93pp
- **Fraud skip rate slightly increased:** Gap between Checkout Attempt and Enter Fraud Service grew from 0.76% to 0.87%, with ProcessOut_CreditCard showing the largest increase (+9 skipped transactions)

**Action:** **Monitor** - Overall PCR remains stable with minimal change (+0.05pp). Continue monitoring FE Validation recovery rates and the MR country performance decline. If FE Validation degradation persists next week, escalate for technical investigation of ApplePay and credit card tokenization errors.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 39,754 | 37,426 | -2,328 | -5.9% | - | - | - |
| Select Payment Method | 15,957 | 15,164 | -793 | -5.0% | 40.14% | 40.52% | +0.38pp |
| Click Submit Form | 14,106 | 13,448 | -658 | -4.7% | 88.40% | 88.68% | +0.28pp |
| FE Validation Passed | 13,509 | 12,777 | -732 | -5.4% | 95.77% | 95.01% | -0.76pp |
| Enter Fraud Service | 12,949 | 12,312 | -637 | -4.9% | 95.85% | 96.36% | +0.51pp |
| Approved by Fraud Service | 12,280 | 11,635 | -645 | -5.3% | 94.83% | 94.50% | -0.33pp |
| Call to PVS | 12,149 | 11,438 | -711 | -5.9% | 98.93% | 98.31% | -0.63pp |
| **Successful Checkout** | 11,659 | 10,996 | -663 | -5.7% | 95.97% | 96.14% | +0.17pp |
| **PCR Rate** | | | | | 29.33% | 29.38% | **+0.05pp** |

### Waterfall Backend

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 46,798 | 44,052 | -2,746 | -5.9% | - | - | - |
| Checkout Attempt | 14,652 | 13,909 | -743 | -5.1% | 31.31% | 31.57% | +0.27pp |
| Enter Fraud Service | 14,541 | 13,788 | -753 | -5.2% | 99.24% | 99.13% | -0.11pp |
| Approved by Fraud Service | 13,543 | 12,860 | -683 | -5.0% | 93.14% | 93.27% | +0.13pp |
| PVS Attempt | 10,480 | 10,330 | -150 | -1.4% | 77.38% | 80.33% | +2.94pp |
| PVS Success | 9,985 | 9,878 | -107 | -1.1% | 95.28% | 95.62% | +0.35pp |
| **Successful Checkout** | 13,026 | 12,283 | -743 | -5.7% | 130.46% | 124.35% | -6.11pp |
| **PCR Rate** | | | | | 27.83% | 27.88% | **+0.05pp** |

### Payment Method Breakdown

| Payment Method | 2026-W19 Attempt | 2026-W19 Success | 2026-W19 Rate | 2026-W20 Attempt | 2026-W20 Success | 2026-W20 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| Braintree_ApplePay | 4,130 | 3,746 | 90.70% | 3,979 | 3,568 | 89.67% | -1.03pp |
| ProcessOut_CreditCard | 4,246 | 3,703 | 87.21% | 3,617 | 3,188 | 88.14% | +0.93pp |
| Adyen_CreditCard | 2,709 | 2,434 | 89.85% | 2,686 | 2,363 | 87.97% | -1.87pp |
| Braintree_Paypal | 1,841 | 1,677 | 91.09% | 1,767 | 1,598 | 90.44% | -0.66pp |
| Braintree_CreditCard | 1,478 | 1,246 | 84.30% | 1,562 | 1,314 | 84.12% | -0.18pp |
| ProcessOut_ApplePay | 245 | 219 | 89.39% | 295 | 252 | 85.42% | -3.96pp |
| NoPayment | 2 | 0 | 0.00% | 3 | 0 | 0.00% | +0.00pp |
| Braintree_Venmo | 1 | 1 | 100.00% | 0 | 0 | 0.00% | -100.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (3 countries in WL)

| Country | Volume | PCR 2026-W19 | PCR 2026-W20 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| MR | 8,924 | 25.07% | 23.02% | -2.05pp | 1 | 3 |
| CK | 4,289 | 41.55% | 43.62% | +2.07pp | 2 | 2 |
| AO | 1,436 | 41.48% | 45.61% | +4.13pp | 4 | 1 |

---

### AO

#### Waterfall GA

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 1,355 | 1,436 | +81 | +5.98pp | - | - | - |
| Select Payment Method | 749 | 875 | +126 | +16.82pp | 55.28% | 60.93% | +5.66pp |
| Click Submit Form | 682 | 818 | +136 | +19.94pp | 91.05% | 93.49% | +2.43pp |
| FE Validation Passed | 662 | 793 | +131 | +19.79pp | 97.07% | 96.94% | -0.12pp |
| Enter Fraud Service | 645 | 779 | +134 | +20.78pp | 97.43% | 98.23% | +0.80pp |
| Approved by Fraud Service | 596 | 710 | +114 | +19.13pp | 92.40% | 91.14% | -1.26pp |
| Call to PVS | 596 | 688 | +92 | +15.44pp | 100.00% | 96.90% | -3.10pp |
| **Successful Checkout** | 562 | 655 | +93 | +16.55pp | 94.30% | 95.20% | +0.91pp |
| **PCR Rate** | | | | | 41.48% | 45.61% | **+4.14pp** |

**Key Driver:** Select Payment Method (+5.66pp)

#### Waterfall Backend

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 1,687 | 1,778 | +91 | +5.39pp | - | - | - |
| Checkout Attempt | 710 | 878 | +168 | +23.66pp | 42.09% | 49.38% | +7.29pp |
| Enter Fraud Service | 708 | 878 | +170 | +24.01pp | 99.72% | 100.00% | +0.28pp |
| Approved by Fraud Service | 648 | 787 | +139 | +21.45pp | 91.53% | 89.64% | -1.89pp |
| PVS Attempt | 647 | 762 | +115 | +17.77pp | 99.85% | 96.82% | -3.02pp |
| PVS Success | 616 | 730 | +114 | +18.51pp | 95.21% | 95.80% | +0.59pp |
| **Successful Checkout** | 626 | 741 | +115 | +18.37pp | 101.62% | 101.51% | -0.12pp |

**Key Driver:** Checkout Attempt (+7.29pp)

---

### MR

#### Waterfall GA

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 10,300 | 8,924 | -1,376 | -13.36pp | - | - | - |
| Select Payment Method | 3,179 | 2,571 | -608 | -19.13pp | 30.86% | 28.81% | -2.05pp |
| Click Submit Form | 2,861 | 2,296 | -565 | -19.75pp | 90.00% | 89.30% | -0.69pp |
| FE Validation Passed | 2,886 | 2,330 | -556 | -19.27pp | 100.87% | 101.48% | +0.61pp |
| Enter Fraud Service | 2,742 | 2,215 | -527 | -19.22pp | 95.01% | 95.06% | +0.05pp |
| Approved by Fraud Service | 2,682 | 2,161 | -521 | -19.43pp | 97.81% | 97.56% | -0.25pp |
| Call to PVS | 2,578 | 2,054 | -524 | -20.33pp | 96.12% | 95.05% | -1.07pp |
| **Successful Checkout** | 2,582 | 2,054 | -528 | -20.45pp | 100.16% | 100.00% | -0.16pp |
| **PCR Rate** | | | | | 25.07% | 23.02% | **-2.05pp** |

**Key Driver:** Select Payment Method (-2.05pp)

#### Waterfall Backend

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 12,194 | 10,459 | -1,735 | -14.23pp | - | - | - |
| Checkout Attempt | 3,084 | 2,437 | -647 | -20.98pp | 25.29% | 23.30% | -1.99pp |
| Enter Fraud Service | 3,079 | 2,425 | -654 | -21.24pp | 99.84% | 99.51% | -0.33pp |
| Approved by Fraud Service | 2,987 | 2,357 | -630 | -21.09pp | 97.01% | 97.20% | +0.18pp |
| PVS Attempt | 90 | 86 | -4 | -4.44pp | 3.01% | 3.65% | +0.64pp |
| PVS Success | 88 | 84 | -4 | -4.55pp | 97.78% | 97.67% | -0.10pp |
| **Successful Checkout** | 2,880 | 2,267 | -613 | -21.28pp | 3272.73% | 2698.81% | -573.92pp |

**Key Driver:** Successful Checkout (-573.92pp)

---

### CK

#### Waterfall GA

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 4,975 | 4,289 | -686 | -13.79pp | - | - | - |
| Select Payment Method | 2,629 | 2,376 | -253 | -9.62pp | 52.84% | 55.40% | +2.55pp |
| Click Submit Form | 2,415 | 2,185 | -230 | -9.52pp | 91.86% | 91.96% | +0.10pp |
| FE Validation Passed | 2,339 | 2,120 | -219 | -9.36pp | 96.85% | 97.03% | +0.17pp |
| Enter Fraud Service | 2,292 | 2,083 | -209 | -9.12pp | 97.99% | 98.25% | +0.26pp |
| Approved by Fraud Service | 2,202 | 2,002 | -200 | -9.08pp | 96.07% | 96.11% | +0.04pp |
| Call to PVS | 2,199 | 1,990 | -209 | -9.50pp | 99.86% | 99.40% | -0.46pp |
| **Successful Checkout** | 2,067 | 1,871 | -196 | -9.48pp | 94.00% | 94.02% | +0.02pp |
| **PCR Rate** | | | | | 41.55% | 43.62% | **+2.08pp** |

**Key Driver:** Select Payment Method (+2.55pp)

#### Waterfall Backend

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 5,502 | 4,824 | -678 | -12.32pp | - | - | - |
| Checkout Attempt | 2,441 | 2,277 | -164 | -6.72pp | 44.37% | 47.20% | +2.84pp |
| Enter Fraud Service | 2,433 | 2,267 | -166 | -6.82pp | 99.67% | 99.56% | -0.11pp |
| Approved by Fraud Service | 2,302 | 2,158 | -144 | -6.26pp | 94.62% | 95.19% | +0.58pp |
| PVS Attempt | 2,300 | 2,145 | -155 | -6.74pp | 99.91% | 99.40% | -0.52pp |
| PVS Success | 2,175 | 2,012 | -163 | -7.49pp | 94.57% | 93.80% | -0.77pp |
| **Successful Checkout** | 2,216 | 2,046 | -170 | -7.67pp | 101.89% | 101.69% | -0.20pp |

**Key Driver:** Checkout Attempt (+2.84pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (-0.76pp) meets threshold (+0.03pp)

### Recovery Rate

| Metric | 2026-W19 | 2026-W20 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 1,904 | 1,982 | 78 |
| Error → Passed | 1,142 | 1,136 | -6 |
| **Recovery Rate** | **59.98%** | **57.32%** | **-2.66pp** |

### Error Type Distribution

| Error Type | 2026-W19 | 2026-W19 % | 2026-W20 | 2026-W20 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 1,212 | 63.7% | 1,280 | 64.6% | +0.93pp |
| terms_not_accepted | 725 | 38.1% | 750 | 37.8% | -0.24pp |
| PAYPAL_POPUP_CLOSED | 293 | 15.4% | 301 | 15.2% | -0.20pp |
| CC_TOKENISE_ERR | 23 | 1.2% | 34 | 1.7% | +0.51pp |
| PAYPAL_TOKENISE_ERR | 25 | 1.3% | 32 | 1.6% | +0.30pp |


---

## Fraud Analysis

**Include reason:** Enter FS Δ (+0.51pp) meets threshold (+0.03pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W19 | 2026-W19 % | 2026-W20 | 2026-W20 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 14,652 | - | 13,909 | - | -743 | -5.1% |
| Enter Fraud Service | 14,541 | - | 13,788 | - | -753 | -5.2% |
| **Gap (Skipped)** | **111** | **0.76%** | **121** | **0.87%** | **10** | **+0.11pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W19 Gap | 2026-W19 % | 2026-W20 Gap | 2026-W20 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Braintree_ApplePay | 32 | 29.4% | 40 | 33.9% | +8 | +4.54pp |
| Braintree_CreditCard | 36 | 33.0% | 37 | 31.4% | +1 | -1.67pp |
| Braintree_Paypal | 25 | 22.9% | 17 | 14.4% | -8 | -8.53pp |
| ProcessOut_CreditCard | 5 | 4.6% | 14 | 11.9% | +9 | +7.28pp |
| Adyen_CreditCard | 11 | 10.1% | 10 | 8.5% | -1 | -1.62pp |
| **Total** | **109** | **100%** | **118** | **100%** | **9** | - |

*% of Gap = Payment Method Gap / Total Gap*

---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (+0.17pp) meets threshold (+0.03pp)

| Decline Reason | 2026-W19 | 2026-W19 % | 2026-W20 | 2026-W20 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Failed Verification: Insufficient Funds | 80 | 28.6% | 80 | 27.8% | 0 | -0.79pp |
| Blocked Verification: Payment method is blocked due to business reasons | 63 | 22.5% | 50 | 17.4% | -13 | -5.14pp |
| ChallengeShopper | 25 | 8.9% | 27 | 9.4% | +2 | +0.45pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 32 | 11.4% | 21 | 7.3% | -11 | -4.14pp |
| Failed Verification: Refused(Refused) | 21 | 7.5% | 20 | 6.9% | -1 | -0.56pp |
| Failed Verification: Declined | 17 | 6.1% | 20 | 6.9% | +3 | +0.87pp |
| Failed Verification: Refused(Not enough balance) | 17 | 6.1% | 19 | 6.6% | +2 | +0.53pp |
| Failed Verification: Refused(FRAUD) | 10 | 3.6% | 18 | 6.2% | +8 | +2.68pp |
| Failed Verification: Refused(Blocked Card) | 9 | 3.2% | 17 | 5.9% | +8 | +2.69pp |
| Failed Verification: Refused(Invalid Card Number) | 6 | 2.1% | 16 | 5.6% | +10 | +3.41pp |
| **Total PVS Failures** | **280** | **100%** | **288** | **100%** | **+8** | - |

---


---

*Report: 2026-05-19*
