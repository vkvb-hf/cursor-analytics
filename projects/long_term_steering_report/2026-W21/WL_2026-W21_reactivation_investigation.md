# Reactivation Investigation: WL 2026-W21

**Metric:** Reactivation Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 89.41% → 89.48% (+0.08%)  
**Volume:** 6,852 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Reactivation Rate showed a marginal improvement from 89.41% to 89.48% (+0.08 pp) in W21, a statistically non-significant change with volume of 6,852 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Stable upward trend from W14 (88.67%) to W21 (89.48%) | +0.08 pp | ✅ |
| L1: Country Scan | AO exceeds ±2.5% threshold | -3.24 pp | ⚠️ |
| L1: PaymentMethod | "Others" flagged with -65.38% change | Low volume (13) | ⚠️ |
| L2: AO Deep-Dive | Apple Pay significant decline | -22.96% | ⚠️ |
| Mix Shift | GN volume dropped -24.2% | Minimal rate impact | ⚠️ |

**Key Findings:**
- AO is the only country exceeding the ±2.5% threshold with a -3.24 pp decline (87.90% vs 90.84% prior week)
- Within AO, Apple Pay experienced a significant drop from 69.23% to 53.33% (-22.96%), though on low volume (15 orders)
- AO decline reasons show "Expired, Invalid, Closed Card, No Account" decreased by -2.53 pp, while "Others" increased by +1.45 pp
- GN experienced a notable volume drop of -24.2% (730 → 553 orders) but maintained stable rates
- Overall WL metric continues a positive 4-week trend since W17 (85.35% → 89.48%)

**Action:** Monitor – The overall change is not statistically significant and the metric remains stable. Continue monitoring AO Apple Pay performance over the next 1-2 weeks to determine if the decline persists or normalizes given the low volume involved.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W21 | 89.48% | 6,852 | +0.08% ← REPORTED CHANGE |
| 2026-W20 | 89.41% | 7,570 | +0.77% |
| 2026-W19 | 88.73% | 9,047 | +2.57% |
| 2026-W18 | 86.51% | 7,436 | +1.36% |
| 2026-W17 | 85.35% | 7,827 | -1.68% |
| 2026-W16 | 86.81% | 8,022 | -2.78% |
| 2026-W15 | 89.29% | 9,277 | +0.70% |
| 2026-W14 | 88.67% | 7,706 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| AO | 87.90% | 90.84% | -3.24% | 314 | ⚠️ |
| CG | 90.98% | 90.25% | +0.80% | 1,064 |  |
| MR | 88.94% | 87.80% | +1.30% | 859 |  |
| KN | 90.55% | 89.28% | +1.43% | 434 |  |

**Countries exceeding ±2.5% threshold:** AO

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 23.08% | 66.67% | -65.38% | 13 | ⚠️ |
| Paypal | 93.33% | 93.37% | -0.04% | 1,320 |  |
| Credit Card | 90.36% | 90.35% | +0.00% | 4,925 |  |
| Apple Pay | 75.08% | 73.52% | +2.13% | 594 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: AO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 53.33% | 69.23% | -22.96% | 15 | 13 | ⚠️ |
| Paypal | 95.00% | 98.11% | -3.17% | 80 | 53 |  |
| Credit Card | 87.67% | 90.34% | -2.95% | 219 | 207 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Expired, Invalid, Closed Card, No Account | 7 | 13 | 2.23% | 4.76% | -2.53 |
| Others | 299 | 256 | 95.22% | 93.77% | +1.45 |
| PayPal Declined, Revoked, Payer Issue | 3 | 1 | 0.96% | 0.37% | +0.59 |
| Blocked, Restricted, Not Permitted | 5 | 3 | 1.59% | 1.10% | +0.49 |

**Root Cause:** Apple + Expired,

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 2,543 | 2,154 | -15.3% | Stable |
| CK | Medium (>85%) | 1,561 | 1,474 | -5.6% | Stable |
| CG | Medium (>85%) | 1,149 | 1,064 | -7.4% | Stable |
| MR | Medium (>85%) | 885 | 859 | -2.9% | Stable |
| GN | Medium (>85%) | 730 | 553 | -24.2% | ⚠️ Volume drop |
| KN | Medium (>85%) | 429 | 434 | +1.2% | Stable |
| AO | Medium (>85%) | 273 | 314 | +15.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| AO | ↓ -3.24% | Apple Pay -23.0% | → Stable | Expired, Invalid, Closed Card, No Account -2.53pp | Apple + Expired, |

---

*Report: 2026-05-26*
