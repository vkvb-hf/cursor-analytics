# PCR Investigation: RTE 2026-W19

**Metric:** Payment Conversion Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 37.89% → 38.59% (+0.70pp)  
**Volume:** 65,181 payment visits  
**Threshold:** +0.35pp (0.5 × |Overall PCR Δ|)

## Executive Summary

## Executive Summary

**Overall:** Payment Conversion Rate improved by +0.70pp (37.89% → 38.59%) on 65,181 payment visits, exceeding the +0.35pp threshold, driven primarily by increased conversion at the Select Payment Method step.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Select Payment Method | ≥ +0.35pp | +0.85pp | ✅ |
| Click Submit Form | ≥ +0.35pp | -0.13pp | ⚠️ |
| FE Validation Passed | ≥ +0.35pp | +0.02pp | ⚠️ |
| Enter Fraud Service | ≥ +0.35pp | +0.17pp | ⚠️ |
| Approved by Fraud Service | ≥ +0.35pp | -0.13pp | ⚠️ |
| Call to PVS | ≥ +0.35pp | -0.01pp | ⚠️ |
| Successful Checkout | ≥ +0.35pp | +0.17pp | ⚠️ |

**Key Findings:**
- **Select Payment Method** is the primary driver of improvement at both L0 (+0.85pp GA) and country level, with FJ (+1.38pp), TO (+4.90pp), and TK (+4.15pp) showing strong gains
- **Braintree_ApplePay** showed the strongest payment method improvement (+1.23pp to 93.09%), while **Braintree_CreditCard** declined significantly (-3.86pp to 84.80%)
- **FJ** contributes the largest volume impact with +1.27pp improvement on 40,460 visits, while **CF** is the only top country showing decline (-0.89pp)
- Backend data shows **PVS Attempt** conversion dropped -0.37pp at L0, warranting monitoring despite overall positive trend
- Overall payment visits decreased by -2.9% (-1,940 visits), but higher funnel conversion rates offset the volume decline

**Action:** **Monitor** - The improvement is positive and driven by identifiable factors (Select Payment Method step, ApplePay performance). Continue monitoring Braintree_CreditCard decline and CF country performance for potential intervention.

---

---

## L0: Cluster-Level Waterfall

### Waterfall GA (Google Analytics)

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 67,121 | 65,181 | -1,940 | -2.9% | - | - | - |
| Select Payment Method | 32,457 | 32,072 | -385 | -1.2% | 48.36% | 49.20% | +0.85pp |
| Click Submit Form | 29,039 | 28,654 | -385 | -1.3% | 89.47% | 89.34% | -0.13pp |
| FE Validation Passed | 28,421 | 28,050 | -371 | -1.3% | 97.87% | 97.89% | +0.02pp |
| Enter Fraud Service | 27,666 | 27,353 | -313 | -1.1% | 97.34% | 97.52% | +0.17pp |
| Approved by Fraud Service | 26,655 | 26,318 | -337 | -1.3% | 96.35% | 96.22% | -0.13pp |
| Call to PVS | 26,550 | 26,212 | -338 | -1.3% | 99.61% | 99.60% | -0.01pp |
| **Successful Checkout** | 25,429 | 25,151 | -278 | -1.1% | 95.78% | 95.95% | +0.17pp |
| **PCR Rate** | | | | | 37.89% | 38.59% | **+0.70pp** |

### Waterfall Backend

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 117,564 | 111,336 | -6,228 | -5.3% | - | - | - |
| Checkout Attempt | 43,278 | 41,790 | -1,488 | -3.4% | 36.81% | 37.54% | +0.72pp |
| Enter Fraud Service | 43,213 | 41,733 | -1,480 | -3.4% | 99.85% | 99.86% | +0.01pp |
| Approved by Fraud Service | 40,887 | 39,469 | -1,418 | -3.5% | 94.62% | 94.58% | -0.04pp |
| PVS Attempt | 40,202 | 38,661 | -1,541 | -3.8% | 98.32% | 97.95% | -0.37pp |
| PVS Success | 38,801 | 37,371 | -1,430 | -3.7% | 96.52% | 96.66% | +0.15pp |
| **Successful Checkout** | 39,682 | 38,363 | -1,319 | -3.3% | 102.27% | 102.65% | +0.38pp |
| **PCR Rate** | | | | | 33.75% | 34.46% | **+0.70pp** |

