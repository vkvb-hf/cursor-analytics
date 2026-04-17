# AR Initial (LL0) Investigation: RTE 2026-W15

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 90.85% → 91.78% (+1.02%)  
**Volume:** 31,091 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) improved from 90.85% to 91.78% (+1.02%) in W15, representing a significant positive change across 31,091 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (91.78% vs 8-wk avg ~92.3%) | +1.02% | ✅ |
| L1: Country Breakdown | 4 countries exceed ±2.5% threshold (TV, TT, TK, TO) | Mixed | ⚠️ |
| L1: Dimension Scan | No payment method or provider exceeds threshold | Stable | ✅ |
| L2: Country Deep-Dives | Root causes identified for flagged countries | Identified | ⚠️ |
| L3: Related Metrics | All funnel metrics improved (+0.85% to +1.02%) | Aligned | ✅ |

**Key Findings:**
- TV declined -3.37% (91.32% from 94.51%) driven by PayPal payment failures (-25.0%) and increased Insufficient Funds declines (+1.34pp)
- TT declined -3.25% (94.95% from 98.15%) due to payment method/provider data issues (None/-100.0%) and spike in "Other reasons" declines (+1.95pp)
- TK improved +5.28% (95.62% from 90.83%) with Adyen performance gains (+6.91%) despite PayPal weakness (-13.33%), primarily from reduced Insufficient Funds (-5.23pp)
- TO improved +6.15% (85.69% from 80.72%) driven by Apple Pay (+7.69%) and Adyen (+8.93%) improvements, with Insufficient Funds declining -4.76pp
- Volume continues downward trend (31,091 vs 46,567 in W08), though mix shift impact remains stable across all countries

**Action:** Monitor - Overall metric is improving and aligned across funnel stages. Continue monitoring TV and TT for PayPal and payment method issues; no escalation required as positive performers (TK, TO) are offsetting declines.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 91.78% | 31,091 | +1.02% ← REPORTED CHANGE |
| 2026-W14 | 90.85% | 31,951 | -0.57% |
| 2026-W13 | 91.37% | 36,416 | -1.29% |
| 2026-W12 | 92.56% | 42,779 | +0.05% |
| 2026-W11 | 92.51% | 46,365 | -0.24% |
| 2026-W10 | 92.73% | 48,166 | -0.92% |
| 2026-W09 | 93.59% | 46,087 | +0.47% |
| 2026-W08 | 93.15% | 46,567 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TV | 91.32% | 94.51% | -3.37% | 334 | ⚠️ |
| TT | 94.95% | 98.15% | -3.25% | 614 | ⚠️ |
| FJ | 91.93% | 91.3% | +0.69% | 19,693 |  |
| YE | 86.49% | 85.26% | +1.45% | 3,006 |  |
| CF | 94.0% | 92.6% | +1.51% | 6,118 |  |
| TK | 95.62% | 90.83% | +5.28% | 297 | ⚠️ |
| TO | 85.69% | 80.72% | +6.15% | 552 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TV, TT, TK, TO

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 95.89% | 98.06% | -2.21% | 1,023 |  |
| Paypal | 95.74% | 95.66% | +0.08% | 3,682 |  |
| Apple Pay | 90.8% | 90.02% | +0.87% | 6,957 |  |
| Credit Card | 91.16% | 89.93% | +1.37% | 19,429 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 78.64% | 79.17% | -0.66% | 103 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 40 |  |
| ProcessOut | 91.72% | 91.41% | +0.34% | 11,281 |  |
| Braintree | 92.48% | 91.68% | +0.88% | 10,759 |  |
| Adyen | 91.12% | 89.2% | +2.15% | 8,908 |  |

---

## L2: TV Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| paypal | 75.0% | 100.0% | -25.00% | 8 | 8 | ⚠️ |
| credit_card | 84.09% | 93.02% | -9.60% | 88 | 86 | ⚠️ |
| klarna | 97.5% | 98.94% | -1.45% | 160 | 188 |  |
| cashcredit | 100.0% | 100.0% | +0.00% | 5 | 2 |  |
| applepay | 87.67% | 85.0% | +3.14% | 73 | 80 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Adyen | 92.74% | 97.08% | -4.47% | 248 | 274 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 5 | 2 |  |
| Braintree | 86.42% | 86.36% | +0.06% | 81 | 88 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 305 | 344 | 91.32% | 94.51% | -3.19 |
| Insufficient Funds | 21 | 18 | 6.29% | 4.95% | +1.34 |
| Other reasons | 5 | 2 | 1.50% | 0.55% | +0.95 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 3 | 0 | 0.90% | 0.00% | +0.90 |

