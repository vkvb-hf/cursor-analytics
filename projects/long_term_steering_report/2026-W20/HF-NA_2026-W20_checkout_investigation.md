# PCR Investigation: HF-NA 2026-W20

**Metric:** Payment Conversion Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 25.82% → 25.93% (+0.11pp)  
**Volume:** 62,102 payment visits  
**Threshold:** +0.05pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate for HF-NA improved slightly from 25.82% to 25.93% (+0.11pp) in 2026-W20, driven primarily by gains in CA (+1.02pp) which offset a minor decline in US (-0.07pp).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | vs threshold ±0.05pp | +0.38pp | ⚠️ |
| Click Submit Form | vs threshold ±0.05pp | -0.09pp | ⚠️ |
| FE Validation Passed | vs threshold ±0.05pp | -0.42pp | ⚠️ |
| Enter Fraud Service | vs threshold ±0.05pp | +0.58pp | ⚠️ |
| Approved by Fraud Service | vs threshold ±0.05pp | -0.42pp | ⚠️ |
| Call to PVS | vs threshold ±0.05pp | +0.35pp | ⚠️ |
| Successful Checkout | vs threshold ±0.05pp | -0.48pp | ⚠️ |

**Key Findings:**
- **Braintree_ApplePay experienced a significant decline** in success rate from 76.60% to 67.41% (-9.19pp), representing the largest payment method degradation despite stable volume (~7,400 attempts)
- **CA showed strong improvement** (+1.02pp PCR) driven by Select Payment Method conversion increasing +1.82pp (49.43% → 51.25%), indicating better early-funnel engagement
- **FE Validation errors shifted** with "terms_not_accepted" errors increasing (+3.09pp share) while "APPLEPAY_DISMISSED" decreased (-1.75pp share), though overall recovery rate remained stable at ~69.6%
- **Fraud Service approval improved** in backend (+1.07pp) despite GA showing a decline (-0.42pp), with the gap between Checkout Attempt and Enter Fraud Service narrowing from 1.12% to 0.97%
- **PVS failures remained stable** (-9 total failures) but "Failed Verification: Declined" increased by 15 cases (+0.96pp share)

**Action:** **Investigate** - The -9.19pp decline in Braintree_ApplePay success rate requires immediate investigation as it represents a material degradation in a high-volume payment method (~30% of attempts).

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 65,557 | 62,102 | -3,455 | -5.3% | - | - | - |
| Select Payment Method | 25,499 | 24,394 | -1,105 | -4.3% | 38.90% | 39.28% | +0.38pp |
| Click Submit Form | 21,918 | 20,946 | -972 | -4.4% | 85.96% | 85.87% | -0.09pp |
| FE Validation Passed | 20,549 | 19,550 | -999 | -4.9% | 93.75% | 93.34% | -0.42pp |
| Enter Fraud Service | 19,837 | 18,986 | -851 | -4.3% | 96.54% | 97.12% | +0.58pp |
| Approved by Fraud Service | 18,834 | 17,947 | -887 | -4.7% | 94.94% | 94.53% | -0.42pp |
| Call to PVS | 18,425 | 17,620 | -805 | -4.4% | 97.83% | 98.18% | +0.35pp |
| **Successful Checkout** | 16,924 | 16,100 | -824 | -4.9% | 91.85% | 91.37% | -0.48pp |
| **PCR Rate** | | | | | 25.82% | 25.93% | **+0.11pp** |

### Waterfall Backend

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 70,781 | 65,525 | -5,256 | -7.4% | - | - | - |
| Checkout Attempt | 25,004 | 23,339 | -1,665 | -6.7% | 35.33% | 35.62% | +0.29pp |
| Enter Fraud Service | 24,725 | 23,112 | -1,613 | -6.5% | 98.88% | 99.03% | +0.14pp |
| Approved by Fraud Service | 22,692 | 21,459 | -1,233 | -5.4% | 91.78% | 92.85% | +1.07pp |
| PVS Attempt | 20,728 | 19,621 | -1,107 | -5.3% | 91.34% | 91.43% | +0.09pp |
| PVS Success | 18,867 | 17,792 | -1,075 | -5.7% | 91.02% | 90.68% | -0.34pp |
| **Successful Checkout** | 19,648 | 17,775 | -1,873 | -9.5% | 104.14% | 99.90% | -4.24pp |
| **PCR Rate** | | | | | 27.76% | 27.13% | **-0.63pp** |