### Payment Method Breakdown

| Payment Method | 2026-W18 Attempt | 2026-W18 Success | 2026-W18 Rate | 2026-W19 Attempt | 2026-W19 Success | 2026-W19 Rate | Δ Rate |
| -------------- | ------------------- | ------------------- | ---------------- | ----------------------- | ----------------------- | -------------------- | ------ |
| ProcessOut_CreditCard | 17,733 | 16,355 | 92.23% | 16,932 | 15,593 | 92.09% | -0.14pp |
| Adyen_CreditCard | 9,721 | 8,735 | 89.86% | 9,613 | 8,609 | 89.56% | -0.30pp |
| Braintree_ApplePay | 9,801 | 9,003 | 91.86% | 9,221 | 8,584 | 93.09% | +1.23pp |
| Braintree_Paypal | 4,901 | 4,551 | 92.86% | 4,821 | 4,473 | 92.78% | -0.08pp |
| Adyen_IDeal | 710 | 657 | 92.54% | 668 | 626 | 93.71% | +1.18pp |
| Adyen_Klarna | 300 | 284 | 94.67% | 325 | 302 | 92.92% | -1.74pp |
| Braintree_CreditCard | 97 | 86 | 88.66% | 204 | 173 | 84.80% | -3.86pp |
| Braintree_Venmo | 11 | 11 | 100.00% | 3 | 3 | 100.00% | +0.00pp |
| visa | 0 | 0 | 0.00% | 2 | 0 | 0.00% | +0.00pp |
| mc | 0 | 0 | 0.00% | 1 | 0 | 0.00% | +0.00pp |

---

## Country-Level Analysis

**Country Selection:** Top 2 by contribution + Top 2 by absolute change (4 countries in RTE)

| Country | Volume | PCR 2026-W18 | PCR 2026-W19 | Δ PCR | Contribution Rank | Change Rank |
|---------|--------|-----------------|-----------------|-------|-------------------|-------------|
| FJ | 40,460 | 38.36% | 39.63% | +1.27pp | 1 | 4 |
| CF | 13,258 | 42.17% | 41.28% | -0.89pp | 2 | 6 |
| TO | 943 | 29.28% | 32.24% | +2.96pp | 3 | 1 |
| TK | 578 | 39.10% | 42.04% | +2.94pp | 6 | 2 |

---

### TK

#### Waterfall GA

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 578 | 578 | 0 | +0.00pp | - | - | - |
| Select Payment Method | 288 | 312 | +24 | +8.33pp | 49.83% | 53.98% | +4.15pp |
| Click Submit Form | 260 | 284 | +24 | +9.23pp | 90.28% | 91.03% | +0.75pp |
| FE Validation Passed | 251 | 269 | +18 | +7.17pp | 96.54% | 94.72% | -1.82pp |
| Enter Fraud Service | 247 | 262 | +15 | +6.07pp | 98.41% | 97.40% | -1.01pp |
| Approved by Fraud Service | 234 | 244 | +10 | +4.27pp | 94.74% | 93.13% | -1.61pp |
| Call to PVS | 235 | 246 | +11 | +4.68pp | 100.43% | 100.82% | +0.39pp |
| **Successful Checkout** | 226 | 243 | +17 | +7.52pp | 96.17% | 98.78% | +2.61pp |
| **PCR Rate** | | | | | 39.10% | 42.04% | **+2.94pp** |

