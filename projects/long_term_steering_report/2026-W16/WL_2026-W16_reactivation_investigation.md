# Reactivation Investigation: WL 2026-W16

**Metric:** Reactivation Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 89.29% → 86.81% (-2.78%)  
**Volume:** 8,022 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Reactivation Rate declined significantly from 89.29% to 86.81% (-2.78pp) in WL 2026-W16, representing the largest week-over-week drop in the 8-week trend period.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL Trend | Significant drop after stable period | -2.78pp | ⚠️ |
| L1: Country Breakdown | 3 countries exceed ±2.5% threshold | CK -5.69%, AO -3.83%, MR -3.64% | ⚠️ |
| L1: PaymentMethod | Credit Card significant decline | -3.24% | ⚠️ |
| L2: CK Deep-Dive | All payment methods declining | Apple Pay -9.64%, Paypal -7.17%, Credit Card -5.32% | ⚠️ |
| L2: AO Deep-Dive | Apple Pay severe decline | -29.14% | ⚠️ |
| L2: MR Deep-Dive | Credit Card decline | -6.33% | ⚠️ |
| Mix Shift | ER volume dropped significantly | -27.5% | ⚠️ |

**Key Findings:**
- CK experienced the largest rate decline (-5.69pp) with all payment methods underperforming; "Expired, Invalid, Closed Card, No Account" decline reasons increased by +3.43pp
- AO saw severe Apple Pay degradation (-29.14%) dropping from 45.16% to 32.00%, though on relatively low volume (25 orders)
- MR Credit Card reactivation dropped -6.33% despite volume increasing +22.7%, suggesting underlying processing issues rather than mix shift
- ER (highest volume country at 2,428 orders) experienced a significant -27.5% volume drop, contributing to overall mix shift
- "Others" decline reason dominates across all flagged countries (84-90% of declines), limiting root cause visibility

**Action:** Investigate — Focus on CK payment processing issues (particularly the +3.43pp increase in expired/invalid card declines) and AO Apple Pay degradation. Request detailed decline code breakdown to resolve "Others" categorization.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 86.81% | 8,022 | -2.78% ← REPORTED CHANGE |
| 2026-W15 | 89.29% | 9,277 | +0.70% |
| 2026-W14 | 88.67% | 7,706 | -0.05% |
| 2026-W13 | 88.71% | 7,954 | -0.49% |
| 2026-W12 | 89.15% | 7,658 | +1.89% |
| 2026-W11 | 87.5% | 9,145 | +1.91% |
| 2026-W10 | 85.86% | 9,675 | -0.12% |
| 2026-W09 | 85.96% | 7,581 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CK | 80.02% | 84.86% | -5.69% | 1,697 | ⚠️ |
| AO | 80.14% | 83.33% | -3.83% | 554 | ⚠️ |
| MR | 85.58% | 88.81% | -3.64% | 735 | ⚠️ |
| ER | 89.37% | 91.04% | -1.83% | 2,428 |  |

**Countries exceeding ±2.5% threshold:** CK, AO, MR

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Credit Card | 87.01% | 89.92% | -3.24% | 5,690 | ⚠️ |
| Paypal | 92.02% | 93.27% | -1.34% | 1,591 |  |
| Apple Pay | 74.05% | 74.94% | -1.18% | 740 |  |
| Others | 100.0% | 33.33% | +200.00% | 1 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: CK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Others | 0.00% | 33.33% | -100.00% | 0 | 3 | ⚠️ |
| Apple Pay | 72.12% | 79.81% | -9.64% | 104 | 104 | ⚠️ |
| Paypal | 86.94% | 93.66% | -7.17% | 268 | 268 | ⚠️ |
| Credit Card | 79.25% | 83.70% | -5.32% | 1,325 | 1,454 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 1,439 | 1,641 | 84.80% | 89.72% | -4.92 |
| Expired, Invalid, Closed Card, No Account | 152 | 101 | 8.96% | 5.52% | +3.43 |
| Blocked, Restricted, Not Permitted | 65 | 43 | 3.83% | 2.35% | +1.48 |
| PayPal Declined, Revoked, Payer Issue | 29 | 12 | 1.71% | 0.66% | +1.05 |
| Fraud, Lost/Stolen Card, Security | 9 | 27 | 0.53% | 1.48% | -0.95 |
| 3DS Authentication Failed/Required | 0 | 3 | 0.00% | 0.16% | -0.16 |
| Call Issuer, Voice Auth Required | 2 | 1 | 0.12% | 0.05% | +0.06 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 1 | 1 | 0.06% | 0.05% | +0.00 |

**Root Cause:** Others + Others

---

## L2: AO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 32.00% | 45.16% | -29.14% | 25 | 31 | ⚠️ |
| Credit Card | 78.27% | 82.13% | -4.70% | 382 | 375 |  |
| Paypal | 93.20% | 93.67% | -0.51% | 147 | 158 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 492 | 508 | 88.81% | 90.07% | -1.26 |
| Blocked, Restricted, Not Permitted | 11 | 8 | 1.99% | 1.42% | +0.57 |
| PayPal Declined, Revoked, Payer Issue | 8 | 6 | 1.44% | 1.06% | +0.38 |
| 3DS Authentication Failed/Required | 1 | 0 | 0.18% | 0.00% | +0.18 |
| Expired, Invalid, Closed Card, No Account | 42 | 42 | 7.58% | 7.45% | +0.13 |

**Root Cause:** Apple + Others

---

## L2: MR Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Credit Card | 87.72% | 93.65% | -6.33% | 521 | 425 | ⚠️ |
| Paypal | 88.06% | 84.21% | +4.57% | 134 | 114 |  |
| Apple Pay | 67.50% | 63.33% | +6.58% | 80 | 60 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 662 | 550 | 90.07% | 91.82% | -1.75 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 24 | 13 | 3.27% | 2.17% | +1.10 |
| Expired, Invalid, Closed Card, No Account | 28 | 17 | 3.81% | 2.84% | +0.97 |
| PayPal Declined, Revoked, Payer Issue | 15 | 15 | 2.04% | 2.50% | -0.46 |
| Gateway Rejected, Risk Threshold | 1 | 0 | 0.14% | 0.00% | +0.14 |
| Call Issuer, Voice Auth Required | 5 | 4 | 0.68% | 0.67% | +0.01 |

**Root Cause:** Credit + Others

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 3,349 | 2,428 | -27.5% | ⚠️ Volume drop |
| CK | Low (>85%) | 1,829 | 1,697 | -7.2% | Stable |
| CG | High (>92%) | 1,429 | 1,241 | -13.2% | Stable |
| GN | Medium (>85%) | 883 | 815 | -7.7% | Stable |
| KN | Medium (>85%) | 624 | 552 | -11.5% | Stable |
| MR | Medium (>85%) | 599 | 735 | +22.7% | Stable |
| AO | Low (>85%) | 564 | 554 | -1.8% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| CK | ↓ -5.69% | Others -100.0% | → Stable | Others -4.92pp | Others + Others |
| AO | ↓ -3.83% | Apple Pay -29.1% | → Stable | Others -1.26pp | Apple + Others |
| MR | ↓ -3.64% | Credit Card -6.3% | → Stable | Others -1.75pp | Credit + Others |

---

*Report: 2026-04-22*
