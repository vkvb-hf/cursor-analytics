# PCAR Investigation: HF-INTL 2026-W17

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 97.13% → 95.74% (-1.43%)  
**Volume:** 34,080 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate declined significantly from 97.13% to 95.74% (-1.43%) in HF-INTL for 2026-W17, representing a notable drop below the 8-week average performance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Overall AR Trend | 8-week pattern | -1.43% WoW | ⚠️ Below recent highs (97.31% in W10) |
| Country Performance | 4 countries flagged | BE -20.40%, NL -10.95%, SE -9.26% | ⚠️ Multiple markets impacted |
| Payment Method | Others category | -16.90% | ⚠️ Alternative payment methods degraded |
| Provider Analysis | Adyen across markets | Consistent declines | ⚠️ Provider-specific issue identified |
| Mix Shift | Volume distribution | NZ -31.3%, NO -31.0% | ⚠️ Major volume shifts detected |

**Key Findings:**
- **BE experienced the largest decline (-20.40%)**, driven by BcmcMobile payment method (59.04% vs 71.43% prior) processed through Adyen (-17.08%)
- **Adyen is the common denominator** across all three declining markets (BE, NL, SE), with approval rates dropping 12-21% for local payment methods (BcmcMobile, iDEAL, Klarna)
- **NL iDEAL transactions** dropped from 90.76% to 77.49% (-14.62%), impacting 1,026 orders through Adyen
- **SE Klarna approvals** fell sharply from 80.44% to 63.33% (-21.27%), with Adyen processing showing identical decline
- **CH showed improvement (+5.71%)** with ApplePay and CreditCard via ProcessOut recovering, coinciding with reduced fraud-related declines (-1.34pp)

**Action:** **Escalate** — Immediate investigation required into Adyen's processing of local European payment methods (BcmcMobile, iDEAL, Klarna). Contact Adyen technical support to identify any configuration changes, outages, or policy updates affecting BE, NL, and SE markets during W17.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 95.74% | 34,080 | -1.43% ← REPORTED CHANGE |
| 2026-W16 | 97.13% | 37,314 | +1.05% |
| 2026-W15 | 96.12% | 36,514 | +0.13% |
| 2026-W14 | 96.0% | 31,465 | +0.83% |
| 2026-W13 | 95.21% | 39,598 | -1.52% |
| 2026-W12 | 96.68% | 38,136 | -0.53% |
| 2026-W11 | 97.2% | 42,932 | -0.11% |
| 2026-W10 | 97.31% | 44,946 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| BE | 74.54% | 93.64% | -20.40% | 1,088 | ⚠️ |
| NL | 79.50% | 89.28% | -10.95% | 1,371 | ⚠️ |
| SE | 81.50% | 89.81% | -9.26% | 1,070 | ⚠️ |
| FR | 97.14% | 98.18% | -1.07% | 5,901 |  |
| CH | 99.32% | 93.96% | +5.71% | 148 | ⚠️ |

**Countries exceeding ±2.5% threshold:** BE, NL, SE, CH

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | 68.13% | 81.98% | -16.90% | 2,372 | ⚠️ |
| Credit Card | 97.96% | 98.36% | -0.40% | 12,020 |  |
| Apple Pay | 97.7% | 97.95% | -0.26% | 11,535 |  |
| Paypal | 97.73% | 97.89% | -0.16% | 8,153 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: BE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Sepa | 100.00% | 0.00% | +0.00% | 1 | 0 |  |
| BcmcMobile | 59.04% | 71.43% | -17.34% | 647 | 154 | ⚠️ |
| Paypal | 94.37% | 97.60% | -3.31% | 71 | 125 |  |
| ApplePay | 95.97% | 96.25% | -0.29% | 124 | 240 |  |
| CreditCard | 98.78% | 97.82% | +0.97% | 245 | 551 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Adyen | 59.23% | 71.43% | -17.08% | 650 | 154 | ⚠️ |
| Braintree | 95.38% | 96.71% | -1.37% | 195 | 365 |  |
| ProcessOut | 98.77% | 97.82% | +0.96% | 243 | 551 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 1,084 | 1,062 | 99.63% | 99.25% | +0.38 |
| Fraud, Lost/Stolen Card, Security | 2 | 4 | 0.18% | 0.37% | -0.19 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 1 | 2 | 0.09% | 0.19% | -0.10 |
| CVV/CVC Mismatch | 0 | 1 | 0.00% | 0.09% | -0.09 |
| PayPal Declined, Revoked, Payer Issue | 1 | 1 | 0.09% | 0.09% | +0.00 |

**Root Cause:** BcmcMobile + Adyen

---

