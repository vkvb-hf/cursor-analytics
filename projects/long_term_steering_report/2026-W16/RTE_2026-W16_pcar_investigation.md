# PCAR Investigation: RTE 2026-W16

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 97.22% → 97.2% (-0.02%)  
**Volume:** 44,111 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate showed a minimal decline of -0.02pp (97.22% → 97.2%) on 44,111 orders, which is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Stability check | -0.02pp | ✅ Within normal variance |
| L1: Country Breakdown | Threshold ±2.5% | No countries exceeded | ✅ No outliers |
| L1: PaymentMethod | Dimension scan | Others +8.69pp | ⚠️ Flagged but low volume |
| L1: PaymentProvider | Dimension scan | No data | ✅ No issues detected |
| Mix Shift | Volume distribution | All stable | ✅ No concerning shifts |

**Key Findings:**
- The -0.02pp decline is well within normal week-over-week fluctuation and is not statistically significant
- No countries exceeded the ±2.5% threshold; TK showed the largest decline at -1.76pp but remains below threshold
- "Others" payment method showed +8.69pp improvement but represents only 1,338 orders (3% of volume)
- TZ volume increased +20.9% week-over-week while maintaining stable approval rates (+1.33pp)
- The 8-week trend shows the rate has been stable between 96.88% and 97.3%, with current week within this range

**Action:** Monitor — No investigation required. The change is minimal, not significant, and no dimensions exceeded alerting thresholds.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 97.2% | 44,111 | -0.02% ← REPORTED CHANGE |
| 2026-W15 | 97.22% | 44,168 | +0.33% |
| 2026-W14 | 96.9% | 39,914 | +0.01% |
| 2026-W13 | 96.89% | 42,897 | +0.01% |
| 2026-W12 | 96.88% | 44,209 | -0.11% |
| 2026-W11 | 96.99% | 47,403 | +0.10% |
| 2026-W10 | 96.89% | 48,399 | -0.42% |
| 2026-W09 | 97.3% | 50,858 | - |

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
| Unknown | nan% | nan% | +nan% | 0 |  |
| Paypal | 98.31% | 98.58% | -0.28% | 5,148 |  |
| Credit Card | 97.87% | 97.86% | +0.01% | 27,332 |  |
| Apple Pay | 97.42% | 97.21% | +0.21% | 10,293 |  |
| Others | 77.8% | 71.58% | +8.69% | 1,338 | ⚠️ |

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
