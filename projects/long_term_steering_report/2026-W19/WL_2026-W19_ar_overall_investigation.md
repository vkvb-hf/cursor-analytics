# AR Overall Investigation: WL 2026-W19

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 89.6% → 89.67% (+0.08%)  
**Volume:** 165,009 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate showed a marginal improvement of +0.08pp (89.6% → 89.67%) on volume of 165,009 orders, which is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within normal range | +0.11pp | ✅ |
| 2_PreDunningAR | Within normal range | +0.08pp | ✅ |
| 3_PostDunningAR | Slight decline | -0.18pp | ⚠️ |
| 6_PaymentApprovalRate | Within normal range | +0.04pp | ✅ |

**Key Findings:**
- No countries exceeded the ±2.5% threshold; all country-level changes are within normal operating variance
- MR showed the largest positive movement at +2.10pp (80.33% → 82.01%), though it remains the lowest-performing country at 82.01%
- KN improved by +1.87pp (86.87% → 88.49%), representing the second-largest positive shift
- PostDunningAR declined by -0.18pp, the only funnel step showing deterioration, suggesting dunning recovery effectiveness may warrant monitoring
- All payment methods and providers remained stable with no significant deviations (largest change: Unknown provider at +1.40pp on minimal volume of 1,250)

**Action:** Monitor - No action required. The change is not significant and all dimensions are within normal thresholds. Continue standard monitoring cadence.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W19 | 89.67% | 165,009 | +0.08% ← REPORTED CHANGE |
| 2026-W18 | 89.6% | 166,895 | -0.54% |
| 2026-W17 | 90.09% | 166,258 | +0.09% |
| 2026-W16 | 90.01% | 164,785 | -0.09% |
| 2026-W15 | 90.09% | 160,979 | +0.86% |
| 2026-W14 | 89.32% | 165,018 | -0.43% |
| 2026-W13 | 89.71% | 169,667 | +0.07% |
| 2026-W12 | 89.65% | 169,891 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| AO | 87.91% | 88.72% | -0.90% | 15,233 |  |
| ER | 89.34% | 89.71% | -0.41% | 67,441 |  |
| GN | 94.92% | 94.09% | +0.88% | 14,255 |  |
| KN | 88.49% | 86.87% | +1.87% | 11,044 |  |
| MR | 82.01% | 80.33% | +2.10% | 20,895 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 86.06% | 86.36% | -0.34% | 21,025 |  |
| Paypal | 94.8% | 94.87% | -0.07% | 24,685 |  |
| Credit Card | 89.08% | 88.94% | +0.16% | 117,311 |  |
| Others | 99.3% | 98.4% | +0.91% | 1,988 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 675 |  |
| Adyen | 90.32% | 90.31% | +0.01% | 38,474 |  |
| ProcessOut | 81.18% | 81.16% | +0.02% | 17,601 |  |
| Braintree | 90.66% | 90.57% | +0.10% | 107,009 |  |
| Unknown | 99.12% | 97.75% | +1.40% | 1,250 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 87.66% | 87.56% | +0.11% | 165,009 | 166,895 |  |
| 2_PreDunningAR | 89.67% | 89.6% | +0.08% | 165,009 | 166,895 |  |
| 3_PostDunningAR | 90.65% | 90.81% | -0.18% | 165,009 | 166,895 |  |
| 6_PaymentApprovalRate | 91.27% | 91.24% | +0.04% | 165,009 | 166,895 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 68,051 | 67,441 | -0.9% | Stable |
| CG | High (>92%) | 43,448 | 44,290 | +1.9% | Stable |
| CK | High (>92%) | 41,405 | 41,704 | +0.7% | Stable |
| MR | Low (>85%) | 22,211 | 20,895 | -5.9% | Stable |
| AO | Medium (>85%) | 15,590 | 15,233 | -2.3% | Stable |
| GN | High (>92%) | 14,971 | 14,255 | -4.8% | Stable |
| KN | Medium (>85%) | 11,123 | 11,044 | -0.7% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-12*
