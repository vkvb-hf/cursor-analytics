# PCAR Investigation: RTE 2026-W15

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 97.22% → 97.2% (-0.02%)  
**Volume:** 44,111 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate remained stable at 97.2%, declining marginally by -0.02pp from 97.22% in W15, with the change classified as not statistically significant across 44,111 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Stable trend (96.88%-97.30% range) | -0.02pp | ✅ |
| L1: Country Breakdown | TT -4.17pp, TZ +3.28pp exceed ±2.5% threshold | Mixed | ⚠️ |
| L1: PaymentMethod | Others -4.35pp flagged | -4.35pp | ⚠️ |
| L2: TT Deep-Dive | Klarna -5.21pp, IDeal -5.10pp | -5.21pp | ⚠️ |
| L2: TZ Deep-Dive | CreditCard +7.79pp, Adyen +7.79pp (improvement) | +7.79pp | ✅ |
| Mix Shift | TO volume -21.0%, all others stable | Minor | ✅ |

**Key Findings:**
- TT declined -4.17pp (74.62% vs 77.86%) driven by Klarna (-5.21pp) and IDeal (-5.10pp) payment methods processed through Adyen (-4.29pp)
- TZ improved +3.28pp (97.10% vs 94.01%) with CreditCard via Adyen showing +7.79pp recovery
- "Others" payment method globally declined -4.35pp but represents low volume (950 orders)
- TO experienced significant volume drop (-21.0%) but maintains high approval rate (98.03%)
- Overall metric stability maintained despite localized fluctuations, with offsetting positive/negative country movements

**Action:** Monitor – The -0.02pp change is not statistically significant. Continue monitoring TT/Klarna performance for sustained degradation patterns; no immediate escalation required.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 97.2% | 44,111 | -0.02% |
| 2026-W15 | 97.22% | 44,168 | +0.33% ← REPORTED CHANGE |
| 2026-W14 | 96.9% | 39,914 | +0.01% |
| 2026-W13 | 96.89% | 42,897 | +0.01% |
| 2026-W12 | 96.88% | 44,209 | -0.11% |
| 2026-W11 | 96.99% | 47,403 | +0.10% |
| 2026-W10 | 96.89% | 48,399 | -0.42% |
| 2026-W09 | 97.3% | 50,858 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TT | 74.62% | 77.86% | -4.17% | 788 | ⚠️ |
| FJ | 97.73% | 97.43% | +0.31% | 30,930 |  |
| YE | 97.37% | 96.63% | +0.77% | 3,655 |  |
| TK | 98.58% | 97.78% | +0.82% | 423 |  |
| TO | 98.03% | 97.08% | +0.98% | 406 |  |
| TZ | 97.10% | 94.01% | +3.28% | 551 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TT, TZ

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | 71.58% | 74.83% | -4.35% | 950 | ⚠️ |
| Credit Card | 97.86% | 97.58% | +0.29% | 27,463 |  |
| Paypal | 98.58% | 98.14% | +0.45% | 5,081 |  |
| Apple Pay | 97.21% | 96.65% | +0.58% | 10,674 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: TT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Klarna | 54.17% | 57.14% | -5.21% | 96 | 77 | ⚠️ |
| IDeal | 73.41% | 77.36% | -5.10% | 583 | 614 | ⚠️ |
| ApplePay | 100.00% | 100.00% | +0.00% | 37 | 45 |  |
| Paypal | 100.00% | 100.00% | +0.00% | 13 | 11 |  |
| CreditCard | 98.31% | 94.87% | +3.62% | 59 | 39 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Adyen | 72.90% | 76.16% | -4.29% | 738 | 730 |  |
| Braintree | 100.00% | 100.00% | +0.00% | 50 | 56 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Fraud, Lost/Stolen Card, Security | 3 | 5 | 0.38% | 0.64% | -0.26 |
| Others | 785 | 781 | 99.62% | 99.36% | +0.26 |

**Root Cause:** Klarna

---

## L2: TZ Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Paypal | 96.76% | 95.81% | +1.00% | 278 | 310 |  |
| ApplePay | 97.96% | 93.57% | +4.69% | 147 | 140 |  |
| CreditCard | 96.83% | 89.83% | +7.79% | 126 | 118 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Braintree | 97.18% | 95.11% | +2.17% | 425 | 450 |  |
| Adyen | 96.83% | 89.83% | +7.79% | 126 | 118 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 548 | 561 | 99.46% | 98.77% | +0.69 |
| CVV/CVC Mismatch | 0 | 3 | 0.00% | 0.53% | -0.53 |
| 3DS Authentication Failed/Required | 0 | 2 | 0.00% | 0.35% | -0.35 |
| PayPal Declined, Revoked, Payer Issue | 2 | 1 | 0.36% | 0.18% | +0.19 |
| Fraud, Lost/Stolen Card, Security | 1 | 0 | 0.18% | 0.00% | +0.18 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 0 | 1 | 0.00% | 0.18% | -0.18 |

**Root Cause:** CreditCard + Adyen

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 28,555 | 30,930 | +8.3% | Stable |
| CF | High (>92%) | 5,813 | 6,939 | +19.4% | Stable |
| YE | High (>92%) | 3,000 | 3,655 | +21.8% | Stable |
| TT | Low (>85%) | 786 | 788 | +0.3% | Stable |
| TZ | High (>92%) | 568 | 551 | -3.0% | Stable |
| TO | High (>92%) | 514 | 406 | -21.0% | ⚠️ Volume drop |
| TV | Low (>85%) | 363 | 476 | +31.1% | Stable |
| TK | High (>92%) | 315 | 423 | +34.3% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TT | ↓ -4.17% | Klarna -5.2% | → Stable | → Stable | Klarna |
| TZ | ↑ +3.28% | CreditCard +7.8% | Adyen +7.8% | → Stable | CreditCard + Adyen |

---

*Report: 2026-04-22*
