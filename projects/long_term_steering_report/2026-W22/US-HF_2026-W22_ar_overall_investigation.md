# AR Overall Investigation: US-HF 2026-W22

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 91.58% → 91.27% (-0.34%)  
**Volume:** 368,679 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** The Pre-Dunning Acceptance Rate declined by -0.31 pp (from 91.58% to 91.27%) in 2026-W22, representing a statistically non-significant change on 368,679 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.30% | ✅ |
| 2_PreDunningAR | Reported Metric | -0.33% | ✅ |
| 3_PostDunningAR | Post-Recovery | -0.53% | ⚠️ |
| 6_PaymentApprovalRate | Final Approval | -0.33% | ✅ |

**Key Findings:**
- US showed a modest decline of -0.32% (92.71% → 92.42%), remaining well within acceptable thresholds
- PaymentProvider "Unknown" flagged with -15.46% decline (51.05% → 43.16%), but volume is minimal at only 329 orders
- The 8-week trend shows a gradual declining pattern from 92.22% (W15) to 91.27% (W22), representing a cumulative -0.95 pp erosion
- PostDunningAR shows the largest funnel step decline at -0.53%, suggesting dunning recovery effectiveness may be weakening
- No countries or major payment dimensions exceeded the ±2.5% threshold requiring deep-dive investigation

**Action:** Monitor — The decline is not statistically significant and no dimensions exceeded investigation thresholds. However, the consistent 8-week downward trend warrants continued observation. If the rate drops below 91% or the trend continues for 2+ additional weeks, escalate for deeper analysis of the PostDunningAR degradation.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W22 | 91.27% | 368,679 | -0.34% ← REPORTED CHANGE |
| 2026-W21 | 91.58% | 386,911 | -0.34% |
| 2026-W20 | 91.89% | 401,763 | +0.12% |
| 2026-W19 | 91.78% | 416,724 | -0.13% |
| 2026-W18 | 91.9% | 414,920 | -0.18% |
| 2026-W17 | 92.07% | 419,106 | -0.02% |
| 2026-W16 | 92.09% | 421,948 | -0.14% |
| 2026-W15 | 92.22% | 408,631 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.42% | 92.71% | -0.32% | 455,505 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 91.07% | 92.33% | -1.36% | 2,149 |  |
| Apple Pay | 84.08% | 84.5% | -0.50% | 50,040 |  |
| Credit Card | 91.91% | 92.2% | -0.31% | 271,909 |  |
| Paypal | 95.48% | 95.69% | -0.22% | 44,581 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 43.16% | 51.05% | -15.46% | 329 | ⚠️ |
| ProcessOut | 86.31% | 87.05% | -0.85% | 56,627 |  |
| Braintree | 92.18% | 92.38% | -0.22% | 309,575 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 1,720 |  |
| Adyen | 94.63% | 93.01% | +1.73% | 428 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.1% | 90.37% | -0.30% | 368,679 | 386,911 |  |
| 2_PreDunningAR | 91.27% | 91.58% | -0.33% | 368,679 | 386,911 |  |
| 3_PostDunningAR | 92.01% | 92.5% | -0.53% | 368,679 | 386,911 |  |
| 6_PaymentApprovalRate | 92.92% | 93.23% | -0.33% | 368,679 | 386,911 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 478,645 | 455,505 | -4.8% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-02*
