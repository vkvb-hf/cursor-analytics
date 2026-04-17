# Reactivation Investigation: US-HF 2026-W15

**Metric:** Reactivation Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 90.99% → 90.47% (-0.57%)  
**Volume:** 21,155 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Reactivation Rate declined by 0.52 percentage points (pp) from 90.99% to 90.47% in W15, a statistically non-significant change within normal weekly fluctuation patterns.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 8-Week Trend | Rate within historical range (85.79%-91.26%) | -0.52pp | ✅ |
| Country Breakdown | US at +0.34%, no country exceeds ±2.5% threshold | +0.34pp | ✅ |
| Payment Method | "Others" flagged at -50.00pp but minimal volume (4 orders) | -50.00pp | ⚠️ |
| Mix Shift | High AR tier volume stable (-0.9%) | -0.9% vol | ✅ |

**Key Findings:**
- The W15 decline of -0.52pp follows a W14 increase of +0.40pp, representing normal week-over-week volatility
- US country-level performance actually improved (+0.34pp), suggesting the aggregate decline is driven by mix or segment composition
- The "Others" payment method shows a dramatic -50.00pp decline but represents only 4 orders (0.02% of volume), making it statistically irrelevant
- Volume increased significantly from 14,736 to 21,155 orders (+43.6%), which may contribute to rate normalization
- Current rate of 90.47% remains elevated compared to the 8-week low of 85.79% in W09

**Action:** Monitor — No significant deviations detected; the change is within normal operating variance and no dimensions exceeded investigation thresholds.

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
