# PCR Investigation: HF-NA 2026-W23

**Metric:** Payment Conversion Rate  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 27.90% → 27.86% (-0.04pp)  
**Volume:** 57,437 payment visits  
**Threshold:** +0.02pp (0.5 × |Overall PCR Δ|)

## Executive Summary

**Overall:** Payment Conversion Rate in HF-NA declined marginally by -0.04pp (27.90% → 27.86%) in W23, remaining essentially stable within normal fluctuation range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ≥ threshold | -0.77pp | ⚠️ |
| Click Submit Form | < threshold | +0.62pp | ✅ |
| FE Validation Passed | ≥ threshold | -0.52pp | ⚠️ |
| Enter Fraud Service | ≥ threshold | +0.45pp | ✅ |
| Approved by Fraud Service | < threshold | +0.06pp | ✅ |
| Call to PVS | ≥ threshold | +1.06pp | ✅ |
| Successful Checkout | ≥ threshold | -0.15pp | ⚠️ |

**Key Findings:**
- **Select Payment Method** saw the largest negative impact (-0.77pp), indicating potential friction in payment method selection, particularly in US where conversion dropped -0.62pp
- **FE Validation** recovery rate declined by -1.93pp (69.77% → 67.84%), with APPLEPAY_DISMISSED errors increasing to 59.3% of all errors
- **Payment method performance improved significantly** across all major providers: ProcessOut_CreditCard (+11.88pp), Braintree_Paypal (+12.54pp), and Adyen_CreditCard (+14.35pp)
- **Country divergence observed:** CA improved +0.95pp while US declined -0.13pp, with CA's Click Submit Form improvement (+1.95pp) driving gains
- **Fraud Service gap reduced** from 1.24% to 0.97% of checkout attempts, with Adyen_CreditCard gap dropping significantly (-63 occurrences)

**Action:** Monitor - The overall decline is minimal (-0.04pp) and within acceptable variance. The improvements in payment method success rates and fraud service efficiency offset losses at early funnel stages. Continue monitoring Select Payment Method drop-off, particularly in US.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 57,736 | 57,437 | -299 | -0.5% | - | - | - |
| Select Payment Method | 24,184 | 23,617 | -567 | -2.3% | 41.89% | 41.12% | -0.77pp |
| Click Submit Form | 20,477 | 20,143 | -334 | -1.6% | 84.67% | 85.29% | +0.62pp |
| FE Validation Passed | 19,240 | 18,822 | -418 | -2.2% | 93.96% | 93.44% | -0.52pp |
| Enter Fraud Service | 18,580 | 18,261 | -319 | -1.7% | 96.57% | 97.02% | +0.45pp |
| Approved by Fraud Service | 17,604 | 17,312 | -292 | -1.7% | 94.75% | 94.80% | +0.06pp |
| Call to PVS | 15,959 | 15,878 | -81 | -0.5% | 90.66% | 91.72% | +1.06pp |
| **Successful Checkout** | 16,108 | 16,002 | -106 | -0.7% | 100.93% | 100.78% | -0.15pp |
| **PCR Rate** | | | | | 27.90% | 27.86% | **-0.04pp** |

### Waterfall Backend

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 53,274 | 61,689 | 8,415 | 15.8% | - | - | - |
| Checkout Attempt | 22,501 | 22,682 | 181 | 0.8% | 42.24% | 36.77% | -5.47pp |
| Enter Fraud Service | 22,222 | 22,462 | 240 | 1.1% | 98.76% | 99.03% | +0.27pp |
| Approved by Fraud Service | 20,713 | 20,949 | 236 | 1.1% | 93.21% | 93.26% | +0.05pp |
| PVS Attempt | 19,330 | 19,505 | 175 | 0.9% | 93.32% | 93.11% | -0.22pp |
| PVS Success | 17,770 | 18,092 | 322 | 1.8% | 91.93% | 92.76% | +0.83pp |
| **Successful Checkout** | 15,432 | 17,936 | 2,504 | 16.2% | 86.84% | 99.14% | +12.29pp |
| **PCR Rate** | | | | | 28.97% | 29.07% | **+0.11pp** |

### Payment Method Breakdown

