# AR Overall Investigation: RTE 2026-W14

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 92.79% → 92.46% (-0.36%)  
**Volume:** 431,853 orders

## Executive Summary

**Overall:** AR Overall declined from 92.79% to 92.46% (-0.36 pp) in W14, continuing a three-week downward trend that has seen the metric drop from a peak of 93.20% in W11.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Consistent decline W11→W14 | -0.74 pp over 3 weeks | ⚠️ |
| L1: Country Impact | No country exceeds ±2.5% threshold | TK largest drop at -1.63 pp | ✅ |
| L1: Payment Method | Credit Card (73% volume) declined | -0.42 pp | ⚠️ |
| L1: Payment Provider | Braintree (68% volume) declined | -0.36 pp | ⚠️ |

**Key Findings:**
- **Sustained decline pattern:** The metric has dropped consecutively for three weeks (W12: -0.12 pp, W13: -0.32 pp, W14: -0.36 pp), with the rate of decline accelerating
- **Credit Card performance:** The largest payment method by volume (316,124 orders / 73%) declined -0.42 pp, driving the majority of the overall drop
- **Braintree impact:** As the dominant payment provider (293,781 orders / 68%), Braintree's -0.36 pp decline directly mirrors the overall metric decline
- **Volume contraction:** Order volume has decreased from 458,408 (W11) to 431,853 (W14), a 5.8% reduction alongside rate deterioration
- **No geographic outliers:** All countries remained within the ±2.5% threshold, indicating a systemic rather than localized issue

**Action:** **Investigate** – The three-week consecutive decline and accelerating rate of deterioration warrants deeper investigation into Credit Card + Braintree transaction failures. Recommend L2 drill-down into Braintree error codes and decline reasons.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 92.46% | 431,853 | -0.36% ← REPORTED CHANGE |
| 2026-W13 | 92.79% | 442,530 | -0.32% |
| 2026-W12 | 93.09% | 443,994 | -0.12% |
| 2026-W11 | 93.2% | 458,408 | +1.80% |
| 2026-W10 | 91.55% | 467,998 | +0.24% |
| 2026-W09 | 91.33% | 466,696 | +0.29% |
| 2026-W08 | 91.07% | 462,049 | -0.28% |
| 2026-W07 | 91.33% | 474,461 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TK | 88.65% | 90.12% | -1.63% | 1,779 |  |
| TZ | 90.11% | 91.42% | -1.43% | 3,013 |  |
| YE | 88.15% | 88.62% | -0.54% | 45,214 |  |
| FJ | 93.62% | 93.97% | -0.37% | 397,332 |  |
| CF | 93.47% | 93.7% | -0.24% | 52,140 |  |
| TT | 97.2% | 96.27% | +0.97% | 4,924 |  |
| TV | 93.41% | 92.01% | +1.52% | 2,065 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Credit Card | 92.08% | 92.47% | -0.42% | 316,124 |
| PaymentMethod | Apple Pay | 90.02% | 90.19% | -0.19% | 54,874 |
| PaymentMethod | Paypal | 96.45% | 96.52% | -0.07% | 55,378 |
| PaymentMethod | Others | 98.28% | 97.93% | +0.36% | 5,477 |
| PaymentProvider | Braintree | 93.41% | 93.75% | -0.36% | 293,781 |
| PaymentProvider | ProcessOut | 91.66% | 91.81% | -0.17% | 60,625 |
| PaymentProvider | Adyen | 89.45% | 89.58% | -0.14% | 76,830 |
| PaymentProvider | No Payment | 100.0% | 97.41% | +2.66% | 534 |
| PaymentProvider | Unknown | 49.4% | 11.43% | +332.23% | 83 |

---

*Report: 2026-04-09*
