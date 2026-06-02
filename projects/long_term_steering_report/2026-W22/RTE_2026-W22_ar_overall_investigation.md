# AR Overall Investigation: RTE 2026-W22

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 92.73% → 92.91% (+0.19%)  
**Volume:** 385,852 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate improved slightly from 92.73% to 92.91% (+0.18 pp) on volume of 385,852 orders; the change is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | +0.13 pp | ✅ |
| 2_PreDunningAR | Reported Metric | +0.18 pp | ✅ |
| 3_PostDunningAR | Dunning Recovery | -0.03 pp | ✅ |
| 6_PaymentApprovalRate | Final Approval | +0.10 pp | ✅ |

**Key Findings:**
- All funnel steps remain stable with no significant degradation; the full funnel shows healthy performance
- No countries exceeded the ±2.5% threshold; TZ showed the largest decline at -0.96 pp while TT showed the strongest improvement at +0.91 pp
- PaymentProvider "Unknown" flagged with -17.58 pp decline, but volume is negligible (72 orders, <0.02% of total)
- Volume declined 3.9% WoW (401,555 → 385,852) continuing a downward trend from W15 peak of 421,405
- All payment methods showed slight improvements (+0.17 to +0.25 pp), indicating broad-based stability

**Action:** Monitor — No significant changes detected; continue standard weekly tracking.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W22 | 92.91% | 385,852 | +0.19% ← REPORTED CHANGE |
| 2026-W21 | 92.73% | 401,555 | +0.01% |
| 2026-W20 | 92.72% | 414,675 | +0.78% |
| 2026-W19 | 92.0% | 427,696 | -0.59% |
| 2026-W18 | 92.55% | 430,745 | -0.20% |
| 2026-W17 | 92.74% | 430,820 | +0.11% |
| 2026-W16 | 92.64% | 429,384 | -0.20% |
| 2026-W15 | 92.83% | 421,405 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TZ | 91.04% | 91.92% | -0.96% | 2,488 |  |
| TV | 93.47% | 94.26% | -0.84% | 1,746 |  |
| TK | 93.17% | 93.88% | -0.76% | 1,873 |  |
| CF | 93.73% | 93.62% | +0.12% | 50,421 |  |
| FJ | 93.80% | 93.68% | +0.13% | 345,674 |  |
| YE | 90.25% | 89.60% | +0.72% | 41,894 |  |
| TT | 97.29% | 96.41% | +0.91% | 4,428 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 92.57% | 92.42% | +0.17% | 283,320 |  |
| Paypal | 96.55% | 96.39% | +0.17% | 49,434 |  |
| Others | 98.14% | 97.9% | +0.24% | 5,315 |  |
| Apple Pay | 90.53% | 90.3% | +0.25% | 47,783 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 55.56% | 67.41% | -17.58% | 72 | ⚠️ |
| No Payment | 100.0% | 100.0% | +0.00% | 631 |  |
| ProcessOut | 91.76% | 91.64% | +0.13% | 81,297 |  |
| Braintree | 93.93% | 93.75% | +0.19% | 231,553 |  |
| Adyen | 90.9% | 90.57% | +0.36% | 72,299 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.21% | 91.1% | +0.13% | 385,852 | 401,555 |  |
| 2_PreDunningAR | 92.91% | 92.73% | +0.18% | 385,852 | 401,555 |  |
| 3_PostDunningAR | 94.32% | 94.35% | -0.03% | 385,852 | 401,555 |  |
| 6_PaymentApprovalRate | 94.94% | 94.84% | +0.10% | 385,852 | 401,555 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 362,650 | 345,674 | -4.7% | Stable |
| CF | High (>92%) | 50,646 | 50,421 | -0.4% | Stable |
| YE | Medium (>85%) | 41,846 | 41,894 | +0.1% | Stable |
| TT | High (>92%) | 4,517 | 4,428 | -2.0% | Stable |
| TZ | Medium (>85%) | 2,957 | 2,488 | -15.9% | Stable |
| TO | Medium (>85%) | 2,954 | 2,689 | -9.0% | Stable |
| TK | High (>92%) | 1,928 | 1,873 | -2.9% | Stable |
| TV | High (>92%) | 1,795 | 1,746 | -2.7% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-02*
