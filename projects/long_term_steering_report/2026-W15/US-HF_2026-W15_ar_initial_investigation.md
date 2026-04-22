# AR Initial (LL0) Investigation: US-HF 2026-W15

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 89.39% → 88.9% (-0.55%)  
**Volume:** 12,393 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** The Pre-Dunning Acceptance Rate for US-HF declined by -0.55pp (from 89.39% to 88.9%) in 2026-W15, though this change is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within normal range | +1.07pp | ✅ |
| 2_PreDunningAR | Within normal range | +0.63pp | ✅ |
| 3_PostDunningAR | Within normal range | +0.65pp | ✅ |
| 6_PaymentApprovalRate | Within normal range | +0.65pp | ✅ |

**Key Findings:**
- The -0.55pp week-over-week decline in Pre-Dunning AR is within normal volatility; the 8-week trend shows rates fluctuating between 87.6% and 90.11%
- No countries exceeded the ±2.5% threshold for investigation; US is the sole market with a stable +0.63pp change in the prior period
- PayPal showed the largest negative movement among payment methods at -1.13pp (90.5% → 89.47%), though volume is relatively small at 855 orders
- All related funnel metrics (FirstRunAR, PostDunningAR, PaymentApprovalRate) showed positive movement, indicating no systemic payment processing issues
- Mix shift analysis confirms US remains in the Medium AR tier (>85%) with stable impact despite a -6.2% volume decrease

**Action:** Monitor – No immediate action required. The decline is not statistically significant and falls within normal weekly variance. Continue standard monitoring for W16.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 88.9% | 12,393 | -0.55% |
| 2026-W15 | 89.39% | 10,922 | +0.63% ← REPORTED CHANGE |
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
| US | 89.39% | 88.83% | +0.63% | 10,922 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 89.47% | 90.5% | -1.13% | 855 |  |
| Others | 97.79% | 98.06% | -0.27% | 407 |  |
| Apple Pay | 87.36% | 87.0% | +0.41% | 3,797 |  |
| Credit Card | 90.11% | 89.3% | +0.91% | 5,863 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Adyen | 100.0% | nan% | +nan% | 1 |  |
| Braintree | 87.5% | 87.53% | -0.04% | 4,791 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 95 |  |
| Unknown | 97.43% | 97.17% | +0.27% | 311 |  |
| ProcessOut | 90.36% | 89.48% | +0.98% | 5,724 |  |

---


## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 88.6% | 87.66% | +1.07% | 10,922 | 11,645 |  |
| 2_PreDunningAR | 89.39% | 88.83% | +0.63% | 10,922 | 11,645 |  |
| 3_PostDunningAR | 89.58% | 89.0% | +0.65% | 10,922 | 11,645 |  |
| 6_PaymentApprovalRate | 89.82% | 89.24% | +0.65% | 10,922 | 11,645 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | Medium (>85%) | 11,645 | 10,922 | -6.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
