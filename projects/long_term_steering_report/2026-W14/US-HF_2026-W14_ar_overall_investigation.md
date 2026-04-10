# AR Overall Investigation: US-HF 2026-W14

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 91.98% → 91.93% (-0.05%)  
**Volume:** 415,885 orders

## Executive Summary

**Overall:** AR Overall declined by -0.05 percentage points (91.98% → 91.93%) on volume of 415,885 orders in W14, representing a minor fluctuation within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (91.48%-92.09%) | -0.05pp | ✅ |
| L1: Country Breakdown | US declined -0.07pp, no countries exceed ±2.5% threshold | -0.07pp | ✅ |
| L1: Payment Method | All methods stable; largest decline Others -0.29pp on low volume | -0.29pp | ✅ |
| L1: Payment Provider | Braintree (primary) declined -0.05pp; Unknown improved +8.23pp on 249 orders | -0.05pp | ✅ |

**Key Findings:**
- The -0.05pp decline matches the primary payment provider Braintree's decline (-0.05pp on 372,325 orders), indicating this is the main contributor
- US is the sole country and showed a -0.07pp decline (92.85% → 92.79%), driving the overall metric movement
- Apple Pay showed slight improvement (+0.15pp) while Credit Card (-0.06pp) and PayPal (-0.11pp) declined marginally
- ProcessOut improved +0.38pp (86.57% → 86.90%) on 41,023 orders, partially offsetting Braintree's decline
- Volume decreased by ~8,200 orders week-over-week (424,103 → 415,885), continuing a multi-week downward volume trend

**Action:** Monitor — The decline is minimal (-0.05pp), within normal weekly variance, and no dimensions exceed alert thresholds. Continue standard monitoring.

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

*Report: 2026-04-10*
