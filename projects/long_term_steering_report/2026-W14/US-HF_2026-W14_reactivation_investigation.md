# Reactivation Investigation: US-HF 2026-W14

**Metric:** Reactivation  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 90.63% → 90.99% (+0.40%)  
**Volume:** 14,736 orders

## Executive Summary

**Overall:** The Reactivation metric improved from 90.63% to 90.99% (+0.40 pp) in W14, continuing a positive trend that has seen the rate increase approximately 5.75 pp since W07 (85.24%).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Sustained upward trend from 85.24% (W07) to 90.99% (W14) | +0.40 pp | ✅ |
| L1: Country | US rate stable at 92.79% vs 92.85% | -0.07 pp | ✅ |
| L1: Payment Method | Apple Pay declined; Credit Card improved | Mixed | ⚠️ |

**Key Findings:**
- The +0.40 pp weekly improvement represents a recovery from W13's -0.69 pp dip, returning closer to W12's peak of 91.26%
- Volume decreased by 7.5% (15,928 → 14,736 orders), which is the lowest volume in the 8-week window
- Apple Pay shows the largest payment method decline at -1.55 pp (88.62% → 87.25%), though it represents only 15.8% of order volume (2,329 orders)
- Credit Card, the dominant payment method with 67.8% of volume (9,982 orders), improved by +0.90 pp (90.4% → 91.21%), driving the overall improvement
- No countries exceeded the ±2.5% threshold, indicating geographic stability

**Action:** Monitor — The metric is trending positively within normal operational variance. Continue tracking Apple Pay performance for potential emerging issues, but no immediate investigation required.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 90.99% | 14,736 | +0.40% ← REPORTED CHANGE |
| 2026-W13 | 90.63% | 15,928 | -0.69% |
| 2026-W12 | 91.26% | 15,787 | +2.56% |
| 2026-W11 | 88.98% | 17,703 | +1.39% |
| 2026-W10 | 87.76% | 22,710 | +2.30% |
| 2026-W09 | 85.79% | 18,047 | -0.06% |
| 2026-W08 | 85.84% | 18,573 | +0.70% |
| 2026-W07 | 85.24% | 19,572 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.79% | 92.85% | -0.07% | 497,052 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Apple Pay | 87.25% | 88.62% | -1.55% | 2,329 |
| PaymentMethod | Others | 100.0% | 100.0% | +0.00% | 3 |
| PaymentMethod | Paypal | 93.68% | 93.58% | +0.11% | 2,422 |
| PaymentMethod | Credit Card | 91.21% | 90.4% | +0.90% | 9,982 |

---

*Report: 2026-04-09*
