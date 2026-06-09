# PCAR Investigation: WL 2026-W23

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 97.04% → 96.88% (-0.16%)  
**Volume:** 8,467 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate declined slightly from 97.04% to 96.88% (-0.16pp) in W23, a statistically non-significant change within normal operating variance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (95.28%-97.59%) | -0.16pp | ✅ |
| L1: Country Breakdown | No country exceeded ±2.5% threshold | Max: ER -1.48pp | ✅ |
| L1: Payment Method | All methods stable | Max: Paypal -0.48pp | ✅ |
| Mix Shift Analysis | KN volume dropped 66.1% | High-AR tier shift | ⚠️ |

**Key Findings:**
- The -0.16pp decline is not statistically significant and falls within the 8-week range of 95.28%-97.59%
- ER showed the largest country-level decline at -1.48pp (93.18% vs 94.58%), but remains below the ±2.5% investigation threshold
- KN experienced a major volume drop of 66.1% (2,655 → 900 orders), though this high-AR tier country actually improved its rate by +0.91pp
- Overall volume decreased 18.5% WoW (10,391 → 8,467 orders), driven primarily by the KN volume reduction
- All payment methods remained stable with changes under 0.5pp

**Action:** Monitor — No immediate investigation required. Continue standard monitoring with attention to KN volume recovery and ER rate trajectory over the next 1-2 weeks.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W23 | 96.88% | 8,467 | -0.16% ← REPORTED CHANGE |
| 2026-W22 | 97.04% | 10,391 | +0.19% |
| 2026-W21 | 96.86% | 9,450 | +1.30% |
| 2026-W20 | 95.62% | 10,330 | +0.36% |
| 2026-W19 | 95.28% | 10,480 | -0.77% |
| 2026-W18 | 96.02% | 10,753 | -1.03% |
| 2026-W17 | 97.02% | 10,957 | -0.58% |
| 2026-W16 | 97.59% | 11,025 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| ER | 93.18% | 94.58% | -1.48% | 1,730 |  |
| CG | 98.03% | 98.38% | -0.35% | 1,577 |  |
| CK | 97.77% | 96.96% | +0.84% | 2,292 |  |
| KN | 98.78% | 97.89% | +0.91% | 900 |  |
| MR | 99.12% | 97.60% | +1.55% | 113 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | nan% | nan% | +nan% | 0 |  |
| Paypal | 97.35% | 97.82% | -0.48% | 981 |  |
| Apple Pay | 96.4% | 96.67% | -0.28% | 2,611 |  |
| Credit Card | 97.05% | 97.08% | -0.03% | 4,875 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| KN | High (>92%) | 2,655 | 900 | -66.1% | ⚠️ Major mix shift |
| CK | High (>92%) | 2,534 | 2,292 | -9.6% | Stable |
| ER | High (>92%) | 1,698 | 1,730 | +1.9% | Stable |
| CG | High (>92%) | 1,539 | 1,577 | +2.5% | Stable |
| GN | High (>92%) | 1,022 | 1,090 | +6.7% | Stable |
| AO | High (>92%) | 818 | 765 | -6.5% | Stable |
| MR | High (>92%) | 125 | 113 | -9.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-09*
