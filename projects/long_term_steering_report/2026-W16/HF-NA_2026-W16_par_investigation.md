# PAR Investigation: HF-NA 2026-W16

**Metric:** Payment Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 94.1% → 94.13% (+0.03%)  
**Volume:** 513,372 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate for HF-NA showed minimal improvement from 94.1% to 94.13% (+0.03pp) in W16, continuing a steady 8-week upward trend from 93.36% in W09, with the change deemed not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.26pp | ⚠️ |
| 2_PreDunningAR | Recovery | -0.12pp | ⚠️ |
| 3_PostDunningAR | Recovery | -0.20pp | ⚠️ |
| 6_PaymentApprovalRate | Final | +0.04pp | ✅ |

**Key Findings:**
- Upstream funnel metrics declined (FirstRunAR -0.26pp, PreDunningAR -0.12pp, PostDunningAR -0.20pp) while final PAR slightly improved, indicating effective downstream recovery mechanisms
- US drove the positive movement (+0.06pp to 94.59%) while CA experienced a minor decline (-0.09pp to 95.76%)
- Apple Pay showed the strongest improvement among payment methods (+0.35pp to 89.07%), though it remains the lowest-performing method
- ProcessOut improved notably (+0.49pp to 92.81%) while Adyen declined slightly (-0.09pp to 95.67%)
- No countries or dimensions exceeded the ±2.5% threshold requiring deep-dive investigation

**Action:** Monitor — The change is not significant and all metrics remain within normal operating ranges. Continue tracking upstream funnel softness in FirstRunAR and PostDunningAR.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 94.13% | 513,372 | +0.03% ← REPORTED CHANGE |
| 2026-W15 | 94.1% | 497,775 | +0.12% |
| 2026-W14 | 93.99% | 507,189 | +0.03% |
| 2026-W13 | 93.96% | 517,599 | +0.10% |
| 2026-W12 | 93.87% | 526,516 | -0.04% |
| 2026-W11 | 93.91% | 539,763 | +0.29% |
| 2026-W10 | 93.64% | 554,777 | +0.30% |
| 2026-W09 | 93.36% | 553,112 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 95.76% | 95.85% | -0.09% | 104,640 |  |
| US | 94.59% | 94.54% | +0.06% | 511,272 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 94.61% | 94.64% | -0.04% | 377,622 |  |
| Others | 98.6% | 98.53% | +0.07% | 4,346 |  |
| Paypal | 96.52% | 96.33% | +0.19% | 62,665 |  |
| Apple Pay | 89.07% | 88.76% | +0.35% | 68,739 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 91.63% | 92.24% | -0.66% | 669 |  |
| Adyen | 95.67% | 95.76% | -0.09% | 24,945 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 3,642 |  |
| Braintree | 94.33% | 94.32% | +0.01% | 383,333 |  |
| ProcessOut | 92.81% | 92.36% | +0.49% | 100,783 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.06% | 91.29% | -0.26% | 513,372 | 497,775 |  |
| 2_PreDunningAR | 92.31% | 92.42% | -0.12% | 513,372 | 497,775 |  |
| 3_PostDunningAR | 93.31% | 93.5% | -0.20% | 513,372 | 497,775 |  |
| 6_PaymentApprovalRate | 94.13% | 94.1% | +0.04% | 513,372 | 497,775 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 492,811 | 511,272 | +3.7% | Stable |
| CA | High (>92%) | 103,253 | 104,640 | +1.3% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
