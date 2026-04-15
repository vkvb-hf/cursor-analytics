# Reactivation Investigation: US-HF 2026-W15

**Metric:** Reactivation Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 90.99% → 90.47% (-0.57%)  
**Volume:** 21,155 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Reactivation Rate declined by -0.57% (from 90.99% to 90.47%) in W15, with volume increasing significantly from 14,736 to 21,155 orders; the change is flagged as not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Within normal range | -0.57% | ✅ |
| L1: Country Breakdown | No country exceeded ±2.5% threshold | US: +0.34% | ✅ |
| L1: PaymentMethod | "Others" flagged but minimal volume | -50.00% (4 orders) | ⚠️ |
| L1: PaymentProvider | No data available | - | ✅ |
| Mix Shift | High AR tier stable | -0.9% volume | ✅ |

**Key Findings:**
- The -0.57% decline follows a +0.40% improvement in W14, representing normal week-over-week fluctuation within the 8-week trend range (85.79% - 91.26%)
- Volume increased by 43.6% (14,736 → 21,155 orders), which may contribute to rate normalization toward the mean
- US country-level performance actually improved by +0.34% (92.78% → 93.09%), suggesting no underlying country-specific issue
- "Others" payment method shows a -50.00% decline but affects only 4 orders, making it statistically irrelevant
- PayPal shows the largest meaningful decline at -1.21% (93.68% → 92.55%) across 3,369 orders

**Action:** Monitor – No significant threshold breaches detected; the decline is within normal variance and not statistically significant. Continue standard weekly tracking.

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

*Report: 2026-04-15*
