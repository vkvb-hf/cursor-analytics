# AR Overall Investigation: US-HF 2026-W19

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 91.9% → 91.78% (-0.13%)  
**Volume:** 416,719 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Pre-Dunning Acceptance Rate for US-HF declined slightly from 91.9% to 91.78% (-0.12 pp) in 2026-W19, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.18 pp | ✅ |
| 2_PreDunningAR | Reported Metric | -0.12 pp | ✅ |
| 3_PostDunningAR | Post-Dunning Recovery | -0.41 pp | ⚠️ |
| 6_PaymentApprovalRate | Final Approval | -0.29 pp | ✅ |

**Key Findings:**
- The -0.12 pp decline in Pre-Dunning AR is within normal fluctuation and not statistically significant; this continues a gradual downward trend observed over the past 4 weeks (from 92.22% in W15 to 91.78% in W19)
- PaymentMethod "Others" showed a notable decline of -2.87 pp (97.51% → 94.64%), though volume is minimal at 2,201 orders (0.5% of total)
- PaymentProvider "Unknown" experienced a significant drop of -27.76 pp (81.06% → 53.3%), but with only 227 orders, impact is negligible
- US is the sole country in this report and showed no threshold breach (-0.12 pp change)
- Post-Dunning AR showed the largest decline across funnel metrics at -0.41 pp, suggesting reduced recovery effectiveness

**Action:** Monitor – The decline is not significant and no dimensions exceeded the ±2.5% threshold at meaningful volume. Continue tracking the gradual downward trend over the next 2-3 weeks to determine if intervention is needed.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W19 | 91.78% | 416,719 | -0.13% ← REPORTED CHANGE |
| 2026-W18 | 91.9% | 414,919 | -0.18% |
| 2026-W17 | 92.07% | 419,106 | -0.02% |
| 2026-W16 | 92.09% | 421,947 | -0.14% |
| 2026-W15 | 92.22% | 408,630 | +0.33% |
| 2026-W14 | 91.92% | 415,885 | -0.07% |
| 2026-W13 | 91.98% | 424,103 | +0.05% |
| 2026-W12 | 91.93% | 433,761 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.86% | 92.98% | -0.13% | 514,523 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 94.64% | 97.51% | -2.94% | 2,201 | ⚠️ |
| Apple Pay | 84.92% | 85.3% | -0.45% | 57,005 |  |
| Credit Card | 92.34% | 92.41% | -0.07% | 306,602 |  |
| Paypal | 95.97% | 95.99% | -0.02% | 50,911 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 53.3% | 81.06% | -34.24% | 227 | ⚠️ |
| Adyen | 93.93% | 94.95% | -1.08% | 478 |  |
| Braintree | 92.49% | 92.59% | -0.11% | 353,463 |  |
| ProcessOut | 87.51% | 87.59% | -0.08% | 60,685 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 1,866 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.49% | 90.65% | -0.18% | 416,719 | 414,919 |  |
| 2_PreDunningAR | 91.78% | 91.9% | -0.13% | 416,719 | 414,919 |  |
| 3_PostDunningAR | 92.57% | 92.98% | -0.45% | 416,719 | 414,919 |  |
| 6_PaymentApprovalRate | 93.33% | 93.62% | -0.30% | 416,719 | 414,919 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 516,129 | 514,523 | -0.3% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-12*
