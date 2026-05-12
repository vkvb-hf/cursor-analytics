# PCAR Investigation: HF-INTL 2026-W19

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 94.18% → 92.95% (-1.31%)  
**Volume:** 33,686 orders  
**Significance:** Significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate declined from 94.18% to 92.95% (-1.31%) in W19, continuing a downward trend that began in W17 (96.67%), representing a cumulative decline of 3.72pp over three weeks.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 8-Week Trend | Sustained decline since W17 | -3.72pp (W17→W19) | ⚠️ |
| Country Breakdown | 3 countries below threshold | DE -4.12%, SE -3.70%, NZ -2.98% | ⚠️ |
| Payment Method | "Others" category major decline | -11.61% | ⚠️ |
| Mix Shift | NO volume drop significant | -25.5% volume | ⚠️ |
| Root Cause Identified | Klarna/Adyen in DE & SE | -64.79% (DE Klarna) | ⚠️ |

**Key Findings:**
- **Klarna + Adyen integration failure in DE:** Klarna approval rate collapsed from 55.81% to 19.65% (-64.79%), with Adyen showing identical decline pattern (-64.49%), affecting 865 orders
- **SE mirrors DE pattern:** Klarna via Adyen declined from 84.02% to 76.92% (-8.45%), indicating a systematic issue with this payment method/provider combination
- **NZ shows separate issue:** Paypal via Braintree dropped from 96.67% to 85.19% (-11.88%), though lower volume (27 orders) limits overall impact
- **LU positive outlier:** CreditCard via Adyen improved significantly (+17.06% to +20.37%), recovering from prior issues with expired/invalid cards
- **Three consecutive weeks of decline:** W17→W18 (-2.58%), W18→W19 (-1.31%) suggests underlying systemic issue rather than isolated incident

**Action:** **Escalate** - Immediate investigation required into Klarna/Adyen integration in DE and SE markets. The 64.79% decline in DE Klarna approval rate represents a critical payment processing failure that requires urgent technical review with the Adyen team.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W19 | 92.95% | 33,686 | -1.31% ← REPORTED CHANGE |
| 2026-W18 | 94.18% | 34,181 | -2.58% |
| 2026-W17 | 96.67% | 34,080 | -0.47% |
| 2026-W16 | 97.13% | 37,314 | +1.05% |
| 2026-W15 | 96.12% | 36,514 | +0.13% |
| 2026-W14 | 96.0% | 31,465 | +0.83% |
| 2026-W13 | 95.21% | 39,598 | -1.52% |
| 2026-W12 | 96.68% | 38,136 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| DE | 88.89% | 92.71% | -4.12% | 7,281 | ⚠️ |
| SE | 87.83% | 91.21% | -3.70% | 986 | ⚠️ |
| NZ | 91.95% | 94.77% | -2.98% | 795 | ⚠️ |
| BE | 81.72% | 83.07% | -1.62% | 1,160 |  |
| LU | 96.49% | 91.43% | +5.54% | 57 | ⚠️ |

**Countries exceeding ±2.5% threshold:** DE, SE, NZ, LU

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | 67.71% | 76.6% | -11.61% | 3,945 | ⚠️ |
| Credit Card | 93.57% | 94.34% | -0.82% | 11,781 |  |
| Paypal | 98.22% | 98.11% | +0.11% | 6,614 |  |
| Apple Pay | 98.01% | 97.58% | +0.44% | 11,346 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: DE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Klarna | 19.65% | 55.81% | -64.79% | 865 | 903 | ⚠️ |
| CreditCard | 95.39% | 96.11% | -0.75% | 889 | 899 |  |
| Paypal | 98.79% | 98.55% | +0.24% | 4,131 | 4,273 |  |
| ApplePay | 98.35% | 96.14% | +2.31% | 1,396 | 1,553 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Adyen | 19.84% | 55.86% | -64.49% | 867 | 904 | ⚠️ |
| ProcessOut | 95.38% | 96.10% | -0.75% | 887 | 898 |  |
| Braintree | 98.68% | 97.91% | +0.79% | 5,527 | 5,826 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 7,237 | 7,595 | 99.40% | 99.57% | -0.17 |
| PayPal Declined, Revoked, Payer Issue | 24 | 14 | 0.33% | 0.18% | +0.15 |
| 3DS Authentication Failed/Required | 8 | 1 | 0.11% | 0.01% | +0.10 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 5 | 12 | 0.07% | 0.16% | -0.09 |
| Fraud, Lost/Stolen Card, Security | 4 | 3 | 0.05% | 0.04% | +0.02 |
| Call Issuer, Voice Auth Required | 2 | 1 | 0.03% | 0.01% | +0.01 |
| Expired, Invalid, Closed Card, No Account | 1 | 0 | 0.01% | 0.00% | +0.01 |
| Blocked, Restricted, Not Permitted | 0 | 1 | 0.00% | 0.01% | -0.01 |
| Gateway Rejected, Risk Threshold | 0 | 1 | 0.00% | 0.01% | -0.01 |

**Root Cause:** Klarna + Adyen

---

