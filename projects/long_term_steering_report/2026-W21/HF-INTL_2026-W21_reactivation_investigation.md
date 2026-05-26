# Reactivation Investigation: HF-INTL 2026-W21

**Metric:** Reactivation Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 89.55% → 90.58% (+1.15%)  
**Volume:** 33,970 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** HF-INTL Reactivation Rate improved from 89.55% to 90.58% (+1.15%) in 2026-W21, representing a significant positive change on 33,970 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 8-Week Trend | Rate recovering from W20 dip | +1.15% | ✅ |
| Country Breakdown | 5 countries exceed ±2.5% threshold | Mixed | ⚠️ |
| CH Deep-Dive | Major rate decline with low volume | -12.25% | ⚠️ |
| AU Deep-Dive | Apple Pay driving improvement | +3.39% | ✅ |
| DK Deep-Dive | PayPal improvement | +3.65% | ✅ |
| LU Deep-Dive | Credit Card recovery, low volume | +4.63% | ✅ |
| Mix Shift | GB volume down 24.7%, CH down 47.2% | Volume shift | ⚠️ |

**Key Findings:**
- CH experienced a significant rate decline (-12.25%) driven by Credit Card payment method (-19.03%), with "Expired, Invalid, Closed Card, No Account" decline reasons increasing by +4.02pp; however, volume is minimal (47 orders)
- AU showed strong improvement (+3.39%) primarily driven by Apple Pay performance surging from 49.66% to 68.12% (+37.15%)
- GB volume dropped significantly (-24.7%, from 11,271 to 8,483 orders) while maintaining stable rate performance (+1.08%)
- DK and LU both improved through PayPal-related gains, though LU has very low volume (32 orders)
- The overall improvement reverses the -0.85% decline seen in W20, bringing rates closer to the W19 baseline of 90.32%

**Action:** Monitor – The overall improvement is positive and the primary concern (CH decline) involves minimal volume. Continue tracking GB volume trends and CH Credit Card performance.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W21 | 90.58% | 33,970 | +1.15% ← REPORTED CHANGE |
| 2026-W20 | 89.55% | 36,895 | -0.85% |
| 2026-W19 | 90.32% | 40,935 | - |
| 2026-W18 | 90.32% | 43,663 | -0.46% |
| 2026-W17 | 90.74% | 40,613 | -0.54% |
| 2026-W16 | 91.23% | 46,003 | -0.26% |
| 2026-W15 | 91.47% | 41,652 | +0.60% |
| 2026-W14 | 90.92% | 32,555 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CH | 80.85% | 92.13% | -12.25% | 47 | ⚠️ |
| GB | 89.81% | 88.86% | +1.08% | 8,483 |  |
| BE | 94.13% | 91.91% | +2.41% | 1,873 |  |
| AU | 86.55% | 83.72% | +3.39% | 4,350 | ⚠️ |
| DK | 92.52% | 89.26% | +3.65% | 869 | ⚠️ |
| LU | 96.88% | 92.59% | +4.63% | 32 | ⚠️ |
| NZ | 83.86% | 79.25% | +5.81% | 1,623 | ⚠️ |

**Countries exceeding ±2.5% threshold:** CH, AU, DK, LU, NZ

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 96.04% | 96.19% | -0.15% | 9,366 |  |
| Others | 97.79% | 97.22% | +0.59% | 3,576 |  |
| Apple Pay | 90.46% | 89.38% | +1.21% | 5,053 |  |
| Credit Card | 85.8% | 84.15% | +1.96% | 15,975 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: CH Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Others | 50.00% | 0.00% | +0.00% | 2 | 0 |  |
| Credit Card | 73.33% | 90.57% | -19.03% | 30 | 53 | ⚠️ |
| Paypal | 100.00% | 95.83% | +4.35% | 8 | 24 |  |
| Apple Pay | 100.00% | 91.67% | +9.09% | 7 | 12 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Expired, Invalid, Closed Card, No Account | 4 | 4 | 8.51% | 4.49% | +4.02 |
| Others | 43 | 84 | 91.49% | 94.38% | -2.89 |
| PayPal Declined, Revoked, Payer Issue | 0 | 1 | 0.00% | 1.12% | -1.12 |

**Root Cause:** Credit + Expired,

---

