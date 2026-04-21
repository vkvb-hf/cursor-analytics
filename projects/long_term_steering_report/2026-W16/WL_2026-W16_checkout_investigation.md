# PCR Investigation: WL 2026-W16

**Metric:** Payment Conversion Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 34.86% → 35.83% (+0.96pp)  
**Volume:** 31,449 payment visits  
**Threshold:** +0.48pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate improved from 34.86% to 35.83% (+0.96pp) in 2026-W16, exceeding the significance threshold of +0.48pp, while payment visits decreased by 10.0% (31,449 visits).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ≥ +0.48pp | +1.01pp | ✅ |
| Click Submit Form | ≥ +0.48pp | +0.10pp | ⚠️ |
| FE Validation Passed | ≥ +0.48pp | -0.23pp | ⚠️ |
| Enter Fraud Service | ≥ +0.48pp | +0.44pp | ⚠️ |
| Approved by Fraud Service | ≥ +0.48pp | -0.32pp | ⚠️ |
| Call to PVS | ≥ +0.48pp | +0.10pp | ⚠️ |
| Successful Checkout | ≥ +0.48pp | +0.45pp | ⚠️ |

**Key Findings:**
- The primary driver of PCR improvement is the Select Payment Method step (+1.01pp), indicating users are more successfully choosing payment options
- CG showed strong improvement (+1.84pp) driven by Select Payment Method (+2.31pp), while GN improved by +2.21pp with the same key driver (+1.58pp)
- MR experienced a decline (-1.51pp) with Select Payment Method dropping by -1.60pp, partially offsetting overall gains
- Braintree_ApplePay conversion improved (+0.88pp to 92.00%) while ProcessOut_CreditCard declined (-1.25pp to 89.48%)
- Backend data shows PVS Attempt rate improved significantly (+1.55pp to 82.21%), contributing to higher checkout success

**Action:** Monitor - Continue tracking Select Payment Method performance across countries, particularly investigating the decline in MR and ProcessOut_CreditCard performance degradation.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 34,952 | 31,449 | -3,503 | -10.0% | - | - | - |
| Select Payment Method | 15,943 | 14,663 | -1,280 | -8.0% | 45.61% | 46.62% | +1.01pp |
| Click Submit Form | 14,597 | 13,439 | -1,158 | -7.9% | 91.56% | 91.65% | +0.10pp |
| FE Validation Passed | 13,905 | 12,771 | -1,134 | -8.2% | 95.26% | 95.03% | -0.23pp |
| Enter Fraud Service | 13,399 | 12,362 | -1,037 | -7.7% | 96.36% | 96.80% | +0.44pp |
| Approved by Fraud Service | 12,678 | 11,657 | -1,021 | -8.1% | 94.62% | 94.30% | -0.32pp |
| Call to PVS | 12,522 | 11,525 | -997 | -8.0% | 98.77% | 98.87% | +0.10pp |
| **Successful Checkout** | 12,186 | 11,268 | -918 | -7.5% | 97.32% | 97.77% | +0.45pp |
| **PCR Rate** | | | | | 34.86% | 35.83% | **+0.96pp** |

### Waterfall Backend

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 48,823 | 44,009 | -4,814 | -9.9% | - | - | - |
| Checkout Attempt | 15,591 | 14,419 | -1,172 | -7.5% | 31.93% | 32.76% | +0.83pp |
| Enter Fraud Service | 15,513 | 14,379 | -1,134 | -7.3% | 99.50% | 99.72% | +0.22pp |
| Approved by Fraud Service | 14,532 | 13,410 | -1,122 | -7.7% | 93.68% | 93.26% | -0.42pp |
| PVS Attempt | 11,721 | 11,024 | -697 | -5.9% | 80.66% | 82.21% | +1.55pp |
| PVS Success | 11,413 | 10,758 | -655 | -5.7% | 97.37% | 97.59% | +0.21pp |
| **Successful Checkout** | 14,100 | 13,044 | -1,056 | -7.5% | 123.54% | 121.25% | -2.29pp |
| **PCR Rate** | | | | | 28.88% | 29.64% | **+0.76pp** |

### Payment Method Breakdown

