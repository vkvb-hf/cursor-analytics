# PAR Investigation: US-HF 2026-W17

**Metric:** Payment Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 93.82% → 93.8% (-0.02%)  
**Volume:** 419,106 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate for US-HF remained essentially stable in 2026-W17, declining marginally by -0.02pp (93.82% → 93.80%), a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | +0.06pp | ✅ |
| 2_PreDunningAR | Pre-Dunning | -0.03pp | ✅ |
| 3_PostDunningAR | Post-Dunning | -0.17pp | ⚠️ |
| 6_PaymentApprovalRate | Final PAR | -0.02pp | ✅ |

**Key Findings:**
- The -0.02pp decline in PAR is within normal weekly fluctuation and flagged as not significant
- Post-Dunning AR showed the largest funnel degradation at -0.17pp (93.08% → 92.92%), suggesting slightly reduced dunning recovery effectiveness
- "Others" payment method declined -0.53pp (91.28% → 90.80%) with 61K volume, the largest drop among payment methods
- All payment providers remained stable; ProcessOut shows no volume in the current week (previously had activity)
- 8-week trend shows PAR has been gradually improving from 93.38% (W10) to 93.80% (W17), with this week's minor dip not breaking the positive trajectory

**Action:** Monitor — No action required. The change is not significant and all dimensions remain within acceptable thresholds. Continue standard weekly monitoring.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 93.8% | 419,106 | -0.02% ← REPORTED CHANGE |
| 2026-W16 | 93.82% | 421,947 | +0.06% |
| 2026-W15 | 93.76% | 408,630 | +0.14% |
| 2026-W14 | 93.63% | 415,885 | +0.05% |
| 2026-W13 | 93.58% | 424,103 | +0.03% |
| 2026-W12 | 93.55% | 433,761 | -0.03% |
| 2026-W11 | 93.58% | 444,619 | +0.21% |
| 2026-W10 | 93.38% | 457,610 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 94.62% | 94.59% | +0.03% | 508,019 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 90.8% | 91.28% | -0.53% | 61,124 |  |
| Apple Pay | 88.16% | 88.06% | +0.12% | 58,028 |  |
| Paypal | 96.6% | 96.49% | +0.12% | 51,246 |  |
| Credit Card | 95.27% | 95.04% | +0.24% | 248,708 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 90.34% | +nan% | 0 |  |
| Unknown | 90.48% | 90.91% | -0.47% | 59,076 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 1,977 |  |
| Braintree | 94.31% | 94.26% | +0.05% | 357,625 |  |
| Adyen | 96.26% | 96.04% | +0.23% | 428 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.84% | 90.79% | +0.06% | 419,106 | 421,947 |  |
| 2_PreDunningAR | 92.07% | 92.1% | -0.03% | 419,106 | 421,947 |  |
| 3_PostDunningAR | 92.92% | 93.08% | -0.17% | 419,106 | 421,947 |  |
| 6_PaymentApprovalRate | 93.8% | 93.82% | -0.02% | 419,106 | 421,947 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 511,272 | 508,019 | -0.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-28*
