# PCR Investigation: WL 2026-W18

**Metric:** Payment Conversion Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 31.86% → 29.74% (-2.11pp)  
**Volume:** 37,721 payment visits  
**Threshold:** +1.06pp (0.5 × |Overall PCR Δ|)

## Executive Summary

**Overall:** Payment Conversion Rate declined by -2.11pp (from 31.86% to 29.74%) in 2026-W18, driven primarily by a significant drop in the Select Payment Method step across all analyzed countries.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | Δ > 1.06pp | -2.89pp | ⚠️ |
| Click Submit Form | Δ > 1.06pp | -0.23pp | ✅ |
| FE Validation Passed | Δ > 1.06pp | +0.06pp | ✅ |
| Enter Fraud Service | Δ > 1.06pp | -0.84pp | ✅ |
| Approved by Fraud Service | Δ > 1.06pp | +1.28pp | ⚠️ |
| Call to PVS | Δ > 1.06pp | +0.34pp | ✅ |
| Successful Checkout | Δ > 1.06pp | -0.54pp | ✅ |

**Key Findings:**
- **Select Payment Method is the primary bottleneck:** The conversion from Payment Visits to Select Payment Method dropped -2.89pp overall, with AO experiencing the steepest decline (-9.97pp), followed by CK (-4.79pp) and ER (-3.61pp)
- **Volume increased but conversion suffered:** Payment visits grew +8.4% (from 34,795 to 37,721), but the increased traffic did not convert proportionally, suggesting potential traffic quality issues or UX friction
- **PVS Success shows backend degradation:** Backend data reveals PVS Success rate declined -1.01pp overall, with ER showing -1.46pp and AO showing -2.10pp drops
- **Fraud Service approval improved:** Despite overall PCR decline, Approved by Fraud Service rate increased +1.28pp (exceeding threshold), indicating fraud is not a contributing factor to the decline
- **AO shows severe underperformance:** AO experienced a -10.06pp PCR drop with checkout attempts down -19.29% while maintaining stable visit volume, indicating a significant country-specific issue

**Action:** Investigate - Focus immediate analysis on the Select Payment Method step, particularly in AO and CK where the largest drops occurred. Investigate potential causes including: payment method display issues, page load performance, or changes to the payment selection UI that may have impacted user engagement.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 34,795 | 37,721 | 2,926 | 8.4% | - | - | - |
| Select Payment Method | 15,001 | 15,173 | 172 | 1.1% | 43.11% | 40.22% | -2.89pp |
| Click Submit Form | 13,364 | 13,482 | 118 | 0.9% | 89.09% | 88.86% | -0.23pp |
| FE Validation Passed | 12,868 | 12,990 | 122 | 0.9% | 96.29% | 96.35% | +0.06pp |
| Enter Fraud Service | 12,424 | 12,433 | 9 | 0.1% | 96.55% | 95.71% | -0.84pp |
| Approved by Fraud Service | 11,607 | 11,774 | 167 | 1.4% | 93.42% | 94.70% | +1.28pp |
| Call to PVS | 11,444 | 11,649 | 205 | 1.8% | 98.60% | 98.94% | +0.34pp |
| **Successful Checkout** | 11,084 | 11,220 | 136 | 1.2% | 96.85% | 96.32% | -0.54pp |
| **PCR Rate** | | | | | 31.86% | 29.74% | **-2.11pp** |

### Waterfall Backend

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 43,233 | 44,387 | 1,154 | 2.7% | - | - | - |
| Checkout Attempt | 14,388 | 14,203 | -185 | -1.3% | 33.28% | 32.00% | -1.28pp |
| Enter Fraud Service | 14,296 | 14,119 | -177 | -1.2% | 99.36% | 99.41% | +0.05pp |
| Approved by Fraud Service | 13,187 | 13,132 | -55 | -0.4% | 92.24% | 93.01% | +0.77pp |
| PVS Attempt | 10,957 | 10,753 | -204 | -1.9% | 83.09% | 81.88% | -1.21pp |
| PVS Success | 10,631 | 10,325 | -306 | -2.9% | 97.02% | 96.02% | -1.01pp |
| **Successful Checkout** | 12,736 | 12,656 | -80 | -0.6% | 119.80% | 122.58% | +2.78pp |
| **PCR Rate** | | | | | 29.46% | 28.51% | **-0.95pp** |

### Payment Method Breakdown

