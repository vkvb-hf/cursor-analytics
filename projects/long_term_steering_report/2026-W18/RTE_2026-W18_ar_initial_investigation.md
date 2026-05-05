# AR Initial (LL0) Investigation: RTE 2026-W18

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 93.18% → 92.55% (-0.68%)  
**Volume:** 32,461 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) declined from 93.18% to 92.55% (-0.63pp) in W18, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (90.85%-93.18%) | -0.63pp | ✅ |
| L1: Country Breakdown | TO exceeded ±2.5% threshold (-3.04%) | -3.04% | ⚠️ |
| L1: Dimension Scan | No payment method/provider exceeded threshold | Credit Card -2.06% | ✅ |
| L2: TO Deep-Dive | PayPal decline (-5.21%), Insufficient Funds +2.32pp | Root cause identified | ⚠️ |
| L3: Related Metrics | All funnel metrics declined similarly (-0.55% to -0.74%) | Consistent pattern | ✅ |
| Mix Shift | No significant volume shifts impacting overall rate | Stable | ✅ |

**Key Findings:**
- TO is the only country exceeding the ±2.5% threshold with a -3.04% decline (from 88.22% to 85.54%, volume: 415 orders)
- Root cause in TO identified as PayPal payment method (-5.21% decline) combined with increased "Insufficient Funds" declines (+2.32pp)
- Credit Card payments showed the largest decline at L1 (-2.06%) but remained below threshold
- Adyen provider declined -1.73% (from 93.17% to 91.56%) across 9,809 orders
- All related funnel metrics (FirstRunAR, PostDunningAR, PaymentApprovalRate) show consistent declines of similar magnitude, indicating a systemic rather than isolated issue

**Action:** Monitor - The overall change is not statistically significant and TO represents only 1.3% of total volume (415/32,461 orders). Continue monitoring PayPal performance in TO and Insufficient Funds trends.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W18 | 92.55% | 32,461 | -0.68% ← REPORTED CHANGE |
| 2026-W17 | 93.18% | 30,471 | +0.75% |
| 2026-W16 | 92.49% | 31,000 | +0.94% |
| 2026-W15 | 91.63% | 29,054 | +0.86% |
| 2026-W14 | 90.85% | 31,832 | -0.61% |
| 2026-W13 | 91.41% | 36,393 | -1.24% |
| 2026-W12 | 92.56% | 42,779 | +0.05% |
| 2026-W11 | 92.51% | 46,365 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TO | 85.54% | 88.22% | -3.04% | 415 | ⚠️ |
| CF | 93.00% | 95.30% | -2.41% | 6,632 |  |
| TV | 91.59% | 93.40% | -1.95% | 309 |  |
| YE | 89.79% | 90.24% | -0.49% | 3,468 |  |
| FJ | 92.88% | 93.05% | -0.18% | 20,093 |  |

**Countries exceeding ±2.5% threshold:** TO

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 90.46% | 92.36% | -2.06% | 8,760 |  |
| Paypal | 96.14% | 96.55% | -0.42% | 3,968 |  |
| Apple Pay | 91.79% | 91.99% | -0.22% | 6,807 |  |
| Others | 93.26% | 93.34% | -0.09% | 12,926 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | nan% | +nan% | 0 |  |
| Adyen | 91.56% | 93.17% | -1.73% | 9,809 |  |
| Braintree | 93.26% | 93.57% | -0.33% | 10,936 |  |
| Unknown | 92.68% | 92.81% | -0.14% | 11,670 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 46 |  |

---

## L2: TO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 1 | 0 |  |
| None | 0.00% | 0.00% | +0.00% | 0 | 2 |  |
| paypal | 93.59% | 98.73% | -5.21% | 78 | 79 | ⚠️ |
| credit_card | 86.52% | 90.46% | -4.35% | 230 | 262 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 4 | 1 |  |
| applepay | 77.45% | 76.42% | +1.36% | 102 | 106 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 0.00% | +0.00% | 1 | 2 |  |
| Adyen | 86.52% | 90.46% | -4.35% | 230 | 262 |  |
| Braintree | 84.44% | 85.95% | -1.75% | 180 | 185 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 4 | 1 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 355 | 397 | 85.54% | 88.22% | -2.68 |
| Insufficient Funds | 41 | 34 | 9.88% | 7.56% | +2.32 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 10 | 8 | 2.41% | 1.78% | +0.63 |
| Unknown | 1 | 2 | 0.24% | 0.44% | -0.20 |
| Other reasons | 8 | 9 | 1.93% | 2.00% | -0.07 |

**Root Cause:** paypal + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.12% | 90.62% | -0.55% | 32,461 | 30,471 |  |
| 2_PreDunningAR | 92.55% | 93.18% | -0.68% | 32,461 | 30,471 |  |
| 3_PostDunningAR | 92.79% | 93.45% | -0.71% | 32,461 | 30,471 |  |
| 6_PaymentApprovalRate | 92.91% | 93.6% | -0.74% | 32,461 | 30,471 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 18,460 | 20,093 | +8.8% | Stable |
| CF | High (>92%) | 6,338 | 6,632 | +4.6% | Stable |
| YE | Medium (>85%) | 3,431 | 3,468 | +1.1% | Stable |
| TT | High (>92%) | 540 | 728 | +34.8% | Stable |
| TZ | High (>92%) | 528 | 520 | -1.5% | Stable |
| TO | Medium (>85%) | 450 | 415 | -7.8% | Stable |
| TV | High (>92%) | 379 | 309 | -18.5% | Stable |
| TK | Medium (>85%) | 345 | 296 | -14.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TO | ↓ -3.04% | paypal -5.2% | → Stable | Insufficient Funds +2.32pp | paypal + Insufficient |

---

*Report: 2026-05-05*
