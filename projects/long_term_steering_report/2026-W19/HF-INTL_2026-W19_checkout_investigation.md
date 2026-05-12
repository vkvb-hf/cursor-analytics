# PCR Investigation: HF-INTL 2026-W19

**Metric:** Payment Conversion Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 36.49% → 36.32% (-0.16pp)  
**Volume:** 69,609 payment visits  
**Threshold:** +0.08pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate for HF-INTL declined slightly from 36.49% to 36.32% (-0.16pp) in 2026-W19, with 69,609 payment visits processed.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | \|Δ\| ≥ 0.08pp? | -0.06pp | ✅ |
| Click Submit Form | \|Δ\| ≥ 0.08pp? | -0.25pp | ⚠️ |
| FE Validation Passed | \|Δ\| ≥ 0.08pp? | +0.03pp | ✅ |
| Enter Fraud Service | \|Δ\| ≥ 0.08pp? | +0.33pp | ⚠️ |
| Approved by Fraud Service | \|Δ\| ≥ 0.08pp? | +0.20pp | ⚠️ |
| Call to PVS | \|Δ\| ≥ 0.08pp? | +0.30pp | ⚠️ |
| Successful Checkout | \|Δ\| ≥ 0.08pp? | -0.88pp | ⚠️ |

**Key Findings:**
- **Successful Checkout conversion dropped significantly (-0.88pp)**, representing the largest negative impact in the GA funnel, with PVS Success in the backend showing a corresponding -1.23pp decline
- **DE is the primary driver of decline** with PCR dropping -2.46pp (37.14% → 34.68%), driven by a severe -4.34pp drop in Successful Checkout conversion from the GA waterfall
- **PVS failures increased by 437 cases (+30%)**, with "Cancelled: Cancelled" errors rising sharply (+188 cases, +6.83pp share) and "RedirectShopper" errors increasing (+174 cases, +3.74pp share)
- **FR showed positive performance (+1.38pp PCR)**, offsetting some of the overall decline with improved Select Payment Method conversion (+1.55pp)
- **Fraud Service gap improved** with fewer checkout attempts skipping fraud checks (-231 cases), primarily from Adyen_Sepa reduction (-190 cases)

**Action:** Investigate — Focus on PVS failure root causes in DE, specifically the increase in "Cancelled: Cancelled" and "RedirectShopper" errors impacting Successful Checkout conversion.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 70,968 | 69,609 | -1,359 | -1.9% | - | - | - |
| Select Payment Method | 39,230 | 38,439 | -791 | -2.0% | 55.28% | 55.22% | -0.06pp |
| Click Submit Form | 32,290 | 31,541 | -749 | -2.3% | 82.31% | 82.05% | -0.25pp |
| FE Validation Passed | 30,372 | 29,676 | -696 | -2.3% | 94.06% | 94.09% | +0.03pp |
| Enter Fraud Service | 28,995 | 28,429 | -566 | -2.0% | 95.47% | 95.80% | +0.33pp |
| Approved by Fraud Service | 27,516 | 27,037 | -479 | -1.7% | 94.90% | 95.10% | +0.20pp |
| Call to PVS | 27,328 | 26,934 | -394 | -1.4% | 99.32% | 99.62% | +0.30pp |
| **Successful Checkout** | 25,894 | 25,285 | -609 | -2.4% | 94.75% | 93.88% | -0.88pp |
| **PCR Rate** | | | | | 36.49% | 36.32% | **-0.16pp** |

### Waterfall Backend

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 88,569 | 86,756 | -1,813 | -2.0% | - | - | - |
| Checkout Attempt | 42,247 | 40,870 | -1,377 | -3.3% | 47.70% | 47.11% | -0.59pp |
| Enter Fraud Service | 40,880 | 39,734 | -1,146 | -2.8% | 96.76% | 97.22% | +0.46pp |
| Approved by Fraud Service | 37,737 | 36,775 | -962 | -2.5% | 92.31% | 92.55% | +0.24pp |
| PVS Attempt | 34,181 | 33,686 | -495 | -1.4% | 90.58% | 91.60% | +1.02pp |
| PVS Success | 32,190 | 31,310 | -880 | -2.7% | 94.18% | 92.95% | -1.23pp |
| **Successful Checkout** | 36,169 | 35,454 | -715 | -2.0% | 112.36% | 113.24% | +0.87pp |
| **PCR Rate** | | | | | 40.84% | 40.87% | **+0.03pp** |

### Payment Method Breakdown

