# PCAR Investigation: HF-INTL 2026-W13

**Metric:** PCAR  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 95.21% → 96.0% (+0.83%)  
**Volume:** 31,465 orders

## Executive Summary

**Overall:** PCAR improved from 95.21% to 96.0% (+0.83pp) in 2026-W13 to W14, representing a recovery from the prior week's decline of -1.52pp.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Metric recovering after W13 dip | +0.83pp | ✅ |
| L1: Country Breakdown | 7 of 8 countries declined; NO improved significantly | Mixed | ⚠️ |
| L1: Country Threshold | NO exceeded ±2.5% threshold (+2.76pp) | +2.76pp | ⚠️ |
| L1: Payment Method | "Others" payment method significant decline | -11.63pp | ⚠️ |

**Key Findings:**
- Norway (NO) showed a significant improvement of +2.76pp (89.86% → 92.35%), exceeding the ±2.5% threshold and flagged for review
- The "Others" payment method experienced a severe decline of -11.63pp (84.74% → 74.88%) on 4,081 orders, indicating a potential issue with alternative payment processing
- Switzerland (CH) had the largest country-level decline at -2.31pp (93.37% → 91.21%) on 2,401 orders
- Volume decreased significantly from 39,598 (W13) to 31,465 (W14), a drop of approximately 20.5%
- Credit Card payments showed slight improvement (+0.11pp) and maintained the highest rate at 97.89%

**Action:** Investigate — The "Others" payment method decline of -11.63pp requires immediate investigation to identify root cause. Additionally, monitor Switzerland's continued decline and validate the Norway improvement is sustainable.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 96.0% | 31,465 | +0.83% |
| 2026-W13 | 95.21% | 39,598 | -1.52% ← REPORTED CHANGE |
| 2026-W12 | 96.68% | 38,136 | -0.53% |
| 2026-W11 | 97.2% | 42,932 | -0.11% |
| 2026-W10 | 97.31% | 44,946 | +0.80% |
| 2026-W09 | 96.54% | 48,662 | +0.04% |
| 2026-W08 | 96.5% | 49,249 | -0.49% |
| 2026-W07 | 96.98% | 48,803 | - |

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
| PaymentMethod | Unknown | nan% | nan% | +nan% | 0 |
| PaymentMethod | Others | 74.88% | 84.74% | -11.63% | 4,081 |
| PaymentMethod | Apple Pay | 97.32% | 97.53% | -0.21% | 12,635 |
| PaymentMethod | Paypal | 97.27% | 97.45% | -0.19% | 8,163 |
| PaymentMethod | Credit Card | 97.89% | 97.78% | +0.11% | 14,719 |

---

*Report: 2026-04-10*
