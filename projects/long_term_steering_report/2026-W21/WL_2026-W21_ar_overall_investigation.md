# AR Overall Investigation: WL 2026-W21

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 89.64% → 89.44% (-0.22%)  
**Volume:** 153,361 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate declined slightly from 89.64% to 89.44% (-0.20pp) in WL 2026-W21, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Largest decline in funnel | -0.57% | ⚠️ |
| 2_PreDunningAR | Reported metric | -0.22% | ✅ |
| 3_PostDunningAR | Downstream impact | -0.32% | ✅ |
| 6_PaymentApprovalRate | End-of-funnel | -0.17% | ✅ |

**Key Findings:**
- No countries exceeded the ±2.5% threshold; MR showed the largest decline at -1.02pp (81.85% → 81.01%) but remains within normal variance
- All payment methods declined slightly, with PayPal showing the largest drop (-0.44pp) though still maintaining the highest rate at 94.17%
- First Run AR shows the most notable decline (-0.57pp), suggesting the issue originates at initial payment attempt rather than retry/dunning stages
- Volume decreased across all major countries (total: 159,098 → 153,361, -3.6%), with GN seeing the largest volume drop (-6.5%)
- Mix shift analysis shows stable composition across all AR tiers with no significant structural changes

**Action:** Monitor — The decline is not statistically significant, no dimensional breakdowns exceed thresholds, and the 8-week trend shows the rate remains within the normal operating range (89.31% - 90.09%). Continue standard monitoring and revisit if the downward trend persists into W22.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W21 | 89.44% | 153,361 | -0.22% ← REPORTED CHANGE |
| 2026-W20 | 89.64% | 159,098 | - |
| 2026-W19 | 89.64% | 165,009 | +0.06% |
| 2026-W18 | 89.59% | 166,895 | -0.56% |
| 2026-W17 | 90.09% | 166,258 | +0.09% |
| 2026-W16 | 90.01% | 164,785 | -0.08% |
| 2026-W15 | 90.08% | 160,979 | +0.86% |
| 2026-W14 | 89.31% | 165,018 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| MR | 81.01% | 81.85% | -1.02% | 20,786 |  |
| GN | 95.18% | 95.55% | -0.39% | 14,205 |  |
| CK | 92.89% | 93.22% | -0.35% | 38,880 |  |
| AO | 88.44% | 88.30% | +0.15% | 14,291 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 94.17% | 94.59% | -0.44% | 22,927 |  |
| Others | 99.02% | 99.35% | -0.34% | 1,929 |  |
| Credit Card | 88.85% | 89.05% | -0.22% | 109,124 |  |
| Apple Pay | 86.23% | 86.29% | -0.08% | 19,381 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 98.82% | 99.22% | -0.40% | 1,273 |  |
| Braintree | 90.08% | 90.4% | -0.35% | 99,707 |  |
| ProcessOut | 82.07% | 82.16% | -0.11% | 15,687 |  |
| Adyen | 90.38% | 90.45% | -0.08% | 36,096 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 598 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 87.33% | 87.83% | -0.57% | 153,361 | 159,098 |  |
| 2_PreDunningAR | 89.44% | 89.64% | -0.22% | 153,361 | 159,098 |  |
| 3_PostDunningAR | 90.52% | 90.81% | -0.32% | 153,361 | 159,098 |  |
| 6_PaymentApprovalRate | 91.14% | 91.3% | -0.17% | 153,361 | 159,098 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 66,405 | 60,964 | -8.2% | Stable |
| CG | High (>92%) | 41,024 | 40,366 | -1.6% | Stable |
| CK | High (>92%) | 40,466 | 38,880 | -3.9% | Stable |
| MR | Low (>85%) | 20,886 | 20,786 | -0.5% | Stable |
| GN | High (>92%) | 15,192 | 14,205 | -6.5% | Stable |
| AO | Medium (>85%) | 14,758 | 14,291 | -3.2% | Stable |
| KN | Medium (>85%) | 11,084 | 11,080 | +0.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-26*
