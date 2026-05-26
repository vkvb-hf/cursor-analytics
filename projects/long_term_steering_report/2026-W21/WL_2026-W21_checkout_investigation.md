# PCR Investigation: WL 2026-W21

**Metric:** Payment Conversion Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 29.38% → 28.66% (-0.72pp)  
**Volume:** 37,936 payment visits  
**Threshold:** +0.36pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined by -0.72pp (29.38% → 28.66%) on 37,936 payment visits in 2026-W21, driven primarily by a significant drop in the Select Payment Method step.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Rate drop exceeds threshold | -1.68pp | ⚠️ |
| Click Submit Form | Rate drop exceeds threshold | -0.76pp | ⚠️ |
| FE Validation Passed | Improvement above threshold | +0.85pp | ✅ |
| Enter Fraud Service | Minor improvement | +0.22pp | ✅ |
| Approved by Fraud Service | Stable | -0.04pp | ✅ |
| Call to PVS | Improvement above threshold | +0.57pp | ✅ |
| Successful Checkout | Improvement above threshold | +0.90pp | ✅ |

**Key Findings:**
- **Select Payment Method** is the primary bottleneck with -1.68pp conversion drop, indicating users are visiting payment pages but not proceeding to select a payment option
- **MR** experienced significant volume increase (+36.7%) but PCR declined by -1.85pp, with Select Payment Method down -1.96pp being the key driver
- **CK** showed strong improvement (+2.55pp PCR) driven by Successful Checkout gains (+2.56pp) and PVS Success improvement (+3.14pp)
- Backend data shows **PVS Attempt** dropped significantly (-4.54pp), though PVS Success rate improved (+1.23pp)
- **Payment Method blocked** errors decreased by -5.27pp share, and overall PVS failures dropped from 244 to 184 (-60), contributing to downstream improvements

**Action:** Investigate — Focus on the Select Payment Method drop, particularly in MR where volume increased substantially but engagement at payment method selection declined. Examine potential UX issues, payment method availability, or pricing display changes affecting user intent.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 37,423 | 37,936 | 513 | 1.4% | - | - | - |
| Select Payment Method | 15,164 | 14,736 | -428 | -2.8% | 40.52% | 38.84% | -1.68pp |
| Click Submit Form | 13,448 | 12,957 | -491 | -3.7% | 88.68% | 87.93% | -0.76pp |
| FE Validation Passed | 12,777 | 12,421 | -356 | -2.8% | 95.01% | 95.86% | +0.85pp |
| Enter Fraud Service | 12,312 | 11,996 | -316 | -2.6% | 96.36% | 96.58% | +0.22pp |
| Approved by Fraud Service | 11,637 | 11,334 | -303 | -2.6% | 94.52% | 94.48% | -0.04pp |
| Call to PVS | 11,438 | 11,205 | -233 | -2.0% | 98.29% | 98.86% | +0.57pp |
| **Successful Checkout** | 10,996 | 10,873 | -123 | -1.1% | 96.14% | 97.04% | +0.90pp |
| **PCR Rate** | | | | | 29.38% | 28.66% | **-0.72pp** |

### Waterfall Backend

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 44,052 | 44,630 | 578 | 1.3% | - | - | - |
| Checkout Attempt | 13,909 | 13,459 | -450 | -3.2% | 31.57% | 30.16% | -1.42pp |
| Enter Fraud Service | 13,788 | 13,357 | -431 | -3.1% | 99.13% | 99.24% | +0.11pp |
| Approved by Fraud Service | 12,860 | 12,470 | -390 | -3.0% | 93.27% | 93.36% | +0.09pp |
| PVS Attempt | 10,330 | 9,450 | -880 | -8.5% | 80.33% | 75.78% | -4.54pp |
| PVS Success | 9,878 | 9,153 | -725 | -7.3% | 95.62% | 96.86% | +1.23pp |
| **Successful Checkout** | 12,283 | 12,082 | -201 | -1.6% | 124.35% | 132.00% | +7.65pp |
| **PCR Rate** | | | | | 27.88% | 27.07% | **-0.81pp** |

### Payment Method Breakdown

