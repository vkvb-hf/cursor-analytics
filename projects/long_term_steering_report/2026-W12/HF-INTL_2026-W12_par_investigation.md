# PAR Investigation: HF-INTL 2026-W12

**Metric:** PAR  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 97.17% → 97.04% (-0.13%)  
**Volume:** 784,389 orders

## Executive Summary

## Executive Summary

**Overall:** PAR declined from 97.17% to 97.04% (-0.13pp) in 2026-W12 on a volume of 784,389 orders, representing the second consecutive weekly decline after a period of improvement.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Consistent pattern? | -0.13pp (2nd consecutive decline) | ⚠️ |
| L1: Country | Any >±2.5% threshold? | NO (-1.70pp), LU (-1.49pp), IE (-1.39pp) | ✅ |
| L1: Payment Method | Significant shift? | Apple Pay -0.11pp, minimal changes | ✅ |
| L1: Payment Provider | Significant shift? | Unknown -1.23pp (low volume: 2,605) | ✅ |

**Key Findings:**
- **Trend reversal emerging:** After peaking at 97.25% in W12, PAR has declined for two consecutive weeks (-0.08pp then -0.13pp), erasing gains from W10-W11
- **Norway leads country declines:** NO experienced the largest drop at -1.70pp (89.86%), followed by LU (-1.49pp) and IE (-1.39pp), though none breach the ±2.5% threshold
- **GB contributes highest absolute impact:** With 230,971 orders (29% of volume) and a -0.53pp decline, GB's deterioration has significant weight on overall PAR
- **Payment dimensions stable:** No payment method or provider shows significant degradation; Unknown provider dropped -1.23pp but represents only 0.3% of volume (2,605 orders)
- **Volume declining:** Order volume dropped from 842,480 to 784,389 (-6.9%), continuing a downward trend from the W11 peak of 897,106

**Action:** **Monitor** – The -0.13pp decline does not breach critical thresholds, and no single dimension shows anomalous behavior exceeding ±2.5%. However, continue monitoring NO, IE, and GB for further deterioration given their consecutive weekly declines.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 97.04% | 784,389 | -0.13% |
| 2026-W13 | 97.17% | 842,480 | -0.08% |
| 2026-W12 | 97.25% | 877,187 | +0.04% ← REPORTED CHANGE |
| 2026-W11 | 97.21% | 897,106 | +0.52% |
| 2026-W10 | 96.71% | 916,831 | +0.51% |
| 2026-W09 | 96.22% | 896,537 | -0.12% |
| 2026-W08 | 96.34% | 884,970 | -0.22% |
| 2026-W07 | 96.55% | 920,370 | - |

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
| PaymentMethod | Apple Pay | 93.47% | 93.57% | -0.11% | 118,640 |
| PaymentMethod | Others | 98.73% | 98.77% | -0.05% | 181,531 |
| PaymentMethod | Credit Card | 96.65% | 96.61% | +0.04% | 354,668 |
| PaymentMethod | Paypal | 99.02% | 98.92% | +0.10% | 222,348 |
| PaymentProvider | Unknown | 89.9% | 91.03% | -1.23% | 2,605 |
| PaymentProvider | No Payment | 99.89% | 99.95% | -0.06% | 5,589 |
| PaymentProvider | ProcessOut | 95.89% | 95.92% | -0.03% | 258,101 |
| PaymentProvider | Braintree | 97.33% | 97.28% | +0.05% | 335,416 |
| PaymentProvider | Adyen | 98.44% | 98.36% | +0.08% | 275,476 |

---

*Report: 2026-04-10*
