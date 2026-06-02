# PAR Investigation: HF-INTL 2026-W22

**Metric:** Payment Approval Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 97.57% → 97.45% (-0.12%)  
**Volume:** 701,486 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate for HF-INTL declined marginally from 97.57% to 97.45% (-0.12pp) in 2026-W22, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | First attempt success | -0.59pp | ⚠️ |
| 2_PreDunningAR | Pre-dunning recovery | -0.48pp | ⚠️ |
| 3_PostDunningAR | Post-dunning recovery | -0.38pp | ⚠️ |
| 6_PaymentApprovalRate | Final approval | -0.12pp | ✅ |

**Key Findings:**
- The -0.12pp decline in PAR is within normal fluctuation and marked as not significant; the 8-week trend shows rates oscillating between 97.26% and 97.57%
- Upstream funnel metrics show larger declines: FirstRunAR dropped -0.59pp (92.94% → 92.4%), indicating the initial payment attempt success rate weakened more than the final approval rate
- AT showed the largest country-level decline at -0.58pp (98.32% → 97.74%), though no country exceeded the ±2.5% threshold requiring deep-dive
- Apple Pay had the steepest payment method decline at -0.29pp (93.91% → 93.64%), while maintaining the lowest approval rate among methods
- Volume decreased -6.3% WoW (748,329 → 701,486 orders); mix shift analysis shows all countries remained stable with no material impact on rates

**Action:** Monitor — Continue standard tracking. The decline is not significant and no dimension exceeded investigation thresholds. Watch FirstRunAR trend as the -0.59pp drop is larger than downstream metrics.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W22 | 97.45% | 701,486 | -0.12% ← REPORTED CHANGE |
| 2026-W21 | 97.57% | 748,329 | +0.04% |
| 2026-W20 | 97.53% | 747,471 | +0.26% |
| 2026-W19 | 97.28% | 789,069 | - |
| 2026-W18 | 97.28% | 780,744 | -0.14% |
| 2026-W17 | 97.42% | 794,597 | +0.03% |
| 2026-W16 | 97.39% | 804,152 | +0.13% |
| 2026-W15 | 97.26% | 744,637 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| AT | 97.74% | 98.32% | -0.58% | 11,910 |  |
| LU | 98.74% | 99.01% | -0.28% | 2,538 |  |
| DK | 98.70% | 98.95% | -0.26% | 32,657 |  |
| GB | 96.59% | 96.83% | -0.25% | 177,783 |  |
| BE | 98.96% | 99.16% | -0.20% | 67,481 |  |
| DE | 98.73% | 98.91% | -0.19% | 182,115 |  |
| AU | 96.41% | 96.27% | +0.14% | 94,369 |  |
| NZ | 94.99% | 94.73% | +0.28% | 19,909 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 93.64% | 93.91% | -0.29% | 92,061 |  |
| Paypal | 98.97% | 99.08% | -0.11% | 171,045 |  |
| Others | 99.46% | 99.57% | -0.11% | 114,929 |  |
| Credit Card | 97.02% | 97.11% | -0.09% | 323,451 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | 96.27% | 96.44% | -0.18% | 199,428 |  |
| Braintree | 97.37% | 97.52% | -0.15% | 257,549 |  |
| Adyen | 98.52% | 98.59% | -0.07% | 238,662 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 4,251 |  |
| Unknown | 90.35% | 89.44% | +1.02% | 1,596 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 92.4% | 92.94% | -0.59% | 701,486 | 748,329 |  |
| 2_PreDunningAR | 94.48% | 94.94% | -0.48% | 701,486 | 748,329 |  |
| 3_PostDunningAR | 96.6% | 96.97% | -0.38% | 701,486 | 748,329 |  |
| 6_PaymentApprovalRate | 97.45% | 97.57% | -0.12% | 701,486 | 748,329 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| DE | High (>92%) | 204,608 | 182,115 | -11.0% | Stable |
| GB | High (>92%) | 194,230 | 177,783 | -8.5% | Stable |
| FR | High (>92%) | 134,066 | 128,778 | -3.9% | Stable |
| NL | High (>92%) | 99,062 | 96,213 | -2.9% | Stable |
| AU | High (>92%) | 95,841 | 94,369 | -1.5% | Stable |
| BE | High (>92%) | 67,838 | 67,481 | -0.5% | Stable |
| DK | High (>92%) | 35,110 | 32,657 | -7.0% | Stable |
| SE | High (>92%) | 34,022 | 33,392 | -1.9% | Stable |
| NO | High (>92%) | 20,266 | 18,033 | -11.0% | Stable |
| NZ | High (>92%) | 19,034 | 19,909 | +4.6% | Stable |
| IE | High (>92%) | 18,635 | 17,988 | -3.5% | Stable |
| AT | High (>92%) | 12,530 | 11,910 | -4.9% | Stable |
| LU | High (>92%) | 3,142 | 2,538 | -19.2% | Stable |
| CH | High (>92%) | 2,147 | 2,142 | -0.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-02*
