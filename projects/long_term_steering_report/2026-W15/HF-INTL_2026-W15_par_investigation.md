# PAR Investigation: HF-INTL 2026-W15

**Metric:** PAR  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 97.04% → 97.27% (+0.24%)  
**Volume:** 744,637 orders

## Executive Summary

**Overall:** PAR improved by +0.24 percentage points (97.04% → 97.27%) on volume of 744,637 orders, continuing a recovery trend from the W10-W11 low point.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range, upward trend from W10 | +0.24 pp | ✅ |
| L1: Country Breakdown | 2 countries (AT, DK) exceed ±2.5% threshold | +1.67 to +3.94 pp | ⚠️ |
| L1: Payment Method | All methods improved or stable | +0.00 to +0.84 pp | ✅ |
| L1: Payment Provider | Minor decline in Unknown provider (-0.70 pp) on low volume | -0.70 to +0.39 pp | ✅ |

**Key Findings:**
- DK showed the largest improvement at +3.94 pp (94.03% → 97.74%) on 37,713 orders, exceeding the ±2.5% threshold
- AT improved by +2.94 pp (92.79% → 95.52%) on 13,962 orders, also flagged for exceeding threshold
- All major countries (DE, GB, FR) showed positive movement ranging from +0.93 pp to +1.66 pp
- Volume declined by ~40K orders (784,406 → 744,637) week-over-week, continuing a 7-week downward volume trend
- Apple Pay showed the largest payment method improvement at +0.84 pp (92.77% → 93.55%)

**Action:** Monitor — The improvement is positive and broad-based across countries and payment dimensions. The flagged countries (AT, DK) show improvements rather than degradation, requiring no immediate intervention. Continue monitoring volume decline trend.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 97.27% | 744,637 | +0.24% ← REPORTED CHANGE |
| 2026-W14 | 97.04% | 784,406 | -0.13% |
| 2026-W13 | 97.17% | 842,482 | -0.08% |
| 2026-W12 | 97.25% | 877,189 | +0.04% |
| 2026-W11 | 97.21% | 897,107 | +0.52% |
| 2026-W10 | 96.71% | 916,831 | +0.51% |
| 2026-W09 | 96.22% | 896,537 | -0.12% |
| 2026-W08 | 96.34% | 884,970 | - |

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
| PaymentMethod | Others | 99.49% | 99.49% | +0.00% | 121,159 |
| PaymentMethod | Paypal | 98.97% | 98.92% | +0.05% | 185,690 |
| PaymentMethod | Credit Card | 96.64% | 96.38% | +0.27% | 338,141 |
| PaymentMethod | Apple Pay | 93.55% | 92.77% | +0.84% | 99,647 |
| PaymentProvider | Unknown | 87.01% | 87.63% | -0.70% | 2,302 |
| PaymentProvider | No Payment | 100.0% | 100.0% | +0.00% | 4,522 |
| PaymentProvider | Adyen | 98.42% | 98.35% | +0.07% | 241,310 |
| PaymentProvider | Braintree | 97.4% | 97.1% | +0.31% | 280,104 |
| PaymentProvider | ProcessOut | 95.87% | 95.5% | +0.39% | 216,399 |

---

*Report: 2026-04-14*
