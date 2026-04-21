# PAR Investigation: US-HF 2026-W16

**Metric:** Payment Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 93.76% → 93.82% (+0.06%)  
**Volume:** 421,947 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate showed a marginal improvement from 93.76% to 93.82% (+0.06 pp) in US-HF for W16, a change that is not statistically significant and continues a stable upward trend observed over the past 8 weeks.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.31 pp | ⚠️ |
| 2_PreDunningAR | Recovery | -0.13 pp | ⚠️ |
| 3_PostDunningAR | Dunning | -0.17 pp | ⚠️ |
| 6_PaymentApprovalRate | Final | +0.07 pp | ✅ |

**Key Findings:**
- The +0.06 pp increase in PAR continues a consistent upward trend, with the rate climbing from 93.16% (W09) to 93.82% (W16) over 8 weeks
- All upstream funnel metrics (FirstRunAR, PreDunningAR, PostDunningAR) showed slight declines (-0.31 pp, -0.13 pp, -0.17 pp respectively), yet PAR still improved
- PaymentProvider "Unknown" flagged with a -6.05 pp decline (86.73% from 92.31%), though volume is minimal (226 orders)
- ProcessOut showed notable improvement at +1.88 pp (90.93% from 89.25%) with meaningful volume (57,911 orders)
- No countries exceeded the ±2.5% threshold; US showed a minor decline of -0.13 pp

**Action:** Monitor — No significant changes detected. Continue standard weekly tracking; no investigation required.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 93.82% | 421,947 | +0.06% ← REPORTED CHANGE |
| 2026-W15 | 93.76% | 408,629 | +0.14% |
| 2026-W14 | 93.63% | 415,885 | +0.05% |
| 2026-W13 | 93.58% | 424,103 | +0.03% |
| 2026-W12 | 93.55% | 433,761 | -0.03% |
| 2026-W11 | 93.58% | 444,619 | +0.21% |
| 2026-W10 | 93.38% | 457,610 | +0.24% |
| 2026-W09 | 93.16% | 455,121 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.97% | 93.09% | -0.13% | 511,272 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 98.47% | 98.66% | -0.20% | 2,284 |  |
| Credit Card | 94.42% | 94.43% | -0.02% | 310,172 |  |
| Paypal | 96.49% | 96.25% | +0.25% | 51,881 |  |
| Apple Pay | 88.05% | 87.63% | +0.48% | 57,610 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 86.73% | 92.31% | -6.05% | 226 | ⚠️ |
| Adyen | 96.03% | 96.34% | -0.33% | 403 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 2,028 |  |
| Braintree | 94.26% | 94.24% | +0.02% | 361,379 |  |
| ProcessOut | 90.93% | 89.25% | +1.88% | 57,911 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.79% | 91.07% | -0.31% | 421,947 | 408,629 |  |
| 2_PreDunningAR | 92.1% | 92.22% | -0.13% | 421,947 | 408,629 |  |
| 3_PostDunningAR | 93.03% | 93.19% | -0.17% | 421,947 | 408,629 |  |
| 6_PaymentApprovalRate | 93.82% | 93.76% | +0.07% | 421,947 | 408,629 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 492,811 | 511,272 | +3.7% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-21*
