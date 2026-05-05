# PAR Investigation: US-HF 2026-W18

**Metric:** Payment Approval Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 93.79% → 93.62% (-0.18%)  
**Volume:** 414,919 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate declined slightly from 93.79% to 93.62% (-0.17pp) in W18, a change that is not statistically significant and remains within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within range | -0.21pp | ✅ |
| 2_PreDunningAR | Within range | -0.18pp | ✅ |
| 3_PostDunningAR | Within range | -0.23pp | ✅ |
| 6_PaymentApprovalRate | Within range | -0.18pp | ✅ |

**Key Findings:**
- The -0.17pp decline is not statistically significant and the current rate (93.62%) matches the rate observed in W14, indicating normal fluctuation
- No countries exceeded the ±2.5% threshold; US showed minimal movement at -0.04pp
- "Others" payment method showed the largest decline (-0.60pp) though still within tolerance, followed by "Unknown" provider (-0.61pp)
- All funnel stages show parallel small declines (-0.18pp to -0.23pp), suggesting no specific funnel bottleneck
- Volume decreased slightly from 419,106 to 414,919 orders (-1.0%), consistent with an 8-week downward volume trend

**Action:** Monitor — No immediate action required. The decline is within normal variance and the metric remains stable within the 8-week historical range (93.54%-93.82%).

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W18 | 93.62% | 414,919 | -0.18% ← REPORTED CHANGE |
| 2026-W17 | 93.79% | 419,106 | -0.03% |
| 2026-W16 | 93.82% | 421,947 | +0.07% |
| 2026-W15 | 93.75% | 408,630 | +0.14% |
| 2026-W14 | 93.62% | 415,885 | +0.04% |
| 2026-W13 | 93.58% | 424,103 | +0.04% |
| 2026-W12 | 93.54% | 433,761 | -0.04% |
| 2026-W11 | 93.58% | 444,619 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 94.57% | 94.61% | -0.04% | 516,129 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 90.22% | 90.77% | -0.60% | 61,326 |  |
| Apple Pay | 87.94% | 88.15% | -0.24% | 56,761 |  |
| Credit Card | 95.14% | 95.27% | -0.13% | 246,004 |  |
| Paypal | 96.69% | 96.6% | +0.09% | 50,828 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | nan% | +nan% | 0 |  |
| Unknown | 89.9% | 90.45% | -0.61% | 59,345 |  |
| Braintree | 94.2% | 94.3% | -0.11% | 353,188 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 1,950 |  |
| Adyen | 96.79% | 96.26% | +0.55% | 436 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.65% | 90.84% | -0.21% | 414,919 | 419,106 |  |
| 2_PreDunningAR | 91.91% | 92.07% | -0.18% | 414,919 | 419,106 |  |
| 3_PostDunningAR | 92.95% | 93.16% | -0.23% | 414,919 | 419,106 |  |
| 6_PaymentApprovalRate | 93.62% | 93.79% | -0.18% | 414,919 | 419,106 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 508,019 | 516,129 | +1.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-05*