| Payment Method | 2026-W22 Attempt | 2026-W22 Success | 2026-W22 Rate | 2026-W23 Attempt | 2026-W23 Success | 2026-W23 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 12,187 | 8,923 | 73.22% | 12,352 | 10,511 | 85.10% | +11.88pp |
| Braintree_ApplePay | 7,072 | 4,296 | 60.75% | 7,186 | 4,893 | 68.09% | +7.34pp |
| Braintree_Paypal | 1,980 | 1,435 | 72.47% | 1,968 | 1,673 | 85.01% | +12.54pp |
| Adyen_CreditCard | 912 | 578 | 63.38% | 826 | 642 | 77.72% | +14.35pp |
| Braintree_CreditCard | 239 | 198 | 82.85% | 245 | 216 | 88.16% | +5.32pp |
| visa | 35 | 1 | 2.86% | 37 | 0 | 0.00% | -2.86pp |
| NoPayment | 34 | 0 | 0.00% | 22 | 0 | 0.00% | +0.00pp |
| mc | 24 | 1 | 4.17% | 17 | 0 | 0.00% | -4.17pp |
| paypal | 13 | 0 | 0.00% | 13 | 1 | 7.69% | +7.69pp |
| amex | 3 | 0 | 0.00% | 8 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (2 countries in HF-NA)

| Country | Volume | PCR 2026-W22 | PCR 2026-W23 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| CA | 12,857 | 33.24% | 34.19% | +0.95pp | 1 | 1 |
| US | 44,580 | 26.16% | 26.03% | -0.13pp | 2 | 2 |

---

### US

#### Waterfall GA

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 43,570 | 44,580 | +1,010 | +2.32pp | - | - | - |
| Select Payment Method | 16,847 | 16,959 | +112 | +0.66pp | 38.67% | 38.04% | -0.62pp |
| Click Submit Form | 14,733 | 14,801 | +68 | +0.46pp | 87.45% | 87.28% | -0.18pp |
| FE Validation Passed | 13,827 | 13,808 | -19 | -0.14pp | 93.85% | 93.29% | -0.56pp |
| Enter Fraud Service | 13,363 | 13,401 | +38 | +0.28pp | 96.64% | 97.05% | +0.41pp |
| Approved by Fraud Service | 12,653 | 12,717 | +64 | +0.51pp | 94.69% | 94.90% | +0.21pp |
| Call to PVS | 11,290 | 11,504 | +214 | +1.90pp | 89.23% | 90.46% | +1.23pp |
| **Successful Checkout** | 11,399 | 11,606 | +207 | +1.82pp | 100.97% | 100.89% | -0.08pp |
| **PCR Rate** | | | | | 26.16% | 26.03% | **-0.13pp** |

**Key Driver:** Call to PVS (+1.23pp)

#### Waterfall Backend

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 40,580 | 48,373 | +7,793 | +19.20pp | - | - | - |
| Checkout Attempt | 16,540 | 16,987 | +447 | +2.70pp | 40.76% | 35.12% | -5.64pp |
| Enter Fraud Service | 16,313 | 16,839 | +526 | +3.22pp | 98.63% | 99.13% | +0.50pp |
| Approved by Fraud Service | 15,221 | 15,750 | +529 | +3.48pp | 93.31% | 93.53% | +0.23pp |
| PVS Attempt | 14,808 | 15,305 | +497 | +3.36pp | 97.29% | 97.17% | -0.11pp |
| PVS Success | 13,384 | 14,014 | +630 | +4.71pp | 90.38% | 91.56% | +1.18pp |
| **Successful Checkout** | 13,948 | 14,507 | +559 | +4.01pp | 104.21% | 103.52% | -0.70pp |

**Key Driver:** Checkout Attempt (-5.64pp)

---

### CA

#### Waterfall GA

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 14,166 | 12,857 | -1,309 | -9.24pp | - | - | - |
| Select Payment Method | 7,337 | 6,658 | -679 | -9.25pp | 51.79% | 51.79% | -0.01pp |
| Click Submit Form | 5,744 | 5,342 | -402 | -7.00pp | 78.29% | 80.23% | +1.95pp |
| FE Validation Passed | 5,413 | 5,014 | -399 | -7.37pp | 94.24% | 93.86% | -0.38pp |
| Enter Fraud Service | 5,217 | 4,860 | -357 | -6.84pp | 96.38% | 96.93% | +0.55pp |
| Approved by Fraud Service | 4,951 | 4,595 | -356 | -7.19pp | 94.90% | 94.55% | -0.35pp |
| Call to PVS | 4,669 | 4,374 | -295 | -6.32pp | 94.30% | 95.19% | +0.89pp |
| **Successful Checkout** | 4,709 | 4,396 | -313 | -6.65pp | 100.86% | 100.50% | -0.35pp |
| **PCR Rate** | | | | | 33.24% | 34.19% | **+0.95pp** |

**Key Driver:** Click Submit Form (+1.95pp)

