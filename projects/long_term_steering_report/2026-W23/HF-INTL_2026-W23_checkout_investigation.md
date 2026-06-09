# PCR Investigation: HF-INTL 2026-W23

**Metric:** Payment Conversion Rate  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 36.88% → 36.96% (+0.07pp)  
**Volume:** 65,071 payment visits  
**Threshold:** +0.04pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate for HF-INTL improved marginally from 36.88% to 36.96% (+0.07pp) in 2026-W23, with payment visits increasing 9.4% to 65,071.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | GA Step Conversion | -1.17pp | ⚠️ |
| Click Submit Form | GA Step Conversion | +0.79pp | ✅ |
| FE Validation Passed | GA Step Conversion | -0.01pp | ✅ |
| Enter Fraud Service | GA Step Conversion | +0.70pp | ✅ |
| Approved by Fraud Service | GA Step Conversion | +0.13pp | ✅ |
| Call to PVS | GA Step Conversion | +0.46pp | ✅ |
| Successful Checkout | GA Step Conversion | +0.01pp | ✅ |

**Key Findings:**
- **Select Payment Method is the primary bottleneck:** GA conversion dropped -1.17pp (56.30% → 55.13%), impacting IE (-4.37pp), AU (-4.17pp), and CH (-4.34pp)
- **Payment method success rates improved significantly:** ProcessOut_CreditCard (+12.19pp), Adyen_Klarna (+13.53pp), and ProcessOut_ApplePay (+17.61pp) all showed strong gains
- **Adyen_Sepa remains non-functional:** 0% success rate with 1,113 attempts, accounting for 87.6% of the Checkout Attempt → Enter Fraud Service gap
- **GB drove positive performance:** PCR increased +1.77pp with volume growth of +2,776 payment visits, offsetting declines in AU (-2.70pp), IE (-5.01pp), and CH (-4.43pp)
- **Backend funnel shows Checkout Attempt decline:** Conversion from Payment Method Listed → Checkout Attempt dropped -6.37pp cluster-wide

**Action:** Investigate — Focus on the Select Payment Method drop-off across AU, IE, and CH, and escalate the persistent Adyen_Sepa failure (0% success rate) to the payments team for resolution.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 59,504 | 65,071 | 5,567 | 9.4% | - | - | - |
| Select Payment Method | 33,500 | 35,874 | 2,374 | 7.1% | 56.30% | 55.13% | -1.17pp |
| Click Submit Form | 27,252 | 29,465 | 2,213 | 8.1% | 81.35% | 82.13% | +0.79pp |
| FE Validation Passed | 25,693 | 27,775 | 2,082 | 8.1% | 94.28% | 94.26% | -0.01pp |
| Enter Fraud Service | 24,804 | 27,007 | 2,203 | 8.9% | 96.54% | 97.23% | +0.70pp |
| Approved by Fraud Service | 23,578 | 25,706 | 2,128 | 9.0% | 95.06% | 95.18% | +0.13pp |
| Call to PVS | 21,836 | 23,924 | 2,088 | 9.6% | 92.61% | 93.07% | +0.46pp |
| **Successful Checkout** | 21,946 | 24,047 | 2,101 | 9.6% | 100.50% | 100.51% | +0.01pp |
| **PCR Rate** | | | | | 36.88% | 36.96% | **+0.07pp** |

### Waterfall Backend

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 62,663 | 78,316 | 15,653 | 25.0% | - | - | - |
| Checkout Attempt | 34,869 | 38,587 | 3,718 | 10.7% | 55.65% | 49.27% | -6.37pp |
| Enter Fraud Service | 33,863 | 37,295 | 3,432 | 10.1% | 97.11% | 96.65% | -0.46pp |
| Approved by Fraud Service | 31,616 | 34,822 | 3,206 | 10.1% | 93.36% | 93.37% | +0.00pp |
| PVS Attempt | 28,130 | 31,799 | 3,669 | 13.0% | 88.97% | 91.32% | +2.34pp |
| PVS Success | 26,575 | 30,221 | 3,646 | 13.7% | 94.47% | 95.04% | +0.57pp |
| **Successful Checkout** | 25,571 | 32,312 | 6,741 | 26.4% | 96.22% | 106.92% | +10.70pp |
| **PCR Rate** | | | | | 40.81% | 41.26% | **+0.45pp** |

