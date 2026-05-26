# PAR Investigation: RTE 2026-W21

**Metric:** Payment Approval Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 94.78% → 94.85% (+0.07%)  
**Volume:** 401,555 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate improved marginally from 94.78% to 94.85% (+0.07pp) on 401,555 orders in W21, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | +0.02pp | ✅ |
| 2_PreDunningAR | Dunning Entry | +0.04pp | ✅ |
| 3_PostDunningAR | Dunning Exit | -0.02pp | ✅ |
| 6_PaymentApprovalRate | Final | +0.07pp | ✅ |

**Key Findings:**
- All funnel stages remained stable with changes within ±0.04pp, indicating no significant movement at any conversion step
- No countries exceeded the ±2.5% threshold; largest decline was TK at -0.65pp (1,928 orders) and largest gain was YE at +0.22pp (41,846 orders)
- PaymentProvider "Unknown" showed a +10.52pp increase but represents only 130 orders (negligible volume impact)
- Volume declined 3.2% week-over-week (414,675 → 401,555), consistent with declines observed across all major countries
- Mix shift analysis shows all countries remain in the High AR tier (>92%) with stable classification despite minor volume fluctuations

**Action:** Monitor — No intervention required. The +0.07pp change is within normal variance, all funnel stages are healthy, and no country or dimension breached investigation thresholds.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W21 | 94.85% | 401,555 | +0.07% ← REPORTED CHANGE |
| 2026-W20 | 94.78% | 414,675 | +0.67% |
| 2026-W19 | 94.15% | 427,696 | -0.52% |
| 2026-W18 | 94.64% | 430,745 | -0.20% |
| 2026-W17 | 94.83% | 430,820 | +0.02% |
| 2026-W16 | 94.81% | 429,384 | -0.06% |
| 2026-W15 | 94.87% | 421,405 | +0.13% |
| 2026-W14 | 94.75% | 431,855 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TK | 94.92% | 95.54% | -0.65% | 1,928 |  |
| TT | 97.83% | 98.18% | -0.36% | 4,517 |  |
| TV | 94.99% | 95.23% | -0.25% | 1,795 |  |
| CF | 94.95% | 95.13% | -0.18% | 50,646 |  |
| FJ | 95.51% | 95.41% | +0.10% | 362,650 |  |
| YE | 94.16% | 93.95% | +0.22% | 41,846 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 98.4% | 98.61% | -0.22% | 5,431 |  |
| Paypal | 97.56% | 97.59% | -0.03% | 51,447 |  |
| Credit Card | 94.68% | 94.62% | +0.06% | 294,609 |  |
| Apple Pay | 92.68% | 92.44% | +0.26% | 50,068 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Adyen | 93.63% | 93.67% | -0.03% | 73,015 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 500 |  |
| ProcessOut | 93.41% | 93.34% | +0.07% | 83,154 |  |
| Braintree | 95.7% | 95.59% | +0.12% | 244,756 |  |
| Unknown | 68.46% | 61.95% | +10.52% | 130 | ⚠️ |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.1% | 91.08% | +0.02% | 401,555 | 414,675 |  |
| 2_PreDunningAR | 92.76% | 92.72% | +0.04% | 401,555 | 414,675 |  |
| 3_PostDunningAR | 94.25% | 94.27% | -0.02% | 401,555 | 414,675 |  |
| 6_PaymentApprovalRate | 94.85% | 94.78% | +0.07% | 401,555 | 414,675 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 375,015 | 362,650 | -3.3% | Stable |
| CF | High (>92%) | 52,629 | 50,646 | -3.8% | Stable |
| YE | High (>92%) | 44,478 | 41,846 | -5.9% | Stable |
| TT | High (>92%) | 4,567 | 4,517 | -1.1% | Stable |
| TZ | High (>92%) | 2,937 | 2,957 | +0.7% | Stable |
| TO | High (>92%) | 2,871 | 2,954 | +2.9% | Stable |
| TK | High (>92%) | 1,949 | 1,928 | -1.1% | Stable |
| TV | High (>92%) | 1,823 | 1,795 | -1.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-26*
