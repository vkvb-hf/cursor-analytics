# PAR Investigation: RTE 2026-W17

**Metric:** Payment Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 94.81% → 94.84% (+0.03%)  
**Volume:** 430,821 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate remained essentially flat at 94.84%, increasing by just +0.03 pp from the prior week—a statistically insignificant change within normal operating variance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline conversion | +0.16 pp | ✅ |
| 2_PreDunningAR | Pre-dunning recovery | +0.12 pp | ✅ |
| 3_PostDunningAR | Post-dunning recovery | -0.14 pp | ⚠️ |
| 6_PaymentApprovalRate | Final approval | +0.03 pp | ✅ |

**Key Findings:**
- No countries exceeded the ±2.5% threshold; TK showed the largest decline at -1.92 pp but with minimal volume (2,081 orders)
- ProcessOut provider shows no volume in current week (0 orders) compared to prior week activity—potential data gap or provider discontinuation
- Post-dunning recovery step showed slight underperformance (-0.14 pp), partially offsetting gains from earlier funnel stages
- Credit Card payment method improved +0.33 pp and represents the largest volume segment (235,907 orders)
- 8-week trend shows gradual decline from W11 peak (95.10%) to current levels, though still well above W10 low (93.42%)

**Action:** Monitor — No significant changes detected. Continue standard weekly review cadence.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 94.84% | 430,821 | +0.03% ← REPORTED CHANGE |
| 2026-W16 | 94.81% | 429,385 | -0.06% |
| 2026-W15 | 94.87% | 421,406 | +0.13% |
| 2026-W14 | 94.75% | 431,856 | -0.20% |
| 2026-W13 | 94.94% | 442,530 | -0.25% |
| 2026-W12 | 95.18% | 443,994 | +0.08% |
| 2026-W11 | 95.1% | 458,408 | +1.80% |
| 2026-W10 | 93.42% | 467,998 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TK | 93.08% | 94.90% | -1.92% | 2,081 |  |
| TV | 93.67% | 94.69% | -1.08% | 2,101 |  |
| TZ | 93.67% | 94.34% | -0.71% | 3,221 |  |
| TT | 97.48% | 97.86% | -0.39% | 4,649 |  |
| FJ | 95.57% | 95.60% | -0.04% | 389,383 |  |
| YE | 93.48% | 93.23% | +0.27% | 44,188 |  |
| CF | 95.15% | 94.81% | +0.36% | 54,258 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 93.52% | 94.01% | -0.52% | 84,895 |  |
| Apple Pay | 92.75% | 92.79% | -0.04% | 54,842 |  |
| Paypal | 97.85% | 97.77% | +0.07% | 55,177 |  |
| Credit Card | 95.09% | 94.78% | +0.33% | 235,907 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 93.46% | +nan% | 0 |  |
| Unknown | 93.13% | 93.37% | -0.26% | 79,263 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 562 |  |
| Braintree | 95.76% | 95.69% | +0.07% | 272,741 |  |
| Adyen | 93.31% | 93.0% | +0.33% | 78,255 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.14% | 90.99% | +0.16% | 430,821 | 429,385 |  |
| 2_PreDunningAR | 92.76% | 92.64% | +0.12% | 430,821 | 429,385 |  |
| 3_PostDunningAR | 94.08% | 94.21% | -0.14% | 430,821 | 429,385 |  |
| 6_PaymentApprovalRate | 94.84% | 94.81% | +0.03% | 430,821 | 429,385 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 395,303 | 389,383 | -1.5% | Stable |
| CF | High (>92%) | 53,579 | 54,258 | +1.3% | Stable |
| YE | High (>92%) | 43,089 | 44,188 | +2.6% | Stable |
| TT | High (>92%) | 4,817 | 4,649 | -3.5% | Stable |
| TO | Medium (>85%) | 3,301 | 3,295 | -0.2% | Stable |
| TZ | High (>92%) | 3,216 | 3,221 | +0.2% | Stable |
| TK | High (>92%) | 2,079 | 2,081 | +0.1% | Stable |
| TV | High (>92%) | 2,053 | 2,101 | +2.3% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-27*
