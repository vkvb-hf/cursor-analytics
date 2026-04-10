# AR Initial (LL0) Investigation: US-HF 2026-W12

**Metric:** AR Initial (LL0)  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 87.53% → 88.84% (+1.50%)  
**Volume:** 11,716 orders

## Executive Summary

**Overall:** AR Initial (LL0) improved from 87.53% to 88.84% (+1.50 pp) in 2026-W12, representing a recovery after the prior week's decline.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | Rate increased +1.50 pp | +1.50 pp | ✅ |
| L1: Country Impact | US declined -0.86 pp (within threshold) | -0.86 pp | ✅ |
| L1: Payment Method | PayPal showed largest drop at -1.92 pp | -1.92 pp | ✅ |
| L1: Payment Provider | Braintree declined -1.66 pp | -1.66 pp | ✅ |

**Key Findings:**
- The +1.50 pp week-over-week improvement reverses the -1.30 pp decline seen in 2026-W13, though the rate (88.84%) remains below the 8-week high of 90.11% from 2026-W11
- Volume decreased significantly to 11,716 orders compared to 14,786 in the prior week (-20.8%), continuing a downward trend from 21,838 orders in 2026-W07
- No countries or dimensions exceeded the ±2.5% threshold; all payment methods showed declines between -0.24 pp and -1.92 pp
- PayPal (-1.92 pp) and Credit Card (-1.80 pp) showed the largest payment method declines, though both remain above 88.9%
- "Others" and "No Payment" categories maintained near-perfect rates (99.76% and 99.49% respectively) despite slight declines from 100%

**Action:** Monitor — The metric has improved and all dimensions remain within acceptable thresholds. Continue tracking to confirm the recovery trend stabilizes and volume patterns normalize.

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
