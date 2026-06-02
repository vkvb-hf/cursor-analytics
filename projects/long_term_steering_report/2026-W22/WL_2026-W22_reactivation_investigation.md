# Reactivation Investigation: WL 2026-W22

**Metric:** Reactivation Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 89.48% → 90.86% (+1.54%)  
**Volume:** 8,322 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Reactivation Rate improved significantly from 89.48% to 90.86% (+1.54%) in W22, continuing a positive 5-week upward trend from the W17 low of 85.35%.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL Trend | 5-week upward trend | +1.54% | ✅ |
| L1: Country Scan | 1 of 5 countries flagged (AO) | +7.45% | ⚠️ |
| L1: PaymentMethod | Apple Pay, Others flagged | +5.31%, +160.00% | ⚠️ |
| L2: AO Deep-Dive | Paypal, Apple Pay improved | +5.26%, +87.50% | ✅ |
| Mix Shift | AO volume dropped 25.5% | -80 orders | ⚠️ |

**Key Findings:**
- AO showed the largest improvement (+7.45pp) driven by Paypal reactivation reaching 100% (up from 95.00%) and Apple Pay jumping from 53.33% to 100%
- Decline reason "Blocked, Restricted, Not Permitted" in AO dropped from 1.59% to 0.00% (-1.59pp), contributing to the rate improvement
- AO volume decreased significantly by 25.5% (314 → 234 orders), meaning fewer but higher-quality reactivation attempts
- Apple Pay across all markets improved +5.31pp (75.08% → 79.07%) with 731 orders
- ER contributed the highest volume (2,674 orders) with a solid +2.03pp improvement

**Action:** Monitor — The improvement is positive and driven by reduced payment blocks in AO and better Apple Pay/Paypal performance. Continue monitoring AO volume trends to ensure the volume drop doesn't mask underlying issues.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W22 | 90.86% | 8,322 | +1.54% ← REPORTED CHANGE |
| 2026-W21 | 89.48% | 6,852 | +0.08% |
| 2026-W20 | 89.41% | 7,570 | +0.77% |
| 2026-W19 | 88.73% | 9,047 | +2.57% |
| 2026-W18 | 86.51% | 7,436 | +1.36% |
| 2026-W17 | 85.35% | 7,827 | -1.68% |
| 2026-W16 | 86.81% | 8,022 | -2.78% |
| 2026-W15 | 89.29% | 9,277 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CK | 89.80% | 89.15% | +0.73% | 2,235 |  |
| KN | 91.75% | 90.55% | +1.32% | 424 |  |
| CG | 92.54% | 90.98% | +1.72% | 1,207 |  |
| ER | 90.61% | 88.81% | +2.03% | 2,674 |  |
| AO | 94.44% | 87.90% | +7.45% | 234 | ⚠️ |

**Countries exceeding ±2.5% threshold:** AO

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 93.24% | 93.33% | -0.09% | 1,584 |  |
| Credit Card | 91.71% | 90.36% | +1.50% | 5,997 |  |
| Apple Pay | 79.07% | 75.08% | +5.31% | 731 | ⚠️ |
| Others | 60.0% | 23.08% | +160.00% | 10 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: AO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Credit Card | 92.02% | 87.67% | +4.97% | 163 | 219 |  |
| Paypal | 100.00% | 95.00% | +5.26% | 60 | 80 | ⚠️ |
| Apple Pay | 100.00% | 53.33% | +87.50% | 11 | 15 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Blocked, Restricted, Not Permitted | 0 | 5 | 0.00% | 1.59% | -1.59 |
| Others | 226 | 299 | 96.58% | 95.22% | +1.36 |
| PayPal Declined, Revoked, Payer Issue | 0 | 3 | 0.00% | 0.96% | -0.96 |
| Expired, Invalid, Closed Card, No Account | 7 | 7 | 2.99% | 2.23% | +0.76 |
| CVV/CVC Mismatch | 1 | 0 | 0.43% | 0.00% | +0.43 |

**Root Cause:** Paypal + Blocked,

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 2,154 | 2,674 | +24.1% | Stable |
| CK | Medium (>85%) | 1,474 | 2,235 | +51.6% | Stable |
| CG | Medium (>85%) | 1,064 | 1,207 | +13.4% | Stable |
| MR | Medium (>85%) | 859 | 877 | +2.1% | Stable |
| GN | Medium (>85%) | 553 | 670 | +21.2% | Stable |
| KN | Medium (>85%) | 434 | 424 | -2.3% | Stable |
| AO | Medium (>85%) | 314 | 234 | -25.5% | ⚠️ Volume drop |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| AO | ↑ +7.45% | Paypal +5.3% | → Stable | Blocked, Restricted, Not Permitted -1.59pp | Paypal + Blocked, |

---

*Report: 2026-06-02*
