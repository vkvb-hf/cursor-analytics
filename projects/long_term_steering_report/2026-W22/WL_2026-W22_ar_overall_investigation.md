# AR Overall Investigation: WL 2026-W22

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 89.28% → 89.34% (+0.07%)  
**Volume:** 149,430 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Pre-Dunning Acceptance Rate (Overall) remained essentially stable at 89.34%, showing a marginal increase of +0.07pp from 89.28% in W21, which is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Stable within range | +0.07pp | ✅ |
| L1: Country Threshold (±2.5%) | KN exceeded threshold | +2.65pp | ⚠️ |
| L1: PaymentMethod | All within normal range | Max +0.21pp | ✅ |
| L1: PaymentProvider | All within normal range | Max +0.26pp | ✅ |
| L2: KN Deep-Dive | PayPal & ProcessOut flagged | +6.56pp / +6.94pp | ⚠️ |
| L3: Related Metrics | Minor variations | -0.27pp to +0.08pp | ✅ |

**Key Findings:**
- KN was the only country exceeding the ±2.5% threshold with a +2.65pp improvement (84.55% → 86.79%), driven by PayPal (+6.56pp) and ProcessOut (+6.94pp)
- The "Other reasons" decline category in KN dropped significantly from 2.69% to 0.00% (-2.69pp), contributing to the acceptance rate improvement
- Overall volume decreased by 2.6% (153,361 → 149,430 orders), continuing a downward trend observed since W18
- GN showed the largest volume decline (-11.1%) among countries but maintained high performance at 94.60%
- Post-Dunning AR showed a slight decline of -0.27pp (90.60% → 90.35%), worth monitoring

**Action:** Monitor — The overall metric is stable and not significant. The KN improvement is positive and appears driven by resolution of "Other reasons" declines. Continue standard monitoring; no escalation required.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W22 | 89.34% | 149,430 | +0.07% ← REPORTED CHANGE |
| 2026-W21 | 89.28% | 153,361 | -0.39% |
| 2026-W20 | 89.63% | 159,098 | -0.01% |
| 2026-W19 | 89.64% | 165,009 | +0.06% |
| 2026-W18 | 89.59% | 166,895 | -0.56% |
| 2026-W17 | 90.09% | 166,258 | +0.09% |
| 2026-W16 | 90.01% | 164,785 | -0.08% |
| 2026-W15 | 90.08% | 160,979 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| GN | 94.60% | 95.16% | -0.59% | 12,634 |  |
| ER | 89.48% | 89.65% | -0.19% | 59,188 |  |
| AO | 88.85% | 88.44% | +0.46% | 14,539 |  |
| MR | 81.63% | 80.89% | +0.92% | 21,254 |  |
| KN | 86.79% | 84.55% | +2.65% | 10,954 | ⚠️ |

**Countries exceeding ±2.5% threshold:** KN

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 85.96% | 85.97% | -0.01% | 18,586 |  |
| Credit Card | 88.75% | 88.73% | +0.03% | 106,325 |  |
| Others | 99.12% | 99.02% | +0.11% | 1,941 |  |
| Paypal | 94.05% | 93.85% | +0.21% | 22,578 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | 81.84% | 82.06% | -0.27% | 15,692 |  |
| Adyen | 90.15% | 90.35% | -0.22% | 35,614 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 605 |  |
| Unknown | 98.97% | 98.82% | +0.15% | 1,260 |  |
| Braintree | 90.07% | 89.84% | +0.26% | 96,259 |  |

---

## L2: KN Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| cashcredit | 100.00% | 100.00% | +0.00% | 15 | 14 |  |
| applepay | 83.71% | 82.87% | +1.02% | 2,910 | 3,070 |  |
| credit_card | 86.61% | 84.64% | +2.34% | 6,552 | 6,633 |  |
| paypal | 93.50% | 87.75% | +6.56% | 1,477 | 1,363 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| No Payment | 100.00% | 100.00% | +0.00% | 15 | 14 |  |
| Braintree | 86.77% | 84.53% | +2.65% | 10,927 | 11,052 |  |
| ProcessOut | 91.67% | 85.71% | +6.94% | 12 | 14 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Other reasons | 0 | 298 | 0.00% | 2.69% | -2.69 |
| 1. SUCCESSFULL | 9,507 | 9,368 | 86.79% | 84.55% | +2.24 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 882 | 843 | 8.05% | 7.61% | +0.44 |
| Insufficient Funds | 565 | 571 | 5.16% | 5.15% | +0.00 |

**Root Cause:** paypal + ProcessOut + Other

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
| AO | Medium (>85%) | 14,291 | 14,539 | +1.7% | Stable |
| GN | High (>92%) | 14,205 | 12,634 | -11.1% | Stable |
| KN | Low (>85%) | 11,080 | 10,954 | -1.1% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| KN | ↑ +2.65% | paypal +6.6% | ProcessOut +6.9% | Other reasons -2.69pp | paypal + ProcessOut + Other |

---

*Report: 2026-06-02*
