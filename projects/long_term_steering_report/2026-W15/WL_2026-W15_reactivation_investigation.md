# Reactivation Investigation: WL 2026-W15

**Metric:** Reactivation  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 88.67% → 89.29% (+0.70%)  
**Volume:** 9,277 orders

## Executive Summary

**Overall:** Reactivation rate improved by +0.70% (from 88.67% to 89.29%) in W15, representing the second consecutive week of improvement and reaching the highest rate in the 8-week observation period.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Sustained improvement pattern | +0.70% WoW | ✅ |
| L1: Country Breakdown | All countries within ±2.5% threshold | +1.07% to +2.17% | ✅ |
| L1: Dimension Scan | PaymentMethod "Others" anomaly detected | -66.67% | ⚠️ |

**Key Findings:**
- Reactivation rate at 89.29% is the highest in 8 weeks, with volume up 20% WoW (9,277 vs 7,706 orders)
- All four countries (GN, ER, MR, AO) showed positive movement ranging from +1.07% to +2.17%, with AO leading at +2.17%
- PaymentMethod "Others" dropped dramatically from 100.0% to 33.33% (-66.67%), though volume is minimal (3 orders)
- Apple Pay showed the strongest improvement among meaningful payment methods at +3.99% (72.06% → 74.94%)
- Credit Card (largest volume at 6,638 orders) and PayPal both showed stable, modest improvements (+0.38% and +0.39% respectively)

**Action:** Monitor — The metric is trending positively with healthy improvements across all countries and major payment methods. The PaymentMethod "Others" decline is statistically insignificant due to low volume (3 orders) and does not warrant investigation.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 89.29% | 9,277 | +0.70% ← REPORTED CHANGE |
| 2026-W14 | 88.67% | 7,706 | -0.05% |
| 2026-W13 | 88.71% | 7,954 | -0.49% |
| 2026-W12 | 89.15% | 7,658 | +1.89% |
| 2026-W11 | 87.5% | 9,145 | +1.91% |
| 2026-W10 | 85.86% | 9,675 | -0.12% |
| 2026-W09 | 85.96% | 7,581 | +1.05% |
| 2026-W08 | 85.07% | 8,046 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| GN | 93.32% | 92.33% | +1.07% | 13,110 |  |
| ER | 90.33% | 89.22% | +1.23% | 68,811 |  |
| MR | 81.43% | 80.25% | +1.47% | 19,468 |  |
| AO | 87.06% | 85.21% | +2.17% | 13,883 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Others | 33.33% | 100.0% | -66.67% | 3 |
| PaymentMethod | Credit Card | 89.92% | 89.58% | +0.38% | 6,638 |
| PaymentMethod | Paypal | 93.27% | 92.9% | +0.39% | 1,842 |
| PaymentMethod | Apple Pay | 74.94% | 72.06% | +3.99% | 794 |

---

*Report: 2026-04-14*
