# AR Initial (LL0) Investigation: HF-INTL 2026-W16

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 91.78% → 91.31% (-0.51%)  
**Volume:** 35,099 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate for HF-INTL declined from 91.78% to 91.31% (-0.51%) in W16, a change that is not statistically significant, with volume increasing from 27,494 to 35,099 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (88.09%-91.78%) | -0.51% | ✅ |
| L1: Country Breakdown | 4 countries exceed ±2.5% threshold | NZ -10.84%, LU -5.06%, NL -3.47%, AU +3.30% | ⚠️ |
| L1: Dimension Scan | No PaymentMethod or Provider exceeds threshold | Max change -1.09% (Adyen) | ✅ |
| L2: NZ Deep-Dive | Significant decline driven by volume surge | Insufficient Funds +7.48pp | ⚠️ |
| L2: LU Deep-Dive | Small volume (92 orders) with rate drop | Insufficient Funds +7.74pp | ⚠️ |
| L2: NL Deep-Dive | ProcessOut -29.54%, credit_card -28.48% | Other reasons +2.28pp | ⚠️ |
| L2: AU Deep-Dive | Positive improvement | Insufficient Funds -2.35pp | ✅ |
| L3: Related Metrics | All funnel metrics declined similarly | -0.38% to -0.85% | ✅ |
| Mix Shift | NZ volume +113%, GB +53.7% | No tier migration | ✅ |

**Key Findings:**
- NZ experienced the largest decline (-10.84%) with volume more than doubling (+113% from 408 to 869 orders); "Insufficient Funds" increased by +7.48pp to 26.35% of transactions
- LU showed a -5.06% decline primarily driven by Adyen (-9.36%) and Unknown provider (-10.00%), with "Insufficient Funds" rising +7.74pp
- NL declined -3.47% with ProcessOut showing severe degradation (-29.54%) and credit_card dropping -28.48%
- AU improved +3.30% with ProcessOut recovering (+4.68%) and "Insufficient Funds" declining -2.35pp
- Overall funnel metrics (1_FirstRunAR through 6_PaymentApprovalRate) all declined proportionally (-0.38% to -0.85%), indicating a systemic rather than stage-specific issue

**Action:** Monitor - The overall decline is not statistically significant and falls within the 8-week normal range. However, closely watch NZ performance given the volume surge and elevated "Insufficient Funds" rates. If NZ decline persists in W17 or volume continues to grow, escalate for ProcessOut investigation.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 91.31% | 35,099 | -0.51% ← REPORTED CHANGE |
| 2026-W15 | 91.78% | 27,494 | +2.13% |
| 2026-W14 | 89.87% | 30,723 | -0.28% |
| 2026-W13 | 90.12% | 34,511 | -1.17% |
| 2026-W12 | 91.19% | 39,023 | -0.41% |
| 2026-W11 | 91.57% | 42,690 | +1.31% |
| 2026-W10 | 90.39% | 47,599 | +2.61% |
| 2026-W09 | 88.09% | 46,648 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| NZ | 69.28% | 77.70% | -10.84% | 869 | ⚠️ |
| LU | 89.13% | 93.88% | -5.06% | 92 | ⚠️ |
| NL | 94.17% | 97.55% | -3.47% | 1,372 | ⚠️ |
| FR | 93.43% | 94.96% | -1.61% | 7,155 |  |
| AU | 84.62% | 81.92% | +3.30% | 2,647 | ⚠️ |

**Countries exceeding ±2.5% threshold:** NZ, LU, NL, AU

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 88.67% | 89.35% | -0.77% | 12,437 |  |
| Others | 96.85% | 97.39% | -0.56% | 5,170 |  |
| Paypal | 96.3% | 96.62% | -0.34% | 6,938 |  |
| Apple Pay | 88.43% | 88.19% | +0.27% | 10,554 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Adyen | 96.36% | 97.42% | -1.09% | 3,018 |  |
| Braintree | 92.47% | 92.94% | -0.50% | 16,329 |  |
| Unknown | 95.8% | 96.07% | -0.28% | 2,239 |  |
| ProcessOut | 87.93% | 88.18% | -0.28% | 13,402 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 111 |  |

