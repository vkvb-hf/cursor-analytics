# Reactivation Investigation: US-HF 2026-W16

**Metric:** Reactivation Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 90.47% → 90.07% (-0.44%)  
**Volume:** 18,897 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** US-HF Reactivation Rate declined by -0.44% (from 90.47% to 90.07%) in 2026-W16, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range | -0.44% | ✅ |
| L1: Country Breakdown | No countries exceed ±2.5% threshold | -0.44% (US) | ✅ |
| L1: Dimension Scan | No payment methods flagged | -1.00% max (Credit Card) | ✅ |
| Mix Shift Analysis | Volume shift stable | -10.7% volume | ✅ |

**Key Findings:**
- The -0.44% decline continues a minor downward trend from 2026-W15 (-0.57%), but remains well above the 8-week low of 85.79% (2026-W09)
- Credit Card payments showed the largest rate decline at -1.00% (89.9% vs 90.81%), representing 68% of total volume (12,893 orders)
- PayPal (+0.67%) and Apple Pay (+0.91%) both improved week-over-week, partially offsetting Credit Card decline
- Order volume decreased by 10.7% (from 21,155 to 18,897 orders) but mix shift impact remains stable
- No countries or dimensions exceeded the ±2.5% investigation threshold

**Action:** Monitor — The decline is not statistically significant and no dimensions breach alerting thresholds. Continue standard weekly monitoring with attention to Credit Card payment performance if the trend persists.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 90.07% | 18,897 | -0.44% ← REPORTED CHANGE |
| 2026-W15 | 90.47% | 21,155 | -0.57% |
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
| US | 90.07% | 90.47% | -0.44% | 18,897 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 89.9% | 90.81% | -1.00% | 12,893 |  |
| Others | 50.0% | 50.0% | +0.00% | 2 |  |
| Paypal | 93.17% | 92.55% | +0.67% | 3,076 |  |
| Apple Pay | 87.56% | 86.77% | +0.91% | 2,926 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 21,155 | 18,897 | -10.7% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
