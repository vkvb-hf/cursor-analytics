# AR Initial (LL0) Investigation: RTE 2026-W22

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 93.06% → 92.81% (-0.27%)  
**Volume:** 27,695 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) declined from 93.06% to 92.81% (-0.27%) in W22, a change that is not statistically significant and falls within normal weekly fluctuation patterns observed over the 8-week trend (range: 91.68% - 93.06%).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Within normal range (91.68%-93.06%) | -0.27% | ✅ |
| L1: Country Breakdown | TZ (-3.41%), TO (-2.67%) exceed ±2.5% threshold | 2 flagged | ⚠️ |
| L1: Dimension Scan | Unknown provider -13.66% (53 vol only) | 1 flagged | ⚠️ |
| L2: TZ Deep-Dive | applepay -8.95%, Insufficient Funds +1.90pp | Root cause identified | ⚠️ |
| L2: TO Deep-Dive | bancontact -6.76%, Insufficient Funds +3.84pp | Root cause identified | ⚠️ |
| L3: Related Metrics | All metrics declined 0.23-0.61% | Consistent pattern | ✅ |
| Mix Shift | All countries stable, no significant volume shifts | No impact | ✅ |

**Key Findings:**
- TZ saw the largest decline (-3.41%), driven by Apple Pay performance dropping from 91.14% to 82.98% (-8.95%) with Insufficient Funds increasing by +1.90pp
- TO declined -2.67%, with bancontact dropping from 94.12% to 87.76% (-6.76%) and Insufficient Funds rising +3.84pp
- Both flagged countries have low volume (TZ: 382, TO: 327), representing only 2.6% of total orders, limiting overall metric impact
- The "Unknown" payment provider showed a -13.66% decline but affects only 53 transactions (0.2% of volume)
- All related metrics (FirstRunAR, PostDunningAR, PaymentApprovalRate) show consistent slight declines (-0.23% to -0.61%), indicating a systemic rather than isolated issue

**Action:** Monitor — The overall change is not significant and the flagged countries represent minimal volume. Continue tracking TZ and TO Apple Pay and bancontact performance for the next 2 weeks to determine if this is a temporary fluctuation or emerging trend.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W22 | 92.81% | 27,695 | -0.27% ← REPORTED CHANGE |
| 2026-W21 | 93.06% | 26,810 | +0.16% |
| 2026-W20 | 92.91% | 28,904 | +0.92% |
| 2026-W19 | 92.06% | 29,441 | -0.28% |
| 2026-W18 | 92.32% | 32,278 | -0.76% |
| 2026-W17 | 93.03% | 30,376 | +0.68% |
| 2026-W16 | 92.4% | 30,986 | +0.79% |
| 2026-W15 | 91.68% | 29,104 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TZ | 91.88% | 95.13% | -3.41% | 382 | ⚠️ |
| TO | 87.16% | 89.54% | -2.67% | 327 | ⚠️ |
| YE | 89.36% | 89.93% | -0.63% | 2,820 |  |
| CF | 93.83% | 94.19% | -0.38% | 5,190 |  |
| FJ | 93.05% | 93.16% | -0.12% | 17,853 |  |
| TT | 96.58% | 94.84% | +1.83% | 585 |  |

**Countries exceeding ±2.5% threshold:** TZ, TO

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 92.33% | 93.22% | -0.95% | 17,159 |  |
| Apple Pay | 91.61% | 91.03% | +0.63% | 6,235 |  |
| Others | 96.27% | 95.09% | +1.25% | 1,020 |  |
| Paypal | 96.56% | 95.19% | +1.44% | 3,281 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 56.6% | 65.56% | -13.66% | 53 | ⚠️ |
| ProcessOut | 93.23% | 94.26% | -1.08% | 10,168 |  |
| Adyen | 91.9% | 92.53% | -0.68% | 7,804 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 46 |  |
| Braintree | 93.28% | 92.46% | +0.88% | 9,624 |  |

---

## L2: TZ Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| applepay | 82.98% | 91.14% | -8.95% | 94 | 79 | ⚠️ |
| credit_card | 90.91% | 93.33% | -2.60% | 77 | 90 |  |
| paypal | 96.21% | 97.29% | -1.11% | 211 | 221 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Braintree | 92.13% | 95.67% | -3.70% | 305 | 300 |  |
| Adyen | 90.91% | 93.33% | -2.60% | 77 | 90 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 351 | 371 | 91.88% | 95.13% | -3.24 |
| Insufficient Funds | 19 | 12 | 4.97% | 3.08% | +1.90 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 11 | 7 | 2.88% | 1.79% | +1.08 |
| Other reasons | 1 | 0 | 0.26% | 0.00% | +0.26 |

**Root Cause:** applepay + Insufficient

---

## L2: TO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 0 | 1 |  |
| bancontact | 87.76% | 94.12% | -6.76% | 49 | 17 | ⚠️ |
| applepay | 82.19% | 85.90% | -4.31% | 73 | 78 |  |
| paypal | 96.36% | 100.00% | -3.64% | 55 | 51 |  |
| credit_card | 85.81% | 87.90% | -2.37% | 148 | 157 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 2 | 2 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 0.00% | +0.00% | 0 | 1 |  |
| Braintree | 88.28% | 91.47% | -3.49% | 128 | 129 |  |
| Adyen | 86.29% | 88.51% | -2.50% | 197 | 174 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 2 | 2 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Insufficient Funds | 35 | 21 | 10.70% | 6.86% | +3.84 |
| 1. SUCCESSFULL | 285 | 274 | 87.16% | 89.54% | -2.39 |
| Other reasons | 1 | 6 | 0.31% | 1.96% | -1.65 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 6 | 4 | 1.83% | 1.31% | +0.53 |
| Unknown | 0 | 1 | 0.00% | 0.33% | -0.33 |

**Root Cause:** bancontact + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.38% | 90.59% | -0.23% | 27,695 | 26,810 |  |
| 2_PreDunningAR | 92.81% | 93.06% | -0.27% | 27,695 | 26,810 |  |
| 3_PostDunningAR | 93.09% | 93.55% | -0.49% | 27,695 | 26,810 |  |
| 6_PaymentApprovalRate | 93.23% | 93.81% | -0.61% | 27,695 | 26,810 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 16,817 | 17,853 | +6.2% | Stable |
| CF | High (>92%) | 5,594 | 5,190 | -7.2% | Stable |
| YE | Medium (>85%) | 2,761 | 2,820 | +2.1% | Stable |
| TT | High (>92%) | 446 | 585 | +31.2% | Stable |
| TZ | High (>92%) | 390 | 382 | -2.1% | Stable |
| TO | Medium (>85%) | 306 | 327 | +6.9% | Stable |
| TK | High (>92%) | 264 | 284 | +7.6% | Stable |
| TV | High (>92%) | 232 | 254 | +9.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TZ | ↓ -3.41% | applepay -9.0% | → Stable | Insufficient Funds +1.90pp | applepay + Insufficient |
| TO | ↓ -2.67% | bancontact -6.8% | → Stable | Insufficient Funds +3.84pp | bancontact + Insufficient |

---

*Report: 2026-06-02*
