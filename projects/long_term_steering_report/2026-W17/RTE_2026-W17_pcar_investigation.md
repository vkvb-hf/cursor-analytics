# PCAR Investigation: RTE 2026-W17

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 97.2% → 96.76% (-0.45%)  
**Volume:** 42,588 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate declined from 97.2% to 96.76% (-0.44pp) in W17, a statistically not significant change across 42,588 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (96.76-97.22%) | -0.44pp | ✅ |
| L1: Country Scan | 3 countries exceed ±2.5% threshold | TT -18.17%, TV -10.47%, TZ -2.60% | ⚠️ |
| L1: Dimension Scan | PaymentMethod "Others" flagged | -20.71% | ⚠️ |
| L2: TT Deep-Dive | IDeal + Adyen identified | IDeal -23.26%, Adyen -20.25% | ⚠️ |
| L2: TV Deep-Dive | Klarna + Adyen identified | Klarna -18.28%, Adyen -13.14% | ⚠️ |
| L2: TZ Deep-Dive | No clear root cause | CreditCard -4.98%, ApplePay -3.17% | ⚠️ |
| Mix Shift | TT volume dropped significantly | -39.1% volume | ⚠️ |

**Key Findings:**
- TT experienced the largest AR drop (-18.17pp), driven by IDeal payments via Adyen (IDeal -23.26%, Adyen -20.25%), with volume also declining 39.1%
- TV showed significant degradation (-10.47pp) attributed to Klarna + Adyen combination (Klarna -18.28%, Adyen -13.14%)
- TZ decline (-2.60pp) lacks a clear root cause; CreditCard and ApplePay both declined moderately but no single dimension exceeded threshold
- Decline reasons remain stable across all flagged countries ("Others" category dominates at 99%+), suggesting provider-side issues rather than fraud or authentication failures
- Overall impact is contained due to low volumes in affected countries (TT: 745, TV: 388, TZ: 496 orders combined = 3.8% of total)

**Action:** Monitor - The overall change is not statistically significant and concentrated in low-volume markets. Continue monitoring Adyen performance in TT and TV for potential provider-side issues with IDeal and Klarna integrations.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 96.76% | 42,588 | -0.45% ← REPORTED CHANGE |
| 2026-W16 | 97.2% | 44,111 | -0.02% |
| 2026-W15 | 97.22% | 44,168 | +0.33% |
| 2026-W14 | 96.9% | 39,914 | +0.01% |
| 2026-W13 | 96.89% | 42,897 | +0.01% |
| 2026-W12 | 96.88% | 44,209 | -0.11% |
| 2026-W11 | 96.99% | 47,403 | +0.10% |
| 2026-W10 | 96.89% | 48,399 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TT | 65.91% | 80.54% | -18.17% | 745 | ⚠️ |
| TV | 76.29% | 85.21% | -10.47% | 388 | ⚠️ |
| TZ | 95.56% | 98.12% | -2.60% | 496 | ⚠️ |
| TK | 98.92% | 100.00% | -1.08% | 277 |  |
| CF | 98.04% | 98.61% | -0.57% | 5,928 |  |
| FJ | 97.45% | 97.69% | -0.25% | 30,705 |  |

**Countries exceeding ±2.5% threshold:** TT, TV, TZ

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | 61.69% | 77.8% | -20.71% | 877 | ⚠️ |
| Apple Pay | 96.81% | 97.42% | -0.62% | 10,314 |  |
| Paypal | 97.97% | 98.31% | -0.34% | 5,126 |  |
| Credit Card | 97.68% | 97.87% | -0.19% | 26,271 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: TT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| IDeal | 62.67% | 81.67% | -23.26% | 576 | 1,009 | ⚠️ |
| CreditCard | 85.00% | 100.00% | -15.00% | 40 | 41 | ⚠️ |
| ApplePay | 100.00% | 98.28% | +1.75% | 36 | 58 |  |
| Paypal | 100.00% | 92.86% | +7.69% | 15 | 14 | ⚠️ |
| Klarna | 57.69% | 49.50% | +16.54% | 78 | 101 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Adyen | 63.40% | 79.50% | -20.25% | 694 | 1,151 | ⚠️ |
| Braintree | 100.00% | 97.22% | +2.86% | 51 | 72 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Fraud, Lost/Stolen Card, Security | 1 | 0 | 0.13% | 0.00% | +0.13 |
| PayPal Declined, Revoked, Payer Issue | 0 | 1 | 0.00% | 0.08% | -0.08 |
| Others | 744 | 1,222 | 99.87% | 99.92% | -0.05 |

**Root Cause:** IDeal + Adyen

---

## L2: TV Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Klarna | 59.63% | 72.97% | -18.28% | 218 | 222 | ⚠️ |
| Paypal | 83.33% | 100.00% | -16.67% | 6 | 10 | ⚠️ |
| CreditCard | 97.70% | 98.13% | -0.44% | 87 | 107 |  |
| ApplePay | 98.70% | 98.85% | -0.15% | 77 | 87 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Adyen | 70.49% | 81.16% | -13.14% | 305 | 329 | ⚠️ |
| Braintree | 97.59% | 98.97% | -1.39% | 83 | 97 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 386 | 425 | 99.48% | 99.77% | -0.28 |
| PayPal Declined, Revoked, Payer Issue | 1 | 0 | 0.26% | 0.00% | +0.26 |
| 3DS Authentication Failed/Required | 1 | 1 | 0.26% | 0.23% | +0.02 |

**Root Cause:** Klarna + Adyen

---

## L2: TZ Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| CreditCard | 93.10% | 97.99% | -4.98% | 116 | 149 |  |
| ApplePay | 94.21% | 97.30% | -3.17% | 121 | 148 |  |
| Paypal | 97.30% | 98.61% | -1.33% | 259 | 288 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Adyen | 93.10% | 97.99% | -4.98% | 116 | 149 |  |
| Braintree | 96.32% | 98.17% | -1.88% | 380 | 436 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 492 | 582 | 99.19% | 99.49% | -0.29 |
| CVV/CVC Mismatch | 2 | 1 | 0.40% | 0.17% | +0.23 |
| 3DS Authentication Failed/Required | 1 | 0 | 0.20% | 0.00% | +0.20 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 0 | 1 | 0.00% | 0.17% | -0.17 |
| PayPal Declined, Revoked, Payer Issue | 1 | 1 | 0.20% | 0.17% | +0.03 |

**Root Cause:** Requires investigation

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 30,779 | 30,705 | -0.2% | Stable |
| CF | High (>92%) | 6,546 | 5,928 | -9.4% | Stable |
| YE | High (>92%) | 3,713 | 3,649 | -1.7% | Stable |
| TT | Low (>85%) | 1,223 | 745 | -39.1% | ⚠️ Volume drop |
| TZ | High (>92%) | 585 | 496 | -15.2% | Stable |
| TO | High (>92%) | 499 | 400 | -19.8% | Stable |
| TV | Medium (>85%) | 426 | 388 | -8.9% | Stable |
| TK | High (>92%) | 340 | 277 | -18.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TT | ↓ -18.17% | IDeal -23.3% | Adyen -20.2% | → Stable | IDeal + Adyen |
| TV | ↓ -10.47% | Klarna -18.3% | Adyen -13.1% | → Stable | Klarna + Adyen |
| TZ | ↓ -2.60% | → Stable | → Stable | → Stable | Requires investigation |

---

*Report: 2026-04-27*
