# PAR Investigation: HF-INTL 2026-W21

**Metric:** Payment Approval Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 97.53% → 97.57% (+0.04%)  
**Volume:** 748,329 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate for HF-INTL remained stable in 2026-W21, showing a marginal improvement of +0.04pp (97.53% → 97.57%) on 748,329 orders, which is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.34pp | ⚠️ |
| 2_PreDunningAR | Recovery | -0.14pp | ⚠️ |
| 3_PostDunningAR | Recovery | -0.28pp | ⚠️ |
| 6_PaymentApprovalRate | Final | +0.05pp | ✅ |

**Key Findings:**
- The 8-week trend shows consistent stability with PAR ranging from 97.03% to 97.57%, indicating healthy baseline performance
- NO showed the largest positive movement at +1.01pp (97.02% → 98.00%), while CH declined -0.73pp (97.26% → 96.55%) on low volume (2,147 orders)
- Upstream funnel metrics (FirstRunAR, PreDunningAR, PostDunningAR) all declined slightly (-0.14pp to -0.34pp), suggesting the PAR improvement came from recovery mechanisms
- Unknown PaymentProvider declined -2.17pp but represents minimal volume (1,627 orders)
- No countries exceeded the ±2.5% threshold requiring deep-dive investigation

**Action:** Monitor — No action required. The change is not significant and all dimensions remain within normal operating ranges.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W21 | 97.57% | 748,329 | +0.04% ← REPORTED CHANGE |
| 2026-W20 | 97.53% | 747,471 | +0.26% |
| 2026-W19 | 97.28% | 789,069 | - |
| 2026-W18 | 97.28% | 780,744 | -0.14% |
| 2026-W17 | 97.42% | 794,597 | +0.03% |
| 2026-W16 | 97.39% | 804,152 | +0.13% |
| 2026-W15 | 97.26% | 744,637 | +0.24% |
| 2026-W14 | 97.03% | 784,406 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CH | 96.55% | 97.26% | -0.73% | 2,147 |  |
| LU | 99.01% | 99.25% | -0.24% | 3,142 |  |
| SE | 98.07% | 98.25% | -0.19% | 34,022 |  |
| GB | 96.84% | 96.88% | -0.05% | 194,230 |  |
| FR | 97.26% | 97.20% | +0.06% | 134,066 |  |
| DE | 98.91% | 98.80% | +0.11% | 204,608 |  |
| NO | 98.00% | 97.02% | +1.01% | 20,266 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 93.91% | 94.02% | -0.11% | 99,888 |  |
| Others | 99.57% | 99.57% | +0.00% | 120,255 |  |
| Paypal | 99.08% | 99.03% | +0.06% | 186,439 |  |
| Credit Card | 97.12% | 97.05% | +0.07% | 341,747 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 89.49% | 91.47% | -2.17% | 1,627 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 4,676 |  |
| Adyen | 98.6% | 98.6% | +0.00% | 248,600 |  |
| Braintree | 97.53% | 97.5% | +0.03% | 280,895 |  |
| ProcessOut | 96.45% | 96.34% | +0.11% | 212,531 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 92.95% | 93.26% | -0.34% | 748,329 | 747,471 |  |
| 2_PreDunningAR | 94.94% | 95.08% | -0.14% | 748,329 | 747,471 |  |
| 3_PostDunningAR | 96.64% | 96.91% | -0.28% | 748,329 | 747,471 |  |
| 6_PaymentApprovalRate | 97.57% | 97.53% | +0.05% | 748,329 | 747,471 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | High (>92%) | 203,866 | 194,230 | -4.7% | Stable |
| DE | High (>92%) | 202,135 | 204,608 | +1.2% | Stable |
| FR | High (>92%) | 129,260 | 134,066 | +3.7% | Stable |
| NL | High (>92%) | 100,326 | 99,062 | -1.3% | Stable |
| AU | High (>92%) | 96,578 | 95,841 | -0.8% | Stable |
| BE | High (>92%) | 65,230 | 67,838 | +4.0% | Stable |
| SE | High (>92%) | 33,815 | 34,022 | +0.6% | Stable |
| DK | High (>92%) | 33,798 | 35,110 | +3.9% | Stable |
| NO | High (>92%) | 20,600 | 20,266 | -1.6% | Stable |
| NZ | High (>92%) | 19,681 | 19,034 | -3.3% | Stable |
| IE | High (>92%) | 18,470 | 18,635 | +0.9% | Stable |
| AT | High (>92%) | 12,230 | 12,530 | +2.5% | Stable |
| LU | High (>92%) | 3,327 | 3,142 | -5.6% | Stable |
| CH | High (>92%) | 2,045 | 2,147 | +5.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-26*
