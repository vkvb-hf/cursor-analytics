# PAR Investigation: HF-INTL 2026-W19

**Metric:** Payment Approval Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 97.29% → 97.29% (+0.00%)  
**Volume:** 789,069 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate for HF-INTL remained completely flat at 97.29% week-over-week (W18 → W19), with no significant change observed across 789,069 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | First-run approval | +0.93pp | ✅ |
| 2_PreDunningAR | Pre-dunning recovery | +0.73pp | ✅ |
| 3_PostDunningAR | Post-dunning recovery | -0.18pp | ⚠️ |
| 6_PaymentApprovalRate | Final approval | +0.00pp | ✅ |

**Key Findings:**
- The PAR has been remarkably stable over the 8-week period, ranging narrowly between 97.03% and 97.42%
- PaymentProvider "Unknown" showed a -3.36pp decline (89.98% → 86.96%), though volume is minimal at 1,794 orders (0.2% of total)
- AU showed the largest country-level decline at -0.37pp (96.15% → 95.80%), while SE improved by +0.71pp (97.67% → 98.36%)
- Upstream funnel metrics improved: FirstRunAR gained +0.93pp and PreDunningAR gained +0.73pp, offsetting a slight -0.18pp decline in PostDunningAR
- No countries exceeded the ±2.5% threshold; all mix shifts remained stable with no material volume redistribution

**Action:** Monitor — No action required. The metric is stable and within normal operating range. Continue routine weekly monitoring.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W19 | 97.29% | 789,069 | - ← REPORTED CHANGE |
| 2026-W18 | 97.29% | 780,744 | -0.13% |
| 2026-W17 | 97.42% | 794,598 | +0.03% |
| 2026-W16 | 97.39% | 804,152 | +0.13% |
| 2026-W15 | 97.26% | 744,637 | +0.24% |
| 2026-W14 | 97.03% | 784,406 | -0.13% |
| 2026-W13 | 97.16% | 842,482 | -0.09% |
| 2026-W12 | 97.25% | 877,189 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| AU | 95.80% | 96.15% | -0.37% | 97,538 |  |
| GB | 96.70% | 96.74% | -0.05% | 206,083 |  |
| DK | 98.58% | 98.42% | +0.16% | 38,750 |  |
| IE | 95.13% | 94.93% | +0.21% | 18,498 |  |
| LU | 99.12% | 98.66% | +0.46% | 3,509 |  |
| SE | 98.36% | 97.67% | +0.71% | 38,231 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 96.72% | 96.77% | -0.06% | 357,518 |  |
| Paypal | 98.93% | 98.97% | -0.04% | 202,689 |  |
| Apple Pay | 93.53% | 93.52% | +0.01% | 107,022 |  |
| Others | 99.52% | 99.48% | +0.04% | 121,840 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 86.96% | 89.98% | -3.36% | 1,794 | ⚠️ |
| ProcessOut | 95.96% | 96.05% | -0.10% | 224,606 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 4,835 |  |
| Braintree | 97.32% | 97.3% | +0.02% | 303,987 |  |
| Adyen | 98.45% | 98.43% | +0.02% | 253,847 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 92.56% | 91.7% | +0.93% | 789,069 | 780,744 |  |
| 2_PreDunningAR | 94.62% | 93.93% | +0.73% | 789,069 | 780,744 |  |
| 3_PostDunningAR | 96.5% | 96.67% | -0.18% | 789,069 | 780,744 |  |
| 6_PaymentApprovalRate | 97.29% | 97.29% | +0.00% | 789,069 | 780,744 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| DE | High (>92%) | 225,472 | 232,594 | +3.2% | Stable |
| GB | High (>92%) | 210,813 | 206,083 | -2.2% | Stable |
| FR | High (>92%) | 134,603 | 136,525 | +1.4% | Stable |
| AU | High (>92%) | 95,241 | 97,538 | +2.4% | Stable |
| NL | High (>92%) | 91,532 | 101,537 | +10.9% | Stable |
| BE | High (>92%) | 67,404 | 67,448 | +0.1% | Stable |
| DK | High (>92%) | 39,006 | 38,750 | -0.7% | Stable |
| SE | High (>92%) | 37,916 | 38,231 | +0.8% | Stable |
| NO | High (>92%) | 22,944 | 22,798 | -0.6% | Stable |
| NZ | High (>92%) | 19,343 | 19,676 | +1.7% | Stable |
| IE | High (>92%) | 19,292 | 18,498 | -4.1% | Stable |
| AT | High (>92%) | 13,866 | 13,976 | +0.8% | Stable |
| LU | High (>92%) | 3,435 | 3,509 | +2.2% | Stable |
| CH | High (>92%) | 2,298 | 2,395 | +4.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-12*