**Root Cause:** paypal + Insufficient

---

## L2: TT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.0% | 0.0% | +0.00% | 4 | 0 |  |
| None | 0.0% | 100.0% | -100.00% | 0 | 1 | ⚠️ |
| sepadirectdebit | 0.0% | 100.0% | -100.00% | 0 | 1 | ⚠️ |
| applepay | 86.96% | 100.0% | -13.04% | 46 | 47 | ⚠️ |
| ideal | 97.45% | 100.0% | -2.55% | 470 | 503 |  |
| klarna | 92.45% | 93.75% | -1.38% | 53 | 48 |  |
| credit_card | 87.5% | 80.65% | +8.50% | 32 | 31 | ⚠️ |
| paypal | 88.89% | 81.25% | +9.40% | 9 | 16 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.0% | 0.0% | +0.00% | 4 | 0 |  |
| No Payment | 0.0% | 100.0% | -100.00% | 0 | 1 | ⚠️ |
| Braintree | 87.27% | 95.24% | -8.36% | 55 | 63 | ⚠️ |
| Adyen | 96.4% | 98.46% | -2.09% | 555 | 583 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 583 | 635 | 94.95% | 98.15% | -3.19 |
| Other reasons | 12 | 0 | 1.95% | 0.00% | +1.95 |
| Insufficient Funds | 10 | 4 | 1.63% | 0.62% | +1.01 |
| Unknown | 4 | 0 | 0.65% | 0.00% | +0.65 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 5 | 8 | 0.81% | 1.24% | -0.42 |

**Root Cause:** None + No + Other

---

## L2: TK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| paypal | 86.67% | 100.0% | -13.33% | 15 | 9 | ⚠️ |
| cashcredit | 100.0% | 100.0% | +0.00% | 3 | 2 |  |
| applepay | 96.61% | 91.89% | +5.13% | 118 | 74 | ⚠️ |
| credit_card | 95.65% | 89.47% | +6.91% | 161 | 133 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 3 | 2 |  |
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
| None | 0.0% | 0.0% | +0.00% | 4 | 0 |  |
| sepadirectdebit | 100.0% | 0.0% | +0.00% | 1 | 0 |  |
| cashcredit | 100.0% | 100.0% | +0.00% | 2 | 6 |  |
| paypal | 98.85% | 95.35% | +3.67% | 87 | 86 |  |
| applepay | 82.35% | 76.47% | +7.69% | 153 | 119 | ⚠️ |
| credit_card | 84.59% | 77.7% | +8.87% | 305 | 287 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.0% | 0.0% | +0.00% | 4 | 0 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 2 | 6 |  |
| Braintree | 88.33% | 84.39% | +4.67% | 240 | 205 |  |
| Adyen | 84.64% | 77.7% | +8.93% | 306 | 287 | ⚠️ |

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
| 1_FirstRunAR | 89.3% | 88.45% | +0.96% | 31,091 | 31,951 |  |
| 2_PreDunningAR | 91.78% | 90.85% | +1.02% | 31,091 | 31,951 |  |
| 3_PostDunningAR | 91.99% | 91.21% | +0.86% | 31,091 | 31,951 |  |
| 6_PaymentApprovalRate | 92.15% | 91.37% | +0.85% | 31,091 | 31,951 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | Medium (>85%) | 20,045 | 19,693 | -1.8% | Stable |
| CF | High (>92%) | 6,067 | 6,118 | +0.8% | Stable |
| YE | Medium (>85%) | 3,650 | 3,006 | -17.6% | Stable |
| TT | High (>92%) | 647 | 614 | -5.1% | Stable |
| TO | Low (>85%) | 498 | 552 | +10.8% | Stable |
| TZ | Medium (>85%) | 462 | 477 | +3.2% | Stable |
| TV | High (>92%) | 364 | 334 | -8.2% | Stable |
| TK | Medium (>85%) | 218 | 297 | +36.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TV | ↓ -3.37% | paypal -25.0% | → Stable | Insufficient Funds +1.34pp | paypal + Insufficient |
| TT | ↓ -3.25% | None -100.0% | No Payment -100.0% | Other reasons +1.95pp | None + No + Other |
| TK | ↑ +5.28% | paypal -13.3% | Adyen +6.9% | Insufficient Funds -5.23pp | paypal + Adyen + Insufficient |
| TO | ↑ +6.15% | applepay +7.7% | Adyen +8.9% | Insufficient Funds -4.76pp | applepay + Adyen + Insufficient |

---

*Report: 2026-04-17*
