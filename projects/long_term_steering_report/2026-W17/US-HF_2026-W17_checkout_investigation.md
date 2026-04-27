# PCR Investigation: US-HF 2026-W17

**Metric:** Payment Conversion Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 25.83% → 25.04% (-0.79pp)  
**Volume:** 42,133 payment visits  
**Threshold:** +0.40pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined from 25.83% to 25.04% (-0.79pp) in US-HF during 2026-W17, with payment visits dropping significantly by 24.7% (55,957 → 42,133).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Entry rate check | -1.42pp | ⚠️ |
| Click Submit Form | Form submission | +0.17pp | ✅ |
| FE Validation Passed | Validation | +0.07pp | ✅ |
| Enter Fraud Service | Fraud entry | +0.08pp | ✅ |
| Approved by Fraud Service | Fraud approval | +1.46pp | ✅ |
| Call to PVS | PVS routing | -0.68pp | ⚠️ |
| Successful Checkout | Final conversion | -0.44pp | ⚠️ |

**Key Findings:**
- The primary PCR decline is driven by a -1.42pp drop in Select Payment Method rate (37.11% → 35.70%), indicating fewer visitors are initiating the payment process
- Backend data shows a severe -7.43pp decline in Checkout Attempt rate (41.31% → 33.88%), suggesting significant top-of-funnel friction
- Fraud Service approval improved substantially (+1.46pp in GA, +1.75pp in Backend), partially offsetting other losses
- All payment methods showed improved success rates week-over-week, with ProcessOut_CreditCard improving +14.00pp and Braintree_ApplePay improving +13.51pp
- PVS failures decreased from 1,175 to 898, with "Blocked Verification: Payment method is blocked due to business reasons" remaining the dominant decline reason (59.4% of failures)

**Action:** Investigate - The significant decline in payment method selection rate (-1.42pp) and checkout attempt rate (-7.43pp) requires investigation into potential UX issues, page load problems, or changes in traffic quality that may be preventing users from initiating checkout.

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
| Blocked Verification: Payment method is blocked due to business reasons | 665 | 56.6% | 533 | 59.4% | -132 | +2.76pp |
| Failed Verification: Insufficient Funds | 208 | 17.7% | 150 | 16.7% | -58 | -1.00pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 67 | 5.7% | 51 | 5.7% | -16 | -0.02pp |
| Failed Verification: Issuer or Cardholder has put a restriction on the card | 63 | 5.4% | 39 | 4.3% | -24 | -1.02pp |
| Failed Verification: Declined - Call Issuer | 38 | 3.2% | 26 | 2.9% | -12 | -0.34pp |
| Failed Verification: Card Issuer Declined CVV | 41 | 3.5% | 23 | 2.6% | -18 | -0.93pp |
| Failed Verification: Declined | 19 | 1.6% | 22 | 2.4% | +3 | +0.83pp |
| Failed Verification: Processor Declined - Fraud Suspected | 29 | 2.5% | 19 | 2.1% | -10 | -0.35pp |
| Failed Verification: Do Not Honor | 13 | 1.1% | 18 | 2.0% | +5 | +0.90pp |
| Failed Verification: Closed Card | 32 | 2.7% | 17 | 1.9% | -15 | -0.83pp |
| **Total PVS Failures** | **1,175** | **100%** | **898** | **100%** | **-277** | - |

---


---

*Report: 2026-04-27*
