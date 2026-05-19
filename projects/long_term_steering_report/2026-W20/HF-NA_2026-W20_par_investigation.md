# PAR Investigation: HF-NA 2026-W20

**Metric:** Payment Approval Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 93.67% → 93.91% (+0.26%)  
**Volume:** 487,754 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate improved slightly from 93.67% to 93.91% (+0.24 pp) in W20, representing a recovery to W18 levels after last week's dip, though this change is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Baseline | +0.28 pp | ✅ |
| 2_PreDunningAR | Dunning Entry | +0.17 pp | ✅ |
| 3_PostDunningAR | Dunning Recovery | +0.08 pp | ✅ |
| 6_PaymentApprovalRate | Final Approval | +0.25 pp | ✅ |

**Key Findings:**
- All funnel stages showed modest improvement, with FirstRunAR (+0.28 pp) contributing most to the overall PAR increase
- PaymentProvider "Unknown" showed a +14.11 pp spike (68.18% → 77.80%), but volume is minimal (419 orders) and flagged as anomaly ⚠️
- Both US (+0.16 pp) and CA (+0.40 pp) improved week-over-week, with no countries exceeding the ±2.5% threshold
- Apple Pay showed the largest improvement among payment methods (+0.55 pp), while PayPal remained flat
- Volume declined 4.0% across both countries (US -4.0%, CA -5.4%), but mix shift impact remains stable

**Action:** Monitor — The improvement is minor and not statistically significant. Continue tracking the 8-week trend, which shows PAR has been gradually declining from 94.12% (W16) to current levels. No immediate investigation required.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W20 | 93.91% | 487,754 | +0.26% ← REPORTED CHANGE |
| 2026-W19 | 93.67% | 508,007 | -0.27% |
| 2026-W18 | 93.92% | 506,464 | -0.11% |
| 2026-W17 | 94.02% | 510,064 | -0.11% |
| 2026-W16 | 94.12% | 513,373 | +0.02% |
| 2026-W15 | 94.1% | 497,777 | +0.12% |
| 2026-W14 | 93.99% | 507,190 | +0.03% |
| 2026-W13 | 93.96% | 517,599 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 94.46% | 94.31% | +0.16% | 493,780 |  |
| CA | 95.95% | 95.57% | +0.40% | 99,511 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 96.55% | 96.56% | +0.00% | 59,303 |  |
| Credit Card | 94.34% | 94.12% | +0.23% | 359,413 |  |
| Apple Pay | 88.89% | 88.4% | +0.55% | 64,963 |  |
| Others | 97.5% | 96.81% | +0.71% | 4,075 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 3,192 |  |
| ProcessOut | 91.95% | 91.8% | +0.17% | 98,876 |  |
| Braintree | 94.26% | 94.03% | +0.25% | 360,493 |  |
| Adyen | 96.07% | 95.5% | +0.60% | 24,774 |  |
| Unknown | 77.8% | 68.18% | +14.11% | 419 | ⚠️ |

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
