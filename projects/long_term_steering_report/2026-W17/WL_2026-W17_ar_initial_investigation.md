# AR Initial (LL0) Investigation: WL 2026-W17

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 91.28% → 92.13% (+0.93%)  
**Volume:** 11,550 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) improved from 91.28% to 92.13% (+0.93%) in W17, a positive but not statistically significant change within normal operating variance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (89.22%-92.13%) | +0.93% | ✅ |
| L1: Country Breakdown | 1 country (ER) exceeded ±2.5% threshold | +2.53% (ER) | ⚠️ |
| L1: Dimension Scan | All PaymentMethods and Providers within tolerance | <±1.5% | ✅ |
| L2: ER Deep-Dive | ProcessOut volume dropped to 0; Unknown provider +6.33% | Mixed signals | ⚠️ |
| L3: Related Metrics | All funnel metrics improved consistently | +0.21% to +0.93% | ✅ |
| Mix Shift | All countries stable despite volume declines | No impact | ✅ |

**Key Findings:**
- ER showed the largest improvement (+2.53%), driven by a +6.33% increase in Unknown payment provider performance and a -1.74pp reduction in Insufficient Funds declines
- ProcessOut provider volume dropped to 0 in ER (from 56 transactions), indicating a potential provider migration or technical issue
- Overall volume decreased 11.3% WoW (13,019 → 11,550), but acceptance rates improved across all related metrics (FirstRunAR, PreDunningAR, PostDunningAR, PaymentApprovalRate)
- Credit card transactions in ER showed concerning decline (-18.22%), though on very low volume (18 transactions)
- The "None" payment method appeared with 1,053 volume in ER (previously 0), suggesting a data classification change

**Action:** Monitor - The improvement is positive and within normal variance. Continue tracking ER's ProcessOut migration and the emergence of "None" payment method classification to ensure data integrity.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 92.13% | 11,550 | +0.93% ← REPORTED CHANGE |
| 2026-W16 | 91.28% | 13,019 | +0.27% |
| 2026-W15 | 91.03% | 11,579 | +1.34% |
| 2026-W14 | 89.83% | 12,770 | +0.68% |
| 2026-W13 | 89.22% | 12,902 | -1.40% |
| 2026-W12 | 90.49% | 13,905 | -1.61% |
| 2026-W11 | 91.97% | 14,300 | +1.08% |
| 2026-W10 | 90.99% | 14,879 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CK | 85.85% | 85.00% | +1.01% | 1,937 |  |
| GN | 94.07% | 93.10% | +1.04% | 1,333 |  |
| MR | 97.01% | 94.95% | +2.16% | 1,971 |  |
| ER | 88.53% | 86.34% | +2.53% | 1,926 | ⚠️ |

**Countries exceeding ±2.5% threshold:** ER

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 92.75% | 92.76% | -0.01% | 3,750 |  |
| Credit Card | 88.37% | 87.56% | +0.93% | 3,260 |  |
| Paypal | 95.39% | 94.16% | +1.30% | 1,324 |  |
| Apple Pay | 93.87% | 92.56% | +1.42% | 3,216 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 84.91% | +nan% | 0 |  |
| Unknown | 92.66% | 92.69% | -0.04% | 3,678 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 15 |  |
| Adyen | 84.72% | 84.51% | +0.25% | 2,206 |  |
| Braintree | 94.66% | 93.36% | +1.39% | 5,651 |  |

---

## L2: ER Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 88.41% | 0.00% | +0.00% | 1,053 | 0 |  |
| venmo | 100.00% | 0.00% | +0.00% | 2 | 0 |  |
| None | 0.00% | 83.15% | -100.00% | 0 | 1,116 | ⚠️ |
| credit_card | 72.22% | 88.31% | -18.22% | 18 | 77 | ⚠️ |
| applepay | 88.09% | 89.38% | -1.44% | 613 | 659 |  |
| paypal | 91.14% | 92.34% | -1.30% | 237 | 222 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 3 | 5 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| ProcessOut | 0.00% | 89.29% | -100.00% | 0 | 56 | ⚠️ |
| Braintree | 88.62% | 90.02% | -1.56% | 870 | 902 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 3 | 5 |  |
| Unknown | 88.41% | 83.15% | +6.33% | 1,053 | 1,116 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,705 | 1,795 | 88.53% | 86.34% | +2.19 |
| Insufficient Funds | 137 | 184 | 7.11% | 8.85% | -1.74 |
| Other reasons | 44 | 71 | 2.28% | 3.42% | -1.13 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 37 | 28 | 1.92% | 1.35% | +0.57 |
| Unknown | 3 | 1 | 0.16% | 0.05% | +0.11 |

**Root Cause:** None + ProcessOut + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 89.45% | 89.26% | +0.21% | 11,550 | 13,019 |  |
| 2_PreDunningAR | 92.13% | 91.28% | +0.93% | 11,550 | 13,019 |  |
| 3_PostDunningAR | 92.23% | 91.53% | +0.77% | 11,550 | 13,019 |  |
| 6_PaymentApprovalRate | 92.39% | 91.7% | +0.76% | 11,550 | 13,019 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| MR | High (>92%) | 2,437 | 1,971 | -19.1% | Stable |
| KN | High (>92%) | 2,393 | 1,963 | -18.0% | Stable |
| CK | Low (>85%) | 2,300 | 1,937 | -15.8% | Stable |
| ER | Medium (>85%) | 2,079 | 1,926 | -7.4% | Stable |
| CG | High (>92%) | 1,837 | 1,690 | -8.0% | Stable |
| GN | High (>92%) | 1,290 | 1,333 | +3.3% | Stable |
| AO | Low (>85%) | 683 | 730 | +6.9% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| ER | ↑ +2.53% | None -100.0% | ProcessOut -100.0% | Insufficient Funds -1.74pp | None + ProcessOut + Insufficient |

---

*Report: 2026-04-27*