---

## L2: NZ Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 92.59% | 0.00% | +0.00% | 27 | 0 |  |
| None | 0.00% | 100.00% | -100.00% | 0 | 21 | ⚠️ |
| paypal | 58.62% | 90.91% | -35.52% | 29 | 11 | ⚠️ |
| credit_card | 68.60% | 76.62% | -10.46% | 586 | 278 | ⚠️ |
| applepay | 69.47% | 73.96% | -6.07% | 226 | 96 | ⚠️ |
| cashcredit | 100.00% | 100.00% | +0.00% | 1 | 2 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Braintree | 58.62% | 90.91% | -35.52% | 29 | 11 | ⚠️ |
| Adyen | 77.78% | 92.31% | -15.74% | 9 | 13 | ⚠️ |
| ProcessOut | 68.78% | 75.68% | -9.12% | 804 | 366 | ⚠️ |
| Unknown | 92.31% | 100.00% | -7.69% | 26 | 16 | ⚠️ |
| No Payment | 100.00% | 100.00% | +0.00% | 1 | 2 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 602 | 317 | 69.28% | 77.70% | -8.42 |
| Insufficient Funds | 229 | 77 | 26.35% | 18.87% | +7.48 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 12 | 1 | 1.38% | 0.25% | +1.14 |
| Other reasons | 23 | 13 | 2.65% | 3.19% | -0.54 |
| Unknown | 3 | 0 | 0.35% | 0.00% | +0.35 |

**Root Cause:** None + Braintree + Insufficient

---

## L2: LU Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 90.00% | 0.00% | +0.00% | 10 | 0 |  |
| None | 0.00% | 100.00% | -100.00% | 0 | 9 | ⚠️ |
| credit_card | 86.11% | 88.89% | -3.13% | 36 | 18 |  |
| applepay | 89.19% | 90.91% | -1.89% | 37 | 11 |  |
| paypal | 100.00% | 100.00% | +0.00% | 6 | 8 |  |
| sepadirectdebit | 100.00% | 100.00% | +0.00% | 3 | 3 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| ProcessOut | 100.00% | 0.00% | +0.00% | 3 | 1 |  |
| Unknown | 90.00% | 100.00% | -10.00% | 10 | 9 | ⚠️ |
| Adyen | 86.11% | 95.00% | -9.36% | 36 | 20 | ⚠️ |
| Braintree | 90.70% | 94.74% | -4.26% | 43 | 19 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Insufficient Funds | 9 | 1 | 9.78% | 2.04% | +7.74 |
| 1. SUCCESSFULL | 82 | 46 | 89.13% | 93.88% | -4.75 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 0 | 1 | 0.00% | 2.04% | -2.04 |
| Other reasons | 1 | 1 | 1.09% | 2.04% | -0.95 |

**Root Cause:** None + Unknown + Insufficient

---

## L2: NL Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 5 | 0 |  |
| None | 0.00% | 88.89% | -100.00% | 0 | 9 | ⚠️ |
| sepadirectdebit | 0.00% | 83.33% | -100.00% | 0 | 6 | ⚠️ |
| credit_card | 61.54% | 86.05% | -28.48% | 104 | 43 | ⚠️ |
| applepay | 86.81% | 92.68% | -6.34% | 144 | 123 | ⚠️ |
| klarna | 96.12% | 98.31% | -2.23% | 103 | 59 |  |
| ideal | 98.76% | 99.04% | -0.29% | 967 | 835 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 32 | 5 |  |
| paypal | 100.00% | 95.83% | +4.35% | 17 | 24 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 88.89% | -100.00% | 5 | 9 | ⚠️ |
| ProcessOut | 60.40% | 85.71% | -29.54% | 101 | 42 | ⚠️ |
| Braintree | 88.20% | 93.20% | -5.36% | 161 | 147 | ⚠️ |
| Adyen | 98.51% | 98.89% | -0.39% | 1,073 | 901 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 32 | 5 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,292 | 1,077 | 94.17% | 97.55% | -3.39 |
| Other reasons | 45 | 11 | 3.28% | 1.00% | +2.28 |
| Insufficient Funds | 27 | 13 | 1.97% | 1.18% | +0.79 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 6 | 2 | 0.44% | 0.18% | +0.26 |
| Unknown | 2 | 1 | 0.15% | 0.09% | +0.06 |

