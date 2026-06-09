# PAR Investigation: US-HF 2026-W23

**Metric:** Payment Approval Rate  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 92.92% → 93.19% (+0.29%)  
**Volume:** 377,552 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate improved slightly from 92.92% to 93.19% (+0.27 pp) in US-HF for 2026-W23, representing a recovery from the prior week's decline but remaining below the 8-week high of 93.81%.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | +0.36 pp | ✅ |
| 2_PreDunningAR | Dunning Entry | +0.36 pp | ✅ |
| 3_PostDunningAR | Dunning Recovery | +0.14 pp | ✅ |
| 6_PaymentApprovalRate | Final Approval | +0.27 pp | ✅ |

**Key Findings:**
- All funnel stages showed positive movement, with the largest gains in FirstRunAR (+0.40 pp) and PreDunningAR (+0.39 pp), indicating improved upstream payment success
- No payment methods or providers exceeded the ±2.5% threshold; all dimensions showed marginal improvements within normal variance
- US volume increased by 2.4% (368,727 → 377,552 orders) with mix shift remaining stable in the High AR tier
- The change is flagged as **not significant**, consistent with the 8-week trend showing typical weekly fluctuations between 92.92% and 93.81%
- ProcessOut continues to show lower approval rates (88.44%) compared to Braintree (94.08%), though both improved marginally

**Action:** Monitor — The +0.27 pp improvement reverses last week's -0.33 pp decline and falls within normal operating variance. No dimensional anomalies require investigation.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W23 | 93.19% | 377,552 | +0.29% ← REPORTED CHANGE |
| 2026-W22 | 92.92% | 368,727 | -0.33% |
| 2026-W21 | 93.23% | 386,946 | -0.28% |
| 2026-W20 | 93.49% | 401,810 | +0.17% |
| 2026-W19 | 93.33% | 416,769 | -0.30% |
| 2026-W18 | 93.61% | 414,970 | -0.19% |
| 2026-W17 | 93.79% | 419,158 | -0.02% |
| 2026-W16 | 93.81% | 421,998 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 94.17% | 93.94% | +0.24% | 464,277 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 96.21% | 96.16% | +0.05% | 45,508 |  |
| Credit Card | 93.81% | 93.55% | +0.29% | 279,316 |  |
| Apple Pay | 87.1% | 86.67% | +0.49% | 50,552 |  |
| Others | 91.91% | 91.29% | +0.68% | 2,176 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 1,744 |  |
| ProcessOut | 88.44% | 88.39% | +0.06% | 58,555 |  |
| Braintree | 94.08% | 93.75% | +0.35% | 316,484 |  |
| Unknown | 44.12% | 43.87% | +0.58% | 306 |  |
| Adyen | 95.9% | 95.33% | +0.60% | 463 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.46% | 90.1% | +0.40% | 377,552 | 368,727 |  |
| 2_PreDunningAR | 91.63% | 91.27% | +0.39% | 377,552 | 368,727 |  |
| 3_PostDunningAR | 92.43% | 92.29% | +0.15% | 377,552 | 368,727 |  |
| 6_PaymentApprovalRate | 93.19% | 92.92% | +0.30% | 377,552 | 368,727 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 455,576 | 464,277 | +1.9% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-09*
