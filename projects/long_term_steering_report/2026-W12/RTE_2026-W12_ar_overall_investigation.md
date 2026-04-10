# AR Overall Investigation: RTE 2026-W12

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 92.79% → 92.46% (-0.36%)  
**Volume:** 431,853 orders

## Executive Summary

**Overall:** AR Overall declined by -0.36% (from 92.79% to 92.46%) in 2026-W12 on a volume of 431,853 orders, continuing a three-week downward trend.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Sustained decline pattern | -0.36% WoW | ⚠️ |
| L1: Country Breakdown | Any country ≥±2.5% threshold | None exceeded | ✅ |
| L1: PaymentMethod | Largest decline | Apple Pay -0.24pp | ✅ |
| L1: PaymentProvider | Largest decline | ProcessOut -0.42pp | ⚠️ |

**Key Findings:**
- The 8-week trend shows AR Overall peaked at 93.2% in W11 and has declined for three consecutive weeks, dropping 0.74pp total since the peak
- TK experienced the largest country-level decline at -1.64pp (93.49% → 91.96%), though volume is relatively low at 2,338 orders
- ProcessOut shows the most significant payment provider decline at -0.42pp (92.20% → 91.81%) on 48,689 orders
- FJ dominates volume (408,532 orders, 94.6% of total) with a minor decline of -0.17pp, indicating broad-based softening rather than isolated issues
- Apple Pay underperforms other payment methods at 90.75% (-0.24pp), the lowest rate among standard payment methods

**Action:** Monitor — No single dimension exceeds critical thresholds, but the sustained three-week decline warrants close observation. If the downward trend continues in W13, escalate investigation into ProcessOut and TK performance.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 92.46% | 431,853 | -0.36% |
| 2026-W13 | 92.79% | 442,530 | -0.32% |
| 2026-W12 | 93.09% | 443,994 | -0.12% ← REPORTED CHANGE |
| 2026-W11 | 93.2% | 458,408 | +1.80% |
| 2026-W10 | 91.55% | 467,998 | +0.24% |
| 2026-W09 | 91.33% | 466,696 | +0.29% |
| 2026-W08 | 91.07% | 462,049 | -0.28% |
| 2026-W07 | 91.33% | 474,461 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TK | 91.96% | 93.49% | -1.64% | 2,338 |  |
| TV | 93.47% | 94.31% | -0.89% | 2,205 |  |
| TO | 86.85% | 87.27% | -0.49% | 3,611 |  |
| FJ | 94.3% | 94.46% | -0.17% | 408,532 |  |
| CF | 93.62% | 93.52% | +0.10% | 53,267 |  |
| YE | 88.62% | 88.28% | +0.39% | 48,432 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Apple Pay | 90.75% | 90.97% | -0.24% | 55,075 |
| PaymentMethod | Credit Card | 92.79% | 92.9% | -0.12% | 324,263 |
| PaymentMethod | Paypal | 96.5% | 96.54% | -0.04% | 57,396 |
| PaymentMethod | Others | 97.38% | 97.36% | +0.03% | 7,260 |
| PaymentProvider | ProcessOut | 91.81% | 92.2% | -0.42% | 48,689 |
| PaymentProvider | Braintree | 94.13% | 94.25% | -0.12% | 314,194 |
| PaymentProvider | Adyen | 89.68% | 89.41% | +0.30% | 78,682 |
| PaymentProvider | No Payment | 95.47% | 94.94% | +0.56% | 2,405 |
| PaymentProvider | Unknown | 25.0% | 7.14% | +250.00% | 24 |

---

*Report: 2026-04-10*
