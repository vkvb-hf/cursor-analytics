# AR Overall Investigation: HF-INTL 2026-W16

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 94.74% → 94.81% (+0.07%)  
**Volume:** 804,152 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate for HF-INTL remained essentially stable in 2026-W16 at 94.81%, showing a minimal +0.07pp increase from 94.74% in W15, which is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.45pp | ⚠️ |
| 2_PreDunningAR | Reported Metric | +0.07pp | ✅ |
| 3_PostDunningAR | Recovery | -0.10pp | ✅ |
| 6_PaymentApprovalRate | Final Approval | +0.14pp | ✅ |

**Key Findings:**
- NO experienced the largest country-level decline at -2.03pp (91.00% → 89.15%), though volume increased +27.4% (24,045 orders) and remains below the ±2.5% investigation threshold
- "Unknown" PaymentProvider showed a notable +4.32pp improvement (85.30% → 88.98%), but represents minimal volume (2,560 orders)
- 1_FirstRunAR declined -0.45pp (93.12% → 92.71%), indicating slight upstream pressure that was recovered in subsequent dunning stages
- SE showed strong volume growth (+22.1%) alongside rate improvement (+1.19pp to 96.32%)
- No countries exceeded the ±2.5% threshold requiring deep-dive investigation

**Action:** Monitor – The +0.07pp change is not significant, no dimension breached investigation thresholds, and the overall rate remains stable within the 8-week trend range (93.13% - 94.90%).

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 94.81% | 804,152 | +0.07% ← REPORTED CHANGE |
| 2026-W15 | 94.74% | 744,637 | +1.19% |
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
| NO | 89.15% | 91.00% | -2.03% | 24,045 |  |
| GB | 93.92% | 94.14% | -0.23% | 209,202 |  |
| BE | 96.24% | 95.51% | +0.76% | 64,642 |  |
| LU | 95.90% | 95.06% | +0.88% | 3,510 |  |
| SE | 96.32% | 95.19% | +1.19% | 38,861 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 89.84% | 89.9% | -0.07% | 108,756 |  |
| Credit Card | 93.05% | 93.0% | +0.06% | 363,793 |  |
| Paypal | 97.87% | 97.74% | +0.13% | 203,503 |  |
| Others | 99.19% | 99.01% | +0.18% | 128,100 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 5,371 |  |
| Braintree | 95.39% | 95.38% | +0.01% | 306,655 |  |
| ProcessOut | 92.62% | 92.53% | +0.09% | 232,848 |  |
| Adyen | 96.07% | 95.98% | +0.09% | 256,718 |  |
| Unknown | 88.98% | 85.3% | +4.32% | 2,560 | ⚠️ |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 92.71% | 93.12% | -0.45% | 804,152 | 744,637 |  |
| 2_PreDunningAR | 94.81% | 94.74% | +0.07% | 804,152 | 744,637 |  |
| 3_PostDunningAR | 96.53% | 96.63% | -0.10% | 804,152 | 744,637 |  |
| 6_PaymentApprovalRate | 97.4% | 97.27% | +0.14% | 804,152 | 744,637 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| DE | High (>92%) | 201,519 | 224,251 | +11.3% | Stable |
| GB | High (>92%) | 185,598 | 209,202 | +12.7% | Stable |
| FR | High (>92%) | 147,984 | 145,977 | -1.4% | Stable |
| NL | High (>92%) | 110,805 | 109,008 | -1.6% | Stable |
| AU | Medium (>85%) | 85,229 | 89,760 | +5.3% | Stable |
| BE | High (>92%) | 64,439 | 64,642 | +0.3% | Stable |
| DK | High (>92%) | 37,713 | 40,108 | +6.4% | Stable |
| SE | High (>92%) | 31,821 | 38,861 | +22.1% | Stable |
| NO | Medium (>85%) | 18,868 | 24,045 | +27.4% | Stable |
| IE | Medium (>85%) | 17,513 | 18,708 | +6.8% | Stable |
| NZ | Medium (>85%) | 16,941 | 18,117 | +6.9% | Stable |
| AT | High (>92%) | 13,962 | 14,079 | +0.8% | Stable |
| LU | High (>92%) | 2,731 | 3,510 | +28.5% | Stable |
| CH | High (>92%) | 2,101 | 2,299 | +9.4% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
