# PAR Investigation: RTE 2026-W14

**Metric:** PAR  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 94.94% → 94.76% (-0.19%)  
**Volume:** 431,853 orders

## Executive Summary

**Overall:** PAR declined from 94.94% to 94.76% (-0.19pp) in W14 with 431,853 orders, continuing a downward trend for the second consecutive week.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Weekly Trend | 2-week consecutive decline (W13: -0.25%, W14: -0.19%) | -0.19pp | ⚠️ |
| L1: Country Breakdown | No country exceeds ±2.5% threshold | Largest: TK -1.63pp | ✅ |
| L1: Dimension Scan | No major anomalies in core payment methods/providers | Credit Card -0.28pp | ✅ |

**Key Findings:**
- **Consecutive weekly decline:** PAR has dropped for two straight weeks (W12: 95.18% → W13: 94.94% → W14: 94.76%), losing 0.42pp total
- **Volume contraction:** Order volume decreased from 442,530 (W13) to 431,853 (W14), a reduction of ~10,700 orders (-2.4%)
- **FJ drives overall performance:** FJ represents 92% of volume (397,332 orders) and declined -0.37pp, directly impacting the aggregate metric
- **Credit Card payment softness:** Credit Card (73% of volume at 316,124 orders) declined -0.28pp, contributing most to the overall drop
- **ProcessOut underperformance:** Among payment providers, ProcessOut showed the largest meaningful decline at -0.42pp (60,625 orders)

**Action:** Monitor — The decline is modest (-0.19pp) with no dimension exceeding alert thresholds. However, track the consecutive weekly decline pattern; if W15 continues the trend, escalate for deeper investigation into FJ/Credit Card/ProcessOut performance.

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

*Report: 2026-04-09*
