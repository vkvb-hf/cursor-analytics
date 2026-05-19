# AR Initial (LL0) Investigation: WL 2026-W20

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 92.19% → 91.91% (-0.30%)  
**Volume:** 12,122 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) declined marginally from 92.19% to 91.91% (-0.28pp) in 2026-W20, a change that is not statistically significant and remains within normal weekly fluctuation range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (89.2%-92.19%) | -0.28pp | ✅ |
| L1: Country Breakdown | ER exceeds ±2.5% threshold (-2.63%) | -2.63% | ⚠️ |
| L1: Dimension Scan | PayPal exceeds threshold (-3.41%) | -3.41% | ⚠️ |
| L2: ER Deep-Dive | PayPal in ER dropped significantly (-17.59%) | -17.59% | ⚠️ |
| L3: Related Metrics | All metrics stable (<1% change) | -0.31% to -0.55% | ✅ |
| Mix Shift Analysis | No significant volume shifts impacting rate | Stable | ✅ |

**Key Findings:**
- ER experienced the largest country-level decline (-2.63%), driven primarily by PayPal payment method dropping from 93.43% to 77.00% (-17.59pp) on a volume of 200 orders
- "Refused" decline reasons in ER increased by +1.99pp (from 1.46% to 3.46%), indicating potential issuer-side rejections
- PayPal globally declined from 93.94% to 90.73% (-3.21pp), with ER contributing significantly to this drop
- Overall metric remains within the 8-week historical range (89.2%-92.19%), suggesting no systemic issue
- Related funnel metrics (FirstRunAR, PostDunningAR, PaymentApprovalRate) all show parallel small declines of 0.45-0.55%, indicating consistent behavior across the payment lifecycle

**Action:** Monitor - The overall decline is not significant and the 8-week trend shows healthy performance. However, continue monitoring PayPal performance in ER for the next 1-2 weeks to determine if the "Refused" decline spike is a transient issue or emerging pattern.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W20 | 91.91% | 12,122 | -0.30% ← REPORTED CHANGE |
| 2026-W19 | 92.19% | 12,196 | +0.27% |
| 2026-W18 | 91.94% | 11,384 | -0.24% |
| 2026-W17 | 92.16% | 11,534 | +1.00% |
| 2026-W16 | 91.25% | 12,998 | +0.29% |
| 2026-W15 | 90.99% | 11,568 | +1.29% |
| 2026-W14 | 89.83% | 12,756 | +0.71% |
| 2026-W13 | 89.2% | 12,894 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| ER | 84.31% | 86.58% | -2.63% | 1,765 | ⚠️ |
| CK | 87.23% | 89.17% | -2.18% | 2,012 |  |
| GN | 94.61% | 93.11% | +1.61% | 1,205 |  |
| AO | 85.65% | 83.84% | +2.16% | 669 |  |

**Countries exceeding ±2.5% threshold:** ER

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 90.73% | 93.94% | -3.41% | 1,273 | ⚠️ |
| Apple Pay | 92.61% | 92.53% | +0.09% | 3,503 |  |
| Credit Card | 90.29% | 90.19% | +0.11% | 6,149 |  |
| Others | 99.42% | 99.3% | +0.12% | 1,197 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Adyen | 86.66% | 87.58% | -1.06% | 2,196 |  |
| Braintree | 93.03% | 93.77% | -0.79% | 5,735 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 16 |  |
| Unknown | 99.39% | 99.26% | +0.13% | 1,145 |  |
| ProcessOut | 90.73% | 89.61% | +1.25% | 3,030 |  |

---

## L2: ER Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 2 | 0 |  |
| None | 0.00% | 0.00% | +0.00% | 0 | 2 |  |
| paypal | 77.00% | 93.43% | -17.59% | 200 | 198 | ⚠️ |
| credit_card | 83.42% | 85.53% | -2.47% | 971 | 1,113 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 1 | 4 |  |
| applepay | 88.49% | 86.45% | +2.36% | 591 | 598 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 0.00% | +0.00% | 2 | 2 |  |
| Braintree | 85.47% | 87.92% | -2.79% | 812 | 828 |  |
| ProcessOut | 83.47% | 85.66% | -2.55% | 950 | 1,081 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 1 | 4 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,488 | 1,658 | 84.31% | 86.58% | -2.27 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 61 | 28 | 3.46% | 1.46% | +1.99 |
| Other reasons | 55 | 51 | 3.12% | 2.66% | +0.45 |
| Insufficient Funds | 159 | 177 | 9.01% | 9.24% | -0.23 |
| Unknown | 2 | 1 | 0.11% | 0.05% | +0.06 |

**Root Cause:** paypal + Refused

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 89.35% | 89.84% | -0.55% | 12,122 | 12,196 |  |
| 2_PreDunningAR | 91.91% | 92.19% | -0.31% | 12,122 | 12,196 |  |
| 3_PostDunningAR | 91.99% | 92.41% | -0.45% | 12,122 | 12,196 |  |
| 6_PaymentApprovalRate | 92.18% | 92.6% | -0.45% | 12,122 | 12,196 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| KN | High (>92%) | 2,452 | 2,266 | -7.6% | Stable |
| MR | High (>92%) | 2,156 | 2,569 | +19.2% | Stable |
| ER | Medium (>85%) | 1,915 | 1,765 | -7.8% | Stable |
| CK | Medium (>85%) | 1,912 | 2,012 | +5.2% | Stable |
| CG | High (>92%) | 1,736 | 1,636 | -5.8% | Stable |
| GN | High (>92%) | 1,233 | 1,205 | -2.3% | Stable |
| AO | Low (>85%) | 792 | 669 | -15.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| ER | ↓ -2.63% | paypal -17.6% | → Stable | Refused - eg: Declined, Closed Card, Do Not Honor, etc. +1.99pp | paypal + Refused |

---

*Report: 2026-05-19*
