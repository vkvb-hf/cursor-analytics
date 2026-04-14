# Reactivation Investigation: RTE 2026-W15

**Metric:** Reactivation  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 89.2% → 90.41% (+1.36%)  
**Volume:** 19,757 orders

## Executive Summary

**Overall:** Reactivation rate improved from 89.2% to 90.41% (+1.21 pp) in W15, continuing a positive 8-week upward trend from 84.71% in W08, with volume at 19,757 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Consistent improvement over 8 weeks | +5.70 pp cumulative | ✅ |
| L1: Country Breakdown | 1 country exceeds ±2.5% threshold | TK: +7.54 pp | ⚠️ |
| L1: Payment Method | All methods within normal range | -1.50 pp to +2.78 pp | ✅ |

**Key Findings:**
- TK showed an exceptional improvement of +7.54 pp (88.65% → 95.33%) with 1,950 orders, flagged as an anomaly requiring review
- Credit Card payments, representing the largest volume (14,461 orders), improved by +1.59 pp to 92.71%
- TV and YE were the only countries showing decline (-1.37 pp and -0.43 pp respectively), though both remain within normal thresholds
- Apple Pay continues to underperform other payment methods at 68.62% (-1.50 pp), though volume is relatively low (1,893 orders)
- The 8-week trend shows sustained positive momentum with the metric climbing from 84.71% to 90.41%

**Action:** Monitor – The overall trend is positive and within expected parameters. Investigate TK's +7.54 pp spike to determine if it represents a sustainable improvement or data anomaly.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 90.41% | 19,757 | +1.36% ← REPORTED CHANGE |
| 2026-W14 | 89.2% | 17,264 | +0.68% |
| 2026-W13 | 88.6% | 19,685 | - |
| 2026-W12 | 88.6% | 20,873 | +1.87% |
| 2026-W11 | 86.97% | 23,790 | +2.19% |
| 2026-W10 | 85.11% | 26,102 | +0.75% |
| 2026-W09 | 84.48% | 24,364 | -0.27% |
| 2026-W08 | 84.71% | 24,536 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TV | 92.14% | 93.41% | -1.37% | 1,895 |  |
| YE | 87.77% | 88.15% | -0.43% | 42,126 |  |
| FJ | 93.97% | 93.62% | +0.38% | 388,956 |  |
| CF | 94.14% | 93.47% | +0.72% | 51,881 |  |
| TZ | 91.69% | 90.11% | +1.76% | 2,660 |  |
| TO | 86.67% | 84.89% | +2.11% | 3,204 |  |
| TK | 95.33% | 88.65% | +7.54% | 1,950 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TK

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Apple Pay | 68.62% | 69.66% | -1.50% | 1,893 |
| PaymentMethod | Paypal | 93.4% | 92.54% | +0.92% | 3,241 |
| PaymentMethod | Credit Card | 92.71% | 91.26% | +1.59% | 14,461 |
| PaymentMethod | Others | 80.25% | 78.08% | +2.78% | 162 |

---

*Report: 2026-04-14*
