# AR Initial (LL0) Investigation: RTE 2026-W17

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 92.47% → 93.34% (+0.94%)  
**Volume:** 30,993 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) improved from 92.47% to 93.34% (+0.94%), a non-significant change within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Consistent upward trend W15-W17 | +0.94% | ✅ |
| L1: Country Breakdown | 2 countries exceed ±2.5% threshold | TK -3.57%, TV -2.78% | ⚠️ |
| L1: Dimension Scan | All payment methods/providers stable | <1.3% change | ✅ |
| L2: TK Deep-Dive | PayPal via Braintree degradation | -11.11%, -5.34% | ⚠️ |
| L2: TV Deep-Dive | Credit card performance decline | -5.06% | ⚠️ |
| L3: Related Metrics | All funnel stages improving consistently | +0.88% to +0.94% | ✅ |
| Mix Shift | No material volume shifts | All stable | ✅ |

**Key Findings:**
- TK experienced a -3.57% AR decline driven by PayPal (-11.11%) and Braintree (-5.34%), with Insufficient Funds increasing +2.37pp
- TV declined -2.78% due to credit_card performance drop (-5.06%) and Insufficient Funds rising +2.33pp
- Both flagged countries have low volume (TK: 345, TV: 379) representing ~2.3% of total volume combined
- Global trend shows steady recovery from W13 low (91.38%) to current W17 high (93.34%)
- All related metrics (FirstRunAR, PostDunningAR, PaymentApprovalRate) show aligned improvement of ~0.9%

**Action:** Monitor - The overall metric is improving and flagged countries represent minimal volume impact. Continue monitoring TK and TV for sustained Insufficient Funds trends over the next 2-3 weeks.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 93.34% | 30,993 | +0.94% ← REPORTED CHANGE |
| 2026-W16 | 92.47% | 31,118 | +0.89% |
| 2026-W15 | 91.65% | 29,043 | +0.89% |
| 2026-W14 | 90.84% | 31,949 | -0.59% |
| 2026-W13 | 91.38% | 36,470 | -1.27% |
| 2026-W12 | 92.56% | 42,779 | +0.05% |
| 2026-W11 | 92.51% | 46,365 | -0.23% |
| 2026-W10 | 92.72% | 48,166 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TK | 91.59% | 94.99% | -3.57% | 345 | ⚠️ |
| TV | 93.40% | 96.07% | -2.78% | 379 | ⚠️ |
| TO | 88.22% | 90.40% | -2.41% | 450 |  |
| FJ | 93.30% | 92.44% | +0.94% | 18,971 |  |
| YE | 90.30% | 88.90% | +1.58% | 3,442 |  |
| CF | 95.31% | 93.54% | +1.89% | 6,338 |  |

**Countries exceeding ±2.5% threshold:** TK, TV

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 96.78% | 96.61% | +0.18% | 3,752 |  |
| Apple Pay | 92.21% | 91.75% | +0.50% | 6,380 |  |
| Others | 93.51% | 92.65% | +0.93% | 12,304 |  |
| Credit Card | 92.44% | 91.51% | +1.02% | 8,557 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 92.07% | +nan% | 0 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 35 |  |
| Braintree | 93.82% | 93.43% | +0.42% | 10,293 |  |
| Adyen | 93.21% | 92.03% | +1.28% | 9,465 |  |
| Unknown | 93.0% | 91.81% | +1.29% | 11,200 |  |

---

## L2: TK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| paypal | 88.89% | 100.00% | -11.11% | 9 | 17 | ⚠️ |
| applepay | 90.16% | 94.67% | -4.76% | 122 | 169 |  |
| credit_card | 92.31% | 94.76% | -2.59% | 208 | 210 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 6 | 3 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Braintree | 90.08% | 95.16% | -5.34% | 131 | 186 | ⚠️ |
| Adyen | 92.31% | 94.76% | -2.59% | 208 | 210 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 6 | 3 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 316 | 379 | 91.59% | 94.99% | -3.39 |
| Insufficient Funds | 22 | 16 | 6.38% | 4.01% | +2.37 |
| Other reasons | 4 | 2 | 1.16% | 0.50% | +0.66 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 3 | 2 | 0.87% | 0.50% | +0.37 |

**Root Cause:** paypal + Braintree + Insufficient

---

## L2: TV Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 0 | 1 |  |
| credit_card | 89.72% | 94.51% | -5.06% | 107 | 91 | ⚠️ |
| applepay | 90.00% | 93.33% | -3.57% | 80 | 75 |  |
| klarna | 96.65% | 98.73% | -2.10% | 179 | 157 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 4 | 2 |  |
| paypal | 100.00% | 100.00% | +0.00% | 9 | 5 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 0.00% | +0.00% | 0 | 1 |  |
| Adyen | 94.06% | 97.18% | -3.21% | 286 | 248 |  |
| Braintree | 91.01% | 93.75% | -2.92% | 89 | 80 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 4 | 2 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 354 | 318 | 93.40% | 96.07% | -2.67 |
| Insufficient Funds | 18 | 8 | 4.75% | 2.42% | +2.33 |
| Other reasons | 5 | 3 | 1.32% | 0.91% | +0.41 |
| Unknown | 0 | 1 | 0.00% | 0.30% | -0.30 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 2 | 1 | 0.53% | 0.30% | +0.23 |

**Root Cause:** credit_card + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.83% | 90.0% | +0.93% | 30,993 | 31,118 |  |
| 2_PreDunningAR | 93.34% | 92.47% | +0.94% | 30,993 | 31,118 |  |
| 3_PostDunningAR | 93.56% | 92.74% | +0.88% | 30,993 | 31,118 |  |
| 6_PaymentApprovalRate | 93.77% | 92.91% | +0.93% | 30,993 | 31,118 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 19,168 | 18,971 | -1.0% | Stable |
| CF | High (>92%) | 6,535 | 6,338 | -3.0% | Stable |
| YE | Medium (>85%) | 3,089 | 3,442 | +11.4% | Stable |
| TT | High (>92%) | 587 | 540 | -8.0% | Stable |
| TZ | High (>92%) | 582 | 528 | -9.3% | Stable |
| TO | Medium (>85%) | 427 | 450 | +5.4% | Stable |
| TK | High (>92%) | 399 | 345 | -13.5% | Stable |
| TV | High (>92%) | 331 | 379 | +14.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TK | ↓ -3.57% | paypal -11.1% | Braintree -5.3% | Insufficient Funds +2.37pp | paypal + Braintree + Insufficient |
| TV | ↓ -2.78% | credit_card -5.1% | → Stable | Insufficient Funds +2.33pp | credit_card + Insufficient |

---

*Report: 2026-04-27*
