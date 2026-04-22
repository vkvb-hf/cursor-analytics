# PCAR Investigation: HF-NA 2026-W16

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 94.08% → 93.86% (-0.23%)  
**Volume:** 23,369 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate declined by -0.23 percentage points (94.08% → 93.86%) on volume of 23,369 orders, with the change flagged as not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 8-Week Trend | Rate within normal range (93.86% vs 8-wk range 93.92%-95.23%) | -0.23pp | ✅ |
| Country Breakdown | No countries exceed ±2.5% threshold | US: -0.29pp, CA: +0.44pp | ✅ |
| Payment Method | No methods exceed threshold; "Others" largest drop at -2.34pp | Low volume (54 orders) | ✅ |
| Mix Shift | CA volume down -10.5% but impact stable | No adverse mix effect | ✅ |

**Key Findings:**
- The -0.23pp decline is within normal weekly fluctuation; the 8-week trend shows rates oscillating between 93.86% and 95.23%
- US drove the majority of the decline (-0.29pp on 18,142 orders), while CA improved (+0.44pp) despite a -10.5% volume drop
- "Others" payment method showed a -2.34pp decline, but with only 54 orders this is not material to overall performance
- Credit Card (largest volume at 13,385 orders) declined -0.42pp, contributing most to the overall rate drop
- No payment providers flagged anomalies; PaymentProvider data returned no flagged results

**Action:** Monitor — The decline is not statistically significant and falls within normal weekly variance. Continue standard monitoring for W17.

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
