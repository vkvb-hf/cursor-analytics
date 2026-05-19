# AR Overall Investigation: HF-NA 2026-W20

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 92.0% → 92.15% (+0.16%)  
**Volume:** 487,754 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate for HF-NA improved marginally from 92.0% to 92.15% (+0.15pp) in W20, a statistically non-significant change within normal operating variance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Within range | +0.28pp | ✅ |
| 2_PreDunningAR | Within range | +0.17pp | ✅ |
| 3_PostDunningAR | Within range | +0.08pp | ✅ |
| 6_PaymentApprovalRate | Within range | +0.25pp | ✅ |

**Key Findings:**
- All funnel stages show modest improvement, with 1_FirstRunAR leading at +0.28pp and improvements carrying through to PaymentApprovalRate (+0.25pp)
- No countries exceeded the ±2.5% threshold; both US (+0.08pp) and CA (+0.39pp) showed stable positive movement
- 8-week trend shows the metric has been in a gradual decline from W15 (92.39%) to W19 (92.0%), with W20 representing a potential stabilization point
- Volume decreased by approximately 4% week-over-week (508,007 → 487,754 orders), consistent across both US (-4.0%) and CA (-5.4%)
- Adyen showed the strongest provider improvement at +0.71pp, while all payment methods remained within normal variance

**Action:** Monitor — No significant changes detected; all dimensions within normal operating thresholds. Continue standard weekly tracking.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W20 | 92.15% | 487,754 | +0.16% ← REPORTED CHANGE |
| 2026-W19 | 92.0% | 508,007 | -0.11% |
| 2026-W18 | 92.1% | 506,464 | -0.09% |
| 2026-W17 | 92.18% | 510,064 | -0.12% |
| 2026-W16 | 92.29% | 513,373 | -0.11% |
| 2026-W15 | 92.39% | 497,777 | +0.27% |
| 2026-W14 | 92.14% | 507,190 | -0.07% |
| 2026-W13 | 92.2% | 517,599 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.93% | 92.86% | +0.08% | 493,780 |  |
| CA | 93.80% | 93.43% | +0.39% | 99,511 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 96.2% | 96.49% | -0.30% | 4,075 |  |
| Paypal | 95.75% | 95.8% | -0.05% | 59,303 |  |
| Credit Card | 92.57% | 92.4% | +0.18% | 359,413 |  |
| Apple Pay | 86.29% | 86.04% | +0.30% | 64,963 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 65.16% | 65.51% | -0.54% | 419 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 3,192 |  |
| ProcessOut | 89.69% | 89.59% | +0.11% | 98,876 |  |
| Braintree | 92.69% | 92.54% | +0.16% | 360,493 |  |
| Adyen | 93.58% | 92.92% | +0.71% | 24,774 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.96% | 90.71% | +0.28% | 487,754 | 508,007 |  |
| 2_PreDunningAR | 92.15% | 92.0% | +0.17% | 487,754 | 508,007 |  |
| 3_PostDunningAR | 93.16% | 93.08% | +0.08% | 487,754 | 508,007 |  |
| 6_PaymentApprovalRate | 93.91% | 93.67% | +0.25% | 487,754 | 508,007 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| US | High (>92%) | 514,530 | 493,780 | -4.0% | Stable |
| CA | High (>92%) | 105,201 | 99,511 | -5.4% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-19*
