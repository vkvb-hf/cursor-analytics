# AR Initial (LL0) Investigation: HF-INTL 2026-W23

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 90.03% → 90.41% (+0.42%)  
**Volume:** 27,339 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate for HF-INTL improved from 90.03% to 90.41% (+0.38pp) in W23, a statistically non-significant change with volume increasing from 22,483 to 27,339 orders (+21.6%).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (90.41% vs 8-wk avg ~91.3%) | +0.42% | ✅ |
| L1: Country Breakdown | 5 countries exceed ±2.5% threshold (NZ, FR, BE, SE, AT) | Mixed | ⚠️ |
| L1: Dimension Scan | All PaymentMethods and Providers within normal range | <1% | ✅ |
| L2: Country Deep-Dives | Insufficient Funds increased in NZ (+3.46pp), FR (+2.69pp), BE (+2.36pp) | Elevated | ⚠️ |
| L3: Related Metrics | All funnel metrics improved consistently (+0.36% to +0.55%) | Aligned | ✅ |
| Mix Shift | No significant tier migrations; FR volume +48.9%, NL +55.1% | Stable | ✅ |

**Key Findings:**
- NZ experienced the largest decline (-3.84pp to 73.95%), driven by Insufficient Funds increasing from 20.33% to 23.80% (+3.46pp) and Apple Pay declining 6.64%
- FR declined -3.67pp despite 48.9% volume growth, with Apple Pay dropping 5.27% and Insufficient Funds rising +2.69pp
- SE showed strong improvement (+4.89pp) with Insufficient Funds decreasing significantly (-4.43pp) and Apple Pay recovering +19.31%
- BE declined -3.21pp with Insufficient Funds increasing +2.36pp, affecting both credit card (-4.87%) and Apple Pay (-3.27%)
- Overall metric improvement masks offsetting country movements; decliners (NZ, FR, BE) were offset by improvers (SE +4.89%, AT +4.97%)

**Action:** Monitor - The overall change is not statistically significant and the metric remains within historical range. Continue monitoring Insufficient Funds trends in NZ, FR, and BE over the next 2 weeks; escalate if decline pattern persists.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W23 | 90.41% | 27,339 | +0.42% ← REPORTED CHANGE |
| 2026-W22 | 90.03% | 22,483 | -1.99% |
| 2026-W21 | 91.86% | 27,878 | -0.36% |
| 2026-W20 | 92.19% | 28,002 | -0.12% |
| 2026-W19 | 92.3% | 30,778 | +1.34% |
| 2026-W18 | 91.08% | 27,138 | -0.23% |
| 2026-W17 | 91.29% | 31,472 | +0.16% |
| 2026-W16 | 91.14% | 32,881 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| NZ | 73.95% | 76.90% | -3.84% | 664 | ⚠️ |
| FR | 91.69% | 95.19% | -3.67% | 5,298 | ⚠️ |
| BE | 90.60% | 93.60% | -3.21% | 1,882 | ⚠️ |
| GB | 90.72% | 89.77% | +1.05% | 6,958 |  |
| DE | 91.93% | 89.77% | +2.40% | 4,437 |  |
| SE | 95.11% | 90.68% | +4.89% | 921 | ⚠️ |
| AT | 92.33% | 87.97% | +4.97% | 287 | ⚠️ |

**Countries exceeding ±2.5% threshold:** NZ, FR, BE, SE, AT

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 96.22% | 96.89% | -0.69% | 5,607 |  |
| Credit Card | 88.05% | 87.82% | +0.26% | 9,306 |  |
| Apple Pay | 86.68% | 85.91% | +0.90% | 8,125 |  |
| Paypal | 94.95% | 93.46% | +1.60% | 4,301 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Adyen | 96.43% | 97.13% | -0.72% | 4,345 |  |
| Unknown | 93.55% | 94.19% | -0.68% | 1,505 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 68 |  |
| ProcessOut | 87.08% | 86.49% | +0.68% | 10,109 |  |
| Braintree | 90.59% | 89.84% | +0.82% | 11,312 |  |

