# PCAR Investigation: RTE 2026-W22

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 97.25% → 97.02% (-0.24%)  
**Volume:** 31,528 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate declined by -0.24pp (97.25% → 97.02%) on volume of 31,528 orders in 2026-W22, a statistically not significant change.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Within normal range | -0.24pp | ✅ |
| L1: Country Breakdown | No countries exceed ±2.5% threshold | TV worst at -2.50pp | ✅ |
| L1: PaymentMethod | No major degradation | Others -1.88pp (low vol) | ✅ |
| L1: PaymentProvider | No data available | N/A | ✅ |
| Mix Shift Analysis | All countries stable impact | TV +28.5% vol increase | ✅ |

**Key Findings:**
- The -0.24pp decline is within normal weekly fluctuation, with the 8-week trend showing rates oscillating between 96.49% and 97.25%
- TV showed the largest rate decline (-2.50pp, 86.39% → 84.24%) but represents only 406 orders (1.3% of volume) and did not exceed threshold
- Overall volume declined -11.4% week-over-week (35,603 → 31,528 orders), consistent with volume decreases across most countries
- FJ, the largest market (22,373 orders, 71% of volume), showed minimal decline of -0.33pp with stable high performance at 97.41%
- "Others" payment method showed -1.88pp decline but with low volume (815 orders) and high baseline rejection rate (76.56%)

**Action:** Monitor — No immediate action required. The decline is not statistically significant and no dimensions exceeded investigation thresholds. Continue standard monitoring.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W22 | 97.02% | 31,528 | -0.24% ← REPORTED CHANGE |
| 2026-W21 | 97.25% | 35,603 | +0.79% |
| 2026-W20 | 96.49% | 38,879 | -0.18% |
| 2026-W19 | 96.66% | 38,661 | +0.15% |
| 2026-W18 | 96.52% | 40,203 | -0.55% |
| 2026-W17 | 97.05% | 42,589 | -0.15% |
| 2026-W16 | 97.2% | 44,111 | -0.02% |
| 2026-W15 | 97.22% | 44,168 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TV | 84.24% | 86.39% | -2.50% | 406 |  |
| FJ | 97.41% | 97.73% | -0.33% | 22,373 |  |
| YE | 97.74% | 97.19% | +0.57% | 2,785 |  |
| TZ | 97.72% | 96.50% | +1.27% | 351 |  |
| TO | 88.13% | 86.63% | +1.72% | 320 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | 76.56% | 78.03% | -1.88% | 815 |  |
| Apple Pay | 96.5% | 97.26% | -0.78% | 7,851 |  |
| Credit Card | 97.88% | 97.88% | -0.01% | 19,297 |  |
| Paypal | 98.26% | 97.97% | +0.30% | 3,565 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 25,459 | 22,373 | -12.1% | Stable |
| CF | High (>92%) | 5,150 | 4,506 | -12.5% | Stable |
| YE | High (>92%) | 3,092 | 2,785 | -9.9% | Stable |
| TT | Low (>85%) | 578 | 512 | -11.4% | Stable |
| TO | Medium (>85%) | 374 | 320 | -14.4% | Stable |
| TZ | High (>92%) | 371 | 351 | -5.4% | Stable |
| TV | Medium (>85%) | 316 | 406 | +28.5% | Stable |
| TK | High (>92%) | 263 | 275 | +4.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-02*
