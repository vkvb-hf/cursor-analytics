# PAR Investigation: US-HF 2026-W12

**Metric:** PAR  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 93.59% → 93.63% (+0.04%)  
**Volume:** 415,885 orders

## Executive Summary

## Executive Summary

**Overall:** PAR (Payment Acceptance Rate) showed a slight improvement from 93.59% to 93.63% (+0.04 pp) in US-HF for week 2026-W12, with a total volume of 415,885 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Stable trend with minor fluctuations | +0.04 pp | ✅ |
| L1: Country (US) | US rate declined | -0.17 pp | ⚠️ |
| L1: Payment Method | Most methods stable; Apple Pay improved | -0.17 pp to +0.24 pp | ✅ |
| L1: Payment Provider | ProcessOut significant improvement; Braintree slight decline | -0.11 pp to +3.55 pp | ⚠️ |

**Key Findings:**
- ProcessOut showed a notable improvement of +3.55 pp (86.04% → 89.10%) with 38,294 orders, potentially driving overall gains
- Braintree, the dominant payment provider handling 392,447 orders, declined by -0.11 pp (94.04% → 93.94%)
- Apple Pay improved by +0.24 pp (86.77% → 86.98%) but remains the lowest-performing payment method at 86.98%
- The US country-level rate shows a -0.17 pp decline despite the overall HF-level improvement, suggesting mix effects
- No dimensions exceeded the ±2.5% threshold flag, indicating no critical anomalies

**Action:** Monitor — The overall metric shows slight improvement and remains stable within normal operating range. Continue tracking ProcessOut's positive trend and Braintree's minor decline given its high volume impact.

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
