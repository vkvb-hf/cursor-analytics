# PCR Investigation: US-HF 2026-W17

**Metric:** Payment Conversion Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 25.83% → 25.04% (-0.79pp)  
**Volume:** 42,133 payment visits  
**Threshold:** +0.40pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined by -0.79pp (25.83% → 25.04%) on 42,133 payment visits in US-HF during 2026-W17, driven primarily by a significant drop in the Select Payment Method step.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Rate change vs threshold | -1.42pp | ⚠️ |
| Click Submit Form | Rate change vs threshold | +0.17pp | ✅ |
| FE Validation Passed | Rate change vs threshold | +0.07pp | ✅ |
| Enter Fraud Service | Rate change vs threshold | +0.08pp | ✅ |
| Approved by Fraud Service | Rate change vs threshold | +1.46pp | ✅ |
| Call to PVS | Rate change vs threshold | -0.68pp | ⚠️ |
| Successful Checkout | Rate change vs threshold | -0.44pp | ⚠️ |

**Key Findings:**
- Select Payment Method conversion dropped significantly by -1.42pp (37.11% → 35.70%), indicating users are abandoning before choosing a payment option
- Backend Checkout Attempt conversion plummeted by -7.43pp (41.31% → 33.88%), suggesting a major upstream issue preventing users from initiating checkout
- Payment volume decreased substantially by -24.7% (55,957 → 42,133 payment visits), indicating reduced traffic or engagement
- Fraud Service approval improved by +1.46pp (92.02% → 93.48%), positively impacting downstream conversion
- All payment methods showed improved success rates (ProcessOut_CreditCard +14.00pp, Braintree_ApplePay +13.51pp), indicating PSP performance is not the issue

**Action:** Investigate - The significant drop in Select Payment Method (-1.42pp) and Backend Checkout Attempt (-7.43pp) conversion requires investigation into potential UX changes, page load issues, or upstream funnel problems that are preventing users from reaching and engaging with payment selection.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 55,957 | 42,133 | -13,824 | -24.7% | - | - | - |
| Select Payment Method | 20,767 | 15,040 | -5,727 | -27.6% | 37.11% | 35.70% | -1.42pp |
| Click Submit Form | 18,240 | 13,235 | -5,005 | -27.4% | 87.83% | 88.00% | +0.17pp |
| FE Validation Passed | 17,167 | 12,466 | -4,701 | -27.4% | 94.12% | 94.19% | +0.07pp |
| Enter Fraud Service | 16,814 | 12,220 | -4,594 | -27.3% | 97.94% | 98.03% | +0.08pp |
| Approved by Fraud Service | 15,472 | 11,423 | -4,049 | -26.2% | 92.02% | 93.48% | +1.46pp |
| Call to PVS | 15,548 | 11,401 | -4,147 | -26.7% | 100.49% | 99.81% | -0.68pp |
| **Successful Checkout** | 14,455 | 10,549 | -3,906 | -27.0% | 92.97% | 92.53% | -0.44pp |
| **PCR Rate** | | | | | 25.83% | 25.04% | **-0.79pp** |

### Waterfall Backend

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 50,112 | 51,507 | 1,395 | 2.8% | - | - | - |
| Checkout Attempt | 20,703 | 17,450 | -3,253 | -15.7% | 41.31% | 33.88% | -7.43pp |
| Enter Fraud Service | 20,593 | 17,390 | -3,203 | -15.6% | 99.47% | 99.66% | +0.19pp |
| Approved by Fraud Service | 18,536 | 15,957 | -2,579 | -13.9% | 90.01% | 91.76% | +1.75pp |
| PVS Attempt | 18,142 | 15,496 | -2,646 | -14.6% | 97.87% | 97.11% | -0.76pp |
| PVS Success | 16,826 | 14,360 | -2,466 | -14.7% | 92.75% | 92.67% | -0.08pp |
| **Successful Checkout** | 13,813 | 14,039 | 226 | 1.6% | 82.09% | 97.76% | +15.67pp |
| **PCR Rate** | | | | | 27.56% | 27.26% | **-0.31pp** |

### Payment Method Breakdown

| Payment Method | 2026-W16 Attempt | 2026-W16 Success | 2026-W16 Rate | 2026-W17 Attempt | 2026-W17 Success | 2026-W17 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 11,305 | 7,836 | 69.31% | 9,759 | 8,131 | 83.32% | +14.00pp |
| Braintree_ApplePay | 7,388 | 4,587 | 62.09% | 5,994 | 4,531 | 75.59% | +13.51pp |
| Braintree_Paypal | 1,655 | 1,187 | 71.72% | 1,360 | 1,145 | 84.19% | +12.47pp |
| Braintree_CreditCard | 264 | 202 | 76.52% | 277 | 231 | 83.39% | +6.88pp |
|  | 54 | 1 | 1.85% | 59 | 0 | 0.00% | -1.85pp |
| Braintree_Venmo | 0 | 0 | 0.00% | 1 | 1 | 100.00% | +100.00pp |
| Adyen_CreditCard | 37 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (1 countries in US-HF)

| Country | Volume | PCR 2026-W16 | PCR 2026-W17 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| US | 42,133 | 25.83% | 25.04% | -0.79pp | 1 | 1 |

