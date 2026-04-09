# AR Initial (LL0) Investigation: RTE 2026-W14

**Metric:** AR Initial (LL0)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 91.4% → 90.89% (-0.56%)  
**Volume:** 31,900 orders

## Executive Summary

## Executive Summary

**Overall:** AR Initial (LL0) declined from 91.4% to 90.89% (-0.51 pp) in W14, continuing a downward trend for the third consecutive week with performance now at its lowest point in the 8-week observation period.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: RTE Overall | 91.4% → 90.89% | -0.51 pp | ⚠️ |
| L1: Country - TO | 71.79% → 68.36% | -3.43 pp | ⚠️ |
| L1: Country - FJ | 83.13% → 82.6% | -0.53 pp | ✅ |
| L1: Country - YE | 76.16% → 75.74% | -0.42 pp | ✅ |
| L1: PaymentMethod - Credit Card | 90.71% → 89.99% | -0.72 pp | ⚠️ |
| L1: PaymentProvider - Adyen | 89.79% → 89.21% | -0.58 pp | ✅ |

**Key Findings:**
- **Sustained decline:** The metric has dropped from 92.56% (W12) to 90.89% (W14) over three weeks, a cumulative decline of 1.67 pp
- **Volume contraction:** Order volume decreased significantly from 36,413 (W13) to 31,900 (W14), a 12.4% reduction in volume
- **TO country underperformance:** TO experienced a -4.77% rate change (71.79% → 68.36%), the largest country-level decline, though volume is relatively small (629 orders)
- **Credit Card degradation:** Credit Card payments, representing the largest volume segment (20,181 orders), declined -0.80 pp and are the primary contributor to the overall decline
- **PaymentProvider "Unknown" anomaly:** A new provider category "Unknown" appeared with 77.55% rate and 49 orders (previously 0%)

**Action:** **Investigate** - The three-week declining trend combined with Credit Card payment method degradation across high-volume segments warrants immediate investigation into payment processing issues, particularly with Adyen (-0.58 pp) which handles significant Credit Card volume.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 90.89% | 31,900 | -0.56% ← REPORTED CHANGE |
| 2026-W13 | 91.4% | 36,413 | -1.25% |
| 2026-W12 | 92.56% | 42,779 | +0.05% |
| 2026-W11 | 92.51% | 46,365 | -0.24% |
| 2026-W10 | 92.73% | 48,166 | -0.92% |
| 2026-W09 | 93.59% | 46,087 | +0.47% |
| 2026-W08 | 93.15% | 46,567 | +0.33% |
| 2026-W07 | 92.84% | 52,390 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TO | 68.36% | 71.79% | -4.77% | 629 | ⚠️ |
| FJ | 82.6% | 83.13% | -0.64% | 38,808 |  |
| YE | 75.74% | 76.16% | -0.55% | 6,365 |  |
| CF | 84.9% | 84.67% | +0.27% | 7,763 |  |
| TT | 94.46% | 92.05% | +2.62% | 722 | ⚠️ |
| TV | 91.67% | 87.32% | +4.98% | 408 | ⚠️ |
| TK | 89.22% | 81.61% | +9.33% | 232 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TO, TT, TV, TK

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Credit Card | 89.99% | 90.71% | -0.80% | 20,181 |
| PaymentMethod | Paypal | 95.65% | 95.97% | -0.33% | 3,814 |
| PaymentMethod | Apple Pay | 90.02% | 90.08% | -0.07% | 7,026 |
| PaymentMethod | Others | 97.95% | 96.06% | +1.97% | 879 |
| PaymentProvider | Unknown | 77.55% | 0.0% | +nan% | 49 |
| PaymentProvider | Adyen | 89.21% | 89.79% | -0.65% | 9,422 |
| PaymentProvider | Braintree | 91.68% | 92.02% | -0.38% | 11,390 |
| PaymentProvider | ProcessOut | 91.53% | 91.32% | +0.23% | 10,970 |
| PaymentProvider | No Payment | 100.0% | 95.76% | +4.43% | 69 |

---

*Report: 2026-04-09*
