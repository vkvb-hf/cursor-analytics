# PAR Investigation: WL 2026-W17

**Metric:** Payment Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 91.69% → 91.69% (+0.00%)  
**Volume:** 166,258 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate remained flat at 91.69% (+0.00%) week-over-week with 166,258 orders processed, representing no significant change from W16 to W17.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | +0.13% | ✅ |
| 2_PreDunningAR | Pre-Dunning | +0.08% | ✅ |
| 3_PostDunningAR | Post-Dunning | -0.20% | ✅ |
| 6_PaymentApprovalRate | Final PAR | +0.00% | ✅ |

**Key Findings:**
- **MR underperformance:** MR declined -2.98% (81.05% → from 83.54%), exceeding the ±2.5% threshold and flagged for attention
- **MR root cause identified:** Increase in "Refused" decline reasons (+2.25pp) combined with payment method data anomaly (None values showing -100% change) driving the degradation
- **MR provider impact:** Braintree in MR declined -2.53% (79.39% from 81.45%) with 14,718 volume; Unknown provider declined -3.20%
- **Credit card weakness in MR:** Credit card approval rate dropped -3.79% (76.52% from 79.54%) representing the largest payment method decline
- **Overall stability maintained:** Despite MR decline, other countries (CK +0.24%, GN +0.26%, AO +0.60%) offset the impact, keeping overall PAR unchanged

**Action:** Monitor - While overall PAR is stable, recommend monitoring MR closely for continued "Refused" decline increases and investigate the payment method data quality issue (None values anomaly). If MR decline persists beyond W18, escalate to payment provider review with Braintree.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 91.69% | 166,258 | - ← REPORTED CHANGE |
| 2026-W16 | 91.69% | 164,785 | +0.04% |
| 2026-W15 | 91.65% | 160,979 | +0.66% |
| 2026-W14 | 91.05% | 165,018 | -0.27% |
| 2026-W13 | 91.3% | 169,667 | -0.02% |
| 2026-W12 | 91.32% | 169,891 | -0.28% |
| 2026-W11 | 91.58% | 174,933 | +1.03% |
| 2026-W10 | 90.65% | 179,965 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| MR | 81.05% | 83.54% | -2.98% | 19,639 | ⚠️ |
| KN | 88.31% | 88.90% | -0.67% | 10,454 |  |
| ER | 91.46% | 91.32% | +0.16% | 72,449 |  |
| CK | 95.64% | 95.41% | +0.24% | 42,618 |  |
| GN | 95.84% | 95.58% | +0.26% | 15,898 |  |
| AO | 94.60% | 94.03% | +0.60% | 15,121 |  |

**Countries exceeding ±2.5% threshold:** MR

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 95.76% | 95.91% | -0.16% | 25,020 |  |
| Credit Card | 92.73% | 92.76% | -0.03% | 102,102 |  |
| Others | 84.09% | 83.85% | +0.28% | 18,863 |  |
| Apple Pay | 88.49% | 88.02% | +0.53% | 20,273 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 87.2% | +nan% | 0 |  |
| Braintree | 92.03% | 92.18% | -0.17% | 108,854 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 732 |  |
| Unknown | 83.39% | 83.12% | +0.32% | 18,057 |  |
| Adyen | 94.44% | 94.07% | +0.39% | 38,615 |  |

---

## L2: MR Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 85.89% | 0.00% | +0.00% | 4,870 | 0 |  |
| None | 0.00% | 88.71% | -100.00% | 0 | 5,295 | ⚠️ |
| credit_card | 76.52% | 79.54% | -3.79% | 9,264 | 8,361 |  |
| applepay | 78.05% | 78.80% | -0.95% | 2,524 | 2,363 |  |
| paypal | 89.55% | 90.15% | -0.66% | 2,920 | 2,529 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 61 | 36 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| ProcessOut | 0.00% | 0.00% | +0.00% | 0 | 2 |  |
| Unknown | 85.86% | 88.70% | -3.20% | 4,860 | 5,293 |  |
| Braintree | 79.39% | 81.45% | -2.53% | 14,718 | 13,253 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 61 | 36 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 15,918 | 15,525 | 81.05% | 83.54% | -2.49 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 2,501 | 1,948 | 12.73% | 10.48% | +2.25 |
| Other reasons | 468 | 399 | 2.38% | 2.15% | +0.24 |
| Insufficient Funds | 752 | 712 | 3.83% | 3.83% | +0.00 |

**Root Cause:** None + Refused

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
| AO | High (>92%) | 14,640 | 15,121 | +3.3% | Stable |
| KN | Medium (>85%) | 11,057 | 10,454 | -5.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| MR | ↓ -2.98% | None -100.0% | → Stable | Refused - eg: Declined, Closed Card, Do Not Honor, etc. +2.25pp | None + Refused |

---

*Report: 2026-04-27*
