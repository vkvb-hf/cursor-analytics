# PCR Investigation: RTE 2026-W14

**Metric:** Payment Conversion Rate  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 37.81% → 39.36% (+1.55pp)  
**Volume:** 63,361 payment visits  
**Threshold:** +0.78pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate improved from 37.81% to 39.36% (+1.55pp) in 2026-W14, exceeding the threshold of +0.78pp, while payment visit volume decreased by 10.4% (from 70,721 to 63,361 visits).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ≥ threshold? | +1.75pp | ✅ |
| Click Submit Form | ≥ threshold? | +0.90pp | ✅ |
| FE Validation Passed | ≥ threshold? | -0.46pp | ⚠️ |
| Enter Fraud Service | ≥ threshold? | -0.21pp | ⚠️ |
| Approved by Fraud Service | ≥ threshold? | -0.09pp | ⚠️ |
| Call to PVS | ≥ threshold? | -0.11pp | ⚠️ |
| Successful Checkout | ≥ threshold? | +0.33pp | ⚠️ |

**Key Findings:**
- **Top-of-funnel improvement drove PCR gains:** Select Payment Method conversion increased +1.75pp (48.18% → 49.93%), representing the largest positive contributor to overall improvement
- **Country-level divergence in Fraud Service performance:** TK saw Fraud Service approval improve +5.88pp while TO experienced a decline of -4.88pp at the same step
- **Backend PVS Attempt shows concerning drop:** Backend waterfall reveals PVS Attempt conversion declined -1.25pp (99.46% → 98.21%), partially offsetting gains
- **FJ dominates volume and contribution:** FJ accounts for 64% of payment visits and showed +2.51pp PCR improvement, primarily driven by Select Payment Method (+2.32pp)
- **Braintree_ApplePay declined:** Payment method success rate dropped -1.71pp (87.23% → 85.51%) despite being the second-highest volume method

**Action:** Monitor — The overall PCR improvement is positive and driven by healthy top-of-funnel gains. However, investigate the divergent Fraud Service performance between TK (+5.88pp) and TO (-4.88pp) to understand if policy changes or regional factors are causing inconsistent outcomes.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 70,721 | 63,361 | -7,360 | -10.4% | - | - | - |
| Select Payment Method | 34,071 | 31,636 | -2,435 | -7.1% | 48.18% | 49.93% | +1.75pp |
| Click Submit Form | 30,388 | 28,501 | -1,887 | -6.2% | 89.19% | 90.09% | +0.90pp |
| FE Validation Passed | 29,663 | 27,689 | -1,974 | -6.7% | 97.61% | 97.15% | -0.46pp |
| Enter Fraud Service | 29,067 | 27,074 | -1,993 | -6.9% | 97.99% | 97.78% | -0.21pp |
| Approved by Fraud Service | 27,935 | 25,995 | -1,940 | -6.9% | 96.11% | 96.01% | -0.09pp |
| Call to PVS | 27,903 | 25,936 | -1,967 | -7.0% | 99.89% | 99.77% | -0.11pp |
| **Successful Checkout** | 26,739 | 24,939 | -1,800 | -6.7% | 95.83% | 96.16% | +0.33pp |
| **PCR Rate** | | | | | 37.81% | 39.36% | **+1.55pp** |

### Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 123,045 | 110,209 | -12,836 | -10.4% | - | - | - |
| Checkout Attempt | 45,411 | 42,850 | -2,561 | -5.6% | 36.91% | 38.88% | +1.97pp |
| Enter Fraud Service | 45,337 | 42,766 | -2,571 | -5.7% | 99.84% | 99.80% | -0.03pp |
| Approved by Fraud Service | 43,132 | 40,642 | -2,490 | -5.8% | 95.14% | 95.03% | -0.10pp |
| PVS Attempt | 42,897 | 39,914 | -2,983 | -7.0% | 99.46% | 98.21% | -1.25pp |
| PVS Success | 41,563 | 38,675 | -2,888 | -6.9% | 96.89% | 96.90% | +0.01pp |
| **Successful Checkout** | 41,426 | 38,814 | -2,612 | -6.3% | 99.67% | 100.36% | +0.69pp |
| **PCR Rate** | | | | | 33.67% | 35.22% | **+1.55pp** |