### Payment Method Breakdown

| Payment Method | 2026-W19 Attempt | 2026-W19 Success | 2026-W19 Rate | 2026-W20 Attempt | 2026-W20 Success | 2026-W20 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 13,865 | 10,952 | 78.99% | 12,623 | 10,077 | 79.83% | +0.84pp |
| Braintree_ApplePay | 7,715 | 5,910 | 76.60% | 7,426 | 5,006 | 67.41% | -9.19pp |
| Braintree_Paypal | 2,064 | 1,756 | 85.08% | 2,067 | 1,752 | 84.76% | -0.32pp |
| Adyen_CreditCard | 909 | 687 | 75.58% | 901 | 717 | 79.58% | +4.00pp |
| Braintree_CreditCard | 398 | 341 | 85.68% | 259 | 222 | 85.71% | +0.04pp |
| visa | 19 | 0 | 0.00% | 25 | 0 | 0.00% | +0.00pp |
| NoPayment | 7 | 0 | 0.00% | 12 | 0 | 0.00% | +0.00pp |
| paypal | 9 | 0 | 0.00% | 10 | 0 | 0.00% | +0.00pp |
| mc | 8 | 2 | 25.00% | 8 | 0 | 0.00% | -25.00pp |
| amex | 3 | 0 | 0.00% | 4 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (2 countries in HF-NA)

| Country | Volume | PCR 2026-W19 | PCR 2026-W20 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| CA | 13,021 | 32.62% | 33.64% | +1.02pp | 1 | 1 |
| US | 49,081 | 23.95% | 23.88% | -0.07pp | 2 | 2 |

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

### CA

#### Waterfall GA

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 14,114 | 13,021 | -1,093 | -7.74pp | - | - | - |
| Select Payment Method | 6,976 | 6,673 | -303 | -4.34pp | 49.43% | 51.25% | +1.82pp |
| Click Submit Form | 5,665 | 5,402 | -263 | -4.64pp | 81.21% | 80.95% | -0.25pp |
| FE Validation Passed | 5,336 | 5,054 | -282 | -5.28pp | 94.19% | 93.56% | -0.63pp |
| Enter Fraud Service | 5,157 | 4,910 | -247 | -4.79pp | 96.65% | 97.15% | +0.51pp |
| Approved by Fraud Service | 4,852 | 4,598 | -254 | -5.23pp | 94.09% | 93.65% | -0.44pp |
| Call to PVS | 4,756 | 4,519 | -237 | -4.98pp | 98.02% | 98.28% | +0.26pp |
| **Successful Checkout** | 4,604 | 4,380 | -224 | -4.87pp | 96.80% | 96.92% | +0.12pp |
| **PCR Rate** | | | | | 32.62% | 33.64% | **+1.02pp** |

**Key Driver:** Select Payment Method (+1.82pp)

#### Waterfall Backend

| Funnel Step | 2026-W19 | 2026-W20 | Δ Count | Δ % | 2026-W19 Conv | 2026-W20 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 14,742 | 13,462 | -1,280 | -8.68pp | - | - | - |
| Checkout Attempt | 6,019 | 5,749 | -270 | -4.49pp | 40.83% | 42.71% | +1.88pp |
| Enter Fraud Service | 5,984 | 5,679 | -305 | -5.10pp | 99.42% | 98.78% | -0.64pp |
| Approved by Fraud Service | 5,474 | 5,209 | -265 | -4.84pp | 91.48% | 91.72% | +0.25pp |
| PVS Attempt | 4,404 | 4,082 | -322 | -7.31pp | 80.45% | 78.36% | -2.09pp |
| PVS Success | 4,240 | 3,939 | -301 | -7.10pp | 96.28% | 96.50% | +0.22pp |
| **Successful Checkout** | 5,263 | 5,039 | -224 | -4.26pp | 124.13% | 127.93% | +3.80pp |

