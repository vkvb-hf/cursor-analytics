# AR Overall Investigation: HF-INTL 2026-W12

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 94.16% → 93.64% (-0.55%)  
**Volume:** 784,389 orders

## Executive Summary

**Overall:** AR Overall declined from 94.16% to 93.64% (-0.52pp) in 2026-W12 on volume of 784,389 orders, marking the third consecutive week of decline.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Sustained decline pattern | -0.55% WoW | ⚠️ |
| L1: Country Breakdown | No countries exceed ±2.5% threshold | NO worst at -1.70% | ✅ |
| L1: Payment Method | Apple Pay underperforming | -0.99% | ⚠️ |
| L1: Payment Provider | Unknown provider flagged | -2.77% | ⚠️ |

**Key Findings:**
- **Sustained downward trend:** AR Overall has declined for 3 consecutive weeks (W11: 94.9% → W12: 94.6% → W13: 94.16% → W14: 93.64%), dropping 1.26pp from the W11 peak
- **Payment Provider "Unknown" showing significant degradation:** -2.77pp decline (89.9% → 87.41%) on 2,605 orders, exceeding the ±2.5% threshold at the dimension level
- **Apple Pay underperformance:** Lowest performing payment method at 89.48% (-0.99pp), handling 118,640 orders (15% of volume)
- **Norway (NO) leading country declines:** Dropped -1.70pp (91.42% → 89.86%) on 26,830 orders, the steepest country-level decline
- **Volume contraction:** Order volume decreased from 842,480 (W13) to 784,389 (W14), a reduction of ~58,000 orders (-6.9%)

**Action:** Investigate — Focus investigation on PaymentProvider "Unknown" (-2.77pp) and Apple Pay payment method (-0.99pp) degradation; correlate with Norway regional performance to determine if issues are linked.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 93.64% | 784,389 | -0.55% |
| 2026-W13 | 94.16% | 842,480 | -0.47% |
| 2026-W12 | 94.6% | 877,187 | -0.32% ← REPORTED CHANGE |
| 2026-W11 | 94.9% | 897,106 | +1.17% |
| 2026-W10 | 93.8% | 916,831 | +0.72% |
| 2026-W09 | 93.13% | 896,537 | -0.45% |
| 2026-W08 | 93.55% | 884,970 | -0.78% |
| 2026-W07 | 94.29% | 920,370 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| NO | 89.86% | 91.42% | -1.70% | 26,830 |  |
| LU | 95.2% | 96.65% | -1.49% | 3,667 |  |
| IE | 90.41% | 91.69% | -1.39% | 18,858 |  |
| CH | 93.37% | 94.44% | -1.13% | 2,399 |  |
| SE | 96.27% | 96.89% | -0.64% | 41,014 |  |
| GB | 93.58% | 94.09% | -0.53% | 230,971 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Apple Pay | 89.48% | 90.38% | -0.99% | 118,640 |
| PaymentMethod | Credit Card | 92.69% | 93.11% | -0.45% | 354,668 |
| PaymentMethod | Others | 97.61% | 97.83% | -0.23% | 181,531 |
| PaymentMethod | Paypal | 97.91% | 97.88% | +0.03% | 222,348 |
| PaymentProvider | Unknown | 87.41% | 89.9% | -2.77% | 2,605 |
| PaymentProvider | ProcessOut | 92.35% | 92.78% | -0.46% | 258,101 |
| PaymentProvider | Braintree | 95.28% | 95.54% | -0.27% | 335,416 |
| PaymentProvider | Adyen | 95.84% | 96.06% | -0.23% | 275,476 |
| PaymentProvider | No Payment | 99.89% | 99.95% | -0.06% | 5,589 |

---

*Report: 2026-04-10*
