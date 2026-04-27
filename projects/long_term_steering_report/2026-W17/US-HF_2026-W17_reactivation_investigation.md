# Reactivation Investigation: US-HF 2026-W17

**Metric:** Reactivation Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 90.07% → 89.71% (-0.40%)  
**Volume:** 15,063 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** US-HF Reactivation Rate declined slightly from 90.07% to 89.71% (-0.36 pp) in W17, a statistically non-significant change continuing a gradual downward trend observed since W12.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Gradual decline from 91.26% (W12) to 89.71% (W17) | -1.55 pp over 5 weeks | ⚠️ |
| L1: Country Breakdown | US is sole country, -0.40% change | -0.36 pp | ✅ |
| L1: PaymentMethod | Paypal shows largest decline (-1.49%) | -1.38 pp | ⚠️ |
| L1: PaymentProvider | No data available | N/A | ✅ |
| Mix Shift | US Medium tier volume dropped 20.3% | -3,834 orders | ⚠️ |

**Key Findings:**
- The -0.36 pp decline is not statistically significant and falls well within normal weekly fluctuation
- PayPal payment method showed the largest rate decline (-1.38 pp, from 93.17% to 91.79%) with 2,532 orders
- Significant volume contraction of 20.3% (18,897 → 15,063 orders) observed week-over-week
- 8-week trend shows rates have declined ~1.55 pp since peak at W12 (91.26%), suggesting gradual erosion rather than acute issue
- No payment providers flagged and no countries exceeded the ±2.5% threshold

**Action:** Monitor – Continue tracking the gradual downward trend and PayPal performance; no immediate investigation warranted given non-significant change and no threshold breaches.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 89.71% | 15,063 | -0.40% ← REPORTED CHANGE |
| 2026-W16 | 90.07% | 18,897 | -0.44% |
| 2026-W15 | 90.47% | 21,155 | -0.57% |
| 2026-W14 | 90.99% | 14,736 | +0.40% |
| 2026-W13 | 90.63% | 15,928 | -0.69% |
| 2026-W12 | 91.26% | 15,787 | +2.56% |
| 2026-W11 | 88.98% | 17,703 | +1.39% |
| 2026-W10 | 87.76% | 22,710 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 89.71% | 90.07% | -0.40% | 15,063 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 91.79% | 93.17% | -1.49% | 2,532 |  |
| Apple Pay | 87.14% | 87.56% | -0.48% | 2,301 |  |
| Credit Card | 89.77% | 89.9% | -0.14% | 10,229 |  |
| Others | 100.0% | 50.0% | +100.00% | 1 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 18,897 | 15,063 | -20.3% | ⚠️ Volume drop |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-27*
