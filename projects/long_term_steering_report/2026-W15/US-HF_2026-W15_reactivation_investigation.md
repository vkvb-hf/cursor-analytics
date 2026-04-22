# Reactivation Investigation: US-HF 2026-W15

**Metric:** Reactivation Rate  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 90.47% → 90.07% (-0.44%)  
**Volume:** 18,897 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Reactivation Rate declined by -0.44% (from 90.47% to 90.07%) in W15, representing a statistically non-significant change on a volume of 18,897 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Within normal variance | -0.44% | ✅ |
| L1: Country Breakdown | US only, no threshold breach | -0.58% | ✅ |
| L1: PaymentMethod Scan | "Others" flagged but minimal volume (4 orders) | -50.00pp | ⚠️ |
| Mix Shift Analysis | Volume shift to Medium tier (+43.6%) | Stable | ✅ |

**Key Findings:**
- The -0.44% decline is within normal weekly fluctuation; the 8-week trend shows overall improvement from 85.79% (W09) to 90.07% (W16)
- US is the sole market with a -0.58% rate decline, but this does not exceed the ±2.5% threshold
- PaymentMethod "Others" shows a -50.00pp drop, but volume is negligible (4 orders) and not statistically meaningful
- Credit Card remains the dominant payment method (14,585 orders) with only a minor -0.45% decline
- Volume increased significantly (+43.6%) in the Medium AR tier, but mix shift impact remained stable

**Action:** Monitor — The decline is not statistically significant, no dimensions exceed thresholds with meaningful volume, and the 8-week trend remains positive. Continue standard monitoring.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 90.07% | 18,897 | -0.44% |
| 2026-W15 | 90.47% | 21,155 | -0.57% ← REPORTED CHANGE |
| 2026-W14 | 90.99% | 14,736 | +0.40% |
| 2026-W13 | 90.63% | 15,928 | -0.69% |
| 2026-W12 | 91.26% | 15,787 | +2.56% |
| 2026-W11 | 88.98% | 17,703 | +1.39% |
| 2026-W10 | 87.76% | 22,710 | +2.30% |
| 2026-W09 | 85.79% | 18,047 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 90.47% | 90.99% | -0.58% | 21,155 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 50.0% | 100.0% | -50.00% | 4 | ⚠️ |
| Paypal | 92.55% | 93.68% | -1.21% | 3,369 |  |
| Apple Pay | 86.77% | 87.25% | -0.55% | 3,197 |  |
| Credit Card | 90.81% | 91.21% | -0.45% | 14,585 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 14,736 | 21,155 | +43.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
