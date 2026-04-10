# AR Overall Investigation: RTE 2026-W13

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 92.79% → 92.46% (-0.36%)  
**Volume:** 431,853 orders

## Executive Summary

**Overall:** AR Overall declined by -0.36% (from 92.79% to 92.46%) in 2026-W13, continuing a downward trend observed over the past three weeks with total volume of 431,853 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 8-Week Trend | Consistent decline W11→W14 | -0.74pp over 3 weeks | ⚠️ |
| Country Threshold (±2.5%) | No countries exceeded threshold | N/A | ✅ |
| Country Performance | TK largest drop | -2.00pp | ⚠️ |
| Payment Method | Apple Pay underperforming | -0.62pp | ⚠️ |
| Payment Provider | Unknown provider anomaly | -54.29pp (low volume: 35) | ⚠️ |
| Major Provider (Braintree) | Slight decline | -0.41pp | ✅ |

**Key Findings:**
- Three consecutive weeks of decline: W11 (93.2%) → W12 (93.09%) → W13 (92.79%) → W14 (92.46%), representing a cumulative -0.74pp drop
- TK experienced the largest country-level decline at -2.00pp (90.12% from 91.96%), followed by TO at -1.72pp and TV at -1.56pp
- Apple Pay shows the weakest payment method performance at 90.19% (-0.62pp), underperforming Credit Card (92.47%) and Paypal (96.52%)
- PaymentProvider "Unknown" dropped -54.29pp but represents negligible volume (35 orders)
- FJ dominates volume (409,231 orders, 95% of total) with a -0.35pp decline, making it the primary driver of overall metric movement

**Action:** Monitor - No individual country exceeded the ±2.5% threshold, but the sustained three-week downward trend warrants close observation. If decline continues in W15, escalate investigation into FJ performance and Apple Pay payment method.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 92.46% | 431,853 | -0.36% |
| 2026-W13 | 92.79% | 442,530 | -0.32% ← REPORTED CHANGE |
| 2026-W12 | 93.09% | 443,994 | -0.12% |
| 2026-W11 | 93.2% | 458,408 | +1.80% |
| 2026-W10 | 91.55% | 467,998 | +0.24% |
| 2026-W09 | 91.33% | 466,696 | +0.29% |
| 2026-W08 | 91.07% | 462,049 | -0.28% |
| 2026-W07 | 91.33% | 474,461 | - |

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
| PaymentMethod | Apple Pay | 90.19% | 90.75% | -0.62% | 55,464 |
| PaymentMethod | Credit Card | 92.47% | 92.79% | -0.34% | 323,597 |
| PaymentMethod | Paypal | 96.52% | 96.5% | +0.03% | 57,290 |
| PaymentMethod | Others | 97.93% | 97.38% | +0.56% | 6,179 |
| PaymentProvider | Unknown | 11.43% | 25.0% | -54.29% | 35 |
| PaymentProvider | Braintree | 93.75% | 94.13% | -0.41% | 310,634 |
| PaymentProvider | Adyen | 89.58% | 89.68% | -0.11% | 78,208 |
| PaymentProvider | ProcessOut | 91.81% | 91.81% | +0.00% | 52,341 |
| PaymentProvider | No Payment | 97.41% | 95.47% | +2.03% | 1,312 |

---

*Report: 2026-04-10*
