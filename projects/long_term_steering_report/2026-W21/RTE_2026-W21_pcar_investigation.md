# PCAR Investigation: RTE 2026-W21

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 96.49% → 97.25% (+0.79%)  
**Volume:** 35,603 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate improved from 96.49% to 97.25% (+0.76pp) in W21, a positive but statistically not significant change within normal weekly fluctuation range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (96.5%-97.25%) | +0.76pp | ✅ |
| L1: Country Scan | TO flagged with -6.65pp decline | 1 of 6 countries | ⚠️ |
| L1: Dimension Scan | No payment methods exceeding threshold | All within ±2.5% | ✅ |
| L2: TO Deep-Dive | Adyen provider down -8.90pp | Root cause identified | ⚠️ |
| Mix Shift | TT volume dropped -39.1%, TZ dropped -24.4% | Low-AR country volume decline | ✅ |

**Key Findings:**
- TO experienced a significant approval rate decline of -6.65pp (92.80% → 86.63%), driven by Adyen provider performance dropping -8.90pp
- In TO, CreditCard volume decreased sharply from 233 to 68 orders (-70.8%) while BcmcMobile volume surged from 3 to 196 orders, shifting payment mix toward a lower-performing method
- Overall RTE improvement partially attributed to volume decline in low-AR countries: TT volume dropped -39.1% (949 → 578) and TZ dropped -24.4% (491 → 371)
- Decline reasons in TO shifted to 100% "Others" category, with 3DS Authentication failures eliminated (1.49pp → 0%)
- Overall volume declined -8.4% (38,879 → 35,603) across most countries, consistent with downward volume trend observed since W17

**Action:** Monitor - Overall metric improved and change is not statistically significant. Continue monitoring TO/Adyen performance for sustained degradation; escalate if TO decline persists beyond W22 or Adyen issues spread to other markets.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W21 | 97.25% | 35,603 | +0.79% ← REPORTED CHANGE |
| 2026-W20 | 96.49% | 38,879 | -0.18% |
| 2026-W19 | 96.66% | 38,661 | +0.15% |
| 2026-W18 | 96.52% | 40,203 | -0.55% |
| 2026-W17 | 97.05% | 42,589 | -0.15% |
| 2026-W16 | 97.2% | 44,111 | -0.02% |
| 2026-W15 | 97.22% | 44,168 | +0.33% |
| 2026-W14 | 96.9% | 39,914 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TO | 86.63% | 92.80% | -6.65% | 374 | ⚠️ |
| YE | 97.19% | 96.80% | +0.40% | 3,092 |  |
| FJ | 97.73% | 97.19% | +0.55% | 25,459 |  |
| TT | 80.80% | 80.30% | +0.62% | 578 |  |
| CF | 98.19% | 96.42% | +1.84% | 5,150 |  |
| TV | 86.39% | 84.50% | +2.24% | 316 |  |

**Countries exceeding ±2.5% threshold:** TO

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Apple Pay | 97.26% | 97.19% | +0.07% | 8,784 |  |
| Paypal | 97.97% | 97.84% | +0.13% | 4,089 |  |
| Credit Card | 97.88% | 96.8% | +1.12% | 21,856 |  |
| Others | 77.92% | 76.59% | +1.73% | 874 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: TO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Paypal | 100.00% | 98.63% | +1.39% | 48 | 73 |  |
| ApplePay | 100.00% | 97.87% | +2.17% | 62 | 94 |  |
| CreditCard | 98.53% | 89.70% | +9.84% | 68 | 233 | ⚠️ |
| BcmcMobile | 75.00% | 33.33% | +125.00% | 196 | 3 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Adyen | 81.06% | 88.98% | -8.90% | 264 | 236 | ⚠️ |
| Braintree | 100.00% | 98.20% | +1.83% | 110 | 167 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 374 | 396 | 100.00% | 98.26% | +1.74 |
| 3DS Authentication Failed/Required | 0 | 6 | 0.00% | 1.49% | -1.49 |
| Fraud, Lost/Stolen Card, Security | 0 | 1 | 0.00% | 0.25% | -0.25 |

**Root Cause:** CreditCard + Adyen + Others

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 27,653 | 25,459 | -7.9% | Stable |
| CF | High (>92%) | 5,525 | 5,150 | -6.8% | Stable |
| YE | High (>92%) | 3,220 | 3,092 | -4.0% | Stable |
| TT | Low (>85%) | 949 | 578 | -39.1% | ⚠️ Volume drop |
| TZ | High (>92%) | 491 | 371 | -24.4% | ⚠️ Volume drop |
| TO | High (>92%) | 403 | 374 | -7.2% | Stable |
| TV | Low (>85%) | 329 | 316 | -4.0% | Stable |
| TK | High (>92%) | 309 | 263 | -14.9% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TO | ↓ -6.65% | CreditCard +9.8% | Adyen -8.9% | Others +1.74pp | CreditCard + Adyen + Others |

---

*Report: 2026-05-26*
