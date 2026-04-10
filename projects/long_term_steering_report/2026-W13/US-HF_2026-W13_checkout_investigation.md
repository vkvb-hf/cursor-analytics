# PCR Investigation: US-HF 2026-W13

**Metric:** Payment Conversion Rate  
**Period:** 2026-W12 → 2026-W13  
**Observation:** 26.18% → 26.77% (+0.59pp)  
**Volume:** 44,370 payment visits  
**Threshold:** +0.30pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate improved by +0.59pp (26.18% → 26.77%) in 2026-W13, exceeding the +0.30pp threshold, driven primarily by a significant improvement in the Click Submit Form step (+4.21pp).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | vs threshold | -1.27pp | ⚠️ |
| Click Submit Form | vs threshold | +4.21pp | ✅ |
| FE Validation Passed | vs threshold | +1.14pp | ✅ |
| Enter Fraud Service | vs threshold | +0.19pp | ✅ |
| Approved by Fraud Service | vs threshold | -0.32pp | ⚠️ |
| Call to PVS | vs threshold | +0.18pp | ✅ |
| Successful Checkout | vs threshold | -0.52pp | ⚠️ |

**Key Findings:**
- **Click Submit Form conversion surged +4.21pp** (84.09% → 88.30%), the largest positive driver of the overall PCR improvement
- **CC_NO_PREPAID_ERR dropped dramatically** from 250 occurrences (6.2%) to just 2 (0.1%), a -6.19pp reduction indicating a likely policy or validation change that improved FE validation recovery rate to 75.67% (+2.50pp)
- **Payment method mix shift:** ProcessOut_CreditCard attempts increased significantly (6,991 → 10,229) while Braintree_CreditCard dropped sharply (3,268 → 281), suggesting a PSP routing change
- **Adyen_CreditCard introduced** with 108 checkout attempts but 0% success rate, creating a 100% gap (108 transactions) between Checkout Attempt and Enter Fraud Service
- **PVS "Blocked Verification" errors increased** (+56 occurrences, +2.73pp share) becoming the dominant decline reason at 55.4% of all PVS failures

**Action:** **Investigate** - The new Adyen_CreditCard integration requires immediate attention due to 100% failure rate at fraud service entry. Monitor the impact of the PSP routing change from Braintree to ProcessOut on overall conversion.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 46,444 | 44,370 | -2,074 | -4.5% | - | - | - |
| Select Payment Method | 18,056 | 16,684 | -1,372 | -7.6% | 38.88% | 37.60% | -1.27pp |
| Click Submit Form | 15,184 | 14,732 | -452 | -3.0% | 84.09% | 88.30% | +4.21pp |
| FE Validation Passed | 14,250 | 13,994 | -256 | -1.8% | 93.85% | 94.99% | +1.14pp |
| Enter Fraud Service | 13,938 | 13,714 | -224 | -1.6% | 97.81% | 98.00% | +0.19pp |
| Approved by Fraud Service | 13,102 | 12,848 | -254 | -1.9% | 94.00% | 93.69% | -0.32pp |
| Call to PVS | 13,082 | 12,852 | -230 | -1.8% | 99.85% | 100.03% | +0.18pp |
| **Successful Checkout** | 12,160 | 11,879 | -281 | -2.3% | 92.95% | 92.43% | -0.52pp |
| **PCR Rate** | | | | | 26.18% | 26.77% | **+0.59pp** |

### Waterfall Backend

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 50,863 | 48,829 | -2,034 | -4.0% | - | - | - |
| Checkout Attempt | 17,752 | 17,802 | 50 | 0.3% | 34.90% | 36.46% | +1.56pp |
| Enter Fraud Service | 17,717 | 17,647 | -70 | -0.4% | 99.80% | 99.13% | -0.67pp |
| Approved by Fraud Service | 15,978 | 15,733 | -245 | -1.5% | 90.18% | 89.15% | -1.03pp |
| PVS Attempt | 15,651 | 15,361 | -290 | -1.9% | 97.95% | 97.64% | -0.32pp |
| PVS Success | 14,543 | 14,219 | -324 | -2.2% | 92.92% | 92.57% | -0.35pp |
| **Successful Checkout** | 14,106 | 13,849 | -257 | -1.8% | 97.00% | 97.40% | +0.40pp |
| **PCR Rate** | | | | | 27.73% | 28.36% | **+0.63pp** |