| Payment Method | 2026-W15 Attempt | 2026-W15 Success | 2026-W15 Rate | 2026-W16 Attempt | 2026-W16 Success | 2026-W16 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| Braintree_ApplePay | 4,486 | 4,088 | 91.13% | 4,252 | 3,912 | 92.00% | +0.88pp |
| ProcessOut_CreditCard | 4,491 | 4,075 | 90.74% | 4,032 | 3,608 | 89.48% | -1.25pp |
| Adyen_CreditCard | 2,937 | 2,626 | 89.41% | 2,766 | 2,500 | 90.38% | +0.97pp |
| Braintree_Paypal | 1,787 | 1,638 | 91.66% | 1,713 | 1,558 | 90.95% | -0.71pp |
| Braintree_CreditCard | 1,547 | 1,375 | 88.88% | 1,288 | 1,141 | 88.59% | -0.29pp |
| ProcessOut_ApplePay | 339 | 297 | 87.61% | 366 | 324 | 88.52% | +0.91pp |
| Braintree_Venmo | 1 | 1 | 100.00% | 1 | 1 | 100.00% | +0.00pp |
| NoPayment | 3 | 0 | 0.00% | 1 | 0 | 0.00% | +0.00pp |
| CreditCard | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (3 countries in WL)

| Country | Volume | PCR 2026-W15 | PCR 2026-W16 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| MR | 8,568 | 23.35% | 21.84% | -1.51pp | 1 | 3 |
| CG | 3,876 | 45.58% | 47.42% | +1.84pp | 2 | 2 |
| GN | 2,422 | 48.04% | 50.25% | +2.21pp | 4 | 1 |

---

### GN

#### Waterfall GA

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 2,371 | 2,422 | +51 | +2.15pp | - | - | - |
| Select Payment Method | 1,755 | 1,831 | +76 | +4.33pp | 74.02% | 75.60% | +1.58pp |
| Click Submit Form | 1,624 | 1,694 | +70 | +4.31pp | 92.54% | 92.52% | -0.02pp |
| FE Validation Passed | 1,310 | 1,371 | +61 | +4.66pp | 80.67% | 80.93% | +0.27pp |
| Enter Fraud Service | 1,230 | 1,303 | +73 | +5.93pp | 93.89% | 95.04% | +1.15pp |
| Approved by Fraud Service | 1,179 | 1,247 | +68 | +5.77pp | 95.85% | 95.70% | -0.15pp |
| Call to PVS | 1,174 | 1,243 | +69 | +5.88pp | 99.58% | 99.68% | +0.10pp |
| **Successful Checkout** | 1,139 | 1,217 | +78 | +6.85pp | 97.02% | 97.91% | +0.89pp |
| **PCR Rate** | | | | | 48.04% | 50.25% | **+2.21pp** |

**Key Driver:** Select Payment Method (+1.58pp)

#### Waterfall Backend

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 4,033 | 4,034 | +1 | +0.02pp | - | - | - |
| Checkout Attempt | 1,584 | 1,668 | +84 | +5.30pp | 39.28% | 41.35% | +2.07pp |
| Enter Fraud Service | 1,576 | 1,667 | +91 | +5.77pp | 99.49% | 99.94% | +0.45pp |
| Approved by Fraud Service | 1,489 | 1,580 | +91 | +6.11pp | 94.48% | 94.78% | +0.30pp |
| PVS Attempt | 1,334 | 1,329 | -5 | -0.37pp | 89.59% | 84.11% | -5.48pp |
| PVS Success | 1,299 | 1,300 | +1 | +0.08pp | 97.38% | 97.82% | +0.44pp |
| **Successful Checkout** | 1,465 | 1,566 | +101 | +6.89pp | 112.78% | 120.46% | +7.68pp |

**Key Driver:** Successful Checkout (+7.68pp)

---

### MR

