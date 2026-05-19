# Reactivation Investigation: HF-INTL 2026-W20

**Metric:** Reactivation Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 90.32% → 89.55% (-0.85%)  
**Volume:** 36,895 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** HF-INTL Reactivation Rate declined from 90.32% to 89.55% (-0.85%) in W20, a statistically not significant change within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate decline within historical variance (range: 90.03%-91.47%) | -0.85% | ✅ |
| L1: Country Scan | DK exceeded ±2.5% threshold | -2.68% | ⚠️ |
| L1: Dimension Scan | No PaymentMethod or PaymentProvider exceeded threshold | -1.50% max | ✅ |
| L2: DK Deep-Dive | Paypal in DK showed significant decline | -8.64% | ⚠️ |
| Mix Shift | FR volume dropped 21.3%; no major AR impact | Stable | ✅ |

**Key Findings:**
- DK is the only country exceeding the ±2.5% threshold with a -2.68% decline (89.26% vs 91.72%), though on low volume (1,071 orders)
- Within DK, Paypal reactivation dropped significantly from 97.30% to 88.89% (-8.64%), but volume is minimal (36 orders)
- DK decline reasons show "Expired, Invalid, Closed Card, No Account" increased by +1.95pp (from 3.47% to 5.42%)
- FR experienced a notable volume drop of -21.3% (6,932 → 5,457) but rate decline of -1.46% remains within threshold
- Positive performance in SE (+1.95%), CH (+2.15%), and NO (+1.55%) partially offset declines

**Action:** Monitor — The overall change is not statistically significant, and the DK anomaly is driven by very low Paypal volume (36 orders). Continue monitoring DK Paypal performance and "Expired Card" decline reasons in the next reporting period.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W20 | 89.55% | 36,895 | -0.85% ← REPORTED CHANGE |
| 2026-W19 | 90.32% | 40,935 | - |
| 2026-W18 | 90.32% | 43,663 | -0.46% |
| 2026-W17 | 90.74% | 40,613 | -0.54% |
| 2026-W16 | 91.23% | 46,003 | -0.26% |
| 2026-W15 | 91.47% | 41,652 | +0.60% |
| 2026-W14 | 90.92% | 32,555 | +0.99% |
| 2026-W13 | 90.03% | 43,179 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| DK | 89.26% | 91.72% | -2.68% | 1,071 | ⚠️ |
| FR | 86.15% | 87.42% | -1.46% | 5,457 |  |
| GB | 88.86% | 90.11% | -1.39% | 11,271 |  |
| NO | 87.44% | 86.11% | +1.55% | 430 |  |
| SE | 89.73% | 88.01% | +1.95% | 1,022 |  |
| CH | 92.13% | 90.20% | +2.15% | 89 |  |

**Countries exceeding ±2.5% threshold:** DK

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 84.15% | 85.43% | -1.50% | 17,278 |  |
| Apple Pay | 89.38% | 89.93% | -0.62% | 5,960 |  |
| Paypal | 96.19% | 96.34% | -0.16% | 9,991 |  |
| Others | 97.22% | 97.32% | -0.11% | 3,666 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: DK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Paypal | 88.89% | 97.30% | -8.64% | 36 | 37 | ⚠️ |
| Credit Card | 88.00% | 90.94% | -3.23% | 850 | 938 |  |
| Others | 100.00% | 100.00% | +0.00% | 4 | 5 |  |
| Apple Pay | 95.03% | 94.09% | +1.00% | 181 | 203 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 971 | 1,100 | 90.66% | 92.98% | -2.32 |
| Expired, Invalid, Closed Card, No Account | 58 | 41 | 5.42% | 3.47% | +1.95 |
| PayPal Declined, Revoked, Payer Issue | 4 | 1 | 0.37% | 0.08% | +0.29 |
| Blocked, Restricted, Not Permitted | 28 | 28 | 2.61% | 2.37% | +0.25 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 0 | 1 | 0.00% | 0.08% | -0.08 |
| Fraud, Lost/Stolen Card, Security | 1 | 2 | 0.09% | 0.17% | -0.08 |
| Call Issuer, Voice Auth Required | 3 | 4 | 0.28% | 0.34% | -0.06 |
| 3DS Authentication Failed/Required | 6 | 6 | 0.56% | 0.51% | +0.05 |

**Root Cause:** Paypal + Others

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | Medium (>85%) | 13,786 | 11,271 | -18.2% | Stable |
| FR | Medium (>85%) | 6,932 | 5,457 | -21.3% | ⚠️ Volume drop |
| DE | High (>92%) | 6,150 | 5,946 | -3.3% | Stable |
| AU | Low (>85%) | 4,052 | 4,747 | +17.2% | Stable |
| NL | High (>92%) | 3,135 | 2,676 | -14.6% | Stable |
| BE | High (>92%) | 1,627 | 1,619 | -0.5% | Stable |
| NZ | Low (>85%) | 1,209 | 1,441 | +19.2% | Stable |
| DK | Medium (>85%) | 1,183 | 1,071 | -9.5% | Stable |
| SE | Medium (>85%) | 1,151 | 1,022 | -11.2% | Stable |
| IE | Medium (>85%) | 741 | 746 | +0.7% | Stable |
| NO | Medium (>85%) | 511 | 430 | -15.9% | Stable |
| AT | High (>92%) | 382 | 353 | -7.6% | Stable |
| CH | Medium (>85%) | 51 | 89 | +74.5% | Stable |
| LU | Medium (>85%) | 24 | 27 | +12.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| DK | ↓ -2.68% | Paypal -8.6% | → Stable | Others -2.32pp | Paypal + Others |

---

*Report: 2026-05-19*