## L2: NL Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
|  | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Sepa | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| IDeal | 77.49% | 90.76% | -14.62% | 1,026 | 1,147 | ⚠️ |
| Paypal | 92.86% | 95.65% | -2.92% | 14 | 23 |  |
| ApplePay | 99.31% | 99.45% | -0.14% | 145 | 181 |  |
| CreditCard | 100.00% | 100.00% | +0.00% | 51 | 74 |  |
| Klarna | 64.44% | 64.25% | +0.31% | 135 | 179 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| NoPayment | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Adyen | 75.97% | 87.18% | -12.86% | 1,161 | 1,326 | ⚠️ |
| Braintree | 98.74% | 99.02% | -0.28% | 159 | 204 |  |
| ProcessOut | 100.00% | 100.00% | +0.00% | 51 | 74 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Fraud, Lost/Stolen Card, Security | 1 | 1 | 0.07% | 0.06% | +0.01 |
| Others | 1,370 | 1,603 | 99.93% | 99.94% | -0.01 |

**Root Cause:** IDeal + Adyen

---

## L2: SE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Klarna | 63.33% | 80.44% | -21.27% | 529 | 639 | ⚠️ |
| ApplePay | 99.22% | 99.32% | -0.10% | 256 | 293 |  |
| Paypal | 100.00% | 100.00% | +0.00% | 14 | 17 |  |
| CreditCard | 99.26% | 98.56% | +0.71% | 271 | 347 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Adyen | 63.33% | 80.44% | -21.27% | 529 | 639 | ⚠️ |
| Braintree | 99.26% | 99.35% | -0.10% | 270 | 310 |  |
| ProcessOut | 99.26% | 98.56% | +0.71% | 271 | 347 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 1,069 | 1,290 | 99.91% | 99.54% | +0.37 |
| PayPal Declined, Revoked, Payer Issue | 0 | 2 | 0.00% | 0.15% | -0.15 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 0 | 2 | 0.00% | 0.15% | -0.15 |
| 3DS Authentication Failed/Required | 0 | 1 | 0.00% | 0.08% | -0.08 |
| Fraud, Lost/Stolen Card, Security | 1 | 1 | 0.09% | 0.08% | +0.02 |

**Root Cause:** Klarna + Adyen

---

## L2: CH Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Paypal | 100.00% | 100.00% | +0.00% | 20 | 23 |  |
| ApplePay | 98.15% | 91.84% | +6.87% | 54 | 49 | ⚠️ |
| CreditCard | 100.00% | 93.51% | +6.94% | 74 | 77 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Adyen | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Braintree | 98.65% | 94.44% | +4.45% | 74 | 72 |  |
| ProcessOut | 100.00% | 93.51% | +6.94% | 74 | 77 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Fraud, Lost/Stolen Card, Security | 0 | 2 | 0.00% | 1.34% | -1.34 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 1 | 0 | 0.68% | 0.00% | +0.68 |
| Others | 147 | 147 | 99.32% | 98.66% | +0.67 |

**Root Cause:** ApplePay + ProcessOut + Fraud,

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | High (>92%) | 9,915 | 8,348 | -15.8% | Stable |
| DE | High (>92%) | 8,708 | 8,900 | +2.2% | Stable |
| FR | High (>92%) | 6,547 | 5,901 | -9.9% | Stable |
| AU | High (>92%) | 2,930 | 3,012 | +2.8% | Stable |
| NL | Medium (>85%) | 1,604 | 1,371 | -14.5% | Stable |
| IE | High (>92%) | 1,394 | 1,323 | -5.1% | Stable |
| SE | Medium (>85%) | 1,296 | 1,070 | -17.4% | Stable |
| DK | High (>92%) | 1,228 | 1,081 | -12.0% | Stable |
| BE | High (>92%) | 1,070 | 1,088 | +1.7% | Stable |
| NZ | High (>92%) | 937 | 644 | -31.3% | ⚠️ Major mix shift |
| NO | High (>92%) | 909 | 627 | -31.0% | ⚠️ Major mix shift |
| AT | High (>92%) | 543 | 505 | -7.0% | Stable |
| CH | High (>92%) | 149 | 148 | -0.7% | Stable |
| LU | High (>92%) | 84 | 62 | -26.2% | ⚠️ Volume drop |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| BE | ↓ -20.40% | BcmcMobile -17.3% | Adyen -17.1% | → Stable | BcmcMobile + Adyen |
| NL | ↓ -10.95% | IDeal -14.6% | Adyen -12.9% | → Stable | IDeal + Adyen |
| SE | ↓ -9.26% | Klarna -21.3% | Adyen -21.3% | → Stable | Klarna + Adyen |
| CH | ↑ +5.71% | ApplePay +6.9% | ProcessOut +6.9% | Fraud, Lost/Stolen Card, Security -1.34pp | ApplePay + ProcessOut + Fraud, |

---

*Report: 2026-04-27*
