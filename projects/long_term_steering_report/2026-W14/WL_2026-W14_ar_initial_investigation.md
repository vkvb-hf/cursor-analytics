# AR Initial (LL0) Investigation: WL 2026-W14

**Metric:** AR Initial (LL0)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 89.23% → 89.84% (+0.68%)  
**Volume:** 12,781 orders

## Executive Summary

## Executive Summary

**Overall:** AR Initial (LL0) improved by +0.68% (from 89.23% to 89.84%) in 2026-W14, though this partial recovery follows two consecutive weeks of decline and remains below the 8-week high of 91.99% seen in W11.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | Week-over-week change | +0.68pp | ✅ |
| L1: Country - GN | Threshold ±2.5% | -3.50pp | ⚠️ |
| L1: Country - AO | Threshold ±2.5% | -2.99pp | ⚠️ |
| L1: Country - ER | Threshold ±2.5% | +3.53pp | ⚠️ |
| L1: PaymentMethod - Others | Significant decline | -6.62pp | ⚠️ |
| L1: PaymentProvider - Braintree | Notable improvement | +3.17pp | ✅ |

**Key Findings:**
- **Volume decline continues:** Order volume dropped from 15,670 (W07) to 12,781 (W14), representing an 18% reduction over 8 weeks
- **Country-level concerns:** GN (-3.50pp) and AO (-2.99pp) both experienced significant rate declines exceeding the ±2.5% threshold
- **Payment method "Others" volatility:** This category dropped -6.62pp (96.2% → 89.83%), though low volume (59 orders) limits impact
- **Braintree driving improvement:** Braintree improved +3.17pp (89.93% → 92.79%) with substantial volume (6,696 orders), contributing positively to overall recovery
- **ER improvement:** Despite low base rate (62.97%), ER improved +3.53pp with the highest volume (5,023 orders)

**Action:** **Investigate** – While the overall metric improved, the sustained volume decline and underperformance in GN and AO warrant deeper investigation into regional factors affecting these markets.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 89.84% | 12,781 | +0.68% ← REPORTED CHANGE |
| 2026-W13 | 89.23% | 12,904 | -1.39% |
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
| GN | 79.7% | 82.6% | -3.50% | 1,823 | ⚠️ |
| AO | 63.95% | 65.92% | -2.99% | 1,559 | ⚠️ |
| CK | 79.09% | 81.08% | -2.45% | 3,386 |  |
| ER | 62.97% | 60.82% | +3.53% | 5,023 | ⚠️ |

**Countries exceeding ±2.5% threshold:** GN, AO, ER

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Others | 89.83% | 96.2% | -6.62% | 59 |
| PaymentMethod | Paypal | 94.88% | 95.06% | -0.19% | 1,561 |
| PaymentMethod | Apple Pay | 90.92% | 90.95% | -0.04% | 3,963 |
| PaymentMethod | Credit Card | 88.15% | 87.03% | +1.29% | 7,198 |
| PaymentProvider | ProcessOut | 87.62% | 89.69% | -2.31% | 3,877 |
| PaymentProvider | Adyen | 84.72% | 86.25% | -1.77% | 2,160 |
| PaymentProvider | No Payment | 100.0% | 100.0% | +0.00% | 22 |
| PaymentProvider | Unknown | 76.92% | 75.0% | +2.56% | 26 |
| PaymentProvider | Braintree | 92.79% | 89.93% | +3.17% | 6,696 |

---

*Report: 2026-04-09*
