# PCR Investigation: US-HF 2026-W14

**Metric:** Payment Conversion Rate  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 26.77% → 26.41% (-0.37pp)  
**Volume:** 44,056 payment visits  
**Threshold:** +0.18pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate declined by -0.37pp (from 26.77% to 26.41%) in US-HF for 2026-W14, with 44,056 payment visits processed.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Rate vs threshold | -0.42pp | ⚠️ |
| Click Submit Form | Rate vs threshold | +0.02pp | ✅ |
| FE Validation Passed | Rate vs threshold | -0.41pp | ⚠️ |
| Enter Fraud Service | Rate vs threshold | +0.12pp | ✅ |
| Approved by Fraud Service | Rate vs threshold | -0.01pp | ✅ |
| Call to PVS | Rate vs threshold | -0.24pp | ⚠️ |
| Successful Checkout | Rate vs threshold | +0.26pp | ✅ |

**Key Findings:**
- **Select Payment Method is the primary drop-off point:** Conversion decreased by -0.42pp (from 37.60% to 37.18%), indicating fewer visitors are proceeding to select a payment option
- **FE Validation recovery rate declined:** Recovery rate dropped from 75.67% to 74.36% (-1.31pp), with "terms_not_accepted" remaining the top error at 51.6% of customers with errors
- **Backend shows improvement in Fraud Service approval:** Approved by Fraud Service improved significantly by +2.75pp (from 89.15% to 91.91%), partially offsetting upstream losses
- **ProcessOut_CreditCard and Braintree_ApplePay success rates improved:** ProcessOut_CreditCard increased +3.21pp (to 82.50%) and ApplePay increased +2.28pp (to 78.00%)
- **PVS failures decreased:** Total PVS failures dropped from 1,013 to 958 (-55 failures), with "Card Not Activated" errors down -1.14pp

**Action:** Investigate - Focus on the Select Payment Method drop-off and FE Validation issues, particularly the "terms_not_accepted" errors which affect over 50% of customers encountering FE errors.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 44,370 | 44,056 | -314 | -0.7% | - | - | - |
| Select Payment Method | 16,684 | 16,381 | -303 | -1.8% | 37.60% | 37.18% | -0.42pp |
| Click Submit Form | 14,732 | 14,468 | -264 | -1.8% | 88.30% | 88.32% | +0.02pp |
| FE Validation Passed | 13,994 | 13,684 | -310 | -2.2% | 94.99% | 94.58% | -0.41pp |
| Enter Fraud Service | 13,714 | 13,426 | -288 | -2.1% | 98.00% | 98.11% | +0.12pp |
| Approved by Fraud Service | 12,848 | 12,577 | -271 | -2.1% | 93.69% | 93.68% | -0.01pp |
| Call to PVS | 12,852 | 12,551 | -301 | -2.3% | 100.03% | 99.79% | -0.24pp |
| **Successful Checkout** | 11,879 | 11,634 | -245 | -2.1% | 92.43% | 92.69% | +0.26pp |
| **PCR Rate** | | | | | 26.77% | 26.41% | **-0.37pp** |

### Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 48,829 | 47,792 | -1,037 | -2.1% | - | - | - |
| Checkout Attempt | 17,802 | 16,949 | -853 | -4.8% | 36.46% | 35.46% | -0.99pp |
| Enter Fraud Service | 17,647 | 16,671 | -976 | -5.5% | 99.13% | 98.36% | -0.77pp |
| Approved by Fraud Service | 15,733 | 15,322 | -411 | -2.6% | 89.15% | 91.91% | +2.75pp |
| PVS Attempt | 15,361 | 14,911 | -450 | -2.9% | 97.64% | 97.32% | -0.32pp |
| PVS Success | 14,219 | 13,845 | -374 | -2.6% | 92.57% | 92.85% | +0.29pp |
| **Successful Checkout** | 13,849 | 13,514 | -335 | -2.4% | 97.40% | 97.61% | +0.21pp |
| **PCR Rate** | | | | | 28.36% | 28.28% | **-0.09pp** |

### Payment Method Breakdown

| Payment Method | 2026-W13 Attempt | 2026-W13 Success | 2026-W13 Rate | 2026-W14 Attempt | 2026-W14 Success | 2026-W14 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 10,229 | 8,111 | 79.29% | 9,309 | 7,680 | 82.50% | +3.21pp |
| Braintree_ApplePay | 5,750 | 4,354 | 75.72% | 5,745 | 4,481 | 78.00% | +2.28pp |
| Braintree_Paypal | 1,298 | 1,131 | 87.13% | 1,384 | 1,193 | 86.20% | -0.93pp |
| Adyen_CreditCard | 108 | 0 | 0.00% | 212 | 0 | 0.00% | +0.00pp |
| Braintree_CreditCard | 281 | 253 | 90.04% | 178 | 158 | 88.76% | -1.27pp |
|  | 136 | 0 | 0.00% | 120 | 1 | 0.83% | +0.83pp |
| Braintree_Venmo | 0 | 0 | 0.00% | 1 | 1 | 100.00% | +100.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (1 countries in US-HF)

| Country | Volume | PCR 2026-W13 | PCR 2026-W14 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| US | 44,056 | 26.77% | 26.41% | -0.36pp | 1 | 1 |

---

### US

#### Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 44,370 | 44,056 | -314 | -0.71pp | - | - | - |
| Select Payment Method | 16,684 | 16,381 | -303 | -1.82pp | 37.60% | 37.18% | -0.42pp |
| Click Submit Form | 14,732 | 14,468 | -264 | -1.79pp | 88.30% | 88.32% | +0.02pp |
| FE Validation Passed | 13,994 | 13,684 | -310 | -2.22pp | 94.99% | 94.58% | -0.41pp |
| Enter Fraud Service | 13,714 | 13,426 | -288 | -2.10pp | 98.00% | 98.11% | +0.12pp |
| Approved by Fraud Service | 12,848 | 12,577 | -271 | -2.11pp | 93.69% | 93.68% | -0.01pp |
| Call to PVS | 12,852 | 12,551 | -301 | -2.34pp | 100.03% | 99.79% | -0.24pp |
| **Successful Checkout** | 11,879 | 11,634 | -245 | -2.06pp | 92.43% | 92.69% | +0.26pp |
| **PCR Rate** | | | | | 26.77% | 26.41% | **-0.37pp** |

**Key Driver:** Select Payment Method (-0.42pp)

#### Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 48,829 | 47,792 | -1,037 | -2.12pp | - | - | - |
| Checkout Attempt | 17,802 | 16,949 | -853 | -4.79pp | 36.46% | 35.46% | -0.99pp |
| Enter Fraud Service | 17,647 | 16,671 | -976 | -5.53pp | 99.13% | 98.36% | -0.77pp |
| Approved by Fraud Service | 15,733 | 15,322 | -411 | -2.61pp | 89.15% | 91.91% | +2.75pp |
| PVS Attempt | 15,361 | 14,911 | -450 | -2.93pp | 97.64% | 97.32% | -0.32pp |
| PVS Success | 14,219 | 13,845 | -374 | -2.63pp | 92.57% | 92.85% | +0.29pp |
| **Successful Checkout** | 14,691 | 14,421 | -270 | -1.84pp | 103.32% | 104.16% | +0.84pp |

**Key Driver:** Approved by Fraud Service (+2.75pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (-0.41pp) meets threshold (+0.18pp)

### Recovery Rate

| Metric | 2026-W13 | 2026-W14 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 3,678 | 3,553 | -125 |
| Error → Passed | 2,783 | 2,642 | -141 |
| **Recovery Rate** | **75.67%** | **74.36%** | **-1.31pp** |

### Error Type Distribution

| Error Type | 2026-W13 | 2026-W13 % | 2026-W14 | 2026-W14 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| terms_not_accepted | 2,064 | 56.1% | 1,834 | 51.6% | -4.50pp |
| APPLEPAY_DISMISSED | 1,840 | 50.0% | 1,805 | 50.8% | +0.77pp |
| PAYPAL_POPUP_CLOSED | 273 | 7.4% | 254 | 7.1% | -0.27pp |
| APPLEPAY_ADDRESS_ZIPCODE_VALIDATION_ERR | 235 | 6.4% | 223 | 6.3% | -0.11pp |
| APPLEPAY_ADDRESS_EMPTY_NAME_ERR | 102 | 2.8% | 113 | 3.2% | +0.41pp |
| CC_TOKENISE_ERR | 102 | 2.8% | 108 | 3.0% | +0.27pp |
| PAYPAL_TOKENISE_ERR | 24 | 0.7% | 23 | 0.6% | -0.01pp |
| CC_NO_PREPAID_ERR | 2 | 0.1% | 2 | 0.1% | +0.00pp |
| EXPRESS_CHECKOUT_APPLEPAY_TOKENISE_ERR | 0 | 0.0% | 1 | 0.0% | +0.03pp |


---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (+0.26pp) meets threshold (+0.18pp)

| Decline Reason | 2026-W13 | 2026-W13 % | 2026-W14 | 2026-W14 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| Blocked Verification: Payment method is blocked due to business reasons | 570 | 56.3% | 534 | 55.7% | -36 | -0.53pp |
| Failed Verification: Insufficient Funds | 166 | 16.4% | 158 | 16.5% | -8 | +0.11pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 64 | 6.3% | 52 | 5.4% | -12 | -0.89pp |
| Failed Verification: Declined - Call Issuer | 36 | 3.6% | 42 | 4.4% | +6 | +0.83pp |
| Failed Verification: Card Issuer Declined CVV | 37 | 3.7% | 34 | 3.5% | -3 | -0.10pp |
| Failed Verification: Issuer or Cardholder has put a restriction on the card | 36 | 3.6% | 33 | 3.4% | -3 | -0.11pp |
| Failed Verification: Cannot Authorize at this time (Policy) | 28 | 2.8% | 29 | 3.0% | +1 | +0.26pp |
| Failed Verification: Processor Declined - Fraud Suspected | 18 | 1.8% | 27 | 2.8% | +9 | +1.04pp |
| Failed Verification: Card Not Activated | 38 | 3.8% | 25 | 2.6% | -13 | -1.14pp |
| Failed Verification: Processor Declined | 20 | 2.0% | 24 | 2.5% | +4 | +0.53pp |
| **Total PVS Failures** | **1,013** | **100%** | **958** | **100%** | **-55** | - |

---


---

*Report: 2026-04-09*
