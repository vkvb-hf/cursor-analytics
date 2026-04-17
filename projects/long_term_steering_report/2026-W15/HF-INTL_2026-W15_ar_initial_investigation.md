# AR Initial (LL0) Investigation: HF-INTL 2026-W15

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 89.67% → 91.78% (+2.35%)  
**Volume:** 27,516 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) for HF-INTL improved significantly from 89.67% to 91.78% (+2.35%) in 2026-W15, representing a positive recovery after two consecutive weeks of decline.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 8-Week Trend Stability | Rate within historical range (88.09%-91.78%) | +2.35% vs prior week | ✅ |
| Volume Change | 27,516 vs 30,838 prior week | -10.8% volume drop | ⚠️ |
| Country Concentration | 7 countries exceeding ±2.5% threshold | FR, DE, BE, AT, DK, NZ, LU all positive | ⚠️ |
| Payment Method Impact | Apple Pay +2.87%, Credit Card +3.38% | Both improving | ✅ |
| Provider Performance | Braintree +2.62%, ProcessOut +3.37% | Both improving | ✅ |
| Decline Reason Shift | Insufficient Funds declining across markets | FR -2.39pp, DE -2.25pp, BE -3.23pp, AT -3.89pp | ✅ |

**Key Findings:**
- Widespread reduction in "Insufficient Funds" declines across all analyzed markets: FR (-2.39pp), DE (-2.25pp), BE (-3.23pp), and AT (-3.89pp) drove the overall AR improvement
- Apple Pay performance improved significantly across multiple countries: FR (+5.11%), DE (+5.70%), BE (+6.14%), AT (+3.98%)
- ProcessOut provider showed strong gains in BE (+8.10%) and AT (+6.22%), while credit card acceptance in DE surged +20.68%
- Significant volume declines observed in high-AR markets: NL (-40.8%), FR (-30.4%), and NZ (-36.5%) may be contributing to favorable mix shift
- All related metrics in the LL0 funnel improved in parallel: FirstRunAR (+2.63%), PostDunningAR (+2.11%), PaymentApprovalRate (+2.05%)

**Action:** Monitor — The improvement appears driven by genuine decline rate reductions (particularly Insufficient Funds) rather than anomalies. Continue monitoring volume trends in FR and NL to ensure mix shift is not masking underlying issues.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 91.78% | 27,516 | +2.35% ← REPORTED CHANGE |
| 2026-W14 | 89.67% | 30,838 | -0.53% |
| 2026-W13 | 90.15% | 34,526 | -1.16% |
| 2026-W12 | 91.21% | 39,195 | -0.36% |
| 2026-W11 | 91.54% | 42,802 | +1.25% |
| 2026-W10 | 90.41% | 47,616 | +2.63% |
| 2026-W09 | 88.09% | 46,657 | -2.36% |
| 2026-W08 | 90.22% | 46,415 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| FR | 94.98% | 92.24% | +2.97% | 5,183 | ⚠️ |
| DE | 94.13% | 91.15% | +3.27% | 6,544 | ⚠️ |
| BE | 94.58% | 90.92% | +4.02% | 1,438 | ⚠️ |
| AT | 92.99% | 89.32% | +4.10% | 670 | ⚠️ |
| DK | 94.13% | 90.2% | +4.37% | 1,074 | ⚠️ |
| NZ | 77.7% | 72.47% | +7.21% | 408 | ⚠️ |
| LU | 93.88% | 84.85% | +10.64% | 49 | ⚠️ |

**Countries exceeding ±2.5% threshold:** FR, DE, BE, AT, DK, NZ, LU

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 97.28% | 97.88% | -0.62% | 4,263 |  |
| Paypal | 96.63% | 95.55% | +1.13% | 5,722 |  |
| Apple Pay | 88.21% | 85.75% | +2.87% | 7,956 | ⚠️ |
| Credit Card | 89.39% | 86.47% | +3.38% | 9,575 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 96.07% | 98.18% | -2.15% | 1,884 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 69 |  |
| Adyen | 97.22% | 97.0% | +0.22% | 2,478 |  |
| Braintree | 92.95% | 90.58% | +2.62% | 12,681 | ⚠️ |
| ProcessOut | 88.22% | 85.34% | +3.37% | 10,404 | ⚠️ |

