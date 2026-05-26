# AR Overall Investigation: HF-INTL 2026-W21

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 95.08% → 94.94% (-0.15%)  
**Volume:** 748,329 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate for HF-INTL decreased slightly from 95.08% to 94.94% (-0.14pp) in 2026-W21, a change that is not statistically significant and remains within normal weekly fluctuation range (93.61% - 95.08% over 8 weeks).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (93.61%-95.08%) | -0.14pp | ✅ |
| L1: Country Breakdown | 1 country (NO) exceeds ±2.5% threshold | NO +3.63% | ⚠️ |
| L1: PaymentMethod | All methods within ±2.5% | Max: -0.64% | ✅ |
| L1: PaymentProvider | Unknown exceeds threshold | -3.24% | ⚠️ |
| L2: NO Deep-Dive | Improvement driven by reduced Insufficient Funds | -3.05pp | ✅ |
| L3: Related Metrics | All funnel metrics stable | Max: -0.34% | ✅ |
| Mix Shift | All countries stable volume impact | N/A | ✅ |

**Key Findings:**
- NO showed significant improvement (+3.63%), driven by a 3.05pp reduction in "Insufficient Funds" declines (from 9.02% to 5.97% of orders)
- The "Unknown" PaymentProvider segment declined -3.24% at L1 level, but represents minimal volume (1,627 orders, <0.2% of total)
- Apple Pay continues to underperform other payment methods at 89.89% vs. overall 94.94%, though change was modest (-0.64pp)
- In NO, applepay showed strong improvement (+5.48%), moving from 84.52% to 89.15%
- Full payment funnel remains healthy: FirstRunAR (92.95%), PreDunningAR (94.94%), PostDunningAR (96.64%), PaymentApprovalRate (97.57%)

**Action:** Monitor - No action required. The -0.14pp decline is not significant, and the flagged NO improvement is a positive trend. Continue standard weekly monitoring.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W21 | 94.94% | 748,329 | -0.15% ← REPORTED CHANGE |
| 2026-W20 | 95.08% | 747,471 | +0.51% |
| 2026-W19 | 94.6% | 789,069 | +0.73% |
| 2026-W18 | 93.91% | 780,744 | -0.73% |
| 2026-W17 | 94.6% | 794,597 | -0.20% |
| 2026-W16 | 94.79% | 804,152 | +0.07% |
| 2026-W15 | 94.72% | 744,637 | +1.19% |
| 2026-W14 | 93.61% | 784,406 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CH | 92.18% | 93.74% | -1.67% | 2,147 |  |
| SE | 95.84% | 96.64% | -0.83% | 34,022 |  |
| LU | 95.83% | 96.51% | -0.71% | 3,142 |  |
| GB | 94.24% | 94.74% | -0.53% | 194,230 |  |
| FR | 94.56% | 94.79% | -0.24% | 134,066 |  |
| NO | 92.89% | 89.64% | +3.63% | 20,266 | ⚠️ |

**Countries exceeding ±2.5% threshold:** NO

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 89.89% | 90.46% | -0.64% | 99,888 |  |
| Credit Card | 93.31% | 93.51% | -0.21% | 341,747 |  |
| Others | 99.13% | 99.18% | -0.05% | 120,255 |  |
| Paypal | 97.94% | 97.88% | +0.06% | 186,439 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 87.89% | 90.84% | -3.24% | 1,627 | ⚠️ |
| Adyen | 96.01% | 96.19% | -0.19% | 248,600 |  |
| Braintree | 95.42% | 95.56% | -0.14% | 280,895 |  |
| ProcessOut | 92.99% | 93.09% | -0.11% | 212,531 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 4,676 |  |

---

## L2: NO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 97.06% | 0.00% | +0.00% | 68 | 0 |  |
| None | 0.00% | 98.15% | -100.00% | 0 | 270 | ⚠️ |
| cashcredit | 100.00% | 100.00% | +0.00% | 105 | 151 |  |
| paypal | 93.24% | 90.10% | +3.48% | 1,094 | 1,141 |  |
| credit_card | 93.47% | 90.32% | +3.49% | 16,124 | 16,047 |  |
| applepay | 89.15% | 84.52% | +5.48% | 2,875 | 2,991 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 90.48% | 97.87% | -7.56% | 21 | 235 | ⚠️ |
| No Payment | 100.00% | 100.00% | +0.00% | 105 | 151 |  |
| ProcessOut | 93.75% | 90.87% | +3.18% | 10,818 | 10,762 |  |
| Adyen | 92.96% | 89.27% | +4.13% | 5,353 | 5,320 |  |
| Braintree | 90.27% | 86.06% | +4.90% | 3,969 | 4,132 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 18,825 | 18,465 | 92.89% | 89.64% | +3.25 |
| Insufficient Funds | 1,209 | 1,858 | 5.97% | 9.02% | -3.05 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 121 | 170 | 0.60% | 0.83% | -0.23 |
| Other reasons | 109 | 103 | 0.54% | 0.50% | +0.04 |
| Unknown | 2 | 4 | 0.01% | 0.02% | -0.01 |

**Root Cause:** None + Unknown + Insufficient

---

## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 92.95% | 93.26% | -0.34% | 748,329 | 747,471 |  |
| 2_PreDunningAR | 94.94% | 95.08% | -0.14% | 748,329 | 747,471 |  |
| 3_PostDunningAR | 96.64% | 96.91% | -0.28% | 748,329 | 747,471 |  |
| 6_PaymentApprovalRate | 97.57% | 97.53% | +0.05% | 748,329 | 747,471 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | High (>92%) | 203,866 | 194,230 | -4.7% | Stable |
| DE | High (>92%) | 202,135 | 204,608 | +1.2% | Stable |
| FR | High (>92%) | 129,260 | 134,066 | +3.7% | Stable |
| NL | High (>92%) | 100,326 | 99,062 | -1.3% | Stable |
| AU | Medium (>85%) | 96,578 | 95,841 | -0.8% | Stable |
| BE | High (>92%) | 65,230 | 67,838 | +4.0% | Stable |
| SE | High (>92%) | 33,815 | 34,022 | +0.6% | Stable |
| DK | High (>92%) | 33,798 | 35,110 | +3.9% | Stable |
| NO | Medium (>85%) | 20,600 | 20,266 | -1.6% | Stable |
| NZ | Medium (>85%) | 19,681 | 19,034 | -3.3% | Stable |
| IE | High (>92%) | 18,470 | 18,635 | +0.9% | Stable |
| AT | High (>92%) | 12,230 | 12,530 | +2.5% | Stable |
| LU | High (>92%) | 3,327 | 3,142 | -5.6% | Stable |
| CH | High (>92%) | 2,045 | 2,147 | +5.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| NO | ↑ +3.63% | None -100.0% | Unknown -7.6% | Insufficient Funds -3.05pp | None + Unknown + Insufficient |

---

*Report: 2026-05-26*
