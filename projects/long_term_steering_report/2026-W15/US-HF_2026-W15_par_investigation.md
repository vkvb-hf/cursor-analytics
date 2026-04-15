# PAR Investigation: US-HF 2026-W15

**Metric:** Payment Approval Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 93.63% → 93.76% (+0.14%)  
**Volume:** 408,629 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate improved slightly from 93.63% to 93.76% (+0.13pp) in W15, continuing a steady 8-week upward trend from 93.13% in W08, with the change classified as not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | +0.44pp | ✅ |
| 2_PreDunningAR | Pre-Dunning | +0.32pp | ✅ |
| 3_PostDunningAR | Post-Dunning | +0.02pp | ✅ |
| 6_PaymentApprovalRate | Final PAR | +0.14pp | ✅ |

**Key Findings:**
- All funnel stages showed positive week-over-week improvement, with FirstRunAR contributing the largest gain (+0.44pp)
- PaymentProvider "Unknown" flagged with -3.36pp decline (95.56% → 92.35%), though volume is minimal (353 orders, <0.1% of total)
- US showed healthy improvement of +0.34pp (92.78% → 93.09%) with no countries exceeding the ±2.5% threshold
- Consistent 8-week positive trend observed: PAR increased +0.63pp total from W08 (93.13%) to W15 (93.76%)
- Volume decline continues (-1.7% WoW), but mix shift analysis shows high-tier AR volume remains stable

**Action:** Monitor — The metric shows healthy, stable improvement with no significant anomalies requiring investigation. Continue standard weekly monitoring.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 93.76% | 408,629 | +0.14% ← REPORTED CHANGE |
| 2026-W14 | 93.63% | 415,885 | +0.05% |
| 2026-W13 | 93.58% | 424,103 | +0.03% |
| 2026-W12 | 93.55% | 433,761 | -0.04% |
| 2026-W11 | 93.59% | 444,619 | +0.22% |
| 2026-W10 | 93.38% | 457,610 | +0.24% |
| 2026-W09 | 93.16% | 455,121 | +0.03% |
| 2026-W08 | 93.13% | 453,781 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 93.09% | 92.78% | +0.34% | 492,811 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 98.66% | 99.36% | -0.70% | 2,397 |  |
| Credit Card | 94.44% | 94.36% | +0.09% | 300,596 |  |
| Paypal | 96.25% | 96.05% | +0.21% | 50,099 |  |
| Apple Pay | 87.63% | 87.38% | +0.29% | 55,537 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 92.35% | 95.56% | -3.36% | 353 | ⚠️ |
| Adyen | 96.34% | 96.43% | -0.09% | 383 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 2,010 |  |
| Braintree | 94.24% | 94.1% | +0.15% | 363,785 |  |
| ProcessOut | 89.26% | 89.0% | +0.29% | 42,098 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.07% | 90.67% | +0.44% | 408,629 | 415,885 |  |
| 2_PreDunningAR | 92.22% | 91.93% | +0.32% | 408,629 | 415,885 |  |
| 3_PostDunningAR | 93.0% | 92.98% | +0.02% | 408,629 | 415,885 |  |
| 6_PaymentApprovalRate | 93.76% | 93.63% | +0.14% | 408,629 | 415,885 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 497,052 | 492,811 | -0.9% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-15*