### Payment Method Breakdown

| Payment Method | 2026-W22 Attempt | 2026-W22 Success | 2026-W22 Rate | 2026-W23 Attempt | 2026-W23 Success | 2026-W23 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 11,212 | 8,639 | 77.05% | 12,686 | 11,321 | 89.24% | +12.19pp |
| Braintree_ApplePay | 9,841 | 6,536 | 66.42% | 11,106 | 8,280 | 74.55% | +8.14pp |
| Braintree_Paypal | 5,594 | 4,478 | 80.05% | 6,334 | 5,836 | 92.14% | +12.09pp |
| Adyen_Klarna | 1,933 | 1,562 | 80.81% | 1,960 | 1,849 | 94.34% | +13.53pp |
| Adyen_CreditCard | 1,893 | 1,680 | 88.75% | 1,502 | 1,479 | 98.47% | +9.72pp |
| ProcessOut_ApplePay | 1,440 | 1,057 | 73.40% | 1,391 | 1,266 | 91.01% | +17.61pp |
| Adyen_IDeal | 1,108 | 882 | 79.60% | 1,280 | 1,184 | 92.50% | +12.90pp |
| Adyen_Sepa | 867 | 1 | 0.12% | 1,113 | 0 | 0.00% | -0.12pp |
| Adyen_BcmcMobile | 792 | 667 | 84.22% | 1,090 | 1,049 | 96.24% | +12.02pp |
| NoPayment | 46 | 0 | 0.00% | 76 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (4 countries in HF-INTL)

| Country | Volume | PCR 2026-W22 | PCR 2026-W23 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| GB | 17,574 | 40.27% | 42.04% | +1.77pp | 1 | 8 |
| AU | 7,711 | 35.70% | 33.00% | -2.70pp | 2 | 3 |
| IE | 2,448 | 47.13% | 42.12% | -5.01pp | 4 | 1 |
| CH | 409 | 27.17% | 22.74% | -4.43pp | 9 | 2 |

---

### CH

#### Waterfall GA

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 357 | 409 | +52 | +14.57pp | - | - | - |
| Select Payment Method | 163 | 169 | +6 | +3.68pp | 45.66% | 41.32% | -4.34pp |
| Click Submit Form | 125 | 121 | -4 | -3.20pp | 76.69% | 71.60% | -5.09pp |
| FE Validation Passed | 118 | 115 | -3 | -2.54pp | 94.40% | 95.04% | +0.64pp |
| Enter Fraud Service | 110 | 108 | -2 | -1.82pp | 93.22% | 93.91% | +0.69pp |
| Approved by Fraud Service | 107 | 106 | -1 | -0.93pp | 97.27% | 98.15% | +0.88pp |
| Call to PVS | 96 | 93 | -3 | -3.12pp | 89.72% | 87.74% | -1.98pp |
| **Successful Checkout** | 97 | 93 | -4 | -4.12pp | 101.04% | 100.00% | -1.04pp |
| **PCR Rate** | | | | | 27.17% | 22.74% | **-4.43pp** |

**Key Driver:** Click Submit Form (-5.09pp)

#### Waterfall Backend

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 462 | 547 | +85 | +18.40pp | - | - | - |
| Checkout Attempt | 136 | 135 | -1 | -0.74pp | 29.44% | 24.68% | -4.76pp |
| Enter Fraud Service | 133 | 134 | +1 | +0.75pp | 97.79% | 99.26% | +1.47pp |
| Approved by Fraud Service | 126 | 129 | +3 | +2.38pp | 94.74% | 96.27% | +1.53pp |
| PVS Attempt | 126 | 129 | +3 | +2.38pp | 100.00% | 100.00% | +0.00pp |
| PVS Success | 115 | 117 | +2 | +1.74pp | 91.27% | 90.70% | -0.57pp |
| **Successful Checkout** | 124 | 126 | +2 | +1.61pp | 107.83% | 107.69% | -0.13pp |

**Key Driver:** Checkout Attempt (-4.76pp)

---

### IE