#### Waterfall Backend

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 12,694 | 13,316 | +622 | +4.90pp | - | - | - |
| Checkout Attempt | 5,961 | 5,695 | -266 | -4.46pp | 46.96% | 42.77% | -4.19pp |
| Enter Fraud Service | 5,909 | 5,623 | -286 | -4.84pp | 99.13% | 98.74% | -0.39pp |
| Approved by Fraud Service | 5,492 | 5,199 | -293 | -5.34pp | 92.94% | 92.46% | -0.48pp |
| PVS Attempt | 4,522 | 4,200 | -322 | -7.12pp | 82.34% | 80.78% | -1.55pp |
| PVS Success | 4,386 | 4,078 | -308 | -7.02pp | 96.99% | 97.10% | +0.10pp |
| **Successful Checkout** | 5,344 | 5,075 | -269 | -5.03pp | 121.84% | 124.45% | +2.61pp |

**Key Driver:** Checkout Attempt (-4.19pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (-0.52pp) meets threshold (+0.02pp)

### Recovery Rate

| Metric | 2026-W22 | 2026-W23 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 4,701 | 4,649 | -52 |
| Error → Passed | 3,280 | 3,154 | -126 |
| **Recovery Rate** | **69.77%** | **67.84%** | **-1.93pp** |

### Error Type Distribution

| Error Type | 2026-W22 | 2026-W22 % | 2026-W23 | 2026-W23 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 2,740 | 58.3% | 2,757 | 59.3% | +1.02pp |
| terms_not_accepted | 1,963 | 41.8% | 1,932 | 41.6% | -0.20pp |
| PAYPAL_POPUP_CLOSED | 449 | 9.6% | 396 | 8.5% | -1.03pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 257 | 5.5% | 276 | 5.9% | +0.47pp |
| CC_TOKENISE_ERR | 152 | 3.2% | 121 | 2.6% | -0.63pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 110 | 2.3% | 108 | 2.3% | -0.02pp |
| PAYPAL_TOKENISE_ERR | 45 | 1.0% | 47 | 1.0% | +0.05pp |
| CC_NO_PREPAID_ERR | 9 | 0.2% | 6 | 0.1% | -0.06pp |
| APPLEPAY_MERCHANT_VALIDATION_ERR | 0 | 0.0% | 4 | 0.1% | +0.09pp |


---

## Fraud Analysis

**Include reason:** Enter FS Δ (+0.45pp) meets threshold (+0.02pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W22 | 2026-W22 % | 2026-W23 | 2026-W23 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 22,501 | - | 22,682 | - | 181 | 0.8% |
| Enter Fraud Service | 22,222 | - | 22,462 | - | 240 | 1.1% |
| **Gap (Skipped)** | **279** | **1.24%** | **220** | **0.97%** | **-59** | **-0.27pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W22 Gap | 2026-W22 % | 2026-W23 Gap | 2026-W23 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Adyen_CreditCard | 195 | 60.4% | 132 | 47.5% | -63 | -12.89pp |
| ProcessOut_CreditCard | 52 | 16.1% | 72 | 25.9% | +20 | +9.80pp |
| Braintree_ApplePay | 28 | 8.7% | 36 | 12.9% | +8 | +4.28pp |
| NoPayment | 34 | 10.5% | 22 | 7.9% | -12 | -2.61pp |
| Braintree_Paypal | 14 | 4.3% | 16 | 5.8% | +2 | +1.42pp |
| **Total** | **323** | **100%** | **278** | **100%** | **-45** | - |

*% of Gap = Payment Method Gap / Total Gap*

---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (-0.15pp) meets threshold (+0.02pp)

| Decline Reason | 2026-W22 | 2026-W22 % | 2026-W23 | 2026-W23 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Blocked Verification: Payment method is blocked due to business reasons | 699 | 57.0% | 652 | 57.3% | -47 | +0.28pp |
| Failed Verification: Insufficient Funds | 250 | 20.4% | 220 | 19.3% | -30 | -1.06pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 111 | 9.1% | 101 | 8.9% | -10 | -0.18pp |
| Failed Verification: Issuer or Cardholder has put a restriction on the card | 62 | 5.1% | 41 | 3.6% | -21 | -1.45pp |
| Failed Verification: Declined | 24 | 2.0% | 37 | 3.3% | +13 | +1.29pp |
| Failed Verification: Closed Card | 10 | 0.8% | 24 | 2.1% | +14 | +1.29pp |
| Failed Verification: Processor Declined - Fraud Suspected | 20 | 1.6% | 19 | 1.7% | -1 | +0.04pp |
| Failed Verification: Cannot Authorize at this time (Policy) | 17 | 1.4% | 16 | 1.4% | -1 | +0.02pp |
| Failed Verification: Expired Card | 17 | 1.4% | 14 | 1.2% | -3 | -0.16pp |
| Failed Verification: Processor Declined | 16 | 1.3% | 14 | 1.2% | -2 | -0.07pp |
| **Total PVS Failures** | **1,226** | **100%** | **1,138** | **100%** | **-88** | - |

---


---

*Report: 2026-06-09*
