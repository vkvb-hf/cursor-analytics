# PCAR Investigation: HF-INTL 2026-W18

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 96.67% → 94.18% (-2.58%)  
**Volume:** 34,181 orders  
**Significance:** Significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate for HF-INTL declined significantly from 96.67% to 94.18% (-2.49 pp) in W18, representing the largest week-over-week drop in the 8-week trend.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 8-Week Trend | Sustained decline or one-time drop? | -2.58% vs prior week | ⚠️ Sharp single-week drop, breaking stable trend |
| Country Impact | Any country >±2.5% threshold? | LU -8.57%, DK -5.01%, DE -4.65%, FR -4.06% | ⚠️ 4 countries flagged |
| Payment Method | Method-level degradation? | CreditCard -3.71%, Others -5.81% | ⚠️ Credit Card and Others declining |
| Provider Impact | Provider-specific issues? | ProcessOut and Adyen flagged across markets | ⚠️ Multi-provider degradation |
| Mix Shift | Volume redistribution impact? | All countries show "Stable" impact | ✅ No significant mix shift |

**Key Findings:**
- **FR shows highest volume impact:** CreditCard approval rate dropped -7.71% (90.59% from 98.15%) via ProcessOut provider, affecting 3,729 orders
- **DE experiencing Klarna/Adyen issues:** New payment method Klarna shows only 55.81% approval rate with 903 orders, processed through Adyen (55.86% approval)
- **DK Mobilepay expansion causing degradation:** Mobilepay volume surged from 3 to 231 orders but maintains low 74.89% approval rate via ProcessOut
- **LU small volume but severe drop:** CreditCard via ProcessOut dropped -50% (though only 2 orders), with Adyen also declining -17.86%
- **Decline reasons largely categorized as "Others":** Specific decline codes not providing actionable insight across most markets

**Action:** **Investigate** - Escalate to Payment Operations team to review ProcessOut performance in FR and DK, and Adyen configuration for Klarna in DE. Request detailed decline code breakdown for "Others" category.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W18 | 94.18% | 34,181 | -2.58% ← REPORTED CHANGE |
| 2026-W17 | 96.67% | 34,080 | -0.47% |
| 2026-W16 | 97.13% | 37,314 | +1.05% |
| 2026-W15 | 96.12% | 36,514 | +0.13% |
| 2026-W14 | 96.0% | 31,465 | +0.83% |
| 2026-W13 | 95.21% | 39,598 | -1.52% |
| 2026-W12 | 96.68% | 38,136 | -0.53% |
| 2026-W11 | 97.2% | 42,932 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| LU | 91.43% | 100.00% | -8.57% | 70 | ⚠️ |
| DK | 94.20% | 99.17% | -5.01% | 1,138 | ⚠️ |
| DE | 92.71% | 97.24% | -4.65% | 7,628 | ⚠️ |
| FR | 93.21% | 97.15% | -4.06% | 6,626 | ⚠️ |
| AU | 95.49% | 97.64% | -2.20% | 2,928 |  |
| GB | 97.54% | 98.36% | -0.83% | 8,662 |  |

**Countries exceeding ±2.5% threshold:** LU, DK, DE, FR

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | 76.6% | 81.32% | -5.81% | 3,868 | ⚠️ |
| Credit Card | 94.34% | 97.98% | -3.71% | 12,005 | ⚠️ |
| Apple Pay | 97.58% | 97.7% | -0.13% | 11,435 |  |
| Paypal | 98.11% | 97.73% | +0.39% | 6,873 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: LU Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Sepa | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| CreditCard | 80.00% | 100.00% | -20.00% | 30 | 28 | ⚠️ |
| ApplePay | 100.00% | 100.00% | +0.00% | 26 | 28 |  |
| Paypal | 100.00% | 100.00% | +0.00% | 14 | 6 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| ProcessOut | 50.00% | 100.00% | -50.00% | 2 | 1 | ⚠️ |
| Adyen | 82.14% | 100.00% | -17.86% | 28 | 27 | ⚠️ |
| Braintree | 100.00% | 100.00% | +0.00% | 40 | 34 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 66 | 62 | 94.29% | 100.00% | -5.71 |
| Expired, Invalid, Closed Card, No Account | 3 | 0 | 4.29% | 0.00% | +4.29 |
| 3DS Authentication Failed/Required | 1 | 0 | 1.43% | 0.00% | +1.43 |

**Root Cause:** CreditCard + ProcessOut + Others

---

## L2: DK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| CreditCard | 98.33% | 99.18% | -0.86% | 480 | 611 |  |
| Paypal | 100.00% | 100.00% | +0.00% | 16 | 35 |  |
| ApplePay | 100.00% | 99.31% | +0.70% | 411 | 432 |  |
| Mobilepay | 74.89% | 66.67% | +12.34% | 231 | 3 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Adyen | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| ProcessOut | 90.72% | 99.02% | -8.39% | 711 | 614 | ⚠️ |
| Braintree | 100.00% | 99.36% | +0.65% | 427 | 467 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Blocked, Restricted, Not Permitted | 0 | 1 | 0.00% | 0.09% | -0.09 |
| Fraud, Lost/Stolen Card, Security | 0 | 1 | 0.00% | 0.09% | -0.09 |
| PayPal Declined, Revoked, Payer Issue | 1 | 0 | 0.09% | 0.00% | +0.09 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 1 | 0 | 0.09% | 0.00% | +0.09 |
| Others | 1,136 | 1,079 | 99.82% | 99.81% | +0.01 |

