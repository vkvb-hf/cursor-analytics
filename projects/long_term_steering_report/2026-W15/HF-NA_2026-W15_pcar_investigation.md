# PCAR Investigation: HF-NA 2026-W15

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 94.12% → 94.08% (-0.04%)  
**Volume:** 23,512 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate declined marginally from 94.12% to 94.08% (-0.04pp) in W15, a statistically non-significant change within normal weekly variance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (93.92%-95.23%) | -0.04pp | ✅ |
| L1: Country Breakdown | No country exceeded ±2.5% threshold | US +0.34pp, CA +0.02pp | ✅ |
| L1: PaymentMethod | "Others" declined -2.49pp but minimal volume (91 orders) | -2.49pp | ✅ |
| L1: PaymentProvider | No data flagged | N/A | ✅ |
| Mix Shift | Both US and CA remain in High AR tier | Stable | ✅ |

**Key Findings:**
- The -0.04pp decline is well within normal weekly fluctuation, with the 8-week range spanning 93.92% to 95.23%
- Both US (+0.34pp) and CA (+0.02pp) showed slight improvements at the country level, indicating no geographic concerns
- "Others" payment method declined -2.49pp but represents only 91 orders (0.4% of volume), making it immaterial to overall performance
- Apple Pay showed a -1.08pp decline (7,678 orders) while Credit Card improved +0.50pp (13,776 orders), partially offsetting each other
- Volume increased 16.3% week-over-week (20,221 → 23,512 orders) with no negative impact on approval rates

**Action:** Monitor — No investigation required. Change is not statistically significant and all dimensional checks pass within acceptable thresholds.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 94.08% | 23,512 | -0.04% ← REPORTED CHANGE |
| 2026-W14 | 94.12% | 20,221 | +0.21% |
| 2026-W13 | 93.92% | 20,751 | -0.29% |
| 2026-W12 | 94.19% | 21,127 | +0.03% |
| 2026-W11 | 94.16% | 22,919 | -1.12% |
| 2026-W10 | 95.23% | 23,025 | +1.30% |
| 2026-W09 | 94.01% | 27,201 | +0.01% |
| 2026-W08 | 94.0% | 26,180 | - |

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
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | 96.7% | 99.17% | -2.49% | 91 |  |
| Apple Pay | 93.46% | 94.48% | -1.08% | 7,678 |  |
| Paypal | 95.42% | 94.97% | +0.48% | 1,967 |  |
| Credit Card | 94.21% | 93.75% | +0.50% | 13,776 |  |

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
