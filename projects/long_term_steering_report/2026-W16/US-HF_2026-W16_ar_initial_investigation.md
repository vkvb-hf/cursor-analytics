# AR Initial (LL0) Investigation: US-HF 2026-W16

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 89.39% → 88.9% (-0.55%)  
**Volume:** 12,393 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) for US-HF declined from 89.39% to 88.9% (-0.49 pp) in W16, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Within normal fluctuation (87.6%-90.11% range) | -0.49 pp | ✅ |
| L1: Country Breakdown | No countries exceeded ±2.5% threshold | -0.55% | ✅ |
| L1: PaymentMethod | All methods within normal variance | -0.35% to -1.73% | ✅ |
| L1: PaymentProvider | Unknown provider flagged at -4.00% | -4.00% | ⚠️ |
| L3: Related Metrics | All funnel metrics declined similarly | -0.48% to -0.59% | ✅ |
| Mix Shift | US volume increased +13.5%, AR tier stable | N/A | ✅ |

**Key Findings:**
- The -0.49 pp decline is within the normal 8-week fluctuation range (87.6% to 90.11%) and is not statistically significant
- "Unknown" PaymentProvider showed a -4.00% decline (93.53% from 97.43%), but represents only 170 orders (1.4% of volume)
- All payment methods declined uniformly (-0.35% to -1.73%), suggesting no isolated payment processing issue
- Related funnel metrics (FirstRunAR, PostDunningAR, PaymentApprovalRate) all declined proportionally (-0.48% to -0.59%), indicating a systemic rather than stage-specific pattern
- Volume increased 13.5% week-over-week (10,922 → 12,393) while the AR tier remained stable in the Medium (>85%) category

**Action:** Monitor – Continue standard tracking. The decline is not significant, falls within historical variance, and no single dimension shows actionable degradation at meaningful volume.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 88.9% | 12,393 | -0.55% ← REPORTED CHANGE |
| 2026-W15 | 89.39% | 10,922 | +0.63% |
| 2026-W14 | 88.83% | 11,645 | +1.40% |
| 2026-W13 | 87.6% | 10,907 | -1.25% |
| 2026-W12 | 88.71% | 14,768 | -1.55% |
| 2026-W11 | 90.11% | 15,868 | +0.95% |
| 2026-W10 | 89.26% | 19,259 | +0.01% |
| 2026-W09 | 89.25% | 18,657 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 88.90% | 89.39% | -0.55% | 12,393 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 96.1% | 97.79% | -1.73% | 282 |  |
| Paypal | 89.03% | 89.47% | -0.49% | 1,003 |  |
| Apple Pay | 86.98% | 87.36% | -0.44% | 4,308 |  |
| Credit Card | 89.79% | 90.11% | -0.35% | 6,800 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 93.53% | 97.43% | -4.00% | 170 | ⚠️ |
| Braintree | 87.13% | 87.5% | -0.42% | 5,383 |  |
| ProcessOut | 90.0% | 90.36% | -0.40% | 6,719 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 112 |  |
| Adyen | 100.0% | 100.0% | +0.00% | 9 |  |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.07% | 88.6% | -0.59% | 12,393 | 10,922 |  |
| 2_PreDunningAR | 88.9% | 89.39% | -0.55% | 12,393 | 10,922 |  |
| 3_PostDunningAR | 89.1% | 89.58% | -0.54% | 12,393 | 10,922 |  |
| 6_PaymentApprovalRate | 89.39% | 89.82% | -0.48% | 12,393 | 10,922 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 10,922 | 12,393 | +13.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
