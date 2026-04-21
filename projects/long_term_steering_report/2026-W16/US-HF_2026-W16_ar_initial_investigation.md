# AR Initial (LL0) Investigation: US-HF 2026-W16

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 89.39% → 88.9% (-0.55%)  
**Volume:** 12,393 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate (Initial Charges) for US-HF declined by -0.55pp (89.39% → 88.9%) on volume of 12,393 orders in 2026-W16; the change is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (87.6%-90.11%) | -0.55pp | ✅ |
| L1: Country Breakdown | No countries exceeded ±2.5% threshold | -0.55pp | ✅ |
| L1: PaymentMethod | All methods declined slightly; Others largest at -1.73pp | -0.35pp to -1.73pp | ✅ |
| L1: PaymentProvider | Unknown flagged at -4.00pp (170 vol) | -4.00pp | ⚠️ |
| L3: Related Metrics | All funnel stages declined similarly (-0.48pp to -0.59pp) | -0.48pp to -0.59pp | ✅ |
| Mix Shift | US Medium tier volume +13.5%, stable impact | +13.5% vol | ✅ |

**Key Findings:**
- The -0.55pp decline is within normal weekly fluctuation range observed over the 8-week period (87.6% to 90.11%)
- PaymentProvider "Unknown" shows a flagged decline of -4.00pp (97.43% → 93.53%), but impacts only 170 orders (1.4% of volume)
- All payment methods experienced minor declines, with "Others" showing the largest drop at -1.73pp on low volume (282 orders)
- Related metrics (FirstRunAR, PostDunningAR, PaymentApprovalRate) show parallel declines of -0.48pp to -0.59pp, indicating a systemic pattern rather than isolated issue
- Volume increased 13.5% week-over-week (10,922 → 12,393) with no material mix shift impact

**Action:** Monitor — The decline is not statistically significant and falls within normal operating range. Continue standard monitoring with attention to the Unknown PaymentProvider segment if the decline persists.

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
| US | 88.9% | 89.39% | -0.55% | 12,393 |  |

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

*Report: 2026-04-21*
