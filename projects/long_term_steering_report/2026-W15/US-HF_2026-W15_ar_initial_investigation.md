# AR Initial (LL0) Investigation: US-HF 2026-W15

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 88.81% → 89.66% (+0.96%)  
**Volume:** 12,162 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) improved from 88.81% to 89.66% (+0.96pp) in W15, a statistically non-significant change that returns the metric closer to its 8-week average range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | +1.45pp | ✅ |
| 2_PreDunningAR | Reported Metric | +0.96pp | ✅ |
| 3_PostDunningAR | Post-Recovery | +0.93pp | ✅ |
| 6_PaymentApprovalRate | Final Approval | +0.95pp | ✅ |

**Key Findings:**
- All funnel stages showed consistent improvement between +0.93pp and +1.45pp, indicating broad-based recovery rather than an isolated issue
- No payment method or provider exceeded the ±2.5% threshold; Credit Card showed the largest improvement at +1.17pp (6,577 orders)
- Volume increased modestly from 11,533 to 12,162 orders (+5.5%), with US remaining in the Medium AR tier (>85%)
- The W15 rate of 89.66% represents a recovery from the W13 dip (87.73%) and aligns with the W10-W11 performance range
- ProcessOut, handling the largest volume (6,433 orders), improved by +1.22pp while Braintree improved by +0.47pp

**Action:** Monitor — No significant anomalies detected; changes are within normal fluctuation and all dimensions are performing consistently.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 89.66% | 12,162 | +0.96% ← REPORTED CHANGE |
| 2026-W14 | 88.81% | 11,533 | +1.23% |
| 2026-W13 | 87.73% | 10,946 | -1.08% |
| 2026-W12 | 88.69% | 14,809 | -1.58% |
| 2026-W11 | 90.11% | 15,868 | +0.95% |
| 2026-W10 | 89.26% | 19,259 | +0.01% |
| 2026-W09 | 89.25% | 18,657 | -0.36% |
| 2026-W08 | 89.57% | 18,802 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 89.66% | 88.81% | +0.96% | 12,162 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 90.26% | 90.45% | -0.21% | 955 |  |
| Others | 98.07% | 98.03% | +0.04% | 415 |  |
| Apple Pay | 87.71% | 87.02% | +0.79% | 4,215 |  |
| Credit Card | 90.3% | 89.26% | +1.17% | 6,577 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Adyen | 100.0% | nan% | +nan% | 1 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 101 |  |
| Unknown | 97.45% | 97.12% | +0.35% | 314 |  |
| Braintree | 87.97% | 87.56% | +0.47% | 5,313 |  |
| ProcessOut | 90.52% | 89.42% | +1.22% | 6,433 |  |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.86% | 87.59% | +1.45% | 12,162 | 11,533 |  |
| 2_PreDunningAR | 89.66% | 88.81% | +0.96% | 12,162 | 11,533 |  |
| 3_PostDunningAR | 89.85% | 89.01% | +0.93% | 12,162 | 11,533 |  |
| 6_PaymentApprovalRate | 90.11% | 89.26% | +0.95% | 12,162 | 11,533 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 11,533 | 12,162 | +5.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-15*
