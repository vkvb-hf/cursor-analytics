# PAR Investigation: WL 2026-W20

**Metric:** Payment Approval Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 91.27% → 91.31% (+0.04%)  
**Volume:** 159,098 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate showed a marginal improvement from 91.27% to 91.31% (+0.04pp) on volume of 159,098 orders, which is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within normal range | +0.19pp | ✅ |
| 2_PreDunningAR | Within normal range | -0.01pp | ✅ |
| 3_PostDunningAR | Within normal range | -0.10pp | ✅ |
| 6_PaymentApprovalRate | Within normal range | +0.05pp | ✅ |

**Key Findings:**
- The +0.04pp change is well within normal weekly fluctuation; 8-week trend shows stable performance ranging from 91.04% to 91.68%
- KN showed the largest country-level decline at -1.95pp (89.51% → 87.76%), but remains below the ±2.5% threshold requiring investigation
- ProcessOut showed notable improvement of +1.44pp (82.22% → 83.40%) though still trails other payment providers significantly
- No countries or dimensions exceeded threshold flags; all segments showing stable performance
- Volume decreased slightly week-over-week (165,009 → 159,098, -3.6%) but mix shift analysis indicates stable tier distribution

**Action:** Monitor — No action required. Continue standard monitoring cadence.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W20 | 91.31% | 159,098 | +0.04% ← REPORTED CHANGE |
| 2026-W19 | 91.27% | 165,009 | +0.03% |
| 2026-W18 | 91.24% | 166,895 | -0.47% |
| 2026-W17 | 91.67% | 166,258 | -0.01% |
| 2026-W16 | 91.68% | 164,785 | +0.03% |
| 2026-W15 | 91.65% | 160,979 | +0.67% |
| 2026-W14 | 91.04% | 165,018 | -0.28% |
| 2026-W13 | 91.3% | 169,667 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| KN | 87.76% | 89.51% | -1.95% | 11,084 |  |
| CK | 95.34% | 95.15% | +0.20% | 40,466 |  |
| AO | 94.36% | 94.07% | +0.31% | 14,758 |  |
| GN | 96.52% | 96.16% | +0.37% | 15,192 |  |
| ER | 90.98% | 90.41% | +0.63% | 66,405 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 95.43% | 95.61% | -0.19% | 23,738 |  |
| Credit Card | 90.98% | 90.9% | +0.08% | 112,982 |  |
| Others | 99.41% | 99.3% | +0.11% | 1,854 |  |
| Apple Pay | 87.63% | 87.43% | +0.23% | 20,524 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Braintree | 91.46% | 91.62% | -0.18% | 103,450 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 638 |  |
| Adyen | 94.11% | 94.02% | +0.09% | 36,997 |  |
| Unknown | 99.31% | 99.12% | +0.19% | 1,153 |  |
| ProcessOut | 83.4% | 82.22% | +1.44% | 16,860 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 87.83% | 87.66% | +0.19% | 159,098 | 165,009 |  |
| 2_PreDunningAR | 89.65% | 89.66% | -0.01% | 159,098 | 165,009 |  |
| 3_PostDunningAR | 90.73% | 90.82% | -0.10% | 159,098 | 165,009 |  |
| 6_PaymentApprovalRate | 91.31% | 91.27% | +0.05% | 159,098 | 165,009 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 67,441 | 66,405 | -1.5% | Stable |
| CG | High (>92%) | 44,290 | 41,024 | -7.4% | Stable |
| CK | High (>92%) | 41,704 | 40,466 | -3.0% | Stable |
| MR | Low (>85%) | 20,895 | 20,886 | +0.0% | Stable |
| AO | High (>92%) | 15,233 | 14,758 | -3.1% | Stable |
| GN | High (>92%) | 14,255 | 15,192 | +6.6% | Stable |
| KN | Medium (>85%) | 11,044 | 11,084 | +0.4% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-19*
