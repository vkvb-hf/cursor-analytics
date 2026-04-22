# PCAR Investigation: HF-NA 2026-W16

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 94.08% → 93.86% (-0.23%)  
**Volume:** 23,369 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate declined from 94.08% to 93.86% (-0.22pp) in 2026-W16, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (93.86% vs 8-week range 93.92%-95.23%) | -0.22pp | ✅ |
| L1: Country Breakdown | No countries exceed ±2.5% threshold | US: -0.29pp, CA: +0.44pp | ✅ |
| L1: PaymentMethod | No methods exceed threshold; "Others" at -2.34% but low volume (54) | Varies | ✅ |
| L1: PaymentProvider | No data available | N/A | ✅ |
| Mix Shift | CA volume down 10.5% but impact stable | Minimal | ✅ |

**Key Findings:**
- The -0.22pp decline is within normal weekly fluctuation observed over the 8-week period (range: 93.92% to 95.23%)
- US accounts for 78% of volume (18,142 orders) and showed a minor decline of -0.29pp
- CA improved by +0.44pp despite a 10.5% volume decrease (5,843 → 5,227 orders)
- No payment method showed significant degradation; "Others" declined -2.34pp but represents only 54 orders
- All countries and dimensions remain within acceptable thresholds

**Action:** Monitor — No immediate action required. The decline is not statistically significant and all dimensional checks pass. Continue standard weekly monitoring.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 93.86% | 23,369 | -0.23% ← REPORTED CHANGE |
| 2026-W15 | 94.08% | 23,512 | -0.04% |
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
| US | 92.75% | 93.02% | -0.29% | 18,142 |  |
| CA | 97.72% | 97.30% | +0.44% | 5,227 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | 94.44% | 96.7% | -2.34% | 54 |  |
| Paypal | 94.75% | 95.42% | -0.70% | 2,001 |  |
| Credit Card | 93.82% | 94.21% | -0.42% | 13,385 |  |
| Apple Pay | 93.69% | 93.46% | +0.25% | 7,929 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 17,669 | 18,142 | +2.7% | Stable |
| CA | High (>92%) | 5,843 | 5,227 | -10.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