| Payment Method | 2026-W20 Attempt | 2026-W20 Success | 2026-W20 Rate | 2026-W21 Attempt | 2026-W21 Success | 2026-W21 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 3,617 | 3,188 | 88.14% | 3,808 | 3,405 | 89.42% | +1.28pp |
| Braintree_ApplePay | 3,979 | 3,568 | 89.67% | 3,718 | 3,373 | 90.72% | +1.05pp |
| Adyen_CreditCard | 2,686 | 2,363 | 87.97% | 2,419 | 2,200 | 90.95% | +2.97pp |
| Braintree_Paypal | 1,767 | 1,598 | 90.44% | 1,727 | 1,596 | 92.41% | +1.98pp |
| Braintree_CreditCard | 1,562 | 1,314 | 84.12% | 1,470 | 1,245 | 84.69% | +0.57pp |
| ProcessOut_ApplePay | 295 | 252 | 85.42% | 314 | 263 | 83.76% | -1.67pp |
| NoPayment | 3 | 0 | 0.00% | 3 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (2 countries in WL)

| Country | Volume | PCR 2026-W20 | PCR 2026-W21 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| MR | 12,199 | 23.02% | 21.17% | -1.85pp | 1 | 2 |
| CK | 3,918 | 43.62% | 46.17% | +2.55pp | 2 | 1 |

---

### MR

#### Waterfall GA

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 8,924 | 12,199 | +3,275 | +36.70pp | - | - | - |
| Select Payment Method | 2,571 | 3,276 | +705 | +27.42pp | 28.81% | 26.85% | -1.96pp |
| Click Submit Form | 2,296 | 2,872 | +576 | +25.09pp | 89.30% | 87.67% | -1.64pp |
| FE Validation Passed | 2,330 | 2,908 | +578 | +24.81pp | 101.48% | 101.25% | -0.23pp |
| Enter Fraud Service | 2,215 | 2,771 | +556 | +25.10pp | 95.06% | 95.29% | +0.22pp |
| Approved by Fraud Service | 2,161 | 2,703 | +542 | +25.08pp | 97.56% | 97.55% | -0.02pp |
| Call to PVS | 2,054 | 2,582 | +528 | +25.71pp | 95.05% | 95.52% | +0.47pp |
| **Successful Checkout** | 2,054 | 2,582 | +528 | +25.71pp | 100.00% | 100.00% | +0.00pp |
| **PCR Rate** | | | | | 23.02% | 21.17% | **-1.85pp** |

**Key Driver:** Select Payment Method (-1.96pp)

#### Waterfall Backend

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 10,459 | 14,186 | +3,727 | +35.63pp | - | - | - |
| Checkout Attempt | 2,437 | 3,004 | +567 | +23.27pp | 23.30% | 21.18% | -2.12pp |
| Enter Fraud Service | 2,425 | 2,998 | +573 | +23.63pp | 99.51% | 99.80% | +0.29pp |
| Approved by Fraud Service | 2,357 | 2,911 | +554 | +23.50pp | 97.20% | 97.10% | -0.10pp |
| PVS Attempt | 86 | 117 | +31 | +36.05pp | 3.65% | 4.02% | +0.37pp |
| PVS Success | 84 | 117 | +33 | +39.29pp | 97.67% | 100.00% | +2.33pp |
| **Successful Checkout** | 2,267 | 2,818 | +551 | +24.31pp | 2698.81% | 2408.55% | -290.26pp |

**Key Driver:** Successful Checkout (-290.26pp)

---

### CK

#### Waterfall GA

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 4,289 | 3,918 | -371 | -8.65pp | - | - | - |
| Select Payment Method | 2,376 | 2,215 | -161 | -6.78pp | 55.40% | 56.53% | +1.14pp |
| Click Submit Form | 2,185 | 2,048 | -137 | -6.27pp | 91.96% | 92.46% | +0.50pp |
| FE Validation Passed | 2,120 | 1,983 | -137 | -6.46pp | 97.03% | 96.83% | -0.20pp |
| Enter Fraud Service | 2,083 | 1,952 | -131 | -6.29pp | 98.25% | 98.44% | +0.18pp |
| Approved by Fraud Service | 2,002 | 1,873 | -129 | -6.44pp | 96.11% | 95.95% | -0.16pp |
| Call to PVS | 1,990 | 1,873 | -117 | -5.88pp | 99.40% | 100.00% | +0.60pp |
| **Successful Checkout** | 1,871 | 1,809 | -62 | -3.31pp | 94.02% | 96.58% | +2.56pp |
| **PCR Rate** | | | | | 43.62% | 46.17% | **+2.55pp** |

