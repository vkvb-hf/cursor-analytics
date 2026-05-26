# AR Initial (LL0) Investigation: WL 2026-W21

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 91.88% → 92.42% (+0.59%)  
**Volume:** 11,163 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) improved from 91.88% to 92.42% (+0.54pp) in 2026-W21, representing a statistically non-significant increase on 11,163 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 8-Week Trend Stability | Within normal range (89.84%-92.42%) | +0.59% | ✅ |
| Country Variance | 1 country exceeds ±2.5% threshold | CK +2.83% | ⚠️ |
| Payment Method Variance | All within ±2.5% threshold | Max: Paypal -1.99% | ✅ |
| Payment Provider Variance | 1 provider exceeds ±2.5% threshold | Adyen +3.50% | ⚠️ |
| Mix Shift Impact | No significant volume shifts | All Stable | ✅ |

**Key Findings:**
- CK showed the largest country-level improvement (+2.83%), driven by credit_card performance increasing from 84.83% to 89.83% (+5.89pp) via Adyen
- Within CK, PayPal experienced a significant decline from 93.63% to 85.57% (-8.06pp), though this was offset by credit card gains
- Adyen globally improved by +3.50% (86.62% → 89.65%), contributing positively to overall performance
- "Refused" decline reasons in CK increased from 1.54% to 3.26% (+1.72pp), while "Other reasons" decreased significantly from 6.17% to 1.83% (-4.33pp)
- All related funnel metrics (FirstRunAR, PostDunningAR, PaymentApprovalRate) showed consistent improvement between +0.50% and +0.80%

**Action:** Monitor - The overall improvement is positive but not statistically significant. Continue tracking CK PayPal performance and Adyen trends over the next 2-3 weeks to confirm stability.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W21 | 92.42% | 11,163 | +0.59% ← REPORTED CHANGE |
| 2026-W20 | 91.88% | 12,112 | -0.31% |
| 2026-W19 | 92.17% | 12,194 | +0.25% |
| 2026-W18 | 91.94% | 11,379 | -0.23% |
| 2026-W17 | 92.15% | 11,532 | +0.99% |
| 2026-W16 | 91.25% | 12,998 | +0.29% |
| 2026-W15 | 90.99% | 11,562 | +1.28% |
| 2026-W14 | 89.84% | 12,754 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| GN | 93.26% | 94.61% | -1.43% | 1,216 |  |
| CG | 91.98% | 93.27% | -1.39% | 1,483 |  |
| AO | 84.62% | 85.65% | -1.21% | 572 |  |
| KN | 95.32% | 94.66% | +0.69% | 2,392 |  |
| CK | 89.64% | 87.17% | +2.83% | 1,747 | ⚠️ |

**Countries exceeding ±2.5% threshold:** CK

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 88.92% | 90.72% | -1.99% | 1,182 |  |
| Apple Pay | 91.86% | 92.6% | -0.80% | 3,230 |  |
| Others | 99.17% | 99.41% | -0.25% | 1,322 |  |
| Credit Card | 91.88% | 90.24% | +1.82% | 5,429 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Braintree | 92.39% | 93.0% | -0.66% | 5,480 |  |
| Unknown | 99.13% | 99.39% | -0.26% | 1,266 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 16 |  |
| ProcessOut | 91.18% | 90.69% | +0.55% | 2,450 |  |
| Adyen | 89.65% | 86.62% | +3.50% | 1,951 | ⚠️ |

---

## L2: CK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 3 | 0 |  |
| None | 0.00% | 0.00% | +0.00% | 0 | 3 |  |
| paypal | 85.57% | 93.63% | -8.60% | 201 | 251 | ⚠️ |
| applepay | 92.53% | 93.67% | -1.22% | 281 | 300 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 4 | 7 |  |
| credit_card | 89.83% | 84.83% | +5.89% | 1,258 | 1,450 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 0.00% | +0.00% | 3 | 3 |  |
| Braintree | 89.63% | 93.65% | -4.29% | 482 | 551 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 4 | 7 |  |
| Adyen | 89.83% | 84.83% | +5.89% | 1,258 | 1,450 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Other reasons | 32 | 124 | 1.83% | 6.17% | -4.33 |
| 1. SUCCESSFULL | 1,566 | 1,753 | 89.64% | 87.17% | +2.47 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 57 | 31 | 3.26% | 1.54% | +1.72 |
| Insufficient Funds | 89 | 100 | 5.09% | 4.97% | +0.12 |
| Unknown | 3 | 3 | 0.17% | 0.15% | +0.02 |

**Root Cause:** paypal + Adyen + Other

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 89.79% | 89.34% | +0.50% | 11,163 | 12,112 |  |
| 2_PreDunningAR | 92.42% | 91.88% | +0.59% | 11,163 | 12,112 |  |
| 3_PostDunningAR | 92.64% | 91.98% | +0.71% | 11,163 | 12,112 |  |
| 6_PaymentApprovalRate | 92.86% | 92.12% | +0.80% | 11,163 | 12,112 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| MR | High (>92%) | 2,567 | 2,261 | -11.9% | Stable |
| KN | High (>92%) | 2,266 | 2,392 | +5.6% | Stable |
| CK | Medium (>85%) | 2,011 | 1,747 | -13.1% | Stable |
| ER | Low (>85%) | 1,759 | 1,492 | -15.2% | Stable |
| CG | High (>92%) | 1,635 | 1,483 | -9.3% | Stable |
| GN | High (>92%) | 1,205 | 1,216 | +0.9% | Stable |
| AO | Medium (>85%) | 669 | 572 | -14.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| CK | ↑ +2.83% | paypal -8.6% | Adyen +5.9% | Other reasons -4.33pp | paypal + Adyen + Other |

---

*Report: 2026-05-26*
