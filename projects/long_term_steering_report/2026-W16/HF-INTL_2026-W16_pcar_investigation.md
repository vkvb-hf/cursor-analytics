# PCAR Investigation: HF-INTL 2026-W16

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 96.12% → 97.13% (+1.05%)  
**Volume:** 37,314 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate for HF-INTL improved significantly from 96.12% to 97.13% (+1.01 pp) in 2026-W16, recovering toward the 97.31% level seen in W10 after a dip in W13.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Upward recovery after W13 dip | +1.05% WoW | ✅ |
| L1: Country Breakdown | 2 countries flagged (BE, DE) | BE +3.72%, DE +4.35% | ⚠️ |
| L1: Dimension Scan | PaymentMethod "Others" flagged | +7.20% | ⚠️ |
| L2: BE Deep-Dive | BcmcMobile via Adyen declining | -6.61% / -6.69% | ⚠️ |
| L2: DE Deep-Dive | Klarna via Adyen declining | -10.81% / -9.23% | ⚠️ |
| Mix Shift | AT volume drop (-22.3%) | Minor impact | ⚠️ |

**Key Findings:**
- The overall +1.01 pp improvement is driven by strong performance in DE (+4.35 pp) and BE (+3.72 pp), despite underlying payment method issues
- In DE, Klarna approval rate dropped sharply from 53.62% to 47.83% (-10.81 pp), with volume declining from 966 to 115 orders—suggesting possible routing changes or Klarna issues via Adyen
- In BE, BcmcMobile approval rate fell from 76.49% to 71.43% (-6.61 pp) with volume decreasing from 370 to 154 orders, linked to Adyen provider performance
- Adyen is the common provider in both flagged countries showing degraded performance for specific local payment methods
- AT experienced a -22.3% volume drop (699 → 543 orders) but maintains High AR tier, warranting monitoring

**Action:** **Monitor** - The overall metric improved significantly and the flagged payment method issues (Klarna in DE, BcmcMobile in BE) appear to have reduced volume impact. Continue monitoring Adyen performance for local payment methods; escalate if Klarna or BcmcMobile volumes return to previous levels without rate recovery.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 97.13% | 37,314 | +1.05% ← REPORTED CHANGE |
| 2026-W15 | 96.12% | 36,514 | +0.13% |
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
| LU | 97.62% | 100.00% | -2.38% | 84 |  |
| SE | 89.81% | 91.93% | -2.30% | 1,296 |  |
| AU | 98.46% | 97.60% | +0.89% | 2,930 |  |
| BE | 93.64% | 90.29% | +3.72% | 1,070 | ⚠️ |
| DE | 96.93% | 92.89% | +4.35% | 8,708 | ⚠️ |

**Countries exceeding ±2.5% threshold:** BE, DE

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Apple Pay | 97.95% | 98.03% | -0.08% | 12,654 |  |
| Paypal | 97.89% | 97.96% | -0.07% | 8,335 |  |
| Credit Card | 98.36% | 98.22% | +0.14% | 14,083 |  |
| Others | 81.98% | 76.47% | +7.20% | 2,242 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: BE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Sepa | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| BcmcMobile | 71.43% | 76.49% | -6.61% | 154 | 370 | ⚠️ |
| ApplePay | 96.25% | 99.05% | -2.82% | 240 | 210 |  |
| CreditCard | 97.82% | 96.93% | +0.92% | 551 | 391 |  |
| Paypal | 97.60% | 96.36% | +1.28% | 125 | 110 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Adyen | 71.43% | 76.55% | -6.69% | 154 | 371 | ⚠️ |
| Braintree | 96.71% | 98.13% | -1.44% | 365 | 320 |  |
| ProcessOut | 97.82% | 96.92% | +0.93% | 551 | 390 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 1,062 | 1,067 | 99.25% | 98.70% | +0.55 |
| CVV/CVC Mismatch | 1 | 3 | 0.09% | 0.28% | -0.18 |
| PayPal Declined, Revoked, Payer Issue | 1 | 3 | 0.09% | 0.28% | -0.18 |
| Fraud, Lost/Stolen Card, Security | 4 | 6 | 0.37% | 0.56% | -0.18 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 2 | 1 | 0.19% | 0.09% | +0.09 |
| Expired, Invalid, Closed Card, No Account | 0 | 1 | 0.00% | 0.09% | -0.09 |

**Root Cause:** BcmcMobile + Adyen

---

## L2: DE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Klarna | 47.83% | 53.62% | -10.81% | 115 | 966 | ⚠️ |
| ApplePay | 96.23% | 96.74% | -0.53% | 1,831 | 1,596 |  |
| Paypal | 97.96% | 98.21% | -0.25% | 5,549 | 5,024 |  |
| CreditCard | 97.94% | 97.85% | +0.09% | 1,213 | 1,022 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Adyen | 48.72% | 53.67% | -9.23% | 117 | 967 | ⚠️ |
| Braintree | 97.53% | 97.85% | -0.33% | 7,380 | 6,620 |  |
| ProcessOut | 97.94% | 97.85% | +0.09% | 1,211 | 1,021 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 8,641 | 8,559 | 99.23% | 99.43% | -0.20 |
| PayPal Declined, Revoked, Payer Issue | 41 | 29 | 0.47% | 0.34% | +0.13 |
| Expired, Invalid, Closed Card, No Account | 5 | 0 | 0.06% | 0.00% | +0.06 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 15 | 10 | 0.17% | 0.12% | +0.06 |
| Fraud, Lost/Stolen Card, Security | 4 | 8 | 0.05% | 0.09% | -0.05 |
| CVV/CVC Mismatch | 0 | 1 | 0.00% | 0.01% | -0.01 |
| Gateway Rejected, Risk Threshold | 1 | 0 | 0.01% | 0.00% | +0.01 |
| Call Issuer, Voice Auth Required | 1 | 1 | 0.01% | 0.01% | +0.00 |

**Root Cause:** Klarna + Adyen

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| DE | High (>92%) | 8,608 | 8,708 | +1.2% | Stable |
| GB | High (>92%) | 8,125 | 9,915 | +22.0% | Stable |
| FR | High (>92%) | 7,408 | 6,547 | -11.6% | Stable |
| AU | High (>92%) | 2,828 | 2,930 | +3.6% | Stable |
| NL | Medium (>85%) | 1,580 | 1,604 | +1.5% | Stable |
| DK | High (>92%) | 1,457 | 1,228 | -15.7% | Stable |
| SE | Medium (>85%) | 1,412 | 1,296 | -8.2% | Stable |
| IE | High (>92%) | 1,282 | 1,394 | +8.7% | Stable |
| BE | Medium (>85%) | 1,081 | 1,070 | -1.0% | Stable |
| NO | High (>92%) | 1,030 | 909 | -11.7% | Stable |
| NZ | High (>92%) | 806 | 937 | +16.3% | Stable |
| AT | High (>92%) | 699 | 543 | -22.3% | ⚠️ Volume drop |
| CH | High (>92%) | 135 | 149 | +10.4% | Stable |
| LU | High (>92%) | 63 | 84 | +33.3% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| BE | ↑ +3.72% | BcmcMobile -6.6% | Adyen -6.7% | → Stable | BcmcMobile + Adyen |
| DE | ↑ +4.35% | Klarna -10.8% | Adyen -9.2% | → Stable | Klarna + Adyen |

---

*Report: 2026-04-22*
