# PAR Investigation: HF-INTL 2026-W13

**Metric:** PAR  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 97.17% → 97.04% (-0.13%)  
**Volume:** 784,389 orders

## Executive Summary

**Overall:** PAR declined by -0.13pp (97.17% → 97.04%) on volume of 784,389 orders in 2026-W13, continuing a downward trend from the recent peak of 97.25% in W12.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Sustained decline pattern | -0.13pp | ⚠️ |
| L1: Country Breakdown | 7 of 8 countries declined | CH -2.31pp, SE -1.29pp | ⚠️ |
| L1: Country Threshold | NO exceeds ±2.5% threshold | +2.76pp | ⚠️ |
| L1: Payment Method | All methods stable or slight decline | Apple Pay -0.36pp | ✅ |
| L1: Payment Provider | Unknown provider significant drop | -5.22pp | ⚠️ |

**Key Findings:**
- CH experienced the largest PAR decline at -2.31pp (93.37% → 91.21%) on 2,401 orders
- SE and BE both declined notably by -1.29pp and -0.88pp respectively, with BE contributing significant volume (75,558 orders)
- PaymentProvider "Unknown" dropped -5.22pp (89.9% → 85.21%) though on limited volume (2,130 orders)
- NO showed anomalous improvement of +2.76pp against the overall declining trend, flagged for threshold breach
- Major markets GB (-0.51pp), DE (-0.41pp), and FR (-0.86pp) all contributed to the overall decline with combined volume exceeding 608,000 orders

**Action:** Investigate — Focus on CH and SE country-specific issues, and identify root cause for "Unknown" payment provider degradation. Monitor NO for data quality or process changes explaining the counter-trend improvement.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 97.04% | 784,389 | -0.13% |
| 2026-W13 | 97.17% | 842,480 | -0.08% ← REPORTED CHANGE |
| 2026-W12 | 97.25% | 877,187 | +0.04% |
| 2026-W11 | 97.21% | 897,106 | +0.52% |
| 2026-W10 | 96.71% | 916,831 | +0.51% |
| 2026-W09 | 96.22% | 896,537 | -0.12% |
| 2026-W08 | 96.34% | 884,970 | -0.22% |
| 2026-W07 | 96.55% | 920,370 | - |

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
| PaymentMethod | Apple Pay | 93.13% | 93.47% | -0.36% | 113,387 |
| PaymentMethod | Paypal | 98.97% | 99.02% | -0.05% | 210,289 |
| PaymentMethod | Credit Card | 96.62% | 96.65% | -0.04% | 350,055 |
| PaymentMethod | Others | 98.77% | 98.73% | +0.05% | 168,749 |
| PaymentProvider | Unknown | 85.21% | 89.9% | -5.22% | 2,130 |
| PaymentProvider | Braintree | 97.2% | 97.33% | -0.13% | 318,019 |
| PaymentProvider | ProcessOut | 95.77% | 95.89% | -0.13% | 247,011 |
| PaymentProvider | Adyen | 98.44% | 98.44% | +0.00% | 270,063 |
| PaymentProvider | No Payment | 99.94% | 99.89% | +0.05% | 5,257 |

---

*Report: 2026-04-10*
