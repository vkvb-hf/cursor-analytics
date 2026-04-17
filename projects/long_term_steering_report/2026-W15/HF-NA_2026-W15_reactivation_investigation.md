# Reactivation Investigation: HF-NA 2026-W15

**Metric:** Reactivation Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 90.95% → 90.24% (-0.78%)  
**Volume:** 26,178 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Reactivation Rate declined from 90.95% to 90.24% (-0.78%, or -0.71 pp) in W15, with the change flagged as not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 8-Week Trend | Rate within normal range (86.89%-91.02%) | -0.71 pp | ✅ |
| Country Breakdown | US +0.34%, CA +0.02% | No country >±2.5% | ✅ |
| Payment Method | Others -52.38% (7 orders) | Low volume outlier | ⚠️ |
| Payment Provider | No data flagged | N/A | ✅ |
| Mix Shift | US -0.9%, CA -2.2% volume | Stable impact | ✅ |

**Key Findings:**
- The -0.78% week-over-week decline is not statistically significant and falls within the normal 8-week fluctuation range (86.89% to 91.02%)
- No countries exceeded the ±2.5% threshold; both US (+0.34%) and CA (+0.02%) showed stable or slightly improved performance
- "Others" payment method showed a -52.38% decline, but this is based on only 7 orders (negligible volume impact)
- Volume increased significantly from 20,279 (W14) to 26,178 (W15), a +29% increase, which may contribute to natural rate variance
- Current rate of 90.24% remains elevated compared to W08-W10 baseline (86.89%-88.23%)

**Action:** Monitor — No investigation required. The decline is not significant, no dimensional flags warrant deep-dive, and the rate remains within healthy historical bounds.

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
