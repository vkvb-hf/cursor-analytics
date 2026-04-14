# AR Initial (LL0) Investigation: US-HF 2026-W15

**Metric:** AR Initial (LL0)  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 88.96% → 89.73% (+0.87%)  
**Volume:** 12,186 orders

## Executive Summary

**Overall:** AR Initial (LL0) improved from 88.96% to 89.73% (+0.77 pp) in W15, representing a positive week-over-week recovery and reaching the highest rate in the 8-week observation period.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: US-HF Overall | +0.77 pp W15 vs W14 | +0.87% | ✅ |
| L1: Country (US) | +0.79 pp (69.72% → 70.51%) | +1.13% | ✅ |
| L1: PaymentMethod | All methods stable or improved | +0.00% to +1.02% | ✅ |
| L1: PaymentProvider | All providers stable or improved | +0.00% to +1.06% | ✅ |

**Key Findings:**
- AR Initial rate reached 89.73% in W15, the highest point in the 8-week trend, recovering from the W12-W13 dip (87.69%)
- Credit Card payments showed the strongest improvement among payment methods (+1.02%, rate: 90.4%) with the highest volume (6,597 orders)
- ProcessOut provider improved by +1.06% (89.69% → 90.64%) handling 6,454 orders, contributing significantly to overall gains
- No countries or dimensions exceeded the ±2.5% threshold, indicating broad-based stable improvement
- Volume decreased to 12,186 orders from a peak of 19,259 in W10, though rate performance remains strong

**Action:** Monitor – The metric shows healthy improvement with no anomalies requiring investigation. Continue tracking to confirm the upward trend sustains through W16.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 89.73% | 12,186 | +0.87% ← REPORTED CHANGE |
| 2026-W14 | 88.96% | 11,570 | +1.45% |
| 2026-W13 | 87.69% | 10,899 | -1.18% |
| 2026-W12 | 88.74% | 14,793 | -1.52% |
| 2026-W11 | 90.11% | 15,868 | +0.95% |
| 2026-W10 | 89.26% | 19,259 | +0.01% |
| 2026-W09 | 89.25% | 18,657 | -0.36% |
| 2026-W08 | 89.57% | 18,802 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 70.51% | 69.72% | +1.13% | 23,822 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Others | 98.07% | 98.06% | +0.00% | 414 |
| PaymentMethod | Paypal | 90.39% | 90.14% | +0.28% | 947 |
| PaymentMethod | Apple Pay | 87.72% | 87.13% | +0.68% | 4,228 |
| PaymentMethod | Credit Card | 90.4% | 89.49% | +1.02% | 6,597 |
| PaymentProvider | Adyen | 100.0% | nan% | +nan% | 1 |
| PaymentProvider | No Payment | 100.0% | 100.0% | +0.00% | 100 |
| PaymentProvider | Unknown | 97.45% | 97.13% | +0.33% | 314 |
| PaymentProvider | Braintree | 87.98% | 87.56% | +0.48% | 5,317 |
| PaymentProvider | ProcessOut | 90.64% | 89.69% | +1.06% | 6,454 |

---

*Report: 2026-04-14*
