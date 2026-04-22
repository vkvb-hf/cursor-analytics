# PAR Investigation: HF-NA 2026-W15

**Metric:** Payment Approval Rate  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 94.1% → 94.13% (+0.03%)  
**Volume:** 513,372 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate for HF-NA remained stable at 94.13% in W16, representing a marginal +0.03pp increase from 94.1% in W15, which is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | +0.38pp | ✅ |
| 2_PreDunningAR | vs FirstRun | +0.28pp | ✅ |
| 3_PostDunningAR | vs PreDunning | -0.01pp | ✅ |
| 6_PaymentApprovalRate | Final | +0.11pp | ✅ |

**Key Findings:**
- PAR shows a consistent upward trend over 8 weeks, rising from 93.36% (W09) to 94.13% (W16), a cumulative gain of +0.77pp
- US drove the weekly improvement with +0.17pp gain (94.38% → 94.54%), while CA remained flat at -0.01pp
- PaymentProvider "Unknown" flagged with -4.09pp decline (96.17% → 92.24%), though volume is minimal (773 orders, 0.15% of total)
- Apple Pay continues to underperform other payment methods at 88.76%, though improved +0.25pp WoW
- No countries exceeded the ±2.5% threshold requiring deep-dive investigation

**Action:** Monitor — The metric change is not significant and all funnel steps show healthy performance. Continue standard monitoring cadence.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 94.13% | 513,372 | +0.03% |
| 2026-W15 | 94.1% | 497,775 | +0.12% ← REPORTED CHANGE |
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
| CA | 95.85% | 95.86% | -0.01% | 103,253 |  |
| US | 94.54% | 94.38% | +0.17% | 492,811 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 98.53% | 99.27% | -0.75% | 4,410 |  |
| Credit Card | 94.64% | 94.57% | +0.08% | 366,511 |  |
| Paypal | 96.33% | 96.19% | +0.15% | 60,610 |  |
| Apple Pay | 88.76% | 88.53% | +0.25% | 66,244 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 92.24% | 96.17% | -4.09% | 773 | ⚠️ |
| Adyen | 95.76% | 95.86% | -0.10% | 24,575 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 3,578 |  |
| ProcessOut | 92.36% | 92.24% | +0.13% | 83,802 |  |
| Braintree | 94.32% | 94.19% | +0.14% | 385,047 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.29% | 90.95% | +0.38% | 497,775 | 507,189 |  |
| 2_PreDunningAR | 92.42% | 92.16% | +0.28% | 497,775 | 507,189 |  |
| 3_PostDunningAR | 93.5% | 93.51% | -0.01% | 497,775 | 507,189 |  |
| 6_PaymentApprovalRate | 94.1% | 93.99% | +0.11% | 497,775 | 507,189 |  |

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

*Report: 2026-04-22*
