# AR Initial (LL0) Investigation: RTE 2026-W14

**Metric:** AR Initial (LL0)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 91.4% → 90.89% (-0.56%)  
**Volume:** 31,900 orders

## Executive Summary

## Executive Summary

**Overall:** AR Initial (LL0) declined from 91.4% to 90.89% (-0.51pp) in W14, continuing a downward trend now spanning 5 consecutive weeks with total decline of 2.70pp since W09.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: RTE Trend | 5-week decline pattern | -2.70pp since W09 | ⚠️ |
| L1: Country | TO largest drop | -4.77% | ⚠️ |
| L1: Payment Method | Credit Card decline | -0.80% | ⚠️ |
| L1: Payment Provider | Unknown provider anomaly | +nan% (new) | ⚠️ |
| Volume | Significant volume drop | 31,900 vs 36,413 (-12.4%) | ⚠️ |

**Key Findings:**
- TO experienced the largest country-level decline at -4.77% (68.36% vs 71.79%), though volume is relatively low at 629 orders
- Credit Card payments, representing the highest volume (20,181 orders / 63% of total), declined -0.80% and are the primary driver of the overall metric decline
- Order volume has dropped significantly from 52,390 (W07) to 31,900 (W14), a 39% reduction over 8 weeks
- A new "Unknown" payment provider appeared with 49 orders at 77.55% rate, requiring investigation
- TK showed strong improvement (+9.33%) but with minimal volume impact (232 orders)

**Action:** **Investigate** - The sustained 5-week declining trend combined with significant volume reduction and Credit Card performance degradation requires root cause analysis, particularly focusing on FJ (highest volume at 38,808 orders with -0.64% decline) and Credit Card payment processing.

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

*Report: 2026-04-10*
