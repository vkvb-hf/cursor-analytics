# PAR Investigation: WL 2026-W18

**Metric:** Payment Approval Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 91.67% → 91.24% (-0.47%)  
**Volume:** 166,895 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate declined by -0.47 percentage points (91.67% → 91.24%) on volume of 166,895 orders, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | First payment attempt | -0.71pp | ⚠️ |
| 2_PreDunningAR | Pre-dunning recovery | -0.53pp | ⚠️ |
| 3_PostDunningAR | Post-dunning recovery | -0.53pp | ⚠️ |
| 6_PaymentApprovalRate | Final approval | -0.47pp | ⚠️ |

**Key Findings:**
- The decline originates at the FirstRunAR step (-0.71pp), with recovery efforts partially mitigating the impact downstream
- All countries show uniform decline between -0.16pp and -0.57pp; no country exceeded the ±2.5% threshold requiring deep-dive investigation
- Credit Card (-0.57pp) and Apple Pay (-0.65pp) payment methods showed the largest declines, while PayPal remained stable (-0.03pp)
- MR experienced a +13.1% volume increase while maintaining a low-tier approval rate (80.62%), though impact remains stable
- The 8-week trend shows rates fluctuating within a narrow band (91.04% - 91.69%), suggesting normal operational variance

**Action:** Monitor — The decline is not statistically significant, no single dimension exceeds alert thresholds, and the change aligns with historical weekly fluctuations. Continue standard monitoring through W19.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W18 | 91.24% | 166,895 | -0.47% ← REPORTED CHANGE |
| 2026-W17 | 91.67% | 166,258 | -0.02% |
| 2026-W16 | 91.69% | 164,785 | +0.04% |
| 2026-W15 | 91.65% | 160,979 | +0.67% |
| 2026-W14 | 91.04% | 165,018 | -0.28% |
| 2026-W13 | 91.3% | 169,667 | -0.02% |
| 2026-W12 | 91.32% | 169,891 | -0.27% |
| 2026-W11 | 91.57% | 174,933 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| ER | 90.93% | 91.46% | -0.57% | 68,051 |  |
| KN | 87.89% | 88.31% | -0.48% | 11,123 |  |
| MR | 80.62% | 81.00% | -0.47% | 22,211 |  |
| CK | 95.21% | 95.62% | -0.43% | 41,405 |  |
| CG | 97.19% | 97.35% | -0.16% | 43,448 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 87.91% | 88.48% | -0.65% | 20,391 |  |
| Credit Card | 92.19% | 92.71% | -0.57% | 102,112 |  |
| Others | 83.83% | 84.05% | -0.27% | 19,148 |  |
| Paypal | 95.72% | 95.75% | -0.03% | 25,244 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | nan% | +nan% | 0 |  |
| Braintree | 91.57% | 92.02% | -0.48% | 109,506 |  |
| Adyen | 94.0% | 94.42% | -0.45% | 38,327 |  |
| Unknown | 83.16% | 83.36% | -0.25% | 18,379 |  |
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
| AO | High (>92%) | 15,121 | 15,590 | +3.1% | Stable |
| KN | Medium (>85%) | 10,454 | 11,123 | +6.4% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-05*
