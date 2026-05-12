# PAR Investigation: WL 2026-W19

**Metric:** Payment Approval Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 91.24% → 91.27% (+0.03%)  
**Volume:** 165,009 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate remained essentially stable at 91.27%, showing a minimal +0.03pp increase week-over-week, which is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within normal range | +0.11pp | ✅ |
| 2_PreDunningAR | Within normal range | +0.08pp | ✅ |
| 3_PostDunningAR | Within normal range | -0.18pp | ✅ |
| 6_PaymentApprovalRate | Within normal range | +0.04pp | ✅ |

**Key Findings:**
- The +0.03pp change in PAR is well within normal weekly fluctuation; the 8-week trend shows the metric oscillating between 91.04% and 91.68%
- No countries exceeded the ±2.5% threshold; MR showed the largest positive movement at +2.06pp (82.28%) while ER declined -0.57pp (90.41%)
- All payment methods and providers showed minimal changes (<1.5pp), with no flags triggered
- Volume decreased slightly from 166,895 to 165,009 orders (-1.1%), with notable volume drops in MR (-5.9%) and GN (-4.8%)
- Mix shift analysis indicates stable composition across all AR tiers with no material impact on the overall rate

**Action:** Monitor — No investigation required. The change is not significant and all dimensions remain within normal operating ranges.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W19 | 91.27% | 165,009 | +0.03% ← REPORTED CHANGE |
| 2026-W18 | 91.24% | 166,895 | -0.47% |
| 2026-W17 | 91.67% | 166,258 | -0.01% |
| 2026-W16 | 91.68% | 164,785 | +0.03% |
| 2026-W15 | 91.65% | 160,979 | +0.67% |
| 2026-W14 | 91.04% | 165,018 | -0.28% |
| 2026-W13 | 91.3% | 169,667 | -0.02% |
| 2026-W12 | 91.32% | 169,891 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| ER | 90.41% | 90.93% | -0.57% | 67,441 |  |
| CG | 97.07% | 97.19% | -0.12% | 44,290 |  |
| GN | 96.17% | 95.87% | +0.32% | 14,255 |  |
| KN | 89.51% | 87.89% | +1.84% | 11,044 |  |
| MR | 82.28% | 80.62% | +2.06% | 20,895 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 87.45% | 87.71% | -0.30% | 21,025 |  |
| Paypal | 95.61% | 95.71% | -0.10% | 24,685 |  |
| Credit Card | 90.91% | 90.81% | +0.11% | 117,311 |  |
| Others | 99.3% | 98.63% | +0.68% | 1,988 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | 82.23% | 82.43% | -0.24% | 17,601 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 675 |  |
| Adyen | 94.04% | 93.99% | +0.05% | 38,474 |  |
| Braintree | 91.62% | 91.57% | +0.05% | 107,009 |  |
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
| AO | High (>92%) | 15,590 | 15,233 | -2.3% | Stable |
| GN | High (>92%) | 14,971 | 14,255 | -4.8% | Stable |
| KN | Medium (>85%) | 11,123 | 11,044 | -0.7% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-12*
