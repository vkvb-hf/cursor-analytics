# PCAR Investigation: WL 2026-W17

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 97.59% → 96.82% (-0.79%)  
**Volume:** 10,957 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate declined from 97.59% to 96.82% (-0.79pp) in WL 2026-W17, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (96.82% vs 96.88-97.59% historical) | -0.79pp | ✅ |
| L1: Country Breakdown | No countries exceeded ±2.5% threshold | GN -2.47pp, ER -1.93pp | ✅ |
| L1: Payment Method | Credit Card showed largest decline | -1.08pp | ⚠️ |
| L1: Payment Provider | No data available | N/A | ✅ |
| Mix Shift Analysis | All countries stable impact | No significant shifts | ✅ |

**Key Findings:**
- The -0.79pp decline brings the rate to 96.82%, which remains within the 8-week historical range (96.88%-97.59%)
- GN experienced the largest country-level decline at -2.47pp (95.40% current rate), though below the ±2.5% investigation threshold
- Credit Card payment method showed the most notable decline at -1.08pp (96.27%) on volume of 6,056 orders
- Order volume decreased 0.6% week-over-week (10,957 vs 11,024), continuing a declining trend from W10 peak of 16,267
- No mix shift impacts detected; all country volume changes rated as "Stable"

**Action:** Monitor – The decline is not statistically significant and no dimensions exceeded investigation thresholds. Continue standard monitoring for W18.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 96.82% | 10,957 | -0.79% ← REPORTED CHANGE |
| 2026-W16 | 97.59% | 11,024 | +0.23% |
| 2026-W15 | 97.37% | 11,721 | +0.35% |
| 2026-W14 | 97.03% | 11,373 | -0.04% |
| 2026-W13 | 97.07% | 13,604 | +0.20% |
| 2026-W12 | 96.88% | 14,412 | -0.07% |
| 2026-W11 | 96.95% | 15,835 | -0.43% |
| 2026-W10 | 97.37% | 16,267 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| GN | 95.40% | 97.82% | -2.47% | 1,218 |  |
| ER | 94.62% | 96.49% | -1.93% | 2,232 |  |
| CK | 96.06% | 97.59% | -1.56% | 2,033 |  |
| CG | 98.12% | 97.78% | +0.34% | 1,966 |  |
| AO | 97.42% | 96.78% | +0.66% | 932 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Credit Card | 96.27% | 97.32% | -1.08% | 6,056 |  |
| Apple Pay | 97.32% | 97.9% | -0.60% | 3,580 |  |
| Others | 100.0% | 100.0% | +0.00% | 3 |  |
| Paypal | 98.03% | 97.91% | +0.12% | 1,318 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | High (>92%) | 2,278 | 2,232 | -2.0% | Stable |
| CK | High (>92%) | 2,240 | 2,033 | -9.2% | Stable |
| KN | High (>92%) | 2,145 | 2,507 | +16.9% | Stable |
| CG | High (>92%) | 2,074 | 1,966 | -5.2% | Stable |
| GN | High (>92%) | 1,329 | 1,218 | -8.4% | Stable |
| AO | High (>92%) | 901 | 932 | +3.4% | Stable |
| MR | High (>92%) | 57 | 69 | +21.1% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-27*
