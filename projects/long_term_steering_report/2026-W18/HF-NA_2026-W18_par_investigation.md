# PAR Investigation: HF-NA 2026-W18

**Metric:** Payment Approval Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 94.02% → 93.93% (-0.10%)  
**Volume:** 506,463 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate for HF-NA declined marginally from 94.02% to 93.93% (-0.09 pp) in W18, a statistically non-significant change within normal weekly fluctuation.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | -0.09 pp | ✅ |
| 2_PreDunningAR | Dunning Eligible | -0.08 pp | ✅ |
| 3_PostDunningAR | Recovery | -0.15 pp | ✅ |
| 6_PaymentApprovalRate | Final Approval | -0.10 pp | ✅ |

**Key Findings:**
- All funnel steps show minor declines (-0.08 pp to -0.15 pp), with PostDunningAR showing the largest drop at -0.15 pp, suggesting slightly reduced recovery effectiveness
- No countries exceeded the ±2.5% threshold; US declined -0.04 pp while CA improved +0.29 pp
- No payment methods or providers were flagged; "Others" payment method showed the largest decline at -0.26 pp but remains within normal range
- 8-week trend shows the rate has been relatively stable, oscillating between 93.87% and 94.13%
- Volume decreased slightly from 510,064 to 506,463 orders (-0.7%), with mix shift impact remaining stable across both US and CA

**Action:** Monitor — The decline is not statistically significant, no dimensions exceeded alert thresholds, and the metric remains within the normal 8-week range. Continue standard monitoring.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W18 | 93.93% | 506,463 | -0.10% ← REPORTED CHANGE |
| 2026-W17 | 94.02% | 510,064 | -0.12% |
| 2026-W16 | 94.13% | 513,372 | +0.03% |
| 2026-W15 | 94.1% | 497,776 | +0.12% |
| 2026-W14 | 93.99% | 507,189 | +0.03% |
| 2026-W13 | 93.96% | 517,599 | +0.10% |
| 2026-W12 | 93.87% | 526,516 | -0.04% |
| 2026-W11 | 93.91% | 539,763 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 94.57% | 94.61% | -0.04% | 516,129 |  |
| CA | 95.62% | 95.34% | +0.29% | 104,972 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 92.23% | 92.48% | -0.26% | 105,439 |  |
| Apple Pay | 88.98% | 89.12% | -0.16% | 67,968 |  |
| Credit Card | 95.2% | 95.28% | -0.09% | 271,280 |  |
| Paypal | 96.68% | 96.53% | +0.16% | 61,776 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | 100.0% | nan% | +nan% | 1 |  |
| Unknown | 91.95% | 92.2% | -0.27% | 101,635 |  |
| Braintree | 94.28% | 94.36% | -0.08% | 375,399 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 3,459 |  |
| Adyen | 95.78% | 95.41% | +0.40% | 25,969 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.88% | 90.96% | -0.09% | 506,463 | 510,064 |  |
| 2_PreDunningAR | 92.11% | 92.19% | -0.08% | 506,463 | 510,064 |  |
| 3_PostDunningAR | 93.24% | 93.38% | -0.15% | 506,463 | 510,064 |  |
| 6_PaymentApprovalRate | 93.93% | 94.02% | -0.10% | 506,463 | 510,064 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 508,019 | 516,129 | +1.6% | Stable |
| CA | High (>92%) | 104,317 | 104,972 | +0.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-05*
