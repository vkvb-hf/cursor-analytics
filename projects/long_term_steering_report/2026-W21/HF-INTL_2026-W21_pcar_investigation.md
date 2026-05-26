# PCAR Investigation: HF-INTL 2026-W21

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 93.5% → 93.72% (+0.24%)  
**Volume:** 28,206 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate for HF-INTL improved marginally from 93.5% to 93.72% (+0.22pp) in W21, though this change is not statistically significant and masks concerning declines in several key markets.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate below W14-W17 levels (96-97%) | -2.95pp vs W17 | ⚠️ |
| L1: Country Variance | 4 countries exceed ±2.5% threshold | AT -3.33%, DE -3.04%, CH -2.91%, FR +3.41% | ⚠️ |
| L1: Payment Method | Others -4.78%, Credit Card +4.18% | Mixed performance | ⚠️ |
| L2: AT Deep-Dive | ApplePay -8.13%, Braintree -5.35% | Provider issue identified | ⚠️ |
| L2: DE Deep-Dive | Klarna -7.73%, Adyen -7.85% | Provider issue identified | ⚠️ |
| Mix Shift | CH volume -20.9% | Minor impact | ✅ |

**Key Findings:**
- DE shows significant decline (-3.04pp) driven by Klarna via Adyen, with Klarna approval rate at only 52.56% (down from 56.96%)
- AT experienced an 8.13pp drop in ApplePay approval rate (91.24% vs 99.32%), linked to Braintree provider declining 5.35pp
- FR showed strong improvement (+3.41pp) driven by Credit Card via ProcessOut recovering from 90.52% to 97.31%
- The 8-week trend reveals a sustained decline from peak performance in W16-W17 (97%+) to current levels (~93.7%)
- Order volume declined 11% WoW (28,206 vs 31,674), with most markets showing volume contraction

**Action:** Investigate — Prioritize root cause analysis for Klarna/Adyen integration in DE and ApplePay/Braintree issues in AT, as these high-volume markets are driving underlying performance degradation despite the headline metric appearing stable.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W21 | 93.72% | 28,206 | +0.24% ← REPORTED CHANGE |
| 2026-W20 | 93.5% | 31,674 | +0.59% |
| 2026-W19 | 92.95% | 33,686 | -1.31% |
| 2026-W18 | 94.18% | 34,181 | -2.58% |
| 2026-W17 | 96.67% | 34,080 | -0.47% |
| 2026-W16 | 97.13% | 37,314 | +1.05% |
| 2026-W15 | 96.12% | 36,514 | +0.13% |
| 2026-W14 | 96.0% | 31,465 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| AT | 93.78% | 97.01% | -3.33% | 386 | ⚠️ |
| DE | 87.92% | 90.67% | -3.04% | 6,480 | ⚠️ |
| CH | 90.57% | 93.28% | -2.91% | 106 | ⚠️ |
| GB | 97.72% | 97.13% | +0.60% | 6,052 |  |
| AU | 97.01% | 95.09% | +2.02% | 2,907 |  |
| FR | 96.77% | 93.57% | +3.41% | 5,750 | ⚠️ |

**Countries exceeding ±2.5% threshold:** AT, DE, CH, FR

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | 71.24% | 74.81% | -4.78% | 3,946 | ⚠️ |
| Apple Pay | 97.14% | 97.88% | -0.76% | 9,150 |  |
| Paypal | 98.05% | 98.09% | -0.04% | 5,336 |  |
| Credit Card | 97.25% | 93.34% | +4.18% | 9,774 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: AT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| ApplePay | 91.24% | 99.32% | -8.13% | 137 | 147 | ⚠️ |
| Paypal | 95.05% | 96.58% | -1.59% | 101 | 117 |  |
| CreditCard | 95.27% | 95.32% | -0.05% | 148 | 171 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Braintree | 92.86% | 98.11% | -5.35% | 238 | 264 | ⚠️ |
| ProcessOut | 95.27% | 95.32% | -0.05% | 148 | 171 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 376 | 429 | 97.41% | 98.62% | -1.21 |
| Fraud, Lost/Stolen Card, Security | 4 | 1 | 1.04% | 0.23% | +0.81 |
| Call Issuer, Voice Auth Required | 1 | 0 | 0.26% | 0.00% | +0.26 |
| PayPal Declined, Revoked, Payer Issue | 3 | 3 | 0.78% | 0.69% | +0.09 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 2 | 2 | 0.52% | 0.46% | +0.06 |

**Root Cause:** ApplePay + Braintree + Others

---

