# AR Initial (LL0) Investigation: RTE 2026-W15

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 91.73% → 92.56% (+0.90%)  
**Volume:** 32,099 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) improved from 91.73% to 92.56% (+0.90pp) in 2026-W15, though this change is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | Rate within normal 8-week range (90.83%-93.59%) | +0.90pp | ✅ |
| L1: Country Breakdown | 3 countries exceed ±2.5% threshold (TV, TK, TO) | Mixed | ⚠️ |
| L1: Dimension Scan | PaymentProvider "Unknown" flagged (+6.85%) but low volume (103) | +6.85pp | ⚠️ |
| L2: Country Deep-Dives | TV declined (-3.36%), TK (+5.28%) and TO (+6.15%) improved | Mixed | ⚠️ |
| L3: Related Metrics | All funnel metrics improved consistently (+0.79% to +0.99%) | Positive | ✅ |
| Mix Shift | TK volume increased +36.2% but impact remains stable | Stable | ✅ |

**Key Findings:**
- TV experienced the largest decline (-3.36pp), driven by PayPal acceptance dropping from 100% to 75% (8 orders) and credit card declining -9.60pp, with Insufficient Funds increasing +1.33pp
- TK showed strong improvement (+5.28pp) primarily from Adyen provider (+6.91pp) and reduced Insufficient Funds declines (-5.23pp), despite PayPal dropping -13.33pp on low volume
- TO improved significantly (+6.15pp) driven by Apple Pay (+7.69pp) and Adyen (+8.93pp), with Insufficient Funds declines decreasing -4.76pp
- All related metrics (FirstRunAR, PreDunningAR, PostDunningAR, PaymentApprovalRate) show aligned improvement between +0.79% and +0.99%, indicating systemic improvement rather than isolated anomaly
- Overall volume decreased from 46,087 (W09) to 32,099 (W16), a downward trend worth monitoring separately

**Action:** Monitor — The overall improvement is not statistically significant, and country-level fluctuations are occurring on relatively low volumes (TV: 334, TK: 297, TO: 552). Continue tracking TV's PayPal and credit card performance over the next 2 weeks.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 92.56% | 32,099 | +0.90% |
| 2026-W15 | 91.73% | 30,171 | +0.99% ← REPORTED CHANGE |
| 2026-W14 | 90.83% | 31,907 | -0.66% |
| 2026-W13 | 91.43% | 36,491 | -1.22% |
| 2026-W12 | 92.56% | 42,779 | +0.05% |
| 2026-W11 | 92.51% | 46,365 | -0.23% |
| 2026-W10 | 92.72% | 48,166 | -0.93% |
| 2026-W09 | 93.59% | 46,087 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TV | 91.32% | 94.49% | -3.36% | 334 | ⚠️ |
| TT | 95.60% | 97.99% | -2.44% | 614 |  |
| FJ | 91.84% | 91.28% | +0.61% | 18,773 |  |
| CF | 94.00% | 92.60% | +1.51% | 6,117 |  |
| YE | 86.50% | 85.18% | +1.55% | 3,007 |  |
| TK | 95.62% | 90.83% | +5.28% | 297 | ⚠️ |
| TO | 85.69% | 80.72% | +6.15% | 552 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TV, TK, TO

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 96.38% | 97.62% | -1.27% | 1,022 |  |
| Paypal | 95.67% | 95.58% | +0.09% | 3,555 |  |
| Apple Pay | 90.6% | 89.91% | +0.77% | 6,637 |  |
| Credit Card | 91.14% | 89.96% | +1.31% | 18,957 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 40 |  |
| ProcessOut | 91.67% | 91.47% | +0.22% | 10,817 |  |
| Braintree | 92.37% | 91.58% | +0.86% | 10,304 |  |
| Adyen | 91.16% | 89.19% | +2.22% | 8,907 |  |
| Unknown | 79.61% | 74.51% | +6.85% | 103 | ⚠️ |

---

