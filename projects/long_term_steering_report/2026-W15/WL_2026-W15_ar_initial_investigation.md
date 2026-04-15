# AR Initial (LL0) Investigation: WL 2026-W15

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 89.83% → 91.04% (+1.35%)  
**Volume:** 11,587 orders  
**Significance:** Significant

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) improved significantly from 89.83% to 91.04% (+1.35%) in W15, driven primarily by reduced Insufficient Funds declines in ER and MR markets.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (90.74%-91.99%) | +1.35% | ✅ |
| L1: Country Breakdown | 2 countries exceed ±2.5% threshold | ER +2.77%, MR +5.15% | ⚠️ |
| L1: PaymentMethod | "Others" shows anomalous change | +8.74% | ⚠️ |
| L1: PaymentProvider | "Unknown" shows anomalous change | +27.03% | ⚠️ |
| L2: ER Deep-Dive | Insufficient Funds decline | -1.74pp | ✅ |
| L2: MR Deep-Dive | Insufficient Funds decline + volume shift to Unknown provider | -3.17pp | ⚠️ |
| L3: Related Metrics | All funnel metrics improved consistently | +1.34% to +2.27% | ✅ |
| Mix Shift | All countries stable impact | No significant shifts | ✅ |

**Key Findings:**
- MR showed the largest improvement (+5.15%) with Insufficient Funds declines dropping by 3.17pp (from 7.10% to 3.93%), accompanied by a significant volume shift to "Unknown" provider (4 → 588 orders)
- ER improved by +2.77% primarily due to Insufficient Funds declines decreasing by 1.74pp (from 10.14% to 8.40%)
- Overall volume declined 9.3% (12,773 → 11,587 orders), continuing an 8-week downward trend from 15,382 orders in W08
- The "Unknown" PaymentProvider category showed a +27.03% rate change with volume increasing from ~50 to 656 orders, indicating potential data classification changes
- All related funnel metrics (FirstRunAR, PostDunningAR, PaymentApprovalRate) improved in parallel, confirming genuine acceptance rate improvement

**Action:** Monitor - The improvement is positive and driven by legitimate decline reason reductions. However, investigate the MR "Unknown" provider volume spike (4 → 588) to ensure proper payment provider attribution and data quality.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 91.04% | 11,587 | +1.35% ← REPORTED CHANGE |
| 2026-W14 | 89.83% | 12,773 | +0.68% |
| 2026-W13 | 89.22% | 12,902 | -1.40% |
| 2026-W12 | 90.49% | 13,906 | -1.63% |
| 2026-W11 | 91.99% | 14,300 | +1.10% |
| 2026-W10 | 90.99% | 14,879 | -0.32% |
| 2026-W09 | 91.28% | 15,292 | +0.60% |
| 2026-W08 | 90.74% | 15,382 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| GN | 89.48% | 88.65% | +0.94% | 1,065 |  |
| CK | 88.53% | 87.68% | +0.97% | 1,961 |  |
| ER | 86.87% | 84.53% | +2.77% | 2,048 | ⚠️ |
| MR | 93.06% | 88.51% | +5.15% | 1,932 | ⚠️ |

**Countries exceeding ±2.5% threshold:** ER, MR

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 90.73% | 90.91% | -0.20% | 3,311 |  |
| Paypal | 95.37% | 94.87% | +0.53% | 1,318 |  |
| Credit Card | 89.57% | 88.14% | +1.61% | 6,269 |  |
| Others | 97.68% | 89.83% | +8.74% | 689 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 11 |  |
| Braintree | 93.08% | 92.78% | +0.33% | 5,538 |  |
| Adyen | 86.25% | 84.72% | +1.81% | 2,109 |  |
| ProcessOut | 89.31% | 87.61% | +1.93% | 3,273 |  |
| Unknown | 97.71% | 76.92% | +27.03% | 656 | ⚠️ |

---

