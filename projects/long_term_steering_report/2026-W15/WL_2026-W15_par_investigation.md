# PAR Investigation: WL 2026-W15

**Metric:** PAR  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 91.05% → 91.65% (+0.66%)  
**Volume:** 160,979 orders

## Executive Summary

**Overall:** PAR improved by +0.60 percentage points (91.05% → 91.65%) on 160,979 orders in W15, continuing a recovery trend that began in W09 (89.88%).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL Trend | 8-week trend direction | +1.77pp since W08 | ✅ |
| L1: Country | Any country ≥±2.5% threshold | None flagged | ✅ |
| L1: Payment Method | Segment volatility | Max Δ +0.69pp (Credit Card) | ✅ |
| L1: Payment Provider | Segment volatility | ProcessOut +2.05pp, Unknown +13.15pp | ⚠️ |

**Key Findings:**
- All four countries (GN, ER, MR, AO) showed improvement, with AO leading at +2.17pp (85.21% → 87.06%)
- ProcessOut payment provider improved significantly by +2.05pp (81.01% → 82.67%) on 17,676 orders, though it remains the lowest-performing provider
- Unknown payment provider shows +13.15pp spike (85.71% → 96.99%), but volume is minimal (664 orders) - likely noise
- Credit Card, representing 71% of volume (115,014 orders), improved +0.69pp driving the majority of the overall gain
- Order volume declined 2.4% WoW (165,018 → 160,979), continuing a downward trend from W08 (179,647)

**Action:** Monitor — The improvement is broad-based across countries and payment methods with no segments breaching alert thresholds. Continue tracking ProcessOut performance and volume decline trend.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 91.65% | 160,979 | +0.66% ← REPORTED CHANGE |
| 2026-W14 | 91.05% | 165,018 | -0.27% |
| 2026-W13 | 91.3% | 169,667 | -0.02% |
| 2026-W12 | 91.32% | 169,891 | -0.28% |
| 2026-W11 | 91.58% | 174,933 | +1.03% |
| 2026-W10 | 90.65% | 179,965 | +0.81% |
| 2026-W09 | 89.92% | 180,862 | +0.04% |
| 2026-W08 | 89.88% | 179,647 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| GN | 93.32% | 92.33% | +1.07% | 13,110 |  |
| ER | 90.33% | 89.22% | +1.23% | 68,811 |  |
| MR | 81.43% | 80.25% | +1.47% | 19,468 |  |
| AO | 87.06% | 85.21% | +2.17% | 13,883 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Others | 98.35% | 98.67% | -0.32% | 1,393 |
| PaymentMethod | Apple Pay | 87.44% | 87.06% | +0.43% | 20,488 |
| PaymentMethod | Paypal | 96.03% | 95.52% | +0.54% | 24,084 |
| PaymentMethod | Credit Card | 91.41% | 90.78% | +0.69% | 115,014 |
| PaymentProvider | No Payment | 100.0% | 100.0% | +0.00% | 683 |
| PaymentProvider | Braintree | 92.22% | 91.8% | +0.45% | 105,580 |
| PaymentProvider | Adyen | 94.13% | 93.51% | +0.67% | 36,376 |
| PaymentProvider | ProcessOut | 82.67% | 81.01% | +2.05% | 17,676 |
| PaymentProvider | Unknown | 96.99% | 85.71% | +13.15% | 664 |

---

*Report: 2026-04-14*
