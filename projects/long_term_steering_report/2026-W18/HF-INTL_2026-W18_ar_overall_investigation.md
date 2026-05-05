# AR Overall Investigation: HF-INTL 2026-W18

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 94.62% → 93.93% (-0.73%)  
**Volume:** 780,744 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate declined from 94.62% to 93.93% (-0.73%, -0.69pp) on 780,744 orders in 2026-W18; the change is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | First attempt acceptance | -1.08% | ⚠️ |
| 2_PreDunningAR | Pre-dunning recovery | -0.73% | ⚠️ |
| 3_PostDunningAR | Post-dunning recovery | -0.38% | ⚠️ |
| 6_PaymentApprovalRate | Final payment approval | -0.13% | ✅ |

**Key Findings:**
- The decline originates upstream at FirstRunAR (-1.08%), with diminishing impact through the funnel as recovery mechanisms engage
- No individual country exceeded the ±2.5% threshold; LU showed the largest decline at -1.97% (3,435 orders), followed by BE at -1.52% (67,404 orders)
- Apple Pay exhibited the steepest payment method decline at -1.29% (101,492 orders), followed by Credit Card at -0.83%
- Mix shift analysis shows stable volume distribution across all countries, with NL experiencing the largest volume drop (-11.2%) but maintaining High AR tier status
- All payment providers showed modest declines (Adyen -0.68%, Braintree -0.63%, Unknown -0.92%), suggesting a broad-based rather than provider-specific issue

**Action:** Monitor — The decline is not statistically significant, no thresholds were breached, and the pattern reflects a broad-based minor softening across geographies and payment methods rather than a localized failure.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W18 | 93.93% | 780,744 | -0.73% ← REPORTED CHANGE |
| 2026-W17 | 94.62% | 794,598 | -0.19% |
| 2026-W16 | 94.8% | 804,152 | +0.07% |
| 2026-W15 | 94.73% | 744,637 | +1.19% |
| 2026-W14 | 93.62% | 784,406 | -0.56% |
| 2026-W13 | 94.15% | 842,482 | -0.47% |
| 2026-W12 | 94.59% | 877,189 | -0.32% |
| 2026-W11 | 94.89% | 897,107 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| LU | 92.02% | 93.87% | -1.97% | 3,435 |  |
| BE | 94.33% | 95.78% | -1.52% | 67,404 |  |
| AT | 93.54% | 94.85% | -1.38% | 13,866 |  |
| IE | 90.01% | 91.21% | -1.31% | 19,292 |  |
| FR | 92.80% | 93.71% | -0.97% | 134,603 |  |
| DE | 96.93% | 97.36% | -0.44% | 225,472 |  |
| GB | 93.63% | 93.91% | -0.30% | 210,813 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 88.78% | 89.94% | -1.29% | 101,492 |  |
| Credit Card | 91.02% | 91.78% | -0.83% | 140,582 |  |
| Others | 94.64% | 95.36% | -0.75% | 338,948 |  |
| Paypal | 97.4% | 97.7% | -0.31% | 199,722 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | nan% | +nan% | 0 |  |
| Unknown | 92.55% | 93.41% | -0.92% | 225,847 |  |
| Adyen | 94.39% | 95.03% | -0.68% | 248,862 |  |
| Braintree | 94.5% | 95.1% | -0.63% | 301,191 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 4,844 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.7% | 92.7% | -1.08% | 780,744 | 794,598 |  |
| 2_PreDunningAR | 93.93% | 94.62% | -0.73% | 780,744 | 794,598 |  |
| 3_PostDunningAR | 96.48% | 96.85% | -0.38% | 780,744 | 794,598 |  |
| 6_PaymentApprovalRate | 97.29% | 97.42% | -0.13% | 780,744 | 794,598 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| DE | High (>92%) | 222,785 | 225,472 | +1.2% | Stable |
| GB | High (>92%) | 208,580 | 210,813 | +1.1% | Stable |
| FR | High (>92%) | 133,904 | 134,603 | +0.5% | Stable |
| NL | High (>92%) | 103,060 | 91,532 | -11.2% | Stable |
| AU | High (>92%) | 93,894 | 95,241 | +1.4% | Stable |
| BE | High (>92%) | 73,015 | 67,404 | -7.7% | Stable |
| DK | High (>92%) | 39,276 | 39,006 | -0.7% | Stable |
| SE | High (>92%) | 38,925 | 37,916 | -2.6% | Stable |
| NO | High (>92%) | 25,000 | 22,944 | -8.2% | Stable |
| NZ | Medium (>85%) | 19,229 | 19,343 | +0.6% | Stable |
| IE | Medium (>85%) | 19,064 | 19,292 | +1.2% | Stable |
| AT | High (>92%) | 13,663 | 13,866 | +1.5% | Stable |
| LU | High (>92%) | 3,738 | 3,435 | -8.1% | Stable |
| CH | Medium (>85%) | 2,253 | 2,298 | +2.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-05*
