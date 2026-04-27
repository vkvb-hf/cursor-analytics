# PAR Investigation: US-HF 2026-W17

**Metric:** Payment Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 93.82% → 93.8% (-0.02%)  
**Volume:** 419,106 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate (PAR) remained essentially flat in US-HF, declining marginally from 93.82% to 93.8% (-0.02pp), a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | First payment attempt | +0.06pp | ✅ |
| 2_PreDunningAR | Pre-dunning recovery | -0.03pp | ✅ |
| 3_PostDunningAR | Post-dunning recovery | -0.18pp | ⚠️ |
| 6_PaymentApprovalRate | Final approval | -0.02pp | ✅ |

**Key Findings:**
- The -0.02pp PAR decline is within normal variance and flagged as not significant; the 8-week trend shows stable performance ranging from 93.38% to 93.82%
- Post-dunning recovery (PostDunningAR) showed the largest funnel decline at -0.18pp (93.07% → 92.9%), partially offsetting gains in FirstRunAR (+0.06pp)
- No payment methods or providers exceeded alert thresholds; "Others" payment method showed the largest decline (-0.51pp) but remains within acceptable range
- US country-level performance actually improved slightly (+0.04pp), indicating no geographic concerns
- Volume mix remained stable with US High AR tier showing minimal shift (-0.6% volume change)

**Action:** Monitor — No investigation required. The change is not statistically significant and all dimensions remain within normal operating ranges. Continue standard weekly monitoring.

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
| US | 94.62% | 94.59% | +0.04% | 508,019 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 90.81% | 91.28% | -0.51% | 61,159 |  |
| Paypal | 96.6% | 96.49% | +0.12% | 51,246 |  |
| Apple Pay | 88.17% | 88.06% | +0.13% | 58,028 |  |
| Credit Card | 95.27% | 95.04% | +0.24% | 248,673 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 90.34% | +nan% | 0 |  |
| Unknown | 90.5% | 90.91% | -0.45% | 59,105 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 1,977 |  |
| Braintree | 94.31% | 94.26% | +0.05% | 357,596 |  |
| Adyen | 96.26% | 96.04% | +0.23% | 428 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.84% | 90.79% | +0.06% | 419,106 | 421,947 |  |
| 2_PreDunningAR | 92.07% | 92.1% | -0.03% | 419,106 | 421,947 |  |
| 3_PostDunningAR | 92.9% | 93.07% | -0.18% | 419,106 | 421,947 |  |
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

*Report: 2026-04-27*