| Payment Method | 2026-W17 Attempt | 2026-W17 Success | 2026-W17 Rate | 2026-W18 Attempt | 2026-W18 Success | 2026-W18 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| Braintree_ApplePay | 4,095 | 3,684 | 89.96% | 4,128 | 3,756 | 90.99% | +1.03pp |
| ProcessOut_CreditCard | 3,893 | 3,417 | 87.77% | 3,942 | 3,463 | 87.85% | +0.08pp |
| Adyen_CreditCard | 2,743 | 2,384 | 86.91% | 2,644 | 2,323 | 87.86% | +0.95pp |
| Braintree_Paypal | 1,742 | 1,575 | 90.41% | 1,677 | 1,517 | 90.46% | +0.05pp |
| Braintree_CreditCard | 1,518 | 1,326 | 87.35% | 1,522 | 1,333 | 87.58% | +0.23pp |
| ProcessOut_ApplePay | 390 | 347 | 88.97% | 287 | 264 | 91.99% | +3.01pp |
| NoPayment | 4 | 0 | 0.00% | 3 | 0 | 0.00% | +0.00pp |
|  | 2 | 2 | 100.00% | 0 | 0 | 0.00% | -100.00pp |
| Braintree_Venmo | 1 | 1 | 100.00% | 0 | 0 | 0.00% | -100.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (3 countries in WL)

| Country | Volume | PCR 2026-W17 | PCR 2026-W18 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| ER | 6,103 | 31.65% | 28.49% | -3.16pp | 1 | 3 |
| CK | 4,562 | 44.65% | 41.01% | -3.64pp | 2 | 2 |
| AO | 1,501 | 52.10% | 42.04% | -10.06pp | 3 | 1 |

---

### ER

#### Waterfall GA

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 5,611 | 6,103 | +492 | +8.77pp | - | - | - |
| Select Payment Method | 2,558 | 2,562 | +4 | +0.16pp | 45.59% | 41.98% | -3.61pp |
| Click Submit Form | 2,262 | 2,245 | -17 | -0.75pp | 88.43% | 87.63% | -0.80pp |
| FE Validation Passed | 2,080 | 2,052 | -28 | -1.35pp | 91.95% | 91.40% | -0.55pp |
| Enter Fraud Service | 2,033 | 1,998 | -35 | -1.72pp | 97.74% | 97.37% | -0.37pp |
| Approved by Fraud Service | 1,893 | 1,881 | -12 | -0.63pp | 93.11% | 94.14% | +1.03pp |
| Call to PVS | 1,889 | 1,878 | -11 | -0.58pp | 99.79% | 99.84% | +0.05pp |
| **Successful Checkout** | 1,776 | 1,739 | -37 | -2.08pp | 94.02% | 92.60% | -1.42pp |
| **PCR Rate** | | | | | 31.65% | 28.49% | **-3.16pp** |

**Key Driver:** Select Payment Method (-3.61pp)

#### Waterfall Backend

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 7,418 | 7,247 | -171 | -2.31pp | - | - | - |
| Checkout Attempt | 2,424 | 2,310 | -114 | -4.70pp | 32.68% | 31.88% | -0.80pp |
| Enter Fraud Service | 2,424 | 2,306 | -118 | -4.87pp | 100.00% | 99.83% | -0.17pp |
| Approved by Fraud Service | 2,235 | 2,141 | -94 | -4.21pp | 92.20% | 92.84% | +0.64pp |
| PVS Attempt | 2,232 | 2,137 | -95 | -4.26pp | 99.87% | 99.81% | -0.05pp |
| PVS Success | 2,112 | 1,991 | -121 | -5.73pp | 94.62% | 93.17% | -1.46pp |
| **Successful Checkout** | 2,115 | 1,997 | -118 | -5.58pp | 100.14% | 100.30% | +0.16pp |

**Key Driver:** PVS Success (-1.46pp)

---

### AO

#### Waterfall GA

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 1,503 | 1,501 | -2 | -0.13pp | - | - | - |
| Select Payment Method | 996 | 845 | -151 | -15.16pp | 66.27% | 56.30% | -9.97pp |
| Click Submit Form | 940 | 769 | -171 | -18.19pp | 94.38% | 91.01% | -3.37pp |
| FE Validation Passed | 912 | 754 | -158 | -17.32pp | 97.02% | 98.05% | +1.03pp |
| Enter Fraud Service | 903 | 728 | -175 | -19.38pp | 99.01% | 96.55% | -2.46pp |
| Approved by Fraud Service | 816 | 671 | -145 | -17.77pp | 90.37% | 92.17% | +1.80pp |
| Call to PVS | 810 | 671 | -139 | -17.16pp | 99.26% | 100.00% | +0.74pp |
| **Successful Checkout** | 783 | 631 | -152 | -19.41pp | 96.67% | 94.04% | -2.63pp |
| **PCR Rate** | | | | | 52.10% | 42.04% | **-10.06pp** |

