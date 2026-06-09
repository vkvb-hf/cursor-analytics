# PCR Investigation: WL 2026-W23

**Metric:** Payment Conversion Rate  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 29.40% → 30.01% (+0.61pp)  
**Volume:** 44,871 payment visits  
**Threshold:** +0.30pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate improved from 29.40% to 30.01% (+0.61pp) in 2026-W23, exceeding the monitoring threshold of +0.30pp, driven primarily by gains in the Select Payment Method step and improved payment method success rates across all providers.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ≥ +0.30pp | +0.27pp | ✅ |
| Click Submit Form | ≥ +0.30pp | +0.34pp | ⚠️ |
| FE Validation Passed | ≥ +0.30pp | +0.51pp | ⚠️ |
| Enter Fraud Service | ≥ +0.30pp | -0.12pp | ✅ |
| Approved by Fraud Service | ≥ +0.30pp | +0.14pp | ✅ |
| Call to PVS | ≥ +0.30pp | +0.50pp | ⚠️ |
| Successful Checkout | ≥ +0.30pp | -0.10pp | ✅ |

**Key Findings:**
- **FE Validation Passed** improved by +0.51pp, with recovery rate increasing from 59.05% to 60.91% (+1.86pp), indicating fewer customers abandoning after validation errors
- **MR** showed strong improvement (+3.67pp PCR), driven by Select Payment Method conversion gains (+3.61pp) with volume increasing 36.74%
- **CK** improved by +4.71pp PCR despite a -19.91% volume decline, with Select Payment Method conversion rising +4.91pp
- All payment methods showed significant success rate improvements: Braintree_ApplePay (+14.61pp), ProcessOut_ApplePay (+15.24pp), Braintree_Paypal (+12.85pp), and ProcessOut_CreditCard (+12.17pp)
- Backend waterfall shows anomalous data with PVS Attempt dropping -20.46pp while Successful Checkout shows +67.39pp, suggesting potential logging or routing changes

**Action:** Monitor - The PCR improvement is positive and driven by legitimate conversion gains across multiple funnel steps and payment methods. Continue monitoring backend logging discrepancies between GA and Backend waterfalls.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 41,501 | 44,871 | 3,370 | 8.1% | - | - | - |
| Select Payment Method | 16,237 | 17,676 | 1,439 | 8.9% | 39.12% | 39.39% | +0.27pp |
| Click Submit Form | 14,322 | 15,651 | 1,329 | 9.3% | 88.21% | 88.54% | +0.34pp |
| FE Validation Passed | 13,844 | 15,208 | 1,364 | 9.9% | 96.66% | 97.17% | +0.51pp |
| Enter Fraud Service | 13,365 | 14,664 | 1,299 | 9.7% | 96.54% | 96.42% | -0.12pp |
| Approved by Fraud Service | 12,758 | 14,019 | 1,261 | 9.9% | 95.46% | 95.60% | +0.14pp |
| Call to PVS | 12,155 | 13,426 | 1,271 | 10.5% | 95.27% | 95.77% | +0.50pp |
| **Successful Checkout** | 12,202 | 13,465 | 1,263 | 10.4% | 100.39% | 100.29% | -0.10pp |
| **PCR Rate** | | | | | 29.40% | 30.01% | **+0.61pp** |

### Waterfall Backend

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 41,220 | 52,484 | 11,264 | 27.3% | - | - | - |
| Checkout Attempt | 14,643 | 16,293 | 1,650 | 11.3% | 35.52% | 31.04% | -4.48pp |
| Enter Fraud Service | 14,555 | 16,203 | 1,648 | 11.3% | 99.40% | 99.45% | +0.05pp |
| Approved by Fraud Service | 13,756 | 15,372 | 1,616 | 11.7% | 94.51% | 94.87% | +0.36pp |
| PVS Attempt | 10,391 | 8,467 | -1,924 | -18.5% | 75.54% | 55.08% | -20.46pp |
| PVS Success | 10,083 | 8,203 | -1,880 | -18.6% | 97.04% | 96.88% | -0.15pp |
| **Successful Checkout** | 11,590 | 14,957 | 3,367 | 29.1% | 114.95% | 182.34% | +67.39pp |
| **PCR Rate** | | | | | 28.12% | 28.50% | **+0.38pp** |

### Payment Method Breakdown

| Payment Method | 2026-W22 Attempt | 2026-W22 Success | 2026-W22 Rate | 2026-W23 Attempt | 2026-W23 Success | 2026-W23 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 3,972 | 3,156 | 79.46% | 5,156 | 4,724 | 91.62% | +12.17pp |
| Braintree_ApplePay | 4,103 | 3,202 | 78.04% | 4,615 | 4,276 | 92.65% | +14.61pp |
| Adyen_CreditCard | 2,882 | 2,319 | 80.46% | 2,675 | 2,477 | 92.60% | +12.13pp |
| Braintree_Paypal | 1,749 | 1,404 | 80.27% | 2,065 | 1,923 | 93.12% | +12.85pp |
| Braintree_CreditCard | 1,633 | 1,288 | 78.87% | 1,479 | 1,291 | 87.29% | +8.42pp |
| ProcessOut_ApplePay | 301 | 221 | 73.42% | 300 | 266 | 88.67% | +15.24pp |
| NoPayment | 3 | 0 | 0.00% | 3 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (2 countries in WL)

| Country | Volume | PCR 2026-W22 | PCR 2026-W23 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| MR | 18,514 | 21.98% | 25.65% | +3.67pp | 1 | 2 |
| CK | 4,497 | 42.05% | 46.76% | +4.71pp | 2 | 1 |

---

### MR

