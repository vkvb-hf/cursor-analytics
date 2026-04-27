# AR Initial (LL0) Investigation: HF-INTL 2026-W17

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 91.38% → 91.82% (+0.48%)  
**Volume:** 33,407 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate for HF-INTL improved slightly from 91.38% to 91.82% (+0.44pp) in W17, a change that is not statistically significant given the volume of 33,407 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (89.78%-91.82%) | +0.44pp | ✅ |
| L1: Country Breakdown | 3 countries exceed ±2.5% threshold (LU, CH, NZ) | LU -7.94%, CH -6.35%, NZ +5.68% | ⚠️ |
| L1: Dimension Scan | Credit Card payment method declined significantly | -5.25% | ⚠️ |
| L2: LU Deep-Dive | Apple Pay and Braintree underperforming | Braintree -12.36% | ⚠️ |
| L2: CH Deep-Dive | PayPal and Braintree declining | Braintree -11.59% | ⚠️ |
| L2: NZ Deep-Dive | ProcessOut volume dropped to zero; Unknown provider absorbed volume | ProcessOut -100% | ⚠️ |
| L3: Related Metrics | All funnel metrics improved consistently | +0.48% to +0.74% | ✅ |

**Key Findings:**
- LU experienced a -7.94% AR decline driven by Apple Pay (-22.38%) and Braintree (-12.36%), with Insufficient Funds increasing by +3.04pp
- CH declined -6.35% with Braintree down -11.59% and Insufficient Funds up +4.29pp, suggesting regional payment processing issues
- NZ improved +5.68% despite ProcessOut volume dropping to zero; traffic shifted to Unknown provider which improved +8.63%
- Credit Card as a payment method declined -5.25% globally (334 volume), though low volume limits impact
- FR volume dropped significantly (-23.6%) but maintained high AR tier performance, creating favorable mix shift

**Action:** Monitor – The overall metric change is not significant and the trend remains stable. Continue tracking LU and CH for Braintree/Insufficient Funds patterns over the next 2 weeks. No immediate escalation required.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 91.82% | 33,407 | +0.48% ← REPORTED CHANGE |
| 2026-W16 | 91.38% | 35,017 | -0.36% |
| 2026-W15 | 91.71% | 27,397 | +2.15% |
| 2026-W14 | 89.78% | 30,611 | -0.40% |
| 2026-W13 | 90.14% | 34,367 | -1.12% |
| 2026-W12 | 91.16% | 38,925 | -0.35% |
| 2026-W11 | 91.48% | 42,589 | +1.21% |
| 2026-W10 | 90.39% | 47,512 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| LU | 82.05% | 89.13% | -7.94% | 78 | ⚠️ |
| CH | 83.94% | 89.63% | -6.35% | 137 | ⚠️ |
| SE | 92.20% | 93.75% | -1.66% | 1,320 |  |
| GB | 92.17% | 90.65% | +1.67% | 9,050 |  |
| FR | 95.10% | 93.40% | +1.82% | 5,466 |  |
| NZ | 73.21% | 69.28% | +5.68% | 810 | ⚠️ |

**Countries exceeding ±2.5% threshold:** LU, CH, NZ

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 83.53% | 88.16% | -5.25% | 334 | ⚠️ |
| Paypal | 95.55% | 96.31% | -0.78% | 6,631 |  |
| Others | 91.47% | 91.73% | -0.29% | 17,378 |  |
| Apple Pay | 90.06% | 89.2% | +0.97% | 9,064 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 87.8% | +nan% | 0 |  |
| Braintree | 92.38% | 92.54% | -0.17% | 15,695 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 89 |  |
| Unknown | 90.27% | 90.03% | +0.26% | 14,653 |  |
| Adyen | 96.23% | 95.87% | +0.37% | 2,970 |  |

---

## L2: LU Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 100.00% | 0.00% | +0.00% | 5 | 0 |  |
| None | 0.00% | 91.67% | -100.00% | 0 | 12 | ⚠️ |
| applepay | 69.23% | 89.19% | -22.38% | 26 | 37 | ⚠️ |
| credit_card | 80.00% | 85.29% | -6.21% | 30 | 34 | ⚠️ |
| paypal | 100.00% | 100.00% | +0.00% | 13 | 6 |  |
| sepadirectdebit | 100.00% | 100.00% | +0.00% | 4 | 3 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| ProcessOut | 0.00% | 100.00% | -100.00% | 0 | 1 | ⚠️ |
| Braintree | 79.49% | 90.70% | -12.36% | 39 | 43 | ⚠️ |
| Adyen | 82.35% | 86.11% | -4.36% | 34 | 36 |  |
| Unknown | 100.00% | 91.67% | +9.09% | 5 | 12 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 64 | 82 | 82.05% | 89.13% | -7.08 |
| Insufficient Funds | 10 | 9 | 12.82% | 9.78% | +3.04 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 2 | 0 | 2.56% | 0.00% | +2.56 |
| Other reasons | 2 | 1 | 2.56% | 1.09% | +1.48 |

