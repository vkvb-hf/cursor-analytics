# AR Overall Investigation: US-HF 2026-W15

**Metric:** AR Overall  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 91.93% → 92.23% (+0.33%)  
**Volume:** 408,629 orders

## Executive Summary

**Overall:** AR Overall improved by +0.33 percentage points (91.93% → 92.23%) in W15, continuing a positive upward trend from the 8-week low of 91.48% in W08.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Sustained improvement trend | +0.75pp from W08 | ✅ |
| L1: Country | US within ±2.5% threshold | +0.34pp | ✅ |
| L1: Payment Method | All methods stable or improving | +0.25pp to +0.68pp | ✅ |
| L1: Payment Provider | Unknown provider spike | +4.44pp | ⚠️ |

**Key Findings:**
- US showed healthy improvement of +0.34pp (92.78% → 93.1%) on 492,811 orders, driving overall metric gains
- Apple Pay demonstrated the strongest improvement among payment methods at +0.68pp (84.57% → 85.14%), though it remains the lowest-performing method at 85.14%
- Braintree, handling 89% of volume (363,784 orders), improved +0.34pp (92.44% → 92.76%)
- Unknown payment provider showed an anomalous +4.44pp spike (87.1% → 90.96%), but on minimal volume (354 orders)
- Volume declined 1.7% week-over-week (415,885 → 408,629), continuing a gradual downward trend from W08

**Action:** Monitor — The metric shows sustained improvement with no dimension exceeding the ±2.5% threshold on meaningful volume. Continue tracking Apple Pay performance as the lowest-converting payment method.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 92.23% | 408,629 | +0.33% ← REPORTED CHANGE |
| 2026-W14 | 91.93% | 415,885 | -0.05% |
| 2026-W13 | 91.98% | 424,103 | +0.05% |
| 2026-W12 | 91.93% | 433,761 | -0.17% |
| 2026-W11 | 92.09% | 444,619 | +0.14% |
| 2026-W10 | 91.96% | 457,610 | +0.34% |
| 2026-W09 | 91.65% | 455,121 | +0.19% |
| 2026-W08 | 91.48% | 453,781 | - |

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
| PaymentMethod | Others | 98.25% | 98.41% | -0.16% | 2,398 |
| PaymentMethod | Paypal | 95.58% | 95.34% | +0.25% | 50,099 |
| PaymentMethod | Credit Card | 92.93% | 92.69% | +0.25% | 300,595 |
| PaymentMethod | Apple Pay | 85.14% | 84.57% | +0.68% | 55,537 |
| PaymentProvider | Adyen | 95.04% | 95.05% | -0.02% | 383 |
| PaymentProvider | No Payment | 100.0% | 100.0% | +0.00% | 2,010 |
| PaymentProvider | Braintree | 92.76% | 92.44% | +0.34% | 363,784 |
| PaymentProvider | ProcessOut | 87.24% | 86.9% | +0.40% | 42,098 |
| PaymentProvider | Unknown | 90.96% | 87.1% | +4.44% | 354 |

---

*Report: 2026-04-14*
