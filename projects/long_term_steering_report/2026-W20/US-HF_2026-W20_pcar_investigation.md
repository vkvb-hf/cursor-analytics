# PCAR Investigation: US-HF 2026-W20

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 89.61% → 89.15% (-0.51%)  
**Volume:** 15,543 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate for US-HF declined from 89.61% to 89.15% (-0.46 pp) in 2026-W20, representing a statistically non-significant change on 15,543 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Sustained decline pattern | -3.42 pp since W13 | ⚠️ |
| L1: Country Breakdown | No country exceeded ±2.5% threshold | -0.51% (US) | ✅ |
| L1: PaymentMethod | Others flagged but low volume | +16.37% (40 orders) | ✅ |
| L1: PaymentProvider | No data available | N/A | ✅ |
| Mix Shift | Volume stable in Medium tier | -4.8% volume shift | ✅ |

**Key Findings:**
- The 8-week trend shows a consistent downward trajectory from 92.57% (W13) to 89.15% (W20), a cumulative decline of 3.42 pp
- The week-over-week change of -0.51% is not statistically significant and no individual dimension breached investigation thresholds
- Credit Card payment method shows the largest absolute volume (8,694 orders) with a -0.86% decline, contributing most to the overall metric movement
- The "Others" payment method flagged with +16.37% change but represents only 40 orders (0.26% of volume), making it non-material
- Order volume decreased 4.8% week-over-week (16,327 → 15,543), remaining in the Medium approval rate tier

**Action:** Monitor — The weekly change is not significant and no dimensions exceeded thresholds; however, the sustained 8-week declining trend warrants continued observation. If the rate drops below 89% or the decline accelerates, escalate for deeper investigation into Credit Card approval patterns.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W20 | 89.15% | 15,543 | -0.51% ← REPORTED CHANGE |
| 2026-W19 | 89.61% | 16,327 | -1.67% |
| 2026-W18 | 91.13% | 16,396 | -1.66% |
| 2026-W17 | 92.67% | 15,496 | -0.09% |
| 2026-W16 | 92.75% | 18,142 | -0.29% |
| 2026-W15 | 93.02% | 17,670 | +0.18% |
| 2026-W14 | 92.85% | 14,911 | +0.30% |
| 2026-W13 | 92.57% | 15,361 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 89.15% | 89.61% | -0.51% | 15,543 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Paypal | 90.32% | 91.2% | -0.97% | 1,322 |  |
| Credit Card | 88.19% | 88.95% | -0.86% | 8,694 |  |
| Apple Pay | 90.32% | 90.34% | -0.02% | 5,487 |  |
| Others | 97.5% | 83.78% | +16.37% | 40 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 16,327 | 15,543 | -4.8% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-19*
