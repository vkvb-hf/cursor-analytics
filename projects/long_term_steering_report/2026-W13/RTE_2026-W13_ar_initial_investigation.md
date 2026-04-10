# AR Initial (LL0) Investigation: RTE 2026-W13

**Metric:** AR Initial (LL0)  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 91.4% → 90.89% (-0.56%)  
**Volume:** 31,900 orders

## Executive Summary

**Overall:** AR Initial (LL0) declined by -0.56pp from 91.4% to 90.89% in W13, continuing a 4-week downward trend that has seen the metric fall from a peak of 93.59% in W09.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall RTE Trend | 4 consecutive weeks of decline (W10-W13) | -0.56pp | ⚠️ |
| L1: Country Breakdown | 3 countries exceed ±2.5% threshold (TK, TO, TV) | TK: -7.82pp, TO: -4.95pp, TV: -3.09pp | ⚠️ |
| L1: Payment Method | All major methods declining | Apple Pay: -1.47pp, Credit Card: -1.39pp | ⚠️ |
| L1: Payment Provider | Adyen worst performer among active providers | -1.50pp | ⚠️ |

**Key Findings:**
- TK experienced the largest country-level drop at -7.82pp (88.53% → 81.61%), though with relatively low volume (348 orders)
- The decline is broad-based across payment methods, with Apple Pay (-1.47pp) and Credit Card (-1.39pp) both contributing significantly given their combined volume of 30,698 orders
- Adyen shows the steepest provider decline at -1.50pp (91.16% → 89.79%) on 9,337 orders, while Braintree (largest volume at 21,813) declined -1.06pp
- Volume has dropped significantly from 52,390 (W07) to 31,900 (W13), a 39% reduction over 7 weeks
- PaymentProvider "Unknown" shows a -100pp drop but with negligible volume (16 orders)

**Action:** Investigate – The persistent 4-week declining trend combined with broad-based deterioration across countries, payment methods, and providers warrants deeper root cause analysis, particularly focusing on Adyen performance and the TK/TO/TV country issues.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 90.89% | 31,900 | -0.56% |
| 2026-W13 | 91.4% | 36,413 | -1.25% ← REPORTED CHANGE |
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
| TK | 81.61% | 88.53% | -7.82% | 348 | ⚠️ |
| TO | 71.79% | 75.53% | -4.95% | 677 | ⚠️ |
| TV | 87.32% | 90.11% | -3.09% | 481 | ⚠️ |
| FJ | 83.13% | 85.25% | -2.49% | 39,892 |  |
| YE | 76.16% | 77.56% | -1.81% | 6,413 |  |
| CF | 84.67% | 85.51% | -0.98% | 7,705 |  |

**Countries exceeding ±2.5% threshold:** TK, TO, TV

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Apple Pay | 90.08% | 91.43% | -1.47% | 7,965 |
| PaymentMethod | Credit Card | 90.71% | 91.99% | -1.39% | 22,733 |
| PaymentMethod | Paypal | 95.97% | 96.29% | -0.34% | 4,167 |
| PaymentMethod | Others | 96.06% | 95.48% | +0.61% | 1,548 |
| PaymentProvider | Unknown | 0.0% | 66.67% | -100.00% | 16 |
| PaymentProvider | Adyen | 89.79% | 91.16% | -1.50% | 9,337 |
| PaymentProvider | ProcessOut | 91.32% | 92.5% | -1.27% | 4,469 |
| PaymentProvider | Braintree | 92.02% | 93.0% | -1.06% | 21,813 |
| PaymentProvider | No Payment | 95.76% | 94.31% | +1.54% | 778 |

---

*Report: 2026-04-10*
