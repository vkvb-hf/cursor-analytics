# PCAR Investigation: WL 2026-W16

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 97.37% → 97.59% (+0.23%)  
**Volume:** 11,024 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate improved by +0.23 percentage points (97.37% → 97.59%) on 11,024 orders in W16, though this change is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Stable upward trend | +0.23 pp | ✅ |
| L1: Country Breakdown | No country exceeded ±2.5% threshold | Max: -1.06 pp (KN) | ✅ |
| L1: Payment Method | All methods within normal range | -0.21 pp to +0.58 pp | ✅ |
| Mix Shift | Volume shifts stable across tiers | GN +17.8% vol (High AR tier) | ✅ |

**Key Findings:**
- The +0.23 pp improvement continues a two-week positive trend (+0.35 pp in W15, +0.23 pp in W16), recovering from the W14 low of 97.03%
- KN showed the largest rate decline at -1.06 pp (88.75% → 87.81%), but remains well below the ±2.5% investigation threshold
- Apple Pay showed the strongest payment method improvement at +0.58 pp (97.34% → 97.90%), while PayPal declined slightly by -0.21 pp
- GN experienced significant volume growth (+17.8%) while maintaining a high approval rate tier (94.19%), contributing positively to the overall metric
- Overall order volume decreased by 6% (11,721 → 11,024), continuing a declining trend from the W11 peak of 15,835

**Action:** Monitor – No significant anomalies detected; continue standard weekly review.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 97.59% | 11,024 | +0.23% ← REPORTED CHANGE |
| 2026-W15 | 97.37% | 11,721 | +0.35% |
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
| KN | 87.81% | 88.75% | -1.06% | 11,057 |  |
| MR | 80.82% | 81.37% | -0.68% | 18,584 |  |
| CK | 93.32% | 93.91% | -0.63% | 43,017 |  |
| AO | 87.79% | 87.06% | +0.83% | 14,640 |  |
| GN | 94.19% | 93.32% | +0.94% | 15,445 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Paypal | 97.91% | 98.12% | -0.21% | 1,291 |  |
| Others | 100.0% | 100.0% | +0.00% | 1 |  |
| Credit Card | 97.32% | 97.24% | +0.08% | 5,966 |  |
| Apple Pay | 97.9% | 97.34% | +0.58% | 3,766 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 68,811 | 69,808 | +1.4% | Stable |
| CG | High (>92%) | 43,937 | 42,996 | -2.1% | Stable |
| CK | High (>92%) | 42,398 | 43,017 | +1.5% | Stable |
| MR | Low (>85%) | 19,468 | 18,584 | -4.5% | Stable |
| AO | Medium (>85%) | 13,883 | 14,640 | +5.5% | Stable |
| GN | High (>92%) | 13,110 | 15,445 | +17.8% | Stable |
| KN | Medium (>85%) | 10,259 | 11,057 | +7.8% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-21*
