# PCAR Investigation: HF-NA 2026-W15

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 94.08% → 93.86% (-0.23%)  
**Volume:** 23,369 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate declined marginally from 94.08% to 93.86% (-0.22 pp) in 2026-W15, a change flagged as not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal variance (93.86%-95.23% range) | -0.22 pp | ✅ |
| L1: Country Breakdown | No country exceeded ±2.5% threshold | CA: -0.40 pp, US: +0.18 pp | ✅ |
| L1: PaymentMethod | "Others" declined -2.49 pp but minimal volume (91 orders) | -2.49 pp | ✅ |
| L1: PaymentProvider | No data available | N/A | ✅ |
| Mix Shift Analysis | Both US and CA remain in High AR tier with stable impact | US: +18.5% vol, CA: +10.0% vol | ✅ |

**Key Findings:**
- The -0.22 pp decline is within normal weekly fluctuation observed over the 8-week period (range: 93.86% - 95.23%)
- US showed a slight improvement (+0.18 pp) while CA experienced a minor decline (-0.40 pp); neither breached the ±2.5% threshold
- "Others" payment method dropped -2.49 pp, but with only 91 orders this has negligible impact on overall rate
- Apple Pay declined -1.08 pp on significant volume (7,678 orders), partially offset by Credit Card improvement (+0.50 pp)
- Volume increased in both countries (US: +18.5%, CA: +10.0%) with both maintaining High AR tier status

**Action:** Monitor — No investigation required. The decline is not statistically significant, no thresholds were breached, and the rate remains consistent with recent weekly performance.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 93.86% | 23,369 | -0.23% |
| 2026-W15 | 94.08% | 23,512 | -0.04% ← REPORTED CHANGE |
| 2026-W14 | 94.12% | 20,221 | +0.21% |
| 2026-W13 | 93.92% | 20,751 | -0.29% |
| 2026-W12 | 94.19% | 21,127 | +0.03% |
| 2026-W11 | 94.16% | 22,919 | -1.12% |
| 2026-W10 | 95.23% | 23,025 | +1.30% |
| 2026-W09 | 94.01% | 27,201 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 97.30% | 97.70% | -0.42% | 5,843 |  |
| US | 93.02% | 92.85% | +0.18% | 17,669 |  |

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
| US | High (>92%) | 14,911 | 17,669 | +18.5% | Stable |
| CA | High (>92%) | 5,310 | 5,843 | +10.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
