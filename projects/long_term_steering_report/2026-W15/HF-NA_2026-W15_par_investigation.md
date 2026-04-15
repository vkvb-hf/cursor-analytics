# PAR Investigation: HF-NA 2026-W15

**Metric:** Payment Approval Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 94.0% → 94.1% (+0.11%)  
**Volume:** 497,775 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate showed a marginal improvement from 94.0% to 94.1% (+0.11pp) on 497,775 orders, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within normal range | +0.38pp | ✅ |
| 2_PreDunningAR | Within normal range | +0.28pp | ✅ |
| 3_PostDunningAR | Within normal range | -0.04pp | ✅ |
| 6_PaymentApprovalRate | Within normal range | +0.11pp | ✅ |

**Key Findings:**
- The 8-week trend shows consistent gradual improvement from 93.27% (W08) to 94.1% (W15), indicating a healthy upward trajectory of +0.83pp over the period
- US drove the week-over-week improvement with +0.34pp gain (92.78% → 93.09%) on 492,811 orders, while CA remained stable at +0.02pp
- PaymentProvider "Unknown" flagged with -4.07pp decline (96.17% → 92.26%), but volume is minimal at only 775 orders (0.16% of total)
- All funnel stages showed positive or neutral movement, with FirstRunAR contributing the largest improvement (+0.38pp)
- No countries exceeded the ±2.5% threshold requiring deep-dive investigation

**Action:** Monitor – The metric change is not significant, all dimensions are within acceptable thresholds, and the 8-week trend demonstrates stable improvement. Continue standard monitoring cadence.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 94.1% | 497,775 | +0.11% ← REPORTED CHANGE |
| 2026-W14 | 94.0% | 507,189 | +0.04% |
| 2026-W13 | 93.96% | 517,599 | +0.10% |
| 2026-W12 | 93.87% | 526,516 | -0.04% |
| 2026-W11 | 93.91% | 539,763 | +0.29% |
| 2026-W10 | 93.64% | 554,777 | +0.30% |
| 2026-W09 | 93.36% | 553,112 | +0.10% |
| 2026-W08 | 93.27% | 548,921 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 93.51% | 93.49% | +0.02% | 103,253 |  |
| US | 93.09% | 92.78% | +0.34% | 492,811 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 98.53% | 99.27% | -0.75% | 4,412 |  |
| Credit Card | 94.65% | 94.57% | +0.08% | 366,509 |  |
| Paypal | 96.33% | 96.19% | +0.15% | 60,610 |  |
| Apple Pay | 88.76% | 88.54% | +0.25% | 66,244 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 92.26% | 96.17% | -4.07% | 775 | ⚠️ |
| Adyen | 95.76% | 95.86% | -0.10% | 24,575 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 3,578 |  |
| ProcessOut | 92.37% | 92.24% | +0.14% | 83,802 |  |
| Braintree | 94.32% | 94.19% | +0.14% | 385,045 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.29% | 90.95% | +0.38% | 497,775 | 507,189 |  |
| 2_PreDunningAR | 92.42% | 92.17% | +0.28% | 497,775 | 507,189 |  |
| 3_PostDunningAR | 93.29% | 93.33% | -0.04% | 497,775 | 507,189 |  |
| 6_PaymentApprovalRate | 94.1% | 94.0% | +0.11% | 497,775 | 507,189 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 497,052 | 492,811 | -0.9% | Stable |
| CA | High (>92%) | 105,530 | 103,253 | -2.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-15*
