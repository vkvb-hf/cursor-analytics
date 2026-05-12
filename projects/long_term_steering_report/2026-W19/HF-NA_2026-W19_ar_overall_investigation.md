# AR Overall Investigation: HF-NA 2026-W19

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 92.11% → 92.01% (-0.11%)  
**Volume:** 508,003 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate declined by -0.11pp (92.11% → 92.01%) on 508,003 orders in W19, a statistically non-significant change continuing a gradual downward trend observed over the past 8 weeks.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.18pp | ⚠️ |
| 2_PreDunningAR | Reported Metric | -0.11pp | ✅ |
| 3_PostDunningAR | Recovery | -0.44pp | ⚠️ |
| 6_PaymentApprovalRate | Final Approval | -0.26pp | ⚠️ |

**Key Findings:**
- No countries exceeded the ±2.5% threshold; US declined -0.13pp while CA improved slightly (+0.02pp)
- PaymentProvider "Unknown" showed a significant drop of -13.66pp (81.29% → 70.18%), though volume is minimal (436 orders)
- The "Others" payment method declined -1.10pp (97.59% → 96.52%) on 4,133 orders
- PostDunningAR shows the largest funnel decline at -0.44pp, indicating reduced recovery effectiveness
- 8-week trend shows consistent gradual decline from 92.13% (W12) to 92.01% (W19), totaling approximately -0.12pp erosion

**Action:** Monitor — The change is not statistically significant and no major dimensions exceeded thresholds. Continue tracking the gradual downward trend and the "Unknown" PaymentProvider anomaly for potential escalation if patterns persist.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W19 | 92.01% | 508,003 | -0.11% ← REPORTED CHANGE |
| 2026-W18 | 92.11% | 506,463 | -0.09% |
| 2026-W17 | 92.19% | 510,064 | -0.12% |
| 2026-W16 | 92.3% | 513,372 | -0.12% |
| 2026-W15 | 92.41% | 497,776 | +0.27% |
| 2026-W14 | 92.16% | 507,189 | -0.07% |
| 2026-W13 | 92.22% | 517,599 | +0.10% |
| 2026-W12 | 92.13% | 526,516 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.86% | 92.98% | -0.13% | 514,523 |  |
| CA | 93.50% | 93.48% | +0.02% | 105,201 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 96.52% | 97.59% | -1.10% | 4,133 |  |
| Apple Pay | 86.04% | 86.43% | -0.44% | 68,133 |  |
| Paypal | 95.82% | 95.89% | -0.08% | 61,809 |  |
| Credit Card | 92.42% | 92.46% | -0.04% | 373,928 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 70.18% | 81.29% | -13.66% | 436 | ⚠️ |
| Adyen | 93.09% | 93.31% | -0.23% | 25,987 |  |
| Braintree | 92.55% | 92.66% | -0.12% | 375,545 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 3,385 |  |
| ProcessOut | 89.6% | 89.57% | +0.03% | 102,650 |  |

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
