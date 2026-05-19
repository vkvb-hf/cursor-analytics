# PAR Investigation: US-HF 2026-W20

**Metric:** Payment Approval Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 93.33% → 93.54% (+0.23%)  
**Volume:** 401,763 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate for US-HF improved slightly from 93.33% to 93.54% (+0.21 pp) in W20, a change that is not statistically significant and falls within normal weekly fluctuation.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | +0.19 pp | ✅ |
| 2_PreDunningAR | Recovery | +0.13 pp | ✅ |
| 3_PostDunningAR | Dunning | +0.06 pp | ✅ |
| 6_PaymentApprovalRate | Final | +0.22 pp | ✅ |

**Key Findings:**
- All funnel stages showed modest improvement, with FirstRunAR contributing the largest gain (+0.17 pp from 90.49% to 90.66%)
- No payment methods or countries exceeded the ±2.5% threshold; all dimensions remain stable
- PaymentProvider "Unknown" showed a +13.98 pp change but represents minimal volume (245 orders), flagged for monitoring only
- Apple Pay continues to underperform other methods at 87.92% vs. Credit Card at 94.06%, though it improved +0.73 pp WoW
- Volume decreased by 3.6% (416,723 → 401,763 orders) while rate improved, consistent with typical volume-rate inverse correlation

**Action:** Monitor — The change is not significant and all indicators are within normal bounds. Continue standard weekly tracking.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W20 | 93.54% | 401,763 | +0.23% ← REPORTED CHANGE |
| 2026-W19 | 93.33% | 416,723 | -0.30% |
| 2026-W18 | 93.61% | 414,920 | -0.19% |
| 2026-W17 | 93.79% | 419,106 | -0.03% |
| 2026-W16 | 93.82% | 421,948 | +0.07% |
| 2026-W15 | 93.75% | 408,631 | +0.14% |
| 2026-W14 | 93.62% | 415,886 | +0.04% |
| 2026-W13 | 93.58% | 424,103 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 94.46% | 94.31% | +0.16% | 493,780 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 96.56% | 96.58% | -0.02% | 49,033 |  |
| Credit Card | 94.06% | 93.9% | +0.17% | 296,124 |  |
| Others | 95.47% | 94.96% | +0.54% | 2,095 |  |
| Apple Pay | 87.92% | 87.29% | +0.73% | 54,511 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 1,743 |  |
| ProcessOut | 89.69% | 89.66% | +0.04% | 59,594 |  |
| Braintree | 94.2% | 93.95% | +0.27% | 339,721 |  |
| Adyen | 95.22% | 94.56% | +0.69% | 460 |  |
| Unknown | 63.27% | 55.51% | +13.98% | 245 | ⚠️ |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.66% | 90.49% | +0.19% | 401,763 | 416,723 |  |
| 2_PreDunningAR | 91.89% | 91.78% | +0.13% | 401,763 | 416,723 |  |
| 3_PostDunningAR | 92.82% | 92.77% | +0.06% | 401,763 | 416,723 |  |
| 6_PaymentApprovalRate | 93.54% | 93.33% | +0.22% | 401,763 | 416,723 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 514,530 | 493,780 | -4.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-19*
