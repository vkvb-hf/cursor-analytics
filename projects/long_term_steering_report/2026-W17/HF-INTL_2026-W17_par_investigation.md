# PAR Investigation: HF-INTL 2026-W17

**Metric:** Payment Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 97.39% → 97.43% (+0.04%)  
**Volume:** 794,598 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate for HF-INTL showed a marginal improvement from 97.39% to 97.43% (+0.04pp) in W17, a statistically non-significant change within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Stable | +0.00pp | ✅ |
| 2_PreDunningAR | Slight decline | -0.19pp | ✅ |
| 3_PostDunningAR | Slight decline | -0.30pp | ⚠️ |
| 6_PaymentApprovalRate | Slight improvement | +0.04pp | ✅ |

**Key Findings:**
- The 8-week trend shows consistent improvement from 96.71% (W10) to 97.43% (W17), representing a +0.72pp gain over the period
- CH experienced the largest country-level decline (-1.24pp), but with minimal volume impact (2,253 orders)
- No countries exceeded the ±2.5% threshold requiring deep-dive investigation
- Payment providers remain stable with Adyen (98.55%) and Braintree (97.44%) performing consistently
- ProcessOut shows no volume in current week (0 orders), indicating potential provider transition or discontinuation

**Action:** Monitor — The change is not statistically significant and no dimensions exceeded investigation thresholds. Continue standard monitoring cadence.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 97.43% | 794,598 | +0.04% ← REPORTED CHANGE |
| 2026-W16 | 97.39% | 804,152 | +0.13% |
| 2026-W15 | 97.26% | 744,637 | +0.24% |
| 2026-W14 | 97.03% | 784,406 | -0.13% |
| 2026-W13 | 97.16% | 842,482 | -0.09% |
| 2026-W12 | 97.25% | 877,189 | +0.04% |
| 2026-W11 | 97.21% | 897,107 | +0.52% |
| 2026-W10 | 96.71% | 916,831 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CH | 96.09% | 97.30% | -1.24% | 2,253 |  |
| IE | 95.50% | 95.99% | -0.51% | 19,064 |  |
| FR | 96.73% | 97.05% | -0.33% | 133,904 |  |
| DK | 98.56% | 98.87% | -0.32% | 39,276 |  |
| GB | 96.71% | 96.42% | +0.30% | 208,580 |  |
| NZ | 94.28% | 93.75% | +0.57% | 19,229 |  |
| AU | 96.30% | 95.70% | +0.62% | 93,894 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 97.35% | 97.77% | -0.43% | 350,591 |  |
| Paypal | 99.02% | 99.03% | -0.01% | 201,607 |  |
| Apple Pay | 94.3% | 93.99% | +0.33% | 101,975 |  |
| Credit Card | 97.59% | 97.17% | +0.44% | 140,425 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 96.46% | +nan% | 0 |  |
| Braintree | 97.44% | 97.45% | -0.01% | 303,499 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 5,290 |  |
| Adyen | 98.55% | 98.53% | +0.02% | 256,441 |  |
| Unknown | 96.09% | 95.49% | +0.63% | 229,368 |  |

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
| AU | High (>92%) | 89,760 | 93,894 | +4.6% | Stable |
| BE | High (>92%) | 64,642 | 73,015 | +13.0% | Stable |
| DK | High (>92%) | 40,108 | 39,276 | -2.1% | Stable |
| SE | High (>92%) | 38,861 | 38,925 | +0.2% | Stable |
| NO | High (>92%) | 24,045 | 25,000 | +4.0% | Stable |
| IE | High (>92%) | 18,708 | 19,064 | +1.9% | Stable |
| NZ | High (>92%) | 18,117 | 19,229 | +6.1% | Stable |
| AT | High (>92%) | 14,079 | 13,663 | -3.0% | Stable |
| LU | High (>92%) | 3,510 | 3,738 | +6.5% | Stable |
| CH | High (>92%) | 2,299 | 2,253 | -2.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-28*
