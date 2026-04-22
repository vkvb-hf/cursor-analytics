# Reactivation Investigation: HF-NA 2026-W15

**Metric:** Reactivation Rate  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 90.24% → 89.41% (-0.92%)  
**Volume:** 23,973 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Reactivation Rate declined by -0.83 pp (from 90.24% to 89.41%) in 2026-W15, with 23,973 orders processed; this change is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Consistent downward trend over last 2 weeks | -0.92% | ⚠️ |
| L1: Country Breakdown | No countries exceeding ±2.5% threshold | CA: -1.70%, US: -0.58% | ✅ |
| L1: PaymentMethod | "Others" flagged with -52.38% change | Volume only 7 orders | ✅ |
| Mix Shift Analysis | US volume +43.6%, CA volume -9.4% | Impact: Stable | ✅ |

**Key Findings:**
- The -0.83 pp decline represents a continuation of a 2-week downward trend (W14: 90.95% → W15: 90.24% → W16: 89.41%), though rates remain above the 8-week low of 86.89% in W09
- CA showed the largest country-level decline at -1.70 pp (90.82% → 89.27%) but remains below the ±2.5% investigation threshold
- The "Others" payment method flagged a -52.38% change, but with only 7 orders this is not operationally meaningful
- US volume increased significantly (+43.6%) while maintaining relatively stable performance (-0.58 pp), indicating no capacity-related degradation
- All major payment methods (Credit Card, PayPal, Apple Pay) showed modest declines between -0.46% and -1.26%, suggesting no payment-specific issues

**Action:** Monitor — The decline is not statistically significant, no dimensions exceeded investigation thresholds, and the metric remains within normal operating range. Continue monitoring for a third consecutive week of decline.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 89.41% | 23,973 | -0.92% |
| 2026-W15 | 90.24% | 26,178 | -0.78% ← REPORTED CHANGE |
| 2026-W14 | 90.95% | 20,279 | +0.29% |
| 2026-W13 | 90.69% | 21,909 | -0.36% |
| 2026-W12 | 91.02% | 21,059 | +1.73% |
| 2026-W11 | 89.47% | 24,019 | +1.41% |
| 2026-W10 | 88.23% | 27,936 | +1.54% |
| 2026-W09 | 86.89% | 23,884 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 89.27% | 90.82% | -1.70% | 5,023 |  |
| US | 90.47% | 90.99% | -0.58% | 21,155 |  |

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
| US | Medium (>85%) | 14,736 | 21,155 | +43.6% | Stable |
| CA | Medium (>85%) | 5,543 | 5,023 | -9.4% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