### Payment Method Breakdown

| Payment Method | 2026-W13 Attempt | 2026-W13 Success | 2026-W13 Rate | 2026-W14 Attempt | 2026-W14 Success | 2026-W14 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 17,491 | 16,234 | 92.81% | 17,123 | 15,943 | 93.11% | +0.30pp |
| Braintree_ApplePay | 11,367 | 9,915 | 87.23% | 10,528 | 9,003 | 85.51% | -1.71pp |
| Adyen_CreditCard | 9,936 | 9,111 | 91.70% | 9,248 | 8,384 | 90.66% | -1.04pp |
| Braintree_Paypal | 5,297 | 4,954 | 93.52% | 4,880 | 4,520 | 92.62% | -0.90pp |
| Adyen_IDeal | 809 | 756 | 93.45% | 676 | 610 | 90.24% | -3.21pp |
| Adyen_Klarna | 378 | 347 | 91.80% | 297 | 273 | 91.92% | +0.12pp |
| Braintree_CreditCard | 125 | 105 | 84.00% | 91 | 75 | 82.42% | -1.58pp |
| Braintree_Venmo | 4 | 4 | 100.00% | 6 | 6 | 100.00% | +0.00pp |
|  | 4 | 0 | 0.00% | 1 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (3 countries in RTE)

| Country | Volume | PCR 2026-W13 | PCR 2026-W14 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| FJ | 40,637 | 37.43% | 39.94% | +2.51pp | 1 | 3 |
| TO | 888 | 44.86% | 39.08% | -5.78pp | 2 | 2 |
| TK | 473 | 40.84% | 46.93% | +6.09pp | 3 | 1 |

---

### TK

#### Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 475 | 473 | -2 | -0.42pp | - | - | - |
| Select Payment Method | 262 | 287 | +25 | +9.54pp | 55.16% | 60.68% | +5.52pp |
| Click Submit Form | 238 | 259 | +21 | +8.82pp | 90.84% | 90.24% | -0.60pp |
| FE Validation Passed | 224 | 246 | +22 | +9.82pp | 94.12% | 94.98% | +0.86pp |
| Enter Fraud Service | 219 | 240 | +21 | +9.59pp | 97.77% | 97.56% | -0.21pp |
| Approved by Fraud Service | 197 | 230 | +33 | +16.75pp | 89.95% | 95.83% | +5.88pp |
| Call to PVS | 198 | 230 | +32 | +16.16pp | 100.51% | 100.00% | -0.51pp |
| **Successful Checkout** | 194 | 222 | +28 | +14.43pp | 97.98% | 96.52% | -1.46pp |
| **PCR Rate** | | | | | 40.84% | 46.93% | **+6.09pp** |

**Key Driver:** Approved by Fraud Service (+5.88pp)

#### Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 679 | 670 | -9 | -1.33pp | - | - | - |
| Checkout Attempt | 311 | 339 | +28 | +9.00pp | 45.80% | 50.60% | +4.79pp |
| Enter Fraud Service | 311 | 339 | +28 | +9.00pp | 100.00% | 100.00% | +0.00pp |
| Approved by Fraud Service | 277 | 315 | +38 | +13.72pp | 89.07% | 92.92% | +3.85pp |
| PVS Attempt | 277 | 315 | +38 | +13.72pp | 100.00% | 100.00% | +0.00pp |
| PVS Success | 277 | 308 | +31 | +11.19pp | 100.00% | 97.78% | -2.22pp |
| **Successful Checkout** | 277 | 309 | +32 | +11.55pp | 100.00% | 100.32% | +0.32pp |

**Key Driver:** Checkout Attempt (+4.79pp)

---

### TO

#### Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 1,246 | 888 | -358 | -28.73pp | - | - | - |
| Select Payment Method | 747 | 509 | -238 | -31.86pp | 59.95% | 57.32% | -2.63pp |
| Click Submit Form | 658 | 445 | -213 | -32.37pp | 88.09% | 87.43% | -0.66pp |
| FE Validation Passed | 626 | 422 | -204 | -32.59pp | 95.14% | 94.83% | -0.31pp |
| Enter Fraud Service | 614 | 403 | -211 | -34.36pp | 98.08% | 95.50% | -2.59pp |
| Approved by Fraud Service | 580 | 361 | -219 | -37.76pp | 94.46% | 89.58% | -4.88pp |
| Call to PVS | 580 | 362 | -218 | -37.59pp | 100.00% | 100.28% | +0.28pp |
| **Successful Checkout** | 559 | 347 | -212 | -37.92pp | 96.38% | 95.86% | -0.52pp |
| **PCR Rate** | | | | | 44.86% | 39.08% | **-5.79pp** |

**Key Driver:** Approved by Fraud Service (-4.88pp)

#### Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 1,617 | 1,267 | -350 | -21.65pp | - | - | - |
| Checkout Attempt | 787 | 581 | -206 | -26.18pp | 48.67% | 45.86% | -2.81pp |
| Enter Fraud Service | 787 | 581 | -206 | -26.18pp | 100.00% | 100.00% | +0.00pp |
| Approved by Fraud Service | 731 | 515 | -216 | -29.55pp | 92.88% | 88.64% | -4.24pp |
| PVS Attempt | 731 | 514 | -217 | -29.69pp | 100.00% | 99.81% | -0.19pp |
| PVS Success | 710 | 499 | -211 | -29.72pp | 97.13% | 97.08% | -0.05pp |
| **Successful Checkout** | 716 | 508 | -208 | -29.05pp | 100.85% | 101.80% | +0.96pp |

**Key Driver:** Approved by Fraud Service (-4.24pp)

---

### FJ

#### Waterfall GA

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 45,842 | 40,637 | -5,205 | -11.35pp | - | - | - |
| Select Payment Method | 21,465 | 19,972 | -1,493 | -6.96pp | 46.82% | 49.15% | +2.32pp |
| Click Submit Form | 19,217 | 18,161 | -1,056 | -5.50pp | 89.53% | 90.93% | +1.41pp |
| FE Validation Passed | 18,659 | 17,530 | -1,129 | -6.05pp | 97.10% | 96.53% | -0.57pp |
| Enter Fraud Service | 18,366 | 17,246 | -1,120 | -6.10pp | 98.43% | 98.38% | -0.05pp |
| Approved by Fraud Service | 17,731 | 16,695 | -1,036 | -5.84pp | 96.54% | 96.81% | +0.26pp |
| Call to PVS | 17,701 | 16,683 | -1,018 | -5.75pp | 99.83% | 99.93% | +0.10pp |
| **Successful Checkout** | 17,158 | 16,232 | -926 | -5.40pp | 96.93% | 97.30% | +0.36pp |
| **PCR Rate** | | | | | 37.43% | 39.94% | **+2.52pp** |

**Key Driver:** Select Payment Method (+2.32pp)

#### Waterfall Backend

| Funnel Step | 2026-W13 | 2026-W14 | Δ Count | Δ % | 2026-W13 Conv | 2026-W14 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 90,783 | 79,968 | -10,815 | -11.91pp | - | - | - |
| Checkout Attempt | 31,262 | 29,929 | -1,333 | -4.26pp | 34.44% | 37.43% | +2.99pp |
| Enter Fraud Service | 31,237 | 29,910 | -1,327 | -4.25pp | 99.92% | 99.94% | +0.02pp |
| Approved by Fraud Service | 29,838 | 28,651 | -1,187 | -3.98pp | 95.52% | 95.79% | +0.27pp |
| PVS Attempt | 29,723 | 28,555 | -1,168 | -3.93pp | 99.61% | 99.66% | +0.05pp |
| PVS Success | 28,937 | 27,820 | -1,117 | -3.86pp | 97.36% | 97.43% | +0.07pp |
| **Successful Checkout** | 29,029 | 27,885 | -1,144 | -3.94pp | 100.32% | 100.23% | -0.08pp |

**Key Driver:** Checkout Attempt (+2.99pp)

---





---

*Report: 2026-04-09*
