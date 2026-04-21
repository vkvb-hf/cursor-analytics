# AR Overall Investigation: HF-INTL 2026-W16

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 94.74% → 94.81% (+0.07%)  
**Volume:** 804,152 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate for HF-INTL improved marginally from 94.74% to 94.81% (+0.07pp) in 2026-W16, a statistically non-significant change across 804,152 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.45pp | ⚠️ |
| 2_PreDunningAR | Reported Metric | +0.07pp | ✅ |
| 3_PostDunningAR | Downstream | -0.10pp | ✅ |
| 6_PaymentApprovalRate | Final Approval | +0.14pp | ✅ |

**Key Findings:**
- No countries exceeded the ±2.5% threshold; NO showed the largest decline at -2.03pp (89.15%) but remains within tolerance
- Unknown PaymentProvider flagged with +4.32pp change, but represents minimal volume (2,560 orders / 0.3% of total)
- SE and NO experienced significant volume growth (+22.1% and +27.4% respectively) without material rate degradation
- 1_FirstRunAR declined by -0.45pp while pre-dunning recovery offset this, indicating dunning effectiveness remains stable
- All major payment methods (Credit Card, PayPal, Apple Pay) showed stable performance within ±0.15pp

**Action:** Monitor — The +0.07pp change is not statistically significant and all dimensions remain within normal operating parameters. Continue standard weekly tracking.

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
| NO | 89.15% | 91.0% | -2.03% | 24,045 |  |
| GB | 93.92% | 94.14% | -0.23% | 209,202 |  |
| BE | 96.24% | 95.51% | +0.76% | 64,642 |  |
| LU | 95.9% | 95.06% | +0.88% | 3,510 |  |
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
| Adyen | 96.07% | 95.98% | +0.09% | 256,718 |  |
| ProcessOut | 92.62% | 92.53% | +0.09% | 232,848 |  |
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

*Report: 2026-04-21*
