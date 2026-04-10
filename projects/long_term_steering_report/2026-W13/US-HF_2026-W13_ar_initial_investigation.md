# AR Initial (LL0) Investigation: US-HF 2026-W13

**Metric:** AR Initial (LL0)  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 87.53% → 88.84% (+1.50%)  
**Volume:** 11,716 orders

## Executive Summary

**Overall:** AR Initial (LL0) improved from 87.53% to 88.84% (+1.50%) in W14, recovering from the prior week's decline and returning closer to the 8-week average performance level.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Rate | 87.53% → 88.84% | +1.31 pp | ✅ |
| L1: US Country | 68.09% → 66.77% | -1.32 pp | ✅ |
| L1: Apple Pay | 87.07% → 84.92% | -2.15 pp | ⚠️ |
| L1: Unknown Provider | 100.0% → 96.91% | -3.09 pp | ⚠️ |
| L1: ProcessOut | 88.77% → 87.54% | -1.23 pp | ✅ |
| L1: Braintree | 88.19% → 87.20% | -0.99 pp | ✅ |

**Key Findings:**
- Overall metric recovered +1.50% after the -1.30% decline reported in W13, suggesting the prior week's drop was temporary
- Apple Pay showed the largest decline among payment methods at -2.48% (84.92% from 87.07%), representing 3,693 orders
- PaymentProvider "Unknown" dropped -3.09 pp (100.0% → 96.91%), though volume is minimal at 97 orders
- PayPal was the only payment method showing improvement at +1.76% (89.48% → 91.05%)
- Volume decreased significantly from recent weeks (11,716 vs. 19,259 in W10), which may amplify rate fluctuations

**Action:** Monitor — The overall metric has recovered and no dimensions exceed the ±2.5% threshold. Continue watching Apple Pay performance over the next 1-2 weeks to confirm it stabilizes.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 88.84% | 11,716 | +1.50% |
| 2026-W13 | 87.53% | 10,955 | -1.30% ← REPORTED CHANGE |
| 2026-W12 | 88.68% | 14,786 | -1.59% |
| 2026-W11 | 90.11% | 15,868 | +0.95% |
| 2026-W10 | 89.26% | 19,259 | +0.01% |
| 2026-W09 | 89.25% | 18,657 | -0.36% |
| 2026-W08 | 89.57% | 18,802 | +0.88% |
| 2026-W07 | 88.79% | 21,838 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 66.77% | 68.09% | -1.95% | 23,515 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Apple Pay | 84.92% | 87.07% | -2.48% | 3,693 |
| PaymentMethod | Others | 98.4% | 99.76% | -1.37% | 187 |
| PaymentMethod | Credit Card | 88.26% | 88.98% | -0.81% | 6,192 |
| PaymentMethod | Paypal | 91.05% | 89.48% | +1.76% | 883 |
| PaymentProvider | Unknown | 96.91% | 100.0% | -3.09% | 97 |
| PaymentProvider | ProcessOut | 87.54% | 88.77% | -1.38% | 4,472 |
| PaymentProvider | Braintree | 87.2% | 88.19% | -1.12% | 6,297 |
| PaymentProvider | No Payment | 100.0% | 99.49% | +0.51% | 89 |

---

*Report: 2026-04-10*
