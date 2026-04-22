# Reactivation Investigation: HF-INTL 2026-W15

**Metric:** Reactivation Rate  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 91.47% → 91.23% (-0.26%)  
**Volume:** 46,003 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** HF-INTL Reactivation Rate declined slightly from 91.47% to 91.23% (-0.24pp) in W16, a statistically non-significant change within normal operating variance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (90.03%-91.47%) | -0.24pp | ✅ |
| L1: Country Breakdown | 4 countries exceed ±2.5% threshold (NZ, NO, CH, LU) | Mixed | ⚠️ |
| L1: Dimension Scan | All PaymentMethods within normal variance | <1.35pp | ✅ |
| L2: Deep-Dive Analysis | Low-volume countries driving flags | Small volumes | ⚠️ |
| Mix Shift | All countries stable despite volume changes | No impact | ✅ |

**Key Findings:**
- NZ declined -3.09pp (80.60% from 83.17%) driven by PayPal performance drop of -8.14% and increased "Expired, Invalid, Closed Card, No Account" declines (+1.89pp)
- NO declined -2.72pp (88.85% from 91.34%) with Credit Card down -4.05% and "Expired, Invalid, Closed Card, No Account" declines increasing +3.00pp
- CH and LU showed positive movements (+5.31pp and +21.32% respectively) but volumes are minimal (49 and 34 orders) making these statistically unreliable
- NO experienced significant volume growth (+108.7%, from 404 to 843 orders) which may have introduced lower-quality transaction mix
- Global PaymentMethod performance remained stable with all methods showing <1.35pp change

**Action:** Monitor — The overall decline is not statistically significant and falls within the 8-week historical range. Continue monitoring NZ and NO for sustained declines in subsequent weeks before escalating.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 91.23% | 46,003 | -0.26% |
| 2026-W15 | 91.47% | 41,652 | +0.60% ← REPORTED CHANGE |
| 2026-W14 | 90.92% | 32,555 | +0.99% |
| 2026-W13 | 90.03% | 43,179 | -0.19% |
| 2026-W12 | 90.2% | 42,003 | -0.20% |
| 2026-W11 | 90.38% | 45,133 | +0.33% |
| 2026-W10 | 90.08% | 48,534 | -0.90% |
| 2026-W09 | 90.9% | 55,010 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| NZ | 80.60% | 83.17% | -3.09% | 1,299 | ⚠️ |
| NO | 88.85% | 91.34% | -2.72% | 843 | ⚠️ |
| DE | 97.56% | 97.07% | +0.51% | 7,103 |  |
| FR | 88.98% | 88.27% | +0.81% | 5,644 |  |
| GB | 91.05% | 89.58% | +1.65% | 14,090 |  |
| CH | 87.76% | 83.33% | +5.31% | 49 | ⚠️ |
| LU | 97.06% | 80.00% | +21.32% | 34 | ⚠️ |

**Countries exceeding ±2.5% threshold:** NZ, NO, CH, LU

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 96.47% | 97.06% | -0.61% | 3,736 |  |
| Paypal | 97.09% | 96.61% | +0.49% | 11,473 |  |
| Credit Card | 86.79% | 86.15% | +0.74% | 19,350 |  |
| Apple Pay | 92.51% | 91.28% | +1.35% | 7,093 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: NZ Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Paypal | 88.46% | 96.30% | -8.14% | 52 | 54 | ⚠️ |
| Credit Card | 80.36% | 83.17% | -3.38% | 1,227 | 1,028 |  |
| Apple Pay | 75.00% | 52.17% | +43.75% | 20 | 23 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 1,113 | 977 | 85.68% | 88.42% | -2.73 |
| Expired, Invalid, Closed Card, No Account | 148 | 105 | 11.39% | 9.50% | +1.89 |
| Blocked, Restricted, Not Permitted | 32 | 20 | 2.46% | 1.81% | +0.65 |
| CVV/CVC Mismatch | 3 | 0 | 0.23% | 0.00% | +0.23 |
| PayPal Declined, Revoked, Payer Issue | 3 | 3 | 0.23% | 0.27% | -0.04 |

**Root Cause:** Paypal + Others

