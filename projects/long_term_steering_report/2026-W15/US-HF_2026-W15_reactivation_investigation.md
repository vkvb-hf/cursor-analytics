# Reactivation Investigation: US-HF 2026-W15

**Metric:** Reactivation  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 90.99% → 90.47% (-0.57%)  
**Volume:** 21,155 orders

## Executive Summary

**Overall:** Reactivation rate declined by -0.57% (from 90.99% to 90.47%) in W15, though this remains within normal weekly fluctuation and the rate stays elevated compared to the 8-week historical range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (85.79%-91.26%) | -0.52pp | ✅ |
| L1: Country Breakdown | No countries exceeding ±2.5% threshold | +0.34pp (US) | ✅ |
| L1: Payment Method | "Others" shows -50pp drop | -50.00pp | ⚠️ |
| L1: Payment Method | Major methods (Credit Card, PayPal, Apple Pay) | -0.45pp to -1.21pp | ✅ |

**Key Findings:**
- W15 volume increased significantly (+43.5%) to 21,155 orders compared to W14's 14,736, which may contribute to rate normalization
- "Others" payment method shows a -50.00pp decline (100.0% → 50.0%), but volume is negligible at only 4 orders
- PayPal experienced the largest decline among major payment methods at -1.21pp (93.68% → 92.55%) with 3,369 orders
- Despite the weekly decline, current rate of 90.47% remains well above the 8-week low of 85.79% (W09)
- US country-level performance actually improved slightly (+0.34pp), suggesting the decline is not geography-driven

**Action:** Monitor – The decline is minor, within normal fluctuation, and driven primarily by a negligible-volume payment method. No significant country or major payment method issues identified.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 90.47% | 21,155 | -0.57% ← REPORTED CHANGE |
| 2026-W14 | 90.99% | 14,736 | +0.40% |
| 2026-W13 | 90.63% | 15,928 | -0.69% |
| 2026-W12 | 91.26% | 15,787 | +2.56% |
| 2026-W11 | 88.98% | 17,703 | +1.39% |
| 2026-W10 | 87.76% | 22,710 | +2.30% |
| 2026-W09 | 85.79% | 18,047 | -0.06% |
| 2026-W08 | 85.84% | 18,573 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 93.1% | 92.78% | +0.34% | 492,811 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Others | 50.0% | 100.0% | -50.00% | 4 |
| PaymentMethod | Paypal | 92.55% | 93.68% | -1.21% | 3,369 |
| PaymentMethod | Apple Pay | 86.77% | 87.25% | -0.55% | 3,197 |
| PaymentMethod | Credit Card | 90.81% | 91.21% | -0.45% | 14,585 |

---

*Report: 2026-04-14*
