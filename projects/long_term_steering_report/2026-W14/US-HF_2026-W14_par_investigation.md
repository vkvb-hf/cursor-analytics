# PAR Investigation: US-HF 2026-W14

**Metric:** PAR  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 93.59% → 93.63% (+0.04%)  
**Volume:** 415,885 orders

## Executive Summary

## Executive Summary

**Overall:** PAR metric showed marginal improvement from 93.59% to 93.63% (+0.04 pp) in W14, continuing a stable upward trend observed over the past 5 weeks.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | 8-week trend stable, +0.25 pp from W07 | +0.04 pp | ✅ |
| L1: Country | US slightly declined (-0.07 pp) | -0.07 pp | ✅ |
| L1: Payment Method | All methods within normal range | Max +0.39 pp (Apple Pay) | ✅ |
| L1: Payment Provider | Unknown provider spike (+8.88 pp) | +8.88 pp | ⚠️ |

**Key Findings:**
- The +0.04 pp week-over-week improvement continues a consistent upward trajectory since W08 (93.13% → 93.63%, +0.50 pp over 6 weeks)
- Volume decreased by 8,218 orders (424,103 → 415,885) representing a -1.9% decline in order volume
- PaymentProvider "Unknown" showed an unusually large improvement of +8.88 pp (87.79% → 95.58%), though on minimal volume (249 orders)
- Apple Pay showed the largest improvement among payment methods at +0.39 pp (87.04% → 87.38%) but remains the lowest-performing method at 87.38%
- No countries exceeded the ±2.5% threshold; US showed a minor decline of -0.07 pp

**Action:** Monitor — The overall metric improvement is positive and within expected variance. The "Unknown" payment provider anomaly warrants observation but impacts negligible volume (<0.1% of orders).

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 93.63% | 415,885 | +0.04% ← REPORTED CHANGE |
| 2026-W13 | 93.59% | 424,103 | +0.04% |
| 2026-W12 | 93.55% | 433,761 | -0.04% |
| 2026-W11 | 93.59% | 444,619 | +0.22% |
| 2026-W10 | 93.38% | 457,610 | +0.24% |
| 2026-W09 | 93.16% | 455,121 | +0.03% |
| 2026-W08 | 93.13% | 453,781 | -0.27% |
| 2026-W07 | 93.38% | 470,140 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.79% | 92.85% | -0.07% | 497,052 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Paypal | 96.05% | 96.06% | -0.01% | 51,200 |
| PaymentMethod | Credit Card | 94.36% | 94.35% | +0.01% | 305,088 |
| PaymentMethod | Others | 99.36% | 99.19% | +0.17% | 2,202 |
| PaymentMethod | Apple Pay | 87.38% | 87.04% | +0.39% | 57,395 |
| PaymentProvider | No Payment | 100.0% | 100.0% | +0.00% | 1,924 |
| PaymentProvider | ProcessOut | 89.01% | 88.93% | +0.08% | 41,023 |
| PaymentProvider | Braintree | 94.1% | 94.02% | +0.09% | 372,325 |
| PaymentProvider | Adyen | 96.43% | 95.74% | +0.72% | 364 |
| PaymentProvider | Unknown | 95.58% | 87.79% | +8.88% | 249 |

---

*Report: 2026-04-09*
