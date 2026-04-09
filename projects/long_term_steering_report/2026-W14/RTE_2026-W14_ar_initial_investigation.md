# AR Initial (LL0) Investigation: RTE 2026-W14

**Metric:** AR Initial (LL0)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 91.4% → 90.89% (-0.56%)  
**Volume:** 31,900 orders

## Executive Summary

## Executive Summary

**Overall:** AR Initial (LL0) declined from 91.4% to 90.89% (-0.56pp) in W14, continuing a three-week downward trend with rates dropping from 92.56% in W12, accompanied by significant volume reduction to 31,900 orders (down from 36,413 in W13).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | 3-week consecutive decline (W12-W14) | -1.67pp cumulative | ⚠️ |
| L1: Country | TO showed largest decline | -4.77pp | ⚠️ |
| L1: Country | TK, TV, TT showed improvements | +2.62pp to +9.33pp | ✅ |
| L1: Payment Method | Credit Card (largest volume) declined | -0.80pp | ⚠️ |
| L1: Payment Provider | Adyen declined | -0.65pp | ⚠️ |
| L1: Payment Provider | Unknown provider anomaly | +nan% (new/data issue) | ⚠️ |

**Key Findings:**
- **Sustained decline:** AR Initial has dropped for 3 consecutive weeks, falling 1.67pp from W12 (92.56%) to W14 (90.89%), now at the lowest point in the 8-week window
- **Volume contraction:** Order volume decreased 39% from W07 peak (52,390) to W14 (31,900), with a 12.4% drop from W13 alone
- **TO country underperformance:** Tonga (TO) experienced a -4.77pp decline (71.79% → 68.36%), the largest country-level drop, though with limited volume (629 orders)
- **Credit Card payment drag:** Credit Card transactions, representing 63% of volume (20,181 orders), declined -0.80pp, contributing most to the overall metric drop
- **Data anomaly:** PaymentProvider "Unknown" shows 49 orders at 77.55% with an undefined prior rate, suggesting a tracking or categorization issue

**Action:** **Investigate** – The three-week declining trend combined with sustained volume reduction warrants deeper analysis into Credit Card payment flows and the root cause of the TO country decline. The "Unknown" payment provider anomaly should also be reviewed for data integrity.

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
| YE | 75.73% | 76.16% | -0.57% | 6,365 |  |
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
