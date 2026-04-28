# AR Initial (LL0) Investigation: HF-INTL 2026-W17

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 91.22% → 91.8% (+0.64%)  
**Volume:** 32,225 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate for HF-INTL improved from 91.22% to 91.8% (+0.58pp) in W17, though the change is not statistically significant with volume declining from 33,935 to 32,225 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (89.7%-91.8%) | +0.58pp | ✅ |
| L1: Country Breakdown | 4 countries exceed ±2.5% threshold | LU -7.94%, CH -5.66%, FR +2.79%, NZ +5.68% | ⚠️ |
| L1: Payment Method | Credit Card declined significantly | -6.09% | ⚠️ |
| L1: Payment Provider | ProcessOut shows no volume (was 87.72%) | -100% volume | ⚠️ |
| L2: Root Cause | Insufficient Funds driving declines | LU +3.04pp, CH +4.37pp | ⚠️ |
| L3: Related Metrics | All funnel metrics improved | +0.64% to +0.91% | ✅ |

**Key Findings:**
- ProcessOut payment provider shows zero volume in W17 across multiple countries (LU, FR, NZ), suggesting a provider migration or outage that is masking underlying performance
- LU experienced the largest AR decline (-7.94pp) driven by Apple Pay dropping from 89.19% to 69.23% and Braintree declining from 90.70% to 79.49%
- CH declined -5.66pp with Insufficient Funds increasing from 5.93% to 10.29% of transactions, primarily through Braintree (-10.14%)
- FR improved +2.79pp despite ProcessOut going offline, with Insufficient Funds declining from 4.26% to 2.55%
- Mix shift shows FR volume dropped -24.4% (7,153 to 5,409) which may be artificially inflating the overall rate improvement

**Action:** Monitor - The overall metric is not significant and trending within normal bounds, but investigate the ProcessOut provider status and the "None" payment method data anomalies appearing across all flagged countries, as these suggest data quality or migration issues rather than true performance changes.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 91.8% | 32,225 | +0.64% ← REPORTED CHANGE |
| 2026-W16 | 91.22% | 33,935 | -0.36% |
| 2026-W15 | 91.55% | 26,541 | +2.06% |
| 2026-W14 | 89.7% | 30,311 | -0.34% |
| 2026-W13 | 90.01% | 34,168 | -1.20% |
| 2026-W12 | 91.1% | 38,627 | -0.37% |
| 2026-W11 | 91.44% | 42,241 | +1.22% |
| 2026-W10 | 90.34% | 47,305 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| LU | 82.05% | 89.13% | -7.94% | 78 | ⚠️ |
| CH | 84.56% | 89.63% | -5.66% | 136 | ⚠️ |
| GB | 92.03% | 90.98% | +1.15% | 8,953 |  |
| NO | 90.66% | 88.66% | +2.26% | 1,092 |  |
| FR | 96.01% | 93.40% | +2.79% | 5,409 | ⚠️ |
| NZ | 73.21% | 69.28% | +5.68% | 810 | ⚠️ |

**Countries exceeding ±2.5% threshold:** LU, CH, FR, NZ

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 82.66% | 88.03% | -6.09% | 323 | ⚠️ |
| Paypal | 95.27% | 95.95% | -0.70% | 5,968 |  |
| Others | 91.6% | 91.77% | -0.18% | 17,167 |  |
| Apple Pay | 90.16% | 89.14% | +1.14% | 8,767 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 87.72% | +nan% | 0 |  |
| Braintree | 92.23% | 92.25% | -0.03% | 14,735 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 86 |  |
| Unknown | 90.38% | 90.11% | +0.30% | 14,471 |  |
| Adyen | 96.39% | 95.75% | +0.66% | 2,933 |  |

---

## L2: LU Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 100.00% | 0.00% | +0.00% | 5 | 0 |  |
| None | 0.00% | 91.67% | -100.00% | 0 | 12 | ⚠️ |
| applepay | 69.23% | 89.19% | -22.38% | 26 | 37 | ⚠️ |
| credit_card | 80.00% | 85.29% | -6.21% | 30 | 34 | ⚠️ |
| paypal | 100.00% | 100.00% | +0.00% | 13 | 6 |  |
| sepadirectdebit | 100.00% | 100.00% | +0.00% | 4 | 3 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| ProcessOut | 0.00% | 100.00% | -100.00% | 0 | 1 | ⚠️ |
| Braintree | 79.49% | 90.70% | -12.36% | 39 | 43 | ⚠️ |
| Adyen | 82.35% | 86.11% | -4.36% | 34 | 36 |  |
| Unknown | 100.00% | 91.67% | +9.09% | 5 | 12 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 64 | 82 | 82.05% | 89.13% | -7.08 |
| Insufficient Funds | 10 | 9 | 12.82% | 9.78% | +3.04 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 2 | 0 | 2.56% | 0.00% | +2.56 |
| Other reasons | 2 | 1 | 2.56% | 1.09% | +1.48 |

**Root Cause:** None + ProcessOut + Insufficient

---

## L2: CH Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 87.50% | 0.00% | +0.00% | 72 | 0 |  |
| None | 0.00% | 89.55% | -100.00% | 0 | 67 | ⚠️ |
| paypal | 76.47% | 89.47% | -14.53% | 17 | 19 | ⚠️ |
| applepay | 81.82% | 89.36% | -8.44% | 44 | 47 | ⚠️ |
| cashcredit | 100.00% | 100.00% | +0.00% | 1 | 1 |  |
| credit_card | 100.00% | 100.00% | +0.00% | 2 | 1 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Braintree | 80.33% | 89.39% | -10.14% | 61 | 66 | ⚠️ |
| Unknown | 87.50% | 89.55% | -2.29% | 72 | 67 |  |
| Adyen | 100.00% | 100.00% | +0.00% | 2 | 1 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 1 | 1 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 115 | 121 | 84.56% | 89.63% | -5.07 |
| Insufficient Funds | 14 | 8 | 10.29% | 5.93% | +4.37 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 4 | 3 | 2.94% | 2.22% | +0.72 |
| Other reasons | 3 | 3 | 2.21% | 2.22% | -0.02 |

