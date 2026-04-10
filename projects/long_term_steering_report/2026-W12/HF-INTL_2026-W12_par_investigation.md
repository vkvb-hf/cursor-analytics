# PAR Investigation: HF-INTL 2026-W12

**Metric:** PAR  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 97.17% → 97.04% (-0.13%)  
**Volume:** 784,389 orders

## Executive Summary

**Overall:** PAR declined by -0.13 percentage points (97.17% → 97.04%) in 2026-W12 on a volume of 784,389 orders, interrupting a positive trend that had seen the metric improve from 96.22% in W09 to 97.25% in W12.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate above 8-week baseline (96.55% W07) | +0.49 pp | ✅ |
| L1: Country Threshold | Any country exceeding ±2.5% threshold | None | ✅ |
| L1: Country Declines | Countries with notable declines | NO (-1.70 pp), LU (-1.49 pp), IE (-1.39 pp) | ⚠️ |
| L1: Payment Method | Payment method variance | Apple Pay -0.11 pp | ✅ |
| L1: Payment Provider | Provider variance | Unknown -1.23 pp (low volume: 2,605) | ✅ |

**Key Findings:**
- NO showed the largest country decline at -1.70 pp (91.42% → 89.86%) on 26,830 orders
- LU and IE also experienced significant declines of -1.49 pp and -1.39 pp respectively, though both have relatively low volumes
- GB, the highest volume country (230,971 orders), declined -0.53 pp which contributed meaningfully to the overall decline due to its scale
- The "Unknown" PaymentProvider showed a -1.23 pp decline but represents only 2,605 orders (0.3% of volume)
- Despite the weekly decline, PAR remains elevated compared to the 8-week low of 96.22% in W09

**Action:** Monitor – The decline is modest (-0.13 pp), no countries exceeded the ±2.5% threshold, and the metric remains within healthy historical range. Continue monitoring NO and IE performance in the next weekly cycle.

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
