# PAR Investigation: WL 2026-W17

**Metric:** Payment Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 91.69% → 91.67% (-0.02%)  
**Volume:** 166,258 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate remained essentially stable at 91.67% in W17, declining by just -0.02pp from 91.69% in W16, a statistically insignificant change across 166,258 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | +0.13% | ✅ |
| 2_PreDunningAR | vs Prior | +0.08% | ✅ |
| 3_PostDunningAR | vs Prior | -0.16% | ⚠️ |
| 6_PaymentApprovalRate | Final | -0.02% | ✅ |

**Key Findings:**
- MR is the only country exceeding the ±2.5% threshold with a -3.04pp decline (83.54% → 81.00%), driven by increased "Refused" declines (+2.27pp)
- In MR, credit_card payment method showed the largest degradation at -3.86% (79.54% → 76.47%) with 9,264 orders
- MR's Braintree provider declined -2.60% (81.45% → 79.33%) across 14,710 transactions
- PostDunningAR shows slight weakness at -0.16%, partially offsetting gains in earlier funnel stages
- 8-week trend shows W17 rate (91.67%) remains elevated compared to W10-W14 range (90.65%-91.32%)

**Action:** Monitor - The overall metric change is not significant. Continue monitoring MR's elevated refusal rates, particularly for credit card transactions through Braintree, but no immediate escalation required.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 91.67% | 166,258 | -0.02% ← REPORTED CHANGE |
| 2026-W16 | 91.69% | 164,785 | +0.04% |
| 2026-W15 | 91.65% | 160,979 | +0.66% |
| 2026-W14 | 91.05% | 165,018 | -0.27% |
| 2026-W13 | 91.3% | 169,667 | -0.02% |
| 2026-W12 | 91.32% | 169,891 | -0.27% |
| 2026-W11 | 91.57% | 174,933 | +1.01% |
| 2026-W10 | 90.65% | 179,965 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| MR | 81.00% | 83.54% | -3.04% | 19,639 | ⚠️ |
| KN | 88.31% | 88.90% | -0.67% | 10,454 |  |
| ER | 91.46% | 91.32% | +0.16% | 72,449 |  |
| CK | 95.62% | 95.41% | +0.23% | 42,618 |  |
| GN | 95.82% | 95.58% | +0.25% | 15,898 |  |
| AO | 94.60% | 94.03% | +0.60% | 15,121 |  |

**Countries exceeding ±2.5% threshold:** MR

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 95.75% | 95.91% | -0.16% | 25,020 |  |
| Credit Card | 92.71% | 92.76% | -0.05% | 102,103 |  |
| Others | 84.06% | 83.85% | +0.26% | 18,862 |  |
| Apple Pay | 88.48% | 88.02% | +0.52% | 20,273 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 87.2% | +nan% | 0 |  |
| Braintree | 92.02% | 92.18% | -0.18% | 108,846 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 732 |  |
| Unknown | 83.37% | 83.12% | +0.30% | 18,062 |  |
| Adyen | 94.42% | 94.07% | +0.37% | 38,618 |  |

---

## L2: MR Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 85.81% | 0.00% | +0.00% | 4,869 | 0 |  |
| None | 0.00% | 88.71% | -100.00% | 0 | 5,295 | ⚠️ |
| credit_card | 76.47% | 79.54% | -3.86% | 9,264 | 8,361 |  |
| applepay | 78.02% | 78.80% | -0.99% | 2,525 | 2,363 |  |
| paypal | 89.52% | 90.15% | -0.70% | 2,920 | 2,529 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 61 | 36 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| ProcessOut | 0.00% | 0.00% | +0.00% | 0 | 2 |  |
| Unknown | 85.81% | 88.70% | -3.27% | 4,868 | 5,293 |  |
| Braintree | 79.33% | 81.45% | -2.60% | 14,710 | 13,253 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 61 | 36 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 15,907 | 15,525 | 81.00% | 83.54% | -2.54 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 2,505 | 1,948 | 12.76% | 10.48% | +2.27 |
| Other reasons | 472 | 399 | 2.40% | 2.15% | +0.26 |
| Insufficient Funds | 755 | 712 | 3.84% | 3.83% | +0.01 |

**Root Cause:** None + Refused

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
| AO | High (>92%) | 14,640 | 15,121 | +3.3% | Stable |
| KN | Medium (>85%) | 11,057 | 10,454 | -5.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| MR | ↓ -3.04% | None -100.0% | → Stable | Refused - eg: Declined, Closed Card, Do Not Honor, etc. +2.27pp | None + Refused |

---

*Report: 2026-04-28*
