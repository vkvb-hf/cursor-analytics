# AR Initial (LL0) Investigation: HF-INTL 2026-W19

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 91.1% → 92.73% (+1.79%)  
**Volume:** 31,928 orders  
**Significance:** Significant

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) for HF-INTL improved significantly from 91.1% to 92.73% (+1.79%) in W19, driven by broad-based gains across multiple European markets.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 8-Week Trend Stability | Rate at 8-week high (92.73%) | +1.79% vs prior week | ✅ |
| Country Concentration | 5 countries exceeded ±2.5% threshold | DE +3.31%, SE +3.90%, IE +4.33%, CH +5.31%, LU +8.58% | ⚠️ |
| Payment Method Impact | Apple Pay improved significantly | +3.06% (9,723 vol) | ⚠️ |
| Payment Provider Impact | Braintree improved, Unknown declined | Braintree +2.53%, Unknown -3.50% | ⚠️ |
| Decline Reason Shift | Insufficient Funds declined across markets | DE -2.00pp, SE -2.95pp, IE -3.32pp, CH -5.59pp | ✅ |
| Related Metrics Alignment | All funnel metrics improved consistently | 1_FirstRunAR +2.05%, PostDunningAR +1.56% | ✅ |

**Key Findings:**
- DE showed the largest volume impact with +98.1% volume growth (4,122 → 8,164 orders) while improving AR by +3.31pp, with credit_card acceptance surging +13.47% and ProcessOut +13.51%
- Insufficient Funds declines dropped materially across all flagged countries: CH (-5.59pp), IE (-3.32pp), SE (-2.95pp), DE (-2.00pp) — suggesting improved customer payment ability or better card validation
- Apple Pay acceptance improved +3.06% globally (9,723 orders) with notable gains in SE (+10.42%), CH (+5.13%), and IE (+7.16%)
- Braintree provider performance improved +2.53% (15,597 orders) with particularly strong gains in SE (+10.46%) and IE (+6.05%)
- Mix shift analysis shows all countries remained stable despite significant volume changes in DE (+98.1%) and NL (+78.0%)

**Action:** Monitor — This is a positive improvement driven by reduced Insufficient Funds declines and improved Apple Pay/Braintree performance. Continue monitoring to confirm trend sustainability, particularly in DE given the significant volume increase.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W19 | 92.73% | 31,928 | +1.79% ← REPORTED CHANGE |
| 2026-W18 | 91.1% | 27,123 | -0.25% |
| 2026-W17 | 91.33% | 31,359 | +0.19% |
| 2026-W16 | 91.16% | 32,858 | -0.32% |
| 2026-W15 | 91.45% | 25,706 | +2.08% |
| 2026-W14 | 89.59% | 29,797 | -0.34% |
| 2026-W13 | 89.9% | 33,681 | -1.25% |
| 2026-W12 | 91.04% | 38,253 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| GB | 92.97% | 91.12% | +2.03% | 8,181 |  |
| DE | 95.24% | 92.19% | +3.31% | 8,164 | ⚠️ |
| SE | 95.77% | 92.17% | +3.90% | 1,087 | ⚠️ |
| IE | 91.20% | 87.42% | +4.33% | 1,296 | ⚠️ |
| CH | 91.06% | 86.47% | +5.31% | 123 | ⚠️ |
| LU | 91.55% | 84.31% | +8.58% | 71 | ⚠️ |

**Countries exceeding ±2.5% threshold:** DE, SE, IE, CH, LU

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 96.35% | 97.06% | -0.73% | 5,257 |  |
| Paypal | 97.38% | 96.49% | +0.93% | 7,066 |  |
| Credit Card | 90.03% | 88.85% | +1.33% | 9,882 |  |
| Apple Pay | 90.15% | 87.47% | +3.06% | 9,723 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 91.83% | 95.15% | -3.50% | 1,468 | ⚠️ |
| No Payment | 100.0% | 100.0% | +0.00% | 81 |  |
| Adyen | 97.49% | 97.45% | +0.05% | 4,350 |  |
| ProcessOut | 88.59% | 87.68% | +1.05% | 10,432 |  |
| Braintree | 94.22% | 91.9% | +2.53% | 15,597 | ⚠️ |