## L2: TV Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| paypal | 75.00% | 100.00% | -25.00% | 8 | 8 | ⚠️ |
| credit_card | 84.09% | 93.02% | -9.60% | 88 | 86 | ⚠️ |
| klarna | 97.50% | 98.94% | -1.45% | 160 | 188 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 5 | 2 |  |
| applepay | 87.67% | 84.81% | +3.37% | 73 | 79 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Adyen | 92.74% | 97.08% | -4.47% | 248 | 274 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 5 | 2 |  |
| Braintree | 86.42% | 86.21% | +0.25% | 81 | 87 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 305 | 343 | 91.32% | 94.49% | -3.17 |
| Insufficient Funds | 21 | 18 | 6.29% | 4.96% | +1.33 |
| Other reasons | 5 | 2 | 1.50% | 0.55% | +0.95 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 3 | 0 | 0.90% | 0.00% | +0.90 |

**Root Cause:** paypal + Insufficient

---

## L2: TK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| paypal | 86.67% | 100.00% | -13.33% | 15 | 9 | ⚠️ |
| cashcredit | 100.00% | 100.00% | +0.00% | 3 | 2 |  |
| applepay | 96.61% | 91.89% | +5.13% | 118 | 74 | ⚠️ |
| credit_card | 95.65% | 89.47% | +6.91% | 161 | 133 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| No Payment | 100.00% | 100.00% | +0.00% | 3 | 2 |  |
| Braintree | 95.49% | 92.77% | +2.93% | 133 | 83 |  |
| Adyen | 95.65% | 89.47% | +6.91% | 161 | 133 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Insufficient Funds | 9 | 18 | 3.03% | 8.26% | -5.23 |
| 1. SUCCESSFULL | 284 | 198 | 95.62% | 90.83% | +4.80 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 2 | 1 | 0.67% | 0.46% | +0.21 |
| Other reasons | 2 | 1 | 0.67% | 0.46% | +0.21 |

**Root Cause:** paypal + Adyen + Insufficient

---

## L2: TO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 4 | 0 |  |
| sepadirectdebit | 100.00% | 0.00% | +0.00% | 1 | 0 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 2 | 6 |  |
| paypal | 98.85% | 95.35% | +3.67% | 87 | 86 |  |
| applepay | 82.35% | 76.47% | +7.69% | 153 | 119 | ⚠️ |
| credit_card | 84.59% | 77.70% | +8.87% | 305 | 287 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 0.00% | +0.00% | 4 | 0 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 2 | 6 |  |
| Braintree | 88.33% | 84.39% | +4.67% | 240 | 205 |  |
| Adyen | 84.64% | 77.70% | +8.93% | 306 | 287 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 473 | 402 | 85.69% | 80.72% | +4.97 |
| Insufficient Funds | 38 | 58 | 6.88% | 11.65% | -4.76 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 17 | 19 | 3.08% | 3.82% | -0.74 |
| Unknown | 4 | 0 | 0.72% | 0.00% | +0.72 |
| Other reasons | 20 | 19 | 3.62% | 3.82% | -0.19 |

**Root Cause:** applepay + Adyen + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 89.19% | 88.48% | +0.80% | 30,171 | 31,907 |  |
| 2_PreDunningAR | 91.73% | 90.83% | +0.99% | 30,171 | 31,907 |  |
| 3_PostDunningAR | 91.96% | 91.21% | +0.82% | 30,171 | 31,907 |  |
| 6_PaymentApprovalRate | 92.1% | 91.37% | +0.79% | 30,171 | 31,907 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | Medium (>85%) | 20,002 | 18,773 | -6.1% | Stable |
| CF | High (>92%) | 6,066 | 6,117 | +0.8% | Stable |
| YE | Medium (>85%) | 3,651 | 3,007 | -17.6% | Stable |
| TT | High (>92%) | 647 | 614 | -5.1% | Stable |
| TO | Low (>85%) | 498 | 552 | +10.8% | Stable |
| TZ | Medium (>85%) | 462 | 477 | +3.2% | Stable |
| TV | High (>92%) | 363 | 334 | -8.0% | Stable |
| TK | Medium (>85%) | 218 | 297 | +36.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TV | ↓ -3.36% | paypal -25.0% | → Stable | Insufficient Funds +1.33pp | paypal + Insufficient |
| TK | ↑ +5.28% | paypal -13.3% | Adyen +6.9% | Insufficient Funds -5.23pp | paypal + Adyen + Insufficient |
| TO | ↑ +6.15% | applepay +7.7% | Adyen +8.9% | Insufficient Funds -4.76pp | applepay + Adyen + Insufficient |

---

*Report: 2026-04-22*
