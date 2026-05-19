# PAR Investigation: HF-INTL 2026-W20

**Metric:** Payment Approval Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 97.28% → 97.56% (+0.29%)  
**Volume:** 747,471 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate for HF-INTL improved modestly from 97.28% to 97.56% (+0.29pp) in W20, a statistically non-significant change within normal weekly fluctuation patterns.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within range | +0.76pp | ✅ |
| 2_PreDunningAR | Within range | +0.50pp | ✅ |
| 3_PostDunningAR | Within range | +0.02pp | ✅ |
| 6_PaymentApprovalRate | Within range | +0.28pp | ✅ |

**Key Findings:**
- All funnel stages showed positive movement, with FirstRunAR driving the largest improvement (+0.76pp from 92.56% to 93.26%)
- No countries exceeded the ±2.5% threshold; CH showed the largest country-level improvement (+1.19pp) but on low volume (2,045 orders)
- PaymentProvider "Unknown" flagged with +7.51pp change (86.22% → 92.69%), though volume is minimal (2,052 orders)
- Volume declined 5.3% WoW (789,069 → 747,471 orders), with notable decreases in DE (-13.1%), CH (-14.6%), and AT (-12.5%)
- All payment methods showed slight improvements, with Apple Pay gaining +0.58pp and Credit Card +0.38pp

**Action:** Monitor — The improvement is not statistically significant and falls within normal operating range. No root cause investigation required.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W20 | 97.56% | 747,471 | +0.29% ← REPORTED CHANGE |
| 2026-W19 | 97.28% | 789,069 | -0.01% |
| 2026-W18 | 97.29% | 780,744 | -0.13% |
| 2026-W17 | 97.42% | 794,597 | +0.03% |
| 2026-W16 | 97.39% | 804,152 | +0.13% |
| 2026-W15 | 97.26% | 744,637 | +0.24% |
| 2026-W14 | 97.03% | 784,406 | -0.13% |
| 2026-W13 | 97.16% | 842,481 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| BE | 99.07% | 98.87% | +0.20% | 65,230 |  |
| GB | 96.90% | 96.69% | +0.21% | 203,866 |  |
| AU | 96.36% | 95.79% | +0.59% | 96,578 |  |
| AT | 98.35% | 97.57% | +0.80% | 12,230 |  |
| FR | 97.27% | 96.48% | +0.81% | 129,260 |  |
| CH | 97.26% | 96.12% | +1.19% | 2,045 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 99.03% | 98.93% | +0.11% | 185,797 |  |
| Others | 99.63% | 99.52% | +0.12% | 118,316 |  |
| Credit Card | 97.07% | 96.71% | +0.38% | 341,711 |  |
| Apple Pay | 94.06% | 93.52% | +0.58% | 101,647 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 4,902 |  |
| Adyen | 98.63% | 98.44% | +0.19% | 245,085 |  |
| Braintree | 97.51% | 97.31% | +0.21% | 281,912 |  |
| ProcessOut | 96.37% | 95.95% | +0.44% | 213,520 |  |
| Unknown | 92.69% | 86.22% | +7.51% | 2,052 | ⚠️ |

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
| AU | High (>92%) | 97,538 | 96,578 | -1.0% | Stable |
| BE | High (>92%) | 67,448 | 65,230 | -3.3% | Stable |
| DK | High (>92%) | 38,750 | 33,798 | -12.8% | Stable |
| SE | High (>92%) | 38,231 | 33,815 | -11.6% | Stable |
| NO | High (>92%) | 22,798 | 20,600 | -9.6% | Stable |
| NZ | High (>92%) | 19,676 | 19,681 | +0.0% | Stable |
| IE | High (>92%) | 18,498 | 18,470 | -0.2% | Stable |
| AT | High (>92%) | 13,976 | 12,230 | -12.5% | Stable |
| LU | High (>92%) | 3,509 | 3,327 | -5.2% | Stable |
| CH | High (>92%) | 2,395 | 2,045 | -14.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-19*
