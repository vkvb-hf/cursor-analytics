# PAR Investigation: HF-INTL 2026-W15

**Metric:** Payment Approval Rate  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 97.27% → 97.4% (+0.13%)  
**Volume:** 804,152 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate for HF-INTL improved slightly from 97.27% to 97.4% (+0.13pp) in 2026-W15, a statistically non-significant change on a volume of 804,152 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within range | +1.77pp | ✅ |
| 2_PreDunningAR | Within range | +1.19pp | ✅ |
| 3_PostDunningAR | Within range | +0.12pp | ✅ |
| 6_PaymentApprovalRate | Within range | +0.24pp | ✅ |

**Key Findings:**
- The 8-week trend shows consistent improvement from 96.22% (W09) to 97.4% (W16), representing a +1.18pp cumulative gain over this period
- No countries exceeded the ±2.5% threshold; CH showed the largest decline (-1.13pp) while DK (+1.34pp) and NO (+1.16pp) showed the strongest improvements
- All payment methods showed stable or improving performance, with Apple Pay showing the largest gain (+0.83pp) albeit from the lowest baseline (93.54%)
- Upstream funnel metrics improved more substantially than PAR itself, with FirstRunAR up +1.77pp and PreDunningAR up +1.19pp
- Volume mix shifts were stable across all countries despite notable volume changes in DK (+25.6%) and NO (+39.2%)

**Action:** Monitor – No investigation required. The metric change is not statistically significant and all dimensions remain within normal operating ranges.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 97.4% | 804,152 | +0.13% |
| 2026-W15 | 97.27% | 744,637 | +0.25% ← REPORTED CHANGE |
| 2026-W14 | 97.03% | 784,406 | -0.13% |
| 2026-W13 | 97.16% | 842,482 | -0.09% |
| 2026-W12 | 97.25% | 877,189 | +0.04% |
| 2026-W11 | 97.21% | 897,107 | +0.52% |
| 2026-W10 | 96.71% | 916,831 | +0.51% |
| 2026-W09 | 96.22% | 896,537 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CH | 97.19% | 98.30% | -1.13% | 2,101 |  |
| DE | 98.65% | 98.49% | +0.16% | 201,519 |  |
| GB | 96.38% | 96.22% | +0.17% | 185,598 |  |
| FR | 97.03% | 96.79% | +0.25% | 147,984 |  |
| NZ | 94.14% | 93.44% | +0.75% | 16,941 |  |
| NO | 97.51% | 96.39% | +1.16% | 18,868 |  |
| DK | 98.93% | 97.62% | +1.34% | 37,713 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 99.49% | 99.49% | +0.00% | 121,157 |  |
| Paypal | 98.97% | 98.92% | +0.05% | 185,690 |  |
| Credit Card | 96.64% | 96.38% | +0.27% | 338,143 |  |
| Apple Pay | 93.54% | 92.77% | +0.83% | 99,647 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 86.99% | 87.56% | -0.64% | 2,299 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 4,522 |  |
| Adyen | 98.42% | 98.35% | +0.06% | 241,311 |  |
| Braintree | 97.39% | 97.09% | +0.31% | 280,104 |  |
| ProcessOut | 95.87% | 95.5% | +0.38% | 216,401 |  |

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
| AU | High (>92%) | 96,471 | 85,229 | -11.7% | Stable |
| BE | High (>92%) | 74,093 | 64,439 | -13.0% | Stable |
| SE | High (>92%) | 35,624 | 31,821 | -10.7% | Stable |
| DK | High (>92%) | 30,036 | 37,713 | +25.6% | Stable |
| NZ | High (>92%) | 19,364 | 16,941 | -12.5% | Stable |
| IE | High (>92%) | 18,775 | 17,513 | -6.7% | Stable |
| NO | High (>92%) | 13,551 | 18,868 | +39.2% | Stable |
| AT | High (>92%) | 12,458 | 13,962 | +12.1% | Stable |
| LU | High (>92%) | 2,765 | 2,731 | -1.2% | Stable |
| CH | High (>92%) | 2,174 | 2,101 | -3.4% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
