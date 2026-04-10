# AR Overall Investigation: US-HF 2026-W13

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 91.98% → 91.93% (-0.05%)  
**Volume:** 415,885 orders

## Executive Summary

**Overall:** AR Overall declined marginally from 91.98% to 91.93% (-0.05 pp) in 2026-W13, representing a minor fluctuation within normal operating range across 415,885 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Volatility within ±0.34 pp range | -0.05 pp | ✅ |
| L1: Country Impact | US only market, +0.05 pp | +0.05 pp | ✅ |
| L1: PaymentMethod | Others declined -0.52 pp (2,230 vol) | -0.52 pp | ✅ |
| L1: PaymentProvider | Unknown dropped -13.50 pp (131 vol) | -13.50 pp | ⚠️ |
| L1: PaymentProvider | Adyen declined -1.12 pp (399 vol) | -1.12 pp | ✅ |

**Key Findings:**
- PaymentProvider "Unknown" experienced a significant rate drop of -13.50 pp (from 92.66% to 80.15%), but with minimal volume impact (131 orders only)
- PaymentProvider "Adyen" showed a -1.12 pp decline (from 96.06% to 94.99%), though volume remains low at 399 orders
- PaymentMethod "Others" declined -0.52 pp (from 99.17% to 98.65%) on 2,230 orders
- Primary payment flows remain stable: Braintree (+0.06 pp, 382,647 orders) and Credit Card (+0.00 pp, 311,435 orders)
- 8-week trend shows overall metric stability, ranging between 91.48% and 92.09%

**Action:** Monitor - The -0.05 pp decline is within normal weekly variance. The PaymentProvider "Unknown" drop warrants observation but has negligible volume impact (<0.1% of total orders).

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
