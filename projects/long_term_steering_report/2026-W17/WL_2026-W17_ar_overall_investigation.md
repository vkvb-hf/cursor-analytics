# AR Overall Investigation: WL 2026-W17

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 90.02% → 90.1% (+0.09%)  
**Volume:** 166,258 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate improved marginally from 90.02% to 90.1% (+0.08pp) in W17, representing a statistically non-significant change across 166,258 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within normal range | +0.13pp | ✅ |
| 2_PreDunningAR | Within normal range | +0.08pp | ✅ |
| 3_PostDunningAR | Slight decline | -0.16pp | ⚠️ |
| 6_PaymentApprovalRate | Stable | -0.02pp | ✅ |

**Key Findings:**
- No countries exceeded the ±2.5% threshold; the largest country-level movement was AO at +1.84pp improvement
- KN showed a minor decline of -0.64pp but remains within acceptable variance
- ProcessOut payment provider shows no current volume (0 orders) compared to prior week activity
- Post-Dunning AR declined by -0.16pp, partially offsetting gains made in earlier funnel stages
- Volume mix remained stable across all country tiers with no significant shifts impacting overall rate

**Action:** Monitor — No investigation required. The metric change is not statistically significant and all dimensions remain within normal operating thresholds.

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
| CK | 93.78% | 93.31% | +0.50% | 42,618 |  |
| AO | 89.40% | 87.79% | +1.84% | 15,121 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 94.88% | 95.03% | -0.16% | 25,020 |  |
| Others | 83.14% | 83.16% | -0.03% | 18,862 |  |
| Credit Card | 90.77% | 90.68% | +0.10% | 102,103 |  |
| Apple Pay | 87.27% | 86.62% | +0.75% | 20,273 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 84.71% | +nan% | 0 |  |
| Braintree | 90.95% | 91.11% | -0.17% | 108,846 |  |
| Unknown | 82.42% | 82.43% | -0.02% | 18,062 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 732 |  |
| Adyen | 91.08% | 90.34% | +0.83% | 38,618 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.19% | 88.07% | +0.13% | 166,258 | 164,785 |  |
| 2_PreDunningAR | 90.1% | 90.02% | +0.08% | 166,258 | 164,785 |  |
| 3_PostDunningAR | 91.03% | 91.18% | -0.16% | 166,258 | 164,785 |  |
| 6_PaymentApprovalRate | 91.67% | 91.69% | -0.02% | 166,258 | 164,785 |  |

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

*Report: 2026-04-28*
