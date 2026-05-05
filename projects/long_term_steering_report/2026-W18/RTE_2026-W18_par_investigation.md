# PAR Investigation: RTE 2026-W18

**Metric:** Payment Approval Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 94.83% → 94.65% (-0.19%)  
**Volume:** 430,746 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate declined by -0.19pp (94.83% → 94.65%) on volume of 430,746 orders in W18, a statistically non-significant change within normal weekly fluctuation range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 1_FirstRunAR | First payment attempt | -0.21pp | ⚠️ |
| 2_PreDunningAR | Before dunning | -0.21pp | ⚠️ |
| 3_PostDunningAR | After dunning | -0.29pp | ⚠️ |
| 6_PaymentApprovalRate | Final approval | -0.19pp | ⚠️ |

**Key Findings:**
- All funnel stages show minor declines (-0.19pp to -0.29pp), with PostDunningAR showing the largest drop at -0.29pp, suggesting dunning recovery was slightly less effective this week
- No countries exceeded the ±2.5% threshold; TV showed the largest country-level decline at -1.67pp but on low volume (1,964 orders)
- Payment methods show uniform minor declines: Others (-0.34pp), Apple Pay (-0.20pp), PayPal (-0.16pp), Credit Card (-0.11pp)
- Mix shift analysis indicates stable volume distribution across all countries with no significant tier migration
- 8-week trend shows PAR has declined from 95.18% (W12) to 94.65% (W18), a gradual -0.53pp erosion over 6 weeks

**Action:** Monitor — The decline is not statistically significant and no single dimension shows anomalous behavior. Continue standard weekly monitoring; if the gradual downward trend from W12 persists beyond W19, consider a trend-based investigation.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W18 | 94.65% | 430,746 | -0.19% ← REPORTED CHANGE |
| 2026-W17 | 94.83% | 430,821 | +0.02% |
| 2026-W16 | 94.81% | 429,385 | -0.06% |
| 2026-W15 | 94.87% | 421,406 | +0.13% |
| 2026-W14 | 94.75% | 431,856 | -0.20% |
| 2026-W13 | 94.94% | 442,530 | -0.25% |
| 2026-W12 | 95.18% | 443,994 | +0.08% |
| 2026-W11 | 95.1% | 458,408 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TV | 92.11% | 93.67% | -1.67% | 1,964 |  |
| TK | 91.97% | 93.08% | -1.19% | 2,017 |  |
| TZ | 93.14% | 93.67% | -0.56% | 3,134 |  |
| TO | 89.95% | 90.23% | -0.31% | 3,214 |  |
| FJ | 95.40% | 95.56% | -0.17% | 396,039 |  |
| YE | 93.61% | 93.46% | +0.16% | 45,256 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 93.19% | 93.51% | -0.34% | 88,400 |  |
| Apple Pay | 92.55% | 92.74% | -0.20% | 55,496 |  |
| Paypal | 97.69% | 97.84% | -0.16% | 55,331 |  |
| Credit Card | 94.98% | 95.09% | -0.11% | 231,519 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| ProcessOut | nan% | nan% | +nan% | 0 |  |
| Unknown | 92.81% | 93.11% | -0.32% | 82,865 |  |
| Braintree | 95.61% | 95.76% | -0.16% | 269,912 |  |
| Adyen | 93.23% | 93.29% | -0.07% | 77,411 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 558 |  |

---


## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 90.95% | 91.14% | -0.21% | 430,746 | 430,821 |  |
| 2_PreDunningAR | 92.56% | 92.75% | -0.21% | 430,746 | 430,821 |  |
| 3_PostDunningAR | 94.05% | 94.33% | -0.29% | 430,746 | 430,821 |  |
| 6_PaymentApprovalRate | 94.65% | 94.83% | -0.19% | 430,746 | 430,821 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 389,383 | 396,039 | +1.7% | Stable |
| CF | High (>92%) | 54,258 | 53,548 | -1.3% | Stable |
| YE | High (>92%) | 44,188 | 45,256 | +2.4% | Stable |
| TT | High (>92%) | 4,649 | 4,511 | -3.0% | Stable |
| TO | Medium (>85%) | 3,295 | 3,214 | -2.5% | Stable |
| TZ | High (>92%) | 3,221 | 3,134 | -2.7% | Stable |
| TV | High (>92%) | 2,101 | 1,964 | -6.5% | Stable |
| TK | High (>92%) | 2,081 | 2,017 | -3.1% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-05*