---

## L2: FR Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 16.67% | 0.0% | +0.00% | 6 | 0 |  |
| None | 0.0% | 0.0% | +0.00% | 0 | 10 |  |
| cashcredit | 100.0% | 100.0% | +0.00% | 3 | 5 |  |
| paypal | 96.79% | 96.58% | +0.22% | 655 | 995 |  |
| credit_card | 94.79% | 92.46% | +2.51% | 3,030 | 4,219 |  |
| applepay | 94.9% | 90.28% | +5.11% | 1,489 | 2,223 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.0% | 0.0% | +0.00% | 5 | 10 |  |
| Adyen | 92.59% | 95.45% | -3.00% | 27 | 22 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 3 | 5 |  |
| ProcessOut | 94.81% | 92.45% | +2.55% | 3,004 | 4,197 |  |
| Braintree | 95.48% | 92.23% | +3.52% | 2,144 | 3,218 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 4,923 | 6,874 | 94.98% | 92.24% | +2.74 |
| Insufficient Funds | 164 | 414 | 3.16% | 5.56% | -2.39 |
| Other reasons | 64 | 105 | 1.23% | 1.41% | -0.17 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 30 | 54 | 0.58% | 0.72% | -0.15 |
| PROVIDER_ERROR: failure executing charge with provider | 0 | 5 | 0.00% | 0.07% | -0.07 |
| Unknown | 2 | 0 | 0.04% | 0.00% | +0.04 |

**Root Cause:** applepay + Insufficient

---

## L2: DE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 9.09% | 0.0% | +0.00% | 44 | 0 |  |
| None | 0.0% | 68.75% | -100.00% | 0 | 32 | ⚠️ |
| klarna | 98.47% | 100.0% | -1.53% | 392 | 219 |  |
| cashcredit | 100.0% | 100.0% | +0.00% | 33 | 12 |  |
| paypal | 97.39% | 96.31% | +1.13% | 3,835 | 2,627 |  |
| applepay | 92.15% | 87.18% | +5.70% | 1,337 | 772 | ⚠️ |
| credit_card | 85.27% | 70.66% | +20.68% | 903 | 576 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 9.09% | 66.67% | -86.36% | 44 | 30 | ⚠️ |
| Adyen | 98.25% | 99.56% | -1.31% | 401 | 225 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 33 | 13 |  |
| Braintree | 96.04% | 94.23% | +1.91% | 5,172 | 3,399 |  |
| ProcessOut | 85.23% | 70.58% | +20.77% | 894 | 571 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 6,160 | 3,863 | 94.13% | 91.15% | +2.98 |
| Insufficient Funds | 205 | 228 | 3.13% | 5.38% | -2.25 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 116 | 110 | 1.77% | 2.60% | -0.82 |
| Unknown | 40 | 10 | 0.61% | 0.24% | +0.38 |
| Other reasons | 23 | 27 | 0.35% | 0.64% | -0.29 |

**Root Cause:** None + Unknown + Insufficient

---

## L2: BE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 98.58% | 0.0% | +0.00% | 494 | 0 |  |
| None | 0.0% | 98.74% | -100.00% | 0 | 396 | ⚠️ |
| paypal | 85.39% | 88.89% | -3.93% | 89 | 117 |  |
| cashcredit | 100.0% | 100.0% | +0.00% | 1 | 5 |  |
| sepadirectdebit | 98.08% | 96.45% | +1.69% | 260 | 394 |  |
| bancontact | 93.97% | 88.76% | +5.86% | 199 | 267 | ⚠️ |
| applepay | 88.33% | 83.23% | +6.14% | 120 | 155 | ⚠️ |
| credit_card | 90.18% | 83.41% | +8.12% | 275 | 440 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 98.58% | 98.74% | -0.16% | 494 | 396 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 1 | 5 |  |
| Braintree | 87.08% | 85.66% | +1.66% | 209 | 272 |  |
| Adyen | 96.34% | 93.39% | +3.16% | 465 | 666 |  |
| ProcessOut | 89.96% | 83.22% | +8.10% | 269 | 435 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,360 | 1,613 | 94.58% | 90.92% | +3.65 |
| Insufficient Funds | 37 | 103 | 2.57% | 5.81% | -3.23 |
| Other reasons | 19 | 36 | 1.32% | 2.03% | -0.71 |
| Unknown | 4 | 1 | 0.28% | 0.06% | +0.22 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 18 | 21 | 1.25% | 1.18% | +0.07 |

