# Reactivation Investigation: US-HF 2026-W15

**Metric:** Reactivation Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 90.99% → 90.47% (-0.57%)  
**Volume:** 21,155 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Reactivation Rate declined from 90.99% to 90.47% (-0.52 pp) in W15, but this change is not statistically significant given the 43.5% increase in order volume.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (85.79%-91.26%) | -0.52 pp | ✅ |
| L1: Country Breakdown | US +0.34 pp, no countries exceed ±2.5% threshold | +0.34 pp | ✅ |
| L1: PaymentMethod | "Others" flagged at -50.00 pp | -50.00 pp | ⚠️ |
| L1: PaymentProvider | No data available | N/A | ✅ |
| Mix Shift | US High AR Tier volume -0.9% | Stable | ✅ |

**Key Findings:**
- The -0.52 pp decline is within normal weekly fluctuation; 8-week trend shows consistent improvement from 85.84% (W08) to 90.47% (W15)
- Volume increased significantly from 14,736 to 21,155 orders (+43.5%), which may explain minor rate variance
- "Others" payment method shows -50.00 pp drop but represents only 4 orders (negligible impact)
- PayPal showed the largest meaningful decline at -1.21 pp (3,369 orders)
- US country-level performance actually improved +0.34 pp despite overall HF decline

**Action:** Monitor — No investigation required. The change is not statistically significant, no countries exceeded the ±2.5% threshold, and the flagged "Others" payment method has minimal volume (4 orders).

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 90.47% | 21,155 | -0.57% ← REPORTED CHANGE |
| 2026-W14 | 90.99% | 14,736 | +0.40% |
| 2026-W13 | 90.63% | 15,928 | -0.69% |
| 2026-W12 | 91.26% | 15,787 | +2.56% |
| 2026-W11 | 88.98% | 17,703 | +1.39% |
| 2026-W10 | 87.76% | 22,710 | +2.30% |
| 2026-W09 | 85.79% | 18,047 | -0.06% |
| 2026-W08 | 85.84% | 18,573 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 93.09% | 92.78% | +0.34% | 492,811 |  |

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
| US | High (>92%) | 497,052 | 492,811 | -0.9% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-17*