#### Waterfall GA

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 9,971 | 8,568 | -1,403 | -14.07pp | - | - | - |
| Select Payment Method | 2,927 | 2,378 | -549 | -18.76pp | 29.36% | 27.75% | -1.60pp |
| Click Submit Form | 2,611 | 2,138 | -473 | -18.12pp | 89.20% | 89.91% | +0.70pp |
| FE Validation Passed | 2,647 | 2,161 | -486 | -18.36pp | 101.38% | 101.08% | -0.30pp |
| Enter Fraud Service | 2,516 | 2,042 | -474 | -18.84pp | 95.05% | 94.49% | -0.56pp |
| Approved by Fraud Service | 2,458 | 1,977 | -481 | -19.57pp | 97.69% | 96.82% | -0.88pp |
| Call to PVS | 2,329 | 1,866 | -463 | -19.88pp | 94.75% | 94.39% | -0.37pp |
| **Successful Checkout** | 2,328 | 1,871 | -457 | -19.63pp | 99.96% | 100.27% | +0.31pp |
| **PCR Rate** | | | | | 23.35% | 21.84% | **-1.51pp** |

**Key Driver:** Select Payment Method (-1.60pp)

#### Waterfall Backend

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 11,687 | 10,070 | -1,617 | -13.84pp | - | - | - |
| Checkout Attempt | 2,756 | 2,243 | -513 | -18.61pp | 23.58% | 22.27% | -1.31pp |
| Enter Fraud Service | 2,754 | 2,241 | -513 | -18.63pp | 99.93% | 99.91% | -0.02pp |
| Approved by Fraud Service | 2,686 | 2,163 | -523 | -19.47pp | 97.53% | 96.52% | -1.01pp |
| PVS Attempt | 68 | 57 | -11 | -16.18pp | 2.53% | 2.64% | +0.10pp |
| PVS Success | 65 | 56 | -9 | -13.85pp | 95.59% | 98.25% | +2.66pp |
| **Successful Checkout** | 2,566 | 2,051 | -515 | -20.07pp | 3947.69% | 3662.50% | -285.19pp |

**Key Driver:** Successful Checkout (-285.19pp)

---

### CG

#### Waterfall GA

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 3,901 | 3,876 | -25 | -0.64pp | - | - | - |
| Select Payment Method | 2,285 | 2,360 | +75 | +3.28pp | 58.57% | 60.89% | +2.31pp |
| Click Submit Form | 2,131 | 2,200 | +69 | +3.24pp | 93.26% | 93.22% | -0.04pp |
| FE Validation Passed | 1,992 | 2,057 | +65 | +3.26pp | 93.48% | 93.50% | +0.02pp |
| Enter Fraud Service | 1,961 | 2,022 | +61 | +3.11pp | 98.44% | 98.30% | -0.15pp |
| Approved by Fraud Service | 1,844 | 1,884 | +40 | +2.17pp | 94.03% | 93.18% | -0.86pp |
| Call to PVS | 1,825 | 1,872 | +47 | +2.58pp | 98.97% | 99.36% | +0.39pp |
| **Successful Checkout** | 1,778 | 1,838 | +60 | +3.37pp | 97.42% | 98.18% | +0.76pp |
| **PCR Rate** | | | | | 45.58% | 47.42% | **+1.84pp** |

**Key Driver:** Select Payment Method (+2.31pp)

#### Waterfall Backend

| Funnel Step | 2026-W15 | 2026-W16 | Δ Count | Δ % | 2026-W15 Conv | 2026-W16 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 6,437 | 6,282 | -155 | -2.41pp | - | - | - |
| Checkout Attempt | 2,205 | 2,257 | +52 | +2.36pp | 34.26% | 35.93% | +1.67pp |
| Enter Fraud Service | 2,195 | 2,254 | +59 | +2.69pp | 99.55% | 99.87% | +0.32pp |
| Approved by Fraud Service | 2,057 | 2,094 | +37 | +1.80pp | 93.71% | 92.90% | -0.81pp |
| PVS Attempt | 2,029 | 2,074 | +45 | +2.22pp | 98.64% | 99.04% | +0.41pp |
| PVS Success | 1,985 | 2,028 | +43 | +2.17pp | 97.83% | 97.78% | -0.05pp |
| **Successful Checkout** | 1,990 | 2,039 | +49 | +2.46pp | 100.25% | 100.54% | +0.29pp |

**Key Driver:** Checkout Attempt (+1.67pp)

---





---

*Report: 2026-04-21*
