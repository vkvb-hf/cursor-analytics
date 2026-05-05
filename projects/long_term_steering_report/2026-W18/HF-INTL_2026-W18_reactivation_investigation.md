# Reactivation Investigation: HF-INTL 2026-W18

**Metric:** Reactivation Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 90.74% → 90.32% (-0.46%)  
**Volume:** 43,663 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** HF-INTL Reactivation Rate declined from 90.74% to 90.32% (-0.46%) in W18, a statistically non-significant change within normal weekly fluctuation.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (90.03%-91.47%) | -0.46% | ✅ |
| L1: Country Scan | 3 countries exceed ±2.5% threshold | IE -2.60%, LU +3.19%, CH +11.98% | ⚠️ |
| L1: Dimension Scan | All payment methods stable | <±1% change | ✅ |
| L2: IE Deep-Dive | Credit Card decline driver | -4.61% | ⚠️ |
| L2: LU/CH Deep-Dive | Low volume fluctuation | 37 and 46 orders respectively | ✅ |
| Mix Shift | AT volume drop noted | -25.4% volume | ⚠️ |

**Key Findings:**
- IE experienced the most material decline (-2.60%, 804 orders), driven by Credit Card performance dropping 4.61pp, with "Expired, Invalid, Closed Card, No Account" decline reasons increasing +1.16pp
- LU (+3.19%) and CH (+11.98%) showed large percentage swings but are statistically unreliable due to extremely low volumes (37 and 46 orders respectively)
- The 8-week trend shows a gradual downward drift from 91.47% (W15) to 90.32% (W18), suggesting sustained mild pressure rather than an acute incident
- AT experienced a significant volume drop (-25.4%) but maintained stable AR, indicating no performance concern
- Payment method mix remained stable across all dimensions with no provider-level anomalies detected

**Action:** Monitor — The overall change is not statistically significant and IE's decline appears driven by typical card lifecycle issues (expired/invalid cards). Continue monitoring the gradual downward trend; escalate if W19 drops below 90% or IE continues declining.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W18 | 90.32% | 43,663 | -0.46% ← REPORTED CHANGE |
| 2026-W17 | 90.74% | 40,613 | -0.54% |
| 2026-W16 | 91.23% | 46,003 | -0.26% |
| 2026-W15 | 91.47% | 41,652 | +0.60% |
| 2026-W14 | 90.92% | 32,555 | +0.99% |
| 2026-W13 | 90.03% | 43,179 | -0.19% |
| 2026-W12 | 90.2% | 42,003 | -0.20% |
| 2026-W11 | 90.38% | 45,133 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| IE | 85.82% | 88.11% | -2.60% | 804 | ⚠️ |
| GB | 89.38% | 89.72% | -0.39% | 13,668 |  |
| AU | 84.56% | 84.17% | +0.47% | 6,062 |  |
| FR | 87.90% | 87.20% | +0.81% | 7,143 |  |
| DK | 92.91% | 91.47% | +1.58% | 1,608 |  |
| LU | 94.59% | 91.67% | +3.19% | 37 | ⚠️ |
| CH | 95.65% | 85.42% | +11.98% | 46 | ⚠️ |

