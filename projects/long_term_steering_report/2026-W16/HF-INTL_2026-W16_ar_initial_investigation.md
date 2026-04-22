# AR Initial (LL0) Investigation: HF-INTL 2026-W16

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 91.78% → 91.42% (-0.39%)  
**Volume:** 35,070 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) declined modestly from 91.78% to 91.42% (-0.39%) in W16, a statistically non-significant change within normal week-over-week fluctuation range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Within historical range (88.11%-91.78%) | -0.39% | ✅ |
| L1: Country Breakdown | 4 countries exceed ±2.5% threshold | NZ -10.84%, LU -5.06%, NL -3.40%, AU +3.35% | ⚠️ |
| L1: Dimension Scan | All payment methods/providers within tolerance | Max change -0.76% (Adyen) | ✅ |
| L2: Country Deep-Dives | Insufficient Funds driving declines in NZ, LU | NZ +7.48pp, LU +7.74pp | ⚠️ |
| L3: Related Metrics | All funnel metrics declined proportionally | 1_FirstRunAR -0.74%, 3_PostDunningAR -0.41% | ✅ |
| Mix Shift Analysis | Volume shifts stable across all tiers | NZ +113%, GB +54% | ✅ |

**Key Findings:**
- NZ experienced the largest decline (-10.84%) driven by a +7.48pp increase in "Insufficient Funds" declines, with volume more than doubling from 408 to 869 orders
- LU showed a -5.06% decline with "Insufficient Funds" increasing by +7.74pp, though volume remains low (92 orders)
- NL declined -3.40% with ProcessOut provider dropping significantly (-29.54%) and credit_card method falling -28.48%
- AU improved +3.35% counter to the overall trend, with ProcessOut performance increasing +4.74% and "Insufficient Funds" decreasing -2.39pp
- Global payment method and provider dimensions show no systemic issues—all changes within ±1% tolerance

**Action:** Monitor — The overall -0.39% decline is not statistically significant and the rate remains within the 8-week historical range. Continue monitoring NZ performance given the volume surge and elevated insufficient funds rate; no escalation required at this time.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 91.42% | 35,070 | -0.39% ← REPORTED CHANGE |
| 2026-W15 | 91.78% | 27,488 | +2.22% |
| 2026-W14 | 89.79% | 30,666 | -0.40% |
| 2026-W13 | 90.15% | 34,400 | -1.10% |
| 2026-W12 | 91.15% | 38,951 | -0.38% |
| 2026-W11 | 91.5% | 42,707 | +1.21% |
| 2026-W10 | 90.41% | 47,636 | +2.61% |
| 2026-W09 | 88.11% | 46,569 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| NZ | 69.28% | 77.70% | -10.84% | 869 | ⚠️ |
| LU | 89.13% | 93.88% | -5.06% | 92 | ⚠️ |
| NL | 94.24% | 97.55% | -3.40% | 1,371 | ⚠️ |
| FR | 93.42% | 94.96% | -1.63% | 7,156 |  |
| AU | 84.62% | 81.88% | +3.35% | 2,647 | ⚠️ |

**Countries exceeding ±2.5% threshold:** NZ, LU, NL, AU

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 88.78% | 89.36% | -0.65% | 12,422 |  |
| Others | 97.02% | 97.4% | -0.39% | 5,166 |  |
| Paypal | 96.41% | 96.63% | -0.23% | 6,934 |  |
| Apple Pay | 88.52% | 88.18% | +0.38% | 10,548 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Adyen | 96.68% | 97.42% | -0.76% | 3,013 |  |
| Braintree | 92.58% | 92.94% | -0.39% | 16,319 |  |
| Unknown | 95.76% | 96.08% | -0.33% | 2,240 |  |
| ProcessOut | 88.03% | 88.17% | -0.16% | 13,387 |  |
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
| Adyen | 77.78% | 91.67% | -15.15% | 9 | 12 | ⚠️ |
| ProcessOut | 68.78% | 75.68% | -9.12% | 804 | 366 | ⚠️ |
| Unknown | 92.31% | 100.00% | -7.69% | 26 | 17 | ⚠️ |
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
| ideal | 98.86% | 99.04% | -0.18% | 966 | 835 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 32 | 5 |  |
| paypal | 100.00% | 95.83% | +4.35% | 17 | 24 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 88.89% | -100.00% | 5 | 9 | ⚠️ |
| ProcessOut | 60.40% | 85.71% | -29.54% | 101 | 42 | ⚠️ |
| Braintree | 88.20% | 93.20% | -5.36% | 161 | 147 | ⚠️ |
| Adyen | 98.60% | 98.89% | -0.29% | 1,072 | 901 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 32 | 5 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,292 | 1,077 | 94.24% | 97.55% | -3.32 |
| Other reasons | 44 | 11 | 3.21% | 1.00% | +2.21 |
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
| applepay | 80.79% | 76.33% | +5.84% | 937 | 900 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Adyen | 82.86% | 88.64% | -6.52% | 35 | 88 | ⚠️ |
| Unknown | 97.85% | 99.40% | -1.56% | 186 | 167 |  |
| Braintree | 92.35% | 92.43% | -0.08% | 327 | 317 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 12 | 8 |  |
| ProcessOut | 82.18% | 78.46% | +4.74% | 2,087 | 2,047 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 2,240 | 2,151 | 84.62% | 81.88% | +2.74 |
| Insufficient Funds | 352 | 412 | 13.30% | 15.68% | -2.39 |
| Other reasons | 26 | 38 | 0.98% | 1.45% | -0.46 |
| Unknown | 4 | 1 | 0.15% | 0.04% | +0.11 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 25 | 25 | 0.94% | 0.95% | -0.01 |

**Root Cause:** None + Adyen + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 89.13% | 89.79% | -0.74% | 35,070 | 27,488 |  |
| 2_PreDunningAR | 91.42% | 91.78% | -0.39% | 35,070 | 27,488 |  |
| 3_PostDunningAR | 91.82% | 92.2% | -0.41% | 35,070 | 27,488 |  |
| 6_PaymentApprovalRate | 92.2% | 92.46% | -0.29% | 35,070 | 27,488 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| DE | High (>92%) | 6,541 | 7,142 | +9.2% | Stable |
| GB | Medium (>85%) | 5,637 | 8,682 | +54.0% | Stable |
| FR | High (>92%) | 5,182 | 7,156 | +38.1% | Stable |
| AU | Low (>85%) | 2,627 | 2,647 | +0.8% | Stable |
| BE | High (>92%) | 1,437 | 1,796 | +25.0% | Stable |
| NL | High (>92%) | 1,104 | 1,371 | +24.2% | Stable |
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
| NL | ↓ -3.40% | None -100.0% | Unknown -100.0% | Other reasons +2.21pp | None + Unknown + Other |
| AU | ↑ +3.35% | None -100.0% | Adyen -6.5% | Insufficient Funds -2.39pp | None + Adyen + Insufficient |

---

*Report: 2026-04-22*
