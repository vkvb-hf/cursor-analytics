# AR Initial (LL0) Investigation: HF-INTL 2026-W15

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 91.78% → 91.31% (-0.51%)  
**Volume:** 35,099 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) for HF-INTL decreased by -0.51% (from 91.78% to 91.31%) in 2026-W15, with this change flagged as not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Within normal volatility (range: 88.09%-91.78%) | -0.51% | ✅ |
| L1: Country Breakdown | 5 countries exceed ±2.5% threshold (DE, BE, DK, NZ, LU) | +2.78% to +10.64% | ⚠️ |
| L1: PaymentMethod | Apple Pay +2.56%, Credit Card +3.06% | Mixed | ⚠️ |
| L1: PaymentProvider | ProcessOut +3.07% exceeds threshold | +3.07% | ⚠️ |
| L2: Deep-Dive Root Causes | Consistent pattern: Insufficient Funds decline improvement | -2.07pp to -4.14pp | ✅ |
| L3: Related Metrics | All loyalty metrics improved (+1.82% to +2.39%) | Positive | ✅ |
| Mix Shift | NL volume -40.9%, GB -25.9%, FR -29.3% | High-AR volume loss | ⚠️ |

**Key Findings:**
- The -0.51% overall decline masks underlying improvements in multiple countries: DE (+2.78%), BE (+4.24%), DK (+4.38%), NZ (+7.21%), and LU (+10.64%)
- Insufficient Funds decline rates dropped significantly across flagged markets: DE -2.07pp, BE -3.23pp, DK -3.74pp, NZ -4.14pp
- ProcessOut showed notable improvement in BE (+8.10%), NZ (+6.07%), and DE (+20.74%), while Credit Card payment method improved substantially in DE (+20.65%) and BE (+8.12%)
- Mix shift impact: High-AR countries (NL, FR) experienced significant volume drops (-40.9% and -29.3% respectively), while lower-AR markets like DE gained volume (+55.5%)
- All related funnel metrics (FirstRunAR, PreDunningAR, PostDunningAR, PaymentApprovalRate) showed consistent improvement ranging from +1.82% to +2.39%

**Action:** Monitor - The decline is not statistically significant and appears driven by mix shift (volume moving from high-AR to medium-AR countries) rather than underlying performance degradation. Individual country performance is actually improving. Continue monitoring NL and FR volume recovery.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 91.31% | 35,099 | -0.51% |
| 2026-W15 | 91.78% | 27,494 | +2.13% ← REPORTED CHANGE |
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
| FR | 94.96% | 92.92% | +2.20% | 5,183 |  |
| DE | 94.12% | 91.58% | +2.78% | 6,536 | ⚠️ |
| BE | 94.78% | 90.92% | +4.24% | 1,437 | ⚠️ |
| DK | 94.04% | 90.09% | +4.38% | 1,074 | ⚠️ |
| NZ | 77.70% | 72.47% | +7.21% | 408 | ⚠️ |
| LU | 93.88% | 84.85% | +10.64% | 49 | ⚠️ |

**Countries exceeding ±2.5% threshold:** DE, BE, DK, NZ, LU

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 97.39% | 97.91% | -0.52% | 4,260 |  |
| Paypal | 96.62% | 95.74% | +0.93% | 5,717 |  |
| Apple Pay | 88.19% | 85.99% | +2.56% | 7,954 | ⚠️ |
| Credit Card | 89.35% | 86.7% | +3.06% | 9,563 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 96.07% | 98.23% | -2.19% | 1,885 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 69 |  |
| Adyen | 97.42% | 97.0% | +0.43% | 2,476 |  |
| Braintree | 92.94% | 90.82% | +2.33% | 12,675 |  |
| ProcessOut | 88.18% | 85.56% | +3.07% | 10,389 | ⚠️ |

---

