# Reactivation Investigation: HF-INTL 2026-W22

**Metric:** Reactivation Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 90.58% → 91.07% (+0.54%)  
**Volume:** 36,789 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** HF-INTL Reactivation Rate improved slightly from 90.58% to 91.07% (+0.49pp) in W22, though the change is not statistically significant given the 36,789 order volume.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (89.55%-91.47%) | +0.49pp | ✅ |
| L1: Country Scan | 4 countries exceed ±2.5% threshold | NO -7.29%, CH +11.32% | ⚠️ |
| L1: PaymentMethod | All methods stable (<2.5% change) | Max +2.23% (Apple Pay) | ✅ |
| L2: NO Deep-Dive | Credit Card decline, Expired cards spike | -8.60% CC, +4.18pp Expired | ⚠️ |
| L2: LU Deep-Dive | Low volume (33 orders), high volatility | -3.03% rate | ✅ |
| L2: FR Deep-Dive | Improvement across all payment methods | +2.68% overall | ✅ |
| L2: CH Deep-Dive | Low volume (50 orders), Credit Card improved | +11.32% rate | ✅ |

**Key Findings:**
- NO experienced a significant rate decline (-7.29pp), driven by Credit Card performance dropping 8.60pp with "Expired, Invalid, Closed Card, No Account" declines increasing +4.18pp (from 6.37% to 10.54%)
- FR showed healthy improvement (+2.68pp) with all payment methods improving, particularly PayPal (+3.33pp)
- CH and LU flagged changes are noise due to extremely low volumes (50 and 33 orders respectively)
- Volume mix shift shows BE (-20.1%), IE (-24.4%), and AT (-27.9%) with significant volume drops, though their rates remained in high/medium tiers
- Overall payment method performance stable with no systemic issues detected

**Action:** Monitor - Focus attention on NO Credit Card expired card declines; consider proactive card update reminders for NO subscribers approaching card expiration

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W22 | 91.07% | 36,789 | +0.54% ← REPORTED CHANGE |
| 2026-W21 | 90.58% | 33,970 | +1.15% |
| 2026-W20 | 89.55% | 36,895 | -0.85% |
| 2026-W19 | 90.32% | 40,935 | - |
| 2026-W18 | 90.32% | 43,663 | -0.46% |
| 2026-W17 | 90.74% | 40,613 | -0.54% |
| 2026-W16 | 91.23% | 46,003 | -0.26% |
| 2026-W15 | 91.47% | 41,652 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| NO | 81.63% | 88.04% | -7.29% | 664 | ⚠️ |
| LU | 93.94% | 96.88% | -3.03% | 33 | ⚠️ |
| DE | 96.64% | 95.87% | +0.80% | 5,655 |  |
| GB | 90.67% | 89.81% | +0.96% | 11,560 |  |
| FR | 89.01% | 86.69% | +2.68% | 5,177 | ⚠️ |
| CH | 90.00% | 80.85% | +11.32% | 50 | ⚠️ |

**Countries exceeding ±2.5% threshold:** NO, LU, FR, CH

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 97.75% | 97.79% | -0.04% | 3,558 |  |
| Paypal | 96.43% | 96.04% | +0.41% | 9,649 |  |
| Credit Card | 86.36% | 85.8% | +0.66% | 17,800 |  |
| Apple Pay | 92.48% | 90.46% | +2.23% | 5,782 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: NO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Credit Card | 78.88% | 86.30% | -8.60% | 535 | 511 | ⚠️ |
| Paypal | 93.18% | 95.92% | -2.85% | 44 | 49 |  |
| Apple Pay | 92.41% | 93.67% | -1.35% | 79 | 79 |  |
| Others | 100.00% | 100.00% | +0.00% | 6 | 5 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Expired, Invalid, Closed Card, No Account | 70 | 41 | 10.54% | 6.37% | +4.18 |
| Others | 579 | 585 | 87.20% | 90.84% | -3.64 |
| 3DS Authentication Failed/Required | 5 | 9 | 0.75% | 1.40% | -0.64 |
| Blocked, Restricted, Not Permitted | 4 | 6 | 0.60% | 0.93% | -0.33 |
| PayPal Declined, Revoked, Payer Issue | 4 | 2 | 0.60% | 0.31% | +0.29 |
| Fraud, Lost/Stolen Card, Security | 0 | 1 | 0.00% | 0.16% | -0.16 |
| Call Issuer, Voice Auth Required | 1 | 0 | 0.15% | 0.00% | +0.15 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 1 | 0 | 0.15% | 0.00% | +0.15 |

