# AR Initial (LL0) Investigation: HF-NA 2026-W20

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 89.72% → 88.94% (-0.87%)  
**Volume:** 15,024 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) declined by -0.78 pp (89.72% → 88.94%) week-over-week, a change that is not statistically significant and remains within the normal 8-week fluctuation range (89.31%-90.11%).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.70% | ⚠️ |
| 2_PreDunningAR | Reported Metric | -0.88% | ⚠️ |
| 3_PostDunningAR | Recovery | -0.78% | ⚠️ |
| 6_PaymentApprovalRate | Final Approval | -0.32% | ✅ |

**Key Findings:**
- PayPal payment method shows the largest decline at -3.81 pp (89.52% → 86.11%) with 1,231 orders, flagged as the only dimension exceeding threshold
- Braintree provider declined -2.07 pp (87.45% → 85.64%) on 6,060 orders, approaching but not exceeding the ±2.5% threshold
- CA volume decreased -8.4% (4,702 → 4,309 orders) while maintaining higher acceptance (92.25%) compared to US (87.61%)
- Decline is consistent across the entire funnel (FirstRunAR through PostDunningAR), suggesting an upstream issue rather than dunning-specific
- No country exceeded the ±2.5% threshold; both US (-0.72%) and CA (-0.90%) showed modest declines

**Action:** Monitor - The overall change is not statistically significant. Continue tracking PayPal performance over the next 1-2 weeks to determine if the -3.81 pp decline represents a developing trend or normal volatility.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W20 | 88.94% | 15,024 | -0.87% ← REPORTED CHANGE |
| 2026-W19 | 89.72% | 15,338 | +0.40% |
| 2026-W18 | 89.36% | 15,785 | -0.83% |
| 2026-W17 | 90.11% | 18,003 | +0.74% |
| 2026-W16 | 89.45% | 18,010 | -0.64% |
| 2026-W15 | 90.03% | 15,988 | +0.33% |
| 2026-W14 | 89.73% | 17,040 | +0.47% |
| 2026-W13 | 89.31% | 16,124 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 92.25% | 93.09% | -0.90% | 4,309 |  |
| US | 87.61% | 88.24% | -0.72% | 10,715 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 86.11% | 89.52% | -3.81% | 1,231 | ⚠️ |
| Apple Pay | 85.63% | 86.99% | -1.57% | 4,682 |  |
| Credit Card | 90.71% | 91.07% | -0.40% | 8,295 |  |
| Others | 94.24% | 92.71% | +1.66% | 816 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Braintree | 85.64% | 87.45% | -2.07% | 6,060 |  |
| ProcessOut | 90.91% | 91.15% | -0.26% | 7,901 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 110 |  |
| Adyen | 95.41% | 94.93% | +0.51% | 676 |  |
| Unknown | 84.48% | 83.07% | +1.69% | 277 |  |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 87.91% | 88.53% | -0.70% | 15,024 | 15,338 |  |
| 2_PreDunningAR | 88.94% | 89.72% | -0.88% | 15,024 | 15,338 |  |
| 3_PostDunningAR | 89.22% | 89.93% | -0.78% | 15,024 | 15,338 |  |
| 6_PaymentApprovalRate | 89.8% | 90.09% | -0.32% | 15,024 | 15,338 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 10,636 | 10,715 | +0.7% | Stable |
| CA | High (>92%) | 4,702 | 4,309 | -8.4% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-19*
