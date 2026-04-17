# Reactivation Investigation: US-HF 2026-W15

**Metric:** Reactivation Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 90.99% → 90.47% (-0.57%)  
**Volume:** 21,155 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Reactivation Rate declined by -0.57% (from 90.99% to 90.47%) in 2026-W15, a statistically non-significant change that remains within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 8-Week Trend | Rate within historical range (85.79%-91.26%) | -0.52pp | ✅ |
| Country Breakdown | US performance (+0.34%) | No threshold breach | ✅ |
| Payment Method | "Others" flagged (-50.00%) | Low volume (4 orders) | ⚠️ |
| Mix Shift | High AR tier volume shift | -0.9% (Stable) | ✅ |

**Key Findings:**
- The -0.57% decline reverses the prior week's +0.40% gain but remains well above the 8-week low of 85.79% (W09)
- Volume increased significantly from 14,736 to 21,155 orders (+43.6%), which may contribute to rate normalization
- "Others" payment method shows a -50.00% decline but represents only 4 orders, making it statistically irrelevant
- US country-level performance actually improved +0.34% despite the overall metric decline
- PayPal showed the largest meaningful decline at -1.21% (3,369 orders), followed by Apple Pay at -0.55% (3,197 orders)

**Action:** Monitor – The decline is not statistically significant, no countries exceeded the ±2.5% threshold, and the flagged payment method ("Others") has negligible volume. Continue standard weekly monitoring.

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
