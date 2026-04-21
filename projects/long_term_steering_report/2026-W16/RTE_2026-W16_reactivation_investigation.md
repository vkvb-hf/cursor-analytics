# Reactivation Investigation: RTE 2026-W16

**Metric:** Reactivation Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 90.41% → 89.16% (-1.38%)  
**Volume:** 18,508 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Reactivation Rate declined from 90.41% to 89.16% (-1.38%, or -1.25pp) in W16, representing a significant drop across 18,508 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate dropped but remains above W09-W13 baseline | -1.38% | ⚠️ |
| L1: Country Breakdown | No country exceeded ±2.5% threshold | Max: TK -1.76% | ✅ |
| L1: PaymentMethod | "Others" segment shows +13.29% but low volume (55) | Paypal -1.56%, Credit Card -1.52% | ⚠️ |
| Mix Shift Analysis | All countries show stable impact | Volume shifts normal | ✅ |

**Key Findings:**
- The -1.38% decline reverses the +1.36% gain from W15, returning the rate closer to W14 levels (89.2%)
- TK showed the largest country-level decline at -1.76%, though still below the ±2.5% threshold
- Credit Card payments (highest volume at 13,671 orders) declined -1.52%, while PayPal declined -1.56%
- Apple Pay maintains notably lower performance (69.47%) compared to other payment methods but showed slight improvement (+1.24%)
- No single country or dimension triggered threshold alerts, suggesting a broad-based, distributed decline

**Action:** Monitor – The decline is significant but no root cause dimension exceeded thresholds. Continue tracking W17 to determine if this is a one-week correction or the start of a trend reversal.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 89.16% | 18,508 | -1.38% ← REPORTED CHANGE |
| 2026-W15 | 90.41% | 19,757 | +1.36% |
| 2026-W14 | 89.2% | 17,264 | +0.68% |
| 2026-W13 | 88.6% | 19,685 | - |
| 2026-W12 | 88.6% | 20,873 | +1.87% |
| 2026-W11 | 86.97% | 23,790 | +2.19% |
| 2026-W10 | 85.11% | 26,102 | +0.75% |
| 2026-W09 | 84.48% | 24,364 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TK | 93.65% | 95.33% | -1.76% | 2,079 |  |
| CF | 93.47% | 94.14% | -0.71% | 53,579 |  |
| FJ | 93.79% | 93.97% | -0.19% | 395,303 |  |
| TZ | 92.91% | 91.69% | +1.33% | 3,216 |  |
| TV | 93.52% | 92.14% | +1.50% | 2,053 |  |
| TO | 88.82% | 86.67% | +2.48% | 3,301 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 91.94% | 93.4% | -1.56% | 2,879 |  |
| Credit Card | 91.3% | 92.71% | -1.52% | 13,671 |  |
| Apple Pay | 69.47% | 68.62% | +1.24% | 1,903 |  |
| Others | 90.91% | 80.25% | +13.29% | 55 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 388,956 | 395,303 | +1.6% | Stable |
| CF | High (>92%) | 51,881 | 53,579 | +3.3% | Stable |
| YE | Medium (>85%) | 42,126 | 43,089 | +2.3% | Stable |
| TT | High (>92%) | 4,617 | 4,817 | +4.3% | Stable |
| TO | Medium (>85%) | 3,204 | 3,301 | +3.0% | Stable |
| TZ | Medium (>85%) | 2,660 | 3,216 | +20.9% | Stable |
| TK | High (>92%) | 1,950 | 2,079 | +6.6% | Stable |
| TV | High (>92%) | 1,895 | 2,053 | +8.3% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-21*
