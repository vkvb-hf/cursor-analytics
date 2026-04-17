# Reactivation Investigation: HF-NA 2026-W15

**Metric:** Reactivation Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 90.95% → 90.24% (-0.78%)  
**Volume:** 26,178 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Reactivation Rate declined from 90.95% to 90.24% (-0.71pp) in W15, representing a non-significant change on a volume of 26,178 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (86.89%-91.02%) | -0.71pp | ✅ |
| L1: Country Breakdown | No country exceeded ±2.5% threshold | US +0.34%, CA +0.02% | ✅ |
| L1: PaymentMethod | "Others" flagged but minimal volume | -52.38% on 7 orders | ✅ |
| Mix Shift | Both US and CA stable | US -0.9%, CA -2.2% vol | ✅ |

**Key Findings:**
- The -0.71pp decline is within normal weekly fluctuation, as the 8-week trend shows rates ranging from 86.89% (W09) to 91.02% (W12)
- Both US (93.09%) and CA (93.51%) showed stable or slightly improved reactivation rates week-over-week
- The "Others" PaymentMethod shows a -52.38% change but is based on only 7 orders, making it statistically irrelevant
- Volume increased significantly from 20,279 (W14) to 26,178 (W15), a +29% increase, which may contribute to rate normalization
- Credit Card (18,327 orders, 70% of volume) showed only a -0.72% change, indicating core payment stability

**Action:** Monitor — No significant degradation detected; all countries and major payment methods within acceptable thresholds.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 90.24% | 26,178 | -0.78% ← REPORTED CHANGE |
| 2026-W14 | 90.95% | 20,279 | +0.29% |
| 2026-W13 | 90.69% | 21,909 | -0.36% |
| 2026-W12 | 91.02% | 21,059 | +1.73% |
| 2026-W11 | 89.47% | 24,019 | +1.41% |
| 2026-W10 | 88.23% | 27,936 | +1.54% |
| 2026-W09 | 86.89% | 23,884 | -0.57% |
| 2026-W08 | 87.39% | 25,523 | - |

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
| Others | 28.57% | 60.0% | -52.38% | 7 | ⚠️ |
| Paypal | 92.78% | 93.97% | -1.26% | 4,016 |  |
| Credit Card | 90.17% | 90.83% | -0.72% | 18,327 |  |
| Apple Pay | 87.98% | 88.39% | -0.46% | 3,828 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

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

*Report: 2026-04-17*
