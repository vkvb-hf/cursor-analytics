# PCR Investigation: WL 2026-W15

**Metric:** Payment Conversion Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 29.88% → 34.85% (+4.97pp)  
**Volume:** 34,943 payment visits  
**Threshold:** +2.48pp (0.5 × |Overall PCR Δ|)

## Executive Summary

**Overall:** Payment Conversion Rate improved significantly from 29.88% to 34.85% (+4.97pp), exceeding the threshold of +2.48pp, driven primarily by substantial gains in the early funnel stage (Select Payment Method).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | >±2.48pp | +4.94pp | ⚠️ |
| Click Submit Form | >±2.48pp | +3.04pp | ⚠️ |
| FE Validation Passed | <±2.48pp | +0.15pp | ✅ |
| Enter Fraud Service | <±2.48pp | +0.15pp | ✅ |
| Approved by Fraud Service | <±2.48pp | +0.02pp | ✅ |
| Call to PVS | <±2.48pp | -0.48pp | ✅ |
| Successful Checkout | <±2.48pp | +0.66pp | ✅ |

**Key Findings:**
- Select Payment Method conversion improved dramatically across all analyzed countries: CG (+14.44pp), AO (+10.21pp), and ER (+9.85pp), indicating a likely UX improvement or marketing change
- Click Submit Form also showed notable improvement (+3.04pp globally), with CG (+5.31pp) and ER (+5.80pp) leading the gains
- Backend data shows a significant drop in PVS Attempt rate (-8.42pp), but this did not negatively impact overall PCR, suggesting improved traffic quality or upstream filtering
- Payment volume decreased slightly (-480 visits, -1.4%), yet absolute successful checkouts increased by 1,593 (+15.1%)
- ProcessOut_ApplePay showed a notable decline (-6.03pp), though with low volume (339 attempts)

**Action:** Monitor - The improvement is positive and widespread across countries. Continue monitoring to confirm the trend is sustained. Investigate the root cause of the Select Payment Method improvement to document and potentially replicate. Also monitor ProcessOut_ApplePay performance given the rate decline.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 35,423 | 34,943 | -480 | -1.4% | - | - | - |
| Select Payment Method | 14,408 | 15,940 | 1,532 | 10.6% | 40.67% | 45.62% | +4.94pp |
| Click Submit Form | 12,752 | 14,593 | 1,841 | 14.4% | 88.51% | 91.55% | +3.04pp |
| FE Validation Passed | 12,132 | 13,906 | 1,774 | 14.6% | 95.14% | 95.29% | +0.15pp |
| Enter Fraud Service | 11,671 | 13,398 | 1,727 | 14.8% | 96.20% | 96.35% | +0.15pp |
| Approved by Fraud Service | 11,037 | 12,673 | 1,636 | 14.8% | 94.57% | 94.59% | +0.02pp |
| Call to PVS | 10,952 | 12,515 | 1,563 | 14.3% | 99.23% | 98.75% | -0.48pp |
| **Successful Checkout** | 10,584 | 12,177 | 1,593 | 15.1% | 96.64% | 97.30% | +0.66pp |
| **PCR Rate** | | | | | 29.88% | 34.85% | **+4.97pp** |

### Waterfall Backend

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 43,656 | 48,823 | 5,167 | 11.8% | - | - | - |
| Checkout Attempt | 13,713 | 15,591 | 1,878 | 13.7% | 31.41% | 31.93% | +0.52pp |
| Enter Fraud Service | 13,666 | 15,513 | 1,847 | 13.5% | 99.66% | 99.50% | -0.16pp |
| Approved by Fraud Service | 12,768 | 14,532 | 1,764 | 13.8% | 93.43% | 93.68% | +0.25pp |
| PVS Attempt | 11,373 | 11,721 | 348 | 3.1% | 89.07% | 80.66% | -8.42pp |
| PVS Success | 11,035 | 11,413 | 378 | 3.4% | 97.03% | 97.37% | +0.34pp |
| **Successful Checkout** | 12,368 | 14,100 | 1,732 | 14.0% | 112.08% | 123.54% | +11.46pp |
| **PCR Rate** | | | | | 28.33% | 28.88% | **+0.55pp** |

