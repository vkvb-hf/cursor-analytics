# PCAR Investigation: WL 2026-W20

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 95.28% → 95.62% (+0.36%)  
**Volume:** 10,330 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate improved by +0.36 pp (95.28% → 95.62%) on 10,330 orders in WL 2026-W20, though this change is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate recovering from W17-W19 decline | +0.36 pp | ⚠️ |
| L1: Country Breakdown | No countries exceeded ±2.5% threshold | Max: ER +1.48 pp | ✅ |
| L1: Payment Method | Credit Card improved, Apple Pay stable | CC +0.68 pp | ✅ |
| Mix Shift Analysis | All countries stable impact | No adverse shifts | ✅ |

**Key Findings:**
- The +0.36 pp improvement represents a partial recovery after three consecutive weeks of decline (W17: 97.02% → W19: 95.28%, cumulative -1.74 pp)
- ER showed the strongest improvement at +1.48 pp (91.88% → 93.23%) on 1,714 orders, though remains the lowest-performing country
- CK was the only country to decline, dropping -0.81 pp (94.57% → 93.80%) on 2,145 orders
- Credit Card payments improved +0.68 pp (93.90% → 94.54%) representing the largest payment method segment at 5,674 orders
- Overall volume declined -1.4% (10,480 → 10,330), continuing a downward trend from W13 (13,605)

**Action:** Monitor — The improvement is not statistically significant and the rate (95.62%) remains well below the W13-W16 baseline (~97%). Continue tracking to confirm recovery trend stabilizes.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W20 | 95.62% | 10,330 | +0.36% ← REPORTED CHANGE |
| 2026-W19 | 95.28% | 10,480 | -0.77% |
| 2026-W18 | 96.02% | 10,753 | -1.03% |
| 2026-W17 | 97.02% | 10,957 | -0.58% |
| 2026-W16 | 97.59% | 11,025 | +0.23% |
| 2026-W15 | 97.37% | 11,722 | +0.35% |
| 2026-W14 | 97.03% | 11,373 | -0.04% |
| 2026-W13 | 97.07% | 13,605 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CK | 93.80% | 94.57% | -0.81% | 2,145 |  |
| KN | 97.00% | 96.46% | +0.57% | 2,604 |  |
| AO | 95.80% | 95.21% | +0.62% | 762 |  |
| ER | 93.23% | 91.88% | +1.48% | 1,714 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | nan% | 100.0% | +nan% | 0 |  |
| Apple Pay | 96.71% | 96.82% | -0.12% | 3,342 |  |
| Paypal | 97.56% | 97.42% | +0.15% | 1,314 |  |
| Credit Card | 94.54% | 93.9% | +0.68% | 5,674 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| KN | High (>92%) | 2,457 | 2,604 | +6.0% | Stable |
| CK | High (>92%) | 2,300 | 2,145 | -6.7% | Stable |
| ER | Medium (>85%) | 1,945 | 1,714 | -11.9% | Stable |
| CG | High (>92%) | 1,791 | 1,785 | -0.3% | Stable |
| GN | High (>92%) | 1,250 | 1,234 | -1.3% | Stable |
| AO | High (>92%) | 647 | 762 | +17.8% | Stable |
| MR | High (>92%) | 90 | 86 | -4.4% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-19*