## L2: DE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Klarna | 52.56% | 56.96% | -7.73% | 1,448 | 1,171 | ⚠️ |
| ApplePay | 96.29% | 97.50% | -1.24% | 1,132 | 1,238 |  |
| Paypal | 98.87% | 98.87% | +0.00% | 3,186 | 3,642 |  |
| CreditCard | 97.48% | 92.00% | +5.95% | 714 | 863 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Adyen | 52.56% | 57.03% | -7.85% | 1,448 | 1,173 | ⚠️ |
| Braintree | 98.19% | 98.52% | -0.34% | 4,318 | 4,880 |  |
| ProcessOut | 97.48% | 91.99% | +5.97% | 714 | 861 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 6,454 | 6,871 | 99.60% | 99.38% | +0.22 |
| 3DS Authentication Failed/Required | 0 | 9 | 0.00% | 0.13% | -0.13 |
| PayPal Declined, Revoked, Payer Issue | 15 | 22 | 0.23% | 0.32% | -0.09 |
| Call Issuer, Voice Auth Required | 2 | 0 | 0.03% | 0.00% | +0.03 |
| Gateway Rejected, Risk Threshold | 0 | 1 | 0.00% | 0.01% | -0.01 |
| Expired, Invalid, Closed Card, No Account | 1 | 2 | 0.02% | 0.03% | -0.01 |
| Fraud, Lost/Stolen Card, Security | 4 | 5 | 0.06% | 0.07% | -0.01 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 4 | 4 | 0.06% | 0.06% | +0.00 |

**Root Cause:** Klarna + Adyen

---

## L2: CH Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Paypal | 87.50% | 100.00% | -12.50% | 8 | 21 | ⚠️ |
| ApplePay | 96.77% | 98.04% | -1.29% | 31 | 51 |  |
| CreditCard | 97.62% | 88.33% | +10.51% | 42 | 60 | ⚠️ |
| Twint | 72.00% | 50.00% | +44.00% | 25 | 2 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Braintree | 94.87% | 98.61% | -3.79% | 39 | 72 |  |
| ProcessOut | 97.62% | 88.33% | +10.51% | 42 | 60 | ⚠️ |
| Adyen | 72.00% | 50.00% | +44.00% | 25 | 2 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 105 | 134 | 99.06% | 100.00% | -0.94 |
| PayPal Declined, Revoked, Payer Issue | 1 | 0 | 0.94% | 0.00% | +0.94 |

**Root Cause:** Paypal + ProcessOut

---

## L2: FR Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| ApplePay | 95.65% | 97.54% | -1.94% | 1,770 | 2,034 |  |
| Paypal | 97.08% | 97.34% | -0.27% | 788 | 902 |  |
| CreditCard | 97.31% | 90.52% | +7.50% | 3,192 | 3,754 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Braintree | 96.09% | 97.48% | -1.42% | 2,558 | 2,936 |  |
| Adyen | 100.00% | 100.00% | +0.00% | 1 | 4 |  |
| ProcessOut | 97.30% | 90.51% | +7.51% | 3,191 | 3,750 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 3DS Authentication Failed/Required | 3 | 22 | 0.05% | 0.33% | -0.28 |
| PayPal Declined, Revoked, Payer Issue | 22 | 15 | 0.38% | 0.22% | +0.16 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 10 | 4 | 0.17% | 0.06% | +0.11 |
| Others | 5,704 | 6,642 | 99.20% | 99.28% | -0.08 |
| Blocked, Restricted, Not Permitted | 4 | 2 | 0.07% | 0.03% | +0.04 |
| Fraud, Lost/Stolen Card, Security | 4 | 3 | 0.07% | 0.04% | +0.02 |
| Expired, Invalid, Closed Card, No Account | 3 | 2 | 0.05% | 0.03% | +0.02 |

**Root Cause:** CreditCard + ProcessOut

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | High (>92%) | 7,532 | 6,052 | -19.6% | Stable |
| DE | Medium (>85%) | 6,914 | 6,480 | -6.3% | Stable |
| FR | High (>92%) | 6,690 | 5,750 | -14.1% | Stable |
| AU | High (>92%) | 2,992 | 2,907 | -2.8% | Stable |
| NL | Medium (>85%) | 1,508 | 1,250 | -17.1% | Stable |
| IE | High (>92%) | 1,315 | 1,217 | -7.5% | Stable |
| BE | Medium (>85%) | 1,127 | 1,074 | -4.7% | Stable |
| DK | High (>92%) | 892 | 751 | -15.8% | Stable |
| SE | Medium (>85%) | 857 | 820 | -4.3% | Stable |
| NZ | High (>92%) | 832 | 820 | -1.4% | Stable |
| AT | High (>92%) | 435 | 386 | -11.3% | Stable |
| NO | High (>92%) | 376 | 509 | +35.4% | Stable |
| CH | High (>92%) | 134 | 106 | -20.9% | ⚠️ Volume drop |
| LU | High (>92%) | 70 | 84 | +20.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| AT | ↓ -3.33% | ApplePay -8.1% | Braintree -5.4% | Others -1.21pp | ApplePay + Braintree + Others |
| DE | ↓ -3.04% | Klarna -7.7% | Adyen -7.8% | → Stable | Klarna + Adyen |
| CH | ↓ -2.91% | Paypal -12.5% | ProcessOut +10.5% | → Stable | Paypal + ProcessOut |
| FR | ↑ +3.41% | CreditCard +7.5% | ProcessOut +7.5% | → Stable | CreditCard + ProcessOut |

---

*Report: 2026-05-26*