**Root Cause:** None + Braintree + Insufficient

---

## L2: FR Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 95.99% | 0.00% | +0.00% | 3,117 | 0 |  |
| None | 0.00% | 92.32% | -100.00% | 0 | 2,461 | ⚠️ |
| cashcredit | 100.00% | 100.00% | +0.00% | 5 | 3 |  |
| credit_card | 93.75% | 93.64% | +0.12% | 16 | 1,634 |  |
| paypal | 97.85% | 97.14% | +0.74% | 698 | 908 |  |
| applepay | 95.23% | 92.87% | +2.54% | 1,573 | 2,147 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| ProcessOut | 0.00% | 94.11% | -100.00% | 0 | 1,595 | ⚠️ |
| No Payment | 100.00% | 100.00% | +0.00% | 5 | 3 |  |
| Braintree | 96.04% | 94.14% | +2.01% | 2,271 | 3,055 |  |
| Unknown | 96.10% | 92.53% | +3.86% | 3,103 | 2,450 |  |
| Adyen | 83.33% | 68.00% | +22.55% | 30 | 50 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 5,193 | 6,681 | 96.01% | 93.40% | +2.61 |
| Insufficient Funds | 138 | 305 | 2.55% | 4.26% | -1.71 |
| Other reasons | 54 | 123 | 1.00% | 1.72% | -0.72 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 23 | 41 | 0.43% | 0.57% | -0.15 |
| Unknown | 1 | 3 | 0.02% | 0.04% | -0.02 |

**Root Cause:** None + ProcessOut + Insufficient

---

## L2: NZ Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 73.99% | 0.00% | +0.00% | 765 | 0 |  |
| None | 0.00% | 68.12% | -100.00% | 0 | 229 | ⚠️ |
| applepay | 0.00% | 70.70% | -100.00% | 0 | 157 | ⚠️ |
| paypal | 53.85% | 58.62% | -8.14% | 26 | 29 | ⚠️ |
| credit_card | 66.67% | 69.98% | -4.73% | 18 | 453 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 1 | 1 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| ProcessOut | 0.00% | 70.00% | -100.00% | 0 | 600 | ⚠️ |
| Adyen | 72.73% | 81.82% | -11.11% | 22 | 11 | ⚠️ |
| Braintree | 53.85% | 58.62% | -8.14% | 26 | 29 | ⚠️ |
| No Payment | 100.00% | 100.00% | +0.00% | 1 | 1 |  |
| Unknown | 73.85% | 67.98% | +8.63% | 761 | 228 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 593 | 602 | 73.21% | 69.28% | +3.93 |
| Insufficient Funds | 186 | 229 | 22.96% | 26.35% | -3.39 |
| Unknown | 0 | 3 | 0.00% | 0.35% | -0.35 |
| Other reasons | 19 | 23 | 2.35% | 2.65% | -0.30 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 12 | 12 | 1.48% | 1.38% | +0.10 |

**Root Cause:** None + ProcessOut + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 89.73% | 88.92% | +0.91% | 32,225 | 33,935 |  |
| 2_PreDunningAR | 91.8% | 91.22% | +0.64% | 32,225 | 33,935 |  |
| 3_PostDunningAR | 92.32% | 91.65% | +0.73% | 32,225 | 33,935 |  |
| 6_PaymentApprovalRate | 92.68% | 92.03% | +0.70% | 32,225 | 33,935 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | Medium (>85%) | 8,588 | 8,953 | +4.3% | Stable |
| FR | High (>92%) | 7,153 | 5,409 | -24.4% | ⚠️ Volume drop |
| DE | High (>92%) | 6,121 | 5,888 | -3.8% | Stable |
| AU | Low (>85%) | 2,643 | 2,684 | +1.6% | Stable |
| BE | High (>92%) | 1,793 | 1,692 | -5.6% | Stable |
| NL | High (>92%) | 1,369 | 1,102 | -19.5% | Stable |
| IE | Medium (>85%) | 1,363 | 1,436 | +5.4% | Stable |
| DK | High (>92%) | 1,228 | 1,109 | -9.7% | Stable |
| SE | High (>92%) | 1,216 | 1,319 | +8.5% | Stable |
| NZ | Low (>85%) | 869 | 810 | -6.8% | Stable |
| NO | Medium (>85%) | 767 | 1,092 | +42.4% | Stable |
| AT | High (>92%) | 598 | 517 | -13.5% | Stable |
| CH | Medium (>85%) | 135 | 136 | +0.7% | Stable |
| LU | Medium (>85%) | 92 | 78 | -15.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| LU | ↓ -7.94% | None -100.0% | ProcessOut -100.0% | Insufficient Funds +3.04pp | None + ProcessOut + Insufficient |
| CH | ↓ -5.66% | None -100.0% | Braintree -10.1% | Insufficient Funds +4.37pp | None + Braintree + Insufficient |
| FR | ↑ +2.79% | None -100.0% | ProcessOut -100.0% | Insufficient Funds -1.71pp | None + ProcessOut + Insufficient |
| NZ | ↑ +5.68% | None -100.0% | ProcessOut -100.0% | Insufficient Funds -3.39pp | None + ProcessOut + Insufficient |

---

*Report: 2026-04-28*
