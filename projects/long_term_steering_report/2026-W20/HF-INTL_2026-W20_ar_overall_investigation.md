# AR Overall Investigation: HF-INTL 2026-W20

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 94.61% → 95.08% (+0.50%)  
**Volume:** 747,471 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate for HF-INTL improved from 94.61% to 95.08% (+0.50pp) in 2026-W20, representing a statistically non-significant positive movement on 747,471 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | +0.76pp | ✅ |
| 2_PreDunningAR | Reported Metric | +0.50pp | ✅ |
| 3_PostDunningAR | Downstream | +0.02pp | ✅ |
| 6_PaymentApprovalRate | End Conversion | +0.28pp | ✅ |

**Key Findings:**
- All funnel metrics showed positive movement, with FirstRunAR leading improvement at +0.76pp (92.56% → 93.26%)
- No countries exceeded the ±2.5% investigation threshold; NO showed the largest decline at -2.34pp (91.78% → 89.64%) but remained within tolerance
- PaymentProvider "Unknown" flagged with +5.91pp change, but represents minimal volume (2,052 orders, <0.3% of total)
- Volume declined 5.3% week-over-week (789,069 → 747,471), with notable decreases in DE (-13.1%), DK (-12.8%), and CH (-14.6%)
- All payment methods improved uniformly, with changes ranging from +0.14pp to +0.77pp

**Action:** Monitor — The improvement is not statistically significant and all dimensions show stable, aligned movement. No investigation required.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W20 | 95.08% | 747,471 | +0.50% ← REPORTED CHANGE |
| 2026-W19 | 94.61% | 789,069 | +0.75% |
| 2026-W18 | 93.91% | 780,744 | -0.73% |
| 2026-W17 | 94.6% | 794,597 | -0.20% |
| 2026-W16 | 94.79% | 804,152 | +0.07% |
| 2026-W15 | 94.72% | 744,637 | +1.19% |
| 2026-W14 | 93.61% | 784,406 | -0.55% |
| 2026-W13 | 94.13% | 842,481 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| NO | 89.64% | 91.78% | -2.34% | 20,600 |  |
| AU | 91.91% | 91.30% | +0.66% | 96,578 |  |
| BE | 96.46% | 95.23% | +1.29% | 65,230 |  |
| DK | 97.86% | 96.42% | +1.50% | 33,798 |  |
| FR | 94.79% | 93.10% | +1.81% | 129,260 |  |
| AT | 96.35% | 94.33% | +2.13% | 12,230 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 99.2% | 99.07% | +0.14% | 118,316 |  |
| Paypal | 97.89% | 97.56% | +0.34% | 185,797 |  |
| Credit Card | 93.51% | 92.88% | +0.68% | 341,711 |  |
| Apple Pay | 90.47% | 89.78% | +0.77% | 101,647 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 4,902 |  |
| Adyen | 96.21% | 95.81% | +0.41% | 245,085 |  |
| Braintree | 95.56% | 95.17% | +0.42% | 281,912 |  |
| ProcessOut | 93.1% | 92.47% | +0.68% | 213,520 |  |
| Unknown | 90.69% | 85.63% | +5.91% | 2,052 | ⚠️ |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 93.26% | 92.56% | +0.76% | 747,471 | 789,069 |  |
| 2_PreDunningAR | 95.08% | 94.61% | +0.50% | 747,471 | 789,069 |  |
| 3_PostDunningAR | 96.7% | 96.68% | +0.02% | 747,471 | 789,069 |  |
| 6_PaymentApprovalRate | 97.56% | 97.28% | +0.28% | 747,471 | 789,069 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| DE | High (>92%) | 232,594 | 202,135 | -13.1% | Stable |
| GB | High (>92%) | 206,083 | 203,866 | -1.1% | Stable |
| FR | High (>92%) | 136,525 | 129,260 | -5.3% | Stable |
| NL | High (>92%) | 101,537 | 100,326 | -1.2% | Stable |
| AU | Medium (>85%) | 97,538 | 96,578 | -1.0% | Stable |
| BE | High (>92%) | 67,448 | 65,230 | -3.3% | Stable |
| DK | High (>92%) | 38,750 | 33,798 | -12.8% | Stable |
| SE | High (>92%) | 38,231 | 33,815 | -11.6% | Stable |
| NO | Medium (>85%) | 22,798 | 20,600 | -9.6% | Stable |
| NZ | Medium (>85%) | 19,676 | 19,681 | +0.0% | Stable |
| IE | Medium (>85%) | 18,498 | 18,470 | -0.2% | Stable |
| AT | High (>92%) | 13,976 | 12,230 | -12.5% | Stable |
| LU | High (>92%) | 3,509 | 3,327 | -5.2% | Stable |
| CH | High (>92%) | 2,395 | 2,045 | -14.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-19*
