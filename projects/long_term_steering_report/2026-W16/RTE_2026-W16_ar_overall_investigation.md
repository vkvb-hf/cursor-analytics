# AR Overall Investigation: RTE 2026-W16

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 92.83% → 92.65% (-0.19%)  
**Volume:** 429,385 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate declined slightly from 92.83% to 92.65% (-0.18pp) in W16, a change that is not statistically significant given the volume of 429,385 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.25pp | ✅ |
| 2_PreDunningAR | Pre-Dunning Recovery | -0.18pp | ✅ |
| 3_PostDunningAR | Post-Dunning Recovery | -0.19pp | ✅ |
| 6_PaymentApprovalRate | Final Approval | -0.06pp | ✅ |

**Key Findings:**
- No countries exceeded the ±2.5% threshold; TK showed the largest decline at -1.76pp (93.65% from 95.33%) but on low volume (2,079 orders)
- PaymentProvider "Unknown" flagged with -13.48% change, but volume is negligible (130 orders) and not material to overall performance
- All major payment methods showed minimal movement: Credit Card -0.32pp, PayPal -0.02pp, Apple Pay +0.28pp
- FJ dominates volume (395,303 orders, 92% of total) with stable performance at -0.19pp
- Mix shift analysis shows all countries stable with no significant volume redistribution impacting rates

**Action:** Monitor — The decline is within normal fluctuation, not statistically significant, and no dimensional breakdowns reveal actionable root causes.

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
| Others | 98.01% | 97.83% | +0.19% | 5,731 |  |
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

*Report: 2026-04-22*
