# AR Initial (LL0) Investigation: US-HF 2026-W17

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 88.73% → 89.24% (+0.57%)  
**Volume:** 13,134 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) improved from 88.73% to 89.24% (+0.51 pp) in W17, a statistically non-significant change within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | +0.59% | ✅ |
| 2_PreDunningAR | Reported Metric | +0.57% | ✅ |
| 3_PostDunningAR | Post-Recovery | +0.46% | ✅ |
| 6_PaymentApprovalRate | Final Approval | +0.32% | ✅ |

**Key Findings:**
- All funnel stages showed modest improvement (+0.32% to +0.59%), indicating healthy payment flow with no recovery concerns
- Credit Card payment method flagged with -7.42% decline (83.13% vs 89.79%), but low volume (160 orders) limits material impact
- No countries exceeded the ±2.5% threshold; US remains the sole market with stable Medium AR tier performance
- Volume increased +6.2% (12,365 → 13,134 orders) with no negative mix shift impact
- ProcessOut provider shows no current volume (0 orders) vs prior week activity

**Action:** Monitor — The change is not statistically significant and falls within normal 8-week variance (87.8%–90.11%). Continue tracking Credit Card payment method performance for potential emerging trend.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 89.24% | 13,134 | +0.57% ← REPORTED CHANGE |
| 2026-W16 | 88.73% | 12,365 | -0.85% |
| 2026-W15 | 89.49% | 10,974 | +0.82% |
| 2026-W14 | 88.76% | 11,560 | +1.09% |
| 2026-W13 | 87.8% | 10,879 | -0.99% |
| 2026-W12 | 88.68% | 14,818 | -1.59% |
| 2026-W11 | 90.11% | 15,868 | +0.95% |
| 2026-W10 | 89.26% | 19,259 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 89.24% | 88.73% | +0.57% | 13,134 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 83.13% | 89.79% | -7.42% | 160 | ⚠️ |
| Others | 90.01% | 89.99% | +0.02% | 7,326 |  |
| Paypal | 90.62% | 89.35% | +1.42% | 1,023 |  |
| Apple Pay | 87.94% | 86.55% | +1.60% | 4,625 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 91.51% | +nan% | 0 |  |
| Adyen | 100.0% | 100.0% | +0.00% | 40 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 66 |  |
| Unknown | 89.87% | 89.81% | +0.06% | 7,223 |  |
| Braintree | 88.27% | 86.85% | +1.63% | 5,805 |  |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.43% | 87.92% | +0.59% | 13,134 | 12,365 |  |
| 2_PreDunningAR | 89.24% | 88.73% | +0.57% | 13,134 | 12,365 |  |
| 3_PostDunningAR | 89.34% | 88.93% | +0.46% | 13,134 | 12,365 |  |
| 6_PaymentApprovalRate | 89.49% | 89.2% | +0.32% | 13,134 | 12,365 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 12,365 | 13,134 | +6.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-28*