**Key Driver:** Successful Checkout (+2.56pp)

#### Waterfall Backend

| Funnel Step | 2026-W20 | 2026-W21 | Δ Count | Δ % | 2026-W20 Conv | 2026-W21 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 4,824 | 4,352 | -472 | -9.78pp | - | - | - |
| Checkout Attempt | 2,277 | 2,101 | -176 | -7.73pp | 47.20% | 48.28% | +1.08pp |
| Enter Fraud Service | 2,267 | 2,097 | -170 | -7.50pp | 99.56% | 99.81% | +0.25pp |
| Approved by Fraud Service | 2,158 | 1,995 | -163 | -7.55pp | 95.19% | 95.14% | -0.06pp |
| PVS Attempt | 2,145 | 1,995 | -150 | -6.99pp | 99.40% | 100.00% | +0.60pp |
| PVS Success | 2,012 | 1,934 | -78 | -3.88pp | 93.80% | 96.94% | +3.14pp |
| **Successful Checkout** | 2,046 | 1,949 | -97 | -4.74pp | 101.69% | 100.78% | -0.91pp |

**Key Driver:** PVS Success (+3.14pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (+0.85pp) meets threshold (+0.36pp)

### Recovery Rate

| Metric | 2026-W20 | 2026-W21 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 1,982 | 1,655 | -327 |
| Error → Passed | 1,136 | 978 | -158 |
| **Recovery Rate** | **57.32%** | **59.09%** | **+1.78pp** |

### Error Type Distribution

| Error Type | 2026-W20 | 2026-W20 % | 2026-W21 | 2026-W21 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 1,280 | 64.6% | 1,064 | 64.3% | -0.29pp |
| terms_not_accepted | 750 | 37.8% | 622 | 37.6% | -0.26pp |
| PAYPAL_POPUP_CLOSED | 301 | 15.2% | 259 | 15.6% | +0.46pp |
| CC_TOKENISE_ERR | 34 | 1.7% | 19 | 1.1% | -0.57pp |
| PAYPAL_TOKENISE_ERR | 32 | 1.6% | 16 | 1.0% | -0.65pp |


---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (+0.90pp) meets threshold (+0.36pp)

| Decline Reason | 2026-W20 | 2026-W20 % | 2026-W21 | 2026-W21 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Failed Verification: Insufficient Funds | 80 | 32.8% | 57 | 31.0% | -23 | -1.81pp |
| Blocked Verification: Payment method is blocked due to business reasons | 50 | 20.5% | 28 | 15.2% | -22 | -5.27pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 21 | 8.6% | 14 | 7.6% | -7 | -1.00pp |
| Failed Verification: Cannot Authorize at this time (Policy) | 9 | 3.7% | 14 | 7.6% | +5 | +3.92pp |
| Failed Verification: Refused(Refused) | 20 | 8.2% | 13 | 7.1% | -7 | -1.13pp |
| Failed Verification: Refused(CVC Declined) | 13 | 5.3% | 13 | 7.1% | 0 | +1.74pp |
| Failed Verification: Processor Declined | 6 | 2.5% | 12 | 6.5% | +6 | +4.06pp |
| Failed Verification: Card Issuer Declined CVV | 13 | 5.3% | 11 | 6.0% | -2 | +0.65pp |
| Failed Verification: Declined | 20 | 8.2% | 11 | 6.0% | -9 | -2.22pp |
| Failed Verification: Issuer or Cardholder has put a restriction on the card | 12 | 4.9% | 11 | 6.0% | -1 | +1.06pp |
| **Total PVS Failures** | **244** | **100%** | **184** | **100%** | **-60** | - |

---


---

*Report: 2026-05-26*
