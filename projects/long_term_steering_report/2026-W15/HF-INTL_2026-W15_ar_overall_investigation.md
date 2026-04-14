# AR Overall Investigation: HF-INTL 2026-W15

**Metric:** AR Overall  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 93.63% → 94.74% (+1.19%)  
**Volume:** 744,637 orders

## Executive Summary

## Executive Summary

**Overall:** AR Overall for HF-INTL improved from 93.63% to 94.74% (+1.11 pp) in W15, recovering to the highest level in the 8-week observation period with 744,637 orders processed.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | +1.19% vs prior week | +1.11 pp | ✅ |
| L1: Country Variance | AT (+2.94%), DK (+3.94%) exceed threshold | >+2.5 pp | ⚠️ |
| L1: Payment Method | Apple Pay (+2.73%) largest improvement | +2.39 pp | ⚠️ |
| L1: Payment Provider | All providers improved | +0.00 to +1.58 pp | ✅ |

**Key Findings:**
- DK showed the strongest improvement at +3.94 pp (94.03% → 97.74%), exceeding the ±2.5% threshold with 37,713 orders
- AT improved significantly by +2.94 pp (92.79% → 95.52%), also flagged for exceeding threshold
- Apple Pay showed notable recovery at +2.73 pp (87.52% → 89.91%) across 99,647 orders, though it remains the lowest-performing payment method
- All six countries improved week-over-week, indicating a broad-based recovery rather than isolated factors
- Volume declined by approximately 5% (784,406 → 744,637 orders) while rate improved, suggesting possible correlation

**Action:** Monitor – The improvement is positive and broad-based across all countries and payment dimensions. Continue monitoring DK and AT to determine if the gains are sustained or represent volatility.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 94.74% | 744,637 | +1.19% ← REPORTED CHANGE |
| 2026-W14 | 93.63% | 784,406 | -0.55% |
| 2026-W13 | 94.15% | 842,482 | -0.48% |
| 2026-W12 | 94.6% | 877,189 | -0.32% |
| 2026-W11 | 94.9% | 897,107 | +1.17% |
| 2026-W10 | 93.8% | 916,831 | +0.72% |
| 2026-W09 | 93.13% | 896,537 | -0.45% |
| 2026-W08 | 93.55% | 884,970 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| DE | 97.33% | 96.44% | +0.93% | 201,519 |  |
| GB | 94.14% | 93.07% | +1.15% | 185,598 |  |
| FR | 94.49% | 92.95% | +1.66% | 147,984 |  |
| IE | 91.93% | 90.41% | +1.67% | 17,513 |  |
| AT | 95.52% | 92.79% | +2.94% | 13,962 | ⚠️ |
| DK | 97.74% | 94.03% | +3.94% | 37,713 | ⚠️ |

**Countries exceeding ±2.5% threshold:** AT, DK

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Others | 98.97% | 98.82% | +0.15% | 121,159 |
| PaymentMethod | Paypal | 97.74% | 97.23% | +0.53% | 185,690 |
| PaymentMethod | Credit Card | 93.0% | 91.59% | +1.53% | 338,141 |
| PaymentMethod | Apple Pay | 89.91% | 87.52% | +2.73% | 99,647 |
| PaymentProvider | No Payment | 100.0% | 100.0% | +0.00% | 4,522 |
| PaymentProvider | Adyen | 95.96% | 95.19% | +0.80% | 241,310 |
| PaymentProvider | Braintree | 95.38% | 94.19% | +1.27% | 280,104 |
| PaymentProvider | ProcessOut | 92.54% | 91.13% | +1.55% | 216,399 |
| PaymentProvider | Unknown | 85.23% | 83.91% | +1.58% | 2,302 |

---

*Report: 2026-04-14*
