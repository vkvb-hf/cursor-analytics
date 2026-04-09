# AR Overall Investigation: WL 2026-W14

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 89.72% → 89.33% (-0.43%)  
**Volume:** 165,018 orders

## Executive Summary

## Executive Summary

**Overall:** AR Overall declined from 89.72% to 89.33% (-0.39 pp) in 2026-W14, with order volume decreasing to 165,018 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL Overall | Week-over-week trend | -0.39 pp | ⚠️ |
| L1: Country | AO exceeds ±2.5% threshold | -3.12 pp | ⚠️ |
| L1: PaymentMethod | Others highest decline | -1.18 pp | ✅ |
| L1: PaymentProvider | Unknown highest decline (low volume) | -4.76 pp | ✅ |
| L1: PaymentProvider | Adyen notable decline | -1.34 pp | ⚠️ |

**Key Findings:**
- AO (Angola) experienced the largest country-level decline at -3.12 pp (from 87.96% to 85.22%), exceeding the ±2.5% threshold with 15,776 orders
- PaymentProvider Adyen showed a -1.34 pp decline (from 90.82% to 89.60%) affecting 38,117 orders, making it the most impactful provider-level change by volume
- Overall order volume dropped by 4,649 orders (from 169,667 to 165,018) compared to the prior week
- The 8-week trend shows the current rate (89.33%) remains above the W07-W09 baseline (~88.2%) but has reversed the positive momentum seen in W10-W13
- PaymentProvider "Unknown" showed a -4.76 pp decline but with minimal volume impact (only 35 orders)

**Action:** Investigate — Focus investigation on AO (Angola) country performance and Adyen payment provider, as these represent the primary drivers of the decline with material order volumes.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 89.33% | 165,018 | -0.43% ← REPORTED CHANGE |
| 2026-W13 | 89.72% | 169,667 | +0.07% |
| 2026-W12 | 89.66% | 169,891 | -0.14% |
| 2026-W11 | 89.79% | 174,933 | +0.80% |
| 2026-W10 | 89.08% | 179,964 | +1.01% |
| 2026-W09 | 88.19% | 180,862 | +0.06% |
| 2026-W08 | 88.14% | 179,647 | -0.50% |
| 2026-W07 | 88.58% | 186,442 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| AO | 85.22% | 87.96% | -3.12% | 15,776 | ⚠️ |
| GN | 92.33% | 93.5% | -1.25% | 14,333 |  |
| ER | 89.23% | 89.92% | -0.77% | 67,730 |  |
| CK | 93.82% | 94.15% | -0.35% | 42,176 |  |
| KN | 88.21% | 87.61% | +0.68% | 11,048 |  |

**Countries exceeding ±2.5% threshold:** AO

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Others | 97.46% | 98.62% | -1.18% | 826 |
| PaymentMethod | Credit Card | 88.8% | 89.23% | -0.48% | 117,492 |
| PaymentMethod | Apple Pay | 85.75% | 86.16% | -0.47% | 21,798 |
| PaymentMethod | Paypal | 94.68% | 94.82% | -0.15% | 24,902 |
| PaymentProvider | Unknown | 57.14% | 60.0% | -4.76% | 35 |
| PaymentProvider | Adyen | 89.6% | 90.82% | -1.34% | 38,117 |
| PaymentProvider | ProcessOut | 79.78% | 79.93% | -0.18% | 18,108 |
| PaymentProvider | Braintree | 90.77% | 90.89% | -0.12% | 108,008 |
| PaymentProvider | No Payment | 100.0% | 100.0% | +0.00% | 750 |

---

*Report: 2026-04-09*