**Root Cause:** Credit + Expired,

---

## L2: LU Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Others | 0.00% | 100.00% | -100.00% | 0 | 2 | ⚠️ |
| Apple Pay | 77.78% | 100.00% | -22.22% | 9 | 5 | ⚠️ |
| Credit Card | 100.00% | 100.00% | +0.00% | 18 | 17 |  |
| Paypal | 100.00% | 87.50% | +14.29% | 6 | 8 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Expired, Invalid, Closed Card, No Account | 1 | 0 | 3.03% | 0.00% | +3.03 |
| Others | 32 | 32 | 96.97% | 100.00% | -3.03 |

**Root Cause:** Others + Expired,

---

## L2: FR Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Others | 0.00% | 0.00% | +0.00% | 1 | 0 |  |
| Credit Card | 86.49% | 84.33% | +2.56% | 3,257 | 3,402 |  |
| Apple Pay | 89.92% | 87.43% | +2.85% | 784 | 883 |  |
| Paypal | 95.68% | 92.60% | +3.33% | 1,135 | 1,243 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 4,780 | 4,993 | 92.33% | 90.32% | +2.01 |
| PayPal Declined, Revoked, Payer Issue | 34 | 74 | 0.66% | 1.34% | -0.68 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 65 | 95 | 1.26% | 1.72% | -0.46 |
| 3DS Authentication Failed/Required | 16 | 31 | 0.31% | 0.56% | -0.25 |
| Blocked, Restricted, Not Permitted | 113 | 134 | 2.18% | 2.42% | -0.24 |
| Expired, Invalid, Closed Card, No Account | 151 | 174 | 2.92% | 3.15% | -0.23 |
| Fraud, Lost/Stolen Card, Security | 17 | 25 | 0.33% | 0.45% | -0.12 |
| CVV/CVC Mismatch | 0 | 1 | 0.00% | 0.02% | -0.02 |
| Call Issuer, Voice Auth Required | 1 | 1 | 0.02% | 0.02% | +0.00 |

**Root Cause:** Others

---

## L2: CH Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 100.00% | 100.00% | +0.00% | 4 | 7 |  |
| Paypal | 100.00% | 100.00% | +0.00% | 7 | 8 |  |
| Credit Card | 86.49% | 73.33% | +17.94% | 37 | 30 | ⚠️ |
| Others | 100.00% | 50.00% | +100.00% | 2 | 2 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Expired, Invalid, Closed Card, No Account | 1 | 4 | 2.00% | 8.51% | -6.51 |
| Others | 49 | 43 | 98.00% | 91.49% | +6.51 |

**Root Cause:** Credit + Expired,

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | Medium (>85%) | 8,483 | 11,560 | +36.3% | Stable |
| DE | High (>92%) | 5,737 | 5,655 | -1.4% | Stable |
| FR | Medium (>85%) | 5,528 | 5,177 | -6.3% | Stable |
| AU | Medium (>85%) | 4,350 | 4,617 | +6.1% | Stable |
| NL | High (>92%) | 2,497 | 2,361 | -5.4% | Stable |
| BE | High (>92%) | 1,873 | 1,496 | -20.1% | ⚠️ Volume drop |
| NZ | Low (>85%) | 1,623 | 1,432 | -11.8% | Stable |
| SE | Medium (>85%) | 967 | 1,516 | +56.8% | Stable |
| DK | High (>92%) | 869 | 1,246 | +43.4% | Stable |
| IE | Medium (>85%) | 868 | 656 | -24.4% | ⚠️ Volume drop |
| NO | Medium (>85%) | 644 | 664 | +3.1% | Stable |
| AT | High (>92%) | 452 | 326 | -27.9% | ⚠️ Volume drop |
| CH | Low (>85%) | 47 | 50 | +6.4% | Stable |
| LU | High (>92%) | 32 | 33 | +3.1% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| NO | ↓ -7.29% | Credit Card -8.6% | → Stable | Expired, Invalid, Closed Card, No Account +4.18pp | Credit + Expired, |
| LU | ↓ -3.03% | Others -100.0% | → Stable | Expired, Invalid, Closed Card, No Account +3.03pp | Others + Expired, |
| FR | ↑ +2.68% | → Stable | → Stable | Others +2.01pp | Others |
| CH | ↑ +11.32% | Credit Card +17.9% | → Stable | Expired, Invalid, Closed Card, No Account -6.51pp | Credit + Expired, |

---

*Report: 2026-06-02*
