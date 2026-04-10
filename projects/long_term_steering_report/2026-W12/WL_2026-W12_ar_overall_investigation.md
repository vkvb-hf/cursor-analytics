# AR Overall Investigation: WL 2026-W12

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 89.72% → 89.33% (-0.43%)  
**Volume:** 165,018 orders

## Executive Summary

## Executive Summary

**Overall:** AR Overall declined from 89.72% to 89.33% (-0.39 pp) in WL 2026-W12, representing a modest deterioration across 165,018 orders, though the metric remains within the normal fluctuation range observed over the 8-week trend.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | Week-over-week change | -0.43% | ⚠️ |
| L1: Country Impact | Any country ≥ ±2.5% threshold | None exceeded | ✅ |
| L1: Payment Method | Significant degradation | Others -1.39%, Apple Pay -0.22% | ⚠️ |
| L1: Payment Provider | Significant degradation | ProcessOut -1.05 pp, Unknown -1.95 pp | ⚠️ |

**Key Findings:**
- MR country showed the largest rate decline at -1.38 pp (80.0% vs 81.12%), though no country exceeded the ±2.5% alerting threshold
- KN country also declined notably by -1.31 pp (87.76% vs 88.93%) with 10,617 orders
- PaymentMethod "Others" degraded by -1.39 pp (87.48% vs 88.71%) on 4,296 orders
- ProcessOut payment provider declined -1.05 pp (78.95% vs 79.79%) across 18,341 orders, representing meaningful volume
- The 8-week trend shows overall stability with AR ranging between 88.14% and 89.79%, suggesting current performance is within normal variance

**Action:** Monitor — The decline is modest and no single dimension exceeds critical thresholds. Continue monitoring MR, KN countries and ProcessOut provider performance in the next weekly cycle.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 89.33% | 165,018 | -0.43% |
| 2026-W13 | 89.72% | 169,667 | +0.07% |
| 2026-W12 | 89.66% | 169,891 | -0.14% ← REPORTED CHANGE |
| 2026-W11 | 89.79% | 174,933 | +0.80% |
| 2026-W10 | 89.08% | 179,964 | +1.01% |
| 2026-W09 | 88.19% | 180,862 | +0.06% |
| 2026-W08 | 88.14% | 179,647 | -0.50% |
| 2026-W07 | 88.58% | 186,442 | - |

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
| PaymentMethod | Others | 87.48% | 88.71% | -1.39% | 4,296 |
| PaymentMethod | Apple Pay | 86.02% | 86.21% | -0.22% | 22,335 |
| PaymentMethod | Credit Card | 89.34% | 89.5% | -0.18% | 117,521 |
| PaymentMethod | Paypal | 94.61% | 94.43% | +0.19% | 25,739 |
| PaymentProvider | Unknown | 96.0% | 97.91% | -1.95% | 75 |
| PaymentProvider | ProcessOut | 78.95% | 79.79% | -1.05% | 18,341 |
| PaymentProvider | Adyen | 90.17% | 90.58% | -0.45% | 39,521 |
| PaymentProvider | No Payment | 99.8% | 99.82% | -0.01% | 1,006 |
| PaymentProvider | Braintree | 91.15% | 91.1% | +0.06% | 110,948 |

---

*Report: 2026-04-10*
