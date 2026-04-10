# AR Overall Investigation: HF-INTL 2026-W13

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 94.16% → 93.64% (-0.55%)  
**Volume:** 784,389 orders

## Executive Summary

**Overall:** AR Overall declined by -0.55% (from 94.16% to 93.64%) in 2026-W13, representing the second consecutive weekly decline in the HF-INTL region with 784,389 orders processed.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Consecutive declines W12-W14 | -0.55% | ⚠️ |
| L1: Country Breakdown | CH exceeds threshold (-2.31pp) | -2.31% | ⚠️ |
| L1: Country Breakdown | NO positive outlier (+2.76pp) | +2.76% | ⚠️ |
| L1: PaymentMethod | Apple Pay underperforming | -1.36% | ⚠️ |
| L1: PaymentProvider | Unknown provider significant drop | -6.11% | ⚠️ |

**Key Findings:**
- CH experienced the largest country-level decline at -2.31pp (91.21% from 93.37%), though volume is relatively low at 2,401 orders
- PaymentProvider "Unknown" showed a significant drop of -6.11pp (82.07% from 87.41%) with 2,130 orders, indicating potential tracking or integration issues
- Apple Pay continues to underperform other payment methods at 88.27% (-1.36pp), affecting 113,387 orders (14.5% of volume)
- GB and FR, the two highest-volume countries (222,020 and 161,318 orders respectively), both declined by -0.51pp and -0.86pp
- NO is the only country showing improvement at +2.76pp, flagged as an outlier worth monitoring

**Action:** Investigate - Focus on the Unknown PaymentProvider drop (-6.11pp) and Apple Pay performance degradation across high-volume markets (GB, FR). Coordinate with payment integration teams to identify root cause.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 93.64% | 784,389 | -0.55% |
| 2026-W13 | 94.16% | 842,480 | -0.47% ← REPORTED CHANGE |
| 2026-W12 | 94.6% | 877,187 | -0.32% |
| 2026-W11 | 94.9% | 897,106 | +1.17% |
| 2026-W10 | 93.8% | 916,831 | +0.72% |
| 2026-W09 | 93.13% | 896,537 | -0.45% |
| 2026-W08 | 93.55% | 884,970 | -0.78% |
| 2026-W07 | 94.29% | 920,370 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CH | 91.21% | 93.37% | -2.31% | 2,401 |  |
| SE | 95.03% | 96.27% | -1.29% | 40,582 |  |
| BE | 95.31% | 96.16% | -0.88% | 75,558 |  |
| AT | 95.19% | 96.03% | -0.88% | 14,386 |  |
| FR | 93.7% | 94.51% | -0.86% | 161,318 |  |
| GB | 93.11% | 93.58% | -0.51% | 222,020 |  |
| DE | 97.22% | 97.62% | -0.41% | 225,448 |  |
| NO | 92.35% | 89.86% | +2.76% | 25,359 | ⚠️ |

**Countries exceeding ±2.5% threshold:** NO

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Apple Pay | 88.27% | 89.48% | -1.36% | 113,387 |
| PaymentMethod | Credit Card | 92.31% | 92.69% | -0.42% | 350,055 |
| PaymentMethod | Paypal | 97.66% | 97.91% | -0.25% | 210,289 |
| PaymentMethod | Others | 97.61% | 97.61% | +0.00% | 168,749 |
| PaymentProvider | Unknown | 82.07% | 87.41% | -6.11% | 2,130 |
| PaymentProvider | Braintree | 94.69% | 95.28% | -0.62% | 318,019 |
| PaymentProvider | ProcessOut | 91.89% | 92.35% | -0.49% | 247,011 |
| PaymentProvider | Adyen | 95.59% | 95.84% | -0.26% | 270,063 |
| PaymentProvider | No Payment | 99.94% | 99.89% | +0.05% | 5,257 |

---

*Report: 2026-04-10*
