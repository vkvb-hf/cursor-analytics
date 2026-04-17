# Reactivation Investigation: WL 2026-W15

**Metric:** Reactivation Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 88.67% → 89.29% (+0.70%)  
**Volume:** 9,277 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Reactivation Rate improved slightly from 88.67% to 89.29% (+0.62 pp) in W15, representing a statistically non-significant change on 9,277 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (85-89%) | +0.70% | ✅ |
| L1: Country Breakdown | No country exceeds ±2.5% threshold | Max +2.17% (AO) | ✅ |
| L1: PaymentMethod | Low-volume anomaly in "Others" | -66.67% (3 orders) | ⚠️ |
| L1: PaymentMethod | Apple Pay improvement | +3.99% (794 orders) | ⚠️ |
| Mix Shift | All countries stable | Max shift -12.0% (AO) | ✅ |

**Key Findings:**
- The +0.70% week-over-week improvement continues an upward trend from W11 (87.5%) to W15 (89.29%), representing a +1.79 pp gain over 4 weeks
- All four countries showed improvement: AO (+2.17%), MR (+1.45%), ER (+1.23%), and GN (+1.07%), with none exceeding the ±2.5% threshold
- Apple Pay showed notable improvement (+3.99% to 74.94%) though it remains the lowest-performing payment method and has low volume (794 orders)
- "Others" payment method dropped -66.67% but represents only 3 orders, making it statistically irrelevant
- Volume increased significantly from 7,706 to 9,277 orders (+20.4%), suggesting healthy reactivation activity

**Action:** Monitor — No significant anomalies detected; continue tracking the positive trend trajectory.

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
