# PCAR Investigation: HF-INTL 2026-W17

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 97.13% → 96.67% (-0.47%)  
**Volume:** 34,080 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate for HF-INTL declined by -0.47pp (97.13% → 96.67%) in 2026-W17, with 34,080 orders processed; this change is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 8-Week Trend | Rate within historical range (95.21%-97.31%) | -0.47pp | ✅ |
| Country Breakdown | BE declined -13.63pp, CH improved +5.71pp | ±2.5% threshold exceeded | ⚠️ |
| Payment Method | All methods stable (<1% change) | -0.80pp max (Others) | ✅ |
| Payment Provider | No significant changes flagged | - | ✅ |
| Mix Shift | NZ -31.3%, NO -31.0% volume drops | Major shifts detected | ⚠️ |

**Key Findings:**
- BE experienced a significant decline of -13.63pp (93.64% → 80.88%), driven primarily by BcmcMobile at 69.71% approval rate with 647 orders processed via Adyen
- CH showed improvement of +5.71pp (93.96% → 99.32%), with ApplePay +6.87pp and ProcessOut +6.94pp, accompanied by reduced fraud-related declines (-1.34pp)
- NZ and NO experienced major volume drops (-31.3% and -31.0% respectively), though both remain in the High AR tier
- BE decline reasons show 99.54% categorized as "Others" with no clear pattern in specific decline codes, requiring further investigation
- Overall rate remains within the 8-week historical range of 95.21%-97.31%

**Action:** Investigate — Priority focus on BE/BcmcMobile/Adyen pathway to identify root cause of -13.63pp decline; monitor NZ and NO volume recovery

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 96.67% | 34,080 | -0.47% ← REPORTED CHANGE |
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
| BE | 80.88% | 93.64% | -13.63% | 1,088 | ⚠️ |
| FR | 97.15% | 98.18% | -1.05% | 5,901 |  |
| AU | 97.64% | 98.46% | -0.83% | 3,012 |  |
| DE | 97.24% | 96.93% | +0.31% | 8,900 |  |
| SE | 91.50% | 89.81% | +1.87% | 1,070 |  |
| LU | 100.00% | 97.62% | +2.44% | 62 |  |
| CH | 99.32% | 93.96% | +5.71% | 148 | ⚠️ |

**Countries exceeding ±2.5% threshold:** BE, CH

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | 81.32% | 81.98% | -0.80% | 2,372 |  |
| Credit Card | 97.98% | 98.36% | -0.39% | 12,020 |  |
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
| Paypal | 94.37% | 97.60% | -3.31% | 71 | 125 |  |
| BcmcMobile | 69.71% | 71.43% | -2.41% | 647 | 154 |  |
| ApplePay | 95.97% | 96.25% | -0.29% | 124 | 240 |  |
| CreditCard | 98.78% | 97.82% | +0.97% | 245 | 551 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Adyen | 69.85% | 71.43% | -2.22% | 650 | 154 |  |
| Braintree | 95.38% | 96.71% | -1.37% | 195 | 365 |  |
| ProcessOut | 98.77% | 97.82% | +0.96% | 243 | 551 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 1,083 | 1,062 | 99.54% | 99.25% | +0.29 |
| Fraud, Lost/Stolen Card, Security | 2 | 4 | 0.18% | 0.37% | -0.19 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 1 | 2 | 0.09% | 0.19% | -0.10 |
| CVV/CVC Mismatch | 0 | 1 | 0.00% | 0.09% | -0.09 |
| PayPal Declined, Revoked, Payer Issue | 2 | 1 | 0.18% | 0.09% | +0.09 |

**Root Cause:** Requires investigation

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
| BE | ↓ -13.63% | → Stable | → Stable | → Stable | Requires investigation |
| CH | ↑ +5.71% | ApplePay +6.9% | ProcessOut +6.9% | Fraud, Lost/Stolen Card, Security -1.34pp | ApplePay + ProcessOut + Fraud, |

---

*Report: 2026-04-28*
