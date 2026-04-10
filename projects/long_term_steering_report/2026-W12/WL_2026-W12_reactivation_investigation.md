# Reactivation Investigation: WL 2026-W12

**Metric:** Reactivation  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 88.71% → 88.67% (-0.05%)  
**Volume:** 7,706 orders

## Executive Summary

**Overall:** Reactivation declined marginally from 88.71% to 88.67% (-0.05pp), representing a minimal week-over-week decrease on 7,706 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL Trend | 8-week stability | -0.05pp | ✅ Within normal variance; rate remains elevated vs W07-W10 baseline (~85-86%) |
| L1: Country | ±2.5% threshold | None exceeded | ✅ All countries within acceptable range (MR -1.38pp largest decline) |
| L1: Dimension | Payment anomalies | -33.33pp Others | ⚠️ "Others" payment method dropped significantly but volume only 6 orders |

**Key Findings:**
- The -0.05pp decline is statistically insignificant and within normal weekly fluctuation
- Current rate (88.67%) remains +3.58pp above the 8-week low of 85.09% (W07), indicating sustained improvement
- All four countries showed slight declines: MR (-1.38pp), KN (-1.31pp), GN (-0.57pp), CK (-0.32pp), but none breached the ±2.5% threshold
- "Others" payment method dropped from 100% to 66.67% (-33.33pp), but with only 6 orders this is not material
- Credit Card (+2.38pp to 89.7%) and PayPal (+1.13pp to 93.19%) both improved, offsetting declines in lower-volume payment methods

**Action:** Monitor — No investigation required. The decline is minimal and the metric remains healthy compared to historical performance.

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
