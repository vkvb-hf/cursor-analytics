# PCAR Investigation: WL 2026-W15

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 97.03% → 97.37% (+0.35%)  
**Volume:** 11,721 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate improved from 97.03% to 97.37% (+0.34 pp) in WL 2026-W15, a statistically non-significant change within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | Rate within 8-week range (96.86%-97.37%) | +0.34 pp | ✅ |
| L1: Country Breakdown | No countries exceeding ±2.5% threshold | All <2.5 pp | ✅ |
| L1: Payment Method | All methods stable, Apple Pay strongest gain | +0.71 pp max | ✅ |
| L1: Payment Provider | No anomalies detected | N/A | ✅ |
| Mix Shift Analysis | Volume shifts stable across all tiers | No impact | ✅ |

**Key Findings:**
- The +0.34 pp improvement returns the approval rate to 97.37%, matching the 8-week high from W10
- All four countries showed positive movement: AO (+2.17 pp), MR (+1.45 pp), ER (+1.23 pp), GN (+1.07 pp)
- Apple Pay showed the strongest payment method improvement at +0.71 pp (96.65% → 97.34%)
- Volume declined 3% week-over-week (11,373 → 11,721 orders), continuing a downward trend from W08 peak of 16,585
- AO experienced a notable -12.0% volume decline but maintained stable approval rate performance

**Action:** Monitor — No investigation required. The metric shows healthy improvement within normal variance, with no countries or dimensions exceeding alert thresholds.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 97.37% | 11,721 | +0.35% ← REPORTED CHANGE |
| 2026-W14 | 97.03% | 11,373 | -0.04% |
| 2026-W13 | 97.07% | 13,604 | +0.20% |
| 2026-W12 | 96.88% | 14,412 | -0.07% |
| 2026-W11 | 96.95% | 15,835 | -0.43% |
| 2026-W10 | 97.37% | 16,267 | +0.03% |
| 2026-W09 | 97.34% | 15,555 | +0.50% |
| 2026-W08 | 96.86% | 16,585 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| GN | 93.32% | 92.33% | +1.07% | 13,110 |  |
| ER | 90.32% | 89.22% | +1.23% | 68,811 |  |
| MR | 81.41% | 80.25% | +1.45% | 19,468 |  |
| AO | 87.06% | 85.21% | +2.17% | 13,883 |  |

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
| ER | Medium (>85%) | 67,730 | 68,811 | +1.6% | Stable |
| CG | High (>92%) | 44,581 | 43,937 | -1.4% | Stable |
| CK | High (>92%) | 42,176 | 42,398 | +0.5% | Stable |
| MR | Low (>85%) | 20,784 | 19,468 | -6.3% | Stable |
| AO | Medium (>85%) | 15,776 | 13,883 | -12.0% | Stable |
| GN | High (>92%) | 14,333 | 13,110 | -8.5% | Stable |
| KN | Medium (>85%) | 11,048 | 10,259 | -7.1% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-17*
