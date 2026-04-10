# AR Initial (LL0) Investigation: WL 2026-W13

**Metric:** AR Initial (LL0)  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 89.23% → 89.84% (+0.68%)  
**Volume:** 12,781 orders

## Executive Summary

## Executive Summary

**Overall:** AR Initial (LL0) improved slightly from 89.23% to 89.84% (+0.61 pp) in 2026-W14, though this follows a declining trend from the 91.99% peak observed in 2026-W11.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0 Trend | 8-week pattern | +0.61 pp WoW | ✅ |
| L1 Country | MR, CK, ER outside ±2.5% | MR -6.73 pp, CK +2.52 pp, ER +6.87 pp | ⚠️ |
| L1 PaymentProvider | Braintree, Unknown flagged | Braintree -3.60 pp, Unknown -25.00 pp | ⚠️ |
| L1 PaymentMethod | Others improved | Others +3.99 pp (low volume: 79) | ✅ |

**Key Findings:**
- MR experienced the largest decline at -6.73 pp (76.83% from 82.38%) with significant volume (3,600 orders), requiring immediate attention
- Braintree payment provider declined -3.60 pp (89.93% from 93.29%) affecting 6,497 orders—the highest volume provider
- ER showed strong improvement of +6.87 pp (60.82% from 56.92%) with the largest volume at 5,197 orders, though absolute rate remains the lowest
- Overall volume has declined steadily from 15,670 (W07) to 12,781 (W14), a reduction of approximately 18%
- Unknown payment provider dropped -25.00 pp but represents minimal volume (12 orders)

**Action:** Investigate — Focus on MR country performance decline and Braintree payment provider degradation, as both represent high-volume segments with significant rate drops.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 89.84% | 12,781 | +0.68% |
| 2026-W13 | 89.23% | 12,904 | -1.39% ← REPORTED CHANGE |
| 2026-W12 | 90.49% | 13,906 | -1.63% |
| 2026-W11 | 91.99% | 14,300 | +1.10% |
| 2026-W10 | 90.99% | 14,879 | -0.32% |
| 2026-W09 | 91.28% | 15,292 | +0.60% |
| 2026-W08 | 90.74% | 15,382 | +0.86% |
| 2026-W07 | 89.97% | 15,670 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| MR | 76.83% | 82.38% | -6.73% | 3,600 | ⚠️ |
| GN | 82.6% | 84.58% | -2.34% | 2,126 |  |
| CK | 81.08% | 79.08% | +2.52% | 3,752 | ⚠️ |
| ER | 60.82% | 56.92% | +6.87% | 5,197 | ⚠️ |

**Countries exceeding ±2.5% threshold:** MR, CK, ER

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Credit Card | 87.03% | 88.5% | -1.66% | 7,363 |
| PaymentMethod | Apple Pay | 90.95% | 91.0% | -0.06% | 3,944 |
| PaymentMethod | Paypal | 95.06% | 94.62% | +0.46% | 1,518 |
| PaymentMethod | Others | 96.2% | 92.51% | +3.99% | 79 |
| PaymentProvider | Unknown | 75.0% | 100.0% | -25.00% | 12 |
| PaymentProvider | Braintree | 89.93% | 93.29% | -3.60% | 6,497 |
| PaymentProvider | ProcessOut | 89.69% | 89.37% | +0.36% | 3,995 |
| PaymentProvider | No Payment | 100.0% | 98.97% | +1.04% | 66 |
| PaymentProvider | Adyen | 86.25% | 84.52% | +2.05% | 2,334 |

---

*Report: 2026-04-10*
