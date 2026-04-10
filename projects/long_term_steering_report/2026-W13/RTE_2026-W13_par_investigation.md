# PAR Investigation: RTE 2026-W13

**Metric:** PAR  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 94.94% → 94.76% (-0.19%)  
**Volume:** 431,853 orders

## Executive Summary

**Overall:** PAR declined by -0.19 percentage points (94.94% → 94.76%) in 2026-W13, continuing a two-week downward trend from the recent peak of 95.18% in 2026-W12.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Sustained decline pattern? | -0.19pp WoW, -0.44pp from W12 peak | ⚠️ |
| L1: Country Impact | Any country Δ > ±2.5%? | None (max: TK at -2.00pp) | ✅ |
| L1: Country Contribution | Top volume country impact? | FJ: -0.35pp (409,231 orders, 95% of volume) | ⚠️ |
| L1: Payment Method | Significant method degradation? | Apple Pay: -0.38pp, Credit Card: -0.27pp | ⚠️ |
| L1: Payment Provider | Provider-specific issues? | Braintree: -0.33pp (310,634 orders) | ⚠️ |

**Key Findings:**
- FJ dominates volume (95% of orders at 409,231) and its -0.35pp decline is the primary driver of the overall PAR drop
- Braintree, handling 72% of transaction volume (310,634 orders), declined -0.33pp and warrants attention as the largest payment provider
- TK showed the steepest country-level decline at -2.00pp, though low volume (2,155 orders) limits overall impact
- Apple Pay underperformed other payment methods with -0.38pp decline across 55,464 orders
- This marks the second consecutive week of decline after PAR peaked at 95.18% in W12

**Action:** Monitor – No single dimension exceeds the ±2.5% threshold, but the consecutive weekly declines and broad-based degradation across FJ, Braintree, and Apple Pay suggest close monitoring through W14. If the downward trend continues, escalate for deeper investigation into Braintree processing in FJ.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 94.76% | 431,853 | -0.19% |
| 2026-W13 | 94.94% | 442,530 | -0.25% ← REPORTED CHANGE |
| 2026-W12 | 95.18% | 443,994 | +0.08% |
| 2026-W11 | 95.1% | 458,408 | +1.80% |
| 2026-W10 | 93.42% | 467,998 | +0.17% |
| 2026-W09 | 93.26% | 466,696 | +0.20% |
| 2026-W08 | 93.07% | 462,049 | -0.04% |
| 2026-W07 | 93.11% | 474,461 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TK | 90.12% | 91.96% | -2.00% | 2,155 |  |
| TO | 85.35% | 86.85% | -1.72% | 3,508 |  |
| TV | 92.01% | 93.47% | -1.56% | 2,191 |  |
| TZ | 91.42% | 91.86% | -0.48% | 3,310 |  |
| FJ | 93.97% | 94.3% | -0.35% | 409,231 |  |
| CF | 93.7% | 93.62% | +0.08% | 52,939 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Apple Pay | 92.37% | 92.72% | -0.38% | 55,464 |
| PaymentMethod | Credit Card | 94.84% | 95.1% | -0.27% | 323,597 |
| PaymentMethod | Paypal | 97.64% | 97.65% | -0.01% | 57,290 |
| PaymentMethod | Others | 98.35% | 97.73% | +0.64% | 6,179 |
| PaymentProvider | Unknown | 37.14% | 37.5% | -0.95% | 35 |
| PaymentProvider | Braintree | 95.62% | 95.93% | -0.33% | 310,634 |
| PaymentProvider | Adyen | 93.0% | 93.14% | -0.16% | 78,208 |
| PaymentProvider | ProcessOut | 93.83% | 93.6% | +0.25% | 52,341 |
| PaymentProvider | No Payment | 97.41% | 95.47% | +2.03% | 1,312 |

---

*Report: 2026-04-10*