**Root Cause:** None + ProcessOut + Insufficient

---

## L2: AT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| cashcredit | 100.0% | 100.0% | +0.00% | 3 | 1 |  |
| paypal | 97.4% | 96.55% | +0.87% | 192 | 116 |  |
| applepay | 93.58% | 90.0% | +3.98% | 218 | 110 |  |
| credit_card | 89.11% | 83.44% | +6.79% | 257 | 157 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 3 | 1 |  |
| Braintree | 95.37% | 93.36% | +2.15% | 410 | 226 |  |
| ProcessOut | 88.98% | 83.77% | +6.22% | 254 | 154 | ⚠️ |
| Adyen | 100.0% | 66.67% | +50.00% | 3 | 3 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Insufficient Funds | 35 | 35 | 5.22% | 9.11% | -3.89 |
| 1. SUCCESSFULL | 623 | 343 | 92.99% | 89.32% | +3.66 |
| Other reasons | 6 | 2 | 0.90% | 0.52% | +0.37 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 6 | 4 | 0.90% | 1.04% | -0.15 |

**Root Cause:** credit_card + ProcessOut + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 89.77% | 87.47% | +2.63% | 27,516 | 30,838 | ⚠️ |
| 2_PreDunningAR | 91.78% | 89.67% | +2.35% | 27,516 | 30,838 |  |
| 3_PostDunningAR | 92.16% | 90.26% | +2.11% | 27,516 | 30,838 |  |
| 6_PaymentApprovalRate | 92.47% | 90.61% | +2.05% | 27,516 | 30,838 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | Medium (>85%) | 7,581 | 5,658 | -25.4% | ⚠️ Volume drop |
| FR | High (>92%) | 7,452 | 5,183 | -30.4% | ⚠️ Major mix shift |
| DE | Medium (>85%) | 4,238 | 6,544 | +54.4% | Stable |
| AU | Low (>85%) | 3,049 | 2,628 | -13.8% | Stable |
| NL | High (>92%) | 1,866 | 1,104 | -40.8% | ⚠️ Major mix shift |
| BE | Medium (>85%) | 1,774 | 1,438 | -18.9% | Stable |
| IE | Medium (>85%) | 1,408 | 1,076 | -23.6% | ⚠️ Volume drop |
| SE | High (>92%) | 993 | 1,006 | +1.3% | Stable |
| DK | Medium (>85%) | 765 | 1,074 | +40.4% | Stable |
| NZ | Low (>85%) | 643 | 408 | -36.5% | ⚠️ Volume drop |
| NO | Medium (>85%) | 477 | 583 | +22.2% | Stable |
| AT | Medium (>85%) | 384 | 670 | +74.5% | Stable |
| CH | Medium (>85%) | 142 | 95 | -33.1% | ⚠️ Volume drop |
| LU | Low (>85%) | 66 | 49 | -25.8% | ⚠️ Volume drop |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| FR | ↑ +2.97% | applepay +5.1% | → Stable | Insufficient Funds -2.39pp | applepay + Insufficient |
| DE | ↑ +3.27% | None -100.0% | Unknown -86.4% | Insufficient Funds -2.25pp | None + Unknown + Insufficient |
| BE | ↑ +4.02% | None -100.0% | ProcessOut +8.1% | Insufficient Funds -3.23pp | None + ProcessOut + Insufficient |
| AT | ↑ +4.10% | credit_card +6.8% | ProcessOut +6.2% | Insufficient Funds -3.89pp | credit_card + ProcessOut + Insufficient |

---

*Report: 2026-04-17*
