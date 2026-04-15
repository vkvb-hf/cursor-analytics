# AR Overall Investigation: HF-INTL 2026-W15

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 93.63% → 94.74% (+1.19%)  
**Volume:** 744,637 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** The Pre-Dunning Acceptance Rate for HF-INTL improved significantly from 93.63% to 94.74% (+1.19%) in 2026-W15, representing a positive recovery after three consecutive weeks of decline.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate returned to near 8-week high | +1.19% | ✅ |
| L1: Country Breakdown | 2 countries exceed ±2.5% threshold (AT, DK) | AT +2.95%, DK +3.94% | ⚠️ |
| L1: PaymentMethod | Apple Pay shows elevated change | +2.73% | ⚠️ |
| L1: PaymentProvider | All providers within threshold | Max +1.55% | ✅ |
| L2: AT Deep-Dive | applepay driving improvement | +5.78% | ⚠️ |
| L2: DK Deep-Dive | applepay + Braintree driving improvement | +6.47%, +5.84% | ⚠️ |
| L3: Related Metrics | All funnel metrics improved or stable | 1_FirstRunAR +1.76% | ✅ |
| Mix Shift | No significant mix impact | All Stable | ✅ |

**Key Findings:**
- Insufficient Funds declines dropped significantly in both flagged countries: AT (-2.05pp) and DK (-3.13pp), driving the overall improvement
- Apple Pay acceptance rate improved across markets, with AT (+5.78%) and DK (+6.47%) showing the largest gains
- DK volume increased +25.6% WoW while maintaining strong AR improvement, indicating healthy growth
- First Run AR improved by +1.76pp (91.51% → 93.12%), suggesting upstream payment processing improvements
- The improvement reverses a 3-week declining trend (W12-W14), returning the rate close to the W11 peak of 94.9%

**Action:** Monitor - This is a positive improvement driven by reduced Insufficient Funds declines, particularly in Apple Pay transactions. Continue monitoring to confirm the trend sustains through W16.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 94.74% | 744,637 | +1.19% ← REPORTED CHANGE |
| 2026-W14 | 93.63% | 784,406 | -0.55% |
| 2026-W13 | 94.15% | 842,482 | -0.48% |
| 2026-W12 | 94.6% | 877,189 | -0.32% |
| 2026-W11 | 94.9% | 897,107 | +1.17% |
| 2026-W10 | 93.8% | 916,831 | +0.72% |
| 2026-W09 | 93.13% | 896,537 | -0.45% |
| 2026-W08 | 93.55% | 884,970 | - |

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
| Others | 98.96% | 98.81% | +0.16% | 121,159 |  |
| Paypal | 97.74% | 97.23% | +0.53% | 185,690 |  |
| Credit Card | 93.0% | 91.59% | +1.53% | 338,141 |  |
| Apple Pay | 89.91% | 87.51% | +2.73% | 99,647 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 4,522 |  |
| Adyen | 95.95% | 95.19% | +0.80% | 241,312 |  |
| Braintree | 95.38% | 94.19% | +1.27% | 280,104 |  |
| Unknown | 85.22% | 83.93% | +1.53% | 2,300 |  |
| ProcessOut | 92.54% | 91.13% | +1.55% | 216,399 |  |

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

*Report: 2026-04-15*
