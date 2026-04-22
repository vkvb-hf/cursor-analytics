# AR Overall Investigation: WL 2026-W15

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 90.1% → 90.03% (-0.08%)  
**Volume:** 164,785 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate remained essentially flat at 90.03%, declining by -0.08pp from the prior week (90.1%), a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | +0.92pp | ✅ |
| 2_PreDunningAR | Reported Metric | +0.87pp | ✅ |
| 3_PostDunningAR | Post-Dunning | +0.61pp | ✅ |
| 6_PaymentApprovalRate | Final Approval | +0.67pp | ✅ |

**Key Findings:**
- All funnel metrics show positive week-over-week improvement ranging from +0.61pp to +0.92pp, indicating healthy payment acceptance performance
- No countries exceeded the ±2.5% threshold; AO showed the largest country-level improvement at +2.17pp
- ProcessOut payment provider improved significantly (+2.32pp), while Unknown provider shows a ⚠️ flag with +69.73% change, though on minimal volume (664 orders)
- Mix shift analysis shows volume declines in AO (-12.0%), GN (-8.5%), and MR (-6.3%), but impact remains stable across all countries
- The 8-week trend shows consistent improvement from 88.19% (W09) to 90.03% (W16), representing a +1.84pp gain over the period

**Action:** Monitor — No significant changes detected; all metrics trending positively within normal operating ranges.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 90.03% | 164,785 | -0.08% |
| 2026-W15 | 90.1% | 160,979 | +0.87% ← REPORTED CHANGE |
| 2026-W14 | 89.32% | 165,018 | -0.45% |
| 2026-W13 | 89.72% | 169,667 | +0.08% |
| 2026-W12 | 89.65% | 169,891 | -0.14% |
| 2026-W11 | 89.78% | 174,933 | +0.79% |
| 2026-W10 | 89.08% | 179,965 | +1.01% |
| 2026-W09 | 88.19% | 180,862 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| GN | 93.32% | 92.33% | +1.07% | 13,110 |  |
| ER | 90.32% | 89.22% | +1.23% | 68,811 |  |
| MR | 81.37% | 80.21% | +1.45% | 19,468 |  |
| AO | 87.06% | 85.21% | +2.17% | 13,883 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 86.04% | 85.75% | +0.33% | 20,488 |  |
| Paypal | 95.25% | 94.68% | +0.61% | 24,084 |  |
| Others | 98.21% | 97.46% | +0.77% | 1,393 |  |
| Credit Card | 89.65% | 88.79% | +0.96% | 115,014 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 683 |  |
| Braintree | 91.25% | 90.76% | +0.54% | 105,580 |  |
| Adyen | 90.56% | 89.6% | +1.07% | 36,376 |  |
| ProcessOut | 81.62% | 79.77% | +2.32% | 17,676 |  |
| Unknown | 96.99% | 57.14% | +69.73% | 664 | ⚠️ |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.17% | 87.37% | +0.92% | 160,979 | 165,018 |  |
| 2_PreDunningAR | 90.1% | 89.32% | +0.87% | 160,979 | 165,018 |  |
| 3_PostDunningAR | 91.21% | 90.66% | +0.61% | 160,979 | 165,018 |  |
| 6_PaymentApprovalRate | 91.65% | 91.05% | +0.67% | 160,979 | 165,018 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 67,730 | 68,811 | +1.6% | Stable |
| CG | High (>92%) | 44,581 | 43,937 | -1.4% | Stable |
| CK | High (>92%) | 42,176 | 42,398 | +0.5% | Stable |
| MR | Low (>85%) | 20,784 | 19,468 | -6.3% | Stable |
| AO | Medium (>85%) | 15,776 | 13,883 | -12.0% | Stable |
| GN | High (>92%) | 14,333 | 13,110 | -8.5% | Stable |
| KN | Medium (>85%) | 11,048 | 10,259 | -7.1% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
