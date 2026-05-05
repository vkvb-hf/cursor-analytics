# AR Initial (LL0) Investigation: HF-INTL 2026-W18

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 91.44% → 91.0% (-0.48%)  
**Volume:** 27,354 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) for HF-INTL declined from 91.44% to 91.0% (-0.44pp) in W18, a change that is **not statistically significant** with volume of 27,354 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Within normal range (89.62%-91.45%) | -0.44pp | ✅ |
| L1: Country Breakdown | 3 countries exceed ±2.5% threshold | FR -2.83%, LU +2.76%, NZ +4.95% | ⚠️ |
| L1: Dimension Scan | Credit Card method shows +4.39% change | Low volume (284) | ✅ |
| L2: FR Deep-Dive | Insufficient Funds increased +2.21pp | 4,701 volume | ⚠️ |
| L2: LU Deep-Dive | Adyen provider declined -7.14% | Very low volume (51) | ✅ |
| L2: NZ Deep-Dive | Rate actually improved +4.95% | 695 volume | ✅ |
| L3: Related Metrics | All metrics declined 0.38-0.75pp | Consistent pattern | ✅ |
| Mix Shift | AT, DE, NL, NO, LU show volume drops >27% | High-AR countries declining | ⚠️ |

**Key Findings:**
- **FR is the primary driver** of the overall decline, with rate dropping -2.83% and "Insufficient Funds" declines increasing from 2.59% to 4.81% (+2.21pp)
- **Volume mix shift observed:** High-AR countries (DE -28.9%, NL -28.9%, AT -30.5%) experienced significant volume drops, which may negatively impact overall rates
- **Apple Pay in FR** showed notable degradation (-4.69%), declining from 95.15% to 90.69%
- **NZ and LU improvements** partially offset FR decline, but LU volume is too small (51 orders) to be meaningful
- **All funnel metrics declined** consistently (FirstRunAR -0.75pp, PreDunningAR -0.44pp, PostDunningAR -0.43pp), suggesting a systemic issue rather than isolated to pre-dunning

**Action:** **Monitor** - The change is not statistically significant and falls within the 8-week normal range. However, recommend tracking FR's "Insufficient Funds" trend and the volume decline in high-AR countries (DE, NL, AT) over the next 1-2 weeks.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W18 | 91.0% | 27,354 | -0.48% ← REPORTED CHANGE |
| 2026-W17 | 91.44% | 31,531 | +0.20% |
| 2026-W16 | 91.26% | 33,178 | -0.21% |
| 2026-W15 | 91.45% | 25,833 | +2.04% |
| 2026-W14 | 89.62% | 29,972 | -0.42% |
| 2026-W13 | 90.0% | 33,903 | -1.10% |
| 2026-W12 | 91.0% | 38,348 | -0.39% |
| 2026-W11 | 91.36% | 41,931 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| FR | 93.21% | 95.93% | -2.83% | 4,701 | ⚠️ |
| GB | 91.64% | 90.99% | +0.71% | 7,771 |  |
| BE | 94.95% | 93.49% | +1.57% | 1,525 |  |
| CH | 86.57% | 84.56% | +2.38% | 134 |  |
| LU | 84.31% | 82.05% | +2.76% | 51 | ⚠️ |
| NZ | 76.83% | 73.21% | +4.95% | 695 | ⚠️ |

**Countries exceeding ±2.5% threshold:** FR, LU, NZ

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 90.52% | 91.38% | -0.94% | 15,217 |  |
| Apple Pay | 88.86% | 89.52% | -0.73% | 7,291 |  |
| Paypal | 96.43% | 94.99% | +1.52% | 4,562 |  |
| Credit Card | 84.51% | 80.95% | +4.39% | 284 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | nan% | +nan% | 0 |  |
| Unknown | 88.87% | 90.05% | -1.32% | 12,421 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 59 |  |
| Braintree | 91.77% | 91.76% | +0.02% | 11,853 |  |
| Adyen | 96.56% | 96.32% | +0.24% | 3,021 |  |

---

## L2: FR Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 93.58% | 0.00% | +0.00% | 2,757 | 0 |  |
| None | 0.00% | 95.89% | -100.00% | 0 | 3,112 | ⚠️ |
| applepay | 90.69% | 95.15% | -4.69% | 1,299 | 1,567 |  |
| credit_card | 93.10% | 94.74% | -1.72% | 29 | 19 |  |
| paypal | 96.91% | 97.84% | -0.95% | 615 | 696 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 1 | 5 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Braintree | 92.69% | 95.98% | -3.43% | 1,914 | 2,263 |  |
| Unknown | 93.73% | 96.00% | -2.37% | 2,742 | 3,099 |  |
| Adyen | 84.09% | 84.38% | -0.34% | 44 | 32 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 1 | 5 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 4,382 | 5,179 | 93.21% | 95.93% | -2.71 |
| Insufficient Funds | 226 | 140 | 4.81% | 2.59% | +2.21 |
| Other reasons | 69 | 56 | 1.47% | 1.04% | +0.43 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 24 | 23 | 0.51% | 0.43% | +0.08 |
| Unknown | 0 | 1 | 0.00% | 0.02% | -0.02 |

