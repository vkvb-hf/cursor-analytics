# PCAR Investigation: HF-INTL 2026-W20

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 92.95% → 93.5% (+0.59%)  
**Volume:** 31,674 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate for HF-INTL improved slightly from 92.95% to 93.5% (+0.59pp) in W20, though this change is not statistically significant and remains below the 8-week average performance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate below W13-W17 levels (95-97%) | +0.59% | ⚠️ |
| L1: Country Breakdown | 2 countries exceed ±2.5% threshold | CH -4.48%, BE +4.77% | ⚠️ |
| L1: Payment Method | "Others" method shows volatility | +10.50% | ⚠️ |
| L2: CH Deep-Dive | CreditCard via ProcessOut declining | -10.26% | ⚠️ |
| L2: BE Deep-Dive | BcmcMobile via Adyen improving | +6.95% | ✅ |
| Mix Shift | NO volume dropped significantly | -31.3% volume | ⚠️ |

**Key Findings:**
- CH experienced a -4.48pp decline driven by CreditCard payments via ProcessOut dropping from 98.44% to 88.33% (-10.26pp), with decline reasons categorized as "Others"
- BE showed strong improvement (+4.77pp) primarily from BcmcMobile via Adyen recovering from 72.68% to 77.73% (+6.95pp)
- The overall rate of 93.5% remains well below the W16-W17 peak of ~97%, indicating a broader downward trend since W17
- NO experienced a major volume shift (-31.3%), though this high-AR country's reduced share may limit positive mix effects
- "Others" payment method improved significantly (+10.50pp) but operates at a low baseline rate of 74.81%

**Action:** Monitor - The reported +0.59pp improvement is not significant. Continue monitoring CH/ProcessOut CreditCard performance and investigate the persistent "Others" decline reasons affecting CH. No immediate escalation required unless CH degradation continues next week.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W20 | 93.5% | 31,674 | +0.59% ← REPORTED CHANGE |
| 2026-W19 | 92.95% | 33,686 | -1.31% |
| 2026-W18 | 94.18% | 34,181 | -2.58% |
| 2026-W17 | 96.67% | 34,080 | -0.47% |
| 2026-W16 | 97.13% | 37,314 | +1.05% |
| 2026-W15 | 96.12% | 36,514 | +0.13% |
| 2026-W14 | 96.0% | 31,465 | +0.83% |
| 2026-W13 | 95.21% | 39,598 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CH | 93.28% | 97.66% | -4.48% | 134 | ⚠️ |
| LU | 94.29% | 96.49% | -2.29% | 70 |  |
| GB | 97.13% | 97.38% | -0.26% | 7,532 |  |
| FR | 93.57% | 93.12% | +0.48% | 6,690 |  |
| DE | 90.67% | 88.89% | +2.01% | 6,914 |  |
| BE | 85.63% | 81.72% | +4.77% | 1,127 | ⚠️ |

**Countries exceeding ±2.5% threshold:** CH, BE

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Credit Card | 93.34% | 93.57% | -0.24% | 11,175 |  |
| Apple Pay | 97.88% | 98.01% | -0.13% | 10,553 |  |
| Paypal | 98.09% | 98.22% | -0.13% | 6,071 |  |
| Others | 74.81% | 67.71% | +10.50% | 3,875 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: CH Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Twint | 50.00% | 0.00% | +0.00% | 2 | 0 |  |
| CreditCard | 88.33% | 98.44% | -10.26% | 60 | 64 | ⚠️ |
| ApplePay | 98.04% | 97.62% | +0.43% | 51 | 42 |  |
| Paypal | 100.00% | 95.45% | +4.76% | 21 | 22 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Adyen | 50.00% | 100.00% | -50.00% | 2 | 1 | ⚠️ |
| ProcessOut | 88.33% | 98.41% | -10.24% | 60 | 63 | ⚠️ |
| Braintree | 98.61% | 96.88% | +1.79% | 72 | 64 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 134 | 126 | 100.00% | 98.44% | +1.56 |
| Fraud, Lost/Stolen Card, Security | 0 | 1 | 0.00% | 0.78% | -0.78 |
| PayPal Declined, Revoked, Payer Issue | 0 | 1 | 0.00% | 0.78% | -0.78 |

**Root Cause:** CreditCard + Adyen + Others

---

## L2: BE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Sepa | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| ApplePay | 98.05% | 98.04% | +0.01% | 154 | 153 |  |
| CreditCard | 97.67% | 97.06% | +0.63% | 215 | 204 |  |
| Paypal | 98.59% | 95.77% | +2.94% | 71 | 71 |  |
| BcmcMobile | 77.73% | 72.68% | +6.95% | 687 | 732 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| ProcessOut | 97.67% | 97.04% | +0.65% | 215 | 203 |  |
| Braintree | 98.22% | 97.32% | +0.93% | 225 | 224 |  |
| Adyen | 77.73% | 72.71% | +6.90% | 687 | 733 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Fraud, Lost/Stolen Card, Security | 3 | 0 | 0.27% | 0.00% | +0.27 |
| PayPal Declined, Revoked, Payer Issue | 0 | 2 | 0.00% | 0.17% | -0.17 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 1 | 2 | 0.09% | 0.17% | -0.08 |
| Others | 1,122 | 1,155 | 99.56% | 99.57% | -0.01 |
| 3DS Authentication Failed/Required | 1 | 1 | 0.09% | 0.09% | +0.00 |

**Root Cause:** BcmcMobile + Adyen

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | High (>92%) | 8,717 | 7,532 | -13.6% | Stable |
| DE | Medium (>85%) | 7,281 | 6,914 | -5.0% | Stable |
| FR | High (>92%) | 7,051 | 6,690 | -5.1% | Stable |
| AU | High (>92%) | 2,631 | 2,992 | +13.7% | Stable |
| NL | Medium (>85%) | 1,724 | 1,508 | -12.5% | Stable |
| IE | High (>92%) | 1,187 | 1,315 | +10.8% | Stable |
| BE | Low (>85%) | 1,160 | 1,127 | -2.8% | Stable |
| SE | Medium (>85%) | 986 | 857 | -13.1% | Stable |
| DK | High (>92%) | 934 | 892 | -4.5% | Stable |
| NZ | Medium (>85%) | 795 | 832 | +4.7% | Stable |
| NO | High (>92%) | 547 | 376 | -31.3% | ⚠️ Major mix shift |
| AT | High (>92%) | 488 | 435 | -10.9% | Stable |
| CH | High (>92%) | 128 | 134 | +4.7% | Stable |
| LU | High (>92%) | 57 | 70 | +22.8% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| CH | ↓ -4.48% | CreditCard -10.3% | Adyen -50.0% | Others +1.56pp | CreditCard + Adyen + Others |
| BE | ↑ +4.77% | BcmcMobile +7.0% | Adyen +6.9% | → Stable | BcmcMobile + Adyen |

---

*Report: 2026-05-19*
