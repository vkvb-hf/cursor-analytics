# AR Initial (LL0) Investigation: HF-INTL 2026-W15

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 89.67% → 91.78% (+2.35%)  
**Volume:** 27,516 orders  
**Significance:** Significant

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate for HF-INTL improved significantly from 89.67% to 91.78% (+2.35%) in W15, driven primarily by strong gains in DE (+6.05pp), AT (+10.34pp), and DK (+8.77pp), partially offset by declines in SE (-6.63pp) and GB (-3.13pp).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (88.09%-91.78%) | +2.35% | ✅ |
| L1: Country Breakdown | 6 countries exceed ±2.5% threshold | Mixed | ⚠️ |
| L1: PaymentMethod | Apple Pay +2.87%, Credit Card +3.38% | Improving | ✅ |
| L1: PaymentProvider | Braintree +2.62%, ProcessOut +3.37% | Improving | ✅ |
| L2: SE Deep-Dive | Braintree -13.25%, Insufficient Funds +5.73pp | Declining | ⚠️ |
| L2: GB Deep-Dive | Adyen -23.46%, volume drop -27% | Declining | ⚠️ |
| L2: DE Deep-Dive | ProcessOut +27.21%, Insufficient Funds -3.14pp | Improving | ✅ |
| L3: Related Metrics | All funnel stages improved +2.05% to +2.63% | Aligned | ✅ |

**Key Findings:**
- **Volume contraction masks improvement:** Total volume dropped 10.8% (30,838 → 27,516), with GB experiencing -27% and NL -35.8%, potentially inflating the rate improvement through mix shift
- **SE performance deterioration:** SE dropped -6.63pp driven by Braintree (-13.25%) and ProcessOut (-10.78%) failures, with "Insufficient Funds" declines surging +5.73pp
- **GB Adyen issue:** Adyen acceptance rate in GB collapsed from 67.23% to 51.46% (-23.46%), though low volume (206 orders) limits overall impact
- **DE recovery driving gains:** DE improved +6.05pp with ProcessOut jumping +27.21% and Credit Card acceptance rising +30.76%, while Insufficient Funds declined -3.14pp
- **Payment method data anomaly:** "None" payment method shows -100% change across multiple countries (SE, GB, DE, LU), suggesting a classification or tracking change

**Action:** **Investigate** - The overall improvement is significant but requires investigation into: (1) the "None" payment method classification change affecting all flagged countries, (2) SE's Braintree/ProcessOut degradation with rising Insufficient Funds, and (3) GB's Adyen performance collapse. Coordinate with Payment Operations to validate data integrity before attributing gains to operational improvements.

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
| SE | 81.92% | 87.74% | -6.63% | 1,549 | ⚠️ |
| GB | 77.56% | 80.07% | -3.13% | 10,285 | ⚠️ |
| FR | 86.18% | 84.43% | +2.07% | 9,933 |  |
| DE | 86.51% | 81.58% | +6.05% | 11,038 | ⚠️ |
| LU | 85.71% | 79.38% | +7.98% | 77 | ⚠️ |
| DK | 89.62% | 82.39% | +8.77% | 1,609 | ⚠️ |
| AT | 88.71% | 80.4% | +10.34% | 1,019 | ⚠️ |

**Countries exceeding ±2.5% threshold:** SE, GB, DE, LU, DK, AT

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

## L2: SE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 97.21% | 0.0% | +0.00% | 179 | 0 |  |
| None | 0.0% | 93.15% | -100.00% | 0 | 146 | ⚠️ |
| paypal | 46.43% | 61.9% | -25.00% | 28 | 21 | ⚠️ |
| credit_card | 69.0% | 78.83% | -12.46% | 471 | 392 | ⚠️ |
| applepay | 70.59% | 80.32% | -12.12% | 357 | 376 | ⚠️ |
| cashcredit | 100.0% | 100.0% | +0.00% | 5 | 5 |  |
| klarna | 98.23% | 97.41% | +0.84% | 509 | 618 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Braintree | 68.83% | 79.35% | -13.25% | 385 | 397 | ⚠️ |
| ProcessOut | 71.23% | 79.83% | -10.78% | 431 | 362 | ⚠️ |
| Adyen | 95.38% | 95.93% | -0.58% | 671 | 762 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 5 | 5 |  |
| Unknown | 91.23% | 84.38% | +8.12% | 57 | 32 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,269 | 1,367 | 81.92% | 87.74% | -5.82 |
| Insufficient Funds | 224 | 136 | 14.46% | 8.73% | +5.73 |
| PROVIDER_ERROR: failure executing charge with provider | 0 | 10 | 0.00% | 0.64% | -0.64 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 28 | 20 | 1.81% | 1.28% | +0.52 |
| Unknown | 6 | 0 | 0.39% | 0.00% | +0.39 |
| Other reasons | 22 | 25 | 1.42% | 1.60% | -0.18 |

**Root Cause:** None + Braintree + Insufficient

---

## L2: GB Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 96.62% | 0.0% | +0.00% | 1,007 | 0 |  |
| None | 0.0% | 97.68% | -100.00% | 0 | 1,338 | ⚠️ |
| credit_card | 73.67% | 76.71% | -3.96% | 3,749 | 5,195 |  |
| applepay | 74.05% | 76.89% | -3.69% | 4,725 | 6,418 |  |
| paypal | 91.91% | 92.31% | -0.44% | 754 | 1,093 |  |
| cashcredit | 100.0% | 100.0% | +0.00% | 50 | 42 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Adyen | 51.46% | 67.23% | -23.46% | 206 | 354 | ⚠️ |
| ProcessOut | 75.04% | 77.72% | -3.45% | 3,557 | 4,923 |  |
| Braintree | 76.52% | 79.14% | -3.31% | 5,477 | 7,511 |  |
| Unknown | 96.58% | 97.76% | -1.20% | 994 | 1,248 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 51 | 50 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 7,977 | 11,278 | 77.56% | 80.07% | -2.51 |
| Insufficient Funds | 1,779 | 2,228 | 17.30% | 15.82% | +1.48 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 292 | 328 | 2.84% | 2.33% | +0.51 |
| Other reasons | 202 | 224 | 1.96% | 1.59% | +0.37 |
| Unknown | 29 | 3 | 0.28% | 0.02% | +0.26 |
| PROVIDER_ERROR: failure executing charge with provider | 6 | 25 | 0.06% | 0.18% | -0.12 |

