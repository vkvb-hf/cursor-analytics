# PAR Investigation: HF-INTL 2026-W18

**Metric:** Payment Approval Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 97.42% → 97.29% (-0.13%)  
**Volume:** 780,744 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate for HF-INTL declined marginally from 97.42% to 97.29% (-0.13pp) in W18, a statistically non-significant change within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | First attempt success | -1.08pp | ⚠️ |
| 2_PreDunningAR | Pre-dunning recovery | -0.73pp | ⚠️ |
| 3_PostDunningAR | Post-dunning recovery | -0.38pp | ⚠️ |
| 6_PaymentApprovalRate | Final approval | -0.13pp | ✅ |

**Key Findings:**
- First Run Approval Rate showed the largest decline at -1.08pp (91.7% vs 92.7%), indicating upstream payment collection issues that were largely recovered through dunning processes
- No countries exceeded the ±2.5% threshold; IE showed the largest country-level decline at -0.56pp (94.95%)
- Apple Pay exhibited the weakest performance among payment methods at 94.03% (-0.28pp), while PayPal remained strongest at 98.97%
- Volume decreased 1.7% WoW (780,744 vs 794,598), with notable volume drops in NL (-11.2%), NO (-8.2%), and LU (-8.1%)
- 8-week trend shows current rate (97.29%) remains within normal historical range (97.03% - 97.42%)

**Action:** Monitor - The decline is not statistically significant and no dimensional breakdowns exceeded alert thresholds. Continue standard monitoring with attention to First Run AR trends in upcoming weeks.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W18 | 97.29% | 780,744 | -0.13% ← REPORTED CHANGE |
| 2026-W17 | 97.42% | 794,598 | +0.03% |
| 2026-W16 | 97.39% | 804,152 | +0.13% |
| 2026-W15 | 97.26% | 744,637 | +0.24% |
| 2026-W14 | 97.03% | 784,406 | -0.13% |
| 2026-W13 | 97.16% | 842,482 | -0.09% |
| 2026-W12 | 97.25% | 877,189 | +0.04% |
| 2026-W11 | 97.21% | 897,107 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| IE | 94.95% | 95.48% | -0.56% | 19,292 |  |
| AT | 97.66% | 98.10% | -0.45% | 13,866 |  |
| SE | 97.67% | 98.02% | -0.36% | 37,916 |  |
| FR | 96.56% | 96.72% | -0.16% | 134,603 |  |
| AU | 96.16% | 96.30% | -0.14% | 95,241 |  |
| NZ | 94.81% | 94.27% | +0.57% | 19,343 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 94.03% | 94.29% | -0.28% | 101,492 |  |
| Others | 97.19% | 97.35% | -0.17% | 338,948 |  |
| Credit Card | 97.53% | 97.59% | -0.06% | 140,582 |  |
| Paypal | 98.97% | 99.02% | -0.05% | 199,722 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | nan% | +nan% | 0 |  |
| Unknown | 95.95% | 96.08% | -0.14% | 225,847 |  |
| Braintree | 97.31% | 97.44% | -0.13% | 301,191 |  |
| Adyen | 98.45% | 98.55% | -0.11% | 248,862 |  |
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
| NZ | High (>92%) | 19,229 | 19,343 | +0.6% | Stable |
| IE | High (>92%) | 19,064 | 19,292 | +1.2% | Stable |
| AT | High (>92%) | 13,663 | 13,866 | +1.5% | Stable |
| LU | High (>92%) | 3,738 | 3,435 | -8.1% | Stable |
| CH | High (>92%) | 2,253 | 2,298 | +2.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-05*