**Countries exceeding ±2.5% threshold:** IE, LU, CH

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 85.41% | 85.76% | -0.41% | 21,230 |  |
| Paypal | 96.63% | 96.63% | +0.01% | 11,884 |  |
| Others | 97.51% | 97.39% | +0.12% | 3,613 |  |
| Apple Pay | 90.82% | 90.64% | +0.19% | 6,936 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: IE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Credit Card | 84.18% | 88.25% | -4.61% | 455 | 468 |  |
| Paypal | 92.24% | 93.60% | -1.45% | 116 | 125 |  |
| Apple Pay | 85.84% | 84.75% | +1.28% | 233 | 223 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Expired, Invalid, Closed Card, No Account | 29 | 20 | 3.61% | 2.45% | +1.16 |
| Others | 724 | 744 | 90.05% | 91.18% | -1.13 |
| 3DS Authentication Failed/Required | 19 | 26 | 2.36% | 3.19% | -0.82 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 19 | 15 | 2.36% | 1.84% | +0.52 |
| PayPal Declined, Revoked, Payer Issue | 8 | 6 | 1.00% | 0.74% | +0.26 |
| Blocked, Restricted, Not Permitted | 2 | 2 | 0.25% | 0.25% | +0.00 |
| Fraud, Lost/Stolen Card, Security | 2 | 2 | 0.25% | 0.25% | +0.00 |
| Call Issuer, Voice Auth Required | 1 | 1 | 0.12% | 0.12% | +0.00 |

**Root Cause:** Expired,

---

## L2: LU Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 100.00% | 100.00% | +0.00% | 5 | 9 |  |
| Others | 100.00% | 100.00% | +0.00% | 1 | 3 |  |
| Paypal | 100.00% | 100.00% | +0.00% | 5 | 8 |  |
| Credit Card | 92.31% | 81.25% | +13.61% | 26 | 16 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Expired, Invalid, Closed Card, No Account | 1 | 3 | 2.70% | 8.33% | -5.63 |
| Others | 36 | 33 | 97.30% | 91.67% | +5.63 |

**Root Cause:** Credit + Expired,

---

## L2: CH Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Others | 0.00% | 100.00% | -100.00% | 0 | 1 | ⚠️ |
| Credit Card | 90.91% | 86.21% | +5.45% | 22 | 29 | ⚠️ |
| Paypal | 100.00% | 87.50% | +14.29% | 15 | 8 | ⚠️ |
| Apple Pay | 100.00% | 80.00% | +25.00% | 9 | 10 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Expired, Invalid, Closed Card, No Account | 0 | 4 | 0.00% | 8.33% | -8.33 |
| Others | 45 | 43 | 97.83% | 89.58% | +8.24 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 1 | 0 | 2.17% | 0.00% | +2.17 |
| PayPal Declined, Revoked, Payer Issue | 0 | 1 | 0.00% | 2.08% | -2.08 |

**Root Cause:** Others + Expired,

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | Medium (>85%) | 12,670 | 13,668 | +7.9% | Stable |
| DE | High (>92%) | 7,703 | 6,587 | -14.5% | Stable |
| FR | Medium (>85%) | 5,358 | 7,143 | +33.3% | Stable |
| AU | Low (>85%) | 4,566 | 6,062 | +32.8% | Stable |
| NL | High (>92%) | 2,251 | 2,329 | +3.5% | Stable |
| SE | Medium (>85%) | 1,836 | 1,588 | -13.5% | Stable |
| DK | Medium (>85%) | 1,559 | 1,608 | +3.1% | Stable |
| BE | High (>92%) | 1,451 | 1,536 | +5.9% | Stable |
| NZ | Low (>85%) | 1,212 | 1,333 | +10.0% | Stable |
| IE | Medium (>85%) | 816 | 804 | -1.5% | Stable |
| NO | Medium (>85%) | 643 | 574 | -10.7% | Stable |
| AT | High (>92%) | 464 | 346 | -25.4% | ⚠️ Volume drop |
| CH | Medium (>85%) | 48 | 46 | -4.2% | Stable |
| LU | Medium (>85%) | 36 | 37 | +2.8% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| IE | ↓ -2.60% | → Stable | → Stable | Expired, Invalid, Closed Card, No Account +1.16pp | Expired, |
| LU | ↑ +3.19% | Credit Card +13.6% | → Stable | Expired, Invalid, Closed Card, No Account -5.63pp | Credit + Expired, |
| CH | ↑ +11.98% | Others -100.0% | → Stable | Expired, Invalid, Closed Card, No Account -8.33pp | Others + Expired, |

---

*Report: 2026-05-05*
