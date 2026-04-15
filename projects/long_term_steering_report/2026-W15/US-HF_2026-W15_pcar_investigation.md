# PCAR Investigation: US-HF 2026-W15

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 92.85% → 93.02% (+0.18%)  
**Volume:** 17,669 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** PCAR for US-HF improved marginally from 92.85% to 93.02% (+0.17 pp) in 2026-W15, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | Rate within normal 8-week range (92.57%-94.58%) | +0.17 pp | ✅ |
| L1: Country Breakdown | No countries exceeding ±2.5% threshold | +0.34 pp (US) | ✅ |
| L1: PaymentMethod | "Others" declined -2.49% but low volume (91 orders) | Mixed | ✅ |
| L1: PaymentProvider | No data available | N/A | ✅ |
| Mix Shift | US High AR tier stable (-0.9% volume shift) | Stable | ✅ |

**Key Findings:**
- The +0.17 pp week-over-week improvement is within normal fluctuation range; the 8-week trend shows rates oscillating between 92.57% and 94.58%
- Credit Card approval rate improved +0.90 pp (92.09% → 92.92%) on the highest volume segment (9,998 orders)
- Apple Pay declined -1.00 pp (93.51% → 92.58%) across 6,169 orders, partially offsetting Credit Card gains
- "Others" payment method showed a -2.49 pp decline but represents negligible volume (91 orders)
- Order volume increased 18.5% week-over-week (14,911 → 17,669 orders) without negatively impacting approval rates

**Action:** Monitor — No investigation required. The change is not statistically significant, no dimensions exceeded thresholds, and the metric remains within normal operating range.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 93.02% | 17,669 | +0.18% ← REPORTED CHANGE |
| 2026-W14 | 92.85% | 14,911 | +0.30% |
| 2026-W13 | 92.57% | 15,361 | -0.38% |
| 2026-W12 | 92.92% | 15,651 | -0.09% |
| 2026-W11 | 93.0% | 16,952 | -1.67% |
| 2026-W10 | 94.58% | 17,681 | +1.54% |
| 2026-W09 | 93.15% | 21,474 | +0.13% |
| 2026-W08 | 93.03% | 20,421 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 93.09% | 92.78% | +0.34% | 492,811 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | 96.7% | 99.17% | -2.49% | 91 |  |
| Apple Pay | 92.58% | 93.51% | -1.00% | 6,169 |  |
| Paypal | 95.39% | 94.57% | +0.87% | 1,411 |  |
| Credit Card | 92.92% | 92.09% | +0.90% | 9,998 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 497,052 | 492,811 | -0.9% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-15*
