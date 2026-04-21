# PCAR Investigation: HF-INTL 2026-W16

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 96.12% → 97.13% (+1.05%)  
**Volume:** 37,314 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate for HF-INTL improved significantly from 96.12% to 97.13% (+1.01 pp) in 2026-W16, recovering toward the 97.31% level observed in W10.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate increased after W13-W15 dip | +1.05% | ✅ |
| L1: Country Breakdown | No countries exceeded ±2.5% threshold | Mixed | ✅ |
| L1: PaymentMethod | "Others" method shows +7.20% improvement | +7.20% | ⚠️ |
| Mix Shift | All countries stable; SE (+22.1%) and NO (+27.4%) volume growth | Stable | ✅ |

**Key Findings:**
- The +1.01 pp rate improvement represents a recovery from the W13 trough (95.21%), bringing performance closer to the 8-week high of 97.31% (W10)
- "Others" payment method showed the largest improvement at +7.20 pp (76.47% → 81.98%), though volume remains low at 2,242 orders
- NO experienced a -2.03 pp rate decline (91.0% → 89.15%) while simultaneously seeing +27.4% volume growth, which warrants monitoring
- SE saw strong volume growth (+22.1%) with a +1.19 pp rate improvement (95.19% → 96.32%)
- Core payment methods (Credit Card, Apple Pay, Paypal) remained stable with rates above 97.8%

**Action:** Monitor — The improvement is positive and no countries exceeded the ±2.5% threshold. Continue tracking NO performance given the rate decline combined with volume surge.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 97.13% | 37,314 | +1.05% ← REPORTED CHANGE |
| 2026-W15 | 96.12% | 36,514 | +0.13% |
| 2026-W14 | 96.0% | 31,465 | +0.83% |
| 2026-W13 | 95.21% | 39,598 | -1.52% |
| 2026-W12 | 96.68% | 38,136 | -0.53% |
| 2026-W11 | 97.2% | 42,932 | -0.11% |
| 2026-W10 | 97.31% | 44,946 | +0.80% |
| 2026-W09 | 96.54% | 48,662 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| NO | 89.15% | 91.0% | -2.03% | 24,045 |  |
| GB | 93.92% | 94.14% | -0.23% | 209,202 |  |
| BE | 96.24% | 95.51% | +0.76% | 64,642 |  |
| LU | 95.9% | 95.06% | +0.88% | 3,510 |  |
| SE | 96.32% | 95.19% | +1.19% | 38,861 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Apple Pay | 97.95% | 98.03% | -0.08% | 12,654 |  |
| Paypal | 97.89% | 97.96% | -0.07% | 8,335 |  |
| Credit Card | 98.36% | 98.22% | +0.14% | 14,083 |  |
| Others | 81.98% | 76.47% | +7.20% | 2,242 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| DE | High (>92%) | 201,519 | 224,251 | +11.3% | Stable |
| GB | High (>92%) | 185,598 | 209,202 | +12.7% | Stable |
| FR | High (>92%) | 147,984 | 145,977 | -1.4% | Stable |
| NL | High (>92%) | 110,805 | 109,008 | -1.6% | Stable |
| AU | Medium (>85%) | 85,229 | 89,760 | +5.3% | Stable |
| BE | High (>92%) | 64,439 | 64,642 | +0.3% | Stable |
| DK | High (>92%) | 37,713 | 40,108 | +6.4% | Stable |
| SE | High (>92%) | 31,821 | 38,861 | +22.1% | Stable |
| NO | Medium (>85%) | 18,868 | 24,045 | +27.4% | Stable |
| IE | Medium (>85%) | 17,513 | 18,708 | +6.8% | Stable |
| NZ | Medium (>85%) | 16,941 | 18,117 | +6.9% | Stable |
| AT | High (>92%) | 13,962 | 14,079 | +0.8% | Stable |
| LU | High (>92%) | 2,731 | 3,510 | +28.5% | Stable |
| CH | High (>92%) | 2,101 | 2,299 | +9.4% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-21*
