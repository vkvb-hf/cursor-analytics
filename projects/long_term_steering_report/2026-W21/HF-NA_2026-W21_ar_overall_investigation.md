# AR Overall Investigation: HF-NA 2026-W21

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 92.15% → 91.84% (-0.34%)  
**Volume:** 468,983 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate declined by -0.34pp (92.15% → 91.84%) on 468,983 orders in 2026-W21, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.30pp | ✅ |
| 2_PreDunningAR | Reported Metric | -0.33pp | ✅ |
| 3_PostDunningAR | Post-Dunning Recovery | -0.42pp | ✅ |
| 6_PaymentApprovalRate | Final Approval | -0.24pp | ✅ |

**Key Findings:**
- All funnel stages show minor declines between -0.24pp and -0.42pp, indicating a broad but shallow decline rather than a localized issue
- PaymentProvider "Unknown" flagged with -5.23pp decline (65.39% → 61.97%), though volume is minimal at only 497 orders
- Both US (-0.23pp) and CA (-0.28pp) declined modestly, with neither exceeding the ±2.5% investigation threshold
- Apple Pay shows the lowest acceptance rate at 85.54% (-0.86pp), underperforming other payment methods
- 8-week trend shows a gradual downward drift from 92.39% (W15) to 91.84% (W21), representing a cumulative -0.55pp decline

**Action:** Monitor — The decline is not statistically significant, no country or major dimension exceeded thresholds, and the flagged "Unknown" provider represents negligible volume (<0.1% of orders).

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W21 | 91.84% | 468,983 | -0.34% ← REPORTED CHANGE |
| 2026-W20 | 92.15% | 487,754 | +0.17% |
| 2026-W19 | 91.99% | 508,007 | -0.12% |
| 2026-W18 | 92.1% | 506,464 | -0.09% |
| 2026-W17 | 92.18% | 510,064 | -0.12% |
| 2026-W16 | 92.29% | 513,373 | -0.11% |
| 2026-W15 | 92.39% | 497,777 | +0.27% |
| 2026-W14 | 92.14% | 507,190 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 93.54% | 93.80% | -0.28% | 95,083 |  |
| US | 92.71% | 92.92% | -0.23% | 478,645 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 95.05% | 96.22% | -1.22% | 4,037 |  |
| Apple Pay | 85.54% | 86.29% | -0.86% | 62,360 |  |
| Credit Card | 92.33% | 92.56% | -0.25% | 345,860 |  |
| Paypal | 95.52% | 95.74% | -0.24% | 56,726 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 61.97% | 65.39% | -5.23% | 497 | ⚠️ |
| ProcessOut | 89.28% | 89.69% | -0.46% | 95,728 |  |
| Braintree | 92.41% | 92.68% | -0.29% | 345,910 |  |
| Adyen | 93.42% | 93.58% | -0.18% | 23,757 |  |
| No Payment | 99.97% | 100.0% | -0.03% | 3,091 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.69% | 90.96% | -0.30% | 468,983 | 487,754 |  |
| 2_PreDunningAR | 91.84% | 92.15% | -0.33% | 468,983 | 487,754 |  |
| 3_PostDunningAR | 92.83% | 93.22% | -0.42% | 468,983 | 487,754 |  |
| 6_PaymentApprovalRate | 93.64% | 93.87% | -0.24% | 468,983 | 487,754 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 493,780 | 478,645 | -3.1% | Stable |
| CA | High (>92%) | 99,511 | 95,083 | -4.4% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-26*
