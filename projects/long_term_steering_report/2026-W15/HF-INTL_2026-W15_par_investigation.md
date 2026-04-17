# PAR Investigation: HF-INTL 2026-W15

**Metric:** Payment Approval Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 97.04% → 97.27% (+0.24%)  
**Volume:** 744,637 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate for HF-INTL improved slightly from 97.04% to 97.27% (+0.24pp) in W15, a change that is not statistically significant, with volume declining from 784,406 to 744,637 orders (-5.1%).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | +1.76% | ✅ |
| 2_PreDunningAR | vs Prior | +1.18% | ✅ |
| 3_PostDunningAR | vs Prior | +0.01% | ✅ |
| 6_PaymentApprovalRate | vs Prior | +0.24% | ✅ |

**Key Findings:**
- Two countries exceeded the ±2.5% threshold: AT (+2.95pp) and DK (+3.94pp), both showing improvement driven by reduced "Insufficient Funds" declines
- In AT, Apple Pay approval rate improved significantly (+5.78pp), with Insufficient Funds declines dropping from 4.63% to 2.58% (-2.05pp)
- In DK, Braintree provider showed notable improvement (+5.84pp), with Insufficient Funds declines dropping from 4.28% to 1.16% (-3.13pp)
- All payment methods and providers at the aggregate level remained stable with no concerning movements
- First Run AR showed the strongest funnel improvement at +1.76%, indicating better initial payment success

**Action:** Monitor - The overall change is not significant and represents positive movement. Continue tracking AT and DK to confirm the "Insufficient Funds" decline reduction is sustained.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 97.27% | 744,637 | +0.24% ← REPORTED CHANGE |
| 2026-W14 | 97.04% | 784,406 | -0.13% |
| 2026-W13 | 97.17% | 842,482 | -0.08% |
| 2026-W12 | 97.25% | 877,189 | +0.04% |
| 2026-W11 | 97.21% | 897,107 | +0.52% |
| 2026-W10 | 96.71% | 916,831 | +0.51% |
| 2026-W09 | 96.22% | 896,537 | -0.12% |
| 2026-W08 | 96.34% | 884,970 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| DE | 97.33% | 96.44% | +0.93% | 201,519 |  |
| GB | 94.14% | 93.07% | +1.15% | 185,598 |  |
| FR | 94.49% | 92.95% | +1.66% | 147,984 |  |
| IE | 91.92% | 90.41% | +1.67% | 17,513 |  |
| AT | 95.52% | 92.78% | +2.95% | 13,962 | ⚠️ |
| DK | 97.74% | 94.03% | +3.94% | 37,713 | ⚠️ |

**Countries exceeding ±2.5% threshold:** AT, DK

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 99.49% | 99.49% | +0.00% | 121,159 |  |
| Paypal | 98.97% | 98.92% | +0.05% | 185,690 |  |
| Credit Card | 96.64% | 96.38% | +0.27% | 338,141 |  |
| Apple Pay | 93.55% | 92.77% | +0.84% | 99,647 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 87.0% | 87.62% | -0.70% | 2,300 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 4,522 |  |
| Adyen | 98.42% | 98.35% | +0.07% | 241,312 |  |
| Braintree | 97.4% | 97.09% | +0.31% | 280,104 |  |
| ProcessOut | 95.87% | 95.5% | +0.39% | 216,399 |  |

---

## L2: AT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| cashcredit | 100.0% | 100.0% | +0.00% | 90 | 65 |  |
| klarna | 100.0% | 100.0% | +0.00% | 2 | 2 |  |
| sepadirectdebit | 99.32% | 98.84% | +0.49% | 884 | 775 |  |
| paypal | 97.96% | 96.99% | +0.99% | 4,941 | 4,354 |  |
| credit_card | 93.54% | 89.87% | +4.08% | 6,071 | 5,530 |  |
| applepay | 93.57% | 88.45% | +5.78% | 1,974 | 1,732 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 90 | 65 |  |
| Adyen | 95.22% | 93.61% | +1.72% | 2,470 | 2,191 |  |
| Braintree | 96.7% | 94.56% | +2.26% | 6,915 | 6,086 |  |
| ProcessOut | 93.76% | 89.58% | +4.67% | 4,487 | 4,116 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 13,336 | 11,558 | 95.52% | 92.78% | +2.74 |
| Insufficient Funds | 360 | 577 | 2.58% | 4.63% | -2.05 |
| Other reasons | 114 | 149 | 0.82% | 1.20% | -0.38 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 152 | 174 | 1.09% | 1.40% | -0.31 |