---

## L2: DE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 51.08% | 0.00% | +0.00% | 139 | 0 |  |
| None | 0.00% | 57.45% | -100.00% | 0 | 94 | ⚠️ |
| cashcredit | 100.00% | 100.00% | +0.00% | 32 | 14 |  |
| paypal | 98.22% | 97.07% | +1.19% | 5,014 | 2,628 |  |
| applepay | 93.46% | 90.01% | +3.83% | 1,636 | 861 |  |
| klarna | 99.28% | 95.45% | +4.00% | 415 | 22 |  |
| credit_card | 86.85% | 76.54% | +13.47% | 928 | 503 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 48.09% | 55.56% | -13.44% | 131 | 90 | ⚠️ |
| No Payment | 100.00% | 100.00% | +0.00% | 32 | 14 |  |
| Braintree | 97.05% | 95.33% | +1.81% | 6,650 | 3,489 |  |
| Adyen | 99.11% | 96.77% | +2.41% | 447 | 31 |  |
| ProcessOut | 86.62% | 76.31% | +13.51% | 904 | 498 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 7,775 | 3,800 | 95.24% | 92.19% | +3.05 |
| Insufficient Funds | 175 | 171 | 2.14% | 4.15% | -2.00 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 115 | 89 | 1.41% | 2.16% | -0.75 |
| Other reasons | 32 | 23 | 0.39% | 0.56% | -0.17 |
| Unknown | 67 | 39 | 0.82% | 0.95% | -0.13 |

**Root Cause:** None + Unknown + Insufficient

---

## L2: SE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 97.37% | 0.00% | +0.00% | 114 | 0 |  |
| None | 0.00% | 96.71% | -100.00% | 0 | 152 | ⚠️ |
| cashcredit | 100.00% | 100.00% | +0.00% | 1 | 6 |  |
| klarna | 99.12% | 97.86% | +1.29% | 455 | 420 |  |
| credit_card | 93.26% | 88.93% | +4.87% | 267 | 262 |  |
| applepay | 92.02% | 83.33% | +10.42% | 238 | 234 | ⚠️ |
| paypal | 83.33% | 75.00% | +11.11% | 12 | 12 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 75.00% | 80.00% | -6.25% | 12 | 25 | ⚠️ |
| No Payment | 100.00% | 100.00% | +0.00% | 1 | 6 |  |
| Adyen | 99.12% | 98.19% | +0.94% | 567 | 553 |  |
| ProcessOut | 93.39% | 89.06% | +4.85% | 257 | 256 |  |
| Braintree | 91.60% | 82.93% | +10.46% | 250 | 246 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,041 | 1,001 | 95.77% | 92.17% | +3.60 |
| Insufficient Funds | 34 | 66 | 3.13% | 6.08% | -2.95 |
| Other reasons | 5 | 10 | 0.46% | 0.92% | -0.46 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 4 | 6 | 0.37% | 0.55% | -0.18 |
| Unknown | 3 | 3 | 0.28% | 0.28% | +0.00 |

**Root Cause:** None + Unknown + Insufficient

---

