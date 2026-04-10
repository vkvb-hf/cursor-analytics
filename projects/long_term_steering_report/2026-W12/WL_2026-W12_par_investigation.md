# PAR Investigation: WL 2026-W12

**Metric:** PAR  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 91.3% → 91.05% (-0.27%)  
**Volume:** 165,018 orders

## Executive Summary

**Overall:** PAR declined by 0.27 percentage points (91.3% → 91.05%) on volume of 165,018 orders, continuing a modest downward trend observed over recent weeks.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Sustained decline pattern | -0.27 pp | ⚠️ |
| L1: Country Breakdown | No country exceeds ±2.5% threshold | -1.38 pp max (MR) | ✅ |
| L1: PaymentMethod | "Others" exceeds threshold | -3.01 pp | ⚠️ |
| L1: PaymentProvider | ProcessOut underperforming | -0.97 pp | ⚠️ |

**Key Findings:**
- PaymentMethod "Others" showed the largest decline at -3.01 pp (90.65% → 87.92%), though volume is relatively low at 4,296 orders
- MR country experienced the steepest country-level decline at -1.38 pp (81.12% → 80.0%) on 18,070 orders
- ProcessOut payment provider declined -0.97 pp (81.37% → 80.58%) affecting 18,341 orders, correlating with MR country performance
- KN country also showed notable decline of -1.31 pp (88.93% → 87.76%) on 10,617 orders
- Overall volume decreased by ~4,649 orders (169,667 → 165,018) week-over-week

**Action:** Investigate — Focus on ProcessOut provider performance in MR region and root cause of PaymentMethod "Others" decline. Monitor KN country trends.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 91.05% | 165,018 | -0.27% |
| 2026-W13 | 91.3% | 169,667 | -0.02% |
| 2026-W12 | 91.32% | 169,891 | -0.28% ← REPORTED CHANGE |
| 2026-W11 | 91.58% | 174,933 | +1.03% |
| 2026-W10 | 90.65% | 179,964 | +0.81% |
| 2026-W09 | 89.92% | 180,862 | +0.04% |
| 2026-W08 | 89.88% | 179,647 | -0.50% |
| 2026-W07 | 90.33% | 186,442 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| MR | 80.0% | 81.12% | -1.38% | 18,070 |  |
| KN | 87.76% | 88.93% | -1.31% | 10,617 |  |
| GN | 93.64% | 94.18% | -0.57% | 16,164 |  |
| CK | 93.33% | 93.63% | -0.32% | 42,397 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Others | 87.92% | 90.65% | -3.01% | 4,296 |
| PaymentMethod | Apple Pay | 87.46% | 87.75% | -0.33% | 22,335 |
| PaymentMethod | Credit Card | 91.29% | 91.51% | -0.24% | 117,521 |
| PaymentMethod | Paypal | 95.42% | 95.41% | +0.00% | 25,739 |
| PaymentProvider | Unknown | 97.33% | 98.43% | -1.11% | 75 |
| PaymentProvider | ProcessOut | 80.58% | 81.37% | -0.97% | 18,341 |
| PaymentProvider | Braintree | 92.15% | 92.38% | -0.25% | 110,948 |
| PaymentProvider | Adyen | 93.76% | 93.98% | -0.24% | 39,521 |
| PaymentProvider | No Payment | 99.8% | 99.82% | -0.01% | 1,006 |

---

*Report: 2026-04-10*