**Key Driver:** Select Payment Method (-9.97pp)

#### Waterfall Backend

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 2,066 | 1,899 | -167 | -8.08pp | - | - | - |
| Checkout Attempt | 1,068 | 862 | -206 | -19.29pp | 51.69% | 45.39% | -6.30pp |
| Enter Fraud Service | 1,067 | 862 | -205 | -19.21pp | 99.91% | 100.00% | +0.09pp |
| Approved by Fraud Service | 935 | 772 | -163 | -17.43pp | 87.63% | 89.56% | +1.93pp |
| PVS Attempt | 932 | 770 | -162 | -17.38pp | 99.68% | 99.74% | +0.06pp |
| PVS Success | 908 | 734 | -174 | -19.16pp | 97.42% | 95.32% | -2.10pp |
| **Successful Checkout** | 912 | 743 | -169 | -18.53pp | 100.44% | 101.23% | +0.79pp |

**Key Driver:** Checkout Attempt (-6.30pp)

---

### CK

#### Waterfall GA

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 3,922 | 4,562 | +640 | +16.32pp | - | - | - |
| Select Payment Method | 2,265 | 2,416 | +151 | +6.67pp | 57.75% | 52.96% | -4.79pp |
| Click Submit Form | 2,078 | 2,221 | +143 | +6.88pp | 91.74% | 91.93% | +0.18pp |
| FE Validation Passed | 2,047 | 2,150 | +103 | +5.03pp | 98.51% | 96.80% | -1.70pp |
| Enter Fraud Service | 1,998 | 2,094 | +96 | +4.80pp | 97.61% | 97.40% | -0.21pp |
| Approved by Fraud Service | 1,852 | 1,985 | +133 | +7.18pp | 92.69% | 94.79% | +2.10pp |
| Call to PVS | 1,848 | 1,979 | +131 | +7.09pp | 99.78% | 99.70% | -0.09pp |
| **Successful Checkout** | 1,751 | 1,871 | +120 | +6.85pp | 94.75% | 94.54% | -0.21pp |
| **PCR Rate** | | | | | 44.65% | 41.01% | **-3.63pp** |

**Key Driver:** Select Payment Method (-4.79pp)

#### Waterfall Backend

| Funnel Step | 2026-W17 | 2026-W18 | Δ Count | Δ % | 2026-W17 Conv | 2026-W18 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 4,763 | 5,086 | +323 | +6.78pp | - | - | - |
| Checkout Attempt | 2,242 | 2,313 | +71 | +3.17pp | 47.07% | 45.48% | -1.59pp |
| Enter Fraud Service | 2,239 | 2,307 | +68 | +3.04pp | 99.87% | 99.74% | -0.13pp |
| Approved by Fraud Service | 2,038 | 2,131 | +93 | +4.56pp | 91.02% | 92.37% | +1.35pp |
| PVS Attempt | 2,033 | 2,127 | +94 | +4.62pp | 99.75% | 99.81% | +0.06pp |
| PVS Success | 1,954 | 2,028 | +74 | +3.79pp | 96.11% | 95.35% | -0.77pp |
| **Successful Checkout** | 1,966 | 2,061 | +95 | +4.83pp | 100.61% | 101.63% | +1.01pp |

**Key Driver:** Checkout Attempt (-1.59pp)

---



## Fraud Analysis

**Include reason:** Approved Δ (+1.28pp) meets threshold (+1.06pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W17 | 2026-W17 % | 2026-W18 | 2026-W18 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 14,388 | - | 14,203 | - | -185 | -1.3% |
| Enter Fraud Service | 14,296 | - | 14,119 | - | -177 | -1.2% |
| **Gap (Skipped)** | **92** | **0.64%** | **84** | **0.59%** | **-8** | **-0.05pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W17 Gap | 2026-W17 % | 2026-W18 Gap | 2026-W18 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Braintree_CreditCard | 33 | 37.5% | 26 | 32.1% | -7 | -5.40pp |
| Braintree_ApplePay | 36 | 40.9% | 24 | 29.6% | -12 | -11.28pp |
| Braintree_Paypal | 10 | 11.4% | 20 | 24.7% | +10 | +13.33pp |
| Adyen_CreditCard | 0 | 0.0% | 7 | 8.6% | +7 | +8.64pp |
| ProcessOut_CreditCard | 5 | 5.7% | 4 | 4.9% | -1 | -0.74pp |
| NoPayment | 4 | 4.5% | 0 | 0.0% | -4 | -4.55pp |
| **Total** | **88** | **100%** | **81** | **100%** | **-7** | - |

*% of Gap = Payment Method Gap / Total Gap*

---


---

*Report: 2026-05-05*
