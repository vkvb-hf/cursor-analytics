# Reactivation Investigation: HF-NA 2026-W15

**Metric:** Reactivation Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 90.95% → 90.24% (-0.78%)  
**Volume:** 26,178 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Reactivation Rate declined from 90.95% to 90.24% (-0.71pp) in W15, representing a statistically non-significant change on 26,178 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal variance (86.89%-91.02% range) | -0.71pp | ✅ |
| L1: Country Breakdown | No country exceeded ±2.5% threshold | US +0.34%, CA +0.02% | ✅ |
| L1: Dimension Scan | "Others" payment method flagged | -52.38% | ⚠️ |
| Mix Shift Analysis | Both US and CA stable | US -0.9%, CA -2.2% vol | ✅ |

**Key Findings:**
- The -0.71pp decline is within normal weekly fluctuation observed over the 8-week period (range: 86.89% - 91.02%)
- Both US (93.09%) and CA (93.51%) showed stable or slightly improved rates, with no country exceeding the ±2.5% investigation threshold
- "Others" PaymentMethod showed a -52.38% change, but volume is negligible (7 orders) making this statistically irrelevant
- W15 had the highest volume in the 8-week period (26,178 orders), representing a +29% increase vs W14 (20,279 orders)
- Credit Card (18,327 orders, -0.72%) drove the majority of volume with minimal rate change

**Action:** Monitor — The decline is not statistically significant, no countries breached thresholds, and the flagged payment method has negligible volume. Continue standard monitoring in W16.

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

*Report: 2026-04-15*