**Root Cause:** Mobilepay + ProcessOut

---

## L2: DE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| CreditCard | 96.11% | 96.99% | -0.91% | 899 | 1,197 |  |
| ApplePay | 96.14% | 96.01% | +0.14% | 1,553 | 1,928 |  |
| Paypal | 98.55% | 97.96% | +0.60% | 4,273 | 5,744 |  |
| Klarna | 55.81% | 48.39% | +15.35% | 903 | 31 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| ProcessOut | 96.10% | 97.07% | -1.00% | 898 | 1,196 |  |
| Braintree | 97.91% | 97.47% | +0.45% | 5,826 | 7,672 |  |
| Adyen | 55.86% | 46.88% | +19.17% | 904 | 32 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 7,595 | 8,839 | 99.57% | 99.31% | +0.25 |
| PayPal Declined, Revoked, Payer Issue | 14 | 33 | 0.18% | 0.37% | -0.19 |
| Fraud, Lost/Stolen Card, Security | 3 | 9 | 0.04% | 0.10% | -0.06 |
| Call Issuer, Voice Auth Required | 1 | 4 | 0.01% | 0.04% | -0.03 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 12 | 12 | 0.16% | 0.13% | +0.02 |
| Expired, Invalid, Closed Card, No Account | 0 | 2 | 0.00% | 0.02% | -0.02 |
| 3DS Authentication Failed/Required | 1 | 0 | 0.01% | 0.00% | +0.01 |
| Gateway Rejected, Risk Threshold | 1 | 0 | 0.01% | 0.00% | +0.01 |
| Blocked, Restricted, Not Permitted | 1 | 1 | 0.01% | 0.01% | +0.00 |

**Root Cause:** Klarna + Adyen

---

## L2: FR Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| CreditCard | 90.59% | 98.15% | -7.71% | 3,729 | 3,353 | ⚠️ |
| ApplePay | 96.47% | 95.72% | +0.78% | 1,981 | 1,730 |  |
| Paypal | 96.83% | 96.09% | +0.78% | 916 | 818 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Adyen | 87.50% | 100.00% | -12.50% | 8 | 3 | ⚠️ |
| ProcessOut | 90.59% | 98.15% | -7.70% | 3,721 | 3,350 | ⚠️ |
| Braintree | 96.58% | 95.84% | +0.78% | 2,897 | 2,548 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 3DS Authentication Failed/Required | 20 | 4 | 0.30% | 0.07% | +0.23 |
| PayPal Declined, Revoked, Payer Issue | 22 | 27 | 0.33% | 0.46% | -0.13 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 9 | 15 | 0.14% | 0.25% | -0.12 |
| Fraud, Lost/Stolen Card, Security | 12 | 7 | 0.18% | 0.12% | +0.06 |
| Blocked, Restricted, Not Permitted | 1 | 4 | 0.02% | 0.07% | -0.05 |
| Expired, Invalid, Closed Card, No Account | 1 | 3 | 0.02% | 0.05% | -0.04 |
| Others | 6,560 | 5,841 | 99.00% | 98.98% | +0.02 |
| CVV/CVC Mismatch | 1 | 0 | 0.02% | 0.00% | +0.02 |

**Root Cause:** CreditCard + Adyen

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| DE | High (>92%) | 8,900 | 7,628 | -14.3% | Stable |
| GB | High (>92%) | 8,348 | 8,662 | +3.8% | Stable |
| FR | High (>92%) | 5,901 | 6,626 | +12.3% | Stable |
| AU | High (>92%) | 3,012 | 2,928 | -2.8% | Stable |
| NL | Medium (>85%) | 1,371 | 1,695 | +23.6% | Stable |
| IE | High (>92%) | 1,323 | 1,157 | -12.5% | Stable |
| BE | Low (>85%) | 1,088 | 1,087 | -0.1% | Stable |
| DK | High (>92%) | 1,081 | 1,138 | +5.3% | Stable |
| SE | Medium (>85%) | 1,070 | 1,035 | -3.3% | Stable |
| NZ | High (>92%) | 644 | 784 | +21.7% | Stable |
| NO | High (>92%) | 627 | 734 | +17.1% | Stable |
| AT | High (>92%) | 505 | 510 | +1.0% | Stable |
| CH | High (>92%) | 148 | 127 | -14.2% | Stable |
| LU | High (>92%) | 62 | 70 | +12.9% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| LU | ↓ -8.57% | CreditCard -20.0% | ProcessOut -50.0% | Others -5.71pp | CreditCard + ProcessOut + Others |
| DK | ↓ -5.01% | Mobilepay +12.3% | ProcessOut -8.4% | → Stable | Mobilepay + ProcessOut |
| DE | ↓ -4.65% | Klarna +15.4% | Adyen +19.2% | → Stable | Klarna + Adyen |
| FR | ↓ -4.06% | CreditCard -7.7% | Adyen -12.5% | → Stable | CreditCard + Adyen |

---

*Report: 2026-05-05*