**Root Cause:** None + Insufficient

---

## L2: LU Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 100.00% | 0.00% | +0.00% | 5 | 0 |  |
| None | 0.00% | 100.00% | -100.00% | 0 | 5 | ⚠️ |
| paypal | 83.33% | 100.00% | -16.67% | 6 | 13 | ⚠️ |
| credit_card | 75.00% | 80.00% | -6.25% | 16 | 30 | ⚠️ |
| sepadirectdebit | 100.00% | 100.00% | +0.00% | 1 | 4 |  |
| applepay | 86.96% | 69.23% | +25.60% | 23 | 26 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Adyen | 76.47% | 82.35% | -7.14% | 17 | 34 | ⚠️ |
| Unknown | 100.00% | 100.00% | +0.00% | 5 | 5 |  |
| Braintree | 86.21% | 79.49% | +8.45% | 29 | 39 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Other reasons | 0 | 2 | 0.00% | 2.56% | -2.56 |
| 1. SUCCESSFULL | 43 | 64 | 84.31% | 82.05% | +2.26 |
| Insufficient Funds | 7 | 10 | 13.73% | 12.82% | +0.90 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 1 | 2 | 1.96% | 2.56% | -0.60 |

**Root Cause:** None + Adyen + Other

---

## L2: NZ Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 77.09% | 0.00% | +0.00% | 659 | 0 |  |
| None | 0.00% | 73.99% | -100.00% | 0 | 765 | ⚠️ |
| cashcredit | 100.00% | 100.00% | +0.00% | 1 | 1 |  |
| paypal | 63.16% | 53.85% | +17.29% | 19 | 26 | ⚠️ |
| credit_card | 81.25% | 66.67% | +21.88% | 16 | 18 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| No Payment | 100.00% | 100.00% | +0.00% | 1 | 1 |  |
| Unknown | 76.48% | 73.85% | +3.56% | 642 | 761 |  |
| Braintree | 63.16% | 53.85% | +17.29% | 19 | 26 | ⚠️ |
| Adyen | 90.91% | 72.73% | +25.00% | 33 | 22 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 534 | 593 | 76.83% | 73.21% | +3.62 |
| Insufficient Funds | 142 | 186 | 20.43% | 22.96% | -2.53 |
| Other reasons | 12 | 19 | 1.73% | 2.35% | -0.62 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 6 | 12 | 0.86% | 1.48% | -0.62 |
| Unknown | 1 | 0 | 0.14% | 0.00% | +0.14 |

**Root Cause:** None + Braintree + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.71% | 89.38% | -0.75% | 27,354 | 31,531 |  |
| 2_PreDunningAR | 91.0% | 91.44% | -0.48% | 27,354 | 31,531 |  |
| 3_PostDunningAR | 91.6% | 91.99% | -0.43% | 27,354 | 31,531 |  |
| 6_PaymentApprovalRate | 91.94% | 92.28% | -0.38% | 27,354 | 31,531 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | Medium (>85%) | 8,315 | 7,771 | -6.5% | Stable |
| DE | High (>92%) | 5,848 | 4,160 | -28.9% | ⚠️ Volume drop |
| FR | High (>92%) | 5,399 | 4,701 | -12.9% | Stable |
| AU | Low (>85%) | 2,683 | 2,872 | +7.0% | Stable |
| BE | High (>92%) | 1,689 | 1,525 | -9.7% | Stable |
| IE | Medium (>85%) | 1,435 | 1,429 | -0.4% | Stable |
| SE | High (>92%) | 1,320 | 1,086 | -17.7% | Stable |
| DK | High (>92%) | 1,108 | 998 | -9.9% | Stable |
| NL | High (>92%) | 1,102 | 784 | -28.9% | ⚠️ Volume drop |
| NO | Medium (>85%) | 1,090 | 788 | -27.7% | ⚠️ Volume drop |
| NZ | Low (>85%) | 810 | 695 | -14.2% | Stable |
| AT | High (>92%) | 518 | 360 | -30.5% | ⚠️ Major mix shift |
| CH | Low (>85%) | 136 | 134 | -1.5% | Stable |
| LU | Low (>85%) | 78 | 51 | -34.6% | ⚠️ Volume drop |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| FR | ↓ -2.83% | None -100.0% | → Stable | Insufficient Funds +2.21pp | None + Insufficient |
| LU | ↑ +2.76% | None -100.0% | Adyen -7.1% | Other reasons -2.56pp | None + Adyen + Other |
| NZ | ↑ +4.95% | None -100.0% | Braintree +17.3% | Insufficient Funds -2.53pp | None + Braintree + Insufficient |

---

*Report: 2026-05-05*
