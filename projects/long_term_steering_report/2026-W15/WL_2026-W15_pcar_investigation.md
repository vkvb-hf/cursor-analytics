# PCAR Investigation: WL 2026-W15

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 97.37% → 97.59% (+0.23%)  
**Volume:** 11,024 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate improved by +0.23pp (97.37% → 97.59%) in 2026-W15, representing a statistically non-significant increase on 11,024 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Stable upward trend | +0.23pp | ✅ |
| L1: Country Breakdown | No country exceeded ±2.5% threshold | Max: MR -1.42pp | ✅ |
| L1: Payment Method | All methods stable | Apple Pay +0.71pp | ✅ |
| Mix Shift Analysis | MR volume dropped 90.2% | Low-volume impact | ⚠️ |

**Key Findings:**
- The +0.23pp improvement continues a positive trend, with rates increasing from 96.88% (W12) to 97.59% (W16) over the past 5 weeks
- MR experienced a significant volume collapse (-90.2%, from 692 to 68 orders) alongside a -1.42pp rate decline, though absolute impact is minimal due to low volume
- ER showed the strongest country-level improvement at +1.37pp (94.88% → 96.18%) on 2,433 orders
- Apple Pay approval rate improved by +0.71pp (96.65% → 97.34%), outperforming other payment methods
- No countries or dimensions exceeded the ±2.5% threshold requiring deep-dive investigation

**Action:** Monitor — The improvement is not statistically significant and no dimensions breach alert thresholds. Continue tracking MR volume recovery in subsequent weeks.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 97.59% | 11,024 | +0.23% |
| 2026-W15 | 97.37% | 11,721 | +0.35% ← REPORTED CHANGE |
| 2026-W14 | 97.03% | 11,373 | -0.04% |
| 2026-W13 | 97.07% | 13,604 | +0.20% |
| 2026-W12 | 96.88% | 14,412 | -0.07% |
| 2026-W11 | 96.95% | 15,835 | -0.43% |
| 2026-W10 | 97.37% | 16,267 | +0.03% |
| 2026-W09 | 97.34% | 15,555 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| MR | 95.59% | 96.97% | -1.42% | 68 |  |
| AO | 97.39% | 97.65% | -0.27% | 804 |  |
| KN | 98.56% | 98.48% | +0.08% | 2,562 |  |
| CK | 96.99% | 96.91% | +0.08% | 2,491 |  |
| CG | 97.83% | 97.74% | +0.10% | 2,029 |  |
| ER | 96.18% | 94.88% | +1.37% | 2,433 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Paypal | 98.12% | 98.13% | -0.01% | 1,327 |  |
| Others | 100.0% | 100.0% | +0.00% | 1 |  |
| Credit Card | 97.24% | 97.0% | +0.24% | 6,522 |  |
| Apple Pay | 97.34% | 96.65% | +0.71% | 3,871 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| CK | High (>92%) | 2,426 | 2,491 | +2.7% | Stable |
| ER | High (>92%) | 2,344 | 2,433 | +3.8% | Stable |
| KN | High (>92%) | 2,100 | 2,562 | +22.0% | Stable |
| CG | High (>92%) | 2,031 | 2,029 | -0.1% | Stable |
| GN | High (>92%) | 1,013 | 1,334 | +31.7% | Stable |
| AO | High (>92%) | 767 | 804 | +4.8% | Stable |
| MR | High (>92%) | 692 | 68 | -90.2% | ⚠️ Major mix shift |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
