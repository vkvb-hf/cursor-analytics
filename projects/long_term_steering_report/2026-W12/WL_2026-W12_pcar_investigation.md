# PCAR Investigation: WL 2026-W12

**Metric:** PCAR  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 97.07% → 97.03% (-0.04%)  
**Volume:** 11,373 orders

## Executive Summary

**Overall:** PCAR declined by 0.04 percentage points (97.07% → 97.03%) on volume of 11,373 orders, representing a minor week-over-week decrease that remains within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL Trend | 8-week stability check | -0.04pp | ✅ Rate stable, well above W07 low of 94.85% |
| L1: Country | Any country >±2.5% threshold | None flagged | ✅ No countries exceed threshold |
| L1: Dimension | Payment method anomalies | -0.70pp Apple Pay | ⚠️ Apple Pay shows largest decline |

**Key Findings:**
- The -0.04pp decline is minimal and follows a +0.20pp improvement the prior week (W13), indicating normal fluctuation
- MR shows the lowest absolute PCAR rate at 80.0% (-1.38pp) with highest volume (18,070 orders), though below the ±2.5% alert threshold
- Apple Pay experienced the largest payment method decline at -0.70pp (97.12% → 96.44%) on 4,550 orders
- Credit Card performance improved +0.31pp (96.74% → 97.04%) on the highest payment volume (8,076 orders)
- Overall 8-week trend shows recovery from W07 low (94.85%) with current rate stabilizing near 97%

**Action:** Monitor — The decline is within normal variance, no dimensions exceed alert thresholds, and the 8-week trend remains stable. Continue standard monitoring with attention to MR's persistently low rate and Apple Pay performance.

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