**Root Cause:** None + Adyen + Insufficient

---

## L2: DE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 7.02% | 0.0% | +0.00% | 57 | 0 |  |
| None | 0.0% | 47.83% | -100.00% | 0 | 46 | ⚠️ |
| klarna | 98.36% | 99.26% | -0.91% | 611 | 408 |  |
| cashcredit | 100.0% | 100.0% | +0.00% | 57 | 38 |  |
| paypal | 93.6% | 92.16% | +1.57% | 6,051 | 4,819 |  |
| applepay | 85.37% | 79.07% | +7.97% | 2,324 | 1,648 | ⚠️ |
| credit_card | 63.93% | 48.89% | +30.76% | 1,938 | 1,628 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 7.02% | 45.45% | -84.56% | 57 | 44 | ⚠️ |
| No Payment | 100.0% | 100.0% | +0.00% | 57 | 39 |  |
| Braintree | 91.32% | 88.82% | +2.81% | 8,375 | 6,467 |  |
| Adyen | 83.46% | 74.56% | +11.94% | 762 | 570 | ⚠️ |
| ProcessOut | 67.38% | 52.97% | +27.21% | 1,787 | 1,467 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 9,549 | 7,005 | 86.51% | 81.58% | +4.93 |
| Insufficient Funds | 737 | 843 | 6.68% | 9.82% | -3.14 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 458 | 447 | 4.15% | 5.21% | -1.06 |
| Other reasons | 241 | 269 | 2.18% | 3.13% | -0.95 |
| Unknown | 53 | 17 | 0.48% | 0.20% | +0.28 |
| PROVIDER_ERROR: failure executing charge with provider | 0 | 6 | 0.00% | 0.07% | -0.07 |

**Root Cause:** None + Unknown + Insufficient

---

## L2: LU Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 100.0% | 0.0% | +0.00% | 9 | 0 |  |
| None | 0.0% | 100.0% | -100.00% | 0 | 11 | ⚠️ |
| paypal | 100.0% | 100.0% | +0.00% | 12 | 10 |  |
| sepadirectdebit | 100.0% | 100.0% | +0.00% | 4 | 3 |  |
| credit_card | 85.71% | 82.14% | +4.35% | 28 | 28 |  |
| applepay | 70.83% | 66.67% | +6.25% | 24 | 45 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| ProcessOut | 0.0% | 0.0% | +0.00% | 1 | 0 |  |
| Unknown | 100.0% | 100.0% | +0.00% | 9 | 11 |  |
| Adyen | 90.32% | 83.87% | +7.69% | 31 | 31 | ⚠️ |
| Braintree | 80.56% | 72.73% | +10.76% | 36 | 55 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Insufficient Funds | 7 | 16 | 9.09% | 16.49% | -7.40 |
| 1. SUCCESSFULL | 66 | 77 | 85.71% | 79.38% | +6.33 |
| Other reasons | 2 | 0 | 2.60% | 0.00% | +2.60 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 2 | 4 | 2.60% | 4.12% | -1.53 |

**Root Cause:** None + Adyen + Insufficient

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
| GB | Low (>85%) | 14,086 | 10,285 | -27.0% | ⚠️ Volume drop |
| FR | Low (>85%) | 11,444 | 9,933 | -13.2% | Stable |
| DE | Low (>85%) | 8,587 | 11,038 | +28.5% | Stable |
| AU | Low (>85%) | 6,367 | 5,492 | -13.7% | Stable |
| NL | High (>92%) | 2,894 | 1,857 | -35.8% | ⚠️ Major mix shift |
| BE | Low (>85%) | 2,669 | 2,206 | -17.3% | Stable |
| IE | Low (>85%) | 2,062 | 1,730 | -16.1% | Stable |
| NZ | Low (>85%) | 1,607 | 1,186 | -26.2% | ⚠️ Volume drop |
| SE | Medium (>85%) | 1,558 | 1,549 | -0.6% | Stable |
| DK | Low (>85%) | 1,153 | 1,609 | +39.5% | Stable |
| NO | Low (>85%) | 773 | 939 | +21.5% | Stable |
| AT | Low (>85%) | 699 | 1,019 | +45.8% | Stable |
| CH | Medium (>85%) | 229 | 159 | -30.6% | ⚠️ Volume drop |
| LU | Low (>85%) | 97 | 77 | -20.6% | ⚠️ Volume drop |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| SE | ↓ -6.63% | None -100.0% | Braintree -13.2% | Insufficient Funds +5.73pp | None + Braintree + Insufficient |
| GB | ↓ -3.13% | None -100.0% | Adyen -23.5% | Insufficient Funds +1.48pp | None + Adyen + Insufficient |
| DE | ↑ +6.05% | None -100.0% | Unknown -84.6% | Insufficient Funds -3.14pp | None + Unknown + Insufficient |
| LU | ↑ +7.98% | None -100.0% | Adyen +7.7% | Insufficient Funds -7.40pp | None + Adyen + Insufficient |

---

*Report: 2026-04-15*
