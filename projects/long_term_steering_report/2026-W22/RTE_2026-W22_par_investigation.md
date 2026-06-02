# PAR Investigation: RTE 2026-W22

**Metric:** Payment Approval Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 94.84% → 94.94% (+0.11%)  
**Volume:** 385,852 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate improved marginally from 94.84% to 94.94% (+0.10pp) on 385,852 orders, a statistically non-significant change within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline conversion | +0.13pp | ✅ |
| 2_PreDunningAR | Pre-dunning recovery | +0.18pp | ✅ |
| 3_PostDunningAR | Post-dunning recovery | -0.03pp | ✅ |
| 6_PaymentApprovalRate | Final approval | +0.10pp | ✅ |

**Key Findings:**
- All funnel stages performing within normal parameters; PreDunningAR showed strongest improvement at +0.18pp
- PaymentProvider "Unknown" flagged with -20.21% change, but minimal volume (72 orders) makes this operationally insignificant
- No countries exceeded the ±2.5% threshold; TV showed largest country-level decline (-0.45pp) on low volume (1,746 orders)
- 8-week trend shows stable performance ranging 94.15%-94.94%, with current week at the high end of the range
- Volume declined -3.9% WoW (401,555 → 385,852), consistent with declining trend observed since W18

**Action:** Monitor — No investigation required. The +0.10pp change is not statistically significant, all dimensions are within thresholds, and the metric remains stable within its historical range.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W22 | 94.94% | 385,852 | +0.11% ← REPORTED CHANGE |
| 2026-W21 | 94.84% | 401,555 | +0.06% |
| 2026-W20 | 94.78% | 414,675 | +0.67% |
| 2026-W19 | 94.15% | 427,696 | -0.52% |
| 2026-W18 | 94.64% | 430,745 | -0.20% |
| 2026-W17 | 94.83% | 430,820 | +0.02% |
| 2026-W16 | 94.81% | 429,384 | -0.06% |
| 2026-W15 | 94.87% | 421,405 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TV | 94.56% | 94.99% | -0.45% | 1,746 |  |
| CF | 94.98% | 94.95% | +0.03% | 50,421 |  |
| FJ | 95.55% | 95.51% | +0.05% | 345,674 |  |
| TT | 98.26% | 97.83% | +0.44% | 4,428 |  |
| YE | 94.57% | 94.14% | +0.46% | 41,894 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 97.62% | 97.56% | +0.06% | 49,434 |  |
| Apple Pay | 92.75% | 92.67% | +0.08% | 47,783 |  |
| Others | 98.48% | 98.4% | +0.08% | 5,315 |  |
| Credit Card | 94.78% | 94.67% | +0.11% | 283,320 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 55.56% | 69.63% | -20.21% | 72 | ⚠️ |
| No Payment | 100.0% | 100.0% | +0.00% | 631 |  |
| Braintree | 95.79% | 95.7% | +0.10% | 231,553 |  |
| ProcessOut | 93.51% | 93.41% | +0.11% | 81,297 |  |
| Adyen | 93.82% | 93.63% | +0.21% | 72,299 |  |

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
| YE | High (>92%) | 41,846 | 41,894 | +0.1% | Stable |
| TT | High (>92%) | 4,517 | 4,428 | -2.0% | Stable |
| TZ | High (>92%) | 2,957 | 2,488 | -15.9% | Stable |
| TO | High (>92%) | 2,954 | 2,689 | -9.0% | Stable |
| TK | High (>92%) | 1,928 | 1,873 | -2.9% | Stable |
| TV | High (>92%) | 1,795 | 1,746 | -2.7% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-02*
