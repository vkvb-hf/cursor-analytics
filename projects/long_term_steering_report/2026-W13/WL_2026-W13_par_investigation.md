# PAR Investigation: WL 2026-W13

**Metric:** PAR  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 91.3% → 91.05% (-0.27%)  
**Volume:** 165,018 orders

## Executive Summary

**Overall:** PAR declined by 0.27 percentage points (91.3% → 91.05%) in 2026-W13, continuing a downward trend observed over the past three weeks.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL Trend | 3-week declining trend (W12-W14) | -0.27pp | ⚠️ |
| L1: Country | No country exceeds ±2.5% threshold | Max: +0.88pp (CK) | ✅ |
| L1: PaymentMethod | Credit Card slight decline | -0.32pp | ✅ |
| L1: PaymentProvider | Unknown provider significant drop | -24.66pp | ⚠️ |
| L1: PaymentProvider | Braintree minor decline | -0.33pp | ✅ |

**Key Findings:**
- PaymentProvider "Unknown" experienced a severe decline of -24.66pp (97.33% → 73.33%), though volume is minimal at only 15 orders
- Credit Card payments, representing the largest volume (120,798 orders), declined by 0.32pp, contributing most to the overall drop
- Braintree, the highest-volume provider (111,236 orders), declined by 0.33pp (92.15% → 91.85%)
- CK showed the strongest improvement at +0.88pp, while ER improved by +0.43pp
- Overall volume decreased by ~4,649 orders (169,667 → 165,018) week-over-week

**Action:** Monitor – The decline is modest and no country breaches the ±2.5% threshold. The PaymentProvider "Unknown" anomaly warrants a quick data quality check due to its extreme swing, but its negligible volume (15 orders) limits impact. Continue monitoring the 3-week downward trend.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 91.05% | 165,018 | -0.27% |
| 2026-W13 | 91.3% | 169,667 | -0.02% ← REPORTED CHANGE |
| 2026-W12 | 91.32% | 169,891 | -0.28% |
| 2026-W11 | 91.58% | 174,933 | +1.03% |
| 2026-W10 | 90.65% | 179,964 | +0.81% |
| 2026-W09 | 89.92% | 180,862 | +0.04% |
| 2026-W08 | 89.88% | 179,647 | -0.50% |
| 2026-W07 | 90.33% | 186,442 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| KN | 87.61% | 87.76% | -0.17% | 10,365 |  |
| CG | 96.76% | 96.84% | -0.08% | 44,477 |  |
| ER | 89.92% | 89.54% | +0.43% | 73,655 |  |
| AO | 87.96% | 87.38% | +0.66% | 16,249 |  |
| CK | 94.15% | 93.33% | +0.88% | 42,197 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Credit Card | 90.99% | 91.29% | -0.32% | 120,798 |
| PaymentMethod | Apple Pay | 87.59% | 87.46% | +0.15% | 22,237 |
| PaymentMethod | Paypal | 95.7% | 95.42% | +0.30% | 25,836 |
| PaymentMethod | Others | 98.87% | 87.92% | +12.46% | 796 |
| PaymentProvider | Unknown | 73.33% | 97.33% | -24.66% | 15 |
| PaymentProvider | Braintree | 91.85% | 92.15% | -0.33% | 111,236 |
| PaymentProvider | No Payment | 100.0% | 99.8% | +0.20% | 747 |
| PaymentProvider | Adyen | 94.33% | 93.76% | +0.61% | 39,337 |
| PaymentProvider | ProcessOut | 81.11% | 80.58% | +0.66% | 18,332 |

---

*Report: 2026-04-10*
