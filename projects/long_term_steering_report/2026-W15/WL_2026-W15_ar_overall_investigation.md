# AR Overall Investigation: WL 2026-W15

**Metric:** AR Overall  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 89.33% → 90.11% (+0.87%)  
**Volume:** 160,979 orders

## Executive Summary

**Overall:** AR Overall improved from 89.33% to 90.11% (+0.78 pp) in W15, continuing a positive trend observed over the past 8 weeks with rates climbing from 88.14% in W08.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Weekly Trend | Rate increasing consistently since W08 | +0.78 pp | ✅ |
| L1: Country Breakdown | All 4 countries improved; none exceeded ±2.5% threshold | +1.07 to +2.17 pp | ✅ |
| L1: Payment Method | All methods improved slightly | +0.34 to +0.96 pp | ✅ |
| L1: Payment Provider | ProcessOut near threshold; Unknown anomaly | +2.31 pp / +69.73 pp | ⚠️ |

**Key Findings:**
- All four countries (GN, ER, MR, AO) showed improvement, with AO leading at +2.17 pp (85.21% → 87.06%)
- ProcessOut provider improved significantly by +2.31 pp (79.78% → 81.62%) on 17,676 orders, approaching the ±2.5% threshold
- Unknown PaymentProvider shows anomalous +69.73 pp change (57.14% → 96.99%), but low volume (664 orders) limits impact
- Volume decreased by ~4,000 orders (165,018 → 160,979) while rate improved, suggesting potential mix shift
- Credit Card remains the dominant payment method (115,014 orders) with solid +0.96 pp improvement

**Action:** Monitor - The improvement is broad-based across all dimensions with no areas exceeding thresholds. Continue monitoring ProcessOut performance and the Unknown provider anomaly in subsequent weeks.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 90.11% | 160,979 | +0.87% ← REPORTED CHANGE |
| 2026-W14 | 89.33% | 165,018 | -0.43% |
| 2026-W13 | 89.72% | 169,667 | +0.07% |
| 2026-W12 | 89.66% | 169,891 | -0.14% |
| 2026-W11 | 89.79% | 174,933 | +0.80% |
| 2026-W10 | 89.08% | 179,965 | +1.01% |
| 2026-W09 | 88.19% | 180,862 | +0.06% |
| 2026-W08 | 88.14% | 179,647 | - |

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
| PaymentMethod | Apple Pay | 86.04% | 85.75% | +0.34% | 20,488 |
| PaymentMethod | Paypal | 95.26% | 94.68% | +0.62% | 24,084 |
| PaymentMethod | Others | 98.21% | 97.46% | +0.77% | 1,393 |
| PaymentMethod | Credit Card | 89.65% | 88.8% | +0.96% | 115,014 |
| PaymentProvider | No Payment | 100.0% | 100.0% | +0.00% | 683 |
| PaymentProvider | Braintree | 91.26% | 90.77% | +0.55% | 105,580 |
| PaymentProvider | Adyen | 90.56% | 89.6% | +1.07% | 36,376 |
| PaymentProvider | ProcessOut | 81.62% | 79.78% | +2.31% | 17,676 |
| PaymentProvider | Unknown | 96.99% | 57.14% | +69.73% | 664 |

---

*Report: 2026-04-14*
