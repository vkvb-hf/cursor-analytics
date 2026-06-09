# AR Overall Investigation: HF-INTL 2026-W23

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 94.49% → 94.63% (+0.15%)  
**Volume:** 725,582 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate for HF-INTL improved marginally from 94.49% to 94.63% (+0.15%) in 2026-W23, processing 725,582 orders. This change is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Within normal volatility range (93.92%-95.08%) | +0.15% | ✅ |
| L1: Country Breakdown | 1 country (CH) exceeded ±2.5% threshold | +2.55% CH | ⚠️ |
| L1: Dimension Scan | All PaymentMethods and Providers stable (<1% change) | Max +0.88% | ✅ |
| L2: CH Deep-Dive | twint discontinued (-100%), credit_card +3.31%, paypal +3.39% | Positive shift | ✅ |
| L3: Related Metrics | All funnel metrics stable (<0.15% change) | Aligned | ✅ |
| Mix Shift | No material volume shifts impacting rate | Stable | ✅ |

**Key Findings:**
- CH showed the largest rate improvement (+2.55%), driven by reduced "Insufficient Funds" declines (-1.51pp) and discontinuation of twint payment method (0 volume vs 20 prior week)
- GB volume increased significantly (+10.5%) while maintaining strong acceptance rate improvement (+0.89%)
- NO experienced the largest decline (-1.33%) but remains within acceptable range at 91.94%
- Apple Pay showed continued improvement (+0.88%) but remains the lowest-performing payment method at 89.72%
- LU volume increased +28.3% week-over-week with rate improvement (+1.43%)

**Action:** Monitor — No escalation required. The overall metric change is not significant and within normal operating range. Continue tracking NO performance and Apple Pay acceptance rates.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W23 | 94.63% | 725,582 | +0.15% ← REPORTED CHANGE |
| 2026-W22 | 94.49% | 701,558 | -0.47% |
| 2026-W21 | 94.94% | 748,425 | -0.15% |
| 2026-W20 | 95.08% | 747,579 | +0.50% |
| 2026-W19 | 94.61% | 789,195 | +0.73% |
| 2026-W18 | 93.92% | 780,887 | -0.72% |
| 2026-W17 | 94.6% | 794,762 | -0.20% |
| 2026-W16 | 94.79% | 804,346 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| NO | 91.94% | 93.18% | -1.33% | 19,419 |  |
| AU | 92.12% | 92.50% | -0.42% | 92,333 |  |
| FR | 93.67% | 94.06% | -0.41% | 135,257 |  |
| GB | 94.59% | 93.75% | +0.89% | 196,495 |  |
| SE | 97.41% | 96.20% | +1.26% | 33,415 |  |
| LU | 95.79% | 94.45% | +1.43% | 3,258 |  |
| CH | 93.89% | 91.55% | +2.55% | 2,094 | ⚠️ |

**Countries exceeding ±2.5% threshold:** CH

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 97.57% | 97.61% | -0.04% | 174,598 |  |
| Others | 98.9% | 98.82% | +0.08% | 119,271 |  |
| Credit Card | 92.98% | 92.89% | +0.10% | 335,175 |  |
| Apple Pay | 89.72% | 88.93% | +0.88% | 96,538 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 88.95% | 89.41% | -0.51% | 1,701 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 5,331 |  |
| ProcessOut | 92.61% | 92.53% | +0.09% | 204,980 |  |
| Adyen | 95.74% | 95.65% | +0.09% | 247,923 |  |
| Braintree | 95.07% | 94.88% | +0.20% | 265,647 |  |

---

## L2: CH Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 72.73% | 0.00% | +0.00% | 44 | 0 |  |
| twint | 0.00% | 90.00% | -100.00% | 0 | 20 | ⚠️ |
| cashcredit | 100.00% | 100.00% | +0.00% | 18 | 11 |  |
| applepay | 91.50% | 90.03% | +1.63% | 341 | 341 |  |
| credit_card | 94.62% | 91.59% | +3.31% | 1,301 | 1,343 |  |
| paypal | 95.64% | 92.51% | +3.39% | 390 | 427 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 0.00% | +0.00% | 1 | 0 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 18 | 11 |  |
| Adyen | 94.03% | 93.01% | +1.10% | 486 | 472 |  |
| Braintree | 93.71% | 91.41% | +2.52% | 731 | 768 |  |
| ProcessOut | 93.94% | 90.80% | +3.46% | 858 | 891 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,966 | 1,961 | 93.89% | 91.55% | +2.34 |
| Insufficient Funds | 71 | 105 | 3.39% | 4.90% | -1.51 |
| Other reasons | 17 | 33 | 0.81% | 1.54% | -0.73 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 40 | 43 | 1.91% | 2.01% | -0.10 |

**Root Cause:** twint + Insufficient

---

## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 92.35% | 92.41% | -0.07% | 725,582 | 701,558 |  |
| 2_PreDunningAR | 94.63% | 94.49% | +0.14% | 725,582 | 701,558 |  |
| 3_PostDunningAR | 96.81% | 96.85% | -0.04% | 725,582 | 701,558 |  |
| 6_PaymentApprovalRate | 97.54% | 97.44% | +0.10% | 725,582 | 701,558 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| DE | High (>92%) | 182,132 | 181,979 | -0.1% | Stable |
| GB | High (>92%) | 177,802 | 196,495 | +10.5% | Stable |
| FR | High (>92%) | 128,794 | 135,257 | +5.0% | Stable |
| NL | High (>92%) | 96,215 | 96,336 | +0.1% | Stable |
| AU | High (>92%) | 94,382 | 92,333 | -2.2% | Stable |
| BE | High (>92%) | 67,484 | 67,663 | +0.3% | Stable |
| SE | High (>92%) | 33,395 | 33,415 | +0.1% | Stable |
| DK | High (>92%) | 32,664 | 33,941 | +3.9% | Stable |
| NZ | Medium (>85%) | 19,911 | 19,142 | -3.9% | Stable |
| NO | High (>92%) | 18,035 | 19,419 | +7.7% | Stable |
| IE | Medium (>85%) | 17,994 | 17,220 | -4.3% | Stable |
| AT | High (>92%) | 11,911 | 10,883 | -8.6% | Stable |
| LU | High (>92%) | 2,539 | 3,258 | +28.3% | Stable |
| CH | Medium (>85%) | 2,142 | 2,094 | -2.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| CH | ↑ +2.55% | twint -100.0% | → Stable | Insufficient Funds -1.51pp | twint + Insufficient |

---

*Report: 2026-06-09*
