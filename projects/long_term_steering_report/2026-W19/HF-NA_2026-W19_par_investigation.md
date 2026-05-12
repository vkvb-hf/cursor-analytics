# PAR Investigation: HF-NA 2026-W19

**Metric:** Payment Approval Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 93.92% → 93.68% (-0.26%)  
**Volume:** 508,003 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate declined slightly from 93.92% to 93.68% (-0.24pp) in W19, a statistically non-significant change within normal weekly fluctuation.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Decline | -0.16pp | ⚠️ |
| 2_PreDunningAR | Decline | -0.10pp | ⚠️ |
| 3_PostDunningAR | Decline | -0.41pp | ⚠️ |
| 6_PaymentApprovalRate | Decline | -0.24pp | ⚠️ |

**Key Findings:**
- PostDunningAR showed the largest decline in the funnel (-0.41pp), suggesting dunning recovery effectiveness decreased more than other stages
- PaymentProvider "Unknown" dropped significantly (-13.86pp to 72.71%), though volume is minimal (436 orders) and impact is negligible
- Both US (-0.27pp) and CA (-0.04pp) declined, with US driving the majority of the change given its higher volume (514,523 orders)
- All payment methods declined, with "Others" showing the largest drop (-1.15pp) but on low volume (4,133 orders)
- Mix shift analysis shows stable country composition with no significant volume shifts between tiers

**Action:** Monitor — The decline is not statistically significant, no countries exceeded the ±2.5% threshold, and the 8-week trend shows the rate remains within historical range (93.87%-94.12%). Continue standard monitoring.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W19 | 93.68% | 508,003 | -0.26% ← REPORTED CHANGE |
| 2026-W18 | 93.92% | 506,463 | -0.11% |
| 2026-W17 | 94.02% | 510,064 | -0.11% |
| 2026-W16 | 94.12% | 513,372 | +0.02% |
| 2026-W15 | 94.1% | 497,776 | +0.12% |
| 2026-W14 | 93.99% | 507,189 | +0.03% |
| 2026-W13 | 93.96% | 517,599 | +0.10% |
| 2026-W12 | 93.87% | 526,516 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 94.32% | 94.57% | -0.27% | 514,523 |  |
| CA | 95.57% | 95.62% | -0.04% | 105,201 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 96.85% | 97.98% | -1.15% | 4,133 |  |
| Apple Pay | 88.41% | 88.96% | -0.62% | 68,133 |  |
| Credit Card | 94.12% | 94.32% | -0.21% | 373,928 |  |
| Paypal | 96.56% | 96.68% | -0.13% | 61,809 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 72.71% | 84.41% | -13.86% | 436 | ⚠️ |
| Adyen | 95.49% | 95.75% | -0.27% | 25,987 |  |
| Braintree | 94.03% | 94.27% | -0.26% | 375,545 |  |
| ProcessOut | 91.8% | 92.03% | -0.25% | 102,650 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 3,385 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.72% | 90.88% | -0.18% | 508,003 | 506,463 |  |
| 2_PreDunningAR | 92.01% | 92.11% | -0.11% | 508,003 | 506,463 |  |
| 3_PostDunningAR | 92.88% | 93.29% | -0.44% | 508,003 | 506,463 |  |
| 6_PaymentApprovalRate | 93.68% | 93.92% | -0.26% | 508,003 | 506,463 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 516,129 | 514,523 | -0.3% | Stable |
| CA | High (>92%) | 104,972 | 105,201 | +0.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-12*
