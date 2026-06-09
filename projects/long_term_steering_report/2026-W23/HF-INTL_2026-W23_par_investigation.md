# PAR Investigation: HF-INTL 2026-W23

**Metric:** Payment Approval Rate  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 97.44% → 97.54% (+0.10%)  
**Volume:** 725,582 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate for HF-INTL improved marginally from 97.44% to 97.54% (+0.10pp) in 2026-W23, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.07pp | ✅ |
| 2_PreDunningAR | Recovery | +0.14pp | ✅ |
| 3_PostDunningAR | Dunning | -0.04pp | ✅ |
| 6_PaymentApprovalRate | Final | +0.10pp | ✅ |

**Key Findings:**
- The +0.10pp change is within normal weekly fluctuation; the 8-week trend shows rates oscillating between 97.28% and 97.57%, indicating stable performance
- No countries exceeded the ±2.5% threshold; NO showed the largest decline (-0.34pp) while GB and CH showed the largest gains (+0.42pp each)
- GB volume increased +10.5% WoW (177,802 → 196,495 orders) while maintaining rate improvement, contributing positively to overall performance
- All payment methods showed slight improvements, with Apple Pay gaining +0.35pp despite having the lowest baseline rate (93.96%)
- Unknown payment provider showed a -0.51pp decline but represents minimal volume (1,701 orders)

**Action:** Monitor — No investigation required. The change is not significant and all dimensions remain within normal operating ranges.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W23 | 97.54% | 725,582 | +0.10% ← REPORTED CHANGE |
| 2026-W22 | 97.44% | 701,558 | -0.13% |
| 2026-W21 | 97.57% | 748,425 | +0.05% |
| 2026-W20 | 97.52% | 747,579 | +0.25% |
| 2026-W19 | 97.28% | 789,195 | - |
| 2026-W18 | 97.28% | 780,887 | -0.14% |
| 2026-W17 | 97.42% | 794,762 | +0.03% |
| 2026-W16 | 97.39% | 804,346 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| NO | 97.64% | 97.97% | -0.34% | 19,419 |  |
| AU | 96.20% | 96.41% | -0.21% | 92,333 |  |
| FR | 97.15% | 97.22% | -0.07% | 135,257 |  |
| NL | 99.71% | 99.63% | +0.08% | 96,336 |  |
| LU | 98.96% | 98.70% | +0.26% | 3,258 |  |
| GB | 96.99% | 96.58% | +0.42% | 196,495 |  |
| CH | 97.09% | 96.69% | +0.42% | 2,094 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 99.01% | 98.97% | +0.05% | 174,598 |  |
| Others | 99.52% | 99.46% | +0.07% | 119,271 |  |
| Credit Card | 97.09% | 97.01% | +0.09% | 335,175 |  |
| Apple Pay | 93.96% | 93.63% | +0.35% | 96,538 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 89.77% | 90.23% | -0.51% | 1,701 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 5,331 |  |
| Adyen | 98.58% | 98.52% | +0.07% | 247,923 |  |
| ProcessOut | 96.36% | 96.26% | +0.10% | 204,980 |  |
| Braintree | 97.47% | 97.37% | +0.11% | 265,647 |  |

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
| NZ | High (>92%) | 19,911 | 19,142 | -3.9% | Stable |
| NO | High (>92%) | 18,035 | 19,419 | +7.7% | Stable |
| IE | High (>92%) | 17,994 | 17,220 | -4.3% | Stable |
| AT | High (>92%) | 11,911 | 10,883 | -8.6% | Stable |
| LU | High (>92%) | 2,539 | 3,258 | +28.3% | Stable |
| CH | High (>92%) | 2,142 | 2,094 | -2.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-09*
