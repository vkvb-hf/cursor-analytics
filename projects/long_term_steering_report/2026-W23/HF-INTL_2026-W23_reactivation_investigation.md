# Reactivation Investigation: HF-INTL 2026-W23

**Metric:** Reactivation Rate  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 91.07% → 90.7% (-0.41%)  
**Volume:** 42,141 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Reactivation Rate for HF-INTL declined slightly from 91.07% to 90.7% (-0.37pp) in W23, a change that is not statistically significant given the volume of 42,141 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (89.55%-91.23%) | -0.37pp | ✅ |
| L1: Country Scan | 2 countries exceed ±2.5% threshold | LU -9.93%, CH +6.06% | ⚠️ |
| L1: Dimension Scan | No payment methods exceed threshold | Max Δ -1.13% (Others) | ✅ |
| L2: LU Deep-Dive | Credit Card decline, low volume | -17.65% on 17 orders | ⚠️ |
| L2: CH Deep-Dive | Net improvement driven by Credit Card | +11.34% on 27 orders | ✅ |
| Mix Shift | SE volume drop -37.8%, others stable | No material AR impact | ✅ |

**Key Findings:**
- LU experienced a -9.93pp drop in reactivation rate, driven primarily by Credit Card transactions declining from 100% to 82.35%, with "Others" decline reasons increasing by 7.23pp
- CH showed a +6.06pp improvement, with Credit Card performance improving +11.34pp (offsetting Apple Pay's -14.29% decline), resulting in a net positive for the overall metric
- Both flagged countries (LU: 39 orders, CH: 44 orders) have extremely low volumes, limiting their impact on the overall HF-INTL rate
- SE experienced a significant volume drop of -37.8% (1,516 → 943 orders) but maintained stable AR performance
- The 8-week trend shows the rate remains within its historical band of 89.55%-91.23%, indicating normal fluctuation

**Action:** Monitor — The overall decline is not statistically significant and is driven by low-volume country fluctuations. Continue standard monitoring; no escalation required unless LU or CH patterns persist in W24.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W23 | 90.7% | 42,141 | -0.41% ← REPORTED CHANGE |
| 2026-W22 | 91.07% | 36,789 | +0.54% |
| 2026-W21 | 90.58% | 33,970 | +1.15% |
| 2026-W20 | 89.55% | 36,895 | -0.85% |
| 2026-W19 | 90.32% | 40,935 | - |
| 2026-W18 | 90.32% | 43,663 | -0.46% |
| 2026-W17 | 90.74% | 40,613 | -0.54% |
| 2026-W16 | 91.23% | 46,003 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| LU | 84.62% | 93.94% | -9.93% | 39 | ⚠️ |
| IE | 84.14% | 85.98% | -2.13% | 637 |  |
| BE | 91.45% | 92.98% | -1.65% | 2,046 |  |
| GB | 89.63% | 90.67% | -1.16% | 14,113 |  |
| AU | 86.06% | 86.98% | -1.06% | 3,788 |  |
| FR | 88.66% | 89.01% | -0.39% | 7,839 |  |
| DK | 93.17% | 91.41% | +1.92% | 1,420 |  |
| CH | 95.45% | 90.00% | +6.06% | 44 | ⚠️ |

**Countries exceeding ±2.5% threshold:** LU, CH

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 96.64% | 97.75% | -1.13% | 3,635 |  |
| Apple Pay | 91.65% | 92.48% | -0.89% | 7,233 |  |
| Credit Card | 86.01% | 86.36% | -0.40% | 20,031 |  |
| Paypal | 96.51% | 96.43% | +0.08% | 11,242 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: LU Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Others | 60.00% | 0.00% | +0.00% | 5 | 0 |  |
| Credit Card | 82.35% | 100.00% | -17.65% | 17 | 18 | ⚠️ |
| Paypal | 100.00% | 100.00% | +0.00% | 10 | 6 |  |
| Apple Pay | 85.71% | 77.78% | +10.20% | 7 | 9 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 35 | 32 | 89.74% | 96.97% | -7.23 |
| Expired, Invalid, Closed Card, No Account | 3 | 1 | 7.69% | 3.03% | +4.66 |
| Call Issuer, Voice Auth Required | 1 | 0 | 2.56% | 0.00% | +2.56 |

**Root Cause:** Credit + Others

---

## L2: CH Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 85.71% | 100.00% | -14.29% | 7 | 4 | ⚠️ |
| Others | 100.00% | 100.00% | +0.00% | 1 | 2 |  |
| Paypal | 100.00% | 100.00% | +0.00% | 9 | 7 |  |
| Credit Card | 96.30% | 86.49% | +11.34% | 27 | 37 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Expired, Invalid, Closed Card, No Account | 0 | 1 | 0.00% | 2.00% | -2.00 |
| Others | 44 | 49 | 100.00% | 98.00% | +2.00 |

**Root Cause:** Apple + Expired,

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | Medium (>85%) | 11,560 | 14,113 | +22.1% | Stable |
| DE | High (>92%) | 5,655 | 6,439 | +13.9% | Stable |
| FR | Medium (>85%) | 5,177 | 7,839 | +51.4% | Stable |
| AU | Medium (>85%) | 4,617 | 3,788 | -18.0% | Stable |
| NL | High (>92%) | 2,361 | 2,512 | +6.4% | Stable |
| SE | Medium (>85%) | 1,516 | 943 | -37.8% | ⚠️ Volume drop |
| BE | High (>92%) | 1,496 | 2,046 | +36.8% | Stable |
| NZ | Low (>85%) | 1,432 | 1,430 | -0.1% | Stable |
| DK | Medium (>85%) | 1,246 | 1,420 | +14.0% | Stable |
| NO | Low (>85%) | 664 | 575 | -13.4% | Stable |
| IE | Medium (>85%) | 656 | 637 | -2.9% | Stable |
| AT | High (>92%) | 326 | 316 | -3.1% | Stable |
| CH | Medium (>85%) | 50 | 44 | -12.0% | Stable |
| LU | High (>92%) | 33 | 39 | +18.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| LU | ↓ -9.93% | Credit Card -17.6% | → Stable | Others -7.23pp | Credit + Others |
| CH | ↑ +6.06% | Apple Pay -14.3% | → Stable | Expired, Invalid, Closed Card, No Account -2.00pp | Apple + Expired, |

---

*Report: 2026-06-09*
