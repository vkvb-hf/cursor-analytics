# AR Overall Investigation: RTE 2026-W16

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 92.83% → 92.65% (-0.19%)  
**Volume:** 429,385 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate declined marginally from 92.83% to 92.65% (-0.19pp) in W16, a change that is not statistically significant across 429,385 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Base metric | -0.28pp | ✅ |
| 2_PreDunningAR | Reported metric | -0.20pp | ✅ |
| 3_PostDunningAR | Recovery rate | -0.20pp | ✅ |
| 6_PaymentApprovalRate | Final approval | -0.06pp | ✅ |

**Key Findings:**
- The -0.19pp decline is within normal weekly fluctuation; the 8-week trend shows rates oscillating between 91.33% (W09) and 93.20% (W11)
- No countries exceeded the ±2.5% threshold; TK showed the largest decline at -1.76pp but with low volume (2,079 orders)
- PaymentProvider "Unknown" flagged with -13.48pp decline, but represents minimal volume (130 orders) and is not materially impacting overall performance
- All major payment methods remained stable: Credit Card (-0.32pp), PayPal (-0.02pp), Apple Pay (+0.28pp)
- Volume mix shift analysis shows stable distribution across all countries with no concerning patterns

**Action:** Monitor — No intervention required. The decline is not significant and all dimension scans show stable performance within normal operating ranges.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 92.65% | 429,385 | -0.19% ← REPORTED CHANGE |
| 2026-W15 | 92.83% | 421,406 | +0.40% |
| 2026-W14 | 92.46% | 431,856 | -0.34% |
| 2026-W13 | 92.78% | 442,530 | -0.33% |
| 2026-W12 | 93.09% | 443,994 | -0.12% |
| 2026-W11 | 93.2% | 458,408 | +1.80% |
| 2026-W10 | 91.55% | 467,998 | +0.24% |
| 2026-W09 | 91.33% | 466,696 | - |

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
| Credit Card | 92.22% | 92.52% | -0.32% | 313,971 |  |
| Paypal | 96.63% | 96.65% | -0.02% | 54,616 |  |
| Others | 97.99% | 97.83% | +0.17% | 5,731 |  |
| Apple Pay | 90.59% | 90.34% | +0.28% | 55,067 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 59.23% | 68.46% | -13.48% | 130 | ⚠️ |
| Adyen | 89.64% | 89.87% | -0.26% | 76,675 |  |
| ProcessOut | 91.52% | 91.72% | -0.22% | 76,371 |  |
| Braintree | 93.8% | 93.87% | -0.07% | 275,655 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 554 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.0% | 91.25% | -0.28% | 429,385 | 421,406 |  |
| 2_PreDunningAR | 92.65% | 92.83% | -0.20% | 429,385 | 421,406 |  |
| 3_PostDunningAR | 94.16% | 94.35% | -0.20% | 429,385 | 421,406 |  |
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

*Report: 2026-04-22*
