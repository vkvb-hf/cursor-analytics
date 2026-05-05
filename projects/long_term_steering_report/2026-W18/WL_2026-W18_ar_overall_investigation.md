# AR Overall Investigation: WL 2026-W18

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 90.09% → 89.61% (-0.53%)  
**Volume:** 166,895 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate declined by -0.53% (from 90.09% to 89.61%) in W18, a statistically non-significant change affecting 166,895 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Upstream decline | -0.71% | ⚠️ |
| 2_PreDunningAR | Reported metric | -0.53% | ⚠️ |
| 3_PostDunningAR | Downstream impact | -0.53% | ⚠️ |
| 6_PaymentApprovalRate | End conversion | -0.47% | ⚠️ |

**Key Findings:**
- The decline appears to originate upstream at FirstRunAR (-0.71%), which then cascades through the funnel with consistent ~0.5% drops at each subsequent step
- No individual country exceeded the ±2.5% threshold; all four countries (AO, CK, ER, MR) showed modest declines between -0.49% and -0.76%
- Credit Card payments showed the largest decline (-0.67%) among payment methods, while PayPal remained stable (+0.00%)
- Adyen showed a higher decline (-0.86%) compared to Braintree (-0.41%) among payment providers
- MR experienced a +13.1% volume increase but maintained stable impact despite having the lowest AR tier (80.42%)

**Action:** Monitor — The change is not statistically significant, no country breached thresholds, and the decline pattern is uniform across the funnel suggesting a systemic but minor fluctuation rather than a specific failure point.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W18 | 89.61% | 166,895 | -0.53% ← REPORTED CHANGE |
| 2026-W17 | 90.09% | 166,258 | +0.09% |
| 2026-W16 | 90.01% | 164,785 | -0.09% |
| 2026-W15 | 90.09% | 160,979 | +0.86% |
| 2026-W14 | 89.32% | 165,018 | -0.43% |
| 2026-W13 | 89.71% | 169,667 | +0.07% |
| 2026-W12 | 89.65% | 169,891 | -0.14% |
| 2026-W11 | 89.78% | 174,933 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| AO | 88.72% | 89.39% | -0.76% | 15,590 |  |
| CK | 93.13% | 93.77% | -0.69% | 41,405 |  |
| ER | 89.72% | 90.18% | -0.51% | 68,051 |  |
| MR | 80.42% | 80.81% | -0.49% | 22,211 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 90.15% | 90.76% | -0.67% | 102,112 |  |
| Apple Pay | 86.79% | 87.26% | -0.54% | 20,391 |  |
| Others | 82.81% | 83.17% | -0.43% | 19,148 |  |
| Paypal | 94.87% | 94.88% | +0.00% | 25,244 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | nan% | +nan% | 0 |  |
| Adyen | 90.29% | 91.07% | -0.86% | 38,327 |  |
| Braintree | 90.57% | 90.94% | -0.41% | 109,506 |  |
| Unknown | 82.12% | 82.45% | -0.39% | 18,379 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 683 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 87.56% | 88.19% | -0.71% | 166,895 | 166,258 |  |
| 2_PreDunningAR | 89.61% | 90.09% | -0.53% | 166,895 | 166,258 |  |
| 3_PostDunningAR | 90.74% | 91.22% | -0.53% | 166,895 | 166,258 |  |
| 6_PaymentApprovalRate | 91.24% | 91.67% | -0.47% | 166,895 | 166,258 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 72,449 | 68,051 | -6.1% | Stable |
| CG | High (>92%) | 43,878 | 43,448 | -1.0% | Stable |
| CK | High (>92%) | 42,618 | 41,405 | -2.8% | Stable |
| MR | Low (>85%) | 19,639 | 22,211 | +13.1% | Stable |
| GN | High (>92%) | 15,898 | 14,971 | -5.8% | Stable |
| AO | Medium (>85%) | 15,121 | 15,590 | +3.1% | Stable |
| KN | Medium (>85%) | 10,454 | 11,123 | +6.4% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-05*
