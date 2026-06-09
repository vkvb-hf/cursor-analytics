# PCR Investigation: US-HF 2026-W23

**Metric:** Payment Conversion Rate  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 26.16% → 26.03% (-0.13pp)  
**Volume:** 44,580 payment visits  
**Threshold:** +0.06pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined slightly from 26.16% to 26.03% (-0.13pp) in US-HF for 2026-W23, with 44,580 payment visits representing a 2.3% volume increase week-over-week.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Payment Visits → Select Payment Method | Engagement | -0.62pp | ⚠️ |
| Select Payment Method → Click Submit Form | Intent | -0.18pp | ⚠️ |
| Click Submit Form → FE Validation Passed | Validation | -0.56pp | ⚠️ |
| FE Validation Passed → Enter Fraud Service | Fraud Entry | +0.41pp | ✅ |
| Enter Fraud Service → Approved by Fraud Service | Fraud Approval | +0.21pp | ✅ |
| Approved by Fraud Service → Call to PVS | PVS Routing | +1.23pp | ✅ |
| Call to PVS → Successful Checkout | PVS Success | -0.08pp | ⚠️ |

**Key Findings:**
- **FE Validation recovery rate declined** from 72.23% to 69.94% (-2.29pp), with APPLEPAY_DISMISSED (55.1%) and terms_not_accepted (50.9%) remaining the dominant error types
- **Backend shows strong improvement** in Successful Checkout conversion (+11.69pp), contrasting with the GA-measured decline, suggesting potential tracking discrepancies
- **Fraud service gap reduced significantly** from 1.37% to 0.87% (-0.50pp), driven primarily by Adyen_CreditCard gap reduction (-93 transactions)
- **ProcessOut_CreditCard success rate improved substantially** from 72.06% to 84.46% (+12.40pp), indicating payment processor performance gains
- **Top-of-funnel engagement dropped** with Select Payment Method conversion declining -0.62pp, contributing to the overall PCR decrease

**Action:** Monitor — The -0.13pp decline is marginal and within normal variance. Backend metrics show positive trends across payment methods. Focus monitoring on FE validation recovery rate and top-of-funnel engagement for US.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 43,570 | 44,580 | 1,010 | 2.3% | - | - | - |
| Select Payment Method | 16,847 | 16,959 | 112 | 0.7% | 38.67% | 38.04% | -0.62pp |
| Click Submit Form | 14,733 | 14,801 | 68 | 0.5% | 87.45% | 87.28% | -0.18pp |
| FE Validation Passed | 13,827 | 13,808 | -19 | -0.1% | 93.85% | 93.29% | -0.56pp |
| Enter Fraud Service | 13,363 | 13,401 | 38 | 0.3% | 96.64% | 97.05% | +0.41pp |
| Approved by Fraud Service | 12,653 | 12,717 | 64 | 0.5% | 94.69% | 94.90% | +0.21pp |
| Call to PVS | 11,290 | 11,504 | 214 | 1.9% | 89.23% | 90.46% | +1.23pp |
| **Successful Checkout** | 11,399 | 11,606 | 207 | 1.8% | 100.97% | 100.89% | -0.08pp |
| **PCR Rate** | | | | | 26.16% | 26.03% | **-0.13pp** |

### Waterfall Backend

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 40,580 | 48,373 | 7,793 | 19.2% | - | - | - |
| Checkout Attempt | 16,540 | 16,987 | 447 | 2.7% | 40.76% | 35.12% | -5.64pp |
| Enter Fraud Service | 16,313 | 16,839 | 526 | 3.2% | 98.63% | 99.13% | +0.50pp |
| Approved by Fraud Service | 15,221 | 15,750 | 529 | 3.5% | 93.31% | 93.53% | +0.23pp |
| PVS Attempt | 14,808 | 15,305 | 497 | 3.4% | 97.29% | 97.17% | -0.11pp |
| PVS Success | 13,384 | 14,014 | 630 | 4.7% | 90.38% | 91.56% | +1.18pp |
| **Successful Checkout** | 11,015 | 13,172 | 2,157 | 19.6% | 82.30% | 93.99% | +11.69pp |
| **PCR Rate** | | | | | 27.14% | 27.23% | **+0.09pp** |

### Payment Method Breakdown

