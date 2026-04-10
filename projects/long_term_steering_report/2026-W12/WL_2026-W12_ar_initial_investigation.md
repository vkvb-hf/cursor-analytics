# AR Initial (LL0) Investigation: WL 2026-W12

**Metric:** AR Initial (LL0)  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 89.23% → 89.84% (+0.68%)  
**Volume:** 12,781 orders

## Executive Summary

## Executive Summary

**Overall:** AR Initial (LL0) improved from 89.23% to 89.84% (+0.61 pp) in 2026-W12, representing a partial recovery after two consecutive weeks of decline, though the rate remains below the 91.99% peak observed in 2026-W11.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0 Trend | 8-week stability | +0.68% WoW | ✅ |
| L1 Country | KN performance | -3.66 pp | ⚠️ |
| L1 Country | ER performance | +2.58 pp | ⚠️ |
| L1 Country | CK performance | +3.90 pp | ⚠️ |
| L1 Country | AO performance | +3.99 pp | ⚠️ |
| L1 Payment Method | Credit Card | -2.88 pp | ⚠️ |
| L1 Payment Provider | Adyen | -2.37 pp | ⚠️ |

**Key Findings:**
- KN experienced a significant decline of -3.66 pp (94.82% → 91.35%) with 2,729 orders, representing the largest negative country movement
- Credit Card payment method declined -2.88 pp (91.13% → 88.5%) affecting 6,287 orders (49% of total volume)
- Adyen payment provider dropped -2.37 pp (86.57% → 84.52%) on 2,732 orders, showing potential processing issues
- CK and AO showed strong improvements (+3.90 pp and +3.99 pp respectively), partially offsetting KN decline
- Overall volume continues declining trend (12,781 vs 15,670 in W07), down ~18% over 8 weeks

**Action:** Investigate — Focus on KN country decline and Credit Card/Adyen payment path degradation, as these represent high-volume segments with material rate drops.

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
