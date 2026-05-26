# AR Initial (LL0) Investigation: HF-INTL 2026-W21

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 92.7% → 92.39% (-0.33%)  
**Volume:** 29,294 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate for HF-INTL declined by -0.33pp (92.7% → 92.39%) in W21, a change that is **not statistically significant** based on 29,294 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 8-Week Trend Stability | Rate within historical range (89.57%-92.71%) | -0.33pp | ✅ Normal fluctuation |
| Country Concentration | 4 countries flagged (LU, CH, SE, NO) | Mixed | ⚠️ Small market volatility |
| Payment Method Impact | No method exceeds ±2.5% threshold | -1.16pp max | ✅ Stable |
| Payment Provider Impact | No provider exceeds ±2.5% threshold | -1.37pp max | ✅ Stable |
| Related Metrics Alignment | All funnel metrics declined similarly | -0.16% to -0.34% | ✅ Consistent pattern |

**Key Findings:**
- **LU** showed the largest decline (-10.33pp), but with only 52 orders, this represents high volatility in a low-volume market; root cause linked to "Insufficient Funds" increase (+7.69pp)
- **CH** declined -6.23pp (94 orders) driven by credit_card payment method drop (-26.83%) and Adyen provider issues (-100% on 1 transaction)
- **SE** declined -4.33pp (890 orders) with ProcessOut showing -9.08% decline and "Insufficient Funds" increasing +2.18pp
- **NO** improved +2.59pp (511 orders), offsetting some decline, with Braintree improving +6.18%
- Mix shift analysis shows **LU volume dropped -26.8%** (71→52 orders), which partially explains the rate volatility

**Action:** **Monitor** — The overall decline is not statistically significant, and the flagged countries (LU, CH) have very low volumes (<100 orders). Continue monitoring SE (890 orders) for ProcessOut performance and "Insufficient Funds" trends in W22.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W21 | 92.39% | 29,294 | -0.33% ← REPORTED CHANGE |
| 2026-W20 | 92.7% | 29,460 | -0.01% |
| 2026-W19 | 92.71% | 31,823 | +2.19% |
| 2026-W18 | 90.72% | 27,243 | -0.57% |
| 2026-W17 | 91.24% | 31,344 | +0.46% |
| 2026-W16 | 90.82% | 33,075 | -0.48% |
| 2026-W15 | 91.26% | 25,710 | +1.89% |
| 2026-W14 | 89.57% | 29,851 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| LU | 84.62% | 94.37% | -10.33% | 52 | ⚠️ |
| CH | 86.17% | 91.89% | -6.23% | 94 | ⚠️ |
| SE | 90.34% | 94.43% | -4.33% | 890 | ⚠️ |
| GB | 91.78% | 92.50% | -0.78% | 7,638 |  |
| DE | 95.12% | 95.41% | -0.31% | 5,898 |  |
| AU | 84.49% | 83.78% | +0.84% | 2,463 |  |
| NO | 92.37% | 90.03% | +2.59% | 511 | ⚠️ |

**Countries exceeding ±2.5% threshold:** LU, CH, SE, NO

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 96.1% | 97.23% | -1.16% | 5,543 |  |
| Others | 96.62% | 97.16% | -0.56% | 5,207 |  |
| Credit Card | 90.96% | 91.2% | -0.27% | 9,597 |  |
| Apple Pay | 89.16% | 89.25% | -0.11% | 8,947 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 93.55% | 94.85% | -1.37% | 1,442 |  |
| Adyen | 96.94% | 97.54% | -0.62% | 4,046 |  |
| Braintree | 92.9% | 93.42% | -0.55% | 13,394 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 68 |  |
| ProcessOut | 89.73% | 89.65% | +0.09% | 10,344 |  |

---

## L2: LU Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 100.00% | 0.00% | +0.00% | 7 | 0 |  |
| None | 0.00% | 100.00% | -100.00% | 0 | 8 | ⚠️ |
| sepadirectdebit | 0.00% | 100.00% | -100.00% | 0 | 4 | ⚠️ |
| applepay | 78.95% | 100.00% | -21.05% | 19 | 22 | ⚠️ |
| credit_card | 76.47% | 92.59% | -17.41% | 17 | 27 | ⚠️ |
| paypal | 100.00% | 80.00% | +25.00% | 9 | 10 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| ProcessOut | 0.00% | 100.00% | -100.00% | 0 | 2 | ⚠️ |
| Adyen | 76.47% | 93.10% | -17.86% | 17 | 29 | ⚠️ |
| Braintree | 85.71% | 93.75% | -8.57% | 28 | 32 | ⚠️ |
| Unknown | 100.00% | 100.00% | +0.00% | 7 | 8 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 44 | 67 | 84.62% | 94.37% | -9.75 |
| Insufficient Funds | 4 | 0 | 7.69% | 0.00% | +7.69 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 2 | 2 | 3.85% | 2.82% | +1.03 |
| Other reasons | 2 | 2 | 3.85% | 2.82% | +1.03 |

**Root Cause:** None + ProcessOut + Insufficient

---

## L2: CH Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| credit_card | 73.17% | 100.00% | -26.83% | 41 | 57 | ⚠️ |
| cashcredit | 100.00% | 100.00% | +0.00% | 2 | 1 |  |
| paypal | 94.74% | 94.12% | +0.66% | 19 | 17 |  |
| applepay | 96.88% | 77.78% | +24.55% | 32 | 36 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Adyen | 0.00% | 100.00% | -100.00% | 0 | 1 | ⚠️ |
| ProcessOut | 73.17% | 100.00% | -26.83% | 41 | 56 | ⚠️ |
| No Payment | 100.00% | 100.00% | +0.00% | 2 | 1 |  |
| Braintree | 96.08% | 83.02% | +15.73% | 51 | 53 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 81 | 102 | 86.17% | 91.89% | -5.72 |
| Insufficient Funds | 10 | 8 | 10.64% | 7.21% | +3.43 |
| Other reasons | 2 | 0 | 2.13% | 0.00% | +2.13 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 1 | 1 | 1.06% | 0.90% | +0.16 |

