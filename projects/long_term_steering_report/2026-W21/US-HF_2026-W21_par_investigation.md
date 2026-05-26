# PAR Investigation: US-HF 2026-W21

**Metric:** Payment Approval Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 93.5% → 93.23% (-0.29%)  
**Volume:** 386,911 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate declined by -0.29pp (93.5% → 93.23%) on 386,911 orders in US-HF for 2026-W21, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.31pp | ⚠️ |
| 2_PreDunningAR | Recovery | -0.34pp | ⚠️ |
| 3_PostDunningAR | Recovery | -0.45pp | ⚠️ |
| 6_PaymentApprovalRate | Final | -0.28pp | ⚠️ |

**Key Findings:**
- All funnel stages show modest declines (-0.28pp to -0.45pp), with PostDunningAR showing the largest drop at -0.45pp
- No countries exceeded the ±2.5% threshold for deep-dive investigation; US declined only -0.19pp
- "Others" payment method showed the largest decline at -1.41pp (93.84% → 92.51%), though volume is minimal (2,204 orders)
- "Unknown" payment provider flagged with +6.22pp increase, but represents negligible volume (335 orders) and low baseline rate (52.24%)
- 8-week trend shows gradual decline from 93.82% (W16) to 93.23% (W21), representing a -0.59pp cumulative decrease over 6 weeks

**Action:** Monitor — The decline is not statistically significant, no dimensional breakdowns exceeded thresholds, and the week-over-week change falls within normal variance observed in the 8-week trend.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W21 | 93.23% | 386,911 | -0.29% ← REPORTED CHANGE |
| 2026-W20 | 93.5% | 401,763 | +0.18% |
| 2026-W19 | 93.33% | 416,723 | -0.30% |
| 2026-W18 | 93.61% | 414,920 | -0.19% |
| 2026-W17 | 93.79% | 419,106 | -0.03% |
| 2026-W16 | 93.82% | 421,948 | +0.07% |
| 2026-W15 | 93.75% | 408,631 | +0.14% |
| 2026-W14 | 93.62% | 415,886 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 94.25% | 94.43% | -0.19% | 478,645 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 92.51% | 93.84% | -1.41% | 2,204 |  |
| Apple Pay | 87.13% | 87.86% | -0.83% | 52,341 |  |
| Credit Card | 93.84% | 94.03% | -0.20% | 285,517 |  |
| Paypal | 96.35% | 96.54% | -0.19% | 46,849 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | 89.27% | 89.61% | -0.38% | 58,388 |  |
| Adyen | 94.98% | 95.22% | -0.25% | 458 |  |
| Braintree | 93.95% | 94.17% | -0.24% | 325,970 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 1,760 |  |
| Unknown | 52.24% | 49.18% | +6.22% | 335 | ⚠️ |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.37% | 90.66% | -0.31% | 386,911 | 401,763 |  |
| 2_PreDunningAR | 91.58% | 91.89% | -0.34% | 386,911 | 401,763 |  |
| 3_PostDunningAR | 92.46% | 92.87% | -0.45% | 386,911 | 401,763 |  |
| 6_PaymentApprovalRate | 93.23% | 93.5% | -0.28% | 386,911 | 401,763 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 493,780 | 478,645 | -3.1% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-26*
