# PCAR Investigation: US-HF 2026-W16

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 93.02% → 92.75% (-0.29%)  
**Volume:** 18,142 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate declined slightly from 93.02% to 92.75% (-0.27 pp) in W16, a statistically non-significant change within normal weekly fluctuation.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (92.57%-94.58%) | -0.27 pp | ✅ |
| L1: Country Breakdown | US threshold check (±2.5%) | -0.13 pp | ✅ |
| L1: PaymentMethod | No flags triggered | Largest: Others -2.34 pp (n=54) | ✅ |
| L1: PaymentProvider | No data available | N/A | ✅ |
| Mix Shift | US volume shift | +3.7% | ✅ Stable |

**Key Findings:**
- The -0.27 pp decline is not statistically significant and falls within the normal 8-week range (92.57% - 94.58%)
- US showed minimal decline of -0.13 pp, well within the ±2.5% threshold
- "Others" payment method showed -2.34 pp decline but represents negligible volume (54 orders)
- Credit Card, the highest volume method (10,008 orders), declined only -0.51 pp
- Volume increased from 17,669 to 18,142 orders (+2.7%), indicating healthy transaction growth despite the minor rate decline

**Action:** Monitor — No investigation required. Continue standard weekly tracking.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 92.75% | 18,142 | -0.29% ← REPORTED CHANGE |
| 2026-W15 | 93.02% | 17,669 | +0.18% |
| 2026-W14 | 92.85% | 14,911 | +0.30% |
| 2026-W13 | 92.57% | 15,361 | -0.38% |
| 2026-W12 | 92.92% | 15,651 | -0.09% |
| 2026-W11 | 93.0% | 16,952 | -1.67% |
| 2026-W10 | 94.58% | 17,681 | +1.54% |
| 2026-W09 | 93.15% | 21,474 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.97% | 93.09% | -0.13% | 511,272 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | 94.44% | 96.7% | -2.34% | 54 |  |
| Paypal | 94.27% | 95.39% | -1.18% | 1,483 |  |
| Credit Card | 92.45% | 92.92% | -0.51% | 10,008 |  |
| Apple Pay | 92.85% | 92.58% | +0.29% | 6,597 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 492,811 | 511,272 | +3.7% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-21*
