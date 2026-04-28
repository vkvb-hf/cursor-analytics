# AR Initial (LL0) Investigation: WL 2026-W17

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 91.27% → 92.15% (+0.96%)  
**Volume:** 11,546 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Pre-Dunning Acceptance Rate (Initial Charges) improved from 91.27% to 92.15% (+0.96%) in W17, a positive but not statistically significant change, with volume decreasing from 13,017 to 11,546 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (89.22%-92.15%) | +0.96% | ✅ |
| L1: Country Breakdown | 1 country exceeds ±2.5% threshold (ER) | +2.53% | ⚠️ |
| L1: Dimension Scan | No payment methods/providers exceed threshold | <1.5% | ✅ |
| L2: ER Deep-Dive | ProcessOut volume dropped to 0; Unknown provider +6.30% | Mixed | ⚠️ |
| L3: Related Metrics | All funnel metrics improved consistently | +0.22% to +0.96% | ✅ |
| Mix Shift | All countries stable despite volume shifts | -19.1% to +6.9% | ✅ |

**Key Findings:**
- ER showed the largest improvement (+2.53%), driven by a +6.30% increase in Unknown provider acceptance rate and reduced Insufficient Funds declines (-1.73pp)
- ProcessOut payment provider completely exited ER (55 → 0 volume), which may have positively impacted overall rates as it had 89.09% acceptance
- Credit card payments in ER dropped significantly in both volume (76 → 18) and rate (-18.08%), flagged as anomaly
- All related metrics (FirstRunAR, PreDunningAR, PostDunningAR, PaymentApprovalRate) moved in the same positive direction, indicating consistent improvement across the funnel
- Overall volume declined 11.3% week-over-week across all major countries, with MR (-19.1%) and KN (-18.0%) seeing the largest drops

**Action:** Monitor - The improvement is positive but not significant. Continue tracking ER's payment provider migration from ProcessOut and the credit card volume decline to ensure these shifts don't reverse the gains.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 92.15% | 11,546 | +0.96% ← REPORTED CHANGE |
| 2026-W16 | 91.27% | 13,017 | +0.26% |
| 2026-W15 | 91.03% | 11,577 | +1.35% |
| 2026-W14 | 89.82% | 12,769 | +0.67% |
| 2026-W13 | 89.22% | 12,902 | -1.40% |
| 2026-W12 | 90.49% | 13,904 | -1.61% |
| 2026-W11 | 91.97% | 14,300 | +1.08% |
| 2026-W10 | 90.99% | 14,879 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| GN | 94.07% | 93.10% | +1.04% | 1,333 |  |
| CK | 85.94% | 84.95% | +1.16% | 1,934 |  |
| MR | 97.01% | 94.95% | +2.16% | 1,972 |  |
| ER | 88.51% | 86.33% | +2.53% | 1,924 | ⚠️ |

**Countries exceeding ±2.5% threshold:** ER

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 92.77% | 92.76% | +0.01% | 3,747 |  |
| Credit Card | 88.38% | 87.55% | +0.94% | 3,261 |  |
| Apple Pay | 93.91% | 92.56% | +1.46% | 3,216 |  |
| Paypal | 95.46% | 94.09% | +1.46% | 1,322 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 84.86% | +nan% | 0 |  |
| Unknown | 92.69% | 92.69% | +0.00% | 3,681 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 15 |  |
| Adyen | 84.74% | 84.5% | +0.28% | 2,208 |  |
| Braintree | 94.68% | 93.34% | +1.43% | 5,642 |  |

---

## L2: ER Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 88.39% | 0.00% | +0.00% | 1,051 | 0 |  |
| venmo | 100.00% | 0.00% | +0.00% | 2 | 0 |  |
| None | 0.00% | 83.15% | -100.00% | 0 | 1,116 | ⚠️ |
| credit_card | 72.22% | 88.16% | -18.08% | 18 | 76 | ⚠️ |
| applepay | 88.09% | 89.38% | -1.44% | 613 | 659 |  |
| paypal | 91.14% | 92.34% | -1.30% | 237 | 222 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 3 | 5 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| ProcessOut | 0.00% | 89.09% | -100.00% | 0 | 55 | ⚠️ |
| Braintree | 88.62% | 90.02% | -1.56% | 870 | 902 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 3 | 5 |  |
| Unknown | 88.39% | 83.15% | +6.30% | 1,051 | 1,116 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,703 | 1,794 | 88.51% | 86.33% | +2.18 |
| Insufficient Funds | 137 | 184 | 7.12% | 8.85% | -1.73 |
| Other reasons | 44 | 71 | 2.29% | 3.42% | -1.13 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 37 | 28 | 1.92% | 1.35% | +0.58 |
| Unknown | 3 | 1 | 0.16% | 0.05% | +0.11 |

**Root Cause:** None + ProcessOut + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 89.46% | 89.26% | +0.22% | 11,546 | 13,017 |  |
| 2_PreDunningAR | 92.15% | 91.27% | +0.96% | 11,546 | 13,017 |  |
| 3_PostDunningAR | 92.27% | 91.53% | +0.81% | 11,546 | 13,017 |  |
| 6_PaymentApprovalRate | 92.39% | 91.7% | +0.75% | 11,546 | 13,017 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| MR | High (>92%) | 2,437 | 1,972 | -19.1% | Stable |
| KN | High (>92%) | 2,393 | 1,963 | -18.0% | Stable |
| CK | Low (>85%) | 2,299 | 1,934 | -15.9% | Stable |
| ER | Medium (>85%) | 2,078 | 1,924 | -7.4% | Stable |
| CG | High (>92%) | 1,837 | 1,690 | -8.0% | Stable |
| GN | High (>92%) | 1,290 | 1,333 | +3.3% | Stable |
| AO | Low (>85%) | 683 | 730 | +6.9% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| ER | ↑ +2.53% | None -100.0% | ProcessOut -100.0% | Insufficient Funds -1.73pp | None + ProcessOut + Insufficient |

---

*Report: 2026-04-28*
