# AR Overall Investigation: US-HF 2026-W17

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 92.1% → 92.07% (-0.03%)  
**Volume:** 419,106 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate for US-HF remained essentially stable in 2026-W17, declining marginally by -0.03pp (92.10% → 92.07%) on volume of 419,106 orders—a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within normal range | +0.06pp | ✅ |
| 2_PreDunningAR | Within normal range | -0.03pp | ✅ |
| 3_PostDunningAR | Within normal range | -0.17pp | ✅ |
| 6_PaymentApprovalRate | Within normal range | -0.02pp | ✅ |

**Key Findings:**
- The -0.03pp decline in Pre-Dunning AR is within normal weekly fluctuation; the 8-week trend shows rates oscillating between 91.92% and 92.22% with no clear directional pattern
- No payment methods or providers exceeded the ±2.5% threshold; the largest movement was "Others" payment method declining -0.86pp (89.39% → 88.63%) on 61,124 orders
- US country-level performance showed a slight improvement of +0.02pp (92.97% → 92.99%)
- ProcessOut provider shows no current volume (0 orders) compared to prior week activity, though this represents minimal overall impact
- Post-Dunning AR showed the largest funnel decline at -0.17pp, but remains within acceptable bounds at 92.92%

**Action:** Monitor — No immediate action required. The change is not significant and all dimensions remain within normal thresholds. Continue standard weekly monitoring.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 92.07% | 419,106 | -0.03% ← REPORTED CHANGE |
| 2026-W16 | 92.1% | 421,947 | -0.13% |
| 2026-W15 | 92.22% | 408,630 | +0.33% |
| 2026-W14 | 91.92% | 415,885 | -0.07% |
| 2026-W13 | 91.98% | 424,103 | +0.05% |
| 2026-W12 | 91.93% | 433,761 | -0.17% |
| 2026-W11 | 92.09% | 444,619 | +0.14% |
| 2026-W10 | 91.96% | 457,610 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.99% | 92.97% | +0.02% | 508,019 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 88.63% | 89.39% | -0.86% | 61,124 |  |
| Paypal | 95.94% | 95.77% | +0.17% | 51,246 |  |
| Credit Card | 93.63% | 93.36% | +0.29% | 248,708 |  |
| Apple Pay | 85.6% | 85.34% | +0.30% | 58,028 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 87.79% | +nan% | 0 |  |
| Unknown | 88.24% | 88.95% | -0.79% | 59,076 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 1,977 |  |
| Braintree | 92.66% | 92.58% | +0.08% | 357,625 |  |
| Adyen | 94.86% | 94.31% | +0.59% | 428 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.84% | 90.79% | +0.06% | 419,106 | 421,947 |  |
| 2_PreDunningAR | 92.07% | 92.1% | -0.03% | 419,106 | 421,947 |  |
| 3_PostDunningAR | 92.92% | 93.08% | -0.17% | 419,106 | 421,947 |  |
| 6_PaymentApprovalRate | 93.8% | 93.82% | -0.02% | 419,106 | 421,947 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 511,272 | 508,019 | -0.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-28*
