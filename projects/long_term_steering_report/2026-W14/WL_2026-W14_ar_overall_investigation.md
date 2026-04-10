# AR Overall Investigation: WL 2026-W14

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 89.72% → 89.33% (-0.43%)  
**Volume:** 165,018 orders

## Executive Summary

**Overall:** AR Overall declined from 89.72% to 89.33% (-0.39 pp) in W14 with volume decreasing from 169,667 to 165,018 orders (-2.7%).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (88.14%-89.79%) | -0.39 pp | ✅ |
| L1: Country Breakdown | AO exceeds ±2.5% threshold | -3.13 pp | ⚠️ |
| L1: PaymentMethod | No values exceed threshold | -1.18 pp max | ✅ |
| L1: PaymentProvider | Unknown low volume anomaly | -4.76 pp | ✅ |

**Key Findings:**
- AO is the primary driver of decline, dropping from 87.96% to 85.21% (-2.75 pp) with 15,776 orders - the only country exceeding the ±2.5% threshold
- PaymentProvider Adyen shows notable decline of -1.34 pp (90.82% → 89.60%) affecting 38,117 orders
- GN experienced the second-largest country decline at -1.25 pp (93.50% → 92.33%) with 14,333 orders
- PaymentProvider Unknown shows -4.76 pp decline but with negligible volume (35 orders)
- Overall volume decreased by ~4,649 orders (-2.7%) week-over-week

**Action:** Investigate - Focus on AO country performance and potential correlation with Adyen payment provider issues

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

*Report: 2026-04-10*
