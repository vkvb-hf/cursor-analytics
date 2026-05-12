# PAR Investigation: US-HF 2026-W19

**Metric:** Payment Approval Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 93.62% → 93.33% (-0.31%)  
**Volume:** 416,719 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate declined slightly from 93.62% to 93.33% (-0.29pp) in 2026-W19, a statistically non-significant change affecting 416,719 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Rate change | -0.18pp | ✅ |
| 2_PreDunningAR | Rate change | -0.13pp | ✅ |
| 3_PostDunningAR | Rate change | -0.45pp | ⚠️ |
| 6_PaymentApprovalRate | Rate change | -0.30pp | ✅ |

**Key Findings:**
- The -0.29pp decline in PAR is within normal fluctuation and marked as not statistically significant
- PostDunningAR showed the largest funnel step decline at -0.45pp (92.98% → 92.57%), suggesting dunning recovery effectiveness weakened
- PaymentProvider "Unknown" experienced a severe drop of -33.39pp (83.33% → 55.51%), though volume is minimal (227 orders)
- PaymentMethod "Others" declined -2.92pp (97.82% → 94.96%) exceeding the ±2.5% threshold, but with low volume (2,201 orders)
- US country-level performance remains stable at 94.32% with no countries exceeding threshold flags

**Action:** Monitor – The overall decline is non-significant and driven primarily by low-volume segments (Unknown provider, Others payment method). Continue standard monitoring with attention to PostDunningAR trends over the next 2-3 weeks.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W19 | 93.33% | 416,719 | -0.31% ← REPORTED CHANGE |
| 2026-W18 | 93.62% | 414,919 | -0.18% |
| 2026-W17 | 93.79% | 419,106 | -0.03% |
| 2026-W16 | 93.82% | 421,947 | +0.07% |
| 2026-W15 | 93.75% | 408,630 | +0.14% |
| 2026-W14 | 93.62% | 415,885 | +0.04% |
| 2026-W13 | 93.58% | 424,103 | +0.04% |
| 2026-W12 | 93.54% | 433,761 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 94.32% | 94.57% | -0.27% | 514,523 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 94.96% | 97.82% | -2.92% | 2,201 | ⚠️ |
| Apple Pay | 87.3% | 87.92% | -0.71% | 57,005 |  |
| Credit Card | 93.9% | 94.13% | -0.24% | 306,602 |  |
| Paypal | 96.58% | 96.69% | -0.11% | 50,911 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 55.51% | 83.33% | -33.39% | 227 | ⚠️ |
| Adyen | 94.56% | 96.79% | -2.30% | 478 |  |
| ProcessOut | 89.66% | 89.98% | -0.36% | 60,685 |  |
| Braintree | 93.95% | 94.2% | -0.26% | 353,463 |  |
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