## L2: AU Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Others | 0.00% | 0.00% | +0.00% | 0 | 1 |  |
| Paypal | 94.74% | 93.87% | +0.93% | 1,141 | 1,223 |  |
| Credit Card | 84.34% | 81.56% | +3.40% | 3,071 | 3,374 |  |
| Apple Pay | 68.12% | 49.66% | +37.15% | 138 | 149 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 3,906 | 4,187 | 89.79% | 88.20% | +1.59 |
| Expired, Invalid, Closed Card, No Account | 318 | 403 | 7.31% | 8.49% | -1.18 |
| PayPal Declined, Revoked, Payer Issue | 52 | 68 | 1.20% | 1.43% | -0.24 |
| CVV/CVC Mismatch | 1 | 6 | 0.02% | 0.13% | -0.10 |
| Blocked, Restricted, Not Permitted | 69 | 79 | 1.59% | 1.66% | -0.08 |
| Fraud, Lost/Stolen Card, Security | 4 | 1 | 0.09% | 0.02% | +0.07 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 0 | 2 | 0.00% | 0.04% | -0.04 |
| 3DS Authentication Failed/Required | 0 | 1 | 0.00% | 0.02% | -0.02 |

**Root Cause:** Apple + Others

---

## L2: DK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Others | 100.00% | 100.00% | +0.00% | 5 | 4 |  |
| Apple Pay | 96.69% | 95.03% | +1.75% | 151 | 181 |  |
| Credit Card | 91.03% | 88.00% | +3.44% | 669 | 850 |  |
| Paypal | 100.00% | 88.89% | +12.50% | 44 | 36 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 813 | 971 | 93.56% | 90.66% | +2.89 |
| Expired, Invalid, Closed Card, No Account | 26 | 58 | 2.99% | 5.42% | -2.42 |
| PayPal Declined, Revoked, Payer Issue | 0 | 4 | 0.00% | 0.37% | -0.37 |
| 3DS Authentication Failed/Required | 8 | 6 | 0.92% | 0.56% | +0.36 |
| Blocked, Restricted, Not Permitted | 21 | 28 | 2.42% | 2.61% | -0.20 |
| Call Issuer, Voice Auth Required | 1 | 3 | 0.12% | 0.28% | -0.17 |
| Fraud, Lost/Stolen Card, Security | 0 | 1 | 0.00% | 0.09% | -0.09 |

**Root Cause:** Paypal + Others

---

## L2: LU Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Paypal | 87.50% | 100.00% | -12.50% | 8 | 7 | ⚠️ |
| Apple Pay | 100.00% | 100.00% | +0.00% | 5 | 4 |  |
| Others | 100.00% | 100.00% | +0.00% | 2 | 3 |  |
| Credit Card | 100.00% | 84.62% | +18.18% | 17 | 13 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 32 | 25 | 100.00% | 92.59% | +7.41 |
| Blocked, Restricted, Not Permitted | 0 | 1 | 0.00% | 3.70% | -3.70 |
| Expired, Invalid, Closed Card, No Account | 0 | 1 | 0.00% | 3.70% | -3.70 |

**Root Cause:** Paypal + Others

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | Medium (>85%) | 11,271 | 8,483 | -24.7% | ⚠️ Volume drop |
| DE | High (>92%) | 5,946 | 5,737 | -3.5% | Stable |
| FR | Medium (>85%) | 5,457 | 5,528 | +1.3% | Stable |
| AU | Low (>85%) | 4,747 | 4,350 | -8.4% | Stable |
| NL | High (>92%) | 2,676 | 2,497 | -6.7% | Stable |
| BE | Medium (>85%) | 1,619 | 1,873 | +15.7% | Stable |
| NZ | Low (>85%) | 1,441 | 1,623 | +12.6% | Stable |
| DK | Medium (>85%) | 1,071 | 869 | -18.9% | Stable |
| SE | Medium (>85%) | 1,022 | 967 | -5.4% | Stable |
| IE | Medium (>85%) | 746 | 868 | +16.4% | Stable |
| NO | Medium (>85%) | 430 | 644 | +49.8% | Stable |
| AT | High (>92%) | 353 | 452 | +28.0% | Stable |
| CH | High (>92%) | 89 | 47 | -47.2% | ⚠️ Major mix shift |
| LU | High (>92%) | 27 | 32 | +18.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| CH | ↓ -12.25% | Credit Card -19.0% | → Stable | Expired, Invalid, Closed Card, No Account +4.02pp | Credit + Expired, |
| AU | ↑ +3.39% | Apple Pay +37.2% | → Stable | Others +1.59pp | Apple + Others |
| DK | ↑ +3.65% | Paypal +12.5% | → Stable | Others +2.89pp | Paypal + Others |
| LU | ↑ +4.63% | Paypal -12.5% | → Stable | Others +7.41pp | Paypal + Others |

---

*Report: 2026-05-26*