**Key Driver:** Successful Checkout (+3.80pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (-0.42pp) meets threshold (+0.05pp)

### Recovery Rate

| Metric | 2026-W19 | 2026-W20 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 5,101 | 5,100 | -1 |
| Error → Passed | 3,537 | 3,549 | 12 |
| **Recovery Rate** | **69.34%** | **69.59%** | **+0.25pp** |

### Error Type Distribution

| Error Type | 2026-W19 | 2026-W19 % | 2026-W20 | 2026-W20 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 2,887 | 56.6% | 2,797 | 54.8% | -1.75pp |
| terms_not_accepted | 2,202 | 43.2% | 2,359 | 46.3% | +3.09pp |
| PAYPAL_POPUP_CLOSED | 473 | 9.3% | 509 | 10.0% | +0.71pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 288 | 5.6% | 288 | 5.6% | +0.00pp |
| CC_TOKENISE_ERR | 143 | 2.8% | 147 | 2.9% | +0.08pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 149 | 2.9% | 136 | 2.7% | -0.25pp |
| PAYPAL_TOKENISE_ERR | 51 | 1.0% | 55 | 1.1% | +0.08pp |
| CC_NO_PREPAID_ERR | 7 | 0.1% | 8 | 0.2% | +0.02pp |
| APPLEPAY_MERCHANT_VALIDATION_ERR | 2 | 0.0% | 4 | 0.1% | +0.04pp |


---

## Fraud Analysis

**Include reason:** Enter FS Δ (+0.58pp) meets threshold (+0.05pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W19 | 2026-W19 % | 2026-W20 | 2026-W20 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 25,004 | - | 23,339 | - | -1,665 | -6.7% |
| Enter Fraud Service | 24,725 | - | 23,112 | - | -1,613 | -6.5% |
| **Gap (Skipped)** | **279** | **1.12%** | **227** | **0.97%** | **-52** | **-0.14pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W19 Gap | 2026-W19 % | 2026-W20 Gap | 2026-W20 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Adyen_CreditCard | 162 | 56.6% | 129 | 56.1% | -33 | -0.56pp |
| ProcessOut_CreditCard | 73 | 25.5% | 53 | 23.0% | -20 | -2.48pp |
| Braintree_ApplePay | 32 | 11.2% | 24 | 10.4% | -8 | -0.75pp |
| Braintree_Paypal | 12 | 4.2% | 12 | 5.2% | 0 | +1.02pp |
| NoPayment | 7 | 2.4% | 12 | 5.2% | +5 | +2.77pp |
| **Total** | **286** | **100%** | **230** | **100%** | **-56** | - |

*% of Gap = Payment Method Gap / Total Gap*

---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (-0.48pp) meets threshold (+0.05pp)

| Decline Reason | 2026-W19 | 2026-W19 % | 2026-W20 | 2026-W20 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Blocked Verification: Payment method is blocked due to business reasons | 736 | 46.1% | 690 | 43.4% | -46 | -2.63pp |
| Failed Verification: Insufficient Funds | 452 | 28.3% | 457 | 28.8% | +5 | +0.47pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 112 | 7.0% | 117 | 7.4% | +5 | +0.35pp |
| Failed Verification: Issuer or Cardholder has put a restriction on the card | 76 | 4.8% | 79 | 5.0% | +3 | +0.22pp |
| Failed Verification: Declined | 37 | 2.3% | 52 | 3.3% | +15 | +0.96pp |
| Failed Verification: Declined - Call Issuer | 44 | 2.8% | 44 | 2.8% | 0 | +0.02pp |
| Failed Verification: Card Issuer Declined CVV | 43 | 2.7% | 42 | 2.6% | -1 | -0.05pp |
| Failed Verification: Processor Declined - Fraud Suspected | 41 | 2.6% | 40 | 2.5% | -1 | -0.05pp |
| Failed Verification: Cannot Authorize at this time (Policy) | 23 | 1.4% | 36 | 2.3% | +13 | +0.83pp |
| Failed Verification: Processor Declined | 34 | 2.1% | 32 | 2.0% | -2 | -0.11pp |
| **Total PVS Failures** | **1,598** | **100%** | **1,589** | **100%** | **-9** | - |

---


---

*Report: 2026-05-19*