---

### US

#### Waterfall GA

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 55,957 | 42,133 | -13,824 | -24.70pp | - | - | - |
| Select Payment Method | 20,767 | 15,040 | -5,727 | -27.58pp | 37.11% | 35.70% | -1.42pp |
| Click Submit Form | 18,240 | 13,235 | -5,005 | -27.44pp | 87.83% | 88.00% | +0.17pp |
| FE Validation Passed | 17,167 | 12,466 | -4,701 | -27.38pp | 94.12% | 94.19% | +0.07pp |
| Enter Fraud Service | 16,814 | 12,220 | -4,594 | -27.32pp | 97.94% | 98.03% | +0.08pp |
| Approved by Fraud Service | 15,472 | 11,423 | -4,049 | -26.17pp | 92.02% | 93.48% | +1.46pp |
| Call to PVS | 15,548 | 11,401 | -4,147 | -26.67pp | 100.49% | 99.81% | -0.68pp |
| **Successful Checkout** | 14,455 | 10,549 | -3,906 | -27.02pp | 92.97% | 92.53% | -0.44pp |
| **PCR Rate** | | | | | 25.83% | 25.04% | **-0.79pp** |

**Key Driver:** Approved by Fraud Service (+1.46pp)

#### Waterfall Backend

| Funnel Step | 2026-W16 | 2026-W17 | Δ Count | Δ % | 2026-W16 Conv | 2026-W17 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 50,112 | 51,507 | +1,395 | +2.78pp | - | - | - |
| Checkout Attempt | 20,703 | 17,450 | -3,253 | -15.71pp | 41.31% | 33.88% | -7.43pp |
| Enter Fraud Service | 20,593 | 17,390 | -3,203 | -15.55pp | 99.47% | 99.66% | +0.19pp |
| Approved by Fraud Service | 18,536 | 15,957 | -2,579 | -13.91pp | 90.01% | 91.76% | +1.75pp |
| PVS Attempt | 18,142 | 15,496 | -2,646 | -14.58pp | 97.87% | 97.11% | -0.76pp |
| PVS Success | 16,826 | 14,360 | -2,466 | -14.66pp | 92.75% | 92.67% | -0.08pp |
| **Successful Checkout** | 17,245 | 14,742 | -2,503 | -14.51pp | 102.49% | 102.66% | +0.17pp |

**Key Driver:** Checkout Attempt (-7.43pp)

---



## Fraud Analysis

**Include reason:** Approved Δ (+1.46pp) meets threshold (+0.40pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W16 | 2026-W16 % | 2026-W17 | 2026-W17 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 20,703 | - | 17,450 | - | -3,253 | -15.7% |
| Enter Fraud Service | 20,593 | - | 17,390 | - | -3,203 | -15.6% |
| **Gap (Skipped)** | **110** | **0.53%** | **60** | **0.34%** | **-50** | **-0.19pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W16 Gap | 2026-W16 % | 2026-W17 Gap | 2026-W17 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| ProcessOut_CreditCard | 39 | 35.5% | 32 | 53.3% | -7 | +17.88pp |
| Braintree_ApplePay | 27 | 24.5% | 20 | 33.3% | -7 | +8.79pp |
| Braintree_Paypal | 6 | 5.5% | 8 | 13.3% | +2 | +7.88pp |
| Adyen_CreditCard | 37 | 33.6% | 0 | 0.0% | -37 | -33.64pp |
| Braintree_CreditCard | 1 | 0.9% | 0 | 0.0% | -1 | -0.91pp |
| **Total** | **110** | **100%** | **60** | **100%** | **-50** | - |

*% of Gap = Payment Method Gap / Total Gap*

---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (-0.44pp) meets threshold (+0.40pp)

| Decline Reason | 2026-W16 | 2026-W16 % | 2026-W17 | 2026-W17 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Blocked Verification: Payment method is blocked due to business reasons | 665 | 56.2% | 593 | 58.0% | -72 | +1.80pp |
| Failed Verification: Insufficient Funds | 208 | 17.6% | 174 | 17.0% | -34 | -0.56pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 67 | 5.7% | 62 | 6.1% | -5 | +0.40pp |
| Failed Verification: Issuer or Cardholder has put a restriction on the card | 63 | 5.3% | 48 | 4.7% | -15 | -0.63pp |
| Failed Verification: Declined - Call Issuer | 38 | 3.2% | 30 | 2.9% | -8 | -0.28pp |
| Failed Verification: Card Issuer Declined CVV | 41 | 3.5% | 28 | 2.7% | -13 | -0.73pp |
| Failed Verification: Declined | 19 | 1.6% | 27 | 2.6% | +8 | +1.03pp |
| Failed Verification: Processor Declined - Fraud Suspected | 29 | 2.4% | 21 | 2.1% | -8 | -0.40pp |
| Failed Verification: Closed Card | 32 | 2.7% | 20 | 2.0% | -12 | -0.75pp |
| Failed Verification: Processor Declined | 22 | 1.9% | 20 | 2.0% | -2 | +0.10pp |
| **Total PVS Failures** | **1,184** | **100%** | **1,023** | **100%** | **-161** | - |

---


---

*Report: 2026-04-28*
