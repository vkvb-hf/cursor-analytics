# PAR Investigation: RTE 2026-W13

**Metric:** PAR  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 94.94% → 94.76% (-0.19%)  
**Volume:** 431,853 orders

## Executive Summary

**Overall:** PAR declined from 94.94% to 94.76% (-0.19pp) in W13 with 431,853 orders processed, continuing a downward trend for the second consecutive week.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Decline pattern observed | -0.19pp WoW | ⚠️ |
| L1: Country Breakdown | No country exceeds ±2.5% threshold | TK worst at -2.00pp | ✅ |
| L1: Payment Method | All methods declined except Others | Apple Pay -0.38pp | ⚠️ |
| L1: Payment Provider | Braintree declined (largest volume) | -0.33pp on 310K orders | ⚠️ |

**Key Findings:**
- PAR has declined for 2 consecutive weeks, dropping from 95.18% (W12) to 94.76% (W14), a total decrease of 0.42pp
- TK showed the largest country-level decline at -2.00pp (90.12%), though volume is low at 2,155 orders
- Braintree, handling 72% of volume (310,634 orders), declined -0.33pp from 95.93% to 95.62%
- Apple Pay showed the steepest payment method decline at -0.38pp (92.37%), processing 55,464 orders
- The "Unknown" payment provider has critically low PAR at 37.14%, though volume is negligible (35 orders)

**Action:** Monitor - The -0.19pp decline is within normal variance and no single dimension exceeds the ±2.5% threshold. Continue tracking Braintree performance given its high volume contribution and the consecutive weekly declines.

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
