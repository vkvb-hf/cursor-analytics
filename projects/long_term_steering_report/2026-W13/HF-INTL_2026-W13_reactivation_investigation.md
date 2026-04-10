# Reactivation Investigation: HF-INTL 2026-W13

**Metric:** Reactivation  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 90.03% → 90.92% (+0.99%)  
**Volume:** 32,555 orders

## Executive Summary

**Overall:** The Reactivation rate for HF-INTL improved from 90.03% to 90.92% (+0.89 pp) in 2026-W14, representing a positive reversal after two consecutive weeks of decline.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | 8-week stability check | +0.99% | ✅ |
| L1: Country Breakdown | Threshold ±2.5% | NO: +2.76%, CH: -2.31% | ⚠️ |
| L1: Payment Method | Dimension scan | Max Δ: -0.82% (Apple Pay) | ✅ |

**Key Findings:**
- Norway (NO) shows a significant positive swing of +2.76 pp (89.86% → 92.35%), exceeding the ±2.5% threshold and flagged for attention
- Switzerland (CH) experienced the largest decline at -2.31 pp (93.37% → 91.21%), approaching the monitoring threshold
- Volume decreased substantially from 43,179 to 32,555 orders (-24.6%), which may amplify rate volatility
- Apple Pay shows the weakest performance among payment methods at 89.81% with a -0.82 pp decline
- The overall improvement breaks a two-week declining trend (W12: -0.20%, W13: -0.19%)

**Action:** Monitor – The overall metric is trending positively and within normal bounds. Continue monitoring Norway's unusual +2.76 pp improvement and Switzerland's -2.31 pp decline to determine if these represent sustained shifts or one-week anomalies.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 90.92% | 32,555 | +0.99% |
| 2026-W13 | 90.03% | 43,179 | -0.19% ← REPORTED CHANGE |
| 2026-W12 | 90.2% | 42,003 | -0.20% |
| 2026-W11 | 90.38% | 45,133 | +0.33% |
| 2026-W10 | 90.08% | 48,534 | -0.90% |
| 2026-W09 | 90.9% | 55,010 | +0.04% |
| 2026-W08 | 90.86% | 54,907 | +1.12% |
| 2026-W07 | 89.85% | 44,800 | - |

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
| PaymentMethod | Apple Pay | 89.81% | 90.55% | -0.82% | 7,114 |
| PaymentMethod | Credit Card | 84.64% | 84.85% | -0.24% | 19,521 |
| PaymentMethod | Paypal | 96.21% | 96.36% | -0.16% | 11,976 |
| PaymentMethod | Others | 97.24% | 96.79% | +0.46% | 4,568 |

---

*Report: 2026-04-10*
