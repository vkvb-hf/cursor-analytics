# Reactivation Investigation: WL 2026-W23

**Metric:** Reactivation Rate  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 90.86% → 91.33% (+0.52%)  
**Volume:** 9,240 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Reactivation Rate improved by +0.52pp (90.86% → 91.33%) on volume of 9,240 orders, a statistically non-significant change continuing an 8-week upward trend.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Consistent improvement since W16 | +4.52pp over 8 weeks | ✅ |
| L1: Country Breakdown | 2 countries flagged (GQ, KN) | GQ -100.00pp, KN -3.19pp | ⚠️ |
| L1: Dimension Scan | PaymentMethod "Others" flagged | -72.22% change | ⚠️ |
| L2: GQ Deep-Dive | Single order failure | 1 order, 0% rate | ✅ (negligible volume) |
| L2: KN Deep-Dive | Apple Pay underperformance | -8.16% change on 93 orders | ⚠️ |
| Mix Shift | AO major volume drop, CK volume drop | AO -45.3%, CK -22.0% | ⚠️ |

**Key Findings:**
- GQ's -100.00pp drop is statistically irrelevant (1 order total) and should be dismissed as noise
- KN shows meaningful degradation (-3.19pp) driven primarily by Apple Pay performance decline (-8.16% on 93 orders) with "Others" decline reasons increasing
- Strong positive 8-week trend continues with rate improving from 86.81% (W16) to 91.33% (W23), representing +4.52pp sustained growth
- Mix shift detected in AO (-45.3% volume) and CK (-22.0% volume), though neither country shows rate deterioration
- Credit Card remains the dominant and stable payment method (92.72% rate, 6,715 orders)

**Action:** Monitor - The overall trend is positive and the week-over-week change is not statistically significant. KN's Apple Pay performance warrants observation over the next 2-3 weeks to determine if the decline persists.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W23 | 91.33% | 9,240 | +0.52% ← REPORTED CHANGE |
| 2026-W22 | 90.86% | 8,322 | +1.54% |
| 2026-W21 | 89.48% | 6,852 | +0.08% |
| 2026-W20 | 89.41% | 7,570 | +0.77% |
| 2026-W19 | 88.73% | 9,047 | +2.57% |
| 2026-W18 | 86.51% | 7,436 | +1.36% |
| 2026-W17 | 85.35% | 7,827 | -1.68% |
| 2026-W16 | 86.81% | 8,022 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| GQ | 0.00% | 100.00% | -100.00% | 1 | ⚠️ |
| KN | 88.81% | 91.75% | -3.19% | 447 | ⚠️ |
| MR | 87.85% | 89.74% | -2.10% | 1,572 |  |
| ER | 91.97% | 90.61% | +1.50% | 3,150 |  |
| CK | 91.16% | 89.80% | +1.52% | 1,743 |  |
| GN | 93.76% | 91.94% | +1.98% | 850 |  |

**Countries exceeding ±2.5% threshold:** GQ, KN

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 16.67% | 60.0% | -72.22% | 6 | ⚠️ |
| Apple Pay | 77.11% | 79.07% | -2.47% | 804 |  |
| Paypal | 92.83% | 93.24% | -0.45% | 1,715 |  |
| Credit Card | 92.72% | 91.71% | +1.10% | 6,715 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: GQ Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Others | 0.00% | 100.00% | -100.00% | 1 | 1 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 1 | 1 | 100.00% | 100.00% | +0.00 |

**Root Cause:** Others

---

## L2: KN Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 73.12% | 79.61% | -8.16% | 93 | 103 | ⚠️ |
| Credit Card | 93.48% | 96.60% | -3.24% | 276 | 265 |  |
| Paypal | 91.03% | 91.07% | -0.05% | 78 | 56 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 415 | 405 | 92.84% | 95.52% | -2.68 |
| Expired, Invalid, Closed Card, No Account | 16 | 10 | 3.58% | 2.36% | +1.22 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 8 | 4 | 1.79% | 0.94% | +0.85 |
| PayPal Declined, Revoked, Payer Issue | 6 | 4 | 1.34% | 0.94% | +0.40 |
| Call Issuer, Voice Auth Required | 2 | 1 | 0.45% | 0.24% | +0.21 |

**Root Cause:** Apple + Others

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 2,674 | 3,150 | +17.8% | Stable |
| CK | Medium (>85%) | 2,235 | 1,743 | -22.0% | ⚠️ Volume drop |
| CG | High (>92%) | 1,207 | 1,349 | +11.8% | Stable |
| MR | Medium (>85%) | 877 | 1,572 | +79.2% | Stable |
| GN | Medium (>85%) | 670 | 850 | +26.9% | Stable |
| KN | Medium (>85%) | 424 | 447 | +5.4% | Stable |
| AO | High (>92%) | 234 | 128 | -45.3% | ⚠️ Major mix shift |
| GQ | High (>92%) | 1 | 1 | +0.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| GQ | ↓ -100.00% | Others -100.0% | → Stable | → Stable | Others |
| KN | ↓ -3.19% | Apple Pay -8.2% | → Stable | Others -2.68pp | Apple + Others |

---

*Report: 2026-06-09*
