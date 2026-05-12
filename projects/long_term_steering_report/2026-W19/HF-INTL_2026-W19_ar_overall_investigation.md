# AR Overall Investigation: HF-INTL 2026-W19

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 93.93% → 94.62% (+0.73%)  
**Volume:** 789,069 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate improved from 93.93% to 94.62% (+0.69 pp) across 789,069 orders in W19, with the change flagged as not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Within normal range (94.15%-94.80%) | +0.69 pp | ✅ |
| L1: Country Breakdown | SE (+2.53%), LU (+4.67%) exceed ±2.5% threshold | 2 flags | ⚠️ |
| L1: PaymentProvider | Unknown provider -3.22% (low volume: 1,794) | 1 flag | ✅ |
| L2: SE Deep-Dive | Braintree +5.30%, Insufficient Funds -2.13 pp | Root cause identified | ⚠️ |
| L2: LU Deep-Dive | Braintree +5.82%, Insufficient Funds -3.70 pp | Root cause identified | ⚠️ |
| L3: Related Metrics | All metrics stable, 1_FirstRunAR +0.93% | No concerns | ✅ |
| Mix Shift | All countries stable, no significant volume shifts | No impact | ✅ |

**Key Findings:**
- SE and LU both show significant AR improvements driven by reduced "Insufficient Funds" declines (-2.13 pp and -3.70 pp respectively)
- Braintree provider performance improved substantially in both flagged countries: SE (+5.30%) and LU (+5.82%)
- Apple Pay showed notable improvements in both SE (+5.71%) and LU (+10.09%), though from lower baseline rates
- The "None" payment method anomaly (-100% in both SE and LU) appears to be a data categorization shift rather than a true operational change
- Overall metric remains within the 8-week normal operating range (94.15%-94.80%), indicating recovery from W18's dip

**Action:** Monitor - The improvement is positive and driven by identifiable factors (reduced Insufficient Funds declines via Braintree). No escalation needed as changes are favorable and statistically not significant. Continue monitoring SE and LU performance in W20 to confirm trend stability.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W19 | 94.62% | 789,069 | +0.73% ← REPORTED CHANGE |
| 2026-W18 | 93.93% | 780,744 | -0.72% |
| 2026-W17 | 94.61% | 794,598 | -0.20% |
| 2026-W16 | 94.8% | 804,152 | +0.07% |
| 2026-W15 | 94.73% | 744,637 | +1.19% |
| 2026-W14 | 93.62% | 784,406 | -0.56% |
| 2026-W13 | 94.15% | 842,482 | -0.47% |
| 2026-W12 | 94.59% | 877,189 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| DE | 97.42% | 96.93% | +0.50% | 232,594 |  |
| BE | 95.22% | 94.31% | +0.96% | 67,448 |  |
| GB | 94.62% | 93.63% | +1.07% | 206,083 |  |
| IE | 91.89% | 90.01% | +2.09% | 18,498 |  |
| SE | 97.31% | 94.91% | +2.53% | 38,231 | ⚠️ |
| LU | 96.35% | 92.05% | +4.67% | 3,509 | ⚠️ |

**Countries exceeding ±2.5% threshold:** SE, LU

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 97.57% | 97.46% | +0.12% | 202,689 |  |
| Others | 99.0% | 98.84% | +0.16% | 121,840 |  |
| Credit Card | 92.89% | 92.08% | +0.88% | 357,518 |  |
| Apple Pay | 89.79% | 88.31% | +1.68% | 107,022 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 86.18% | 89.04% | -3.22% | 1,794 | ⚠️ |
| No Payment | 100.0% | 100.0% | +0.00% | 4,835 |  |
| Braintree | 95.18% | 94.54% | +0.67% | 303,987 |  |
| ProcessOut | 92.47% | 91.79% | +0.74% | 224,606 |  |
| Adyen | 95.8% | 95.1% | +0.74% | 253,847 |  |

---

