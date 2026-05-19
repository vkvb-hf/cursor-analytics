# Reactivation Investigation: US-HF 2026-W20

**Metric:** Reactivation Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 90.74% → 90.2% (-0.60%)  
**Volume:** 14,787 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Reactivation Rate declined by -0.54pp (90.74% → 90.2%) in US-HF for 2026-W20, with 14,787 orders processed; this change is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Trend | Within normal 8-week range (89.71%-90.99%) | -0.54pp | ✅ |
| L1: Country | No countries exceed ±2.5% threshold | -0.59% | ✅ |
| L1: PaymentMethod | All methods within normal range | -0.65% max (Credit Card) | ✅ |
| Mix Shift | US Medium tier stable despite -15.2% volume drop | Stable | ✅ |

**Key Findings:**
- The -0.54pp decline is within normal weekly fluctuation, with the 8-week range spanning 89.71% to 90.99%
- Volume decreased significantly by 15.2% (17,431 → 14,787 orders) compared to 2026-W19, but mix shift impact remains stable
- Credit Card payments showed the largest decline at -0.65% (91.14% → 90.55%), representing 69% of total volume (10,230 orders)
- Apple Pay was the only payment method showing improvement at +0.31% (85.82% → 86.08%)
- No dimensional segments exceeded the ±2.5% investigation threshold

**Action:** Monitor – No immediate action required. The decline is not statistically significant and falls within normal weekly variance. Continue standard monitoring in 2026-W21.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W20 | 90.2% | 14,787 | -0.60% ← REPORTED CHANGE |
| 2026-W19 | 90.74% | 17,431 | +0.11% |
| 2026-W18 | 90.64% | 13,634 | +1.04% |
| 2026-W17 | 89.71% | 15,063 | -0.40% |
| 2026-W16 | 90.07% | 18,897 | -0.44% |
| 2026-W15 | 90.47% | 21,155 | -0.57% |
| 2026-W14 | 90.99% | 14,736 | +0.40% |
| 2026-W13 | 90.63% | 15,928 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 90.20% | 90.74% | -0.59% | 14,787 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 75.0% | nan% | +nan% | 4 |  |
| Credit Card | 90.55% | 91.14% | -0.65% | 10,230 |  |
| Paypal | 93.15% | 93.67% | -0.56% | 2,160 |  |
| Apple Pay | 86.08% | 85.82% | +0.31% | 2,393 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 17,431 | 14,787 | -15.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-19*