#### Waterfall GA

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 2,983 | 2,448 | -535 | -17.93pp | - | - | - |
| Select Payment Method | 1,829 | 1,394 | -435 | -23.78pp | 61.31% | 56.94% | -4.37pp |
| Click Submit Form | 1,609 | 1,186 | -423 | -26.29pp | 87.97% | 85.08% | -2.89pp |
| FE Validation Passed | 1,542 | 1,132 | -410 | -26.59pp | 95.84% | 95.45% | -0.39pp |
| Enter Fraud Service | 1,494 | 1,107 | -387 | -25.90pp | 96.89% | 97.79% | +0.90pp |
| Approved by Fraud Service | 1,441 | 1,054 | -387 | -26.86pp | 96.45% | 95.21% | -1.24pp |
| Call to PVS | 1,403 | 1,028 | -375 | -26.73pp | 97.36% | 97.53% | +0.17pp |
| **Successful Checkout** | 1,406 | 1,031 | -375 | -26.67pp | 100.21% | 100.29% | +0.08pp |
| **PCR Rate** | | | | | 47.13% | 42.12% | **-5.02pp** |

**Key Driver:** Select Payment Method (-4.37pp)

#### Waterfall Backend

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 3,284 | 2,855 | -429 | -13.06pp | - | - | - |
| Checkout Attempt | 1,987 | 1,494 | -493 | -24.81pp | 60.51% | 52.33% | -8.18pp |
| Enter Fraud Service | 1,980 | 1,491 | -489 | -24.70pp | 99.65% | 99.80% | +0.15pp |
| Approved by Fraud Service | 1,889 | 1,403 | -486 | -25.73pp | 95.40% | 94.10% | -1.31pp |
| PVS Attempt | 1,039 | 1,107 | +68 | +6.54pp | 55.00% | 78.90% | +23.90pp |
| PVS Success | 1,024 | 1,092 | +68 | +6.64pp | 98.56% | 98.64% | +0.09pp |
| **Successful Checkout** | 1,869 | 1,386 | -483 | -25.84pp | 182.52% | 126.92% | -55.60pp |

**Key Driver:** Successful Checkout (-55.60pp)

---

### AU

#### Waterfall GA

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 7,790 | 7,711 | -79 | -1.01pp | - | - | - |
| Select Payment Method | 4,085 | 3,722 | -363 | -8.89pp | 52.44% | 48.27% | -4.17pp |
| Click Submit Form | 3,434 | 3,085 | -349 | -10.16pp | 84.06% | 82.89% | -1.18pp |
| FE Validation Passed | 3,191 | 2,856 | -335 | -10.50pp | 92.92% | 92.58% | -0.35pp |
| Enter Fraud Service | 3,117 | 2,785 | -332 | -10.65pp | 97.68% | 97.51% | -0.17pp |
| Approved by Fraud Service | 2,908 | 2,653 | -255 | -8.77pp | 93.29% | 95.26% | +1.97pp |
| Call to PVS | 2,775 | 2,541 | -234 | -8.43pp | 95.43% | 95.78% | +0.35pp |
| **Successful Checkout** | 2,781 | 2,545 | -236 | -8.49pp | 100.22% | 100.16% | -0.06pp |
| **PCR Rate** | | | | | 35.70% | 33.00% | **-2.69pp** |

**Key Driver:** Select Payment Method (-4.17pp)

#### Waterfall Backend

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 7,079 | 8,345 | +1,266 | +17.88pp | - | - | - |
| Checkout Attempt | 3,568 | 3,217 | -351 | -9.84pp | 50.40% | 38.55% | -11.85pp |
| Enter Fraud Service | 3,547 | 3,203 | -344 | -9.70pp | 99.41% | 99.56% | +0.15pp |
| Approved by Fraud Service | 3,267 | 3,010 | -257 | -7.87pp | 92.11% | 93.97% | +1.87pp |
| PVS Attempt | 2,799 | 2,655 | -144 | -5.14pp | 85.67% | 88.21% | +2.53pp |
| PVS Success | 2,710 | 2,567 | -143 | -5.28pp | 96.82% | 96.69% | -0.13pp |
| **Successful Checkout** | 3,180 | 2,925 | -255 | -8.02pp | 117.34% | 113.95% | -3.40pp |

