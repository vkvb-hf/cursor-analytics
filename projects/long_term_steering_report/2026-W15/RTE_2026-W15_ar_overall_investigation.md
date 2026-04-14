# AR Overall Investigation: RTE 2026-W15

**Metric:** AR Overall  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 92.46% → 92.83% (+0.40%)  
**Volume:** 421,406 orders

## Executive Summary

**Overall:** AR Overall improved from 92.46% to 92.83% (+0.37 pp) in W15, recovering partially from the prior week's decline, with volume of 421,406 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (91.07%-93.20%) | +0.37 pp | ✅ |
| L1: Country Breakdown | 1 country exceeds ±2.5% threshold (TK) | TK: +7.54 pp | ⚠️ |
| L1: Payment Method | All methods within normal variance | -0.77 pp to +0.48 pp | ✅ |
| L1: Payment Provider | Unknown provider shows high volatility | +35.88 pp (low volume) | ⚠️ |

**Key Findings:**
- TK showed significant improvement of +7.54 pp (88.65% → 95.33%) on 1,950 orders, flagged as outlier exceeding ±2.5% threshold
- TV experienced the largest decline at -1.37 pp (93.41% → 92.14%) but on low volume (1,895 orders)
- FJ, the highest volume country (388,956 orders / 92% of total), improved slightly by +0.38 pp, driving overall metric recovery
- "Unknown" Payment Provider shows +35.88 pp change but is statistically insignificant (131 orders)
- Overall trend shows stabilization after two consecutive weeks of decline (W13-W14)

**Action:** Monitor - The improvement is within normal operating range and primarily driven by stable performance in high-volume country FJ. Continue monitoring TK to confirm if the +7.54 pp improvement is sustained or anomalous.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 92.83% | 421,406 | +0.40% ← REPORTED CHANGE |
| 2026-W14 | 92.46% | 431,853 | -0.34% |
| 2026-W13 | 92.78% | 442,530 | -0.33% |
| 2026-W12 | 93.09% | 443,994 | -0.12% |
| 2026-W11 | 93.2% | 458,408 | +1.80% |
| 2026-W10 | 91.55% | 467,998 | +0.24% |
| 2026-W09 | 91.33% | 466,696 | +0.29% |
| 2026-W08 | 91.07% | 462,049 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TV | 92.14% | 93.41% | -1.37% | 1,895 |  |
| YE | 87.77% | 88.15% | -0.43% | 42,126 |  |
| FJ | 93.97% | 93.62% | +0.38% | 388,956 |  |
| CF | 94.14% | 93.47% | +0.72% | 51,881 |  |
| TZ | 91.69% | 90.11% | +1.76% | 2,660 |  |
| TO | 86.67% | 84.89% | +2.11% | 3,204 |  |
| TK | 95.33% | 88.65% | +7.54% | 1,950 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TK

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Others | 97.55% | 98.3% | -0.77% | 5,340 |
| PaymentMethod | Paypal | 96.65% | 96.45% | +0.21% | 53,618 |
| PaymentMethod | Apple Pay | 90.34% | 90.01% | +0.37% | 53,550 |
| PaymentMethod | Credit Card | 92.52% | 92.08% | +0.48% | 308,898 |
| PaymentProvider | No Payment | 100.0% | 100.0% | +0.00% | 510 |
| PaymentProvider | ProcessOut | 91.73% | 91.65% | +0.08% | 64,367 |
| PaymentProvider | Adyen | 89.86% | 89.45% | +0.46% | 74,351 |
| PaymentProvider | Braintree | 93.87% | 93.41% | +0.49% | 282,047 |
| PaymentProvider | Unknown | 67.94% | 50.0% | +35.88% | 131 |

---

*Report: 2026-04-14*
