# AR Overall Investigation: US-HF 2026-W14

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 91.98% → 91.93% (-0.05%)  
**Volume:** 415,885 orders

## Executive Summary

**Overall:** AR Overall declined marginally by -0.05 percentage points (91.98% → 91.93%) on a volume of 415,885 orders, representing a minor fluctuation within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (91.48%-92.09%) | -0.05 pp | ✅ |
| L1: Country Breakdown | US only, no countries exceeding ±2.5% threshold | -0.06 pp | ✅ |
| L1: Payment Method | Minor declines across most methods | -0.29 pp max (Others) | ✅ |
| L1: Payment Provider | Braintree stable, ProcessOut improved | -0.05 pp to +8.23 pp | ✅ |

**Key Findings:**
- The -0.05 pp decline is consistent with normal week-over-week volatility observed in the 8-week trend (range: -0.20 pp to +0.34 pp)
- PaymentMethod "Others" showed the largest decline at -0.29 pp (98.65% → 98.37%), but represents minimal volume (2,202 orders)
- Braintree, the dominant payment provider (372,325 orders, ~90% of volume), declined only -0.05 pp (92.49% → 92.44%)
- ProcessOut showed improvement of +0.38 pp (86.57% → 86.90%) on 41,023 orders
- Apple Pay improved slightly by +0.15 pp (84.44% → 84.57%) despite having the lowest rate among major payment methods

**Action:** Monitor – No investigation required. The change is within normal operating variance, no dimensions exceeded alert thresholds, and the 8-week trend shows stable performance.

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
| US | 92.79% | 92.85% | -0.06% | 497,052 |  |

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
