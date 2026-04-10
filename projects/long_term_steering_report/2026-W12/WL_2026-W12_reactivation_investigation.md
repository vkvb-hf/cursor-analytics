# Reactivation Investigation: WL 2026-W12

**Metric:** Reactivation  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 88.71% → 88.67% (-0.05%)  
**Volume:** 7,706 orders

## Executive Summary

**Overall:** Reactivation rate declined marginally from 88.71% to 88.67% (-0.04 pp), representing a minor fluctuation within normal operating range on a volume of 7,706 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (85.07%-89.15%) | -0.04 pp | ✅ |
| L1: Country Breakdown | No country exceeds ±2.5% threshold | Max: MR -1.38 pp | ✅ |
| L1: Dimension Scan | PaymentMethod "Others" shows -33.33 pp drop | Low volume (6 orders) | ⚠️ |

**Key Findings:**
- The -0.04 pp decline is negligible and consistent with week-over-week volatility observed in the 8-week trend (range: -0.49 pp to +1.91 pp)
- MR shows the largest country decline at -1.38 pp (80.0% vs 81.12%) but remains below the ±2.5% investigation threshold
- PaymentMethod "Others" dropped -33.33 pp, but this is statistically insignificant with only 6 orders
- Credit Card payments (highest volume at 5,581 orders) improved +2.38 pp to 89.7%, providing a positive offset
- Overall 8-week trend shows improvement from 85.09% (W07) to 88.67% (W14), indicating healthy metric trajectory

**Action:** Monitor – No investigation required. The decline is minimal, no country breaches the ±2.5% threshold, and the dimension anomaly (PaymentMethod "Others") lacks sufficient volume for concern.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 88.67% | 7,706 | -0.05% |
| 2026-W13 | 88.71% | 7,954 | -0.49% |
| 2026-W12 | 89.15% | 7,658 | +1.89% ← REPORTED CHANGE |
| 2026-W11 | 87.5% | 9,145 | +1.91% |
| 2026-W10 | 85.86% | 9,675 | -0.12% |
| 2026-W09 | 85.96% | 7,581 | +1.05% |
| 2026-W08 | 85.07% | 8,046 | -0.02% |
| 2026-W07 | 85.09% | 8,553 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| MR | 80.0% | 81.12% | -1.38% | 18,070 |  |
| KN | 87.76% | 88.93% | -1.31% | 10,617 |  |
| GN | 93.64% | 94.18% | -0.57% | 16,164 |  |
| CK | 93.33% | 93.63% | -0.32% | 42,397 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Others | 66.67% | 100.0% | -33.33% | 6 |
| PaymentMethod | Apple Pay | 73.98% | 73.22% | +1.04% | 588 |
| PaymentMethod | Paypal | 93.19% | 92.15% | +1.13% | 1,483 |
| PaymentMethod | Credit Card | 89.7% | 87.61% | +2.38% | 5,581 |

---

*Report: 2026-04-10*
