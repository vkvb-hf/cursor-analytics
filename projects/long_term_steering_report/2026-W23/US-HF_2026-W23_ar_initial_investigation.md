# AR Initial (LL0) Investigation: US-HF 2026-W23

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 85.71% → 85.5% (-0.25%)  
**Volume:** 10,716 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) declined slightly from 85.71% to 85.50% (-0.21pp) week-over-week, a statistically non-significant change on volume of 10,716 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.14pp | ✅ |
| 2_PreDunningAR | Reported Metric | -0.24pp | ✅ |
| 3_PostDunningAR | Post-Dunning Recovery | -0.11pp | ✅ |
| 6_PaymentApprovalRate | Final Approval | +0.20pp | ✅ |

**Key Findings:**
- US is the only country in scope and showed a minor decline of -0.24pp, well within normal variance and below the ±2.5% threshold
- PayPal payment method declined -2.84pp (87.82% → 85.32%) on 831 orders, flagged as the most notable segment deterioration
- "Others" payment method improved +5.61pp but represents only 299 orders (low impact)
- "Unknown" payment provider showed +6.24pp improvement but on minimal volume (90 orders)
- 8-week trend shows consistent gradual decline from 88.91% (W16) to 85.50% (W23), representing a cumulative -3.41pp erosion

**Action:** Monitor – The weekly change is not significant and no country exceeded thresholds. However, the sustained 8-week downward trend (-3.41pp cumulative) and PayPal's -2.84pp decline warrant continued observation. If the trend continues for 2+ more weeks, escalate for deeper investigation into PayPal performance.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W23 | 85.5% | 10,716 | -0.25% ← REPORTED CHANGE |
| 2026-W22 | 85.71% | 9,850 | -1.10% |
| 2026-W21 | 86.66% | 9,729 | -1.13% |
| 2026-W20 | 87.65% | 10,764 | -0.72% |
| 2026-W19 | 88.29% | 10,681 | -0.06% |
| 2026-W18 | 88.34% | 10,794 | -0.82% |
| 2026-W17 | 89.07% | 12,928 | +0.18% |
| 2026-W16 | 88.91% | 12,285 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 85.50% | 85.71% | -0.24% | 10,716 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 85.32% | 87.82% | -2.84% | 831 | ⚠️ |
| Credit Card | 86.18% | 86.47% | -0.34% | 6,013 |  |
| Apple Pay | 83.85% | 83.86% | -0.01% | 3,573 |  |
| Others | 91.97% | 87.08% | +5.61% | 299 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | 86.25% | 86.78% | -0.61% | 5,869 |  |
| Braintree | 84.09% | 84.31% | -0.26% | 4,543 |  |
| Adyen | 100.0% | 100.0% | +0.00% | 111 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 103 |  |
| Unknown | 73.33% | 69.03% | +6.24% | 90 | ⚠️ |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 84.71% | 84.82% | -0.14% | 10,716 | 9,850 |  |
| 2_PreDunningAR | 85.5% | 85.71% | -0.24% | 10,716 | 9,850 |  |
| 3_PostDunningAR | 85.64% | 85.74% | -0.11% | 10,716 | 9,850 |  |
| 6_PaymentApprovalRate | 85.91% | 85.74% | +0.20% | 10,716 | 9,850 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 9,850 | 10,716 | +8.8% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-06-09*
