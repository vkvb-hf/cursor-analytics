# PCAR Investigation: US-HF 2026-W15

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 92.85% → 93.02% (+0.18%)  
**Volume:** 17,669 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** PCAR for US-HF improved marginally from 92.85% to 93.02% (+0.17pp) in 2026-W15, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (92.57%-94.58%) | +0.17pp | ✅ |
| L1: Country Breakdown | No countries exceeding ±2.5% threshold | +0.34pp (US) | ✅ |
| L1: PaymentMethod | "Others" declined -2.49% but low volume (91 orders) | Mixed | ✅ |
| L1: PaymentProvider | No data available | N/A | ✅ |
| Mix Shift | High AR tier stable, minor volume decrease (-0.9%) | Stable | ✅ |

**Key Findings:**
- The +0.17pp week-over-week improvement is within normal weekly fluctuation and not statistically significant
- Credit Card approval rate improved from 92.09% to 92.92% (+0.83pp), representing the largest payment method by volume (9,998 orders)
- "Others" payment method showed a -2.49% decline, but with only 91 orders, this has negligible impact on overall rate
- Volume increased 18.5% WoW (14,911 → 17,669 orders), returning closer to W10 levels (17,681)
- 8-week trend shows rate has stabilized in the 92.5%-93.5% range after a peak of 94.58% in W10

**Action:** Monitor — No investigation required. The change is not significant, all funnel checks pass, and the rate remains within normal operating range.

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
