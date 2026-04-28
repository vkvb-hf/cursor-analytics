# PAR Investigation: RTE 2026-W17

**Metric:** Payment Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 94.81% → 94.83% (+0.02%)  
**Volume:** 430,821 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate remained essentially flat at 94.83%, up +0.02pp from 94.81% in W16, a statistically insignificant change within normal operating variance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | First attempt success | +0.16pp | ✅ |
| 2_PreDunningAR | Pre-dunning recovery | +0.12pp | ✅ |
| 3_PostDunningAR | Post-dunning recovery | -0.10pp | ⚠️ |
| 6_PaymentApprovalRate | Final approval | +0.02pp | ✅ |

**Key Findings:**
- No countries exceeded the ±2.5% threshold; TK showed the largest decline at -1.92pp (2,081 orders) but remains within acceptable bounds
- Post-dunning recovery (3_PostDunningAR) showed a slight decline of -0.10pp, partially offsetting gains in earlier funnel stages
- ProcessOut payment provider shows 0 volume in W17 vs. active volume in W16 (93.46% rate), indicating potential provider transition or data issue
- Credit Card payments improved +0.33pp to 95.09%, representing the largest payment method (235,932 orders)
- Volume mix remained stable across all country tiers with no significant shifts impacting overall rate

**Action:** Monitor – No action required. The +0.02pp change is not statistically significant and all metrics remain within normal operating ranges. Continue standard weekly monitoring.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 94.83% | 430,821 | +0.02% ← REPORTED CHANGE |
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
| TV | 93.67% | 94.64% | -1.03% | 2,101 |  |
| TZ | 93.67% | 94.34% | -0.71% | 3,221 |  |
| TT | 97.48% | 97.86% | -0.39% | 4,649 |  |
| FJ | 95.56% | 95.60% | -0.04% | 389,383 |  |
| YE | 93.48% | 93.23% | +0.26% | 44,188 |  |
| CF | 95.14% | 94.81% | +0.35% | 54,258 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 93.51% | 94.01% | -0.53% | 84,869 |  |
| Apple Pay | 92.74% | 92.79% | -0.06% | 54,842 |  |
| Paypal | 97.84% | 97.77% | +0.07% | 55,178 |  |
| Credit Card | 95.09% | 94.78% | +0.33% | 235,932 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 93.46% | +nan% | 0 |  |
| Unknown | 93.12% | 93.37% | -0.27% | 79,239 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 562 |  |
| Braintree | 95.76% | 95.69% | +0.07% | 272,767 |  |
| Adyen | 93.3% | 93.0% | +0.32% | 78,253 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.14% | 90.99% | +0.16% | 430,821 | 429,385 |  |
| 2_PreDunningAR | 92.75% | 92.64% | +0.12% | 430,821 | 429,385 |  |
| 3_PostDunningAR | 94.15% | 94.24% | -0.10% | 430,821 | 429,385 |  |
| 6_PaymentApprovalRate | 94.83% | 94.81% | +0.02% | 430,821 | 429,385 |  |

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

*Report: 2026-04-28*
