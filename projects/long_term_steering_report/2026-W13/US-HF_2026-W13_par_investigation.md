# PAR Investigation: US-HF 2026-W13

**Metric:** PAR  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 93.59% → 93.63% (+0.04%)  
**Volume:** 415,885 orders

## Executive Summary

## Executive Summary

**Overall:** PAR improved marginally from 93.59% to 93.63% (+0.04 pp) in 2026-W13, continuing a positive trend observed over the past several weeks.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Stable improvement pattern | +0.04 pp | ✅ |
| L1: Country Breakdown | US within threshold | +0.05 pp | ✅ |
| L1: Payment Method | Minor fluctuations | -0.09 pp to +0.28 pp | ✅ |
| L1: Payment Provider | Unknown provider volatility | -6.43 pp | ⚠️ |

**Key Findings:**
- PAR has shown consistent week-over-week improvement since W09, rising from 93.16% to 93.63% (+0.47 pp over 5 weeks)
- PayPal payment method showed the strongest improvement at +0.28 pp (95.79% → 96.06%) with 52,426 orders
- **Unknown PaymentProvider dropped significantly by -6.43 pp** (93.82% → 87.79%), though volume is minimal at only 131 orders
- Adyen provider declined by -0.84 pp (96.55% → 95.74%), but represents very low volume (399 orders)
- Braintree, handling the majority of volume (382,647 orders), improved slightly by +0.09 pp (93.94% → 94.02%)

**Action:** Monitor – The overall trend is positive and no major dimensions exceed the ±2.5% threshold at meaningful volumes. Continue tracking the Unknown PaymentProvider for potential data quality issues.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 93.63% | 415,885 | +0.04% |
| 2026-W13 | 93.59% | 424,103 | +0.04% ← REPORTED CHANGE |
| 2026-W12 | 93.55% | 433,761 | -0.04% |
| 2026-W11 | 93.59% | 444,619 | +0.22% |
| 2026-W10 | 93.38% | 457,610 | +0.24% |
| 2026-W09 | 93.16% | 455,121 | +0.03% |
| 2026-W08 | 93.13% | 453,781 | -0.27% |
| 2026-W07 | 93.38% | 470,140 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.85% | 92.8% | +0.05% | 505,599 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Others | 99.19% | 99.28% | -0.09% | 2,230 |
| PaymentMethod | Credit Card | 94.35% | 94.38% | -0.03% | 311,435 |
| PaymentMethod | Apple Pay | 87.04% | 86.98% | +0.07% | 58,012 |
| PaymentMethod | Paypal | 96.06% | 95.79% | +0.28% | 52,426 |
| PaymentProvider | Unknown | 87.79% | 93.82% | -6.43% | 131 |
| PaymentProvider | Adyen | 95.74% | 96.55% | -0.84% | 399 |
| PaymentProvider | ProcessOut | 88.93% | 89.1% | -0.19% | 38,861 |
| PaymentProvider | No Payment | 100.0% | 99.96% | +0.04% | 2,065 |
| PaymentProvider | Braintree | 94.02% | 93.94% | +0.09% | 382,647 |

---

*Report: 2026-04-10*
