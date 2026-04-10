# AR Overall Investigation: US-HF 2026-W12

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 91.98% → 91.93% (-0.05%)  
**Volume:** 415,885 orders

## Executive Summary

**Overall:** AR Overall declined by -0.05pp (91.98% → 91.93%) on volume of 415,885 orders in US-HF for 2026-W12.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal fluctuation (91.48%-92.09% range) | -0.05pp | ✅ |
| L1: Country | US declined -0.17pp | -0.17pp | ✅ |
| L1: PaymentMethod | Credit Card largest impact (-0.21pp on 316,708 vol) | -0.21pp | ✅ |
| L1: PaymentProvider | ProcessOut improved +2.85pp; Unknown declined -0.56pp | Mixed | ⚠️ |

**Key Findings:**
- US showed a -0.17pp decline (92.95% → 92.8%) representing the entire volume impact
- Credit Card payment method declined -0.21pp (92.94% → 92.75%) on the highest volume (316,708 orders), driving the overall drop
- PaymentProvider "Unknown" showed the largest negative delta at -0.56pp, though on minimal volume (259 orders)
- ProcessOut improved significantly by +2.85pp (83.86% → 86.25%) on 38,294 orders, partially offsetting declines
- The 8-week trend shows the rate remains within the established range (91.48%-92.09%), with W12 matching W14 at 91.93%

**Action:** Monitor – The decline is minor (-0.05pp) and within normal weekly fluctuation patterns. Credit Card performance via Braintree should be tracked for continued degradation in the next 1-2 weeks.

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
