# PAR Investigation: WL 2026-W23

**Metric:** Payment Approval Rate  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 90.96% → 91.44% (+0.53%)  
**Volume:** 153,811 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate improved slightly from 90.96% to 91.44% (+0.48pp) in W23, representing a recovery from the prior week's dip but remaining within normal fluctuation range and not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within normal range | +0.36pp | ✅ |
| 2_PreDunningAR | Within normal range | +0.52pp | ✅ |
| 3_PostDunningAR | Within normal range | +0.35pp | ✅ |
| 6_PaymentApprovalRate | Within normal range | +0.48pp | ✅ |

**Key Findings:**
- All funnel steps showed modest improvement in W23, with PreDunningAR showing the largest gain (+0.52pp), suggesting improved payment success before retry logic
- No countries exceeded the ±2.5% threshold; KN showed the largest country-level improvement (+1.32pp) while AO showed a minor decline (-0.35pp)
- Apple Pay showed the strongest payment method improvement (+0.94pp to 88.15%), though it remains the lowest-performing method
- ProcessOut provider improved by +0.89pp but continues to underperform at 83.76% compared to Adyen (93.8%) and Braintree (91.61%)
- Mix shift analysis shows stable volume distribution across all country tiers with no significant compositional changes

**Action:** Monitor — The improvement is modest and not statistically significant. Continue standard weekly monitoring; no investigation required.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W23 | 91.44% | 153,811 | +0.53% ← REPORTED CHANGE |
| 2026-W22 | 90.96% | 149,452 | -0.19% |
| 2026-W21 | 91.13% | 153,383 | -0.18% |
| 2026-W20 | 91.29% | 159,125 | +0.02% |
| 2026-W19 | 91.27% | 165,044 | +0.03% |
| 2026-W18 | 91.24% | 166,925 | -0.46% |
| 2026-W17 | 91.66% | 166,292 | -0.02% |
| 2026-W16 | 91.68% | 164,829 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| AO | 94.03% | 94.36% | -0.35% | 14,887 |  |
| ER | 90.95% | 90.76% | +0.20% | 60,315 |  |
| MR | 82.57% | 81.84% | +0.90% | 20,891 |  |
| GN | 96.79% | 95.88% | +0.94% | 13,422 |  |
| KN | 89.20% | 88.04% | +1.32% | 11,545 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 99.15% | 99.28% | -0.13% | 2,350 |  |
| Paypal | 95.16% | 94.85% | +0.32% | 22,982 |  |
| Credit Card | 91.07% | 90.62% | +0.49% | 109,412 |  |
| Apple Pay | 88.15% | 87.32% | +0.94% | 19,067 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 99.03% | 99.13% | -0.10% | 1,546 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 706 |  |
| Adyen | 93.8% | 93.57% | +0.24% | 36,959 |  |
| Braintree | 91.61% | 91.13% | +0.52% | 98,777 |  |
| ProcessOut | 83.76% | 83.03% | +0.89% | 15,823 |  |

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
| AO | High (>92%) | 14,544 | 14,887 | +2.4% | Stable |
| GN | High (>92%) | 12,636 | 13,422 | +6.2% | Stable |
| KN | Medium (>85%) | 10,954 | 11,545 | +5.4% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-09*
