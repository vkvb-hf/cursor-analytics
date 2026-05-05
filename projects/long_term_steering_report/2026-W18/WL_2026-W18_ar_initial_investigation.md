# AR Initial (LL0) Investigation: WL 2026-W18

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 92.17% → 91.98% (-0.21%)  
**Volume:** 11,390 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) declined marginally from 92.17% to 91.98% (-0.19pp) in W18, a change that is not statistically significant and remains within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.13pp | ✅ |
| 2_PreDunningAR | Reported Metric | -0.20pp | ✅ |
| 3_PostDunningAR | Dunning Recovery | -0.11pp | ✅ |
| 6_PaymentApprovalRate | Final Approval | -0.08pp | ✅ |

**Key Findings:**
- No countries exceeded the ±2.5% threshold; GN showed the largest decline at -1.38pp (92.78% current)
- All payment methods experienced minor declines, with Apple Pay showing the largest drop at -0.47pp
- Braintree provider showed a -0.72pp decline (94.02% current) while Adyen remained stable (+0.06pp)
- Volume decreased by 1.3% (11,538 → 11,390 orders), continuing a downward trend from W11 (14,300)
- Mix shift analysis shows all country tiers remained stable with no significant volume migrations impacting rates

**Action:** Monitor — The -0.19pp decline is not significant, no dimensional breakdowns exceeded thresholds, and the 8-week trend shows W18 rate (91.98%) remains comparable to W11 baseline (91.97%).

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W18 | 91.98% | 11,390 | -0.21% ← REPORTED CHANGE |
| 2026-W17 | 92.17% | 11,538 | +1.00% |
| 2026-W16 | 91.26% | 13,013 | +0.29% |
| 2026-W15 | 91.0% | 11,572 | +1.29% |
| 2026-W14 | 89.84% | 12,761 | +0.71% |
| 2026-W13 | 89.21% | 12,899 | -1.41% |
| 2026-W12 | 90.49% | 13,904 | -1.61% |
| 2026-W11 | 91.97% | 14,300 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| GN | 92.78% | 94.07% | -1.38% | 1,288 |  |
| CG | 94.09% | 95.21% | -1.17% | 1,574 |  |
| KN | 95.71% | 96.64% | -0.96% | 2,189 |  |
| ER | 89.33% | 88.56% | +0.87% | 1,875 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 93.49% | 93.93% | -0.47% | 3,009 |  |
| Credit Card | 88.1% | 88.39% | -0.34% | 3,268 |  |
| Paypal | 95.33% | 95.46% | -0.14% | 1,178 |  |
| Others | 93.06% | 92.77% | +0.32% | 3,935 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | nan% | +nan% | 0 |  |
| Braintree | 94.02% | 94.7% | -0.72% | 5,432 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 10 |  |
| Adyen | 84.79% | 84.74% | +0.06% | 2,084 |  |
| Unknown | 92.99% | 92.69% | +0.32% | 3,864 |  |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 89.34% | 89.46% | -0.13% | 11,390 | 11,538 |  |
| 2_PreDunningAR | 91.98% | 92.17% | -0.20% | 11,390 | 11,538 |  |
| 3_PostDunningAR | 92.18% | 92.28% | -0.11% | 11,390 | 11,538 |  |
| 6_PaymentApprovalRate | 92.32% | 92.39% | -0.08% | 11,390 | 11,538 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| MR | High (>92%) | 1,972 | 1,962 | -0.5% | Stable |
| KN | High (>92%) | 1,962 | 2,189 | +11.6% | Stable |
| CK | Medium (>85%) | 1,929 | 1,710 | -11.4% | Stable |
| ER | Medium (>85%) | 1,923 | 1,875 | -2.5% | Stable |
| CG | High (>92%) | 1,690 | 1,574 | -6.9% | Stable |
| GN | High (>92%) | 1,333 | 1,288 | -3.4% | Stable |
| AO | Low (>85%) | 729 | 792 | +8.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-05*
