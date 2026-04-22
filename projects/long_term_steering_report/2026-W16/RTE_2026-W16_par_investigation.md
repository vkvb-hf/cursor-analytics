# PAR Investigation: RTE 2026-W16

**Metric:** Payment Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 94.87% → 94.81% (-0.06%)  
**Volume:** 429,385 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate declined marginally from 94.87% to 94.81% (-0.06pp) on 429,385 orders in W16, a statistically non-significant change within normal operational variance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Base conversion | -0.28pp | ⚠️ |
| 2_PreDunningAR | Pre-dunning recovery | -0.20pp | ⚠️ |
| 3_PostDunningAR | Post-dunning recovery | -0.20pp | ⚠️ |
| 6_PaymentApprovalRate | Final approval | -0.06pp | ✅ |

**Key Findings:**
- The -0.06pp decline is well within the 8-week volatility range (93.26% to 95.18%), indicating normal fluctuation
- PaymentProvider "Unknown" shows a significant -12.90pp decline (71.54% → 62.31%), but with only 130 orders, impact on overall rate is negligible (<0.01pp)
- TK experienced the largest country-level decline at -1.30pp (96.15% → 94.90%), but no country exceeded the ±2.5% investigation threshold
- All high-volume segments (FJ at 395,303 orders, Credit Card at 313,971 orders, Braintree at 275,655 orders) showed minimal movement (<0.15pp)
- Dunning recovery efforts reduced the gap: FirstRunAR dropped -0.28pp while final PAR only dropped -0.06pp, indicating effective recovery mechanisms

**Action:** Monitor — No investigation required. The change is not statistically significant, no dimension exceeded alert thresholds, and the metric remains stable within historical norms.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 94.81% | 429,385 | -0.06% ← REPORTED CHANGE |
| 2026-W15 | 94.87% | 421,406 | +0.13% |
| 2026-W14 | 94.75% | 431,856 | -0.20% |
| 2026-W13 | 94.94% | 442,530 | -0.25% |
| 2026-W12 | 95.18% | 443,994 | +0.08% |
| 2026-W11 | 95.1% | 458,408 | +1.80% |
| 2026-W10 | 93.42% | 467,998 | +0.17% |
| 2026-W09 | 93.26% | 466,696 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TK | 94.90% | 96.15% | -1.30% | 2,079 |  |
| CF | 94.81% | 95.33% | -0.54% | 53,579 |  |
| FJ | 95.60% | 95.65% | -0.05% | 395,303 |  |
| YE | 93.23% | 93.01% | +0.24% | 43,089 |  |
| TZ | 94.34% | 93.23% | +1.19% | 3,216 |  |
| TO | 90.55% | 88.89% | +1.87% | 3,301 |  |
| TV | 94.69% | 92.88% | +1.95% | 2,053 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 94.59% | 94.73% | -0.15% | 313,971 |  |
| Paypal | 97.77% | 97.72% | +0.05% | 54,616 |  |
| Others | 98.46% | 98.26% | +0.21% | 5,731 |  |
| Apple Pay | 92.79% | 92.51% | +0.31% | 55,067 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 62.31% | 71.54% | -12.90% | 130 | ⚠️ |
| Adyen | 93.0% | 93.13% | -0.13% | 76,675 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 554 |  |
| Braintree | 95.69% | 95.65% | +0.03% | 275,655 |  |
| ProcessOut | 93.49% | 93.45% | +0.05% | 76,371 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.0% | 91.25% | -0.28% | 429,385 | 421,406 |  |
| 2_PreDunningAR | 92.65% | 92.83% | -0.20% | 429,385 | 421,406 |  |
| 3_PostDunningAR | 94.14% | 94.33% | -0.20% | 429,385 | 421,406 |  |
| 6_PaymentApprovalRate | 94.81% | 94.87% | -0.06% | 429,385 | 421,406 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 388,956 | 395,303 | +1.6% | Stable |
| CF | High (>92%) | 51,881 | 53,579 | +3.3% | Stable |
| YE | High (>92%) | 42,126 | 43,089 | +2.3% | Stable |
| TT | High (>92%) | 4,617 | 4,817 | +4.3% | Stable |
| TO | Medium (>85%) | 3,204 | 3,301 | +3.0% | Stable |
| TZ | High (>92%) | 2,660 | 3,216 | +20.9% | Stable |
| TK | High (>92%) | 1,950 | 2,079 | +6.6% | Stable |
| TV | High (>92%) | 1,895 | 2,053 | +8.3% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
