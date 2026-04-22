# PCAR Investigation: HF-INTL 2026-W15

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 96.12% → 97.13% (+1.05%)  
**Volume:** 37,314 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate for HF-INTL improved significantly in 2026-W15, increasing from 96.12% to 97.13% (+1.01 pp) on 37,314 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate recovering from W13 dip (95.21%) | +1.01 pp | ✅ |
| L1: Country Breakdown | SE +4.23 pp, CH +5.51 pp exceed threshold | 2 flagged | ⚠️ |
| L1: Payment Method | All methods stable (within ±2.5%) | Max +1.83 pp | ✅ |
| L2: SE Deep-Dive | Klarna +9.53 pp, Adyen +9.53 pp | Improvement | ✅ |
| L2: CH Deep-Dive | ApplePay +7.64 pp, Braintree +8.58 pp | Improvement | ✅ |
| Mix Shift | All countries stable impact | No negative shifts | ✅ |

**Key Findings:**
- SE showed the largest improvement driven by Klarna (+9.53 pp to 85.36%) and Adyen (+9.53 pp to 85.36%), with volume increasing +60.3% WoW
- CH improved +5.51 pp, led by ApplePay (+7.64 pp) and Braintree (+8.58 pp), though on low volume (135 orders)
- IE was the only country showing decline (-0.71 pp to 97.89%), but remains within acceptable range and at high absolute performance
- NO experienced significant volume growth (+148.2%) while maintaining stable approval rates
- All flagged changes represent positive improvements rather than degradation

**Action:** Monitor — The +1.01 pp improvement is a positive recovery trend. Continue monitoring SE and CH to ensure Klarna/Adyen and ApplePay/Braintree improvements sustain at scale.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 97.13% | 37,314 | +1.05% |
| 2026-W15 | 96.12% | 36,514 | +0.13% ← REPORTED CHANGE |
| 2026-W14 | 96.0% | 31,465 | +0.83% |
| 2026-W13 | 95.21% | 39,598 | -1.52% |
| 2026-W12 | 96.68% | 38,136 | -0.53% |
| 2026-W11 | 97.2% | 42,932 | -0.11% |
| 2026-W10 | 97.31% | 44,946 | +0.80% |
| 2026-W09 | 96.54% | 48,662 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| IE | 97.89% | 98.60% | -0.71% | 1,282 |  |
| BE | 90.29% | 89.26% | +1.15% | 1,081 |  |
| LU | 100.00% | 98.36% | +1.67% | 63 |  |
| NL | 90.44% | 88.46% | +2.24% | 1,580 |  |
| SE | 91.93% | 88.20% | +4.23% | 1,412 | ⚠️ |
| CH | 95.56% | 90.57% | +5.51% | 135 | ⚠️ |

**Countries exceeding ±2.5% threshold:** SE, CH

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Apple Pay | 98.03% | 98.16% | -0.13% | 12,006 |  |
| Credit Card | 98.22% | 98.2% | +0.03% | 13,439 |  |
| Paypal | 97.96% | 97.76% | +0.20% | 7,741 |  |
| Others | 76.47% | 75.1% | +1.83% | 3,328 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: SE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| CreditCard | 97.64% | 98.71% | -1.08% | 381 | 232 |  |
| ApplePay | 98.78% | 98.47% | +0.32% | 329 | 196 |  |
| Paypal | 94.74% | 88.89% | +6.58% | 19 | 18 | ⚠️ |
| Klarna | 85.36% | 77.93% | +9.53% | 683 | 435 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| ProcessOut | 97.64% | 98.71% | -1.08% | 381 | 232 |  |
| Braintree | 98.56% | 97.66% | +0.92% | 348 | 214 |  |
| Adyen | 85.36% | 77.93% | +9.53% | 683 | 435 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Policy, Lifecycle, Revocation, Limit Exceeded | 8 | 1 | 0.57% | 0.11% | +0.45 |
| PayPal Declined, Revoked, Payer Issue | 0 | 2 | 0.00% | 0.23% | -0.23 |
| Others | 1,404 | 878 | 99.43% | 99.66% | -0.23 |

**Root Cause:** Paypal + Adyen

---

## L2: CH Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| CreditCard | 95.45% | 92.19% | +3.54% | 66 | 64 |  |
| ApplePay | 93.75% | 87.10% | +7.64% | 48 | 31 | ⚠️ |
| Paypal | 100.00% | 90.91% | +10.00% | 21 | 11 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| ProcessOut | 95.45% | 92.19% | +3.54% | 66 | 64 |  |
| Braintree | 95.65% | 88.10% | +8.58% | 69 | 42 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 134 | 101 | 99.26% | 95.28% | +3.98 |
| Fraud, Lost/Stolen Card, Security | 0 | 2 | 0.00% | 1.89% | -1.89 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 1 | 2 | 0.74% | 1.89% | -1.15 |
| PayPal Declined, Revoked, Payer Issue | 0 | 1 | 0.00% | 0.94% | -0.94 |

**Root Cause:** ApplePay + Braintree + Others

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FR | High (>92%) | 8,159 | 7,408 | -9.2% | Stable |
| GB | High (>92%) | 6,795 | 8,125 | +19.6% | Stable |
| DE | High (>92%) | 6,652 | 8,608 | +29.4% | Stable |
| AU | High (>92%) | 2,464 | 2,828 | +14.8% | Stable |
| NL | Medium (>85%) | 1,629 | 1,580 | -3.0% | Stable |
| IE | High (>92%) | 1,069 | 1,282 | +19.9% | Stable |
| BE | Medium (>85%) | 1,043 | 1,081 | +3.6% | Stable |
| DK | High (>92%) | 966 | 1,457 | +50.8% | Stable |
| SE | Medium (>85%) | 881 | 1,412 | +60.3% | Stable |
| NZ | High (>92%) | 658 | 806 | +22.5% | Stable |
| AT | High (>92%) | 567 | 699 | +23.3% | Stable |
| NO | High (>92%) | 415 | 1,030 | +148.2% | Stable |
| CH | Medium (>85%) | 106 | 135 | +27.4% | Stable |
| LU | High (>92%) | 61 | 63 | +3.3% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| SE | ↑ +4.23% | Paypal +6.6% | Adyen +9.5% | → Stable | Paypal + Adyen |
| CH | ↑ +5.51% | ApplePay +7.6% | Braintree +8.6% | Others +3.98pp | ApplePay + Braintree + Others |

---

*Report: 2026-04-22*
