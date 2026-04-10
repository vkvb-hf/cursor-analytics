# PAR Investigation: RTE 2026-W12

**Metric:** PAR  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 94.94% → 94.76% (-0.19%)  
**Volume:** 431,853 orders

## Executive Summary

**Overall:** PAR declined by -0.19pp (94.94% → 94.76%) on volume of 431,853 orders, continuing a two-week downward trend after peaking at 95.18% in W12.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Overall PAR | -0.19pp decline | -0.19% | ⚠️ |
| Country Threshold (±2.5%) | No countries exceed threshold | N/A | ✅ |
| Top Country (FJ) | 94.46% → 94.30% | -0.17% | ✅ |
| Payment Provider (Unknown) | 42.86% → 37.50% | -12.50% | ⚠️ |
| Payment Provider (Braintree) | 95.85% → 95.93% | +0.08% | ✅ |

**Key Findings:**
- TK showed the largest country decline at -1.64pp (93.49% → 91.96%), though volume is low at 2,338 orders
- PaymentProvider "Unknown" dropped significantly by -12.50pp (42.86% → 37.50%), but with minimal volume (24 orders)
- FJ dominates volume (408,532 orders, 95% of total) with a minor decline of -0.17pp, driving the overall metric movement
- Adyen showed improvement of +0.33pp (92.84% → 93.14%) on 78,682 orders
- The 8-week trend shows PAR has declined for two consecutive weeks after reaching a peak of 95.18% in W12

**Action:** Monitor – The decline is modest (-0.19pp) with no countries exceeding the ±2.5% threshold. Continue monitoring TK performance and the downward trend pattern.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 94.76% | 431,853 | -0.19% |
| 2026-W13 | 94.94% | 442,530 | -0.25% |
| 2026-W12 | 95.18% | 443,994 | +0.08% ← REPORTED CHANGE |
| 2026-W11 | 95.1% | 458,408 | +1.80% |
| 2026-W10 | 93.42% | 467,998 | +0.17% |
| 2026-W09 | 93.26% | 466,696 | +0.20% |
| 2026-W08 | 93.07% | 462,049 | -0.04% |
| 2026-W07 | 93.11% | 474,461 | - |

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
| PaymentMethod | Others | 97.73% | 97.83% | -0.10% | 7,260 |
| PaymentMethod | Apple Pay | 92.72% | 92.79% | -0.07% | 55,075 |
| PaymentMethod | Paypal | 97.65% | 97.61% | +0.04% | 57,396 |
| PaymentMethod | Credit Card | 95.1% | 94.99% | +0.12% | 324,263 |
| PaymentProvider | Unknown | 37.5% | 42.86% | -12.50% | 24 |
| PaymentProvider | ProcessOut | 93.6% | 93.67% | -0.07% | 48,689 |
| PaymentProvider | Braintree | 95.93% | 95.85% | +0.08% | 314,194 |
| PaymentProvider | Adyen | 93.14% | 92.84% | +0.33% | 78,682 |
| PaymentProvider | No Payment | 95.47% | 94.94% | +0.56% | 2,405 |

---

*Report: 2026-04-10*
