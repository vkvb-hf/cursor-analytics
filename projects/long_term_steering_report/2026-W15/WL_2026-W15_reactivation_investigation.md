# Reactivation Investigation: WL 2026-W15

**Metric:** Reactivation Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 88.67% → 89.29% (+0.70%)  
**Volume:** 9,277 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Reactivation Rate improved from 88.67% to 89.29% (+0.62 pp) in WL 2026-W15, with volume increasing to 9,277 orders; however, this change is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Metric within normal range (85-89% band) | +0.62 pp | ✅ |
| L1: Country Breakdown | No country exceeded ±2.5% threshold | All <2.5% | ✅ |
| L1: PaymentMethod | "Others" dropped -66.67%, Apple Pay +3.99% | Mixed | ⚠️ |
| Mix Shift | Volume shifts stable across tiers | No significant impact | ✅ |

**Key Findings:**
- The +0.62 pp improvement continues an upward trend from the 85.07% low in W08 to 89.29% in W15, representing a +4.22 pp recovery over 8 weeks
- "Others" PaymentMethod showed a -66.67% change, but volume is negligible (only 3 orders) — not operationally meaningful
- Apple Pay improved +3.99 pp (72.06% → 74.94%) on 794 orders, flagged but still the lowest-performing payment method
- AO experienced the largest country-level improvement at +2.17 pp (85.21% → 87.06%) but did not exceed the ±2.5% threshold
- Volume decreased notably in MR (-6.3%), AO (-12.0%), and GN (-8.5%), but mix shift impact remains stable

**Action:** Monitor — No significant changes detected and no thresholds exceeded. Continue standard tracking; observe Apple Pay performance trend in coming weeks.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 89.29% | 9,277 | +0.70% ← REPORTED CHANGE |
| 2026-W14 | 88.67% | 7,706 | -0.05% |
| 2026-W13 | 88.71% | 7,954 | -0.49% |
| 2026-W12 | 89.15% | 7,658 | +1.89% |
| 2026-W11 | 87.5% | 9,145 | +1.91% |
| 2026-W10 | 85.86% | 9,675 | -0.12% |
| 2026-W09 | 85.96% | 7,581 | +1.05% |
| 2026-W08 | 85.07% | 8,046 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| GN | 93.32% | 92.33% | +1.07% | 13,110 |  |
| ER | 90.32% | 89.22% | +1.23% | 68,811 |  |
| MR | 81.41% | 80.25% | +1.45% | 19,468 |  |
| AO | 87.06% | 85.21% | +2.17% | 13,883 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 33.33% | 100.0% | -66.67% | 3 | ⚠️ |
| Credit Card | 89.92% | 89.58% | +0.38% | 6,638 |  |
| Paypal | 93.27% | 92.9% | +0.39% | 1,842 |  |
| Apple Pay | 74.94% | 72.06% | +3.99% | 794 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 67,730 | 68,811 | +1.6% | Stable |
| CG | High (>92%) | 44,581 | 43,937 | -1.4% | Stable |
| CK | High (>92%) | 42,176 | 42,398 | +0.5% | Stable |
| MR | Low (>85%) | 20,784 | 19,468 | -6.3% | Stable |
| AO | Medium (>85%) | 15,776 | 13,883 | -12.0% | Stable |
| GN | High (>92%) | 14,333 | 13,110 | -8.5% | Stable |
| KN | Medium (>85%) | 11,048 | 10,259 | -7.1% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-17*
