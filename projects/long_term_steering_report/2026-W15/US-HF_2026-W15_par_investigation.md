# PAR Investigation: US-HF 2026-W15

**Metric:** PAR  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 93.63% → 93.76% (+0.14%)  
**Volume:** 408,629 orders

## Executive Summary

**Overall:** PAR improved by +0.14 pp (93.63% → 93.76%) in 2026-W15, continuing a steady upward trend over the past 8 weeks.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | 8-week trend direction | +0.63 pp since W08 | ✅ |
| L1: Country Impact | US exceeds ±2.5% threshold | +0.34 pp | ✅ |
| L1: PaymentMethod | Any dimension exceeds ±2.5% | Max Δ: -0.70 pp (Others) | ✅ |
| L1: PaymentProvider | Any dimension exceeds ±2.5% | -3.34 pp (Unknown) | ⚠️ |

**Key Findings:**
- PAR has shown consistent improvement for 6 consecutive weeks, rising from 93.13% (W08) to 93.76% (W15)
- PaymentProvider "Unknown" declined significantly by -3.34 pp (95.56% → 92.37%), though volume is minimal at 354 orders
- US improved by +0.34 pp (92.78% → 93.1%) with 492,811 orders, driving the overall positive trend
- Braintree, the dominant payment provider (363,784 orders, 89% of volume), improved by +0.15 pp
- Apple Pay remains the lowest-performing payment method at 87.63%, though it improved by +0.29 pp

**Action:** Monitor — The metric shows healthy improvement with no significant negative signals at scale. The PaymentProvider "Unknown" decline warrants observation but represents <0.1% of volume.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 93.76% | 408,629 | +0.14% ← REPORTED CHANGE |
| 2026-W14 | 93.63% | 415,885 | +0.05% |
| 2026-W13 | 93.58% | 424,103 | +0.03% |
| 2026-W12 | 93.55% | 433,761 | -0.04% |
| 2026-W11 | 93.59% | 444,619 | +0.22% |
| 2026-W10 | 93.38% | 457,610 | +0.24% |
| 2026-W09 | 93.16% | 455,121 | +0.03% |
| 2026-W08 | 93.13% | 453,781 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 93.1% | 92.78% | +0.34% | 492,811 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Others | 98.67% | 99.36% | -0.70% | 2,398 |
| PaymentMethod | Credit Card | 94.44% | 94.36% | +0.09% | 300,595 |
| PaymentMethod | Paypal | 96.25% | 96.05% | +0.21% | 50,099 |
| PaymentMethod | Apple Pay | 87.63% | 87.38% | +0.29% | 55,537 |
| PaymentProvider | Unknown | 92.37% | 95.56% | -3.34% | 354 |
| PaymentProvider | Adyen | 96.34% | 96.43% | -0.09% | 383 |
| PaymentProvider | No Payment | 100.0% | 100.0% | +0.00% | 2,010 |
| PaymentProvider | Braintree | 94.24% | 94.1% | +0.15% | 363,784 |
| PaymentProvider | ProcessOut | 89.26% | 89.0% | +0.29% | 42,098 |

---

*Report: 2026-04-14*