**Key Driver:** Select Payment Method (+4.15pp)

#### Waterfall Backend

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 871 | 936 | +65 | +7.46pp | - | - | - |
| Checkout Attempt | 348 | 387 | +39 | +11.21pp | 39.95% | 41.35% | +1.39pp |
| Enter Fraud Service | 348 | 387 | +39 | +11.21pp | 100.00% | 100.00% | +0.00pp |
| Approved by Fraud Service | 324 | 348 | +24 | +7.41pp | 93.10% | 89.92% | -3.18pp |
| PVS Attempt | 324 | 348 | +24 | +7.41pp | 100.00% | 100.00% | +0.00pp |
| PVS Success | 320 | 347 | +27 | +8.44pp | 98.77% | 99.71% | +0.95pp |
| **Successful Checkout** | 321 | 348 | +27 | +8.41pp | 100.31% | 100.29% | -0.02pp |

**Key Driver:** Approved by Fraud Service (-3.18pp)

---

### CF

#### Waterfall GA

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 12,711 | 13,258 | +547 | +4.30pp | - | - | - |
| Select Payment Method | 6,658 | 6,768 | +110 | +1.65pp | 52.38% | 51.05% | -1.33pp |
| Click Submit Form | 6,056 | 6,131 | +75 | +1.24pp | 90.96% | 90.59% | -0.37pp |
| FE Validation Passed | 6,031 | 6,088 | +57 | +0.95pp | 99.59% | 99.30% | -0.29pp |
| Enter Fraud Service | 5,853 | 5,923 | +70 | +1.20pp | 97.05% | 97.29% | +0.24pp |
| Approved by Fraud Service | 5,581 | 5,659 | +78 | +1.40pp | 95.35% | 95.54% | +0.19pp |
| Call to PVS | 5,543 | 5,619 | +76 | +1.37pp | 99.32% | 99.29% | -0.03pp |
| **Successful Checkout** | 5,360 | 5,473 | +113 | +2.11pp | 96.70% | 97.40% | +0.70pp |
| **PCR Rate** | | | | | 42.17% | 41.28% | **-0.89pp** |

**Key Driver:** Select Payment Method (-1.33pp)

#### Waterfall Backend

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 14,566 | 15,103 | +537 | +3.69pp | - | - | - |
| Checkout Attempt | 6,876 | 6,905 | +29 | +0.42pp | 47.21% | 45.72% | -1.49pp |
| Enter Fraud Service | 6,834 | 6,866 | +32 | +0.47pp | 99.39% | 99.44% | +0.05pp |
| Approved by Fraud Service | 6,364 | 6,401 | +37 | +0.58pp | 93.12% | 93.23% | +0.10pp |
| PVS Attempt | 5,977 | 6,009 | +32 | +0.54pp | 93.92% | 93.88% | -0.04pp |
| PVS Success | 5,816 | 5,886 | +70 | +1.20pp | 97.31% | 97.95% | +0.65pp |
| **Successful Checkout** | 6,244 | 6,308 | +64 | +1.02pp | 107.36% | 107.17% | -0.19pp |

**Key Driver:** Checkout Attempt (-1.49pp)

---

### FJ

#### Waterfall GA

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 42,822 | 40,460 | -2,362 | -5.52pp | - | - | - |
| Select Payment Method | 20,402 | 19,834 | -568 | -2.78pp | 47.64% | 49.02% | +1.38pp |
| Click Submit Form | 18,347 | 17,886 | -461 | -2.51pp | 89.93% | 90.18% | +0.25pp |
| FE Validation Passed | 17,838 | 17,434 | -404 | -2.26pp | 97.23% | 97.47% | +0.25pp |
| Enter Fraud Service | 17,487 | 17,096 | -391 | -2.24pp | 98.03% | 98.06% | +0.03pp |
| Approved by Fraud Service | 16,937 | 16,548 | -389 | -2.30pp | 96.85% | 96.79% | -0.06pp |
| Call to PVS | 16,887 | 16,491 | -396 | -2.34pp | 99.70% | 99.66% | -0.05pp |
| **Successful Checkout** | 16,425 | 16,036 | -389 | -2.37pp | 97.26% | 97.24% | -0.02pp |
| **PCR Rate** | | | | | 38.36% | 39.63% | **+1.28pp** |

