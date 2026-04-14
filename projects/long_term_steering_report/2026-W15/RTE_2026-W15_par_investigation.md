# PAR Investigation: RTE 2026-W15

**Metric:** PAR  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 94.75% → 94.87% (+0.13%)  
**Volume:** 421,406 orders

## Executive Summary

## Executive Summary

**Overall:** PAR improved from 94.75% to 94.87% (+0.13 pp) in 2026-W15, continuing a modest recovery after the dip observed in W13-W14, though still below the 8-week high of 95.18% reached in W12.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Sustained improvement after W10 baseline (~93%) | +0.13 pp | ✅ |
| L1: Country Breakdown | 6 of 7 countries within threshold; TK flagged | TK: +7.54 pp | ⚠️ |
| L1: PaymentMethod | All methods stable, minor variations | -0.80 pp to +0.16 pp | ✅ |
| L1: PaymentProvider | Unknown provider significant decline, low volume | Unknown: -9.48 pp | ⚠️ |

**Key Findings:**
- TK showed an exceptional +7.54 pp improvement (88.65% → 95.33%), though volume remains low at 1,950 orders — warrants investigation to understand if this is sustainable or anomalous
- PaymentProvider "Unknown" declined sharply by -9.48 pp (79.27% → 71.76%), but with only 131 orders, impact on overall PAR is negligible
- FJ dominates volume (388,956 orders, 92% of total) and improved slightly (+0.38 pp), driving the overall metric improvement
- TV experienced the largest decline among countries at -1.37 pp (93.41% → 92.14%), though low volume (1,895 orders) limits impact
- Overall volume decreased by 10,447 orders (-2.4%) compared to W14, continuing a downward volume trend since W11

**Action:** Monitor — The +0.13 pp improvement is positive but modest. Continue tracking TK for sustained performance and investigate the "Unknown" PaymentProvider decline if volume increases.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 94.87% | 421,406 | +0.13% ← REPORTED CHANGE |
| 2026-W14 | 94.75% | 431,853 | -0.20% |
| 2026-W13 | 94.94% | 442,530 | -0.25% |
| 2026-W12 | 95.18% | 443,994 | +0.08% |
| 2026-W11 | 95.1% | 458,408 | +1.80% |
| 2026-W10 | 93.42% | 467,998 | +0.17% |
| 2026-W09 | 93.26% | 466,696 | +0.20% |
| 2026-W08 | 93.07% | 462,049 | - |

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
| PaymentMethod | Others | 98.26% | 99.05% | -0.80% | 5,340 |
| PaymentMethod | Paypal | 97.72% | 97.71% | +0.01% | 53,618 |
| PaymentMethod | Credit Card | 94.73% | 94.58% | +0.16% | 308,898 |
| PaymentMethod | Apple Pay | 92.51% | 92.36% | +0.16% | 53,550 |
| PaymentProvider | Unknown | 71.76% | 79.27% | -9.48% | 131 |
| PaymentProvider | No Payment | 100.0% | 100.0% | +0.00% | 510 |
| PaymentProvider | ProcessOut | 93.45% | 93.43% | +0.02% | 64,367 |
| PaymentProvider | Braintree | 95.66% | 95.51% | +0.15% | 282,047 |
| PaymentProvider | Adyen | 93.13% | 92.88% | +0.27% | 74,351 |

---

*Report: 2026-04-14*