## L2: ER Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.0% | 0.0% | +0.00% | 5 | 0 |  |
| None | 0.0% | 0.0% | +0.00% | 0 | 3 |  |
| cashcredit | 100.0% | 100.0% | +0.00% | 2 | 4 |  |
| applepay | 88.25% | 86.51% | +2.01% | 630 | 734 |  |
| credit_card | 84.78% | 82.24% | +3.10% | 1,183 | 1,306 |  |
| paypal | 95.61% | 91.7% | +4.27% | 228 | 241 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.0% | 0.0% | +0.00% | 5 | 3 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 2 | 4 |  |
| Braintree | 89.94% | 87.68% | +2.59% | 885 | 998 |  |
| ProcessOut | 84.86% | 82.23% | +3.20% | 1,156 | 1,283 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,779 | 1,934 | 86.87% | 84.53% | +2.34 |
| Insufficient Funds | 172 | 232 | 8.40% | 10.14% | -1.74 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 22 | 46 | 1.07% | 2.01% | -0.94 |
| Other reasons | 70 | 73 | 3.42% | 3.19% | +0.23 |
| Unknown | 5 | 2 | 0.24% | 0.09% | +0.16 |
| PROVIDER_ERROR: failure executing charge with provider | 0 | 1 | 0.00% | 0.04% | -0.04 |

**Root Cause:** Insufficient

---

## L2: MR Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 99.83% | 0.0% | +0.00% | 589 | 0 |  |
| None | 0.0% | 100.0% | -100.00% | 0 | 5 | ⚠️ |
| venmo | 0.0% | 100.0% | -100.00% | 0 | 1 | ⚠️ |
| applepay | 90.57% | 91.56% | -1.08% | 318 | 533 |  |
| paypal | 98.72% | 97.19% | +1.57% | 156 | 285 |  |
| credit_card | 88.38% | 85.35% | +3.55% | 869 | 1,317 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| No Payment | 0.0% | 100.0% | -100.00% | 0 | 1 | ⚠️ |
| Unknown | 100.0% | 100.0% | +0.00% | 588 | 4 |  |
| Braintree | 87.84% | 86.47% | +1.59% | 510 | 894 |  |
| ProcessOut | 91.37% | 89.94% | +1.59% | 834 | 1,242 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,798 | 1,895 | 93.06% | 88.51% | +4.55 |
| Insufficient Funds | 76 | 152 | 3.93% | 7.10% | -3.17 |
| Other reasons | 40 | 68 | 2.07% | 3.18% | -1.11 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 17 | 26 | 0.88% | 1.21% | -0.33 |
| State_failed | 1 | 0 | 0.05% | 0.00% | +0.05 |

**Root Cause:** None + No + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.35% | 86.39% | +2.27% | 11,587 | 12,773 |  |
| 2_PreDunningAR | 91.04% | 89.83% | +1.35% | 11,587 | 12,773 |  |
| 3_PostDunningAR | 91.29% | 90.08% | +1.34% | 11,587 | 12,773 |  |
| 6_PaymentApprovalRate | 91.46% | 90.23% | +1.36% | 11,587 | 12,773 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| KN | High (>92%) | 2,455 | 2,023 | -17.6% | Stable |
| ER | Low (>85%) | 2,288 | 2,048 | -10.5% | Stable |
| MR | Medium (>85%) | 2,141 | 1,932 | -9.8% | Stable |
| CG | High (>92%) | 1,952 | 1,832 | -6.1% | Stable |
| CK | Medium (>85%) | 1,810 | 1,961 | +8.3% | Stable |
| GN | Medium (>85%) | 1,286 | 1,065 | -17.2% | Stable |
| AO | Low (>85%) | 841 | 726 | -13.7% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| ER | ↑ +2.77% | → Stable | → Stable | Insufficient Funds -1.74pp | Insufficient |
| MR | ↑ +5.15% | None -100.0% | No Payment -100.0% | Insufficient Funds -3.17pp | None + No + Insufficient |

---

*Report: 2026-04-15*
