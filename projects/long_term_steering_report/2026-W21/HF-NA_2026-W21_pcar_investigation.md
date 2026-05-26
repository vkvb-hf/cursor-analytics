# PCAR Investigation: HF-NA 2026-W21

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 90.68% → 92.33% (+1.82%)  
**Volume:** 18,883 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate improved significantly from 90.68% to 92.33% (+1.82%) in W21, representing a partial recovery toward the 94.12% baseline seen in W14.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Recovery from W20 dip, still below W14-W17 levels | +1.65pp | ⚠️ |
| L1: Country Breakdown | No countries exceeded ±2.5% threshold | US +1.60pp, CA +0.82pp | ✅ |
| L1: Payment Method | Credit Card improved, Others declined | CC +2.46pp, Others -6.59pp | ⚠️ |
| Mix Shift | CA volume increased (+10.6%), US decreased (-7.6%) | Higher-AR CA gaining share | ✅ |

**Key Findings:**
- US drove the majority of improvement with rate increasing from 89.15% to 90.75% (+1.60pp) on 14,363 orders (76% of volume)
- Credit Card payment method showed strong recovery (+2.46pp to 92.46%), accounting for 11,017 orders
- "Others" payment method declined significantly (-6.59pp to 90.91%), though volume is minimal (55 orders)
- Mix shift toward higher-performing CA (+10.6% volume growth at 97.32% rate) contributed positively to overall rate
- Despite W21 improvement, the rate remains 1.79pp below the W14 baseline of 94.12%, indicating an incomplete recovery

**Action:** Monitor - The improvement is encouraging but the metric has not fully recovered to W14-W17 levels. Continue tracking Credit Card performance and overall trend in W22 to confirm sustained recovery.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W21 | 92.33% | 18,883 | +1.82% ← REPORTED CHANGE |
| 2026-W20 | 90.68% | 19,628 | -0.37% |
| 2026-W19 | 91.02% | 20,734 | -1.55% |
| 2026-W18 | 92.45% | 21,206 | -1.59% |
| 2026-W17 | 93.94% | 20,363 | +0.09% |
| 2026-W16 | 93.86% | 23,369 | -0.23% |
| 2026-W15 | 94.08% | 23,513 | -0.04% |
| 2026-W14 | 94.12% | 20,221 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 97.32% | 96.50% | +0.85% | 4,520 |  |
| US | 90.75% | 89.15% | +1.80% | 14,363 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | 90.91% | 97.5% | -6.76% | 55 | ⚠️ |
| Apple Pay | 91.98% | 91.59% | +0.43% | 6,062 |  |
| Paypal | 92.74% | 91.46% | +1.40% | 1,749 |  |
| Credit Card | 92.46% | 90.0% | +2.73% | 11,017 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 15,543 | 14,363 | -7.6% | Stable |
| CA | High (>92%) | 4,085 | 4,520 | +10.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-26*
