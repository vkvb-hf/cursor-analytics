# AR Overall Investigation: US-HF 2026-W12

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 91.98% → 91.93% (-0.05%)  
**Volume:** 415,885 orders

## Executive Summary

**Overall:** AR Overall declined by -0.05 percentage points (91.98% → 91.93%) on a volume of 415,885 orders in 2026-W12, representing a minor week-over-week decrease within normal fluctuation range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (91.48%-92.09%) | -0.05 pp | ✅ |
| L1: Country Breakdown | US declined -0.17 pp, no country exceeded ±2.5% threshold | -0.17 pp | ✅ |
| L1: PaymentMethod | Credit Card declined -0.21 pp (highest volume impact) | -0.21 pp | ⚠️ |
| L1: PaymentProvider | Braintree declined -0.15 pp (392,447 orders) | -0.15 pp | ⚠️ |
| L1: PaymentProvider | ProcessOut improved +2.85 pp (38,294 orders) | +2.85 pp | ✅ |

**Key Findings:**
- Credit Card payment method showed the largest decline at -0.21 pp, impacting 316,708 orders (76% of volume)
- Braintree, the dominant payment provider with 392,447 orders, declined -0.15 pp contributing to the overall drop
- ProcessOut showed significant improvement of +2.85 pp, though on smaller volume (38,294 orders)
- Unknown PaymentProvider had the steepest decline at -0.56 pp but minimal volume impact (259 orders)
- The 8-week trend shows the current rate (91.93%) is within normal operating range, with W11 being the recent peak at 92.09%

**Action:** Monitor – The decline is minor (-0.05 pp) and within normal weekly fluctuation. Continue monitoring Credit Card and Braintree performance over the next 1-2 weeks to determine if this is a sustained trend or normal variance.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 91.93% | 415,885 | -0.05% |
| 2026-W13 | 91.98% | 424,103 | +0.05% |
| 2026-W12 | 91.93% | 433,761 | -0.17% ← REPORTED CHANGE |
| 2026-W11 | 92.09% | 444,619 | +0.14% |
| 2026-W10 | 91.96% | 457,610 | +0.34% |
| 2026-W09 | 91.65% | 455,121 | +0.19% |
| 2026-W08 | 91.48% | 453,781 | -0.20% |
| 2026-W07 | 91.66% | 470,140 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.8% | 92.95% | -0.17% | 517,442 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Others | 99.17% | 99.39% | -0.22% | 2,647 |
| PaymentMethod | Credit Card | 92.75% | 92.94% | -0.21% | 316,708 |
| PaymentMethod | Paypal | 95.16% | 95.19% | -0.03% | 53,733 |
| PaymentMethod | Apple Pay | 84.47% | 84.45% | +0.03% | 60,673 |
| PaymentProvider | Unknown | 92.66% | 93.19% | -0.56% | 259 |
| PaymentProvider | Braintree | 92.43% | 92.58% | -0.15% | 392,447 |
| PaymentProvider | No Payment | 99.96% | 100.0% | -0.04% | 2,355 |
| PaymentProvider | Adyen | 96.06% | 93.81% | +2.40% | 406 |
| PaymentProvider | ProcessOut | 86.25% | 83.86% | +2.85% | 38,294 |

---

*Report: 2026-04-10*