### Payment Method Breakdown

| Payment Method | 2026-W12 Attempt | 2026-W12 Success | 2026-W12 Rate | 2026-W13 Attempt | 2026-W13 Success | 2026-W13 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 6,991 | 5,697 | 81.49% | 10,229 | 8,111 | 79.29% | -2.20pp |
| Braintree_ApplePay | 5,978 | 4,515 | 75.53% | 5,750 | 4,354 | 75.72% | +0.19pp |
| Braintree_Paypal | 1,395 | 1,187 | 85.09% | 1,298 | 1,131 | 87.13% | +2.04pp |
| Braintree_CreditCard | 3,268 | 2,706 | 82.80% | 281 | 253 | 90.04% | +7.23pp |
|  | 119 | 0 | 0.00% | 136 | 0 | 0.00% | +0.00pp |
| Adyen_CreditCard | 0 | 0 | 0.00% | 108 | 0 | 0.00% | +0.00pp |
| Braintree_Venmo | 1 | 1 | 100.00% | 0 | 0 | 0.00% | -100.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (1 countries in US-HF)

| Country | Volume | PCR 2026-W12 | PCR 2026-W13 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| US | 44,370 | 26.18% | 26.77% | +0.59pp | 1 | 1 |

---

### US

#### Waterfall GA

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 46,444 | 44,370 | -2,074 | -4.47pp | - | - | - |
| Select Payment Method | 18,056 | 16,684 | -1,372 | -7.60pp | 38.88% | 37.60% | -1.27pp |
| Click Submit Form | 15,184 | 14,732 | -452 | -2.98pp | 84.09% | 88.30% | +4.21pp |
| FE Validation Passed | 14,250 | 13,994 | -256 | -1.80pp | 93.85% | 94.99% | +1.14pp |
| Enter Fraud Service | 13,938 | 13,714 | -224 | -1.61pp | 97.81% | 98.00% | +0.19pp |
| Approved by Fraud Service | 13,102 | 12,848 | -254 | -1.94pp | 94.00% | 93.69% | -0.32pp |
| Call to PVS | 13,082 | 12,852 | -230 | -1.76pp | 99.85% | 100.03% | +0.18pp |
| **Successful Checkout** | 12,160 | 11,879 | -281 | -2.31pp | 92.95% | 92.43% | -0.52pp |
| **PCR Rate** | | | | | 26.18% | 26.77% | **+0.59pp** |

**Key Driver:** Click Submit Form (+4.21pp)

#### Waterfall Backend

| Funnel Step | 2026-W12 | 2026-W13 | Δ Count | Δ % | 2026-W12 Conv | 2026-W13 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 50,863 | 48,829 | -2,034 | -4.00pp | - | - | - |
| Checkout Attempt | 17,752 | 17,802 | +50 | +0.28pp | 34.90% | 36.46% | +1.56pp |
| Enter Fraud Service | 17,717 | 17,647 | -70 | -0.40pp | 99.80% | 99.13% | -0.67pp |
| Approved by Fraud Service | 15,978 | 15,733 | -245 | -1.53pp | 90.18% | 89.15% | -1.03pp |
| PVS Attempt | 15,651 | 15,361 | -290 | -1.85pp | 97.95% | 97.64% | -0.32pp |
| PVS Success | 14,543 | 14,219 | -324 | -2.23pp | 92.92% | 92.57% | -0.35pp |
| **Successful Checkout** | 14,855 | 14,691 | -164 | -1.10pp | 102.15% | 103.32% | +1.17pp |

