# PAR Investigation: HF-NA 2026-W16

**Metric:** Payment Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 94.1% → 94.13% (+0.03%)  
**Volume:** 513,372 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate for HF-NA remained stable in W16, showing a marginal increase of +0.03pp (94.10% → 94.13%) on volume of 513,372 orders, which is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.26pp | ⚠️ |
| 2_PreDunningAR | Recovery | -0.12pp | ⚠️ |
| 3_PostDunningAR | Recovery | -0.20pp | ⚠️ |
| 6_PaymentApprovalRate | Final | +0.03pp | ✅ |

**Key Findings:**
- The 8-week trend shows consistent improvement from 93.36% (W09) to 94.13% (W16), representing a cumulative gain of +0.77pp over 7 weeks
- All upstream funnel metrics (FirstRunAR, PreDunningAR, PostDunningAR) declined week-over-week, yet final PAR still improved slightly, suggesting effective downstream recovery mechanisms
- No countries exceeded the ±2.5% threshold; US (+0.06pp) contributed positively while CA (-0.10pp) showed minor decline
- Apple Pay showed the largest positive movement among payment methods (+0.35pp), though it remains the lowest-performing method at 89.07%
- ProcessOut provider improved by +0.48pp (92.36% → 92.81%) on significant volume of 100,783 orders

**Action:** Monitor — No action required. The change is not significant and all metrics remain within normal operating ranges. Continue standard weekly monitoring.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 94.13% | 513,372 | +0.03% ← REPORTED CHANGE |
| 2026-W15 | 94.1% | 497,776 | +0.12% |
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
| CA | 95.75% | 95.84% | -0.10% | 104,640 |  |
| US | 94.59% | 94.54% | +0.06% | 511,272 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 94.61% | 94.64% | -0.04% | 377,623 |  |
| Others | 98.6% | 98.53% | +0.07% | 4,345 |  |
| Paypal | 96.52% | 96.33% | +0.19% | 62,665 |  |
| Apple Pay | 89.07% | 88.76% | +0.35% | 68,739 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 91.62% | 92.24% | -0.67% | 668 |  |
| Adyen | 95.67% | 95.76% | -0.09% | 24,945 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 3,642 |  |
| Braintree | 94.33% | 94.32% | +0.01% | 383,334 |  |
| ProcessOut | 92.81% | 92.36% | +0.48% | 100,783 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.06% | 91.29% | -0.26% | 513,372 | 497,776 |  |
| 2_PreDunningAR | 92.31% | 92.42% | -0.12% | 513,372 | 497,776 |  |
| 3_PostDunningAR | 93.32% | 93.51% | -0.20% | 513,372 | 497,776 |  |
| 6_PaymentApprovalRate | 94.13% | 94.1% | +0.03% | 513,372 | 497,776 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 492,812 | 511,272 | +3.7% | Stable |
| CA | High (>92%) | 103,253 | 104,640 | +1.3% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
