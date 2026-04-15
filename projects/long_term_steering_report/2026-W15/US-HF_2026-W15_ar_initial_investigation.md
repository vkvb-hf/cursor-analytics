# AR Initial (LL0) Investigation: US-HF 2026-W15

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 88.81% → 89.66% (+0.96%)  
**Volume:** 12,162 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) improved from 88.81% to 89.66% (+0.85 pp) in W15, a non-significant increase within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (87.73%-90.11%) | +0.85 pp | ✅ |
| L1: Country Breakdown | US changed +1.13%, no countries exceeded ±2.5% threshold | +1.13 pp | ✅ |
| L1: Payment Method | All methods within normal variance (-0.21 to +1.17 pp) | Mixed | ✅ |
| L1: Payment Provider | ProcessOut +1.22 pp, Braintree +0.47 pp | Positive | ✅ |
| L3: Related Metrics | All funnel metrics improved (FirstRunAR +1.45 pp leading) | +0.93-1.45 pp | ✅ |
| Mix Shift | US Low tier volume decreased 3.2%, impact stable | -3.2% vol | ✅ |

**Key Findings:**
- All acceptance funnel metrics improved in parallel: FirstRunAR (+1.45 pp), PreDunningAR (+0.96 pp), PostDunningAR (+0.93 pp), and PaymentApprovalRate (+0.95 pp)
- Credit Card acceptance improved most among payment methods (+1.17 pp to 90.3%), driving the largest volume segment (6,577 orders)
- ProcessOut showed strongest provider improvement (+1.22 pp to 90.52%) with significant volume (6,433 orders)
- Volume decreased 21% week-over-week (11,533 → 12,162 orders), though still below W08-W11 levels (15,000-19,000)
- No dimensional flags triggered; all changes within normal operating thresholds

**Action:** Monitor — The improvement is not statistically significant and all metrics are moving directionally positive within expected variance. No investigation required.

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
| US | 70.51% | 69.72% | +1.13% | 23,822 |  |

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
| US | Low (>85%) | 24,598 | 23,822 | -3.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-15*