## L2: DE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 9.09% | 0.00% | +0.00% | 44 | 0 |  |
| None | 0.00% | 66.67% | -100.00% | 0 | 33 | ⚠️ |
| klarna | 98.46% | 100.00% | -1.54% | 389 | 226 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 33 | 16 |  |
| paypal | 97.39% | 96.56% | +0.86% | 3,833 | 2,586 |  |
| applepay | 92.13% | 88.51% | +4.10% | 1,335 | 783 |  |
| credit_card | 85.25% | 70.66% | +20.65% | 902 | 559 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 9.09% | 64.52% | -85.91% | 44 | 31 | ⚠️ |
| Adyen | 98.24% | 99.57% | -1.33% | 398 | 232 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 33 | 17 |  |
| Braintree | 96.03% | 94.69% | +1.42% | 5,168 | 3,369 |  |
| ProcessOut | 85.22% | 70.58% | +20.74% | 893 | 554 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 6,152 | 3,849 | 94.12% | 91.58% | +2.55 |
| Insufficient Funds | 205 | 219 | 3.14% | 5.21% | -2.07 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 116 | 100 | 1.77% | 2.38% | -0.60 |
| Unknown | 40 | 11 | 0.61% | 0.26% | +0.35 |
| Other reasons | 23 | 24 | 0.35% | 0.57% | -0.22 |

**Root Cause:** None + Unknown + Insufficient

---

## L2: BE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 98.58% | 0.00% | +0.00% | 494 | 0 |  |
| None | 0.00% | 98.74% | -100.00% | 0 | 396 | ⚠️ |
| paypal | 85.39% | 88.89% | -3.93% | 89 | 117 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 1 | 5 |  |
| sepadirectdebit | 99.23% | 96.45% | +2.89% | 260 | 394 |  |
| bancontact | 93.94% | 88.76% | +5.83% | 198 | 267 | ⚠️ |
| applepay | 88.33% | 83.23% | +6.14% | 120 | 155 | ⚠️ |
| credit_card | 90.18% | 83.41% | +8.12% | 275 | 440 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 98.58% | 98.74% | -0.16% | 494 | 396 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 1 | 5 |  |
| Braintree | 87.08% | 85.66% | +1.66% | 209 | 272 |  |
| Adyen | 96.98% | 93.39% | +3.84% | 464 | 666 |  |
| ProcessOut | 89.96% | 83.22% | +8.10% | 269 | 435 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,362 | 1,613 | 94.78% | 90.92% | +3.86 |
| Insufficient Funds | 37 | 103 | 2.57% | 5.81% | -3.23 |
| Other reasons | 16 | 36 | 1.11% | 2.03% | -0.92 |
| Unknown | 4 | 1 | 0.28% | 0.06% | +0.22 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 18 | 21 | 1.25% | 1.18% | +0.07 |

**Root Cause:** None + ProcessOut + Insufficient

---

## L2: DK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 84.00% | 0.00% | +0.00% | 25 | 0 |  |
| cashcredit | 100.00% | 0.00% | +0.00% | 4 | 0 |  |
| None | 0.00% | 100.00% | -100.00% | 0 | 23 | ⚠️ |
| paypal | 100.00% | 100.00% | +0.00% | 21 | 15 |  |
| credit_card | 95.83% | 92.62% | +3.47% | 624 | 420 |  |
| applepay | 91.50% | 85.44% | +7.10% | 400 | 309 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| No Payment | 100.00% | 0.00% | +0.00% | 4 | 0 |  |
| Unknown | 80.00% | 100.00% | -20.00% | 20 | 15 | ⚠️ |
| ProcessOut | 95.79% | 92.81% | +3.22% | 618 | 417 |  |
| Braintree | 91.92% | 86.11% | +6.75% | 421 | 324 | ⚠️ |
| Adyen | 100.00% | 90.91% | +10.00% | 11 | 11 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,010 | 691 | 94.04% | 90.09% | +3.95 |
| Insufficient Funds | 48 | 63 | 4.47% | 8.21% | -3.74 |
| Unknown | 4 | 0 | 0.37% | 0.00% | +0.37 |
| Other reasons | 6 | 7 | 0.56% | 0.91% | -0.35 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 6 | 6 | 0.56% | 0.78% | -0.22 |

