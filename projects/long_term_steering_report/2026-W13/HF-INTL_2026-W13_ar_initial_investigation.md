# AR Initial (LL0) Investigation: HF-INTL 2026-W13

**Metric:** AR Initial (LL0)  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 90.12% → 90.13% (+0.01%)  
**Volume:** 31,165 orders

## Executive Summary

## Executive Summary

**Overall:** The AR Initial (LL0) metric for HF-INTL remained essentially stable in 2026-W13, improving marginally from 90.12% to 90.13% (+0.01 pp) on a volume of 31,165 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | 8-week trend shows decline from 91.7% (W07) to 90.13% (W14) | -1.57 pp | ⚠️ |
| L1: Country - CH | Switzerland rate dropped significantly | -11.69 pp | ⚠️ |
| L1: Country - NZ | New Zealand rate declined | -5.98 pp | ⚠️ |
| L1: Payment Method | All major methods declined (PayPal, Apple Pay, Credit Card) | -1.41 to -1.96 pp | ⚠️ |
| L1: Payment Provider | Braintree and ProcessOut both declined | -1.57 to -1.76 pp | ⚠️ |

**Key Findings:**
- Switzerland (CH) experienced the largest country-level decline at -11.69 pp (from 87.5% to 77.27%), though on relatively low volume (198 orders)
- New Zealand (NZ) showed a significant decline of -5.98 pp (from 51.84% to 48.74%) on 1,783 orders, with an already-low baseline rate
- The 8-week trend reveals a broader decline from 91.7% in W07 to 90.13% in W14, representing a -1.57 pp erosion over this period
- PayPal showed the steepest payment method decline at -1.96 pp (from 96.85% to 94.95%)
- Volume has decreased significantly from 52,771 orders (W07) to 31,165 orders (W14), a 41% reduction

**Action:** Investigate — While the week-over-week change is minimal (+0.01 pp), the flagged countries (CH and NZ) exceeding the ±2.5% threshold and the broader 8-week downward trend warrant deeper investigation into root causes, particularly in Switzerland and New Zealand.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 90.13% | 31,165 | +0.01% |
| 2026-W13 | 90.12% | 34,718 | -1.28% ← REPORTED CHANGE |
| 2026-W12 | 91.29% | 39,323 | -0.29% |
| 2026-W11 | 91.56% | 42,918 | +1.24% |
| 2026-W10 | 90.44% | 47,739 | +2.70% |
| 2026-W09 | 88.06% | 46,648 | -2.38% |
| 2026-W08 | 90.21% | 46,404 | -1.62% |
| 2026-W07 | 91.7% | 52,771 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CH | 77.27% | 87.5% | -11.69% | 198 | ⚠️ |
| NZ | 48.74% | 51.84% | -5.98% | 1,783 | ⚠️ |
| FR | 85.35% | 87.11% | -2.01% | 10,870 |  |
| DE | 85.34% | 86.93% | -1.84% | 11,022 |  |
| GB | 78.23% | 79.15% | -1.16% | 14,166 |  |
| SE | 84.0% | 82.03% | +2.40% | 1,894 |  |

**Countries exceeding ±2.5% threshold:** CH, NZ

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Paypal | 94.95% | 96.85% | -1.96% | 6,360 |
| PaymentMethod | Apple Pay | 86.1% | 87.78% | -1.91% | 10,325 |
| PaymentMethod | Credit Card | 88.66% | 89.92% | -1.41% | 11,372 |
| PaymentMethod | Others | 94.22% | 93.52% | +0.75% | 6,661 |
| PaymentProvider | Braintree | 90.91% | 92.53% | -1.76% | 15,307 |
| PaymentProvider | ProcessOut | 86.51% | 87.89% | -1.57% | 13,986 |
| PaymentProvider | Unknown | 96.51% | 97.32% | -0.84% | 1,661 |
| PaymentProvider | Adyen | 97.49% | 97.17% | +0.34% | 3,630 |
| PaymentProvider | No Payment | 97.76% | 97.4% | +0.37% | 134 |

---

*Report: 2026-04-10*
