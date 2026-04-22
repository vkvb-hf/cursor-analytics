# PCAR Investigation: US-HF 2026-W15

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 93.02% → 92.75% (-0.29%)  
**Volume:** 18,142 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate declined by -0.27 pp (from 93.02% to 92.75%) in W16, a statistically non-significant change within normal weekly fluctuation range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (92.57%-94.58%) | -0.27 pp | ✅ |
| L1: Country Breakdown | No countries exceeding ±2.5% threshold | +0.18 pp (US) | ✅ |
| L1: Payment Method | No methods exceeding ±2.5% threshold | -2.49% (Others) low volume | ✅ |
| Mix Shift | Volume shifted to High AR tier | +18.5% volume | ✅ |

**Key Findings:**
- The -0.29% week-over-week decline is within normal operating variance, with rates fluctuating between 92.57% and 94.58% over the past 8 weeks
- US showed a slight improvement of +0.18 pp in the prior period comparison, with no countries breaching the ±2.5% threshold
- "Others" payment method showed a -2.49% decline but represents only 91 orders (0.5% of volume), making it statistically insignificant
- Apple Pay experienced a -1.00 pp decline (92.58% from 93.51%) across 6,169 orders, worth monitoring but below threshold
- Volume increased +18.5% week-over-week (14,911 → 17,669 orders) while maintaining stable High AR tier performance

**Action:** Monitor — No immediate investigation required. Continue standard weekly monitoring with attention to Apple Pay performance trends.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 92.75% | 18,142 | -0.29% |
| 2026-W15 | 93.02% | 17,669 | +0.18% ← REPORTED CHANGE |
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
| US | 93.02% | 92.85% | +0.18% | 17,669 |  |

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
| US | High (>92%) | 14,911 | 17,669 | +18.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
