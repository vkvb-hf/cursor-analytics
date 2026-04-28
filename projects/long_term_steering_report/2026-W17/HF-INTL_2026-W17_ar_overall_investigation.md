# AR Overall Investigation: HF-INTL 2026-W17

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 94.81% → 94.63% (-0.19%)  
**Volume:** 794,598 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate for HF-INTL declined marginally from 94.81% to 94.63% (-0.19pp) in 2026-W17, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (93.63%-94.90%) | -0.19pp | ✅ |
| L1: Country Breakdown | NO exceeded ±2.5% threshold (+4.53%) | +4.53pp | ⚠️ |
| L1: Dimension Scan | No payment methods/providers exceed threshold | -1.22pp max | ✅ |
| L2: NO Deep-Dive | ProcessOut volume dropped to 0; Unknown provider surged | -100% / +26.51pp | ⚠️ |
| L3: Related Metrics | All metrics stable, PostDunningAR -0.30pp | -0.30pp | ✅ |
| Mix Shift | All countries stable, no significant volume shifts | - | ✅ |

**Key Findings:**
- NO showed a significant **improvement** of +4.53pp (89.15% → 93.19%), driven by a reduction in "Insufficient Funds" declines (-3.78pp)
- ProcessOut payment provider volume in NO dropped from 13,027 to 0 orders, with traffic shifting to Unknown provider (96 → 13,382 orders)
- The "None" payment method appeared in NO with 13,420 orders at 94.78% acceptance, suggesting a data classification or routing change
- LU (-2.11pp) and CH (-1.77pp) showed declines but remain below the ±2.5% alert threshold
- Overall volume decreased slightly from 804,152 to 794,598 orders (-1.2%)

**Action:** **Monitor** - The overall decline is not significant and the flagged country (NO) actually improved. Recommend tracking the ProcessOut → Unknown provider migration in NO to ensure this routing change continues to perform well.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 94.63% | 794,598 | -0.19% ← REPORTED CHANGE |
| 2026-W16 | 94.81% | 804,152 | +0.07% |
| 2026-W15 | 94.74% | 744,637 | +1.19% |
| 2026-W14 | 93.63% | 784,406 | -0.55% |
| 2026-W13 | 94.15% | 842,482 | -0.47% |
| 2026-W12 | 94.59% | 877,189 | -0.33% |
| 2026-W11 | 94.9% | 897,107 | +1.17% |
| 2026-W10 | 93.8% | 916,831 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| LU | 93.87% | 95.90% | -2.11% | 3,738 |  |
| CH | 91.39% | 93.04% | -1.77% | 2,253 |  |
| FR | 93.71% | 94.48% | -0.81% | 133,904 |  |
| DE | 97.37% | 97.53% | -0.16% | 222,785 |  |
| AU | 92.12% | 91.18% | +1.03% | 93,894 |  |
| NO | 93.19% | 89.15% | +4.53% | 25,000 | ⚠️ |

**Countries exceeding ±2.5% threshold:** NO

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 95.28% | 96.45% | -1.22% | 350,591 |  |
| Credit Card | 91.96% | 92.87% | -0.98% | 140,425 |  |
| Apple Pay | 89.95% | 90.1% | -0.16% | 101,975 |  |
| Paypal | 97.72% | 97.84% | -0.13% | 201,607 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 92.58% | +nan% | 0 |  |
| Adyen | 95.16% | 95.77% | -0.64% | 256,441 |  |
| Braintree | 95.11% | 95.37% | -0.27% | 303,499 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 5,290 |  |
| Unknown | 93.27% | 93.25% | +0.02% | 229,368 |  |

---

## L2: NO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 94.78% | 0.00% | +0.00% | 13,420 | 0 |  |
| None | 0.00% | 75.51% | -100.00% | 0 | 98 | ⚠️ |
| cashcredit | 100.00% | 100.00% | +0.00% | 151 | 169 |  |
| credit_card | 92.22% | 89.85% | +2.65% | 6,302 | 18,841 |  |
| paypal | 92.50% | 89.76% | +3.05% | 1,360 | 1,377 |  |
| applepay | 89.14% | 85.11% | +4.74% | 3,767 | 3,560 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| ProcessOut | 0.00% | 90.11% | -100.00% | 0 | 13,027 | ⚠️ |
| No Payment | 100.00% | 100.00% | +0.00% | 151 | 169 |  |
| Adyen | 92.02% | 89.25% | +3.10% | 6,340 | 5,816 |  |
| Braintree | 90.03% | 86.41% | +4.19% | 5,127 | 4,937 |  |
| Unknown | 94.88% | 75.00% | +26.51% | 13,382 | 96 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 23,298 | 21,437 | 93.19% | 89.15% | +4.04 |
| Insufficient Funds | 1,383 | 2,239 | 5.53% | 9.31% | -3.78 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 168 | 208 | 0.67% | 0.87% | -0.19 |
| Unknown | 11 | 22 | 0.04% | 0.09% | -0.05 |
| Other reasons | 140 | 139 | 0.56% | 0.58% | -0.02 |

**Root Cause:** None + ProcessOut + Insufficient

---

## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 92.7% | 92.7% | +0.00% | 794,598 | 804,152 |  |
| 2_PreDunningAR | 94.63% | 94.81% | -0.19% | 794,598 | 804,152 |  |
| 3_PostDunningAR | 96.46% | 96.74% | -0.30% | 794,598 | 804,152 |  |
| 6_PaymentApprovalRate | 97.43% | 97.39% | +0.03% | 794,598 | 804,152 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| DE | High (>92%) | 224,251 | 222,785 | -0.7% | Stable |
| GB | High (>92%) | 209,202 | 208,580 | -0.3% | Stable |
| FR | High (>92%) | 145,977 | 133,904 | -8.3% | Stable |
| NL | High (>92%) | 109,008 | 103,060 | -5.5% | Stable |
| AU | Medium (>85%) | 89,760 | 93,894 | +4.6% | Stable |
| BE | High (>92%) | 64,642 | 73,015 | +13.0% | Stable |
| DK | High (>92%) | 40,108 | 39,276 | -2.1% | Stable |
| SE | High (>92%) | 38,861 | 38,925 | +0.2% | Stable |
| NO | Medium (>85%) | 24,045 | 25,000 | +4.0% | Stable |
| IE | High (>92%) | 18,708 | 19,064 | +1.9% | Stable |
| NZ | Medium (>85%) | 18,117 | 19,229 | +6.1% | Stable |
| AT | High (>92%) | 14,079 | 13,663 | -3.0% | Stable |
| LU | High (>92%) | 3,510 | 3,738 | +6.5% | Stable |
| CH | High (>92%) | 2,299 | 2,253 | -2.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| NO | ↑ +4.53% | None -100.0% | ProcessOut -100.0% | Insufficient Funds -3.78pp | None + ProcessOut + Insufficient |

---

*Report: 2026-04-28*
