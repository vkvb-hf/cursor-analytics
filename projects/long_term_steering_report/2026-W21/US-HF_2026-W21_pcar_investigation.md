# PCAR Investigation: US-HF 2026-W21

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 89.15% → 90.75% (+1.79%)  
**Volume:** 14,363 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate for US-HF improved from 89.15% to 90.75% (+1.79%) in 2026-W21, representing a recovery after three consecutive weeks of decline.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate recovering from W18-W20 dip | +1.60pp | ✅ |
| L1: Country Breakdown | US within threshold (+1.80%) | +1.80% | ✅ |
| L1: PaymentMethod | Credit Card improved; Others declined | Mixed | ⚠️ |
| L1: PaymentProvider | No data available | N/A | ✅ |
| Mix Shift | Volume declined 7.6% but impact stable | -7.6% vol | ✅ |

**Key Findings:**
- Credit Card approval rate improved significantly from 88.19% to 90.76% (+2.92%), driving the overall improvement with 8,186 orders (57% of volume)
- "Others" payment method declined sharply from 97.5% to 90.91% (-6.76%), though volume is minimal at only 55 orders
- Current rate of 90.75% remains below the 8-week high of 93.02% (W15), indicating partial recovery only
- Order volume decreased from 15,543 to 14,363 (-7.6% WoW), continuing a downward volume trend since W16
- Apple Pay and PayPal remained stable with minimal change (+0.38% and +0.77% respectively)

**Action:** Monitor – The improvement is positive and driven by Credit Card performance, but continued observation is recommended to confirm sustained recovery toward the 92-93% baseline seen in W14-W17.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W21 | 90.75% | 14,363 | +1.79% ← REPORTED CHANGE |
| 2026-W20 | 89.15% | 15,543 | -0.51% |
| 2026-W19 | 89.61% | 16,327 | -1.67% |
| 2026-W18 | 91.13% | 16,396 | -1.66% |
| 2026-W17 | 92.67% | 15,496 | -0.09% |
| 2026-W16 | 92.75% | 18,142 | -0.29% |
| 2026-W15 | 93.02% | 17,670 | +0.18% |
| 2026-W14 | 92.85% | 14,911 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 90.75% | 89.15% | +1.80% | 14,363 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | 90.91% | 97.5% | -6.76% | 55 | ⚠️ |
| Apple Pay | 90.67% | 90.32% | +0.38% | 4,909 |  |
| Paypal | 91.01% | 90.32% | +0.77% | 1,213 |  |
| Credit Card | 90.76% | 88.19% | +2.92% | 8,186 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 15,543 | 14,363 | -7.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-26*