**Key Driver:** Checkout Attempt (+1.56pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (+1.14pp) meets threshold (+0.30pp)

### Recovery Rate

| Metric | 2026-W12 | 2026-W13 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 4,003 | 3,678 | -325 |
| Error → Passed | 2,929 | 2,783 | -146 |
| **Recovery Rate** | **73.17%** | **75.67%** | **+2.50pp** |

### Error Type Distribution

| Error Type | 2026-W12 | 2026-W12 % | 2026-W13 | 2026-W13 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| terms_not_accepted | 2,074 | 51.8% | 2,064 | 56.1% | +4.31pp |
| APPLEPAY_DISMISSED | 1,949 | 48.7% | 1,840 | 50.0% | +1.34pp |
| PAYPAL_POPUP_CLOSED | 268 | 6.7% | 273 | 7.4% | +0.73pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 213 | 5.3% | 235 | 6.4% | +1.07pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 109 | 2.7% | 102 | 2.8% | +0.05pp |
| CC_TOKENISE_ERR | 91 | 2.3% | 102 | 2.8% | +0.50pp |
| PAYPAL_TOKENISE_ERR | 33 | 0.8% | 24 | 0.7% | -0.17pp |
| CC_NO_PREPAID_ERR | 250 | 6.2% | 2 | 0.1% | -6.19pp |
| APPLEPAY_MERCHANT_VALIDATION_ERR | 3 | 0.1% | 0 | 0.0% | -0.07pp |
| VENMO_TOKENISE_ERR | 1 | 0.0% | 0 | 0.0% | -0.02pp |


---

## Fraud Analysis

**Include reason:** Approved Δ (-0.32pp) meets threshold (+0.30pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W12 | 2026-W12 % | 2026-W13 | 2026-W13 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 17,752 | - | 17,802 | - | 50 | 0.3% |
| Enter Fraud Service | 17,717 | - | 17,647 | - | -70 | -0.4% |
| **Gap (Skipped)** | **35** | **0.20%** | **155** | **0.87%** | **120** | **+0.67pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W12 Gap | 2026-W12 % | 2026-W13 Gap | 2026-W13 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Adyen_CreditCard | 0 | 0.0% | 108 | 69.7% | +108 | +69.68pp |
| ProcessOut_CreditCard | 17 | 48.6% | 27 | 17.4% | +10 | -31.15pp |
| Braintree_ApplePay | 8 | 22.9% | 19 | 12.3% | +11 | -10.60pp |
| Braintree_Paypal | 5 | 14.3% | 1 | 0.6% | -4 | -13.64pp |
| Braintree_CreditCard | 4 | 11.4% | 0 | 0.0% | -4 | -11.43pp |
|  | 1 | 2.9% | 0 | 0.0% | -1 | -2.86pp |
| **Total** | **35** | **100%** | **155** | **100%** | **120** | - |

*% of Gap = Payment Method Gap / Total Gap*

---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (-0.52pp) meets threshold (+0.30pp)

| Decline Reason | 2026-W12 | 2026-W12 % | 2026-W13 | 2026-W13 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Blocked Verification: Payment method is blocked due to business reasons | 514 | 52.7% | 570 | 55.4% | +56 | +2.73pp |
| Failed Verification: Insufficient Funds | 199 | 20.4% | 166 | 16.1% | -33 | -4.26pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 58 | 5.9% | 64 | 6.2% | +6 | +0.28pp |
| Failed Verification: Card Not Activated | 43 | 4.4% | 38 | 3.7% | -5 | -0.71pp |
| Failed Verification: Card Issuer Declined CVV | 48 | 4.9% | 37 | 3.6% | -11 | -1.32pp |
| Failed Verification: Declined - Call Issuer | 22 | 2.3% | 36 | 3.5% | +14 | +1.25pp |
| Failed Verification: Issuer or Cardholder has put a restriction on the card | 19 | 1.9% | 36 | 3.5% | +17 | +1.55pp |
| Failed Verification: Closed Card | 28 | 2.9% | 33 | 3.2% | +5 | +0.34pp |
| Failed Verification: Cannot Authorize at this time (Policy) | 17 | 1.7% | 28 | 2.7% | +11 | +0.98pp |
| Failed Verification: Processor Declined | 27 | 2.8% | 20 | 1.9% | -7 | -0.82pp |
| **Total PVS Failures** | **975** | **100%** | **1,028** | **100%** | **+53** | - |

---


---

*Report: 2026-04-10*
