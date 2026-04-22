# AR Overall Investigation: HF-INTL 2026-W15

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 94.74% → 94.81% (+0.07%)  
**Volume:** 804,152 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate for HF-INTL improved marginally from 94.74% to 94.81% (+0.07pp) in 2026-W15, a statistically non-significant change across 804,152 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Within normal variance | +0.07pp | ✅ |
| L1: Country Breakdown | 2 countries exceed ±2.5% threshold (AT, DK) | AT +2.97%, DK +3.94% | ⚠️ |
| L1: PaymentMethod | 1 method exceeds threshold (Apple Pay) | +2.73pp | ⚠️ |
| L1: PaymentProvider | All providers within threshold | Max +1.54pp | ✅ |
| L2: AT Deep-Dive | applepay improvement driven by Insufficient Funds decline | -2.05pp decline reasons | ⚠️ |
| L2: DK Deep-Dive | Insufficient Funds decline driving improvement | -3.13pp decline reasons | ⚠️ |
| L3: Related Metrics | All funnel metrics improved | 1_FirstRunAR +1.77pp | ✅ |

**Key Findings:**
- AT and DK both showed significant improvements (+2.97% and +3.94% respectively), driven primarily by reduced "Insufficient Funds" declines (-2.05pp in AT, -3.13pp in DK)
- Apple Pay performance improved substantially across flagged countries: +5.78% in AT and +6.46% in DK
- DK volume increased +25.6% WoW while maintaining improved acceptance rates, indicating healthy growth
- First Run AR showed the strongest funnel improvement at +1.77pp, suggesting upstream payment processing improvements are benefiting the entire funnel
- Mix shift analysis shows stable impact across all countries despite volume fluctuations

**Action:** Monitor - The overall change is not statistically significant and represents positive improvement. Continue monitoring AT and DK Apple Pay performance and Insufficient Funds trends to confirm sustained improvement.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 94.81% | 804,152 | +0.07% |
| 2026-W15 | 94.74% | 744,637 | +1.19% ← REPORTED CHANGE |
| 2026-W14 | 93.63% | 784,406 | -0.55% |
| 2026-W13 | 94.15% | 842,482 | -0.47% |
| 2026-W12 | 94.59% | 877,189 | -0.33% |
| 2026-W11 | 94.9% | 897,107 | +1.17% |
| 2026-W10 | 93.8% | 916,831 | +0.72% |
| 2026-W09 | 93.13% | 896,537 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| DE | 97.34% | 96.43% | +0.94% | 201,519 |  |
| GB | 94.14% | 93.07% | +1.15% | 185,598 |  |
| FR | 94.49% | 92.95% | +1.66% | 147,984 |  |
| IE | 91.92% | 90.41% | +1.67% | 17,513 |  |
| AT | 95.52% | 92.77% | +2.97% | 13,962 | ⚠️ |
| DK | 97.73% | 94.03% | +3.94% | 37,713 | ⚠️ |

**Countries exceeding ±2.5% threshold:** AT, DK

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 99.01% | 98.8% | +0.22% | 121,157 |  |
| Paypal | 97.74% | 97.22% | +0.53% | 185,690 |  |
| Credit Card | 93.0% | 91.59% | +1.53% | 338,143 |  |
| Apple Pay | 89.9% | 87.51% | +2.73% | 99,647 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 4,522 |  |
| Adyen | 95.98% | 95.18% | +0.84% | 241,311 |  |
| Braintree | 95.38% | 94.18% | +1.27% | 280,104 |  |
| Unknown | 85.3% | 84.11% | +1.41% | 2,299 |  |
| ProcessOut | 92.53% | 91.13% | +1.54% | 216,401 |  |

---

## L2: AT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| cashcredit | 100.00% | 100.00% | +0.00% | 90 | 65 |  |
| klarna | 100.00% | 100.00% | +0.00% | 2 | 2 |  |
| sepadirectdebit | 99.43% | 98.71% | +0.73% | 884 | 775 |  |
| paypal | 97.96% | 96.99% | +0.99% | 4,941 | 4,354 |  |
| credit_card | 93.54% | 89.87% | +4.08% | 6,071 | 5,530 |  |
| applepay | 93.57% | 88.45% | +5.78% | 1,974 | 1,732 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| No Payment | 100.00% | 100.00% | +0.00% | 90 | 65 |  |
| Adyen | 95.26% | 93.56% | +1.82% | 2,470 | 2,191 |  |
| Braintree | 96.70% | 94.56% | +2.26% | 6,915 | 6,086 |  |
| ProcessOut | 93.76% | 89.58% | +4.67% | 4,487 | 4,116 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 13,337 | 11,557 | 95.52% | 92.77% | +2.76 |
| Insufficient Funds | 360 | 577 | 2.58% | 4.63% | -2.05 |
| Other reasons | 113 | 150 | 0.81% | 1.20% | -0.39 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 152 | 174 | 1.09% | 1.40% | -0.31 |

**Root Cause:** applepay + Insufficient

---

## L2: DK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 65.79% | 0.00% | +0.00% | 38 | 0 |  |
| None | 0.00% | 70.59% | -100.00% | 0 | 34 | ⚠️ |
| cashcredit | 100.00% | 100.00% | +0.00% | 238 | 173 |  |
| paypal | 96.47% | 94.78% | +1.78% | 1,104 | 901 |  |
| credit_card | 98.17% | 94.92% | +3.42% | 28,919 | 22,890 |  |
| applepay | 96.32% | 90.48% | +6.46% | 7,414 | 6,038 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 62.50% | 66.67% | -6.25% | 32 | 24 | ⚠️ |
| No Payment | 100.00% | 100.00% | +0.00% | 238 | 173 |  |
| ProcessOut | 98.17% | 95.19% | +3.13% | 21,035 | 16,787 |  |
| Adyen | 98.15% | 94.16% | +4.24% | 7,890 | 6,113 |  |
| Braintree | 96.34% | 91.04% | +5.82% | 8,518 | 6,939 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 36,858 | 28,242 | 97.73% | 94.03% | +3.71 |
| Insufficient Funds | 436 | 1,286 | 1.16% | 4.28% | -3.13 |
| Other reasons | 230 | 309 | 0.61% | 1.03% | -0.42 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 177 | 189 | 0.47% | 0.63% | -0.16 |
| Unknown | 12 | 10 | 0.03% | 0.03% | +0.00 |

**Root Cause:** None + Unknown + Insufficient

---

## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 93.12% | 91.5% | +1.77% | 744,637 | 784,406 |  |
| 2_PreDunningAR | 94.74% | 93.63% | +1.19% | 744,637 | 784,406 |  |
| 3_PostDunningAR | 96.63% | 96.51% | +0.12% | 744,637 | 784,406 |  |
| 6_PaymentApprovalRate | 97.27% | 97.03% | +0.24% | 744,637 | 784,406 |  |

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
| AT | ↑ +2.97% | applepay +5.8% | → Stable | Insufficient Funds -2.05pp | applepay + Insufficient |
| DK | ↑ +3.94% | None -100.0% | Unknown -6.2% | Insufficient Funds -3.13pp | None + Unknown + Insufficient |

---

*Report: 2026-04-22*
