# AR Initial (LL0) Investigation: WL 2026-W13

**Metric:** AR Initial (LL0)  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 89.23% → 89.84% (+0.68%)  
**Volume:** 12,781 orders

## Executive Summary

## Executive Summary

**Overall:** AR Initial (LL0) improved slightly from 89.23% to 89.84% (+0.68pp) in 2026-W13, though this follows a broader declining trend from 91.99% in 2026-W11.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0 Overall Trend | 8-week stability | +0.68pp WoW | ✅ |
| L1 Country - MR | Threshold ±2.5% | -6.73pp | ⚠️ |
| L1 Country - CK | Threshold ±2.5% | +2.52pp | ⚠️ |
| L1 Country - ER | Threshold ±2.5% | +6.87pp | ⚠️ |
| L1 PaymentProvider - Braintree | Rate change | -3.60pp | ⚠️ |
| L1 PaymentProvider - Unknown | Rate change | -25.00pp | ⚠️ |

**Key Findings:**
- **MR experienced significant decline:** AR Initial dropped -6.73pp (82.38% → 76.83%) with substantial volume of 3,600 orders, requiring immediate attention
- **Braintree payment provider degradation:** Rate declined -3.60pp (93.29% → 89.93%) affecting 6,497 orders (largest provider volume)
- **ER showed strong recovery:** Rate improved +6.87pp (56.92% → 60.82%) on 5,197 orders, though absolute rate remains lowest at 60.82%
- **Volume decline continues:** Total volume dropped from 15,670 (W07) to 12,781 (W14), representing an 18% reduction over 8 weeks
- **PaymentProvider "Unknown" anomaly:** -25.00pp drop, though only 12 orders affected (low impact)

**Action:** **Investigate** - Priority focus on MR country decline (-6.73pp) and Braintree provider degradation (-3.60pp), as both represent significant volume segments with material rate deterioration.

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