**Key Driver:** Select Payment Method (+1.38pp)

#### Waterfall Backend

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 85,981 | 79,074 | -6,907 | -8.03pp | - | - | - |
| Checkout Attempt | 30,038 | 28,520 | -1,518 | -5.05pp | 34.94% | 36.07% | +1.13pp |
| Enter Fraud Service | 30,020 | 28,506 | -1,514 | -5.04pp | 99.94% | 99.95% | +0.01pp |
| Approved by Fraud Service | 28,615 | 27,212 | -1,403 | -4.90pp | 95.32% | 95.46% | +0.14pp |
| PVS Attempt | 28,528 | 27,034 | -1,494 | -5.24pp | 99.70% | 99.35% | -0.35pp |
| PVS Success | 27,725 | 26,293 | -1,432 | -5.17pp | 97.19% | 97.26% | +0.07pp |
| **Successful Checkout** | 27,810 | 26,455 | -1,355 | -4.87pp | 100.31% | 100.62% | +0.31pp |

**Key Driver:** Checkout Attempt (+1.13pp)

---

### TO

#### Waterfall GA

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Visits | 963 | 943 | -20 | -2.08pp | - | - | - |
| Select Payment Method | 444 | 481 | +37 | +8.33pp | 46.11% | 51.01% | +4.90pp |
| Click Submit Form | 369 | 398 | +29 | +7.86pp | 83.11% | 82.74% | -0.36pp |
| FE Validation Passed | 355 | 373 | +18 | +5.07pp | 96.21% | 93.72% | -2.49pp |
| Enter Fraud Service | 333 | 347 | +14 | +4.20pp | 93.80% | 93.03% | -0.77pp |
| Approved by Fraud Service | 309 | 326 | +17 | +5.50pp | 92.79% | 93.95% | +1.16pp |
| Call to PVS | 309 | 325 | +16 | +5.18pp | 100.00% | 99.69% | -0.31pp |
| **Successful Checkout** | 282 | 304 | +22 | +7.80pp | 91.26% | 93.54% | +2.28pp |
| **PCR Rate** | | | | | 29.28% | 32.24% | **+2.95pp** |

**Key Driver:** Select Payment Method (+4.90pp)

#### Waterfall Backend

| Funnel Step | 2026-W18 | 2026-W19 | Δ Count | Δ % | 2026-W18 Conv | 2026-W19 Conv | Δ Conv |
| ----------- | ----------- | --------------- | ------- | --- | ---------------- | -------------------- | ------ |
| Payment Method Listed | 1,377 | 1,397 | +20 | +1.45pp | - | - | - |
| Checkout Attempt | 456 | 502 | +46 | +10.09pp | 33.12% | 35.93% | +2.82pp |
| Enter Fraud Service | 456 | 502 | +46 | +10.09pp | 100.00% | 100.00% | +0.00pp |
| Approved by Fraud Service | 412 | 449 | +37 | +8.98pp | 90.35% | 89.44% | -0.91pp |
| PVS Attempt | 412 | 448 | +36 | +8.74pp | 100.00% | 99.78% | -0.22pp |
| PVS Success | 380 | 422 | +42 | +11.05pp | 92.23% | 94.20% | +1.96pp |
| **Successful Checkout** | 402 | 444 | +42 | +10.45pp | 105.79% | 105.21% | -0.58pp |

**Key Driver:** Checkout Attempt (+2.82pp)

---





---

*Report: 2026-05-12*
