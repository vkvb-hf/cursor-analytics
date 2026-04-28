# Reactivation Investigation: HF-INTL 2026-W17

**Metric:** Reactivation Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 91.23% → 90.74% (-0.54%)  
**Volume:** 40,613 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** HF-INTL Reactivation Rate declined by -0.54% (from 91.23% to 90.74%) in W17, a statistically non-significant change within normal weekly fluctuation range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (90.03%-91.47%) | -0.54% | ✅ |
| L1: Country Scan | 2 countries exceed ±2.5% threshold (LU, NO) | LU -8.33%, NO -3.16% | ⚠️ |
| L1: Dimension Scan | No payment methods exceed threshold | Max -0.70% | ✅ |
| L2: LU Deep-Dive | Credit Card drop with low volume (16 orders) | -18.75% | ⚠️ |
| L2: NO Deep-Dive | PayPal decline with low volume (41 orders) | -7.41% | ⚠️ |
| Mix Shift | Volume drops in GB (-25%), DE (-21.4%), NO (-29.8%) | High-performing markets down | ⚠️ |

**Key Findings:**
- LU experienced -8.33% decline driven by Credit Card failures (-18.75%), with "Expired, Invalid, Closed Card" decline reason increasing by +8.33pp, though total volume is minimal (36 orders)
- NO declined -3.16% primarily due to PayPal performance drop (-7.41%) and increased 3DS Authentication failures (+1.46pp)
- Significant volume reductions in high-performing markets: GB (-25.0%), DE (-21.4%), and NO (-29.8%) may be masking rate impacts
- Global payment method performance remained stable with no dimension exceeding the ±2.5% threshold
- The overall rate of 90.74% remains within the 8-week historical range (90.03%-91.47%)

**Action:** Monitor - The decline is not statistically significant and affected countries have low volumes. Continue tracking LU Credit Card and NO PayPal performance in W18 to confirm if patterns persist.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 90.74% | 40,613 | -0.54% ← REPORTED CHANGE |
| 2026-W16 | 91.23% | 46,003 | -0.26% |
| 2026-W15 | 91.47% | 41,652 | +0.60% |
| 2026-W14 | 90.92% | 32,555 | +0.99% |
| 2026-W13 | 90.03% | 43,179 | -0.19% |
| 2026-W12 | 90.2% | 42,003 | -0.20% |
| 2026-W11 | 90.38% | 45,133 | +0.33% |
| 2026-W10 | 90.08% | 48,534 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| LU | 91.67% | 100.00% | -8.33% | 36 | ⚠️ |
| NO | 86.16% | 88.97% | -3.16% | 643 | ⚠️ |
| FR | 87.20% | 88.70% | -1.69% | 5,358 |  |
| AU | 84.17% | 85.54% | -1.61% | 4,566 |  |
| GB | 89.72% | 89.32% | +0.45% | 12,670 |  |
| SE | 91.83% | 90.13% | +1.88% | 1,836 |  |
| NZ | 83.33% | 81.68% | +2.02% | 1,212 |  |
| CH | 85.42% | 83.64% | +2.13% | 48 |  |

**Countries exceeding ±2.5% threshold:** LU, NO

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 90.64% | 91.29% | -0.70% | 6,647 |  |
| Paypal | 96.63% | 97.07% | -0.45% | 11,540 |  |
| Credit Card | 85.76% | 86.09% | -0.38% | 18,596 |  |
| Others | 97.39% | 96.9% | +0.51% | 3,830 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: LU Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Credit Card | 81.25% | 100.00% | -18.75% | 16 | 21 | ⚠️ |
| Apple Pay | 100.00% | 100.00% | +0.00% | 9 | 6 |  |
| Others | 100.00% | 100.00% | +0.00% | 3 | 3 |  |
| Paypal | 100.00% | 100.00% | +0.00% | 8 | 7 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Expired, Invalid, Closed Card, No Account | 3 | 0 | 8.33% | 0.00% | +8.33 |
| Others | 33 | 37 | 91.67% | 100.00% | -8.33 |

**Root Cause:** Credit + Expired,

---

## L2: NO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Paypal | 90.24% | 97.47% | -7.41% | 41 | 79 | ⚠️ |
| Credit Card | 84.84% | 87.08% | -2.58% | 521 | 720 |  |
| Apple Pay | 92.59% | 94.87% | -2.40% | 81 | 117 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 560 | 827 | 87.09% | 90.28% | -3.19 |
| 3DS Authentication Failed/Required | 15 | 8 | 2.33% | 0.87% | +1.46 |
| Blocked, Restricted, Not Permitted | 7 | 4 | 1.09% | 0.44% | +0.65 |
| PayPal Declined, Revoked, Payer Issue | 3 | 0 | 0.47% | 0.00% | +0.47 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 4 | 3 | 0.62% | 0.33% | +0.29 |
| Expired, Invalid, Closed Card, No Account | 53 | 74 | 8.24% | 8.08% | +0.16 |
| Call Issuer, Voice Auth Required | 1 | 0 | 0.16% | 0.00% | +0.16 |

**Root Cause:** Paypal + Others

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | Medium (>85%) | 16,889 | 12,670 | -25.0% | ⚠️ Volume drop |
| DE | High (>92%) | 9,803 | 7,703 | -21.4% | ⚠️ Volume drop |
| FR | Medium (>85%) | 4,681 | 5,358 | +14.5% | Stable |
| AU | Medium (>85%) | 3,990 | 4,566 | +14.4% | Stable |
| NL | High (>92%) | 2,512 | 2,251 | -10.4% | Stable |
| SE | Medium (>85%) | 1,520 | 1,836 | +20.8% | Stable |
| BE | High (>92%) | 1,453 | 1,451 | -0.1% | Stable |
| NZ | Low (>85%) | 1,392 | 1,212 | -12.9% | Stable |
| DK | High (>92%) | 1,352 | 1,559 | +15.3% | Stable |
| IE | Medium (>85%) | 989 | 816 | -17.5% | Stable |
| NO | Medium (>85%) | 916 | 643 | -29.8% | ⚠️ Volume drop |
| AT | High (>92%) | 414 | 464 | +12.1% | Stable |
| CH | Low (>85%) | 55 | 48 | -12.7% | Stable |
| LU | High (>92%) | 37 | 36 | -2.7% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| LU | ↓ -8.33% | Credit Card -18.8% | → Stable | Expired, Invalid, Closed Card, No Account +8.33pp | Credit + Expired, |
| NO | ↓ -3.16% | Paypal -7.4% | → Stable | Others -3.19pp | Paypal + Others |

---

*Report: 2026-04-28*
