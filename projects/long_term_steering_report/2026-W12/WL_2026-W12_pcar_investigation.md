# PCAR Investigation: WL 2026-W12

**Metric:** PCAR  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 97.07% → 97.03% (-0.04%)  
**Volume:** 11,373 orders

## Executive Summary

**Overall:** PCAR declined by -0.04 percentage points (pp) from 97.07% to 97.03% in WL 2026-W12, representing a minor week-over-week decrease on a volume of 11,373 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL Trend | 8-week stability check | -0.04 pp | ✅ Within normal range; rate stable at ~97% for past 4 weeks |
| L1: Country | ±2.5% threshold | None exceeded | ✅ No country flagged; largest decline MR at -1.38 pp |
| L1: Dimension (Payment) | Payment method variance | Apple Pay -0.70 pp | ⚠️ Apple Pay shows notable decline vs other methods |

**Key Findings:**
- The -0.04 pp decline is minimal and within normal weekly fluctuation; the 8-week trend shows recovery from a low of 94.85% in W07 to stable ~97% range
- No countries exceeded the ±2.5% threshold, though MR (-1.38 pp) and KN (-1.31 pp) showed the largest declines
- Apple Pay experienced a -0.70 pp decline (96.44% from 97.12%), underperforming compared to Credit Card which improved +0.31 pp
- Volume decreased significantly from 13,604 (W13) to 11,373 (W12), a drop of ~16% in order volume
- Credit Card remains the highest volume payment method (8,076 orders) and showed positive performance (+0.31 pp)

**Action:** Monitor — The decline is minor (-0.04 pp) with no dimensions exceeding alert thresholds. Continue monitoring Apple Pay performance and volume trends in the next weekly cycle.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 97.03% | 11,373 | -0.04% |
| 2026-W13 | 97.07% | 13,604 | +0.20% |
| 2026-W12 | 96.88% | 14,412 | -0.07% ← REPORTED CHANGE |
| 2026-W11 | 96.95% | 15,835 | -0.43% |
| 2026-W10 | 97.37% | 16,267 | +0.03% |
| 2026-W09 | 97.34% | 15,555 | +0.50% |
| 2026-W08 | 96.86% | 16,585 | +2.12% |
| 2026-W07 | 94.85% | 16,452 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| MR | 80.0% | 81.12% | -1.38% | 18,070 |  |
| KN | 87.76% | 88.93% | -1.31% | 10,617 |  |
| GN | 93.64% | 94.18% | -0.57% | 16,164 |  |
| CK | 93.33% | 93.63% | -0.32% | 42,397 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Unknown | nan% | nan% | +nan% | 0 |
| PaymentMethod | Others | nan% | nan% | +nan% | 0 |
| PaymentMethod | Apple Pay | 96.44% | 97.12% | -0.70% | 4,550 |
| PaymentMethod | Paypal | 97.31% | 97.48% | -0.17% | 1,786 |
| PaymentMethod | Credit Card | 97.04% | 96.74% | +0.31% | 8,076 |

---

*Report: 2026-04-10*
