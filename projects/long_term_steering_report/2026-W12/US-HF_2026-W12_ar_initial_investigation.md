# AR Initial (LL0) Investigation: US-HF 2026-W12

**Metric:** AR Initial (LL0)  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 87.53% → 88.84% (+1.50%)  
**Volume:** 11,716 orders

## Executive Summary

**Overall:** AR Initial (LL0) for US-HF improved from 87.53% to 88.84% (+1.31 pp) in 2026-W12, representing a positive recovery from the prior week's decline.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | Week-over-week change | +1.31 pp | ✅ |
| L1: Country Impact | US threshold (±2.5%) | -0.86 pp | ✅ |
| L1: Payment Method | PayPal decline | -1.92 pp | ⚠️ |
| L1: Payment Method | Credit Card decline | -1.80 pp | ⚠️ |
| L1: Payment Provider | Braintree decline | -1.66 pp | ⚠️ |
| L1: Payment Provider | ProcessOut decline | -1.58 pp | ⚠️ |

**Key Findings:**
- The +1.31 pp improvement in W12 partially recovers from the -1.30 pp decline observed in W13, though the rate (88.84%) remains below the W11 peak of 90.11%
- Volume decreased significantly from 14,786 (W12) to 11,716 (W14), representing a ~21% reduction in order volume
- All payment methods showed declines, with PayPal experiencing the largest drop (-1.92 pp) on 1,150 orders and Credit Card declining -1.80 pp on the highest volume (8,177 orders)
- Both major payment providers declined: Braintree (-1.66 pp, 10,357 orders) and ProcessOut (-1.58 pp, 4,006 orders)
- No countries exceeded the ±2.5% threshold, indicating the changes are distributed across payment dimensions rather than geographic factors

**Action:** Monitor – The overall metric improved and no single dimension exceeds critical thresholds, but the consistent declines across all payment methods and providers warrant continued observation over the next 1-2 weeks to confirm stabilization.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 88.84% | 11,716 | +1.50% |
| 2026-W13 | 87.53% | 10,955 | -1.30% |
| 2026-W12 | 88.68% | 14,786 | -1.59% ← REPORTED CHANGE |
| 2026-W11 | 90.11% | 15,868 | +0.95% |
| 2026-W10 | 89.26% | 19,259 | +0.01% |
| 2026-W09 | 89.25% | 18,657 | -0.36% |
| 2026-W08 | 89.57% | 18,802 | +0.88% |
| 2026-W07 | 88.79% | 21,838 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 68.09% | 68.68% | -0.86% | 27,055 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Paypal | 89.48% | 91.23% | -1.92% | 1,150 |
| PaymentMethod | Credit Card | 88.98% | 90.62% | -1.80% | 8,177 |
| PaymentMethod | Apple Pay | 87.07% | 88.24% | -1.32% | 5,036 |
| PaymentMethod | Others | 99.76% | 100.0% | -0.24% | 423 |
| PaymentProvider | Braintree | 88.19% | 89.68% | -1.66% | 10,357 |
| PaymentProvider | ProcessOut | 88.77% | 90.19% | -1.58% | 4,006 |
| PaymentProvider | No Payment | 99.49% | 100.0% | -0.51% | 196 |
| PaymentProvider | Unknown | 100.0% | 100.0% | +0.00% | 227 |

---

*Report: 2026-04-10*
