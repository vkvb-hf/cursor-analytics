# AR Initial (LL0) Investigation: WL 2026-W19

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 91.97% → 92.22% (+0.27%)  
**Volume:** 12,211 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) improved slightly from 91.97% to 92.22% (+0.25pp) in W19, a statistically non-significant change within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (89.21%-92.22%) | +0.27% | ✅ |
| L1: Country Breakdown | 2 countries exceed ±2.5% threshold (ER, CK) | ER -2.96%, CK +4.62% | ⚠️ |
| L1: Dimension Scan | Adyen shows +3.37% improvement | +3.37% | ⚠️ |
| L2: ER Deep-Dive | Insufficient Funds increased +1.68pp | -2.96% | ⚠️ |
| L2: CK Deep-Dive | Credit Card/Adyen improved +6.09% | +4.62% | ✅ |
| L3: Related Metrics | All funnel stages stable | +0.25% to +0.57% | ✅ |
| Mix Shift | No significant volume shifts impacting rate | Stable | ✅ |

**Key Findings:**
- ER declined -2.96% driven primarily by increased "Insufficient Funds" declines (+1.68pp), affecting both Apple Pay (-4.70%) and Braintree (-3.86%)
- CK improved +4.62% with credit card transactions via Adyen showing +6.09% improvement and "Insufficient Funds" declines decreasing by -2.26pp
- The offsetting movements in ER (negative) and CK (positive) resulted in minimal net impact to the overall metric
- All related funnel metrics (FirstRunAR, PostDunningAR, PaymentApprovalRate) moved in sync with slight improvements (+0.25% to +0.57%)
- Volume increased 7.2% WoW (11,388 → 12,211 orders) with no concerning mix shifts

**Action:** Monitor - The overall change is not statistically significant and falls within normal variance. Continue monitoring ER for sustained Insufficient Funds trends; no immediate escalation required.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W19 | 92.22% | 12,211 | +0.27% ← REPORTED CHANGE |
| 2026-W18 | 91.97% | 11,388 | -0.21% |
| 2026-W17 | 92.16% | 11,536 | +0.99% |
| 2026-W16 | 91.26% | 13,007 | +0.30% |
| 2026-W15 | 90.99% | 11,570 | +1.29% |
| 2026-W14 | 89.83% | 12,760 | +0.69% |
| 2026-W13 | 89.21% | 12,898 | -1.41% |
| 2026-W12 | 90.49% | 13,903 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| ER | 86.68% | 89.32% | -2.96% | 1,922 | ⚠️ |
| CG | 93.44% | 94.10% | -0.70% | 1,738 |  |
| KN | 95.15% | 95.66% | -0.54% | 2,452 |  |
| MR | 98.10% | 97.50% | +0.61% | 2,156 |  |
| AO | 83.84% | 83.21% | +0.76% | 792 |  |
| CK | 89.18% | 85.25% | +4.62% | 1,914 | ⚠️ |

**Countries exceeding ±2.5% threshold:** ER, CK

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 93.94% | 95.33% | -1.45% | 1,238 |  |
| Others | 99.3% | 99.22% | +0.08% | 1,279 |  |
| Apple Pay | 92.54% | 92.41% | +0.14% | 3,498 |  |
| Credit Card | 90.24% | 89.78% | +0.51% | 6,196 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | 89.66% | 90.73% | -1.18% | 2,959 |  |
| Braintree | 93.8% | 94.08% | -0.30% | 5,786 |  |
| Unknown | 99.26% | 99.37% | -0.11% | 1,222 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 18 |  |
| Adyen | 87.6% | 84.75% | +3.37% | 2,226 | ⚠️ |

---

## L2: ER Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 2 | 0 |  |
| applepay | 86.50% | 90.76% | -4.70% | 600 | 617 |  |
| credit_card | 85.68% | 87.51% | -2.10% | 1,117 | 1,049 |  |
| paypal | 93.47% | 94.17% | -0.75% | 199 | 206 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 4 | 1 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 0.00% | +0.00% | 2 | 0 |  |
| Braintree | 87.97% | 91.50% | -3.86% | 831 | 847 |  |
| ProcessOut | 85.81% | 87.51% | -1.95% | 1,085 | 1,025 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 4 | 1 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,666 | 1,673 | 86.68% | 89.32% | -2.64 |
| Insufficient Funds | 177 | 141 | 9.21% | 7.53% | +1.68 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 28 | 17 | 1.46% | 0.91% | +0.55 |
| Other reasons | 50 | 42 | 2.60% | 2.24% | +0.36 |
| Unknown | 1 | 0 | 0.05% | 0.00% | +0.05 |

**Root Cause:** Insufficient

---

## L2: CK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 2 | 0 |  |
| None | 0.00% | 0.00% | +0.00% | 0 | 2 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 4 | 1 |  |
| paypal | 92.93% | 92.27% | +0.72% | 198 | 181 |  |
| applepay | 93.31% | 91.41% | +2.08% | 284 | 291 |  |
| credit_card | 87.94% | 82.89% | +6.09% | 1,426 | 1,233 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 0.00% | +0.00% | 2 | 2 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 4 | 1 |  |
| Braintree | 93.15% | 91.74% | +1.54% | 482 | 472 |  |
| Adyen | 87.94% | 82.89% | +6.09% | 1,426 | 1,233 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,707 | 1,456 | 89.18% | 85.25% | +3.94 |
| Insufficient Funds | 99 | 127 | 5.17% | 7.44% | -2.26 |
| Other reasons | 70 | 88 | 3.66% | 5.15% | -1.49 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 36 | 35 | 1.88% | 2.05% | -0.17 |
| Unknown | 2 | 2 | 0.10% | 0.12% | -0.01 |

**Root Cause:** credit_card + Adyen + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 89.85% | 89.34% | +0.57% | 12,211 | 11,388 |  |
| 2_PreDunningAR | 92.22% | 91.97% | +0.28% | 12,211 | 11,388 |  |
| 3_PostDunningAR | 92.41% | 92.18% | +0.25% | 12,211 | 11,388 |  |
| 6_PaymentApprovalRate | 92.63% | 92.32% | +0.34% | 12,211 | 11,388 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| KN | High (>92%) | 2,189 | 2,452 | +12.0% | Stable |
| MR | High (>92%) | 1,961 | 2,156 | +9.9% | Stable |
| ER | Medium (>85%) | 1,873 | 1,922 | +2.6% | Stable |
| CK | Medium (>85%) | 1,708 | 1,914 | +12.1% | Stable |
| CG | High (>92%) | 1,577 | 1,738 | +10.2% | Stable |
| GN | High (>92%) | 1,288 | 1,237 | -4.0% | Stable |
| AO | Low (>85%) | 792 | 792 | +0.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| ER | ↓ -2.96% | → Stable | → Stable | Insufficient Funds +1.68pp | Insufficient |
| CK | ↑ +4.62% | credit_card +6.1% | Adyen +6.1% | Insufficient Funds -2.26pp | credit_card + Adyen + Insufficient |

---

*Report: 2026-05-12*
