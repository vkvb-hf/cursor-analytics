# PCAR Investigation: WL 2026-W19

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 96.02% → 95.28% (-0.77%)  
**Volume:** 10,480 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate declined by -0.77 percentage points (96.02% → 95.28%) on 10,480 orders in W19, with the change flagged as not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Sustained decline pattern | -1.74pp over 4 weeks | ⚠️ |
| L1: Country Breakdown | Any country >±2.5% threshold | None exceeded | ✅ |
| L1: PaymentMethod | Credit Card performance | -1.08pp | ⚠️ |
| L1: PaymentProvider | Provider-level issues | No data available | ✅ |
| Mix Shift | Volume distribution changes | All stable | ✅ |

**Key Findings:**
- The 8-week trend shows a consistent downward trajectory from 97.59% (W16) to 95.28% (W19), representing a cumulative decline of -2.31pp over four weeks
- ER showed the largest country-level decline at -1.39pp (93.17% → 91.88%), though below the 2.5% threshold requiring deep-dive
- Credit Card payment method declined -1.08pp (94.93% → 93.90%) and represents the largest volume segment (5,805 orders), making it the primary driver of overall rate decline
- Volume has decreased ~28% from W12 (14,412) to W19 (10,480), with CG experiencing the largest week-over-week volume drop (-10.3%)
- No single country or dimension exceeded flagging thresholds, indicating a broad-based decline rather than an isolated issue

**Action:** Monitor – While the week-over-week change is not statistically significant, the sustained 4-week declining trend warrants close monitoring. If the trend continues into W20 or Credit Card approval rate drops below 93%, escalate for deeper investigation into payment processor performance.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W19 | 95.28% | 10,480 | -0.77% ← REPORTED CHANGE |
| 2026-W18 | 96.02% | 10,753 | -1.03% |
| 2026-W17 | 97.02% | 10,957 | -0.58% |
| 2026-W16 | 97.59% | 11,024 | +0.23% |
| 2026-W15 | 97.37% | 11,721 | +0.35% |
| 2026-W14 | 97.03% | 11,373 | -0.04% |
| 2026-W13 | 97.07% | 13,604 | +0.20% |
| 2026-W12 | 96.88% | 14,412 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| ER | 91.88% | 93.17% | -1.39% | 1,945 |  |
| KN | 96.46% | 97.55% | -1.12% | 2,457 |  |
| CK | 94.57% | 95.35% | -0.82% | 2,300 |  |
| CG | 96.98% | 97.65% | -0.68% | 1,791 |  |
| MR | 97.78% | 96.51% | +1.31% | 90 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | 100.0% | nan% | +nan% | 1 |  |
| Credit Card | 93.9% | 94.93% | -1.08% | 5,805 |  |
| Apple Pay | 96.82% | 97.48% | -0.68% | 3,397 |  |
| Paypal | 97.42% | 97.16% | +0.27% | 1,277 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---



## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| KN | High (>92%) | 2,534 | 2,457 | -3.0% | Stable |
| ER | High (>92%) | 2,137 | 1,945 | -9.0% | Stable |
| CK | High (>92%) | 2,127 | 2,300 | +8.1% | Stable |
| CG | High (>92%) | 1,997 | 1,791 | -10.3% | Stable |
| GN | High (>92%) | 1,102 | 1,250 | +13.4% | Stable |
| AO | High (>92%) | 770 | 647 | -16.0% | Stable |
| MR | High (>92%) | 86 | 90 | +4.7% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

No countries exceeded threshold for deep-dive.

---

*Report: 2026-05-12*