---

## L2: NO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Credit Card | 86.51% | 90.16% | -4.05% | 682 | 315 |  |
| Apple Pay | 97.85% | 96.77% | +1.11% | 93 | 62 |  |
| Paypal | 100.00% | 92.59% | +8.00% | 68 | 27 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Expired, Invalid, Closed Card, No Account | 67 | 20 | 7.95% | 4.95% | +3.00 |
| Others | 760 | 375 | 90.15% | 92.82% | -2.67 |
| 3DS Authentication Failed/Required | 14 | 4 | 1.66% | 0.99% | +0.67 |
| Blocked, Restricted, Not Permitted | 1 | 3 | 0.12% | 0.74% | -0.62 |
| PayPal Declined, Revoked, Payer Issue | 0 | 1 | 0.00% | 0.25% | -0.25 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 1 | 1 | 0.12% | 0.25% | -0.13 |

**Root Cause:** Paypal + Expired,

---

## L2: CH Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Credit Card | 86.11% | 90.00% | -4.32% | 36 | 20 |  |
| Paypal | 83.33% | 77.78% | +7.14% | 6 | 9 | ⚠️ |
| Apple Pay | 100.00% | 76.92% | +30.00% | 7 | 13 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 43 | 41 | 87.76% | 97.62% | -9.86 |
| Expired, Invalid, Closed Card, No Account | 4 | 1 | 8.16% | 2.38% | +5.78 |
| Blocked, Restricted, Not Permitted | 1 | 0 | 2.04% | 0.00% | +2.04 |
| PayPal Declined, Revoked, Payer Issue | 1 | 0 | 2.04% | 0.00% | +2.04 |

**Root Cause:** Paypal + Others

---

## L2: LU Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Others | 100.00% | 0.00% | +0.00% | 3 | 0 |  |
| Apple Pay | 90.00% | 100.00% | -10.00% | 10 | 2 | ⚠️ |
| Paypal | 100.00% | 100.00% | +0.00% | 6 | 5 |  |
| Credit Card | 100.00% | 72.22% | +38.46% | 15 | 18 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 34 | 20 | 100.00% | 80.00% | +20.00 |
| Expired, Invalid, Closed Card, No Account | 0 | 4 | 0.00% | 16.00% | -16.00 |
| Blocked, Restricted, Not Permitted | 0 | 1 | 0.00% | 4.00% | -4.00 |

**Root Cause:** Apple + Others

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | Medium (>85%) | 9,382 | 14,090 | +50.2% | Stable |
| FR | Medium (>85%) | 5,770 | 5,644 | -2.2% | Stable |
| DE | High (>92%) | 5,634 | 7,103 | +26.1% | Stable |
| AU | Medium (>85%) | 3,589 | 4,223 | +17.7% | Stable |
| NL | High (>92%) | 2,174 | 2,437 | +12.1% | Stable |
| BE | High (>92%) | 1,215 | 1,317 | +8.4% | Stable |
| SE | Medium (>85%) | 1,181 | 1,769 | +49.8% | Stable |
| DK | High (>92%) | 1,138 | 1,776 | +56.1% | Stable |
| NZ | Low (>85%) | 1,105 | 1,299 | +17.6% | Stable |
| IE | Medium (>85%) | 569 | 613 | +7.7% | Stable |
| NO | Medium (>85%) | 404 | 843 | +108.7% | Stable |
| AT | High (>92%) | 325 | 455 | +40.0% | Stable |
| CH | Low (>85%) | 42 | 49 | +16.7% | Stable |
| LU | Low (>85%) | 25 | 34 | +36.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| NZ | ↓ -3.09% | Paypal -8.1% | → Stable | Others -2.73pp | Paypal + Others |
| NO | ↓ -2.72% | Paypal +8.0% | → Stable | Expired, Invalid, Closed Card, No Account +3.00pp | Paypal + Expired, |
| CH | ↑ +5.31% | Paypal +7.1% | → Stable | Others -9.86pp | Paypal + Others |
| LU | ↑ +21.32% | Apple Pay -10.0% | → Stable | Others +20.00pp | Apple + Others |

---

*Report: 2026-04-22*