## L2: IE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 97.55% | 0.00% | +0.00% | 204 | 0 |  |
| None | 0.00% | 98.41% | -100.00% | 0 | 189 | ⚠️ |
| cashcredit | 0.00% | 100.00% | -100.00% | 0 | 1 | ⚠️ |
| paypal | 97.14% | 97.14% | +0.00% | 105 | 105 |  |
| credit_card | 88.81% | 85.48% | +3.90% | 536 | 599 |  |
| applepay | 89.80% | 83.80% | +7.16% | 451 | 537 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| No Payment | 0.00% | 100.00% | -100.00% | 0 | 1 | ⚠️ |
| Unknown | 95.65% | 96.74% | -1.12% | 92 | 92 |  |
| Adyen | 96.12% | 95.54% | +0.62% | 129 | 112 |  |
| ProcessOut | 89.21% | 85.96% | +3.78% | 519 | 584 |  |
| Braintree | 91.19% | 85.98% | +6.05% | 556 | 642 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,182 | 1,251 | 91.20% | 87.42% | +3.78 |
| Insufficient Funds | 81 | 137 | 6.25% | 9.57% | -3.32 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 7 | 15 | 0.54% | 1.05% | -0.51 |
| Unknown | 4 | 2 | 0.31% | 0.14% | +0.17 |
| Other reasons | 22 | 26 | 1.70% | 1.82% | -0.12 |

**Root Cause:** None + No + Insufficient

---

## L2: CH Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| paypal | 88.89% | 91.30% | -2.65% | 27 | 23 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 1 | 2 |  |
| applepay | 94.87% | 90.24% | +5.13% | 39 | 41 | ⚠️ |
| credit_card | 89.29% | 82.09% | +8.77% | 56 | 67 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Adyen | 100.00% | 0.00% | +0.00% | 1 | 0 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 1 | 2 |  |
| Braintree | 92.42% | 90.63% | +1.99% | 66 | 64 |  |
| ProcessOut | 89.09% | 82.09% | +8.53% | 55 | 67 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Insufficient Funds | 7 | 15 | 5.69% | 11.28% | -5.59 |
| 1. SUCCESSFULL | 112 | 115 | 91.06% | 86.47% | +4.59 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 3 | 2 | 2.44% | 1.50% | +0.94 |
| Other reasons | 1 | 1 | 0.81% | 0.75% | +0.06 |

**Root Cause:** applepay + ProcessOut + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.64% | 88.82% | +2.05% | 31,928 | 27,123 |  |
| 2_PreDunningAR | 92.73% | 91.1% | +1.79% | 31,928 | 27,123 |  |
| 3_PostDunningAR | 93.16% | 91.73% | +1.56% | 31,928 | 27,123 |  |
| 6_PaymentApprovalRate | 93.42% | 92.02% | +1.52% | 31,928 | 27,123 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | Medium (>85%) | 7,749 | 8,181 | +5.6% | Stable |
| FR | High (>92%) | 4,609 | 4,079 | -11.5% | Stable |
| DE | High (>92%) | 4,122 | 8,164 | +98.1% | Stable |
| AU | Low (>85%) | 2,870 | 2,867 | -0.1% | Stable |
| BE | High (>92%) | 1,523 | 1,829 | +20.1% | Stable |
| IE | Medium (>85%) | 1,431 | 1,296 | -9.4% | Stable |
| SE | High (>92%) | 1,086 | 1,087 | +0.1% | Stable |
| DK | High (>92%) | 998 | 1,043 | +4.5% | Stable |
| NO | Medium (>85%) | 787 | 718 | -8.8% | Stable |
| NL | High (>92%) | 783 | 1,394 | +78.0% | Stable |
| NZ | Low (>85%) | 694 | 632 | -8.9% | Stable |
| AT | Medium (>85%) | 287 | 444 | +54.7% | Stable |
| CH | Medium (>85%) | 133 | 123 | -7.5% | Stable |
| LU | Low (>85%) | 51 | 71 | +39.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| DE | ↑ +3.31% | None -100.0% | Unknown -13.4% | Insufficient Funds -2.00pp | None + Unknown + Insufficient |
| SE | ↑ +3.90% | None -100.0% | Unknown -6.2% | Insufficient Funds -2.95pp | None + Unknown + Insufficient |
| IE | ↑ +4.33% | None -100.0% | No Payment -100.0% | Insufficient Funds -3.32pp | None + No + Insufficient |
| CH | ↑ +5.31% | applepay +5.1% | ProcessOut +8.5% | Insufficient Funds -5.59pp | applepay + ProcessOut + Insufficient |

---

*Report: 2026-05-12*