---

## L2: NZ Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 100.00% | 0.00% | +0.00% | 9 | 0 |  |
| None | 0.00% | 95.00% | -100.00% | 0 | 20 | ⚠️ |
| applepay | 68.81% | 73.71% | -6.64% | 202 | 232 | ⚠️ |
| credit_card | 75.69% | 78.32% | -3.35% | 432 | 452 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 5 | 2 |  |
| paypal | 68.75% | 58.82% | +16.88% | 16 | 17 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 75.00% | -100.00% | 0 | 4 | ⚠️ |
| Adyen | 86.67% | 92.00% | -5.80% | 15 | 25 | ⚠️ |
| ProcessOut | 73.57% | 76.74% | -4.14% | 628 | 675 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 5 | 2 |  |
| Braintree | 68.75% | 58.82% | +16.88% | 16 | 17 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Insufficient Funds | 158 | 147 | 23.80% | 20.33% | +3.46 |
| 1. SUCCESSFULL | 491 | 556 | 73.95% | 76.90% | -2.96 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 5 | 7 | 0.75% | 0.97% | -0.22 |
| Other reasons | 10 | 12 | 1.51% | 1.66% | -0.15 |
| Unknown | 0 | 1 | 0.00% | 0.14% | -0.14 |

**Root Cause:** None + Unknown + Insufficient

---

## L2: FR Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 8 | 0 |  |
| None | 0.00% | 0.00% | +0.00% | 0 | 5 |  |
| cashcredit | 100.00% | 0.00% | +0.00% | 1 | 0 |  |
| applepay | 89.00% | 93.96% | -5.27% | 1,546 | 1,026 | ⚠️ |
| credit_card | 92.39% | 95.40% | -3.15% | 3,101 | 2,064 |  |
| paypal | 95.95% | 98.05% | -2.14% | 642 | 462 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| No Payment | 100.00% | 0.00% | +0.00% | 1 | 0 |  |
| Unknown | 0.00% | 0.00% | +0.00% | 6 | 2 |  |
| Braintree | 91.04% | 95.23% | -4.40% | 2,188 | 1,488 |  |
| ProcessOut | 92.42% | 95.39% | -3.12% | 3,073 | 2,040 |  |
| Adyen | 83.33% | 85.19% | -2.17% | 30 | 27 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 4,858 | 3,386 | 91.69% | 95.19% | -3.50 |
| Insufficient Funds | 305 | 109 | 5.76% | 3.06% | +2.69 |
| Other reasons | 89 | 42 | 1.68% | 1.18% | +0.50 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 43 | 14 | 0.81% | 0.39% | +0.42 |
| Unknown | 3 | 6 | 0.06% | 0.17% | -0.11 |

**Root Cause:** applepay + Insufficient

---

## L2: BE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 97.66% | 0.00% | +0.00% | 427 | 0 |  |
| cashcredit | 100.00% | 0.00% | +0.00% | 1 | 0 |  |
| None | 0.00% | 99.34% | -100.00% | 0 | 455 | ⚠️ |
| credit_card | 78.41% | 82.43% | -4.87% | 227 | 148 |  |
| applepay | 74.40% | 76.92% | -3.27% | 168 | 104 |  |
| bancontact | 89.53% | 91.91% | -2.59% | 592 | 408 |  |
| sepadirectdebit | 97.70% | 97.54% | +0.17% | 392 | 406 |  |
| paypal | 94.67% | 91.38% | +3.60% | 75 | 58 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| No Payment | 100.00% | 0.00% | +0.00% | 1 | 0 |  |
| ProcessOut | 78.80% | 81.02% | -2.74% | 217 | 137 |  |
| Adyen | 92.56% | 94.79% | -2.36% | 994 | 825 |  |
| Braintree | 80.66% | 82.10% | -1.75% | 243 | 162 |  |
| Unknown | 97.66% | 99.34% | -1.69% | 427 | 455 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,705 | 1,478 | 90.60% | 93.60% | -3.01 |
| Insufficient Funds | 129 | 71 | 6.85% | 4.50% | +2.36 |
| Unknown | 10 | 1 | 0.53% | 0.06% | +0.47 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 17 | 10 | 0.90% | 0.63% | +0.27 |
| Other reasons | 21 | 19 | 1.12% | 1.20% | -0.09 |