### Payment Method Breakdown

| Payment Method | 2026-W14 Attempt | 2026-W14 Success | 2026-W14 Rate | 2026-W15 Attempt | 2026-W15 Success | 2026-W15 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 3,917 | 3,516 | 89.76% | 4,491 | 4,075 | 90.74% | +0.97pp |
| Braintree_ApplePay | 3,733 | 3,417 | 91.53% | 4,486 | 4,088 | 91.13% | -0.41pp |
| Adyen_CreditCard | 2,796 | 2,510 | 89.77% | 2,937 | 2,626 | 89.41% | -0.36pp |
| Braintree_Paypal | 1,663 | 1,503 | 90.38% | 1,787 | 1,638 | 91.66% | +1.28pp |
| Braintree_CreditCard | 1,317 | 1,154 | 87.62% | 1,547 | 1,375 | 88.88% | +1.26pp |
| ProcessOut_ApplePay | 283 | 265 | 93.64% | 339 | 297 | 87.61% | -6.03pp |
| NoPayment | 1 | 0 | 0.00% | 3 | 0 | 0.00% | +0.00pp |
| Braintree_Venmo | 1 | 1 | 100.00% | 1 | 1 | 100.00% | +0.00pp |
|  | 2 | 2 | 100.00% | 0 | 0 | 0.00% | -100.00pp |
| CreditCard | 0 | 0 | 0.00% | 0 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (3 countries in WL)

| Country | Volume | PCR 2026-W14 | PCR 2026-W15 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| CG | 3,899 | 32.74% | 45.60% | +12.86pp | 1 | 1 |
| ER | 4,938 | 29.91% | 39.25% | +9.34pp | 2 | 4 |
| AO | 1,087 | 47.50% | 58.60% | +11.10pp | 7 | 2 |

---

### ER

#### Waterfall GA

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 6,075 | 4,938 | -1,137 | -18.72pp | - | - | - |
| Select Payment Method | 2,616 | 2,613 | -3 | -0.11pp | 43.06% | 52.92% | +9.85pp |
| Click Submit Form | 2,287 | 2,436 | +149 | +6.52pp | 87.42% | 93.23% | +5.80pp |
| FE Validation Passed | 2,071 | 2,222 | +151 | +7.29pp | 90.56% | 91.22% | +0.66pp |
| Enter Fraud Service | 2,031 | 2,167 | +136 | +6.70pp | 98.07% | 97.52% | -0.54pp |
| Approved by Fraud Service | 1,937 | 2,024 | +87 | +4.49pp | 95.37% | 93.40% | -1.97pp |
| Call to PVS | 1,931 | 2,022 | +91 | +4.71pp | 99.69% | 99.90% | +0.21pp |
| **Successful Checkout** | 1,817 | 1,938 | +121 | +6.66pp | 94.10% | 95.85% | +1.75pp |
| **PCR Rate** | | | | | 29.91% | 39.25% | **+9.34pp** |

**Key Driver:** Select Payment Method (+9.85pp)

#### Waterfall Backend

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 7,976 | 8,318 | +342 | +4.29pp | - | - | - |
| Checkout Attempt | 2,496 | 2,621 | +125 | +5.01pp | 31.29% | 31.51% | +0.22pp |
| Enter Fraud Service | 2,496 | 2,620 | +124 | +4.97pp | 100.00% | 99.96% | -0.04pp |
| Approved by Fraud Service | 2,353 | 2,439 | +86 | +3.65pp | 94.27% | 93.09% | -1.18pp |
| PVS Attempt | 2,344 | 2,433 | +89 | +3.80pp | 99.62% | 99.75% | +0.14pp |
| PVS Success | 2,224 | 2,340 | +116 | +5.22pp | 94.88% | 96.18% | +1.30pp |
| **Successful Checkout** | 2,232 | 2,347 | +115 | +5.15pp | 100.36% | 100.30% | -0.06pp |

**Key Driver:** PVS Success (+1.30pp)

---

### AO

