# AR Overall Investigation: US-HF 2026-W15

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 92.22% → 92.1% (-0.13%)  
**Volume:** 421,947 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate for US-HF declined marginally from 92.22% to 92.1% (-0.12pp) in 2026-W15, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within normal range | +0.44pp | ✅ |
| 2_PreDunningAR | Within normal range | +0.32pp | ✅ |
| 3_PostDunningAR | Within normal range | +0.02pp | ✅ |
| 6_PaymentApprovalRate | Within normal range | +0.14pp | ✅ |

**Key Findings:**
- The -0.13% week-over-week change is within normal fluctuation; the 8-week trend shows rates oscillating between 91.65% and 92.22%, indicating stable performance
- No countries exceeded the ±2.5% threshold; US remains the sole market at 93.09% (+0.33pp), performing above the overall rate
- PaymentProvider "Unknown" showed a +5.33pp spike (87.1% → 91.74%) but with minimal volume (351 orders), flagged as ⚠️ but low impact
- Apple Pay continues to have the lowest acceptance rate among payment methods at 85.13%, though it improved +0.67pp week-over-week
- Mix shift analysis shows stable composition with US High AR tier volume declining only 0.9%

**Action:** Monitor - No immediate action required. The decline is not significant and all funnel metrics are improving week-over-week. Continue standard monitoring cadence.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 92.1% | 421,947 | -0.13% |
| 2026-W15 | 92.22% | 408,629 | +0.32% ← REPORTED CHANGE |
| 2026-W14 | 91.93% | 415,885 | -0.05% |
| 2026-W13 | 91.98% | 424,103 | +0.05% |
| 2026-W12 | 91.93% | 433,761 | -0.17% |
| 2026-W11 | 92.09% | 444,619 | +0.14% |
| 2026-W10 | 91.96% | 457,610 | +0.34% |
| 2026-W09 | 91.65% | 455,121 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 93.09% | 92.78% | +0.33% | 492,811 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 98.37% | 98.41% | -0.04% | 2,395 |  |
| Credit Card | 92.92% | 92.69% | +0.25% | 300,598 |  |
| Paypal | 95.57% | 95.34% | +0.25% | 50,099 |  |
| Apple Pay | 85.13% | 84.56% | +0.67% | 55,537 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Adyen | 95.04% | 95.05% | -0.02% | 383 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 2,010 |  |
| Braintree | 92.75% | 92.44% | +0.34% | 363,787 |  |
| ProcessOut | 87.24% | 86.9% | +0.40% | 42,098 |  |
| Unknown | 91.74% | 87.1% | +5.33% | 351 | ⚠️ |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.07% | 90.67% | +0.44% | 408,629 | 415,885 |  |
| 2_PreDunningAR | 92.22% | 91.93% | +0.32% | 408,629 | 415,885 |  |
| 3_PostDunningAR | 93.19% | 93.17% | +0.02% | 408,629 | 415,885 |  |
| 6_PaymentApprovalRate | 93.76% | 93.63% | +0.14% | 408,629 | 415,885 |  |

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

*Report: 2026-04-22*
