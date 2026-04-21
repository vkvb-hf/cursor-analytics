# PAR Investigation: HF-INTL 2026-W16

**Metric:** Payment Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 97.27% → 97.4% (+0.13%)  
**Volume:** 804,152 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate for HF-INTL improved marginally from 97.27% to 97.4% (+0.13pp) in W16, a statistically non-significant change within normal operating variance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.45pp | ⚠️ |
| 2_PreDunningAR | Recovery | +0.07pp | ✅ |
| 3_PostDunningAR | Recovery | -0.10pp | ⚠️ |
| 6_PaymentApprovalRate | Final | +0.14pp | ✅ |

**Key Findings:**
- NO showed the largest country-level decline at -2.03pp (91.0% → 89.15%), though volume increased +27.4% (24,045 orders); still below the ±2.5% investigation threshold
- Unknown payment provider flagged with +3.14pp change (86.99% → 89.73%), but represents minimal volume (2,560 orders)
- 8-week trend shows steady recovery from W09 low of 96.22% to current 97.4%, representing +1.18pp improvement over the period
- FirstRunAR declined -0.45pp while final PAR still improved, suggesting effective dunning recovery mechanisms
- All major countries (DE, GB, FR, NL) maintained stable performance with volume growth in DE (+11.3%) and GB (+12.7%)

**Action:** Monitor — No significant changes detected; continue standard weekly tracking. Watch NO performance if volume growth continues alongside rate decline.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 97.4% | 804,152 | +0.13% ← REPORTED CHANGE |
| 2026-W15 | 97.27% | 744,637 | +0.25% |
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
| Paypal | 99.04% | 98.97% | +0.07% | 203,503 |  |
| Others | 99.57% | 99.49% | +0.08% | 128,100 |  |
| Credit Card | 96.81% | 96.64% | +0.19% | 363,793 |  |
| Apple Pay | 93.73% | 93.54% | +0.21% | 108,756 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 5,371 |  |
| Braintree | 97.46% | 97.39% | +0.07% | 306,655 |  |
| Adyen | 98.53% | 98.42% | +0.11% | 256,718 |  |
| ProcessOut | 96.09% | 95.87% | +0.23% | 232,848 |  |
| Unknown | 89.73% | 86.99% | +3.14% | 2,560 | ⚠️ |

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
