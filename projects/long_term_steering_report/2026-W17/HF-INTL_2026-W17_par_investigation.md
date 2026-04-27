# PAR Investigation: HF-INTL 2026-W17

**Metric:** Payment Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 97.39% → 97.45% (+0.06%)  
**Volume:** 794,598 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Approval Rate for HF-INTL showed a marginal improvement of +0.06 pp (97.39% → 97.45%) in W17, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | Stable | +0.00 pp | ✅ |
| 2_PreDunningAR | Slight decline | -0.19 pp | ✅ |
| 3_PostDunningAR | Decline | -0.35 pp | ⚠️ |
| 6_PaymentApprovalRate | Improvement | +0.05 pp | ✅ |

**Key Findings:**
- The +0.06 pp change continues a 5-week upward trend, with PAR rising from 96.71% (W10) to 97.45% (W17), representing a cumulative +0.74 pp improvement
- CH showed the largest country-level decline (-1.24 pp), but with only 2,253 orders, the volume impact is minimal
- PostDunningAR declined by -0.35 pp, suggesting late-stage recovery efforts were less effective this week, though this was offset by upstream improvements
- Apple Pay showed the strongest payment method improvement (+0.36 pp to 94.32%), while Credit Card also improved (+0.45 pp to 97.61%)
- ProcessOut shows 0 volume in W17 (previously 96.46% rate), indicating this provider may have been deprecated or experienced an outage

**Action:** Monitor — No thresholds exceeded and the overall trend remains stable-to-positive. Continue tracking PostDunningAR performance and ProcessOut provider status.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 97.45% | 794,598 | +0.06% ← REPORTED CHANGE |
| 2026-W16 | 97.39% | 804,152 | +0.12% |
| 2026-W15 | 97.27% | 744,637 | +0.25% |
| 2026-W14 | 97.03% | 784,406 | -0.13% |
| 2026-W13 | 97.16% | 842,482 | -0.09% |
| 2026-W12 | 97.25% | 877,189 | +0.04% |
| 2026-W11 | 97.21% | 897,107 | +0.52% |
| 2026-W10 | 96.71% | 916,831 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CH | 96.09% | 97.30% | -1.24% | 2,253 |  |
| IE | 95.52% | 95.99% | -0.49% | 19,064 |  |
| DK | 98.56% | 98.87% | -0.31% | 39,276 |  |
| FR | 96.79% | 97.05% | -0.27% | 133,904 |  |
| GB | 96.72% | 96.42% | +0.31% | 208,580 |  |
| NZ | 94.28% | 93.75% | +0.57% | 19,229 |  |
| AU | 96.30% | 95.70% | +0.62% | 93,894 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 97.38% | 97.77% | -0.40% | 350,746 |  |
| Paypal | 99.03% | 99.03% | +0.00% | 201,591 |  |
| Apple Pay | 94.32% | 93.99% | +0.36% | 101,967 |  |
| Credit Card | 97.61% | 97.17% | +0.45% | 140,294 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | 96.46% | +nan% | 0 |  |
| Braintree | 97.45% | 97.45% | +0.00% | 303,475 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 5,290 |  |
| Adyen | 98.57% | 98.53% | +0.04% | 256,294 |  |
| Unknown | 96.12% | 95.49% | +0.67% | 229,539 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 92.7% | 92.71% | +0.00% | 794,598 | 804,152 |  |
| 2_PreDunningAR | 94.63% | 94.81% | -0.19% | 794,598 | 804,152 |  |
| 3_PostDunningAR | 96.29% | 96.63% | -0.35% | 794,598 | 804,152 |  |
| 6_PaymentApprovalRate | 97.45% | 97.39% | +0.05% | 794,598 | 804,152 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| DE | High (>92%) | 224,251 | 222,785 | -0.7% | Stable |
| GB | High (>92%) | 209,202 | 208,580 | -0.3% | Stable |
| FR | High (>92%) | 145,977 | 133,904 | -8.3% | Stable |
| NL | High (>92%) | 109,008 | 103,060 | -5.5% | Stable |
| AU | High (>92%) | 89,760 | 93,894 | +4.6% | Stable |
| BE | High (>92%) | 64,642 | 73,015 | +13.0% | Stable |
| DK | High (>92%) | 40,108 | 39,276 | -2.1% | Stable |
| SE | High (>92%) | 38,861 | 38,925 | +0.2% | Stable |
| NO | High (>92%) | 24,045 | 25,000 | +4.0% | Stable |
| IE | High (>92%) | 18,708 | 19,064 | +1.9% | Stable |
| NZ | High (>92%) | 18,117 | 19,229 | +6.1% | Stable |
| AT | High (>92%) | 14,079 | 13,663 | -3.0% | Stable |
| LU | High (>92%) | 3,510 | 3,738 | +6.5% | Stable |
| CH | High (>92%) | 2,299 | 2,253 | -2.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-04-27*
