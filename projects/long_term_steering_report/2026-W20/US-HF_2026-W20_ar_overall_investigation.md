# AR Overall Investigation: US-HF 2026-W20

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 91.78% → 91.89% (+0.12%)  
**Volume:** 401,763 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Pre-Dunning Acceptance Rate for US-HF improved marginally from 91.78% to 91.89% (+0.11 pp) in 2026-W20, a statistically non-significant change on 401,763 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | +0.19 pp | ✅ |
| 2_PreDunningAR | Reported Metric | +0.13 pp | ✅ |
| 3_PostDunningAR | Post-Recovery | +0.06 pp | ✅ |
| 6_PaymentApprovalRate | Final Approval | +0.22 pp | ✅ |

**Key Findings:**
- All funnel stages showed slight improvements, with PaymentApprovalRate showing the largest gain (+0.22 pp)
- PaymentProvider "Unknown" flagged with -9.64% change, but represents minimal volume (245 orders) with negligible impact
- No countries exceeded the ±2.5% threshold; US rate improved slightly from 92.86% to 92.93% (+0.08 pp)
- 8-week trend shows gradual decline from 92.22% (W15) to current 91.89%, suggesting a slow downward drift despite this week's minor uptick
- Volume decreased by 3.6% WoW (416,723 → 401,763), consistent with the -4.0% volume shift in the High AR tier

**Action:** Monitor — No significant changes detected; continue standard tracking of the gradual 8-week downward trend.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W20 | 91.89% | 401,763 | +0.12% ← REPORTED CHANGE |
| 2026-W19 | 91.78% | 416,723 | -0.13% |
| 2026-W18 | 91.9% | 414,920 | -0.18% |
| 2026-W17 | 92.07% | 419,106 | -0.02% |
| 2026-W16 | 92.09% | 421,948 | -0.14% |
| 2026-W15 | 92.22% | 408,631 | +0.33% |
| 2026-W14 | 91.92% | 415,886 | -0.07% |
| 2026-W13 | 91.98% | 424,103 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.93% | 92.86% | +0.08% | 493,780 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 93.7% | 94.64% | -0.99% | 2,095 |  |
| Paypal | 95.87% | 95.96% | -0.09% | 49,033 |  |
| Credit Card | 92.44% | 92.34% | +0.11% | 296,124 |  |
| Apple Pay | 85.29% | 84.92% | +0.44% | 54,511 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 48.16% | 53.3% | -9.64% | 245 | ⚠️ |
| ProcessOut | 87.51% | 87.51% | +0.00% | 59,594 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 1,743 |  |
| Braintree | 92.65% | 92.49% | +0.17% | 339,721 |  |
| Adyen | 94.35% | 93.93% | +0.44% | 460 |  |

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
