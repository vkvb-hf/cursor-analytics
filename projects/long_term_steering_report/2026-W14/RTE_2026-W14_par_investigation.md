# PAR Investigation: RTE 2026-W14

**Metric:** PAR  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 94.94% → 94.76% (-0.19%)  
**Volume:** 431,853 orders

## Executive Summary

**Overall:** PAR declined by 0.19 percentage points (94.94% → 94.76%) in 2026-W14, continuing a two-week downward trend from the recent peak of 95.18% in W12.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 8-Week Trend | Rate above 8-week average (~93.9%) | -0.19 pp | ✅ |
| Country Variance | Any country ±2.5% threshold | None exceeded | ✅ |
| Top Volume Country (FJ) | Rate stability | -0.37 pp | ✅ |
| Payment Method | Major method stability | Credit Card -0.28 pp | ⚠️ |
| Payment Provider | Provider stability | ProcessOut -0.42 pp | ⚠️ |

**Key Findings:**
- TK experienced the largest rate decline at -1.63 pp (90.12% → 88.65%), though volume is low at 1,779 orders
- TZ also showed significant decline of -1.43 pp (91.42% → 90.11%) with 3,013 orders
- Credit Card payments (73% of volume at 316,124 orders) declined -0.28 pp, driving the majority of the overall drop
- ProcessOut provider showed the steepest decline among major providers at -0.42 pp (93.83% → 93.44%)
- FJ, representing 92% of total volume (397,332 orders), declined -0.37 pp and is the primary contributor to the overall metric movement

**Action:** Monitor - The decline is modest (-0.19 pp) and the current rate remains above the 8-week average. Continue monitoring Credit Card payment method and ProcessOut provider performance. If the downward trend continues into W15, escalate for deeper investigation into FJ market performance.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 94.76% | 431,853 | -0.19% ← REPORTED CHANGE |
| 2026-W13 | 94.94% | 442,530 | -0.25% |
| 2026-W12 | 95.18% | 443,994 | +0.08% |
| 2026-W11 | 95.1% | 458,408 | +1.80% |
| 2026-W10 | 93.42% | 467,998 | +0.17% |
| 2026-W09 | 93.26% | 466,696 | +0.20% |
| 2026-W08 | 93.07% | 462,049 | -0.04% |
| 2026-W07 | 93.11% | 474,461 | - |

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
| PaymentMethod | Credit Card | 94.58% | 94.84% | -0.28% | 316,124 |
| PaymentMethod | Apple Pay | 92.36% | 92.37% | -0.01% | 54,874 |
| PaymentMethod | Paypal | 97.71% | 97.64% | +0.07% | 55,378 |
| PaymentMethod | Others | 99.05% | 98.35% | +0.71% | 5,477 |
| PaymentProvider | ProcessOut | 93.44% | 93.83% | -0.42% | 60,625 |
| PaymentProvider | Adyen | 92.88% | 93.0% | -0.13% | 76,830 |
| PaymentProvider | Braintree | 95.51% | 95.62% | -0.11% | 293,781 |
| PaymentProvider | No Payment | 100.0% | 97.41% | +2.66% | 534 |
| PaymentProvider | Unknown | 79.52% | 37.14% | +114.09% | 83 |

---

*Report: 2026-04-10*
