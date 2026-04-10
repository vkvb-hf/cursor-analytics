# AR Initial (LL0) Investigation: WL 2026-W12

**Metric:** AR Initial (LL0)  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 89.23% → 89.84% (+0.68%)  
**Volume:** 12,781 orders

## Executive Summary

## Executive Summary

**Overall:** AR Initial (LL0) improved from 89.23% to 89.84% (+0.68pp) in 2026-W12, representing a partial recovery after two consecutive weeks of decline, though still below the 91.99% peak observed in 2026-W11.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Rate | 89.23% → 89.84% | +0.68pp | ✅ |
| L1: Country - KN | 94.82% → 91.35% | -3.66pp | ⚠️ |
| L1: Country - ER | 55.49% → 56.92% | +2.58pp | ⚠️ |
| L1: Country - CK | 76.11% → 79.08% | +3.90pp | ⚠️ |
| L1: Country - AO | 62.94% → 65.46% | +3.99pp | ⚠️ |
| L1: PaymentMethod - Credit Card | 91.13% → 88.5% | -2.88pp | ⚠️ |
| L1: PaymentProvider - Adyen | 86.57% → 84.52% | -2.37pp | ⚠️ |

**Key Findings:**
- KN experienced the largest negative swing (-3.66pp) despite having the highest current rate (91.35%), with significant volume (2,729 orders) warranting investigation
- Credit Card payment method declined -2.88pp (91.13% → 88.5%) and represents the highest volume segment at 6,287 orders, masking gains elsewhere
- Adyen provider showed the steepest decline among payment providers (-2.37pp), potentially linked to Credit Card performance issues
- CK and AO showed strong recovery (+3.90pp and +3.99pp respectively), though both remain well below the overall average at 79.08% and 65.46%
- Overall volume has declined steadily from 15,670 (W07) to 12,781 (W14), a decrease of approximately 18%

**Action:** Investigate — Focus on KN country decline and Credit Card/Adyen payment path degradation, as these high-volume segments are suppressing overall recovery despite gains in smaller markets.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 89.84% | 12,781 | +0.68% |
| 2026-W13 | 89.23% | 12,904 | -1.39% |
| 2026-W12 | 90.49% | 13,906 | -1.63% ← REPORTED CHANGE |
| 2026-W11 | 91.99% | 14,300 | +1.10% |
| 2026-W10 | 90.99% | 14,879 | -0.32% |
| 2026-W09 | 91.28% | 15,292 | +0.60% |
| 2026-W08 | 90.74% | 15,382 | +0.86% |
| 2026-W07 | 89.97% | 15,670 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| KN | 91.35% | 94.82% | -3.66% | 2,729 | ⚠️ |
| ER | 56.92% | 55.49% | +2.58% | 5,220 | ⚠️ |
| CK | 79.08% | 76.11% | +3.90% | 4,207 | ⚠️ |
| AO | 65.46% | 62.94% | +3.99% | 1,679 | ⚠️ |

**Countries exceeding ±2.5% threshold:** KN, ER, CK, AO

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Credit Card | 88.5% | 91.13% | -2.88% | 6,287 |
| PaymentMethod | Apple Pay | 91.0% | 91.81% | -0.87% | 4,146 |
| PaymentMethod | Others | 92.51% | 92.79% | -0.30% | 1,856 |
| PaymentMethod | Paypal | 94.62% | 94.53% | +0.10% | 1,617 |
| PaymentProvider | Adyen | 84.52% | 86.57% | -2.37% | 2,732 |
| PaymentProvider | ProcessOut | 89.37% | 91.18% | -1.98% | 4,194 |
| PaymentProvider | Braintree | 93.29% | 93.83% | -0.58% | 6,721 |
| PaymentProvider | No Payment | 98.97% | 99.04% | -0.07% | 194 |
| PaymentProvider | Unknown | 100.0% | 100.0% | +0.00% | 65 |

---

*Report: 2026-04-10*
