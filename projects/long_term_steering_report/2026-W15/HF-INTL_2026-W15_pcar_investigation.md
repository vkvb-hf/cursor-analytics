# PCAR Investigation: HF-INTL 2026-W15

**Metric:** PCAR  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 96.0% → 96.12% (+0.13%)  
**Volume:** 36,514 orders

## Executive Summary

**Overall:** PCAR improved by +0.13 percentage points (96.0% → 96.12%) on a volume of 36,514 orders in 2026-W15, representing a modest recovery after the -1.52pp decline observed in W13.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal variance | +0.13pp | ✅ |
| L1: Country Breakdown | 2 countries exceed ±2.5% threshold (AT, DK) | +2.94pp / +3.94pp | ⚠️ |
| L1: Payment Method | No significant anomalies detected | -0.13pp to +1.83pp | ✅ |

**Key Findings:**
- DK showed the largest positive movement at +3.94pp (94.03% → 97.74%) on 37,713 orders, contributing significantly to the overall improvement
- AT improved by +2.94pp (92.79% → 95.52%) on 13,962 orders, exceeding the ±2.5% threshold
- Volume decreased by 26% compared to W11 peak (36,514 vs 42,932), continuing a multi-week volume decline trend
- "Others" payment method remains a concern at 76.47% rate despite +1.83pp improvement, significantly underperforming other payment methods (97-98% range)
- The current rate (96.12%) remains below the 8-week high of 97.31% achieved in W10

**Action:** Monitor – The improvement is positive but modest. Continue tracking DK and AT for sustained performance, and investigate the low conversion rate for "Others" payment method if volume increases.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 96.12% | 36,514 | +0.13% ← REPORTED CHANGE |
| 2026-W14 | 96.0% | 31,465 | +0.83% |
| 2026-W13 | 95.21% | 39,598 | -1.52% |
| 2026-W12 | 96.68% | 38,136 | -0.53% |
| 2026-W11 | 97.2% | 42,932 | -0.11% |
| 2026-W10 | 97.31% | 44,946 | +0.80% |
| 2026-W09 | 96.54% | 48,662 | +0.04% |
| 2026-W08 | 96.5% | 49,249 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| DE | 97.33% | 96.44% | +0.93% | 201,519 |  |
| GB | 94.14% | 93.07% | +1.15% | 185,598 |  |
| FR | 94.49% | 92.95% | +1.66% | 147,984 |  |
| IE | 91.93% | 90.41% | +1.67% | 17,513 |  |
| AT | 95.52% | 92.79% | +2.94% | 13,962 | ⚠️ |
| DK | 97.74% | 94.03% | +3.94% | 37,713 | ⚠️ |

**Countries exceeding ±2.5% threshold:** AT, DK

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Unknown | nan% | nan% | +nan% | 0 |
| PaymentMethod | Apple Pay | 98.03% | 98.16% | -0.13% | 12,006 |
| PaymentMethod | Credit Card | 98.22% | 98.2% | +0.03% | 13,439 |
| PaymentMethod | Paypal | 97.96% | 97.76% | +0.20% | 7,741 |
| PaymentMethod | Others | 76.47% | 75.1% | +1.83% | 3,328 |

---

*Report: 2026-04-14*