## L2: SE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 91.27% | 0.00% | +0.00% | 126 | 0 |  |
| None | 0.00% | 84.24% | -100.00% | 0 | 184 | ⚠️ |
| cashcredit | 100.00% | 100.00% | +0.00% | 243 | 221 |  |
| klarna | 99.26% | 99.08% | +0.19% | 16,165 | 16,292 |  |
| paypal | 93.98% | 90.70% | +3.62% | 897 | 903 |  |
| credit_card | 96.18% | 92.25% | +4.25% | 17,025 | 16,565 |  |
| applepay | 94.91% | 89.79% | +5.71% | 3,775 | 3,751 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| No Payment | 100.00% | 100.00% | +0.00% | 243 | 221 |  |
| Adyen | 98.43% | 97.24% | +1.23% | 22,306 | 22,281 |  |
| ProcessOut | 96.19% | 92.37% | +4.13% | 10,989 | 10,708 |  |
| Braintree | 94.73% | 89.97% | +5.30% | 4,672 | 4,654 | ⚠️ |
| Unknown | 47.62% | 44.23% | +7.66% | 21 | 52 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 37,204 | 35,987 | 97.31% | 94.91% | +2.40 |
| Insufficient Funds | 673 | 1,474 | 1.76% | 3.89% | -2.13 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 171 | 237 | 0.45% | 0.63% | -0.18 |
| Other reasons | 172 | 205 | 0.45% | 0.54% | -0.09 |
| Unknown | 11 | 13 | 0.03% | 0.03% | -0.01 |

**Root Cause:** None + Braintree + Insufficient

---

## L2: LU Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 100.00% | 0.00% | +0.00% | 6 | 0 |  |
| None | 0.00% | 100.00% | -100.00% | 0 | 6 | ⚠️ |
| cashcredit | 100.00% | 100.00% | +0.00% | 26 | 12 |  |
| sepadirectdebit | 99.57% | 99.56% | +0.01% | 468 | 455 |  |
| paypal | 98.73% | 95.22% | +3.69% | 631 | 669 |  |
| credit_card | 95.46% | 90.66% | +5.29% | 1,984 | 1,896 | ⚠️ |
| applepay | 92.89% | 84.38% | +10.09% | 394 | 397 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| ProcessOut | 50.00% | 0.00% | +0.00% | 2 | 1 |  |
| Unknown | 100.00% | 100.00% | +0.00% | 6 | 6 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 26 | 12 |  |
| Adyen | 96.29% | 92.43% | +4.18% | 2,450 | 2,350 |  |
| Braintree | 96.49% | 91.18% | +5.82% | 1,025 | 1,066 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 3,381 | 3,162 | 96.35% | 92.05% | +4.30 |
| Insufficient Funds | 44 | 170 | 1.25% | 4.95% | -3.70 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 37 | 51 | 1.05% | 1.48% | -0.43 |
| Other reasons | 47 | 52 | 1.34% | 1.51% | -0.17 |

**Root Cause:** None + Braintree + Insufficient

---

## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 92.56% | 91.7% | +0.93% | 789,069 | 780,744 |  |
| 2_PreDunningAR | 94.62% | 93.93% | +0.73% | 789,069 | 780,744 |  |
| 3_PostDunningAR | 96.5% | 96.67% | -0.18% | 789,069 | 780,744 |  |
| 6_PaymentApprovalRate | 97.29% | 97.29% | +0.00% | 789,069 | 780,744 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| DE | High (>92%) | 225,472 | 232,594 | +3.2% | Stable |
| GB | High (>92%) | 210,813 | 206,083 | -2.2% | Stable |
| FR | High (>92%) | 134,603 | 136,525 | +1.4% | Stable |
| AU | Medium (>85%) | 95,241 | 97,538 | +2.4% | Stable |
| NL | High (>92%) | 91,532 | 101,537 | +10.9% | Stable |
| BE | High (>92%) | 67,404 | 67,448 | +0.1% | Stable |
| DK | High (>92%) | 39,006 | 38,750 | -0.7% | Stable |
| SE | High (>92%) | 37,916 | 38,231 | +0.8% | Stable |
| NO | High (>92%) | 22,944 | 22,798 | -0.6% | Stable |
| NZ | Medium (>85%) | 19,343 | 19,676 | +1.7% | Stable |
| IE | Medium (>85%) | 19,292 | 18,498 | -4.1% | Stable |
| AT | High (>92%) | 13,866 | 13,976 | +0.8% | Stable |
| LU | High (>92%) | 3,435 | 3,509 | +2.2% | Stable |
| CH | Medium (>85%) | 2,298 | 2,395 | +4.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| SE | ↑ +2.53% | None -100.0% | Braintree +5.3% | Insufficient Funds -2.13pp | None + Braintree + Insufficient |
| LU | ↑ +4.67% | None -100.0% | Braintree +5.8% | Insufficient Funds -3.70pp | None + Braintree + Insufficient |

---

*Report: 2026-05-12*
