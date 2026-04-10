# Reactivation Investigation: RTE 2026-W12

**Metric:** Reactivation  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 88.6% → 89.2% (+0.68%)  
**Volume:** 17,264 orders

## Executive Summary

**Overall:** Reactivation rate improved from 88.6% to 89.2% (+0.68 pp) week-over-week, continuing a positive upward trend observed over the past 5 weeks.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 8-Week Trend | Consistent improvement since W09 | +4.7 pp from W09 to W14 | ✅ |
| Country Breakdown | No country exceeds ±2.5% threshold | Largest: TK at -1.64 pp | ✅ |
| Payment Method | Credit Card shows notable improvement | +2.79 pp | ⚠️ |
| Volume Trend | Declining order volume | 17,264 vs 19,685 prior week | ⚠️ |

**Key Findings:**
- Reactivation rate has steadily climbed from 84.48% (W09) to 89.2% (W14), representing a +4.72 pp improvement over 5 weeks
- Credit Card payment method showed the strongest improvement at +2.79 pp (88.45% → 90.92%), driving 14,723 orders (85% of volume)
- TK experienced the largest country-level decline at -1.64 pp (93.49% → 91.96%), though still within acceptable thresholds
- Apple Pay continues to underperform other payment methods with the lowest reactivation rate at 66.77% (-1.42 pp)
- Order volume has decreased by 12.3% week-over-week (19,685 → 17,264), warranting monitoring

**Action:** Monitor - The metric shows healthy improvement with no dimensions exceeding alert thresholds. Continue tracking the declining volume trend and Apple Pay's persistent underperformance for potential future investigation.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 89.2% | 17,264 | +0.68% |
| 2026-W13 | 88.6% | 19,685 | - |
| 2026-W12 | 88.6% | 20,873 | +1.87% ← REPORTED CHANGE |
| 2026-W11 | 86.97% | 23,790 | +2.19% |
| 2026-W10 | 85.11% | 26,102 | +0.75% |
| 2026-W09 | 84.48% | 24,364 | -0.27% |
| 2026-W08 | 84.71% | 24,536 | -1.01% |
| 2026-W07 | 85.57% | 24,688 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TK | 91.96% | 93.49% | -1.64% | 2,338 |  |
| TV | 93.47% | 94.31% | -0.89% | 2,205 |  |
| TO | 86.85% | 87.27% | -0.49% | 3,611 |  |
| FJ | 94.3% | 94.46% | -0.17% | 408,532 |  |
| CF | 93.62% | 93.52% | +0.10% | 53,267 |  |
| YE | 88.62% | 88.28% | +0.39% | 48,432 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Apple Pay | 66.77% | 67.73% | -1.42% | 1,971 |
| PaymentMethod | Paypal | 92.28% | 92.2% | +0.08% | 3,808 |
| PaymentMethod | Others | 74.93% | 74.16% | +1.05% | 371 |
| PaymentMethod | Credit Card | 90.92% | 88.45% | +2.79% | 14,723 |

---

*Report: 2026-04-10*