| Payment Method | 2026-W18 Attempt | 2026-W18 Success | 2026-W18 Rate | 2026-W19 Attempt | 2026-W19 Success | 2026-W19 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 13,625 | 11,801 | 86.61% | 13,184 | 11,590 | 87.91% | +1.30pp |
| Braintree_ApplePay | 12,090 | 10,209 | 84.44% | 11,993 | 10,216 | 85.18% | +0.74pp |
| Braintree_Paypal | 8,048 | 7,349 | 91.31% | 7,478 | 6,872 | 91.90% | +0.58pp |
| Adyen_Klarna | 1,773 | 1,659 | 93.57% | 1,768 | 1,645 | 93.04% | -0.53pp |
| Adyen_CreditCard | 1,524 | 1,485 | 97.44% | 1,481 | 1,450 | 97.91% | +0.47pp |
| Adyen_IDeal | 1,390 | 1,268 | 91.22% | 1,386 | 1,256 | 90.62% | -0.60pp |
| ProcessOut_ApplePay | 1,540 | 1,363 | 88.51% | 1,384 | 1,249 | 90.25% | +1.74pp |
| Adyen_Sepa | 1,118 | 2 | 0.18% | 929 | 3 | 0.32% | +0.14pp |
| Adyen_BcmcMobile | 698 | 666 | 95.42% | 770 | 732 | 95.06% | -0.35pp |
| ProcessOut_Mobilepay | 240 | 231 | 96.25% | 285 | 273 | 95.79% | -0.46pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (4 countries in HF-INTL)

| Country | Volume | PCR 2026-W18 | PCR 2026-W19 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| DE | 12,606 | 37.14% | 34.68% | -2.46pp | 1 | 3 |
| FR | 15,961 | 29.34% | 30.72% | +1.38pp | 2 | 6 |
| AT | 1,015 | 30.19% | 33.50% | +3.31pp | 5 | 1 |
| LU | 93 | 50.55% | 47.31% | -3.24pp | 14 | 2 |

---

### FR

#### Waterfall GA

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 15,425 | 15,961 | +536 | +3.47pp | - | - | - |
| Select Payment Method | 7,219 | 7,717 | +498 | +6.90pp | 46.80% | 48.35% | +1.55pp |
| Click Submit Form | 5,803 | 6,143 | +340 | +5.86pp | 80.39% | 79.60% | -0.78pp |
| FE Validation Passed | 5,384 | 5,763 | +379 | +7.04pp | 92.78% | 93.81% | +1.03pp |
| Enter Fraud Service | 5,099 | 5,439 | +340 | +6.67pp | 94.71% | 94.38% | -0.33pp |
| Approved by Fraud Service | 4,680 | 5,012 | +332 | +7.09pp | 91.78% | 92.15% | +0.37pp |
| Call to PVS | 4,662 | 5,034 | +372 | +7.98pp | 99.62% | 100.44% | +0.82pp |
| **Successful Checkout** | 4,525 | 4,903 | +378 | +8.35pp | 97.06% | 97.40% | +0.34pp |
| **PCR Rate** | | | | | 29.34% | 30.72% | **+1.38pp** |

**Key Driver:** Select Payment Method (+1.55pp)

#### Waterfall Backend

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 19,464 | 20,010 | +546 | +2.81pp | - | - | - |
| Checkout Attempt | 7,660 | 8,020 | +360 | +4.70pp | 39.35% | 40.08% | +0.73pp |
| Enter Fraud Service | 7,637 | 7,996 | +359 | +4.70pp | 99.70% | 99.70% | +0.00pp |
| Approved by Fraud Service | 6,662 | 7,048 | +386 | +5.79pp | 87.23% | 88.14% | +0.91pp |
| PVS Attempt | 6,626 | 7,051 | +425 | +6.41pp | 99.46% | 100.04% | +0.58pp |
| PVS Success | 6,176 | 6,566 | +390 | +6.31pp | 93.21% | 93.12% | -0.09pp |
| **Successful Checkout** | 6,502 | 6,959 | +457 | +7.03pp | 105.28% | 105.99% | +0.71pp |

**Key Driver:** Approved by Fraud Service (+0.91pp)

---

### DE

