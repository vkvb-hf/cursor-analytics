# AR Initial (LL0) Investigation: WL 2026-W15

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 89.83% → 91.04% (+1.35%)  
**Volume:** 11,587 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** The Pre-Dunning Acceptance Rate (Initial Charges) improved from 89.83% to 91.04% (+1.35%) in 2026-W15, representing a significant positive movement with 11,587 orders processed.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (90.74%-91.99%) | +1.21pp | ✅ |
| L1: Country Breakdown | MR exceeds ±2.5% threshold | +4.84% | ⚠️ |
| L1: PaymentMethod | Others exceeds threshold | +8.74% | ⚠️ |
| L1: PaymentProvider | Unknown exceeds threshold | +27.03% | ⚠️ |
| L2: MR Deep-Dive | PaymentMethod shifts identified | None -100%, venmo -100% | ⚠️ |
| L3: Related Metrics | All funnel metrics improving consistently | +1.34% to +2.27% | ✅ |

**Key Findings:**
- MR drove significant improvement (+4.84%) with successful transactions increasing from 76.28% to 79.97% (+3.69pp), while "Insufficient Funds" declines dropped by 1.89pp
- The "Unknown" PaymentProvider segment showed a dramatic +27.03% increase (76.92% → 97.71%), though volume remains low at 656 orders
- "Others" PaymentMethod improved significantly (+8.74%) from 89.83% to 97.68% with 689 orders
- Volume declined 9.3% week-over-week (12,773 → 11,587), continuing a downward trend from 15,382 in W08
- All related metrics (1_FirstRunAR, 2_PreDunningAR, 3_PostDunningAR, 6_PaymentApprovalRate) show consistent improvement ranging from +1.34% to +2.27%

**Action:** Monitor - The improvement is positive and driven by genuine reduction in decline rates in MR, particularly "Insufficient Funds" (-1.89pp). Continue monitoring the "Unknown" PaymentProvider segment to ensure data quality, and track volume decline trends.

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
| GN | 78.65% | 79.7% | -1.32% | 1,527 |  |
| CK | 79.91% | 79.09% | +1.03% | 3,703 |  |
| ER | 64.45% | 62.95% | +2.38% | 4,529 |  |
| MR | 79.97% | 76.28% | +4.84% | 3,215 | ⚠️ |

**Countries exceeding ±2.5% threshold:** MR

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

## L2: MR Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 99.5% | 0.0% | +0.00% | 596 | 0 |  |
| cashcredit | 100.0% | 0.0% | +0.00% | 1 | 0 |  |
| None | 0.0% | 100.0% | -100.00% | 0 | 5 | ⚠️ |
| venmo | 0.0% | 100.0% | -100.00% | 1 | 1 | ⚠️ |
| applepay | 82.8% | 84.22% | -1.69% | 558 | 792 |  |
| credit_card | 70.93% | 71.54% | -0.85% | 1,789 | 2,326 |  |
| paypal | 91.11% | 86.87% | +4.89% | 270 | 434 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Braintree | 67.62% | 69.55% | -2.77% | 1,152 | 1,583 |  |
| Unknown | 99.66% | 100.0% | -0.34% | 595 | 4 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 1 | 1 |  |
| ProcessOut | 81.66% | 81.62% | +0.05% | 1,467 | 1,970 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 2,571 | 2,714 | 79.97% | 76.28% | +3.69 |
| Insufficient Funds | 232 | 324 | 7.22% | 9.11% | -1.89 |
| Other reasons | 169 | 240 | 5.26% | 6.75% | -1.49 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 240 | 280 | 7.47% | 7.87% | -0.40 |
| Unknown | 2 | 0 | 0.06% | 0.00% | +0.06 |
| State_failed | 1 | 0 | 0.03% | 0.00% | +0.03 |

**Root Cause:** None + Insufficient

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
| ER | Low (>85%) | 5,023 | 4,529 | -9.8% | Stable |
| MR | Low (>85%) | 3,558 | 3,215 | -9.6% | Stable |
| CK | Low (>85%) | 3,386 | 3,703 | +9.4% | Stable |
| KN | High (>92%) | 2,973 | 2,480 | -16.6% | Stable |
| CG | Medium (>85%) | 2,951 | 2,812 | -4.7% | Stable |
| GN | Low (>85%) | 1,823 | 1,527 | -16.2% | Stable |
| AO | Low (>85%) | 1,559 | 1,399 | -10.3% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| MR | ↑ +4.84% | None -100.0% | → Stable | Insufficient Funds -1.89pp | None + Insufficient |

---

*Report: 2026-04-15*