**Key Driver:** Checkout Attempt (-11.85pp)

---

### GB

#### Waterfall GA

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 14,798 | 17,574 | +2,776 | +18.76pp | - | - | - |
| Select Payment Method | 8,548 | 10,327 | +1,779 | +20.81pp | 57.76% | 58.76% | +1.00pp |
| Click Submit Form | 7,077 | 8,637 | +1,560 | +22.04pp | 82.79% | 83.64% | +0.84pp |
| FE Validation Passed | 6,545 | 8,043 | +1,498 | +22.89pp | 92.48% | 93.12% | +0.64pp |
| Enter Fraud Service | 6,380 | 7,912 | +1,532 | +24.01pp | 97.48% | 98.37% | +0.89pp |
| Approved by Fraud Service | 6,113 | 7,561 | +1,448 | +23.69pp | 95.82% | 95.56% | -0.25pp |
| Call to PVS | 5,918 | 7,339 | +1,421 | +24.01pp | 96.81% | 97.06% | +0.25pp |
| **Successful Checkout** | 5,959 | 7,388 | +1,429 | +23.98pp | 100.69% | 100.67% | -0.03pp |
| **PCR Rate** | | | | | 40.27% | 42.04% | **+1.77pp** |

**Key Driver:** Select Payment Method (+1.00pp)

#### Waterfall Backend

| Funnel Step | 2026-W22 | 2026-W23 | Δ Count | Δ % | 2026-W22 Conv | 2026-W23 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 15,391 | 20,599 | +5,208 | +33.84pp | - | - | - |
| Checkout Attempt | 8,940 | 10,860 | +1,920 | +21.48pp | 58.09% | 52.72% | -5.36pp |
| Enter Fraud Service | 8,896 | 10,827 | +1,931 | +21.71pp | 99.51% | 99.70% | +0.19pp |
| Approved by Fraud Service | 8,383 | 10,164 | +1,781 | +21.25pp | 94.23% | 93.88% | -0.36pp |
| PVS Attempt | 6,590 | 8,072 | +1,482 | +22.49pp | 78.61% | 79.42% | +0.81pp |
| PVS Success | 6,476 | 7,953 | +1,477 | +22.81pp | 98.27% | 98.53% | +0.26pp |
| **Successful Checkout** | 8,292 | 10,052 | +1,760 | +21.23pp | 128.04% | 126.39% | -1.65pp |

**Key Driver:** Checkout Attempt (-5.36pp)

---



## Fraud Analysis

**Include reason:** Enter FS Δ (+0.70pp) meets threshold (+0.04pp)

### Gap (Checkout Attempt → Enter Fraud Service)

| Metric | 2026-W22 | 2026-W22 % | 2026-W23 | 2026-W23 % | Δ Count | Δ % |
|--------|-------------|---------------|-----------------|-------------------|---------|-----|
| Checkout Attempt | 34,869 | - | 38,587 | - | 3,718 | 10.7% |
| Enter Fraud Service | 33,863 | - | 37,295 | - | 3,432 | 10.1% |
| **Gap (Skipped)** | **1,006** | **2.89%** | **1,292** | **3.35%** | **286** | **+0.46pp** |

*Gap % = Gap / Checkout Attempt*

### Gap by Payment Method

| Payment Method | 2026-W22 Gap | 2026-W22 % | 2026-W23 Gap | 2026-W23 % | Δ Count | Δ % |
|----------------|-----------------|---------------|---------------------|-------------------|---------|-----|
| Adyen_Sepa | 867 | 88.2% | 1,113 | 87.6% | +246 | -0.56pp |
| NoPayment | 46 | 4.7% | 76 | 6.0% | +30 | +1.30pp |
| ProcessOut_CreditCard | 22 | 2.2% | 33 | 2.6% | +11 | +0.36pp |
| Braintree_ApplePay | 37 | 3.8% | 31 | 2.4% | -6 | -1.32pp |
| Braintree_Paypal | 11 | 1.1% | 17 | 1.3% | +6 | +0.22pp |
| **Total** | **983** | **100%** | **1,270** | **100%** | **287** | - |

*% of Gap = Payment Method Gap / Total Gap*

---


---

*Report: 2026-06-09*
