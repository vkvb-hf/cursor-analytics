# PCAR Investigation: RTE 2026-W23

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 97.0% → 97.11% (+0.11%)  
**Volume:** 36,387 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate improved slightly from 97.0% to 97.11% (+0.11pp) in W23, a change that is not statistically significant, with the metric remaining stable within its 8-week historical range of 96.49%-97.25%.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall RTE Trend | Within normal range (96.49%-97.25%) | +0.11pp | ✅ |
| L1: Country Breakdown | TT exceeded ±2.5% threshold | -3.23pp | ⚠️ |
| L1: PaymentMethod | No methods exceeded threshold | - | ✅ |
| L2: TT Deep-Dive | Paypal and Klarna flagged | -20.0pp, -14.01pp | ⚠️ |
| Mix Shift | TV volume dropped 29.0% | - | ⚠️ |

**Key Findings:**
- TT showed the largest country-level decline at -3.23pp (78.85% vs 81.48%), driven primarily by Paypal dropping from 100% to 80% (5 orders) and Klarna declining from 69.05% to 59.38% (64 orders)
- Decline reasons in TT shifted with "Fraud, Lost/Stolen Card, Security" appearing for 7 transactions (1.12% of declines) where previously there were none
- TV experienced a significant volume drop of -29.0% (451 → 320 orders) while also declining -2.40pp in approval rate
- FJ, the highest volume country (26,504 orders, 73% of total), remained stable with a +0.29pp improvement
- Overall volume decreased across the 8-week period from 44,111 (W16) to 36,387 (W23)

**Action:** Monitor - The overall metric change is not significant and TT represents low volume (624 orders, <2% of total). Continue monitoring TT's Paypal and Klarna performance, and track whether the new fraud-related declines persist.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W23 | 97.11% | 36,387 | +0.11% ← REPORTED CHANGE |
| 2026-W22 | 97.0% | 35,018 | -0.26% |
| 2026-W21 | 97.25% | 35,603 | +0.79% |
| 2026-W20 | 96.49% | 38,879 | -0.18% |
| 2026-W19 | 96.66% | 38,661 | +0.15% |
| 2026-W18 | 96.52% | 40,203 | -0.55% |
| 2026-W17 | 97.05% | 42,589 | -0.15% |
| 2026-W16 | 97.2% | 44,111 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TT | 78.85% | 81.48% | -3.23% | 624 | ⚠️ |
| TV | 80.94% | 82.93% | -2.40% | 320 |  |
| TZ | 95.98% | 97.97% | -2.03% | 398 |  |
| TO | 86.50% | 87.68% | -1.34% | 400 |  |
| YE | 97.24% | 97.71% | -0.49% | 3,005 |  |
| FJ | 97.68% | 97.40% | +0.29% | 26,504 |  |

**Countries exceeding ±2.5% threshold:** TT

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | 75.31% | 75.91% | -0.79% | 980 |  |
| Paypal | 97.99% | 98.15% | -0.16% | 4,021 |  |
| Credit Card | 97.91% | 97.85% | +0.06% | 22,816 |  |
| Apple Pay | 97.04% | 96.61% | +0.45% | 8,570 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: TT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Paypal | 80.00% | 100.00% | -20.00% | 5 | 7 | ⚠️ |
| Klarna | 59.38% | 69.05% | -14.01% | 64 | 42 | ⚠️ |
| ApplePay | 97.83% | 100.00% | -2.17% | 46 | 47 |  |
| IDeal | 77.87% | 78.65% | -0.99% | 470 | 431 |  |
| CreditCard | 100.00% | 100.00% | +0.00% | 39 | 40 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Braintree | 96.08% | 100.00% | -3.92% | 51 | 54 |  |
| Adyen | 77.31% | 79.53% | -2.79% | 573 | 513 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 616 | 567 | 98.72% | 100.00% | -1.28 |
| Fraud, Lost/Stolen Card, Security | 7 | 0 | 1.12% | 0.00% | +1.12 |
| PayPal Declined, Revoked, Payer Issue | 1 | 0 | 0.16% | 0.00% | +0.16 |

**Root Cause:** Paypal + Others

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 24,878 | 26,504 | +6.5% | Stable |
| CF | High (>92%) | 5,010 | 4,869 | -2.8% | Stable |
| YE | High (>92%) | 3,060 | 3,005 | -1.8% | Stable |
| TT | Low (>85%) | 567 | 624 | +10.1% | Stable |
| TV | Low (>85%) | 451 | 320 | -29.0% | ⚠️ Volume drop |
| TZ | High (>92%) | 394 | 398 | +1.0% | Stable |
| TO | Medium (>85%) | 357 | 400 | +12.0% | Stable |
| TK | High (>92%) | 301 | 267 | -11.3% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TT | ↓ -3.23% | Paypal -20.0% | → Stable | Others -1.28pp | Paypal + Others |

---

*Report: 2026-06-09*
