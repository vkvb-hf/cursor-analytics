# AR Initial (LL0) Investigation: RTE 2026-W15

**Metric:** AR Initial (LL0)  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 90.88% → 91.76% (+0.97%)  
**Volume:** 31,081 orders

## Executive Summary

## Executive Summary

**Overall:** AR Initial (LL0) improved from 90.88% to 91.76% (+0.97pp) in W15, representing a partial recovery after two consecutive weeks of decline, though the metric remains below the 8-week high of 93.59% observed in W09.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: RTE Overall | +0.97pp improvement | +0.97pp | ✅ |
| L1: Country Variance | 4 countries exceed ±2.5% threshold | Mixed | ⚠️ |
| L1: Payment Method | Minor decline in "Others" (-2.11pp) | -2.11pp | ✅ |
| L1: Payment Provider | Adyen improved +2.16pp | +2.16pp | ✅ |

**Key Findings:**
- TV experienced the largest decline (-5.75pp, from 91.67% to 86.4%) though with low volume (375 orders)
- TT declined significantly (-3.10pp, from 94.46% to 91.53%) with 685 orders
- TO showed strong improvement (+10.03pp, from 68.36% to 75.22%) indicating potential recovery from prior issues
- Volume decreased substantially from W08-W12 average (~46K) to current 31,081 orders, a trend worth monitoring
- Adyen payment provider improved +2.16pp (89.2% → 91.13%) processing 8,908 orders

**Action:** Monitor – The overall metric improved and no single high-volume segment shows critical degradation. Continue tracking TV and TT for sustained underperformance, and monitor the declining volume trend.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 91.76% | 31,081 | +0.97% ← REPORTED CHANGE |
| 2026-W14 | 90.88% | 31,924 | -0.51% |
| 2026-W13 | 91.35% | 36,477 | -1.31% |
| 2026-W12 | 92.56% | 42,779 | +0.05% |
| 2026-W11 | 92.51% | 46,365 | -0.24% |
| 2026-W10 | 92.73% | 48,166 | -0.92% |
| 2026-W09 | 93.59% | 46,087 | +0.47% |
| 2026-W08 | 93.15% | 46,567 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TV | 86.4% | 91.67% | -5.75% | 375 | ⚠️ |
| TT | 91.53% | 94.46% | -3.10% | 685 | ⚠️ |
| YE | 74.09% | 75.73% | -2.17% | 5,723 |  |
| FJ | 82.39% | 82.6% | -0.25% | 35,734 |  |
| CF | 85.96% | 84.9% | +1.25% | 7,864 |  |
| TZ | 86.09% | 83.4% | +3.23% | 539 | ⚠️ |
| TO | 75.22% | 68.36% | +10.03% | 686 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TV, TT, TZ, TO

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Others | 95.99% | 98.06% | -2.11% | 1,023 |
| PaymentMethod | Paypal | 95.78% | 95.7% | +0.09% | 3,675 |
| PaymentMethod | Apple Pay | 90.81% | 89.82% | +1.10% | 6,975 |
| PaymentMethod | Credit Card | 91.11% | 90.04% | +1.19% | 19,408 |
| PaymentProvider | Unknown | 78.85% | 79.17% | -0.40% | 104 |
| PaymentProvider | ProcessOut | 91.62% | 91.63% | -0.01% | 11,262 |
| PaymentProvider | No Payment | 100.0% | 100.0% | +0.00% | 40 |
| PaymentProvider | Braintree | 92.51% | 91.54% | +1.06% | 10,767 |
| PaymentProvider | Adyen | 91.13% | 89.2% | +2.16% | 8,908 |

---

*Report: 2026-04-14*
