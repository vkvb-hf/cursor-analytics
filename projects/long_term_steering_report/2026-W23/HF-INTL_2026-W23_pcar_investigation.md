# PCAR Investigation: HF-INTL 2026-W23

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 94.47% → 95.04% (+0.60%)  
**Volume:** 31,799 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate for HF-INTL improved modestly from 94.47% to 95.04% (+0.60%) in 2026-W23, though this change is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Recovering from W18 dip, but below W16-W17 peak (97%+) | +0.60% | ⚠️ |
| L1: Country Scan | 1 country (AT) exceeded ±2.5% threshold | +4.79% in AT | ⚠️ |
| L1: Dimension Scan | All payment methods stable, no flags | <2.5% changes | ✅ |
| L2: AT Deep-Dive | Paypal +10.20%, Braintree +6.92% | Positive improvement | ✅ |
| Mix Shift | All countries stable, no adverse volume shifts | No impact | ✅ |

**Key Findings:**
- AT showed the largest improvement at +4.79%, driven by Paypal approval rates jumping from 90.74% to 100.00% (+10.20pp) on 107 orders
- Braintree provider in AT improved significantly from 92.70% to 99.12% (+6.42pp) across 226 orders
- PayPal-related decline reasons in AT dropped from 7 occurrences (1.88%) to 0, indicating resolved payer issues
- Overall rate remains ~2pp below the W16 peak of 97.13%, suggesting gradual recovery is still in progress
- Volume increased 13.0% WoW (28,130 → 31,799), with GB (+22.5%) and BE (+33.9%) showing strong growth

**Action:** Monitor — The improvement is positive but not statistically significant. Continue tracking AT performance to confirm Paypal/Braintree gains are sustained, and monitor overall trend recovery toward the 97%+ baseline from W16-W17.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W23 | 95.04% | 31,799 | +0.60% ← REPORTED CHANGE |
| 2026-W22 | 94.47% | 28,130 | +0.80% |
| 2026-W21 | 93.72% | 28,206 | +0.24% |
| 2026-W20 | 93.5% | 31,674 | +0.59% |
| 2026-W19 | 92.95% | 33,686 | -1.31% |
| 2026-W18 | 94.18% | 34,181 | -2.58% |
| 2026-W17 | 96.67% | 34,080 | -0.47% |
| 2026-W16 | 97.13% | 37,314 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| LU | 96.15% | 97.59% | -1.47% | 104 |  |
| GB | 98.53% | 98.27% | +0.26% | 8,072 |  |
| NL | 92.27% | 91.00% | +1.40% | 1,605 |  |
| DE | 89.81% | 88.18% | +1.84% | 6,328 |  |
| AT | 98.89% | 94.37% | +4.79% | 361 | ⚠️ |

**Countries exceeding ±2.5% threshold:** AT

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Credit Card | 98.19% | 98.14% | +0.05% | 11,536 |  |
| Apple Pay | 98.02% | 97.6% | +0.43% | 10,600 |  |
| Paypal | 98.14% | 97.42% | +0.74% | 5,645 |  |
| Others | 73.77% | 72.09% | +2.33% | 4,018 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: AT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| CreditCard | 98.52% | 97.14% | +1.42% | 135 | 140 |  |
| ApplePay | 98.32% | 94.40% | +4.15% | 119 | 125 |  |
| Paypal | 100.00% | 90.74% | +10.20% | 107 | 108 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| ProcessOut | 98.52% | 97.14% | +1.42% | 135 | 140 |  |
| Braintree | 99.12% | 92.70% | +6.92% | 226 | 233 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 359 | 363 | 99.45% | 97.32% | +2.13 |
| PayPal Declined, Revoked, Payer Issue | 0 | 7 | 0.00% | 1.88% | -1.88 |
| Fraud, Lost/Stolen Card, Security | 1 | 3 | 0.28% | 0.80% | -0.53 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 1 | 0 | 0.28% | 0.00% | +0.28 |

**Root Cause:** Paypal + Braintree + Others

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | High (>92%) | 6,590 | 8,072 | +22.5% | Stable |
| DE | Medium (>85%) | 5,711 | 6,328 | +10.8% | Stable |
| FR | High (>92%) | 5,681 | 6,805 | +19.8% | Stable |
| AU | High (>92%) | 2,799 | 2,655 | -5.1% | Stable |
| NL | Medium (>85%) | 1,344 | 1,605 | +19.4% | Stable |
| BE | Low (>85%) | 1,205 | 1,613 | +33.9% | Stable |
| IE | High (>92%) | 1,039 | 1,107 | +6.5% | Stable |
| DK | High (>92%) | 963 | 915 | -5.0% | Stable |
| SE | Medium (>85%) | 876 | 758 | -13.5% | Stable |
| NZ | High (>92%) | 755 | 826 | +9.4% | Stable |
| NO | High (>92%) | 585 | 521 | -10.9% | Stable |
| AT | High (>92%) | 373 | 361 | -3.2% | Stable |
| CH | Medium (>85%) | 126 | 129 | +2.4% | Stable |
| LU | High (>92%) | 83 | 104 | +25.3% | Stable |
| ES | Low (>85%) | 0 | 0 | +0.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| AT | ↑ +4.79% | Paypal +10.2% | Braintree +6.9% | Others +2.13pp | Paypal + Braintree + Others |

---

*Report: 2026-06-09*