**Root Cause:** credit_card + Adyen + Insufficient

---

## L2: SE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 99.23% | 0.00% | +0.00% | 130 | 0 |  |
| None | 0.00% | 98.90% | -100.00% | 0 | 91 | ⚠️ |
| paypal | 66.67% | 100.00% | -33.33% | 18 | 13 | ⚠️ |
| credit_card | 83.09% | 91.74% | -9.42% | 207 | 242 | ⚠️ |
| applepay | 81.18% | 85.78% | -5.36% | 186 | 204 | ⚠️ |
| klarna | 97.41% | 100.00% | -2.59% | 348 | 344 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 1 | 3 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| ProcessOut | 83.25% | 91.56% | -9.08% | 203 | 237 | ⚠️ |
| Braintree | 79.90% | 86.64% | -7.77% | 204 | 217 | ⚠️ |
| Adyen | 97.84% | 100.00% | -2.16% | 464 | 426 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 1 | 3 |  |
| Unknown | 94.44% | 92.86% | +1.71% | 18 | 14 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 804 | 847 | 90.34% | 94.43% | -4.09 |
| Insufficient Funds | 67 | 48 | 7.53% | 5.35% | +2.18 |
| Other reasons | 11 | 0 | 1.24% | 0.00% | +1.24 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 7 | 1 | 0.79% | 0.11% | +0.68 |
| Unknown | 1 | 1 | 0.11% | 0.11% | +0.00 |

**Root Cause:** None + ProcessOut + Insufficient

---

## L2: NO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 100.00% | 0.00% | +0.00% | 62 | 0 |  |
| None | 0.00% | 98.86% | -100.00% | 0 | 176 | ⚠️ |
| cashcredit | 0.00% | 100.00% | -100.00% | 0 | 1 | ⚠️ |
| paypal | 80.95% | 81.82% | -1.06% | 21 | 11 |  |
| credit_card | 94.97% | 91.63% | +3.64% | 298 | 227 |  |
| applepay | 84.62% | 79.04% | +7.05% | 130 | 167 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| No Payment | 0.00% | 100.00% | -100.00% | 0 | 1 | ⚠️ |
| Adyen | 100.00% | 100.00% | +0.00% | 54 | 41 |  |
| Unknown | 100.00% | 98.59% | +1.43% | 18 | 142 |  |
| ProcessOut | 94.79% | 91.36% | +3.75% | 288 | 220 |  |
| Braintree | 84.11% | 79.21% | +6.18% | 151 | 178 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Insufficient Funds | 32 | 52 | 6.26% | 8.93% | -2.67 |
| 1. SUCCESSFULL | 472 | 524 | 92.37% | 90.03% | +2.33 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 5 | 3 | 0.98% | 0.52% | +0.46 |
| Unknown | 0 | 1 | 0.00% | 0.17% | -0.17 |
| Other reasons | 2 | 2 | 0.39% | 0.34% | +0.05 |

**Root Cause:** None + No + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.52% | 90.67% | -0.16% | 29,294 | 29,460 |  |
| 2_PreDunningAR | 92.39% | 92.7% | -0.34% | 29,294 | 29,460 |  |
| 3_PostDunningAR | 92.89% | 93.17% | -0.30% | 29,294 | 29,460 |  |
| 6_PaymentApprovalRate | 93.19% | 93.4% | -0.23% | 29,294 | 29,460 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | High (>92%) | 8,690 | 7,638 | -12.1% | Stable |
| FR | High (>92%) | 5,359 | 5,527 | +3.1% | Stable |
| DE | High (>92%) | 5,146 | 5,898 | +14.6% | Stable |
| AU | Low (>85%) | 2,584 | 2,463 | -4.7% | Stable |
| BE | High (>92%) | 1,579 | 1,680 | +6.4% | Stable |
| IE | Medium (>85%) | 1,264 | 1,429 | +13.1% | Stable |
| NL | High (>92%) | 1,240 | 1,100 | -11.3% | Stable |
| DK | High (>92%) | 904 | 814 | -10.0% | Stable |
| SE | High (>92%) | 897 | 890 | -0.8% | Stable |
| NZ | Low (>85%) | 744 | 726 | -2.4% | Stable |
| NO | Medium (>85%) | 582 | 511 | -12.2% | Stable |
| AT | High (>92%) | 289 | 472 | +63.3% | Stable |
| CH | Medium (>85%) | 111 | 94 | -15.3% | Stable |
| LU | High (>92%) | 71 | 52 | -26.8% | ⚠️ Volume drop |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| LU | ↓ -10.33% | None -100.0% | ProcessOut -100.0% | Insufficient Funds +7.69pp | None + ProcessOut + Insufficient |
| CH | ↓ -6.23% | credit_card -26.8% | Adyen -100.0% | Insufficient Funds +3.43pp | credit_card + Adyen + Insufficient |
| SE | ↓ -4.33% | None -100.0% | ProcessOut -9.1% | Insufficient Funds +2.18pp | None + ProcessOut + Insufficient |
| NO | ↑ +2.59% | None -100.0% | No Payment -100.0% | Insufficient Funds -2.67pp | None + No + Insufficient |

---

*Report: 2026-05-26*
