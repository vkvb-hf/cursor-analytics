# AR Overall Investigation: US-HF 2026-W14

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 91.98% → 91.93% (-0.05%)  
**Volume:** 415,885 orders

## Executive Summary

**Overall:** AR Overall declined slightly from 91.98% to 91.93% (-0.05 pp) in W14, representing a minor decrease within normal weekly fluctuation range across 415,885 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (91.48%-92.09%) | -0.05 pp | ✅ |
| L1: Country Breakdown | US declined -0.07 pp | -0.07 pp | ✅ |
| L1: PaymentMethod | All methods within ±0.29 pp | -0.29 pp max | ✅ |
| L1: PaymentProvider | Unknown improved +8.23 pp (low volume) | +8.23 pp | ⚠️ |

**Key Findings:**
- The -0.05 pp decline is minimal and consistent with the 8-week trend pattern showing normal oscillation between 91.48% and 92.09%
- No countries exceeded the ±2.5% threshold; US (sole country) declined only -0.07 pp
- PaymentMethod "Others" showed the largest decline at -0.29 pp but represents only 2,202 orders (0.5% of volume)
- ProcessOut provider improved +0.38 pp (41,023 orders), partially offsetting Braintree's -0.05 pp decline (372,325 orders)
- Unknown PaymentProvider showed +8.23 pp improvement but volume is negligible (249 orders)

**Action:** Monitor - The decline is within normal weekly variance and no dimension exceeds concerning thresholds. Continue standard monitoring for W15.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 91.93% | 415,885 | -0.05% ← REPORTED CHANGE |
| 2026-W13 | 91.98% | 424,103 | +0.05% |
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
| US | 92.79% | 92.85% | -0.07% | 497,052 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Others | 98.37% | 98.65% | -0.29% | 2,202 |
| PaymentMethod | Paypal | 95.34% | 95.44% | -0.11% | 51,200 |
| PaymentMethod | Credit Card | 92.7% | 92.76% | -0.06% | 305,088 |
| PaymentMethod | Apple Pay | 84.57% | 84.44% | +0.15% | 57,395 |
| PaymentProvider | Braintree | 92.44% | 92.49% | -0.05% | 372,325 |
| PaymentProvider | No Payment | 100.0% | 100.0% | +0.00% | 1,924 |
| PaymentProvider | Adyen | 95.05% | 94.99% | +0.07% | 364 |
| PaymentProvider | ProcessOut | 86.9% | 86.57% | +0.38% | 41,023 |
| PaymentProvider | Unknown | 86.75% | 80.15% | +8.23% | 249 |

---

*Report: 2026-04-09*
