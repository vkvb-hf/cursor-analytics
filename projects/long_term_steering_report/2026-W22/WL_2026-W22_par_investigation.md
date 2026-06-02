# PAR Investigation: WL 2026-W22

**Metric:** Payment Approval Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 91.13% → 90.97% (-0.18%)  
**Volume:** 149,430 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate declined marginally from 91.13% to 90.97% (-0.16pp) in W22, representing a statistically non-significant change on 149,430 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within normal range | +0.08pp | ✅ |
| 2_PreDunningAR | Within normal range | +0.07pp | ✅ |
| 3_PostDunningAR | Slight decline | -0.27pp | ⚠️ |
| 6_PaymentApprovalRate | Slight decline | -0.18pp | ✅ |

**Key Findings:**
- No countries exceeded the ±2.5% threshold; CK showed the largest decline at -0.64pp (94.72%) and GN at -0.52pp (95.88%)
- PostDunningAR showed the largest funnel step decline at -0.27pp, suggesting recovery efforts were slightly less effective this week
- Adyen showed the steepest provider decline at -0.66pp while Braintree remained stable (+0.01pp)
- Volume decreased by 2.6% (153,361 → 149,430), with GN (-11.1%) and CG (-10.0%) showing notable volume drops
- 8-week trend shows gradual rate decline from 91.65% (W15) to 90.97% (W22), a cumulative -0.68pp erosion

**Action:** Monitor — The decline is not statistically significant and no single dimension breaches investigation thresholds. Continue tracking the gradual downward trend over the next 2-3 weeks.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W22 | 90.97% | 149,430 | -0.18% ← REPORTED CHANGE |
| 2026-W21 | 91.13% | 153,361 | -0.18% |
| 2026-W20 | 91.29% | 159,098 | +0.02% |
| 2026-W19 | 91.27% | 165,009 | +0.03% |
| 2026-W18 | 91.24% | 166,895 | -0.47% |
| 2026-W17 | 91.67% | 166,258 | -0.01% |
| 2026-W16 | 91.68% | 164,785 | +0.03% |
| 2026-W15 | 91.65% | 160,979 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CK | 94.72% | 95.33% | -0.64% | 39,729 |  |
| GN | 95.88% | 96.39% | -0.52% | 12,634 |  |
| CG | 97.09% | 97.04% | +0.05% | 36,321 |  |
| AO | 94.36% | 94.31% | +0.05% | 14,539 |  |
| MR | 81.84% | 81.19% | +0.80% | 21,254 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 94.85% | 95.19% | -0.36% | 22,578 |  |
| Apple Pay | 87.32% | 87.59% | -0.31% | 18,586 |  |
| Credit Card | 90.63% | 90.76% | -0.15% | 106,325 |  |
| Others | 99.28% | 99.17% | +0.11% | 1,941 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Adyen | 93.58% | 94.2% | -0.66% | 35,614 |  |
| ProcessOut | 83.02% | 83.13% | -0.13% | 15,692 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 605 |  |
| Braintree | 91.13% | 91.12% | +0.01% | 96,259 |  |
| Unknown | 99.13% | 99.06% | +0.07% | 1,260 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 87.39% | 87.33% | +0.08% | 149,430 | 153,361 |  |
| 2_PreDunningAR | 89.34% | 89.28% | +0.07% | 149,430 | 153,361 |  |
| 3_PostDunningAR | 90.35% | 90.6% | -0.27% | 149,430 | 153,361 |  |
| 6_PaymentApprovalRate | 90.97% | 91.13% | -0.18% | 149,430 | 153,361 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 60,964 | 59,188 | -2.9% | Stable |
| CG | High (>92%) | 40,366 | 36,321 | -10.0% | Stable |
| CK | High (>92%) | 38,880 | 39,729 | +2.2% | Stable |
| MR | Low (>85%) | 20,786 | 21,254 | +2.3% | Stable |
| AO | High (>92%) | 14,291 | 14,539 | +1.7% | Stable |
| GN | High (>92%) | 14,205 | 12,634 | -11.1% | Stable |
| KN | Medium (>85%) | 11,080 | 10,954 | -1.1% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-02*
