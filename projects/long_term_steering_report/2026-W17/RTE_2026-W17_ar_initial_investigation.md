# AR Initial (LL0) Investigation: RTE 2026-W17

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 92.41% → 93.2% (+0.85%)  
**Volume:** 30,640 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) improved from 92.41% to 93.2% (+0.85pp) in W17, with the change flagged as not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | Within normal range (+0.85%) | +0.79pp | ✅ |
| L1: Country Breakdown | 2 countries exceed ±2.5% threshold | TK -3.57%, TV -2.78% | ⚠️ |
| L1: Dimension Scan | All payment methods/providers stable | <1% variance | ✅ |
| L2: TK Deep-Dive | Braintree + PayPal decline spike | Insufficient Funds +2.37pp | ⚠️ |
| L2: TV Deep-Dive | Credit card decline spike | Insufficient Funds +2.33pp | ⚠️ |
| L3: Related Metrics | All funnel metrics improving consistently | +0.81% to +0.85% | ✅ |
| Mix Shift | No significant volume shifts impacting rate | All stable | ✅ |

**Key Findings:**
- TK experienced a -3.57% AR decline driven by PayPal (-11.11%) and Braintree (-5.34%), with Insufficient Funds increasing by +2.37pp
- TV declined -2.78% primarily due to credit card performance (-5.06%), also linked to Insufficient Funds rising +2.33pp
- Both flagged countries have relatively small volumes (TK: 345, TV: 379) representing ~2.4% of total volume
- The 8-week trend shows steady recovery from W13 low (91.39%) to current W17 high (93.2%)
- All related funnel metrics (FirstRunAR, PostDunningAR, PaymentApprovalRate) show aligned improvement of +0.81% to +0.85%

**Action:** Monitor - Overall metric is improving and not significant. Continue tracking TK and TV for Insufficient Funds trends, but no escalation required given low volume impact.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 93.2% | 30,640 | +0.85% ← REPORTED CHANGE |
| 2026-W16 | 92.41% | 30,922 | +0.81% |
| 2026-W15 | 91.67% | 29,087 | +0.84% |
| 2026-W14 | 90.91% | 31,920 | -0.53% |
| 2026-W13 | 91.39% | 36,392 | -1.26% |
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
| FJ | 93.07% | 92.34% | +0.79% | 18,625 |  |
| YE | 90.25% | 88.87% | +1.55% | 3,435 |  |
| CF | 95.31% | 93.54% | +1.89% | 6,338 |  |

**Countries exceeding ±2.5% threshold:** TK, TV

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 96.65% | 96.51% | +0.15% | 3,735 |  |
| Apple Pay | 92.02% | 91.66% | +0.39% | 6,215 |  |
| Others | 93.34% | 92.61% | +0.79% | 12,132 |  |
| Credit Card | 92.35% | 91.44% | +0.99% | 8,558 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 91.89% | +nan% | 0 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 35 |  |
| Braintree | 93.61% | 93.37% | +0.26% | 10,116 |  |
| Unknown | 92.8% | 91.77% | +1.13% | 11,031 |  |
| Adyen | 93.19% | 92.02% | +1.28% | 9,458 |  |

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
| 1_FirstRunAR | 90.7% | 89.94% | +0.85% | 30,640 | 30,922 |  |
| 2_PreDunningAR | 93.2% | 92.41% | +0.85% | 30,640 | 30,922 |  |
| 3_PostDunningAR | 93.44% | 92.69% | +0.81% | 30,640 | 30,922 |  |
| 6_PaymentApprovalRate | 93.62% | 92.85% | +0.83% | 30,640 | 30,922 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 18,970 | 18,625 | -1.8% | Stable |
| CF | High (>92%) | 6,535 | 6,338 | -3.0% | Stable |
| YE | Medium (>85%) | 3,091 | 3,435 | +11.1% | Stable |
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

*Report: 2026-04-28*
