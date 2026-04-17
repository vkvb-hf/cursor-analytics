# AR Overall Investigation: US-HF 2026-W15

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 91.93% → 92.22% (+0.32%)  
**Volume:** 408,629 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate for US-HF improved slightly from 91.93% to 92.22% (+0.29 pp) in W15, a non-significant change within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | +0.44 pp | ✅ |
| 2_PreDunningAR | Reported Metric | +0.32 pp | ✅ |
| 3_PostDunningAR | Post-Recovery | +0.02 pp | ✅ |
| 6_PaymentApprovalRate | Final Approval | +0.14 pp | ✅ |

**Key Findings:**
- All funnel metrics showed slight positive movement, with FirstRunAR leading the improvement at +0.44 pp
- No countries exceeded the ±2.5% investigation threshold; US showed stable performance at 93.09% (+0.34 pp)
- Payment Provider "Unknown" flagged with +4.73 pp change, but volume is minimal (353 orders, <0.1% of total)
- Volume continues gradual decline trend: 408,629 orders in W15 vs 453,781 in W08 (-9.9% over 8 weeks)
- 8-week trend shows stable acceptance rate oscillating between 91.48% and 92.22%, indicating consistent system performance

**Action:** Monitor — No investigation required. The change is not statistically significant, all dimensions are within thresholds, and the metric remains stable within historical range.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 92.22% | 408,629 | +0.32% ← REPORTED CHANGE |
| 2026-W14 | 91.93% | 415,885 | -0.05% |
| 2026-W13 | 91.98% | 424,103 | +0.05% |
| 2026-W12 | 91.93% | 433,761 | -0.17% |
| 2026-W11 | 92.09% | 444,619 | +0.14% |
| 2026-W10 | 91.96% | 457,610 | +0.34% |
| 2026-W09 | 91.65% | 455,121 | +0.19% |
| 2026-W08 | 91.48% | 453,781 | - |

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
| Others | 98.29% | 98.41% | -0.12% | 2,397 |  |
| Credit Card | 92.92% | 92.69% | +0.25% | 300,596 |  |
| Paypal | 95.58% | 95.34% | +0.25% | 50,099 |  |
| Apple Pay | 85.13% | 84.57% | +0.67% | 55,537 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Adyen | 95.04% | 95.05% | -0.02% | 383 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 2,010 |  |
| Braintree | 92.75% | 92.44% | +0.34% | 363,785 |  |
| ProcessOut | 87.24% | 86.9% | +0.40% | 42,098 |  |
| Unknown | 91.22% | 87.1% | +4.73% | 353 | ⚠️ |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.07% | 90.67% | +0.44% | 408,629 | 415,885 |  |
| 2_PreDunningAR | 92.22% | 91.93% | +0.32% | 408,629 | 415,885 |  |
| 3_PostDunningAR | 93.0% | 92.98% | +0.02% | 408,629 | 415,885 |  |
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

*Report: 2026-04-17*