#### Waterfall GA

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 13,596 | 12,606 | -990 | -7.28pp | - | - | - |
| Select Payment Method | 8,151 | 7,437 | -714 | -8.76pp | 59.95% | 59.00% | -0.96pp |
| Click Submit Form | 6,440 | 5,863 | -577 | -8.96pp | 79.01% | 78.84% | -0.17pp |
| FE Validation Passed | 6,186 | 5,594 | -592 | -9.57pp | 96.06% | 95.41% | -0.64pp |
| Enter Fraud Service | 5,742 | 5,252 | -490 | -8.53pp | 92.82% | 93.89% | +1.06pp |
| Approved by Fraud Service | 5,576 | 5,059 | -517 | -9.27pp | 97.11% | 96.33% | -0.78pp |
| Call to PVS | 5,540 | 5,036 | -504 | -9.10pp | 99.35% | 99.55% | +0.19pp |
| **Successful Checkout** | 5,050 | 4,372 | -678 | -13.43pp | 91.16% | 86.81% | -4.34pp |
| **PCR Rate** | | | | | 37.14% | 34.68% | **-2.46pp** |

**Key Driver:** Successful Checkout (-4.34pp)

#### Waterfall Backend

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 17,544 | 16,484 | -1,060 | -6.04pp | - | - | - |
| Checkout Attempt | 8,562 | 7,930 | -632 | -7.38pp | 48.80% | 48.11% | -0.70pp |
| Enter Fraud Service | 8,509 | 7,871 | -638 | -7.50pp | 99.38% | 99.26% | -0.12pp |
| Approved by Fraud Service | 8,104 | 7,431 | -673 | -8.30pp | 95.24% | 94.41% | -0.83pp |
| PVS Attempt | 7,628 | 7,281 | -347 | -4.55pp | 94.13% | 97.98% | +3.86pp |
| PVS Success | 7,072 | 6,472 | -600 | -8.48pp | 92.71% | 88.89% | -3.82pp |
| **Successful Checkout** | 7,904 | 7,329 | -575 | -7.27pp | 111.76% | 113.24% | +1.48pp |

**Key Driver:** PVS Attempt (+3.86pp)

---

### AT

#### Waterfall GA

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 1,156 | 1,015 | -141 | -12.20pp | - | - | - |
| Select Payment Method | 586 | 548 | -38 | -6.48pp | 50.69% | 53.99% | +3.30pp |
| Click Submit Form | 429 | 420 | -9 | -2.10pp | 73.21% | 76.64% | +3.43pp |
| FE Validation Passed | 387 | 397 | +10 | +2.58pp | 90.21% | 94.52% | +4.31pp |
| Enter Fraud Service | 374 | 367 | -7 | -1.87pp | 96.64% | 92.44% | -4.20pp |
| Approved by Fraud Service | 364 | 352 | -12 | -3.30pp | 97.33% | 95.91% | -1.41pp |
| Call to PVS | 364 | 352 | -12 | -3.30pp | 100.00% | 100.00% | +0.00pp |
| **Successful Checkout** | 349 | 340 | -9 | -2.58pp | 95.88% | 96.59% | +0.71pp |
| **PCR Rate** | | | | | 30.19% | 33.50% | **+3.31pp** |

**Key Driver:** FE Validation Passed (+4.31pp)

#### Waterfall Backend

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 1,552 | 1,365 | -187 | -12.05pp | - | - | - |
| Checkout Attempt | 551 | 528 | -23 | -4.17pp | 35.50% | 38.68% | +3.18pp |
| Enter Fraud Service | 539 | 520 | -19 | -3.53pp | 97.82% | 98.48% | +0.66pp |
| Approved by Fraud Service | 515 | 492 | -23 | -4.47pp | 95.55% | 94.62% | -0.93pp |
| PVS Attempt | 510 | 488 | -22 | -4.31pp | 99.03% | 99.19% | +0.16pp |
| PVS Success | 492 | 472 | -20 | -4.07pp | 96.47% | 96.72% | +0.25pp |
| **Successful Checkout** | 498 | 483 | -15 | -3.01pp | 101.22% | 102.33% | +1.11pp |

**Key Driver:** Checkout Attempt (+3.18pp)

---

### LU

#### Waterfall GA

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 91 | 93 | +2 | +2.20pp | - | - | - |
| Select Payment Method | 64 | 60 | -4 | -6.25pp | 70.33% | 64.52% | -5.81pp |
| Click Submit Form | 58 | 52 | -6 | -10.34pp | 90.62% | 86.67% | -3.96pp |
| FE Validation Passed | 54 | 50 | -4 | -7.41pp | 93.10% | 96.15% | +3.05pp |
| Enter Fraud Service | 53 | 49 | -4 | -7.55pp | 98.15% | 98.00% | -0.15pp |
| Approved by Fraud Service | 53 | 47 | -6 | -11.32pp | 100.00% | 95.92% | -4.08pp |
| Call to PVS | 52 | 45 | -7 | -13.46pp | 98.11% | 95.74% | -2.37pp |
| **Successful Checkout** | 46 | 44 | -2 | -4.35pp | 88.46% | 97.78% | +9.32pp |
| **PCR Rate** | | | | | 50.55% | 47.31% | **-3.24pp** |