#### Waterfall GA

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 13,540 | 18,514 | +4,974 | +36.74pp | - | - | - |
| Select Payment Method | 3,733 | 5,773 | +2,040 | +54.65pp | 27.57% | 31.18% | +3.61pp |
| Click Submit Form | 3,312 | 5,183 | +1,871 | +56.49pp | 88.72% | 89.78% | +1.06pp |
| FE Validation Passed | 3,371 | 5,247 | +1,876 | +55.65pp | 101.78% | 101.23% | -0.55pp |
| Enter Fraud Service | 3,211 | 5,017 | +1,806 | +56.24pp | 95.25% | 95.62% | +0.36pp |
| Approved by Fraud Service | 3,159 | 4,944 | +1,785 | +56.51pp | 98.38% | 98.54% | +0.16pp |
| Call to PVS | 2,971 | 4,744 | +1,773 | +59.68pp | 94.05% | 95.95% | +1.91pp |
| **Successful Checkout** | 2,976 | 4,748 | +1,772 | +59.54pp | 100.17% | 100.08% | -0.08pp |
| **PCR Rate** | | | | | 21.98% | 25.65% | **+3.67pp** |

**Key Driver:** Select Payment Method (+3.61pp)

#### Waterfall Backend

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 13,208 | 21,467 | +8,259 | +62.53pp | - | - | - |
| Checkout Attempt | 3,367 | 5,429 | +2,062 | +61.24pp | 25.49% | 25.29% | -0.20pp |
| Enter Fraud Service | 3,362 | 5,418 | +2,056 | +61.15pp | 99.85% | 99.80% | -0.05pp |
| Approved by Fraud Service | 3,306 | 5,330 | +2,024 | +61.22pp | 98.33% | 98.38% | +0.04pp |
| PVS Attempt | 125 | 113 | -12 | -9.60pp | 3.78% | 2.12% | -1.66pp |
| PVS Success | 122 | 112 | -10 | -8.20pp | 97.60% | 99.12% | +1.52pp |
| **Successful Checkout** | 3,183 | 5,214 | +2,031 | +63.81pp | 2609.02% | 4655.36% | +2046.34pp |

**Key Driver:** Successful Checkout (+2046.34pp)

---

### CK

#### Waterfall GA

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 5,615 | 4,497 | -1,118 | -19.91pp | - | - | - |
| Select Payment Method | 2,907 | 2,549 | -358 | -12.32pp | 51.77% | 56.68% | +4.91pp |
| Click Submit Form | 2,665 | 2,333 | -332 | -12.46pp | 91.68% | 91.53% | -0.15pp |
| FE Validation Passed | 2,593 | 2,287 | -306 | -11.80pp | 97.30% | 98.03% | +0.73pp |
| Enter Fraud Service | 2,541 | 2,253 | -288 | -11.33pp | 97.99% | 98.51% | +0.52pp |
| Approved by Fraud Service | 2,452 | 2,169 | -283 | -11.54pp | 96.50% | 96.27% | -0.23pp |
| Call to PVS | 2,358 | 2,100 | -258 | -10.94pp | 96.17% | 96.82% | +0.65pp |
| **Successful Checkout** | 2,361 | 2,103 | -258 | -10.93pp | 100.13% | 100.14% | +0.02pp |
| **PCR Rate** | | | | | 42.05% | 46.76% | **+4.72pp** |

**Key Driver:** Select Payment Method (+4.91pp)

#### Waterfall Backend

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 5,263 | 4,936 | -327 | -6.21pp | - | - | - |
| Checkout Attempt | 2,655 | 2,405 | -250 | -9.42pp | 50.45% | 48.72% | -1.72pp |
| Enter Fraud Service | 2,653 | 2,401 | -252 | -9.50pp | 99.92% | 99.83% | -0.09pp |
| Approved by Fraud Service | 2,534 | 2,294 | -240 | -9.47pp | 95.51% | 95.54% | +0.03pp |
| PVS Attempt | 2,534 | 2,292 | -242 | -9.55pp | 100.00% | 99.91% | -0.09pp |
| PVS Success | 2,457 | 2,241 | -216 | -8.79pp | 96.96% | 97.77% | +0.81pp |
| **Successful Checkout** | 2,473 | 2,252 | -221 | -8.94pp | 100.65% | 100.49% | -0.16pp |

**Key Driver:** Checkout Attempt (-1.72pp)

---



## FE Validation Errors

**Include reason:** FE Validation Passed Δ Conv (+0.51pp) meets threshold (+0.30pp)

### Recovery Rate

| Metric | 2026-W22 | 2026-W23 | Δ |
|--------|-------------|-----------------|---|
| Customers with FE Error | 1,663 | 1,627 | -36 |
| Error → Passed | 982 | 991 | 9 |
| **Recovery Rate** | **59.05%** | **60.91%** | **+1.86pp** |

### Error Type Distribution

| Error Type | 2026-W22 | 2026-W22 % | 2026-W23 | 2026-W23 % | Δ % |
| ---------- | ----------- | ------------- | --------------- | ----------------- | ----- |
| APPLEPAY_DISMISSED | 1,063 | 63.9% | 1,107 | 68.0% | +4.12pp |
| terms_not_accepted | 635 | 38.2% | 577 | 35.5% | -2.72pp |
| PAYPAL_POPUP_CLOSED | 264 | 15.9% | 242 | 14.9% | -1.00pp |
| CC_TOKENISE_ERR | 18 | 1.1% | 24 | 1.5% | +0.39pp |
| PAYPAL_TOKENISE_ERR | 19 | 1.1% | 19 | 1.2% | +0.03pp |


---


---

*Report: 2026-06-09*
