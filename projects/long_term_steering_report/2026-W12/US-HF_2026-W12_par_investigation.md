# PAR Investigation: US-HF 2026-W12

**Metric:** PAR  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 93.59% → 93.63% (+0.04%)  
**Volume:** 415,885 orders

## Executive Summary

**Overall:** PAR improved marginally by +0.04 pp (93.59% → 93.63%) on volume of 415,885 orders in 2026-W12, continuing a stable trend within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal variance (93.13%-93.63% range) | +0.04 pp | ✅ |
| L1: Country | US at 92.8%, down -0.17 pp | -0.17 pp | ✅ |
| L1: Payment Method | Apple Pay improved +0.24 pp; Others declined -0.17 pp | Mixed | ✅ |
| L1: Payment Provider | ProcessOut improved +3.55 pp; Braintree declined -0.11 pp | Mixed | ⚠️ |

**Key Findings:**
- ProcessOut shows significant improvement of +3.55 pp (86.04% → 89.10%) on 38,294 orders, exceeding the ±2.5% threshold
- Braintree, the dominant provider (392,447 orders), declined slightly by -0.11 pp (94.04% → 93.94%)
- Apple Pay improved +0.24 pp (86.77% → 86.98%) but remains the lowest-performing payment method at 86.98%
- US country-level rate declined -0.17 pp (92.95% → 92.80%), though no countries exceeded the ±2.5% alert threshold
- Volume continues declining trend (470,140 in W07 → 415,885 in W12), down ~11.5% over 8 weeks

**Action:** Monitor – The overall metric is stable with minor positive movement. Continue tracking ProcessOut's improvement trajectory and Apple Pay's below-average performance.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 93.63% | 415,885 | +0.04% |
| 2026-W13 | 93.59% | 424,103 | +0.04% |
| 2026-W12 | 93.55% | 433,761 | -0.04% ← REPORTED CHANGE |
| 2026-W11 | 93.59% | 444,619 | +0.22% |
| 2026-W10 | 93.38% | 457,610 | +0.24% |
| 2026-W09 | 93.16% | 455,121 | +0.03% |
| 2026-W08 | 93.13% | 453,781 | -0.27% |
| 2026-W07 | 93.38% | 470,140 | - |

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
| PaymentMethod | Others | 99.28% | 99.45% | -0.17% | 2,647 |
| PaymentMethod | Credit Card | 94.38% | 94.45% | -0.08% | 316,708 |
| PaymentMethod | Paypal | 95.79% | 95.81% | -0.02% | 53,733 |
| PaymentMethod | Apple Pay | 86.98% | 86.77% | +0.24% | 60,673 |
| PaymentProvider | Braintree | 93.94% | 94.04% | -0.11% | 392,447 |
| PaymentProvider | Unknown | 93.82% | 93.91% | -0.09% | 259 |
| PaymentProvider | No Payment | 99.96% | 100.0% | -0.04% | 2,355 |
| PaymentProvider | Adyen | 96.55% | 95.54% | +1.05% | 406 |
| PaymentProvider | ProcessOut | 89.1% | 86.04% | +3.55% | 38,294 |

---

*Report: 2026-04-10*