**Root Cause:** applepay + Insufficient

---

## L2: DK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 65.79% | 0.0% | +0.00% | 38 | 0 |  |
| None | 0.0% | 70.59% | -100.00% | 0 | 34 | ⚠️ |
| cashcredit | 100.0% | 100.0% | +0.00% | 238 | 173 |  |
| paypal | 96.47% | 94.78% | +1.78% | 1,104 | 901 |  |
| credit_card | 98.17% | 94.92% | +3.42% | 28,919 | 22,890 |  |
| applepay | 96.33% | 90.48% | +6.47% | 7,414 | 6,038 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 238 | 173 |  |
| Unknown | 62.5% | 62.5% | +0.00% | 32 | 24 |  |
| ProcessOut | 98.17% | 95.19% | +3.13% | 21,035 | 16,787 |  |
| Adyen | 98.15% | 94.18% | +4.22% | 7,890 | 6,113 |  |
| Braintree | 96.35% | 91.04% | +5.84% | 8,518 | 6,939 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 36,859 | 28,242 | 97.74% | 94.03% | +3.71 |
| Insufficient Funds | 436 | 1,286 | 1.16% | 4.28% | -3.13 |
| Other reasons | 230 | 309 | 0.61% | 1.03% | -0.42 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 176 | 189 | 0.47% | 0.63% | -0.16 |
| Unknown | 12 | 10 | 0.03% | 0.03% | +0.00 |

**Root Cause:** None + Braintree + Insufficient

---

## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 93.12% | 91.51% | +1.76% | 744,637 | 784,406 |  |
| 2_PreDunningAR | 94.74% | 93.63% | +1.18% | 744,637 | 784,406 |  |
| 3_PostDunningAR | 96.42% | 96.41% | +0.01% | 744,637 | 784,406 |  |
| 6_PaymentApprovalRate | 97.27% | 97.04% | +0.24% | 744,637 | 784,406 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | High (>92%) | 205,600 | 185,598 | -9.7% | Stable |
| DE | High (>92%) | 205,169 | 201,519 | -1.8% | Stable |
| FR | High (>92%) | 158,173 | 147,984 | -6.4% | Stable |
| NL | High (>92%) | 118,190 | 110,805 | -6.2% | Stable |
| AU | Medium (>85%) | 96,471 | 85,229 | -11.7% | Stable |
| BE | High (>92%) | 74,093 | 64,439 | -13.0% | Stable |
| SE | High (>92%) | 35,624 | 31,821 | -10.7% | Stable |
| DK | High (>92%) | 30,036 | 37,713 | +25.6% | Stable |
| NZ | Medium (>85%) | 19,364 | 16,941 | -12.5% | Stable |
| IE | Medium (>85%) | 18,775 | 17,513 | -6.7% | Stable |
| NO | Medium (>85%) | 13,551 | 18,868 | +39.2% | Stable |
| AT | High (>92%) | 12,458 | 13,962 | +12.1% | Stable |
| LU | High (>92%) | 2,765 | 2,731 | -1.2% | Stable |
| CH | High (>92%) | 2,174 | 2,101 | -3.4% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| AT | ↑ +2.95% | applepay +5.8% | → Stable | Insufficient Funds -2.05pp | applepay + Insufficient |
| DK | ↑ +3.94% | None -100.0% | Braintree +5.8% | Insufficient Funds -3.13pp | None + Braintree + Insufficient |

---

*Report: 2026-04-17*
