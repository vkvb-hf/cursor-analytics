# AR Overall Investigation: WL 2026-W15

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 89.33% → 90.1% (+0.86%)  
**Volume:** 160,979 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate improved from 89.33% to 90.1% (+0.86 pp) week-over-week, with the change flagged as not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | +0.92 pp | ✅ |
| 2_PreDunningAR | Reported Metric | +0.87 pp | ✅ |
| 3_PostDunningAR | Dunning Recovery | +0.53 pp | ✅ |
| 6_PaymentApprovalRate | Final Approval | +0.67 pp | ✅ |

**Key Findings:**
- All funnel stages showed positive movement, with 1_FirstRunAR leading at +0.92 pp, indicating broad-based improvement across the payment acceptance pipeline
- No countries exceeded the ±2.5% threshold; AO showed the largest country-level improvement at +2.17 pp (87.06% current)
- ProcessOut provider improved significantly (+2.31 pp to 81.62%) though remains the lowest-performing provider; Unknown provider shows anomalous +69.73% change but represents minimal volume (664 orders)
- Volume declined 2.4% week-over-week (165,018 → 160,979 orders), with notable drops in AO (-12.0%), GN (-8.5%), and MR (-6.3%)
- The 8-week trend shows steady improvement from 88.14% (W08) to 90.1% (W15), representing cumulative gain of +1.96 pp

**Action:** Monitor — The improvement is positive but not statistically significant. Continue tracking the upward trend, particularly ProcessOut's performance recovery and volume shifts in AO and GN.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 90.1% | 160,979 | +0.86% ← REPORTED CHANGE |
| 2026-W14 | 89.33% | 165,018 | -0.43% |
| 2026-W13 | 89.72% | 169,667 | +0.07% |
| 2026-W12 | 89.66% | 169,891 | -0.13% |
| 2026-W11 | 89.78% | 174,933 | +0.79% |
| 2026-W10 | 89.08% | 179,965 | +1.01% |
| 2026-W09 | 88.19% | 180,862 | +0.06% |
| 2026-W08 | 88.14% | 179,647 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| GN | 93.32% | 92.33% | +1.07% | 13,110 |  |
| ER | 90.32% | 89.22% | +1.23% | 68,811 |  |
| MR | 81.41% | 80.25% | +1.45% | 19,468 |  |
| AO | 87.06% | 85.21% | +2.17% | 13,883 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 86.04% | 85.75% | +0.34% | 20,488 |  |
| Paypal | 95.26% | 94.68% | +0.61% | 24,084 |  |
| Others | 98.21% | 97.46% | +0.77% | 1,393 |  |
| Credit Card | 89.65% | 88.8% | +0.96% | 115,014 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 683 |  |
| Braintree | 91.26% | 90.77% | +0.54% | 105,580 |  |
| Adyen | 90.56% | 89.6% | +1.07% | 36,376 |  |
| ProcessOut | 81.62% | 79.78% | +2.31% | 17,676 |  |
| Unknown | 96.99% | 57.14% | +69.73% | 664 | ⚠️ |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.17% | 87.37% | +0.92% | 160,979 | 165,018 |  |
| 2_PreDunningAR | 90.1% | 89.33% | +0.87% | 160,979 | 165,018 |  |
| 3_PostDunningAR | 91.03% | 90.55% | +0.53% | 160,979 | 165,018 |  |
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

*Report: 2026-04-15*
