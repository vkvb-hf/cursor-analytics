# AR Initial (LL0) Investigation: WL 2026-W14

**Metric:** AR Initial (LL0)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 89.23% → 89.84% (+0.68%)  
**Volume:** 12,781 orders

## Executive Summary

**Overall:** AR Initial (LL0) improved by +0.68 percentage points (89.23% → 89.84%) in W14, showing a partial recovery after two consecutive weeks of decline, though still below the W11 peak of 91.99%.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | Rate improved vs prior week | +0.68 pp | ✅ |
| L0: Volume Trend | Volume declined vs prior week | -123 orders | ⚠️ |
| L1: Country (GN) | Rate declined significantly | -3.50 pp | ⚠️ |
| L1: Country (AO) | Rate declined significantly | -3.08 pp | ⚠️ |
| L1: Country (ER) | Rate improved significantly | +3.50 pp | ✅ |
| L1: PaymentMethod (Others) | Rate declined significantly | -6.62 pp | ⚠️ |
| L1: PaymentProvider (Braintree) | Rate improved | +3.17 pp | ✅ |

**Key Findings:**
- Volume continues a persistent downward trend, declining from 15,670 orders in W07 to 12,781 in W14 (-18.4% over 8 weeks)
- GN and AO both showed significant rate declines (-3.50 pp and -3.08 pp respectively), exceeding the ±2.5% threshold
- ER showed strong improvement (+3.50 pp), partially offsetting declines in other countries
- PaymentMethod "Others" experienced a sharp decline (-6.62 pp), though volume is minimal (59 orders)
- Braintree improved +3.17 pp and handles the largest volume (6,696 orders), contributing positively to overall performance

**Action:** Monitor – The overall metric improved and the rate is recovering. However, investigate the sustained volume decline and monitor GN/AO performance in W15. If country-level declines persist, escalate for deeper analysis.

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
| AO | 63.89% | 65.92% | -3.08% | 1,559 | ⚠️ |
| CK | 79.09% | 81.08% | -2.45% | 3,386 |  |
| ER | 62.95% | 60.82% | +3.50% | 5,023 | ⚠️ |

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

*Report: 2026-04-10*
