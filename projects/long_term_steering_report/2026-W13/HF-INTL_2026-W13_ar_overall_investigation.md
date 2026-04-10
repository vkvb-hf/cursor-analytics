# AR Overall Investigation: HF-INTL 2026-W13

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 94.16% → 93.64% (-0.55%)  
**Volume:** 784,389 orders

## Executive Summary

**Overall:** AR Overall for HF-INTL declined from 94.16% to 93.64% (-0.55pp) in W13→W14, continuing a 3-week downward trend with volume decreasing to 784,389 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Sustained decline pattern (W12-W14) | -0.96pp over 3 weeks | ⚠️ |
| L1: Country Breakdown | 7 of 8 countries declined; CH worst at -2.31pp | -2.31pp to +2.76pp range | ⚠️ |
| L1: Payment Method | Apple Pay lowest performer | -1.36pp | ⚠️ |
| L1: Payment Provider | Unknown provider significant drop | -6.11pp | ⚠️ |

**Key Findings:**
- **Payment Provider "Unknown" dropped -6.11pp** (87.41% → 82.07%), though low volume (2,130 orders) limits overall impact
- **Switzerland (CH) saw the largest country decline at -2.31pp** (93.37% → 91.21%), albeit on small volume (2,401 orders)
- **Apple Pay underperforms** at 88.27% (-1.36pp), the lowest rate among payment methods with significant volume (113,387 orders)
- **Norway (NO) improved +2.76pp** (89.86% → 92.35%), the only country showing positive movement and exceeding the ±2.5% threshold
- **GB and FR represent high-impact volume** (383,338 combined orders) both declining -0.51pp and -0.86pp respectively

**Action:** **Investigate** – The sustained 3-week decline, combined with the significant drop in the "Unknown" payment provider and Apple Pay underperformance, warrants investigation into payment processing issues, particularly for Braintree and ProcessOut which serve Apple Pay and Credit Card transactions.

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