**Root Cause:** None + Unknown + Other

---

## L2: AU Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 98.02% | 0.00% | +0.00% | 202 | 0 |  |
| None | 0.00% | 99.05% | -100.00% | 0 | 211 | ⚠️ |
| paypal | 92.35% | 92.43% | -0.08% | 327 | 317 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 12 | 7 |  |
| credit_card | 83.06% | 80.12% | +3.68% | 1,169 | 1,192 |  |
| applepay | 80.79% | 76.44% | +5.68% | 937 | 900 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Adyen | 82.86% | 88.64% | -6.52% | 35 | 88 | ⚠️ |
| Unknown | 97.85% | 99.40% | -1.56% | 186 | 167 |  |
| Braintree | 92.35% | 92.43% | -0.08% | 327 | 317 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 12 | 8 |  |
| ProcessOut | 82.18% | 78.51% | +4.68% | 2,087 | 2,047 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 2,240 | 2,152 | 84.62% | 81.92% | +2.71 |
| Insufficient Funds | 352 | 411 | 13.30% | 15.65% | -2.35 |
| Other reasons | 26 | 38 | 0.98% | 1.45% | -0.46 |
| Unknown | 4 | 1 | 0.15% | 0.04% | +0.11 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 25 | 25 | 0.94% | 0.95% | -0.01 |

**Root Cause:** None + Adyen + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 89.02% | 89.78% | -0.85% | 35,099 | 27,494 |  |
| 2_PreDunningAR | 91.31% | 91.78% | -0.51% | 35,099 | 27,494 |  |
| 3_PostDunningAR | 91.7% | 92.19% | -0.54% | 35,099 | 27,494 |  |
| 6_PaymentApprovalRate | 92.1% | 92.46% | -0.38% | 35,099 | 27,494 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| DE | High (>92%) | 6,536 | 7,172 | +9.7% | Stable |
| GB | Medium (>85%) | 5,647 | 8,681 | +53.7% | Stable |
| FR | High (>92%) | 5,183 | 7,155 | +38.0% | Stable |
| AU | Low (>85%) | 2,627 | 2,647 | +0.8% | Stable |
| BE | High (>92%) | 1,437 | 1,796 | +25.0% | Stable |
| NL | High (>92%) | 1,104 | 1,372 | +24.3% | Stable |
| IE | Medium (>85%) | 1,076 | 1,365 | +26.9% | Stable |
| DK | High (>92%) | 1,074 | 1,230 | +14.5% | Stable |
| SE | Medium (>85%) | 1,006 | 1,217 | +21.0% | Stable |
| AT | High (>92%) | 670 | 600 | -10.4% | Stable |
| NO | Medium (>85%) | 582 | 768 | +32.0% | Stable |
| NZ | Low (>85%) | 408 | 869 | +113.0% | Stable |
| CH | Medium (>85%) | 95 | 135 | +42.1% | Stable |
| LU | High (>92%) | 49 | 92 | +87.8% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| NZ | ↓ -10.84% | None -100.0% | Braintree -35.5% | Insufficient Funds +7.48pp | None + Braintree + Insufficient |
| LU | ↓ -5.06% | None -100.0% | Unknown -10.0% | Insufficient Funds +7.74pp | None + Unknown + Insufficient |
| NL | ↓ -3.47% | None -100.0% | Unknown -100.0% | Other reasons +2.28pp | None + Unknown + Other |
| AU | ↑ +3.30% | None -100.0% | Adyen -6.5% | Insufficient Funds -2.35pp | None + Adyen + Insufficient |

---

*Report: 2026-04-22*