**Root Cause:** None + Insufficient

---

## L2: SE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 97.16% | 0.00% | +0.00% | 141 | 0 |  |
| None | 0.00% | 97.08% | -100.00% | 0 | 137 | ⚠️ |
| cashcredit | 100.00% | 100.00% | +0.00% | 3 | 1 |  |
| klarna | 98.67% | 98.54% | +0.14% | 377 | 342 |  |
| credit_card | 89.40% | 83.89% | +6.57% | 217 | 180 | ⚠️ |
| paypal | 90.91% | 81.82% | +11.11% | 11 | 11 | ⚠️ |
| applepay | 93.02% | 77.97% | +19.31% | 172 | 177 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Adyen | 98.82% | 98.94% | -0.12% | 510 | 471 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 3 | 1 |  |
| Unknown | 75.00% | 75.00% | +0.00% | 16 | 16 |  |
| ProcessOut | 89.47% | 83.14% | +7.62% | 209 | 172 | ⚠️ |
| Braintree | 92.90% | 78.19% | +18.81% | 183 | 188 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 876 | 769 | 95.11% | 90.68% | +4.43 |
| Insufficient Funds | 32 | 67 | 3.47% | 7.90% | -4.43 |
| Other reasons | 9 | 4 | 0.98% | 0.47% | +0.51 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 1 | 4 | 0.11% | 0.47% | -0.36 |
| Unknown | 3 | 4 | 0.33% | 0.47% | -0.15 |

**Root Cause:** None + ProcessOut + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.19% | 87.88% | +0.36% | 27,339 | 22,483 |  |
| 2_PreDunningAR | 90.41% | 90.03% | +0.41% | 27,339 | 22,483 |  |
| 3_PostDunningAR | 90.93% | 90.54% | +0.43% | 27,339 | 22,483 |  |
| 6_PaymentApprovalRate | 91.32% | 90.82% | +0.55% | 27,339 | 22,483 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | Medium (>85%) | 5,592 | 6,958 | +24.4% | Stable |
| DE | Medium (>85%) | 3,696 | 4,437 | +20.0% | Stable |
| FR | High (>92%) | 3,557 | 5,298 | +48.9% | Stable |
| AU | Low (>85%) | 2,602 | 2,588 | -0.5% | Stable |
| BE | High (>92%) | 1,579 | 1,882 | +19.2% | Stable |
| IE | Medium (>85%) | 1,354 | 1,365 | +0.8% | Stable |
| SE | Medium (>85%) | 848 | 921 | +8.6% | Stable |
| NL | High (>92%) | 821 | 1,273 | +55.1% | Stable |
| DK | High (>92%) | 749 | 857 | +14.4% | Stable |
| NZ | Low (>85%) | 723 | 664 | -8.2% | Stable |
| NO | Medium (>85%) | 449 | 592 | +31.8% | Stable |
| AT | Medium (>85%) | 349 | 287 | -17.8% | Stable |
| CH | Low (>85%) | 108 | 110 | +1.9% | Stable |
| LU | Medium (>85%) | 56 | 107 | +91.1% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| NZ | ↓ -3.84% | None -100.0% | Unknown -100.0% | Insufficient Funds +3.46pp | None + Unknown + Insufficient |
| FR | ↓ -3.67% | applepay -5.3% | → Stable | Insufficient Funds +2.69pp | applepay + Insufficient |
| BE | ↓ -3.21% | None -100.0% | → Stable | Insufficient Funds +2.36pp | None + Insufficient |
| SE | ↑ +4.89% | None -100.0% | ProcessOut +7.6% | Insufficient Funds -4.43pp | None + ProcessOut + Insufficient |

---

*Report: 2026-06-09*
