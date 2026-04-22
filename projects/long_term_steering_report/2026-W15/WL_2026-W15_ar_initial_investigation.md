# AR Initial (LL0) Investigation: WL 2026-W15

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 91.05% → 91.28% (+0.25%)  
**Volume:** 13,021 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) improved from 91.05% to 91.28% (+0.23pp) in 2026-W15, a statistically non-significant change with volume of 13,021 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Within normal volatility (range: 89.22%-91.98%) | +0.25% | ✅ |
| L1: Country Variance | 2 countries exceed ±2.5% threshold (ER, MR) | ER +2.77%, MR +5.19% | ⚠️ |
| L1: PaymentMethod | "Others" segment shows anomaly | +8.74% | ⚠️ |
| L1: PaymentProvider | "Unknown" segment shows anomaly | +27.03% | ⚠️ |
| L2: ER Deep-Dive | Improvement driven by decline reason shifts | Insufficient Funds -1.74pp | ✅ |
| L2: MR Deep-Dive | Volume shift to "Unknown" provider (4→588) | Insufficient Funds -3.16pp | ⚠️ |
| L3: Related Metrics | All funnel stages improved consistently | +1.35% to +2.28% | ✅ |
| Mix Shift | No significant tier migration | All stable | ✅ |

**Key Findings:**
- MR showed the largest improvement (+5.19pp) driven by a 3.16pp reduction in "Insufficient Funds" declines and a significant volume shift to "Unknown" provider (from 4 to 588 transactions)
- ER improved by +2.77pp primarily due to reduced "Insufficient Funds" declines (-1.74pp) and "Refused" declines (-0.94pp)
- The "Unknown" PaymentProvider segment at aggregate level jumped from 76.92% to 97.71% (+27.03pp), correlating with MR's volume shift
- Related metrics show consistent improvement across the funnel: FirstRunAR (+2.28%), PreDunningAR (+1.36%), PostDunningAR (+1.35%)
- Overall volume declined 10.5% WoW (from 12,774 to 11,583 orders) across most countries

**Action:** Monitor - The improvement is positive but the MR volume shift to "Unknown" provider warrants tracking over the next 2-3 weeks to confirm this is intentional routing and not a data classification issue.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 91.28% | 13,021 | +0.25% |
| 2026-W15 | 91.05% | 11,583 | +1.37% ← REPORTED CHANGE |
| 2026-W14 | 89.82% | 12,774 | +0.67% |
| 2026-W13 | 89.22% | 12,902 | -1.40% |
| 2026-W12 | 90.49% | 13,905 | -1.62% |
| 2026-W11 | 91.98% | 14,300 | +1.09% |
| 2026-W10 | 90.99% | 14,879 | -0.32% |
| 2026-W09 | 91.28% | 15,292 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| GN | 89.48% | 88.65% | +0.94% | 1,065 |  |
| CK | 88.57% | 87.68% | +1.01% | 1,959 |  |
| ER | 86.87% | 84.53% | +2.77% | 2,048 | ⚠️ |
| MR | 93.06% | 88.47% | +5.19% | 1,932 | ⚠️ |

**Countries exceeding ±2.5% threshold:** ER, MR

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 90.73% | 90.91% | -0.20% | 3,311 |  |
| Paypal | 95.37% | 94.87% | +0.53% | 1,317 |  |
| Credit Card | 89.58% | 88.13% | +1.64% | 6,266 |  |
| Others | 97.68% | 89.83% | +8.74% | 689 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 11 |  |
| Braintree | 93.08% | 92.78% | +0.33% | 5,537 |  |
| Adyen | 86.29% | 84.72% | +1.86% | 2,108 |  |
| ProcessOut | 89.3% | 87.59% | +1.95% | 3,271 |  |
| Unknown | 97.71% | 76.92% | +27.03% | 656 | ⚠️ |

---

## L2: ER Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 5 | 0 |  |
| None | 0.00% | 0.00% | +0.00% | 0 | 3 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 2 | 4 |  |
| applepay | 88.25% | 86.51% | +2.01% | 630 | 734 |  |
| credit_card | 84.78% | 82.24% | +3.10% | 1,183 | 1,306 |  |
| paypal | 95.61% | 91.70% | +4.27% | 228 | 241 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 0.00% | +0.00% | 5 | 3 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 2 | 4 |  |
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
| None | 99.83% | 0.00% | +0.00% | 589 | 0 |  |
| None | 0.00% | 100.00% | -100.00% | 0 | 5 | ⚠️ |
| venmo | 0.00% | 100.00% | -100.00% | 0 | 1 | ⚠️ |
| applepay | 90.57% | 91.56% | -1.08% | 318 | 533 |  |
| paypal | 98.72% | 97.19% | +1.57% | 156 | 285 |  |
| credit_card | 88.38% | 85.28% | +3.63% | 869 | 1,318 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| No Payment | 0.00% | 100.00% | -100.00% | 0 | 1 | ⚠️ |
| Unknown | 100.00% | 100.00% | +0.00% | 588 | 4 |  |
| Braintree | 87.84% | 86.47% | +1.59% | 510 | 894 |  |
| ProcessOut | 91.37% | 89.86% | +1.67% | 834 | 1,243 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,798 | 1,895 | 93.06% | 88.47% | +4.60 |
| Insufficient Funds | 76 | 152 | 3.93% | 7.10% | -3.16 |
| Other reasons | 40 | 69 | 2.07% | 3.22% | -1.15 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 17 | 26 | 0.88% | 1.21% | -0.33 |
| State_failed | 1 | 0 | 0.05% | 0.00% | +0.05 |

**Root Cause:** None + No + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.34% | 86.38% | +2.28% | 11,583 | 12,774 |  |
| 2_PreDunningAR | 91.05% | 89.82% | +1.36% | 11,583 | 12,774 |  |
| 3_PostDunningAR | 91.31% | 90.09% | +1.35% | 11,583 | 12,774 |  |
| 6_PaymentApprovalRate | 91.46% | 90.23% | +1.36% | 11,583 | 12,774 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| KN | High (>92%) | 2,455 | 2,023 | -17.6% | Stable |
| ER | Low (>85%) | 2,288 | 2,048 | -10.5% | Stable |
| MR | Medium (>85%) | 2,142 | 1,932 | -9.8% | Stable |
| CG | High (>92%) | 1,952 | 1,830 | -6.3% | Stable |
| CK | Medium (>85%) | 1,810 | 1,959 | +8.2% | Stable |
| GN | Medium (>85%) | 1,286 | 1,065 | -17.2% | Stable |
| AO | Low (>85%) | 841 | 726 | -13.7% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| ER | ↑ +2.77% | → Stable | → Stable | Insufficient Funds -1.74pp | Insufficient |
| MR | ↑ +5.19% | None -100.0% | No Payment -100.0% | Insufficient Funds -3.16pp | None + No + Insufficient |

---

*Report: 2026-04-22*
