# PAR Investigation: US-HF 2026-W15

**Metric:** Payment Approval Rate  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 93.76% → 93.82% (+0.06%)  
**Volume:** 421,947 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate for US-HF showed a marginal improvement of +0.06 pp (93.76% → 93.82%) in 2026-W15, which is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | +0.44 pp | ✅ |
| 2_PreDunningAR | Pre-Dunning | +0.32 pp | ✅ |
| 3_PostDunningAR | Post-Dunning | +0.02 pp | ✅ |
| 6_PaymentApprovalRate | Final PAR | +0.14 pp | ✅ |

**Key Findings:**
- All funnel stages showed positive movement, with the largest improvement at FirstRunAR (+0.44 pp), indicating upstream approval improvements are driving the overall gain
- PaymentProvider "Unknown" flagged with -3.41 pp decline (95.56% → 92.31%), but volume is minimal at 351 orders (<0.1% of total)
- PaymentMethod "Others" declined -0.70 pp (99.36% → 98.66%) on low volume (2,395 orders)
- US is the sole country in this report, showing steady improvement at +0.17 pp with stable High AR tier mix
- 8-week trend shows consistent upward trajectory from 93.16% (W09) to 93.82% (W16), representing +0.66 pp cumulative improvement

**Action:** Monitor — No significant changes detected; continue standard tracking. The minor decline in "Unknown" PaymentProvider warrants observation but not investigation given negligible volume.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 93.82% | 421,947 | +0.06% |
| 2026-W15 | 93.76% | 408,629 | +0.14% ← REPORTED CHANGE |
| 2026-W14 | 93.63% | 415,885 | +0.05% |
| 2026-W13 | 93.58% | 424,103 | +0.03% |
| 2026-W12 | 93.55% | 433,761 | -0.03% |
| 2026-W11 | 93.58% | 444,619 | +0.21% |
| 2026-W10 | 93.38% | 457,610 | +0.24% |
| 2026-W09 | 93.16% | 455,121 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 94.54% | 94.38% | +0.17% | 492,811 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 98.66% | 99.36% | -0.70% | 2,395 |  |
| Credit Card | 94.43% | 94.35% | +0.08% | 300,598 |  |
| Paypal | 96.25% | 96.05% | +0.21% | 50,099 |  |
| Apple Pay | 87.63% | 87.38% | +0.29% | 55,537 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 92.31% | 95.56% | -3.41% | 351 | ⚠️ |
| Adyen | 96.34% | 96.43% | -0.09% | 383 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 2,010 |  |
| Braintree | 94.24% | 94.1% | +0.15% | 363,787 |  |
| ProcessOut | 89.25% | 88.99% | +0.29% | 42,098 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.07% | 90.67% | +0.44% | 408,629 | 415,885 |  |
| 2_PreDunningAR | 92.22% | 91.93% | +0.32% | 408,629 | 415,885 |  |
| 3_PostDunningAR | 93.19% | 93.17% | +0.02% | 408,629 | 415,885 |  |
| 6_PaymentApprovalRate | 93.76% | 93.63% | +0.14% | 408,629 | 415,885 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 497,052 | 492,811 | -0.9% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-22*
