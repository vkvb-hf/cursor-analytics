# AR Initial (LL0) Investigation: WL 2026-W15

**Metric:** AR Initial (LL0)  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 89.83% → 91.04% (+1.35%)  
**Volume:** 11,588 orders

## Executive Summary

**Overall:** AR Initial (LL0) improved from 89.83% to 91.04% (+1.21 pp) in W15, continuing a recovery trend after the W12 low point, though on reduced volume (11,588 orders, down from 12,774).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | Rate increased +1.21 pp | +1.35% | ✅ |
| L1: Country Analysis | MR exceeded ±2.5% threshold | +4.84% | ⚠️ |
| L1: Payment Method | Others segment volatility | +8.74% | ⚠️ |
| L1: Payment Provider | Unknown provider anomaly | +27.03% | ⚠️ |

**Key Findings:**
- MR showed the largest country-level improvement at +4.84% (76.28% → 79.97%), driving overall metric gains with 3,215 orders
- PaymentProvider "Unknown" exhibited an extreme rate jump of +27.03 pp (76.92% → 97.71%) on 656 orders, suggesting data classification changes or a specific cohort shift
- PaymentMethod "Others" improved significantly by +8.74 pp (89.83% → 97.68%) on 689 orders, indicating improved processing for non-standard payment types
- Volume declined 9.3% week-over-week (12,774 → 11,588), which may artificially inflate rate improvements
- ER remains the lowest-performing country at 64.45%, though it improved +2.38% from prior week

**Action:** Monitor – The overall improvement is positive, but the anomalous spikes in "Unknown" provider (+27.03 pp) and "Others" payment method (+8.74 pp) warrant investigation to confirm data quality. Track MR performance to determine if the +4.84% gain is sustained.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 91.04% | 11,588 | +1.35% ← REPORTED CHANGE |
| 2026-W14 | 89.83% | 12,774 | +0.67% |
| 2026-W13 | 89.23% | 12,902 | -1.39% |
| 2026-W12 | 90.49% | 13,906 | -1.63% |
| 2026-W11 | 91.99% | 14,300 | +1.10% |
| 2026-W10 | 90.99% | 14,879 | -0.32% |
| 2026-W09 | 91.28% | 15,292 | +0.60% |
| 2026-W08 | 90.74% | 15,382 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| GN | 78.65% | 79.7% | -1.32% | 1,527 |  |
| CK | 79.91% | 79.09% | +1.03% | 3,703 |  |
| ER | 64.45% | 62.95% | +2.38% | 4,529 |  |
| MR | 79.97% | 76.28% | +4.84% | 3,215 | ⚠️ |

**Countries exceeding ±2.5% threshold:** MR

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Apple Pay | 90.73% | 90.91% | -0.20% | 3,312 |
| PaymentMethod | Paypal | 95.37% | 94.87% | +0.53% | 1,318 |
| PaymentMethod | Credit Card | 89.57% | 88.14% | +1.61% | 6,269 |
| PaymentMethod | Others | 97.68% | 89.83% | +8.74% | 689 |
| PaymentProvider | No Payment | 100.0% | 100.0% | +0.00% | 11 |
| PaymentProvider | Braintree | 93.09% | 92.78% | +0.33% | 5,539 |
| PaymentProvider | Adyen | 86.25% | 84.72% | +1.81% | 2,109 |
| PaymentProvider | ProcessOut | 89.31% | 87.61% | +1.93% | 3,273 |
| PaymentProvider | Unknown | 97.71% | 76.92% | +27.03% | 656 |

---

*Report: 2026-04-14*
