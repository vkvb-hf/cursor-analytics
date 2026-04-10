# AR Overall Investigation: HF-INTL 2026-W12

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 94.16% → 93.64% (-0.55%)  
**Volume:** 784,389 orders

## Executive Summary

**Overall:** AR Overall declined by -0.55% (from 94.16% to 93.64%) in 2026-W12, representing the third consecutive week of decline with a total volume of 784,389 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Consistent decline pattern | -0.55% WoW | ⚠️ |
| L1: Country Breakdown | NO, LU, IE leading declines | -1.70% to -1.13% | ⚠️ |
| L1: Country Threshold | Countries exceeding ±2.5% | None | ✅ |
| L1: PaymentMethod | Apple Pay underperforming | -0.99% | ⚠️ |
| L1: PaymentProvider | Unknown provider flagged | -2.77% | ⚠️ |

**Key Findings:**
- Three consecutive weeks of decline: W11 (+1.17%) → W12 (-0.32%) → W13 (-0.47%) → W14 (-0.55%), indicating an accelerating negative trend
- NO shows the largest country-level decline at -1.70pp (89.86%), followed by LU at -1.49pp and IE at -1.39pp
- PaymentProvider "Unknown" shows the most significant dimension decline at -2.77pp (87.41%), though volume is limited (2,605 orders)
- Apple Pay continues to underperform other payment methods at 89.48% (-0.99pp), with substantial volume of 118,640 orders
- GB represents the largest volume (230,971 orders) with a -0.53pp decline, contributing significantly to overall metric movement

**Action:** Investigate — The sustained three-week declining trend combined with notable drops in NO, IE, and the Apple Pay payment method warrants deeper investigation into root causes before further deterioration occurs.

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