**Key Driver:** Successful Checkout (+9.32pp)

#### Waterfall Backend

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 311 | 288 | -23 | -7.40pp | - | - | - |
| Checkout Attempt | 97 | 69 | -28 | -28.87pp | 31.19% | 23.96% | -7.23pp |
| Enter Fraud Service | 74 | 63 | -11 | -14.86pp | 76.29% | 91.30% | +15.02pp |
| Approved by Fraud Service | 73 | 60 | -13 | -17.81pp | 98.65% | 95.24% | -3.41pp |
| PVS Attempt | 70 | 57 | -13 | -18.57pp | 95.89% | 95.00% | -0.89pp |
| PVS Success | 64 | 55 | -9 | -14.06pp | 91.43% | 96.49% | +5.06pp |
| **Successful Checkout** | 84 | 59 | -25 | -29.76pp | 131.25% | 107.27% | -23.98pp |

**Key Driver:** Successful Checkout (-23.98pp)

---



## Fraud Analysis

**Include reason:** Enter FS Δ (+0.33pp) meets threshold (+0.08pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W18 | 2026-W18 % | 2026-W19 | 2026-W19 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 42,247 | - | 40,870 | - | -1,377 | -3.3% |
| Enter Fraud Service | 40,880 | - | 39,734 | - | -1,146 | -2.8% |
| **Gap (Skipped)** | **1,367** | **3.24%** | **1,136** | **2.78%** | **-231** | **-0.46pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W18 Gap | 2026-W18 % | 2026-W19 Gap | 2026-W19 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Adyen_Sepa | 1,118 | 84.2% | 928 | 83.9% | -190 | -0.28pp |
| Braintree_ApplePay | 56 | 4.2% | 50 | 4.5% | -6 | +0.30pp |
| ProcessOut_CreditCard | 48 | 3.6% | 49 | 4.4% | +1 | +0.82pp |
| NoPayment | 58 | 4.4% | 40 | 3.6% | -18 | -0.75pp |
| Braintree_Paypal | 48 | 3.6% | 39 | 3.5% | -9 | -0.09pp |
| **Total** | **1,328** | **100%** | **1,106** | **100%** | **-222** | - |

*% of Gap = Payment Method Gap / Total Gap*

---

## Payment Verification Errors

**Include reason:** PVS Success Δ Conv (-0.88pp) meets threshold (+0.08pp)

| Decline Reason | 2026-W18 | 2026-W18 % | 2026-W19 | 2026-W19 % | Δ Count | Δ % |
| -------------- | ----------- | ------------- | --------------- | ----------------- | ------- | ----- |
| RedirectShopper | 343 | 23.7% | 517 | 27.4% | +174 | +3.74pp |
| Cancelled: Cancelled | 196 | 13.5% | 384 | 20.4% | +188 | +6.83pp |
| CHARGE_STATE_FAILURE: No action was initiated on the transaction yet. | 226 | 15.6% | 250 | 13.3% | +24 | -2.34pp |
| Pending | 156 | 10.8% | 174 | 9.2% | +18 | -1.54pp |
| Failed Verification: Insufficient Funds | 182 | 12.6% | 153 | 8.1% | -29 | -4.45pp |
| CHARGE_STATE_FAILURE: The 3DS check has expired | 69 | 4.8% | 97 | 5.1% | +28 | +0.38pp |
| Verified | 77 | 5.3% | 86 | 4.6% | +9 | -0.75pp |
| CHARGE_STATE_FAILURE: Customer abandoned payment after 60 minutes | 62 | 4.3% | 84 | 4.5% | +22 | +0.18pp |
| Failed Verification: Funding Instrument In The PayPal Account Was Declined By The Processor Or Bank, Or It Can't Be Used For This Payment | 69 | 4.8% | 79 | 4.2% | +10 | -0.57pp |
| Failed Verification: Declined | 69 | 4.8% | 62 | 3.3% | -7 | -1.47pp |
| **Total PVS Failures** | **1,449** | **100%** | **1,886** | **100%** | **+437** | - |

---


---

*Report: 2026-05-12*
