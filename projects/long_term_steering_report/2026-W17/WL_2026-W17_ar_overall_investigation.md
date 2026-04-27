# AR Overall Investigation: WL 2026-W17

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 90.02% → 90.1% (+0.09%)  
**Volume:** 166,258 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate remained stable at 90.1%, showing a marginal improvement of +0.09pp from the prior week (90.02%), which is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within normal range | +0.13pp | ✅ |
| 2_PreDunningAR | Within normal range | +0.08pp | ✅ |
| 3_PostDunningAR | Slight decline | -0.20pp | ⚠️ |
| 6_PaymentApprovalRate | No change | +0.00pp | ✅ |

**Key Findings:**
- No countries exceeded the ±2.5% threshold; all country-level movements were within normal variance (KN: -0.64pp, AO: +1.84pp, CK: +0.50pp, GN: +0.18pp)
- ProcessOut payment provider shows 0 volume in current week versus 84.71% rate in prior week, indicating potential provider discontinuation or data issue
- AO showed the strongest improvement at +1.84pp (87.79% → 89.41%) while KN had the largest decline at -0.64pp (87.81% → 87.25%)
- Mix shift analysis shows stable volume distribution across AR tiers with no significant structural changes
- Post-Dunning AR showed a slight decline of -0.20pp (91.15% → 90.96%), partially offsetting pre-dunning gains

**Action:** Monitor – No immediate action required. Continue standard weekly monitoring; verify ProcessOut volume drop if this provider is expected to be active.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 90.1% | 166,258 | +0.09% ← REPORTED CHANGE |
| 2026-W16 | 90.02% | 164,785 | -0.09% |
| 2026-W15 | 90.1% | 160,979 | +0.87% |
| 2026-W14 | 89.32% | 165,018 | -0.43% |
| 2026-W13 | 89.71% | 169,667 | +0.07% |
| 2026-W12 | 89.65% | 169,891 | -0.14% |
| 2026-W11 | 89.78% | 174,933 | +0.79% |
| 2026-W10 | 89.08% | 179,965 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| KN | 87.25% | 87.81% | -0.64% | 10,454 |  |
| GN | 94.36% | 94.19% | +0.18% | 15,898 |  |
| CK | 93.78% | 93.32% | +0.50% | 42,618 |  |
| AO | 89.41% | 87.79% | +1.84% | 15,121 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 94.88% | 95.03% | -0.16% | 25,020 |  |
| Others | 83.14% | 83.16% | -0.02% | 18,863 |  |
| Credit Card | 90.77% | 90.68% | +0.10% | 102,102 |  |
| Apple Pay | 87.27% | 86.62% | +0.75% | 20,273 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 84.71% | +nan% | 0 |  |
| Braintree | 90.95% | 91.11% | -0.17% | 108,854 |  |
| Unknown | 82.41% | 82.43% | -0.02% | 18,057 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 732 |  |
| Adyen | 91.09% | 90.34% | +0.83% | 38,615 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.19% | 88.07% | +0.13% | 166,258 | 164,785 |  |
| 2_PreDunningAR | 90.1% | 90.02% | +0.08% | 166,258 | 164,785 |  |
| 3_PostDunningAR | 90.96% | 91.15% | -0.20% | 166,258 | 164,785 |  |
| 6_PaymentApprovalRate | 91.69% | 91.69% | +0.00% | 166,258 | 164,785 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 69,808 | 72,449 | +3.8% | Stable |
| CK | High (>92%) | 43,017 | 42,618 | -0.9% | Stable |
| CG | High (>92%) | 42,996 | 43,878 | +2.1% | Stable |
| MR | Low (>85%) | 18,584 | 19,639 | +5.7% | Stable |
| GN | High (>92%) | 15,445 | 15,898 | +2.9% | Stable |
| AO | Medium (>85%) | 14,640 | 15,121 | +3.3% | Stable |
| KN | Medium (>85%) | 11,057 | 10,454 | -5.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-27*