| Payment Method | 2026-W22 Attempt | 2026-W22 Success | 2026-W22 Rate | 2026-W23 Attempt | 2026-W23 Success | 2026-W23 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 9,136 | 6,583 | 72.06% | 9,445 | 7,977 | 84.46% | +12.40pp |
| Braintree_ApplePay | 5,566 | 3,299 | 59.27% | 5,761 | 3,846 | 66.76% | +7.49pp |
| Braintree_Paypal | 1,337 | 933 | 69.78% | 1,361 | 1,132 | 83.17% | +13.39pp |
| Braintree_CreditCard | 239 | 198 | 82.85% | 245 | 216 | 88.16% | +5.32pp |
| Adyen_CreditCard | 185 | 0 | 0.00% | 92 | 0 | 0.00% | +0.00pp |
| visa | 35 | 1 | 2.86% | 37 | 0 | 0.00% | -2.86pp |
| mc | 24 | 1 | 4.17% | 17 | 0 | 0.00% | -4.17pp |
| paypal | 13 | 0 | 0.00% | 13 | 1 | 7.69% | +7.69pp |
| amex | 3 | 0 | 0.00% | 8 | 0 | 0.00% | +0.00pp |
| discover | 2 | 0 | 0.00% | 8 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (1 countries in US-HF)

| Country | Volume | PCR 2026-W22 | PCR 2026-W23 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| US | 44,580 | 26.16% | 26.03% | -0.13pp | 1 | 1 |

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



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (-0.56pp) meets threshold (+0.06pp)

### Recovery Rate

| Metric | 2026-W22 | 2026-W23 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 3,821 | 3,793 | -28 |
| Error → Passed | 2,760 | 2,653 | -107 |
| **Recovery Rate** | **72.23%** | **69.94%** | **-2.29pp** |

### Error Type Distribution

| Error Type | 2026-W22 | 2026-W22 % | 2026-W23 | 2026-W23 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 2,096 | 54.9% | 2,091 | 55.1% | +0.27pp |
| terms_not_accepted | 1,963 | 51.4% | 1,932 | 50.9% | -0.44pp |
| PAYPAL_POPUP_CLOSED | 268 | 7.0% | 270 | 7.1% | +0.10pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 201 | 5.3% | 215 | 5.7% | +0.41pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 101 | 2.6% | 98 | 2.6% | -0.06pp |
| CC_TOKENISE_ERR | 121 | 3.2% | 91 | 2.4% | -0.77pp |
| PAYPAL_TOKENISE_ERR | 29 | 0.8% | 26 | 0.7% | -0.07pp |
| CC_NO_PREPAID_ERR | 9 | 0.2% | 6 | 0.2% | -0.08pp |
| APPLEPAY_MERCHANT_VALIDATION_ERR | 0 | 0.0% | 3 | 0.1% | +0.08pp |


---

## Fraud Analysis

**Include reason:** Enter FS Δ (+0.41pp) meets threshold (+0.06pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W22 | 2026-W22 % | 2026-W23 | 2026-W23 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 16,540 | - | 16,987 | - | 447 | 2.7% |
| Enter Fraud Service | 16,313 | - | 16,839 | - | 526 | 3.2% |
| **Gap (Skipped)** | **227** | **1.37%** | **148** | **0.87%** | **-79** | **-0.50pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W22 Gap | 2026-W22 % | 2026-W23 Gap | 2026-W23 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Adyen_CreditCard | 185 | 68.8% | 92 | 44.7% | -93 | -24.11pp |
| ProcessOut_CreditCard | 45 | 16.7% | 66 | 32.0% | +21 | +15.31pp |
| Braintree_ApplePay | 27 | 10.0% | 32 | 15.5% | +5 | +5.50pp |
| Braintree_Paypal | 12 | 4.5% | 16 | 7.8% | +4 | +3.31pp |
| **Total** | **269** | **100%** | **206** | **100%** | **-63** | - |

*% of Gap = Payment Method Gap / Total Gap*

---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (-0.08pp) meets threshold (+0.06pp)

| Decline Reason | 2026-W22 | 2026-W22 % | 2026-W23 | 2026-W23 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Blocked Verification: Payment method is blocked due to business reasons | 699 | 59.6% | 652 | 59.5% | -47 | -0.05pp |
| Failed Verification: Insufficient Funds | 224 | 19.1% | 197 | 18.0% | -27 | -1.11pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 97 | 8.3% | 91 | 8.3% | -6 | +0.04pp |
| Failed Verification: Issuer or Cardholder has put a restriction on the card | 62 | 5.3% | 41 | 3.7% | -21 | -1.54pp |
| Failed Verification: Declined | 14 | 1.2% | 30 | 2.7% | +16 | +1.55pp |
| Failed Verification: Closed Card | 10 | 0.9% | 24 | 2.2% | +14 | +1.34pp |
| Failed Verification: Processor Declined - Fraud Suspected | 19 | 1.6% | 18 | 1.6% | -1 | +0.02pp |
| Failed Verification: Cannot Authorize at this time (Policy) | 15 | 1.3% | 15 | 1.4% | 0 | +0.09pp |
| Failed Verification: Expired Card | 17 | 1.4% | 14 | 1.3% | -3 | -0.17pp |
| Failed Verification: Processor Declined | 16 | 1.4% | 13 | 1.2% | -3 | -0.18pp |
| **Total PVS Failures** | **1,173** | **100%** | **1,095** | **100%** | **-78** | - |

---


---

*Report: 2026-06-09*
