# Reactivation Investigation: WL 2026-W13

**Metric:** Reactivation  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 88.71% → 88.67% (-0.05%)  
**Volume:** 7,706 orders

## Executive Summary

**Overall:** Reactivation rate experienced a marginal decline of -0.05pp (88.71% → 88.67%) in W13, representing a minor fluctuation within normal operating parameters on a volume of 7,706 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Sustained pattern or anomaly? | -0.05pp | ✅ Minor dip following strong 2-week gains (+1.89pp, +1.91pp) |
| L1: Country | Any country Δ > ±2.5%? | Max: +0.88pp (CK) | ✅ All countries within threshold |
| L1: Dimension | Any dimension Δ > ±2.5%? | Max: -1.91pp (Apple Pay) | ✅ No significant dimension anomalies |

**Key Findings:**
- The -0.05pp decline is negligible and follows two consecutive weeks of strong improvement (W11: +1.91pp, W12: +1.89pp), indicating a natural stabilization
- No countries exceeded the ±2.5% threshold; KN showed the largest decline at -0.17pp while CK improved by +0.88pp
- Apple Pay showed the most notable payment method decline (-1.91pp) but remains below threshold and represents only 627 orders (8% of volume)
- Overall reactivation rate of 88.67% remains elevated compared to earlier weeks (W07-W10 averaged ~85.5%)
- The "Others" payment method shows +50.00pp change but is statistically insignificant with only 3 orders

**Action:** Monitor — No investigation required. Continue standard monitoring as the decline is within normal variance and no dimensions breach alert thresholds.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 88.67% | 7,706 | -0.05% |
| 2026-W13 | 88.71% | 7,954 | -0.49% ← REPORTED CHANGE |
| 2026-W12 | 89.15% | 7,658 | +1.89% |
| 2026-W11 | 87.5% | 9,145 | +1.91% |
| 2026-W10 | 85.86% | 9,675 | -0.12% |
| 2026-W09 | 85.96% | 7,581 | +1.05% |
| 2026-W08 | 85.07% | 8,046 | -0.02% |
| 2026-W07 | 85.09% | 8,553 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| KN | 87.61% | 87.76% | -0.17% | 10,365 |  |
| CG | 96.76% | 96.84% | -0.08% | 44,477 |  |
| ER | 89.92% | 89.54% | +0.43% | 73,655 |  |
| AO | 87.96% | 87.38% | +0.66% | 16,249 |  |
| CK | 94.15% | 93.33% | +0.88% | 42,197 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Apple Pay | 72.57% | 73.98% | -1.91% | 627 |
| PaymentMethod | Paypal | 92.37% | 93.19% | -0.88% | 1,573 |
| PaymentMethod | Credit Card | 89.46% | 89.7% | -0.26% | 5,751 |
| PaymentMethod | Others | 100.0% | 66.67% | +50.00% | 3 |

---

*Report: 2026-04-10*