## L2: SE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Klarna | 76.92% | 84.02% | -8.45% | 481 | 507 | ⚠️ |
| ApplePay | 98.74% | 99.57% | -0.83% | 239 | 233 |  |
| CreditCard | 97.62% | 97.14% | +0.49% | 252 | 280 |  |
| Paypal | 100.00% | 93.33% | +7.14% | 14 | 15 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Adyen | 76.92% | 84.02% | -8.45% | 481 | 507 | ⚠️ |
| Braintree | 98.81% | 99.19% | -0.38% | 253 | 248 |  |
| ProcessOut | 97.62% | 97.14% | +0.49% | 252 | 280 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 986 | 1,031 | 100.00% | 99.61% | +0.39 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 0 | 2 | 0.00% | 0.19% | -0.19 |
| Fraud, Lost/Stolen Card, Security | 0 | 1 | 0.00% | 0.10% | -0.10 |
| PayPal Declined, Revoked, Payer Issue | 0 | 1 | 0.00% | 0.10% | -0.10 |

**Root Cause:** Klarna + Adyen

---

## L2: NZ Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
|  | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Paypal | 85.19% | 96.67% | -11.88% | 27 | 30 | ⚠️ |
| CreditCard | 90.35% | 93.35% | -3.21% | 539 | 526 |  |
| ApplePay | 96.51% | 97.81% | -1.33% | 229 | 228 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Adyen | 0.00% | 0.00% | +0.00% | 1 | 0 |  |
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| NoPayment | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Braintree | 85.19% | 96.67% | -11.88% | 27 | 30 | ⚠️ |
| ProcessOut | 92.31% | 94.69% | -2.52% | 767 | 754 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 783 | 777 | 98.49% | 99.11% | -0.62 |
| PayPal Declined, Revoked, Payer Issue | 6 | 2 | 0.75% | 0.26% | +0.50 |
| Blocked, Restricted, Not Permitted | 1 | 0 | 0.13% | 0.00% | +0.13 |
| 3DS Authentication Failed/Required | 2 | 2 | 0.25% | 0.26% | +0.00 |
| Fraud, Lost/Stolen Card, Security | 2 | 2 | 0.25% | 0.26% | +0.00 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 1 | 1 | 0.13% | 0.13% | +0.00 |

**Root Cause:** Paypal + Braintree

---

## L2: LU Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Sepa | 100.00% | 0.00% | +0.00% | 1 | 0 |  |
| ApplePay | 95.24% | 100.00% | -4.76% | 21 | 26 |  |
| Paypal | 100.00% | 100.00% | +0.00% | 8 | 14 |  |
| CreditCard | 96.30% | 80.00% | +20.37% | 27 | 30 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Braintree | 96.55% | 100.00% | -3.45% | 29 | 40 |  |
| Adyen | 96.15% | 82.14% | +17.06% | 26 | 28 | ⚠️ |
| ProcessOut | 100.00% | 50.00% | +100.00% | 2 | 2 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Expired, Invalid, Closed Card, No Account | 1 | 3 | 1.75% | 4.29% | -2.53 |
| Others | 55 | 66 | 96.49% | 94.29% | +2.21 |
| Fraud, Lost/Stolen Card, Security | 1 | 0 | 1.75% | 0.00% | +1.75 |
| 3DS Authentication Failed/Required | 0 | 1 | 0.00% | 1.43% | -1.43 |

**Root Cause:** CreditCard + Adyen + Expired,

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | High (>92%) | 8,662 | 8,717 | +0.6% | Stable |
| DE | High (>92%) | 7,628 | 7,281 | -4.5% | Stable |
| FR | High (>92%) | 6,626 | 7,051 | +6.4% | Stable |
| AU | High (>92%) | 2,928 | 2,631 | -10.1% | Stable |
| NL | Medium (>85%) | 1,695 | 1,724 | +1.7% | Stable |
| IE | High (>92%) | 1,157 | 1,187 | +2.6% | Stable |
| DK | High (>92%) | 1,138 | 934 | -17.9% | Stable |
| BE | Low (>85%) | 1,087 | 1,160 | +6.7% | Stable |
| SE | Medium (>85%) | 1,035 | 986 | -4.7% | Stable |
| NZ | High (>92%) | 784 | 795 | +1.4% | Stable |
| NO | High (>92%) | 734 | 547 | -25.5% | ⚠️ Volume drop |
| AT | High (>92%) | 510 | 488 | -4.3% | Stable |
| CH | High (>92%) | 127 | 128 | +0.8% | Stable |
| LU | Medium (>85%) | 70 | 57 | -18.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| DE | ↓ -4.12% | Klarna -64.8% | Adyen -64.5% | → Stable | Klarna + Adyen |
| SE | ↓ -3.70% | Klarna -8.4% | Adyen -8.4% | → Stable | Klarna + Adyen |
| NZ | ↓ -2.98% | Paypal -11.9% | Braintree -11.9% | → Stable | Paypal + Braintree |
| LU | ↑ +5.54% | CreditCard +20.4% | Adyen +17.1% | Expired, Invalid, Closed Card, No Account -2.53pp | CreditCard + Adyen + Expired, |

---

*Report: 2026-05-12*
