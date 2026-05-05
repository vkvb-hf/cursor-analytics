# Reactivation Investigation: US-HF 2026-W18

**Metric:** Reactivation Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 89.71% → 90.64% (+1.04%)  
**Volume:** 13,634 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Reactivation Rate improved from 89.71% to 90.64% (+1.04 pp) in W18, representing a significant positive change on 13,634 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (88.98%-91.26%) | +1.04 pp | ✅ |
| L1: Country Breakdown | No countries exceeding ±2.5% threshold | +1.04 pp (US only) | ✅ |
| L1: Dimension Scan | "Others" payment method flagged (-100 pp) | Negligible (1 order) | ✅ |
| Mix Shift Analysis | US Medium tier volume decreased 9.5% | Stable impact | ✅ |

**Key Findings:**
- The +1.04 pp improvement reverses three consecutive weeks of decline (W15-W17) and brings the rate closer to the 8-week high of 91.26% (W12)
- PayPal showed the strongest improvement at +1.80 pp (93.44%), followed by Credit Card at +1.22 pp (90.87%)
- Apple Pay slightly declined by -0.32 pp but remains within normal range at 86.86%
- Order volume decreased by 9.5% (15,063 → 13,634), continuing a downward trend from W16's peak of 18,897
- The flagged "Others" payment method change (-100 pp) is statistically insignificant with only 1 order

**Action:** Monitor — The improvement is positive and no dimensions exceed investigation thresholds. Continue tracking to confirm the upward trend stabilizes.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W18 | 90.64% | 13,634 | +1.04% ← REPORTED CHANGE |
| 2026-W17 | 89.71% | 15,063 | -0.40% |
| 2026-W16 | 90.07% | 18,897 | -0.44% |
| 2026-W15 | 90.47% | 21,155 | -0.57% |
| 2026-W14 | 90.99% | 14,736 | +0.40% |
| 2026-W13 | 90.63% | 15,928 | -0.69% |
| 2026-W12 | 91.26% | 15,787 | +2.56% |
| 2026-W11 | 88.98% | 17,703 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 90.64% | 89.71% | +1.04% | 13,634 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 0.0% | 100.0% | -100.00% | 1 | ⚠️ |
| Apple Pay | 86.86% | 87.14% | -0.32% | 2,138 |  |
| Credit Card | 90.87% | 89.77% | +1.22% | 9,316 |  |
| Paypal | 93.44% | 91.79% | +1.80% | 2,179 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 15,063 | 13,634 | -9.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-05*
