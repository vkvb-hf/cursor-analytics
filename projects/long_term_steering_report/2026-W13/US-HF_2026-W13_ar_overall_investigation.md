# AR Overall Investigation: US-HF 2026-W13

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 91.98% → 91.93% (-0.05%)  
**Volume:** 415,885 orders

## Executive Summary

**Overall:** AR Overall for US-HF declined marginally by -0.05pp (91.98% → 91.93%) in 2026-W13 on a volume of 415,885 orders, remaining within normal weekly fluctuation range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (91.48%-92.09%) | -0.05pp | ✅ |
| L1: Country Impact | US +0.05pp, no countries exceeding ±2.5% | +0.05pp | ✅ |
| L1: PaymentMethod | Others -0.52pp, Apple Pay -0.04pp | Mixed | ✅ |
| L1: PaymentProvider | Unknown -13.50pp (131 orders) | -13.50pp | ⚠️ |

**Key Findings:**
- The -0.05pp decline is a minor fluctuation; the prior week (W13) showed a +0.05pp increase, indicating normal variance
- PaymentProvider "Unknown" dropped significantly by -13.50pp (80.15% vs 92.66%), but volume is negligible at only 131 orders (0.03% of total)
- PaymentProvider "Adyen" declined -1.12pp (94.99% vs 96.06%) on low volume of 399 orders
- Primary payment flows remain stable: Braintree (+0.06pp, 382,647 orders) and Credit Card (+0.00pp, 311,435 orders)
- Overall volume decreased by ~8,218 orders week-over-week (415,885 vs 424,103)

**Action:** Monitor — The decline is minimal and within normal operating range. The PaymentProvider "Unknown" drop, while significant in rate, affects negligible volume and does not warrant escalation.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 91.93% | 415,885 | -0.05% |
| 2026-W13 | 91.98% | 424,103 | +0.05% ← REPORTED CHANGE |
| 2026-W12 | 91.93% | 433,761 | -0.17% |
| 2026-W11 | 92.09% | 444,619 | +0.14% |
| 2026-W10 | 91.96% | 457,610 | +0.34% |
| 2026-W09 | 91.65% | 455,121 | +0.19% |
| 2026-W08 | 91.48% | 453,781 | -0.20% |
| 2026-W07 | 91.66% | 470,140 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.85% | 92.8% | +0.05% | 505,599 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Others | 98.65% | 99.17% | -0.52% | 2,230 |
| PaymentMethod | Apple Pay | 84.44% | 84.47% | -0.04% | 58,012 |
| PaymentMethod | Credit Card | 92.76% | 92.75% | +0.00% | 311,435 |
| PaymentMethod | Paypal | 95.44% | 95.16% | +0.30% | 52,426 |
| PaymentProvider | Unknown | 80.15% | 92.66% | -13.50% | 131 |
| PaymentProvider | Adyen | 94.99% | 96.06% | -1.12% | 399 |
| PaymentProvider | No Payment | 100.0% | 99.96% | +0.04% | 2,065 |
| PaymentProvider | Braintree | 92.49% | 92.43% | +0.06% | 382,647 |
| PaymentProvider | ProcessOut | 86.57% | 86.25% | +0.38% | 38,861 |

---

*Report: 2026-04-10*
