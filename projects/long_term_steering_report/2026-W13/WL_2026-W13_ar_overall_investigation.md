# AR Overall Investigation: WL 2026-W13

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 89.72% → 89.33% (-0.43%)  
**Volume:** 165,018 orders

## Executive Summary

## Executive Summary

**Overall:** AR Overall declined by -0.43pp (from 89.72% to 89.33%) in WL 2026-W13 with a volume of 165,018 orders, reversing the positive trend observed in prior weeks.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Sustained decline pattern? | -0.43pp | ✅ Minor fluctuation within normal range (88.14%-89.79%) |
| L1: Country Breakdown | Any country Δ > ±2.5%? | Max: +0.88pp (CK) | ✅ No countries exceed threshold |
| L1: PaymentMethod | Any method Δ > ±2.5%? | +12.74pp (Others) | ⚠️ "Others" shows significant swing but low volume (796) |
| L1: PaymentProvider | Any provider Δ > ±2.5%? | -37.50pp (Unknown) | ⚠️ "Unknown" provider dropped significantly but minimal volume (15) |

**Key Findings:**
- The -0.43pp decline breaks a 4-week positive trend that had lifted AR Overall from 88.14% (W08) to 89.72% (W13)
- No country exceeded the ±2.5% threshold; all country movements were within -0.17pp to +0.88pp
- PaymentProvider "Unknown" showed a -37.50pp drop (60.0% vs 96.0%), but with only 15 orders this is statistically insignificant
- Credit Card payments, representing the largest volume (120,798 orders), declined slightly by -0.13pp
- Braintree, the largest payment provider (111,236 orders), declined -0.29pp from 91.15% to 90.89%

**Action:** Monitor – The decline is minor (-0.43pp) and no significant dimensional drivers were identified. The flagged anomalies in "Unknown" provider and "Others" payment method have negligible volume impact.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 89.33% | 165,018 | -0.43% |
| 2026-W13 | 89.72% | 169,667 | +0.07% ← REPORTED CHANGE |
| 2026-W12 | 89.66% | 169,891 | -0.14% |
| 2026-W11 | 89.79% | 174,933 | +0.80% |
| 2026-W10 | 89.08% | 179,964 | +1.01% |
| 2026-W09 | 88.19% | 180,862 | +0.06% |
| 2026-W08 | 88.14% | 179,647 | -0.50% |
| 2026-W07 | 88.58% | 186,442 | - |

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
| PaymentMethod | Credit Card | 89.23% | 89.34% | -0.13% | 120,798 |
| PaymentMethod | Apple Pay | 86.16% | 86.02% | +0.16% | 22,237 |
| PaymentMethod | Paypal | 94.82% | 94.61% | +0.23% | 25,836 |
| PaymentMethod | Others | 98.62% | 87.48% | +12.74% | 796 |
| PaymentProvider | Unknown | 60.0% | 96.0% | -37.50% | 15 |
| PaymentProvider | Braintree | 90.89% | 91.15% | -0.29% | 111,236 |
| PaymentProvider | No Payment | 100.0% | 99.8% | +0.20% | 747 |
| PaymentProvider | Adyen | 90.82% | 90.17% | +0.71% | 39,337 |
| PaymentProvider | ProcessOut | 79.93% | 78.95% | +1.24% | 18,332 |

---

*Report: 2026-04-10*