#### Waterfall GA

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 1,282 | 1,087 | -195 | -15.21pp | - | - | - |
| Select Payment Method | 822 | 808 | -14 | -1.70pp | 64.12% | 74.33% | +10.21pp |
| Click Submit Form | 766 | 775 | +9 | +1.17pp | 93.19% | 95.92% | +2.73pp |
| FE Validation Passed | 735 | 750 | +15 | +2.04pp | 95.95% | 96.77% | +0.82pp |
| Enter Fraud Service | 708 | 735 | +27 | +3.81pp | 96.33% | 98.00% | +1.67pp |
| Approved by Fraud Service | 634 | 665 | +31 | +4.89pp | 89.55% | 90.48% | +0.93pp |
| Call to PVS | 630 | 664 | +34 | +5.40pp | 99.37% | 99.85% | +0.48pp |
| **Successful Checkout** | 609 | 637 | +28 | +4.60pp | 96.67% | 95.93% | -0.73pp |
| **PCR Rate** | | | | | 47.50% | 58.60% | **+11.10pp** |

**Key Driver:** Select Payment Method (+10.21pp)

#### Waterfall Backend

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 1,760 | 1,900 | +140 | +7.95pp | - | - | - |
| Checkout Attempt | 869 | 900 | +31 | +3.57pp | 49.38% | 47.37% | -2.01pp |
| Enter Fraud Service | 869 | 900 | +31 | +3.57pp | 100.00% | 100.00% | +0.00pp |
| Approved by Fraud Service | 768 | 806 | +38 | +4.95pp | 88.38% | 89.56% | +1.18pp |
| PVS Attempt | 767 | 804 | +37 | +4.82pp | 99.87% | 99.75% | -0.12pp |
| PVS Success | 749 | 783 | +34 | +4.54pp | 97.65% | 97.39% | -0.27pp |
| **Successful Checkout** | 754 | 784 | +30 | +3.98pp | 100.67% | 100.13% | -0.54pp |

**Key Driver:** Checkout Attempt (-2.01pp)

---

### CG

#### Waterfall GA

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 5,375 | 3,899 | -1,476 | -27.46pp | - | - | - |
| Select Payment Method | 2,374 | 2,285 | -89 | -3.75pp | 44.17% | 58.60% | +14.44pp |
| Click Submit Form | 2,088 | 2,131 | +43 | +2.06pp | 87.95% | 93.26% | +5.31pp |
| FE Validation Passed | 1,946 | 1,993 | +47 | +2.42pp | 93.20% | 93.52% | +0.32pp |
| Enter Fraud Service | 1,912 | 1,961 | +49 | +2.56pp | 98.25% | 98.39% | +0.14pp |
| Approved by Fraud Service | 1,814 | 1,844 | +30 | +1.65pp | 94.87% | 94.03% | -0.84pp |
| Call to PVS | 1,804 | 1,825 | +21 | +1.16pp | 99.45% | 98.97% | -0.48pp |
| **Successful Checkout** | 1,760 | 1,778 | +18 | +1.02pp | 97.56% | 97.42% | -0.14pp |
| **PCR Rate** | | | | | 32.74% | 45.60% | **+12.86pp** |

**Key Driver:** Select Payment Method (+14.44pp)

#### Waterfall Backend

| Funnel Step | 2026-W14 | 2026-W15 | Δ Count | Δ % | 2026-W14 Conv | 2026-W15 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 6,536 | 6,437 | -99 | -1.51pp | - | - | - |
| Checkout Attempt | 2,182 | 2,205 | +23 | +1.05pp | 33.38% | 34.26% | +0.87pp |
| Enter Fraud Service | 2,179 | 2,195 | +16 | +0.73pp | 99.86% | 99.55% | -0.32pp |
| Approved by Fraud Service | 2,045 | 2,057 | +12 | +0.59pp | 93.85% | 93.71% | -0.14pp |
| PVS Attempt | 2,031 | 2,029 | -2 | -0.10pp | 99.32% | 98.64% | -0.68pp |
| PVS Success | 1,985 | 1,985 | 0 | +0.00pp | 97.74% | 97.83% | +0.10pp |
| **Successful Checkout** | 1,988 | 1,990 | +2 | +0.10pp | 100.15% | 100.25% | +0.10pp |

**Key Driver:** Checkout Attempt (+0.87pp)

---





---

*Report: 2026-04-14*
