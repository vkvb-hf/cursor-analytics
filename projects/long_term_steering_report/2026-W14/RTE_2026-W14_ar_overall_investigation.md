# AR Overall Investigation: RTE 2026-W14

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 92.79% → 92.46% (-0.36%)  
**Volume:** 431,853 orders

## Executive Summary

**Overall:** AR Overall declined by 0.33 percentage points (92.79% → 92.46%) in W14, continuing a 3-week downward trend from the W11 peak of 93.2%.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | Rate declined for 3rd consecutive week | -0.36% | ⚠️ |
| L1: Country Impact | No country exceeded ±2.5% threshold | Largest: TK -1.63% | ✅ |
| L1: Volume Driver | FJ dominates volume (397,332 of 431,853) | FJ -0.37% | ⚠️ |
| L1: Payment Method | Credit Card (largest segment) declined | -0.42% | ⚠️ |
| L1: Payment Provider | Braintree (largest provider) declined | -0.36% | ⚠️ |

**Key Findings:**
- **Sustained decline:** AR Overall has dropped 0.74pp over the past 3 weeks (W11: 93.2% → W14: 92.46%), indicating a persistent negative trend rather than an isolated incident
- **FJ drives overall impact:** FJ accounts for 92% of order volume (397,332 orders) and its -0.37pp decline directly mirrors the overall metric movement
- **Credit Card payment method underperforming:** Credit Card transactions (316,124 orders, 73% of volume) declined -0.42pp, slightly worse than the overall average
- **Braintree as primary provider contributor:** Braintree handles 68% of transactions (293,781 orders) and declined -0.36pp, aligning with the overall drop
- **Volume contraction:** Order volume decreased by 10,677 orders (-2.4%) week-over-week, continuing a decline from W7's peak of 474,461

**Action:** **Investigate** – The 3-week consecutive decline warrants deeper analysis into FJ market performance and Credit Card/Braintree processing issues. Prioritize root cause analysis on the FJ + Braintree + Credit Card combination which represents the majority of impacted transactions.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 92.46% | 431,853 | -0.36% ← REPORTED CHANGE |
| 2026-W13 | 92.79% | 442,530 | -0.32% |
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
| TK | 88.65% | 90.12% | -1.63% | 1,779 |  |
| TZ | 90.11% | 91.42% | -1.43% | 3,013 |  |
| YE | 88.15% | 88.62% | -0.53% | 45,214 |  |
| FJ | 93.62% | 93.97% | -0.37% | 397,332 |  |
| CF | 93.47% | 93.7% | -0.24% | 52,140 |  |
| TT | 97.2% | 96.27% | +0.97% | 4,924 |  |
| TV | 93.41% | 92.01% | +1.52% | 2,065 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Credit Card | 92.08% | 92.47% | -0.42% | 316,124 |
| PaymentMethod | Apple Pay | 90.02% | 90.19% | -0.19% | 54,874 |
| PaymentMethod | Paypal | 96.45% | 96.52% | -0.07% | 55,378 |
| PaymentMethod | Others | 98.28% | 97.93% | +0.36% | 5,477 |
| PaymentProvider | Braintree | 93.41% | 93.75% | -0.36% | 293,781 |
| PaymentProvider | ProcessOut | 91.66% | 91.81% | -0.17% | 60,625 |
| PaymentProvider | Adyen | 89.45% | 89.58% | -0.14% | 76,830 |
| PaymentProvider | No Payment | 100.0% | 97.41% | +2.66% | 534 |
| PaymentProvider | Unknown | 49.4% | 11.43% | +332.23% | 83 |

---

*Report: 2026-04-09*