**Root Cause:** None + ProcessOut + Insufficient

---

## L2: CH Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 87.50% | 0.00% | +0.00% | 72 | 0 |  |
| None | 0.00% | 89.55% | -100.00% | 0 | 67 | ⚠️ |
| paypal | 72.22% | 89.47% | -19.28% | 18 | 19 | ⚠️ |
| applepay | 81.82% | 89.36% | -8.44% | 44 | 47 | ⚠️ |
| cashcredit | 100.00% | 100.00% | +0.00% | 1 | 1 |  |
| credit_card | 100.00% | 100.00% | +0.00% | 2 | 1 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Braintree | 79.03% | 89.39% | -11.59% | 62 | 66 | ⚠️ |
| Unknown | 87.50% | 89.55% | -2.29% | 72 | 67 |  |
| Adyen | 100.00% | 100.00% | +0.00% | 2 | 1 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 1 | 1 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 115 | 121 | 83.94% | 89.63% | -5.69 |
| Insufficient Funds | 14 | 8 | 10.22% | 5.93% | +4.29 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 5 | 3 | 3.65% | 2.22% | +1.43 |
| Other reasons | 3 | 3 | 2.19% | 2.22% | -0.03 |

**Root Cause:** None + Braintree + Insufficient

---

## L2: NZ Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 73.99% | 0.00% | +0.00% | 765 | 0 |  |
| None | 0.00% | 68.12% | -100.00% | 0 | 229 | ⚠️ |
| applepay | 0.00% | 70.70% | -100.00% | 0 | 157 | ⚠️ |
| paypal | 53.85% | 58.62% | -8.14% | 26 | 29 | ⚠️ |
| credit_card | 66.67% | 69.98% | -4.73% | 18 | 453 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 1 | 1 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| ProcessOut | 0.00% | 70.00% | -100.00% | 0 | 600 | ⚠️ |
| Adyen | 72.73% | 81.82% | -11.11% | 22 | 11 | ⚠️ |
| Braintree | 53.85% | 58.62% | -8.14% | 26 | 29 | ⚠️ |
| No Payment | 100.00% | 100.00% | +0.00% | 1 | 1 |  |
| Unknown | 73.85% | 67.98% | +8.63% | 761 | 228 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 593 | 602 | 73.21% | 69.28% | +3.93 |
| Insufficient Funds | 186 | 229 | 22.96% | 26.35% | -3.39 |
| Unknown | 0 | 3 | 0.00% | 0.35% | -0.35 |
| Other reasons | 19 | 23 | 2.35% | 2.65% | -0.30 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 12 | 12 | 1.48% | 1.38% | +0.10 |

**Root Cause:** None + ProcessOut + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 89.76% | 89.1% | +0.74% | 33,407 | 35,017 |  |
| 2_PreDunningAR | 91.82% | 91.38% | +0.48% | 33,407 | 35,017 |  |
| 3_PostDunningAR | 92.31% | 91.79% | +0.56% | 33,407 | 35,017 |  |
| 6_PaymentApprovalRate | 92.73% | 92.18% | +0.60% | 33,407 | 35,017 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | Medium (>85%) | 8,688 | 9,050 | +4.2% | Stable |
| FR | High (>92%) | 7,153 | 5,466 | -23.6% | ⚠️ Volume drop |
| DE | High (>92%) | 7,101 | 6,891 | -3.0% | Stable |
| AU | Low (>85%) | 2,643 | 2,684 | +1.6% | Stable |
| BE | High (>92%) | 1,793 | 1,700 | -5.2% | Stable |
| NL | High (>92%) | 1,369 | 1,104 | -19.4% | Stable |
| IE | Medium (>85%) | 1,364 | 1,438 | +5.4% | Stable |
| DK | High (>92%) | 1,228 | 1,111 | -9.5% | Stable |
| SE | High (>92%) | 1,216 | 1,320 | +8.6% | Stable |
| NZ | Low (>85%) | 869 | 810 | -6.8% | Stable |
| NO | Medium (>85%) | 768 | 1,099 | +43.1% | Stable |
| AT | High (>92%) | 598 | 519 | -13.2% | Stable |
| CH | Medium (>85%) | 135 | 137 | +1.5% | Stable |
| LU | Medium (>85%) | 92 | 78 | -15.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| LU | ↓ -7.94% | None -100.0% | ProcessOut -100.0% | Insufficient Funds +3.04pp | None + ProcessOut + Insufficient |
| CH | ↓ -6.35% | None -100.0% | Braintree -11.6% | Insufficient Funds +4.29pp | None + Braintree + Insufficient |
| NZ | ↑ +5.68% | None -100.0% | ProcessOut -100.0% | Insufficient Funds -3.39pp | None + ProcessOut + Insufficient |

---

*Report: 2026-04-27*
