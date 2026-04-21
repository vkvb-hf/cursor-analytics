# PAR Investigation: RTE 2026-W16

**Metric:** Payment Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 94.87% → 94.81% (-0.06%)  
**Volume:** 429,385 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate experienced a minor decline from 94.87% to 94.81% (-0.06 pp) in W16, which is not statistically significant and remains within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.28 pp | ✅ |
| 2_PreDunningAR | Dunning Setup | -0.20 pp | ✅ |
| 3_PostDunningAR | Dunning Recovery | -0.20 pp | ✅ |
| 6_PaymentApprovalRate | Final Approval | -0.06 pp | ✅ |

**Key Findings:**
- The -0.06 pp decline is well within normal week-over-week fluctuation; the 8-week trend shows the rate has improved significantly from 93.26% (W09) to 94.81% (W16)
- TK showed the largest country-level decline at -1.76 pp (95.33% → 93.65%), but with only 2,079 orders, impact on overall rate is minimal
- PaymentProvider "Unknown" flagged with -12.90 pp decline (71.54% → 62.31%), however volume is negligible at only 130 orders
- All major payment methods remained stable: Credit Card (-0.15 pp), Paypal (+0.05 pp), Apple Pay (+0.31 pp)
- No countries exceeded the ±2.5% threshold requiring deep-dive investigation; mix shift analysis shows stable volume distribution across all regions

**Action:** Monitor — No immediate action required. The decline is not significant and all major dimensions are performing within expected ranges.

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
| TK | 93.65% | 95.33% | -1.76% | 2,079 |  |
| CF | 93.47% | 94.14% | -0.71% | 53,579 |  |
| FJ | 93.79% | 93.97% | -0.19% | 395,303 |  |
| TZ | 92.91% | 91.69% | +1.33% | 3,216 |  |
| TV | 93.52% | 92.14% | +1.50% | 2,053 |  |
| TO | 88.82% | 86.67% | +2.48% | 3,301 |  |

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
| YE | Medium (>85%) | 42,126 | 43,089 | +2.3% | Stable |
| TT | High (>92%) | 4,617 | 4,817 | +4.3% | Stable |
| TO | Medium (>85%) | 3,204 | 3,301 | +3.0% | Stable |
| TZ | Medium (>85%) | 2,660 | 3,216 | +20.9% | Stable |
| TK | High (>92%) | 1,950 | 2,079 | +6.6% | Stable |
| TV | High (>92%) | 1,895 | 2,053 | +8.3% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-21*
