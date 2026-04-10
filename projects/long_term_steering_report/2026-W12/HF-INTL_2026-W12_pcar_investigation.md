# PCAR Investigation: HF-INTL 2026-W12

**Metric:** PCAR  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 95.21% → 96.0% (+0.83%)  
**Volume:** 31,465 orders

## Executive Summary

**Overall:** PCAR improved by +0.83pp (from 95.21% to 96.0%) in 2026-W12 with a volume of 31,465 orders, partially recovering from the prior week's decline.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Sustained decline pattern | -0.98pp from W07 baseline (96.98%) | ⚠️ |
| L1: Country Breakdown | Any country ≥±2.5% threshold | None exceeded threshold | ✅ |
| L1: Dimension Scan | PaymentMethod anomalies | Others at -2.37pp (84.74%) | ⚠️ |

**Key Findings:**
- NO showed the largest country decline at -1.70pp (89.86% vs 91.42%) with significant volume of 26,830 orders
- IE also underperformed with -1.39pp decline (90.41% vs 91.69%) on 18,858 orders
- PaymentMethod "Others" dropped -2.37pp to 84.74%, approaching the investigation threshold
- GB represents the highest volume (230,971 orders) with a moderate decline of -0.53pp
- Volume has decreased substantially from W07 (48,803) to W14 (31,465), a ~35% reduction

**Action:** Monitor - While the week-over-week metric improved, continue monitoring NO and IE country performance and the "Others" payment method which is trending toward the ±2.5% threshold.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 96.0% | 31,465 | +0.83% |
| 2026-W13 | 95.21% | 39,598 | -1.52% |
| 2026-W12 | 96.68% | 38,136 | -0.53% ← REPORTED CHANGE |
| 2026-W11 | 97.2% | 42,932 | -0.11% |
| 2026-W10 | 97.31% | 44,946 | +0.80% |
| 2026-W09 | 96.54% | 48,662 | +0.04% |
| 2026-W08 | 96.5% | 49,249 | -0.49% |
| 2026-W07 | 96.98% | 48,803 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| NO | 89.86% | 91.42% | -1.70% | 26,830 |  |
| LU | 95.2% | 96.65% | -1.49% | 3,667 |  |
| IE | 90.41% | 91.69% | -1.39% | 18,858 |  |
| CH | 93.37% | 94.44% | -1.13% | 2,399 |  |
| SE | 96.27% | 96.89% | -0.64% | 41,014 |  |
| GB | 93.58% | 94.09% | -0.53% | 230,971 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Unknown | nan% | nan% | +nan% | 0 |
| PaymentMethod | Others | 84.74% | 86.8% | -2.37% | 2,772 |
| PaymentMethod | Apple Pay | 97.53% | 98.13% | -0.62% | 12,214 |
| PaymentMethod | Paypal | 97.45% | 97.79% | -0.34% | 8,483 |
| PaymentMethod | Credit Card | 97.78% | 97.79% | +0.00% | 14,667 |

---

*Report: 2026-04-10*
