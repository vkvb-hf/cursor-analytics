# AR Overall Investigation: HF-NA 2026-W22

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 91.84% → 91.72% (-0.13%)  
**Volume:** 452,722 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate declined slightly from 91.84% to 91.72% (-0.13pp) in W22, a change that is not statistically significant, continuing a gradual downward trend observed over the 8-week period.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.28pp | ⚠️ |
| 2_PreDunningAR | Reported Metric | -0.13pp | ✅ |
| 3_PostDunningAR | Post-Recovery | -0.40pp | ⚠️ |
| 6_PaymentApprovalRate | Final Approval | -0.22pp | ✅ |

**Key Findings:**
- All funnel stages show minor declines this week, with PostDunningAR showing the largest drop (-0.40pp), suggesting dunning recovery effectiveness decreased
- PaymentProvider "Unknown" flagged with significant decline (-10.01pp), though volume is minimal (482 orders) and unlikely to impact overall performance
- US showed a -0.32pp decline while CA improved by +0.51pp, but neither country exceeded the ±2.5% threshold requiring investigation
- 8-week trend shows consistent gradual erosion from 92.39% (W15) to 91.72% (W22), representing a cumulative decline of -0.67pp
- No payment method exceeded threshold; all changes were within normal operational variance (largest: "Others" at -0.65pp on 4,015 volume)

**Action:** Monitor — The week-over-week change is not significant and no dimensions exceeded investigation thresholds. However, the persistent 8-week declining trend warrants continued observation; if the rate drops below 91.5% or the trend continues for 2+ additional weeks, escalate for deeper analysis.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W22 | 91.72% | 452,722 | -0.13% ← REPORTED CHANGE |
| 2026-W21 | 91.84% | 468,983 | -0.33% |
| 2026-W20 | 92.14% | 487,754 | +0.16% |
| 2026-W19 | 91.99% | 508,009 | -0.12% |
| 2026-W18 | 92.1% | 506,464 | -0.09% |
| 2026-W17 | 92.18% | 510,064 | -0.12% |
| 2026-W16 | 92.29% | 513,373 | -0.11% |
| 2026-W15 | 92.39% | 497,777 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.42% | 92.71% | -0.32% | 455,505 |  |
| CA | 94.02% | 93.54% | +0.51% | 97,516 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 94.47% | 95.09% | -0.65% | 4,015 |  |
| Paypal | 95.25% | 95.52% | -0.28% | 54,714 |  |
| Apple Pay | 85.43% | 85.54% | -0.12% | 60,250 |  |
| Credit Card | 92.24% | 92.33% | -0.10% | 333,743 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 55.39% | 61.55% | -10.01% | 482 | ⚠️ |
| Braintree | 92.24% | 92.41% | -0.18% | 329,966 |  |
| ProcessOut | 89.18% | 89.28% | -0.10% | 94,707 |  |
| No Payment | 100.0% | 99.97% | +0.03% | 3,120 |  |
| Adyen | 94.13% | 93.42% | +0.76% | 24,447 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.44% | 90.69% | -0.28% | 452,722 | 468,983 |  |
| 2_PreDunningAR | 91.72% | 91.84% | -0.13% | 452,722 | 468,983 |  |
| 3_PostDunningAR | 92.52% | 92.9% | -0.40% | 452,722 | 468,983 |  |
| 6_PaymentApprovalRate | 93.43% | 93.64% | -0.22% | 452,722 | 468,983 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 478,645 | 455,505 | -4.8% | Stable |
| CA | High (>92%) | 95,083 | 97,516 | +2.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-02*
