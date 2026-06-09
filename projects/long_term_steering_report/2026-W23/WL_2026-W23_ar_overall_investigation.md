# AR Overall Investigation: WL 2026-W23

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 89.32% → 89.84% (+0.58%)  
**Volume:** 153,811 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate improved slightly from 89.32% to 89.84% (+0.52 pp) on volume of 153,811 orders, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within normal range | +0.40 pp | ✅ |
| 2_PreDunningAR | Within normal range | +0.58 pp | ✅ |
| 3_PostDunningAR | Within normal range | +0.38 pp | ✅ |
| 6_PaymentApprovalRate | Within normal range | +0.52 pp | ✅ |

**Key Findings:**
- No countries exceeded the ±2.5% threshold for investigation; all country-level movements are within normal variance
- KN showed the largest country improvement at +1.73 pp (86.77% → 88.27%), while AO had a minor decline of -0.84 pp
- All payment methods showed stable performance; Credit Card (+0.60 pp) and Apple Pay (+0.79 pp) showed slight improvements on significant volume
- Braintree, the largest payment provider by volume (98,777 orders), improved by +0.64 pp
- Mix shift analysis indicates stable volume distribution across all AR tiers with no significant rebalancing

**Action:** Monitor — No significant deviations detected. Continue standard weekly monitoring.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W23 | 89.84% | 153,811 | +0.58% ← REPORTED CHANGE |
| 2026-W22 | 89.32% | 149,452 | +0.07% |
| 2026-W21 | 89.26% | 153,383 | -0.40% |
| 2026-W20 | 89.62% | 159,125 | -0.01% |
| 2026-W19 | 89.63% | 165,044 | +0.04% |
| 2026-W18 | 89.59% | 166,925 | -0.54% |
| 2026-W17 | 90.08% | 166,292 | +0.08% |
| 2026-W16 | 90.01% | 164,829 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| AO | 88.10% | 88.85% | -0.84% | 14,887 |  |
| ER | 89.87% | 89.48% | +0.43% | 60,315 |  |
| GN | 95.30% | 94.60% | +0.74% | 13,422 |  |
| MR | 82.20% | 81.50% | +0.86% | 20,891 |  |
| KN | 88.27% | 86.77% | +1.73% | 11,545 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 98.85% | 99.12% | -0.28% | 2,350 |  |
| Paypal | 94.31% | 94.04% | +0.28% | 22,982 |  |
| Credit Card | 89.26% | 88.73% | +0.60% | 109,412 |  |
| Apple Pay | 86.63% | 85.95% | +0.79% | 19,067 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 98.58% | 98.97% | -0.39% | 1,546 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 706 |  |
| Adyen | 90.27% | 90.13% | +0.15% | 36,959 |  |
| Braintree | 90.63% | 90.05% | +0.64% | 98,777 |  |
| ProcessOut | 82.6% | 81.84% | +0.93% | 15,823 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 87.75% | 87.39% | +0.40% | 153,811 | 149,452 |  |
| 2_PreDunningAR | 89.84% | 89.32% | +0.58% | 153,811 | 149,452 |  |
| 3_PostDunningAR | 90.87% | 90.52% | +0.38% | 153,811 | 149,452 |  |
| 6_PaymentApprovalRate | 91.44% | 90.96% | +0.52% | 153,811 | 149,452 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 59,197 | 60,315 | +1.9% | Stable |
| CK | High (>92%) | 39,730 | 41,389 | +4.2% | Stable |
| CG | High (>92%) | 36,335 | 37,690 | +3.7% | Stable |
| MR | Low (>85%) | 21,254 | 20,891 | -1.7% | Stable |
| AO | Medium (>85%) | 14,544 | 14,887 | +2.4% | Stable |
| GN | High (>92%) | 12,636 | 13,422 | +6.2% | Stable |
| KN | Medium (>85%) | 10,954 | 11,545 | +5.4% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-09*
