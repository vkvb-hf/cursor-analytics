# AR Initial (LL0) Investigation: HF-NA 2026-W15

**Metric:** AR Initial (LL0)  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 89.74% → 90.03% (+0.32%)  
**Volume:** 17,357 orders

## Executive Summary

## Executive Summary

**Overall:** AR Initial (LL0) improved from 89.74% to 90.03% (+0.29 pp), continuing a two-week upward trend and reaching the highest rate in the 8-week observation period.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Rate | +0.29 pp | 89.74% → 90.03% | ✅ |
| L1: Country - US | +0.79 pp | 69.72% → 70.51% | ✅ |
| L1: Country - CA | -0.37 pp | 80.88% → 80.51% | ✅ |
| L1: PaymentMethod | Max Δ: -1.70 pp (Others) | Within threshold | ✅ |
| L1: PaymentProvider | Max Δ: -1.92 pp (Unknown) | Within threshold | ✅ |

**Key Findings:**
- US showed meaningful improvement (+0.79 pp) with the largest volume (23,822 orders), driving the overall positive trend
- Credit Card payment method improved +0.67 pp (89.61% → 90.28%) with the highest volume (9,716 orders), contributing significantly to overall gains
- ProcessOut provider improved +0.70 pp (89.75% → 90.45%) across 9,503 orders
- "Others" payment method and "Unknown" provider showed declines (-1.70 pp and -1.92 pp respectively), but low volumes (809 and 655 orders) limited impact
- No countries exceeded the ±2.5% threshold; all changes within normal operating range

**Action:** Monitor — The metric shows healthy improvement with no anomalies requiring investigation. Continue tracking the positive momentum in US and Credit Card performance.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 90.03% | 17,357 | +0.32% ← REPORTED CHANGE |
| 2026-W14 | 89.74% | 17,090 | +0.59% |
| 2026-W13 | 89.21% | 16,158 | -0.54% |
| 2026-W12 | 89.69% | 21,087 | -1.24% |
| 2026-W11 | 90.82% | 21,784 | +1.09% |
| 2026-W10 | 89.84% | 25,446 | +0.25% |
| 2026-W09 | 89.62% | 25,208 | -0.19% |
| 2026-W08 | 89.79% | 25,674 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 80.51% | 80.88% | -0.46% | 7,465 |  |
| US | 70.51% | 69.72% | +1.13% | 23,822 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Others | 97.16% | 98.84% | -1.70% | 809 |
| PaymentMethod | Paypal | 89.8% | 89.96% | -0.18% | 1,402 |
| PaymentMethod | Apple Pay | 88.58% | 88.44% | +0.16% | 5,430 |
| PaymentMethod | Credit Card | 90.28% | 89.61% | +0.76% | 9,716 |
| PaymentProvider | Unknown | 96.49% | 98.38% | -1.92% | 655 |
| PaymentProvider | Adyen | 92.55% | 93.12% | -0.61% | 94 |
| PaymentProvider | No Payment | 100.0% | 100.0% | +0.00% | 131 |
| PaymentProvider | Braintree | 88.64% | 88.61% | +0.04% | 6,974 |
| PaymentProvider | ProcessOut | 90.45% | 89.75% | +0.77% | 9,503 |

---

*Report: 2026-04-14*
