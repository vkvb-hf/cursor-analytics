# AR Overall Investigation: WL 2026-W14

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 89.72% → 89.33% (-0.43%)  
**Volume:** 165,018 orders

## Executive Summary

**Overall:** AR Overall declined from 89.72% to 89.33% (-0.43 pp) in W14, reversing the positive trend observed in W13, with total volume of 165,018 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | Week-over-week change | -0.43 pp | ⚠️ |
| L1: Country Breakdown | Countries exceeding ±2.5% threshold | AO: -3.13 pp | ⚠️ |
| L1: Payment Method | Top degradation | Others: -1.18 pp | ✅ |
| L1: Payment Provider | Top degradation | Adyen: -1.34 pp | ⚠️ |

**Key Findings:**
- AO is the primary country driver with a significant -3.13 pp decline (85.21% from 87.96%) on 15,776 orders, exceeding the ±2.5% threshold
- Adyen payment provider showed notable degradation of -1.34 pp (89.60% from 90.82%) affecting 38,117 orders
- Volume decreased by 4,649 orders (165,018 vs 169,667) representing a -2.7% reduction week-over-week
- The decline breaks a two-week recovery pattern (W10-W13) that had brought AR from 88.19% to 89.72%
- ProcessOut maintains the lowest AR among major providers at 79.78% with 18,108 orders

**Action:** Investigate – Focus investigation on AO country performance and Adyen provider degradation as primary contributors to the overall decline.

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
| AO | 85.21% | 87.96% | -3.13% | 15,776 | ⚠️ |
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
