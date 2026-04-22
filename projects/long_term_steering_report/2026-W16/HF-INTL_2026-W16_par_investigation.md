# PAR Investigation: HF-INTL 2026-W16

**Metric:** Payment Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 97.27% → 97.4% (+0.13%)  
**Volume:** 804,152 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate for HF-INTL improved slightly from 97.27% to 97.4% (+0.13pp) in W16, a statistically non-significant change within normal operating variance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.44pp | ⚠️ |
| 2_PreDunningAR | Recovery | +0.08pp | ✅ |
| 3_PostDunningAR | Recovery | -0.11pp | ⚠️ |
| 6_PaymentApprovalRate | Final | +0.14pp | ✅ |

**Key Findings:**
- PAR at 97.4% represents the highest rate in the 8-week trend, continuing an upward trajectory from 96.22% in W09
- No countries exceeded the ±2.5% threshold; NZ showed the largest decline at -0.41pp (93.75%) while AU improved +0.50pp
- Unknown PaymentProvider flagged with +3.17pp change, but represents minimal volume (2,560 orders, <0.5% of total)
- FirstRunAR declined -0.44pp to 92.71%, suggesting initial payment attempts are slightly less successful despite overall PAR improvement
- Mix shift analysis shows stable composition across all countries, with notable volume growth in NO (+27.4%), LU (+28.5%), and SE (+22.1%)

**Action:** Monitor — The change is not statistically significant and all dimensions remain within normal thresholds. Continue standard weekly tracking.

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
| NZ | 93.75% | 94.14% | -0.41% | 18,117 |  |
| DE | 98.75% | 98.65% | +0.10% | 224,251 |  |
| BE | 99.00% | 98.80% | +0.20% | 64,642 |  |
| IE | 95.99% | 95.62% | +0.39% | 18,708 |  |
| SE | 98.13% | 97.74% | +0.40% | 38,861 |  |
| AU | 95.70% | 95.22% | +0.50% | 89,760 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 99.03% | 98.97% | +0.07% | 203,503 |  |
| Others | 99.57% | 99.49% | +0.08% | 128,100 |  |
| Credit Card | 96.81% | 96.63% | +0.19% | 363,793 |  |
| Apple Pay | 93.73% | 93.54% | +0.21% | 108,756 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 5,371 |  |
| Braintree | 97.46% | 97.39% | +0.07% | 306,655 |  |
| Adyen | 98.53% | 98.42% | +0.11% | 256,718 |  |
| ProcessOut | 96.09% | 95.87% | +0.24% | 232,848 |  |
| Unknown | 89.73% | 86.97% | +3.17% | 2,560 | ⚠️ |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 92.71% | 93.12% | -0.44% | 804,152 | 744,637 |  |
| 2_PreDunningAR | 94.82% | 94.74% | +0.08% | 804,152 | 744,637 |  |
| 3_PostDunningAR | 96.56% | 96.67% | -0.11% | 804,152 | 744,637 |  |
| 6_PaymentApprovalRate | 97.4% | 97.27% | +0.14% | 804,152 | 744,637 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| DE | High (>92%) | 201,519 | 224,251 | +11.3% | Stable |
| GB | High (>92%) | 185,598 | 209,202 | +12.7% | Stable |
| FR | High (>92%) | 147,984 | 145,977 | -1.4% | Stable |
| NL | High (>92%) | 110,805 | 109,008 | -1.6% | Stable |
| AU | High (>92%) | 85,229 | 89,760 | +5.3% | Stable |
| BE | High (>92%) | 64,439 | 64,642 | +0.3% | Stable |
| DK | High (>92%) | 37,713 | 40,108 | +6.4% | Stable |
| SE | High (>92%) | 31,821 | 38,861 | +22.1% | Stable |
| NO | High (>92%) | 18,868 | 24,045 | +27.4% | Stable |
| IE | High (>92%) | 17,513 | 18,708 | +6.8% | Stable |
| NZ | High (>92%) | 16,941 | 18,117 | +6.9% | Stable |
| AT | High (>92%) | 13,962 | 14,079 | +0.8% | Stable |
| LU | High (>92%) | 2,731 | 3,510 | +28.5% | Stable |
| CH | High (>92%) | 2,101 | 2,299 | +9.4% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
