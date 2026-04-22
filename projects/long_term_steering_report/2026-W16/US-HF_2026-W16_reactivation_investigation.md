# Reactivation Investigation: US-HF 2026-W16

**Metric:** Reactivation Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 90.47% → 90.07% (-0.44%)  
**Volume:** 18,897 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** US-HF Reactivation Rate declined from 90.47% to 90.07% (-0.40pp) in 2026-W16, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal fluctuation range (85.79%-91.26%) | -0.40pp | ✅ |
| L1: Country Breakdown | No countries exceeding ±2.5% threshold | -0.44% | ✅ |
| L1: Dimension Scan | No payment methods flagged; Credit Card largest decline | -1.00% | ✅ |
| Mix Shift Analysis | US Medium tier volume down 10.7% but impact stable | -10.7% vol | ✅ |

**Key Findings:**
- The -0.40pp decline continues a two-week downward trend (W14: 90.99% → W15: 90.47% → W16: 90.07%), though rate remains well above the 8-week low of 85.79% (W09)
- Credit Card payments showed the largest rate decline (-1.00%) and represent the highest volume (12,893 orders, ~68% of total)
- PayPal (+0.67%) and Apple Pay (+0.91%) both improved, partially offsetting Credit Card declines
- Order volume decreased by 10.7% (21,155 → 18,897) week-over-week, but mix shift impact remains stable
- No individual country or dimension exceeded investigation thresholds

**Action:** Monitor — The decline is not statistically significant and no dimensions exceeded alert thresholds. Continue standard monitoring; if Credit Card rate decline persists for a third consecutive week, consider targeted investigation.

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
