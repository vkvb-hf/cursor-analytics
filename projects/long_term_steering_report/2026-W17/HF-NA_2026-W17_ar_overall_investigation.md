# AR Overall Investigation: HF-NA 2026-W17

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 92.31% → 92.19% (-0.13%)  
**Volume:** 510,064 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate declined slightly from 92.31% to 92.19% (-0.12pp) in W17, a change that is not statistically significant and remains within normal weekly fluctuation range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.10pp | ✅ |
| 2_PreDunningAR | Reported Metric | -0.13pp | ✅ |
| 3_PostDunningAR | Post-Dunning | -0.27pp | ✅ |
| 6_PaymentApprovalRate | Final Approval | -0.11pp | ✅ |

**Key Findings:**
- All funnel metrics showed minor declines (0.10-0.27pp), with PostDunningAR showing the largest drop at -0.27pp, indicating dunning recovery was slightly less effective this week
- CA experienced a -0.47pp decline (93.58% → 93.13%) while US remained essentially flat (+0.02pp), though neither exceeded the ±2.5% threshold
- "Others" payment method showed the largest decline at -1.05pp (91.36% → 90.4%) with 105K volume, and "Unknown" provider mirrored this with -1.05pp decline
- 8-week trend shows the metric oscillating in a narrow band between 92.0% and 92.41%, with W17 at 92.19% remaining within historical norms
- Mix shift analysis shows stable volume distribution between US and CA with minimal movement (-0.6% and -0.3% respectively)

**Action:** Monitor — The decline is not significant and all metrics remain within normal operating ranges. Continue standard weekly monitoring with attention to CA performance and "Others/Unknown" payment category trends.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 92.19% | 510,064 | -0.13% ← REPORTED CHANGE |
| 2026-W16 | 92.31% | 513,372 | -0.11% |
| 2026-W15 | 92.41% | 497,776 | +0.27% |
| 2026-W14 | 92.16% | 507,189 | -0.07% |
| 2026-W13 | 92.22% | 517,599 | +0.10% |
| 2026-W12 | 92.13% | 526,516 | -0.15% |
| 2026-W11 | 92.27% | 539,763 | +0.29% |
| 2026-W10 | 92.0% | 554,777 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 93.13% | 93.58% | -0.47% | 104,317 |  |
| US | 92.99% | 92.97% | +0.02% | 508,019 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 90.4% | 91.36% | -1.05% | 105,192 |  |
| Paypal | 95.78% | 95.69% | +0.09% | 62,032 |  |
| Apple Pay | 86.58% | 86.44% | +0.16% | 69,057 |  |
| Credit Card | 93.48% | 93.26% | +0.23% | 273,783 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 88.38% | +nan% | 0 |  |
| Unknown | 90.05% | 91.01% | -1.05% | 101,371 |  |
| Adyen | 92.01% | 92.47% | -0.50% | 25,715 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 3,500 |  |
| Braintree | 92.7% | 92.65% | +0.06% | 379,478 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.96% | 91.06% | -0.10% | 510,064 | 513,372 |  |
| 2_PreDunningAR | 92.19% | 92.31% | -0.13% | 510,064 | 513,372 |  |
| 3_PostDunningAR | 93.13% | 93.38% | -0.27% | 510,064 | 513,372 |  |
| 6_PaymentApprovalRate | 94.03% | 94.13% | -0.11% | 510,064 | 513,372 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 511,272 | 508,019 | -0.6% | Stable |
| CA | High (>92%) | 104,640 | 104,317 | -0.3% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-28*
