# AR Overall Investigation: US-HF 2026-W16

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 92.22% → 92.1% (-0.13%)  
**Volume:** 421,947 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate declined modestly from 92.22% to 92.1% (-0.12pp) on volume of 421,947 orders, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.31pp | ⚠️ |
| 2_PreDunningAR | Reported Metric | -0.12pp | ✅ |
| 3_PostDunningAR | Post-Dunning | -0.17pp | ✅ |
| 6_PaymentApprovalRate | Final Approval | +0.07pp | ✅ |

**Key Findings:**
- The -0.12pp decline in Pre-Dunning AR falls within normal weekly fluctuation (8-week range: 91.65% to 92.22%)
- PaymentProvider "Unknown" shows a significant -10.77pp drop (91.74% → 81.86%), but volume is minimal at only 226 orders
- Credit Card payments declined -0.25pp while representing the largest volume (310,172 orders), contributing most to the overall decline
- No countries exceeded the ±2.5% threshold; US is the sole market at -0.13pp
- FirstRunAR shows the largest funnel decline at -0.31pp, suggesting initial payment attempts are the primary pressure point

**Action:** Monitor — The decline is not significant and within normal variance. Continue tracking Unknown PaymentProvider performance despite low volume, and watch FirstRunAR trends for potential upstream issues.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 92.1% | 421,947 | -0.13% ← REPORTED CHANGE |
| 2026-W15 | 92.22% | 408,629 | +0.32% |
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
| US | 92.97% | 93.09% | -0.13% | 511,272 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 97.94% | 98.37% | -0.44% | 2,284 |  |
| Credit Card | 92.69% | 92.92% | -0.25% | 310,172 |  |
| Paypal | 95.79% | 95.57% | +0.22% | 51,881 |  |
| Apple Pay | 85.36% | 85.13% | +0.27% | 57,610 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 81.86% | 91.74% | -10.77% | 226 | ⚠️ |
| Adyen | 94.54% | 95.04% | -0.52% | 403 |  |
| Braintree | 92.66% | 92.75% | -0.10% | 361,379 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 2,028 |  |
| ProcessOut | 88.36% | 87.24% | +1.28% | 57,911 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.79% | 91.07% | -0.31% | 421,947 | 408,629 |  |
| 2_PreDunningAR | 92.1% | 92.22% | -0.13% | 421,947 | 408,629 |  |
| 3_PostDunningAR | 93.03% | 93.19% | -0.17% | 421,947 | 408,629 |  |
| 6_PaymentApprovalRate | 93.82% | 93.76% | +0.07% | 421,947 | 408,629 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 492,811 | 511,272 | +3.7% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