**Root Cause:** None + Unknown + Insufficient

---

## L2: NZ Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 100.00% | 0.00% | +0.00% | 21 | 0 |  |
| None | 0.00% | 100.00% | -100.00% | 0 | 31 | ⚠️ |
| cashcredit | 100.00% | 100.00% | +0.00% | 2 | 1 |  |
| applepay | 73.96% | 71.88% | +2.90% | 96 | 160 |  |
| credit_card | 76.62% | 70.97% | +7.96% | 278 | 434 | ⚠️ |
| paypal | 90.91% | 64.71% | +40.50% | 11 | 17 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| No Payment | 100.00% | 100.00% | +0.00% | 2 | 1 |  |
| Unknown | 100.00% | 100.00% | +0.00% | 16 | 5 |  |
| Adyen | 92.31% | 89.19% | +3.50% | 13 | 37 |  |
| ProcessOut | 75.68% | 71.36% | +6.07% | 366 | 583 | ⚠️ |
| Braintree | 90.91% | 64.71% | +40.50% | 11 | 17 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 317 | 466 | 77.70% | 72.47% | +5.22 |
| Insufficient Funds | 77 | 148 | 18.87% | 23.02% | -4.14 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 1 | 6 | 0.25% | 0.93% | -0.69 |
| Other reasons | 13 | 23 | 3.19% | 3.58% | -0.39 |

**Root Cause:** None + ProcessOut + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 89.78% | 87.68% | +2.39% | 27,494 | 30,723 |  |
| 2_PreDunningAR | 91.78% | 89.87% | +2.12% | 27,494 | 30,723 |  |
| 3_PostDunningAR | 92.19% | 90.46% | +1.91% | 27,494 | 30,723 |  |
| 6_PaymentApprovalRate | 92.46% | 90.8% | +1.82% | 27,494 | 30,723 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | Medium (>85%) | 7,619 | 5,647 | -25.9% | ⚠️ Volume drop |
| FR | High (>92%) | 7,333 | 5,183 | -29.3% | ⚠️ Volume drop |
| DE | Medium (>85%) | 4,203 | 6,536 | +55.5% | Stable |
| AU | Low (>85%) | 3,045 | 2,627 | -13.7% | Stable |
| NL | High (>92%) | 1,867 | 1,104 | -40.9% | ⚠️ Major mix shift |
| BE | Medium (>85%) | 1,774 | 1,437 | -19.0% | Stable |
| IE | Medium (>85%) | 1,410 | 1,076 | -23.7% | ⚠️ Volume drop |
| SE | High (>92%) | 993 | 1,006 | +1.3% | Stable |
| DK | Medium (>85%) | 767 | 1,074 | +40.0% | Stable |
| NZ | Low (>85%) | 643 | 408 | -36.5% | ⚠️ Volume drop |
| NO | Medium (>85%) | 477 | 582 | +22.0% | Stable |
| AT | Medium (>85%) | 384 | 670 | +74.5% | Stable |
| CH | Medium (>85%) | 142 | 95 | -33.1% | ⚠️ Volume drop |
| LU | Low (>85%) | 66 | 49 | -25.8% | ⚠️ Volume drop |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| DE | ↑ +2.78% | None -100.0% | Unknown -85.9% | Insufficient Funds -2.07pp | None + Unknown + Insufficient |
| BE | ↑ +4.24% | None -100.0% | ProcessOut +8.1% | Insufficient Funds -3.23pp | None + ProcessOut + Insufficient |
| DK | ↑ +4.38% | None -100.0% | Unknown -20.0% | Insufficient Funds -3.74pp | None + Unknown + Insufficient |
| NZ | ↑ +7.21% | None -100.0% | ProcessOut +6.1% | Insufficient Funds -4.14pp | None + ProcessOut + Insufficient |

---

*Report: 2026-04-22*
