# AR Overall Investigation: US-HF 2026-W23

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 91.27% → 91.63% (+0.39%)  
**Volume:** 377,552 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** The Pre-Dunning Acceptance Rate for US-HF improved slightly from 91.27% to 91.63% (+0.36 pp) in 2026-W23, representing a partial recovery from the prior week's decline but remaining below the 8-week high of 92.09% observed in W16.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within normal range | +0.40% | ✅ |
| 2_PreDunningAR | Within normal range | +0.39% | ✅ |
| 3_PostDunningAR | Within normal range | +0.15% | ✅ |
| 6_PaymentApprovalRate | Within normal range | +0.30% | ✅ |

**Key Findings:**
- All payment funnel metrics showed modest improvement week-over-week, with FirstRunAR leading at +0.40 pp, suggesting upstream acceptance gains drove the overall improvement
- No countries or dimensions exceeded the ±2.5% threshold; US showed a +0.31 pp improvement on 464,277 orders
- Apple Pay continues to underperform other payment methods at 84.68% acceptance rate vs. Credit Card at 92.24% and PayPal at 95.59%
- The "Unknown" PaymentProvider segment shows a concerning 43.14% acceptance rate but represents minimal volume (306 orders)
- Volume declined 10.5% from 8-week high (421,998 in W16 to 377,552 in W23), though mix remains stable in the High AR tier

**Action:** Monitor – The change is not statistically significant and all segments are within normal thresholds. Continue standard monitoring cadence.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W23 | 91.63% | 377,552 | +0.39% ← REPORTED CHANGE |
| 2026-W22 | 91.27% | 368,727 | -0.34% |
| 2026-W21 | 91.58% | 386,946 | -0.34% |
| 2026-W20 | 91.89% | 401,810 | +0.12% |
| 2026-W19 | 91.78% | 416,769 | -0.13% |
| 2026-W18 | 91.9% | 414,970 | -0.18% |
| 2026-W17 | 92.07% | 419,158 | -0.02% |
| 2026-W16 | 92.09% | 421,998 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.70% | 92.41% | +0.31% | 464,277 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 95.59% | 95.48% | +0.12% | 45,508 |  |
| Credit Card | 92.24% | 91.91% | +0.36% | 279,316 |  |
| Others | 91.77% | 91.24% | +0.58% | 2,176 |  |
| Apple Pay | 84.68% | 84.07% | +0.72% | 50,552 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 43.14% | 43.87% | -1.66% | 306 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 1,744 |  |
| ProcessOut | 86.43% | 86.32% | +0.14% | 58,555 |  |
| Braintree | 92.58% | 92.18% | +0.44% | 316,484 |  |
| Adyen | 95.25% | 94.63% | +0.66% | 463 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.46% | 90.1% | +0.40% | 377,552 | 368,727 |  |
| 2_PreDunningAR | 91.63% | 91.27% | +0.39% | 377,552 | 368,727 |  |
| 3_PostDunningAR | 92.43% | 92.29% | +0.15% | 377,552 | 368,727 |  |
| 6_PaymentApprovalRate | 93.19% | 92.92% | +0.30% | 377,552 | 368,727 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 455,576 | 464,277 | +1.9% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-09*
