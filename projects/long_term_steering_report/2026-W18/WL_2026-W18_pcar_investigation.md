# PCAR Investigation: WL 2026-W18

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 97.02% → 96.02% (-1.03%)  
**Volume:** 10,753 orders  
**Significance:** Significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate declined significantly from 97.02% to 96.02% (-1.00 pp) in W18, representing the largest week-over-week drop in the 8-week observation period.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | WoW change significant? | -1.00 pp | ⚠️ |
| L1: Country Breakdown | Any country >±2.5% threshold? | None exceeded | ✅ |
| L1: Payment Method | Major payment method decline? | Credit Card -1.76 pp | ⚠️ |
| L1: Payment Provider | Provider-specific issues? | No data available | ✅ |
| Mix Shift | Volume redistribution impact? | All countries stable | ✅ |

**Key Findings:**
- Credit Card approval rate dropped from 96.63% to 94.93% (-1.70 pp), affecting 5,995 orders (56% of total volume) — the largest contributor to overall decline
- AO showed the steepest country-level decline at -2.16 pp (95.32% from 97.42%) with a concurrent -17.4% volume drop
- MR declined -2.07 pp despite +24.6% volume increase, though absolute volume remains low (86 orders)
- ER continues to have the lowest approval rate at 93.17% (-1.54 pp) with significant volume (2,137 orders)
- Apple Pay was the only payment method showing improvement (+0.17 pp to 97.48%)

**Action:** Investigate — The Credit Card payment method decline warrants immediate investigation as it impacts the majority of transaction volume. Recommend drilling into Credit Card transactions by country and error codes to identify root cause.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W18 | 96.02% | 10,753 | -1.03% ← REPORTED CHANGE |
| 2026-W17 | 97.02% | 10,957 | -0.58% |
| 2026-W16 | 97.59% | 11,024 | +0.23% |
| 2026-W15 | 97.37% | 11,721 | +0.35% |
| 2026-W14 | 97.03% | 11,373 | -0.04% |
| 2026-W13 | 97.07% | 13,604 | +0.20% |
| 2026-W12 | 96.88% | 14,412 | -0.07% |
| 2026-W11 | 96.95% | 15,835 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| AO | 95.32% | 97.42% | -2.16% | 770 |  |
| MR | 96.51% | 98.55% | -2.07% | 86 |  |
| ER | 93.17% | 94.62% | -1.54% | 2,137 |  |
| KN | 97.55% | 98.80% | -1.27% | 2,534 |  |
| CK | 95.35% | 96.11% | -0.80% | 2,127 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | nan% | 100.0% | +nan% | 0 |  |
| Unknown | nan% | nan% | +nan% | 0 |  |
| Credit Card | 94.93% | 96.63% | -1.76% | 5,995 |  |
| Paypal | 97.16% | 98.03% | -0.89% | 1,266 |  |
| Apple Pay | 97.48% | 97.32% | +0.17% | 3,492 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| KN | High (>92%) | 2,507 | 2,534 | +1.1% | Stable |
| ER | High (>92%) | 2,232 | 2,137 | -4.3% | Stable |
| CK | High (>92%) | 2,033 | 2,127 | +4.6% | Stable |
| CG | High (>92%) | 1,966 | 1,997 | +1.6% | Stable |
| GN | High (>92%) | 1,218 | 1,102 | -9.5% | Stable |
| AO | High (>92%) | 932 | 770 | -17.4% | Stable |
| MR | High (>92%) | 69 | 86 | +24.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-05*
