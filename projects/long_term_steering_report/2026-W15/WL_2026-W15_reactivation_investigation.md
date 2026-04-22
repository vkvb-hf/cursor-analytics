# Reactivation Investigation: WL 2026-W15

**Metric:** Reactivation Rate  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 89.29% → 86.81% (-2.78%)  
**Volume:** 8,022 orders  
**Significance:** Significant

## Executive Summary

**Overall:** Reactivation Rate declined significantly from 89.29% to 86.81% (-2.78 pp) in W15→W16, with 8,022 orders processed.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL Trend | 8-week pattern review | -2.78% vs prior week | ⚠️ Significant drop after W15 peak |
| L1: Country Scan | AO, CG outside ±2.5% threshold | AO -2.57%, CG +2.64% | ⚠️ Mixed signals |
| L1: Dimension Scan | PaymentMethod anomalies | Others -66.67%, Apple Pay +3.99% | ⚠️ Low-volume outlier |
| L2: AO Deep-Dive | Apple Pay performance | -9.68% decline | ⚠️ Root cause identified |
| L2: CG Deep-Dive | All methods improving | +2.51% to +2.68% | ✅ Positive trend |

**Key Findings:**
- AO experienced a -2.57 pp decline driven primarily by Apple Pay, which dropped from 50.00% to 45.16% (-9.68%) on low volume (31 orders)
- AO's "Expired, Invalid, Closed Card, No Account" decline reasons increased by +1.77 pp (from 5.67% to 7.45%), suggesting card lifecycle issues
- CG showed improvement (+2.64 pp) with all payment methods gaining 2.5-2.7 pp, partially offsetting the overall decline
- Volume shifted significantly: GN saw +154.5% volume increase, CK +38.7%, while AO volume dropped -20.0%
- The "Others" payment method showed a dramatic -66.67% change but only represents 3 orders (noise)

**Action:** Investigate — Focus on AO's Apple Pay integration and elevated expired card declines; coordinate with payment operations to review card-on-file refresh processes for AO market.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 86.81% | 8,022 | -2.78% |
| 2026-W15 | 89.29% | 9,277 | +0.70% ← REPORTED CHANGE |
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
| AO | 83.33% | 85.53% | -2.57% | 564 | ⚠️ |
| CK | 84.86% | 85.90% | -1.21% | 1,829 |  |
| ER | 91.04% | 89.51% | +1.71% | 3,349 |  |
| CG | 92.72% | 90.33% | +2.64% | 1,429 | ⚠️ |

**Countries exceeding ±2.5% threshold:** AO, CG

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 33.33% | 100.0% | -66.67% | 3 | ⚠️ |
| Credit Card | 89.92% | 89.58% | +0.38% | 6,638 |  |
| Paypal | 93.27% | 92.9% | +0.39% | 1,842 |  |
| Apple Pay | 74.94% | 72.06% | +3.99% | 794 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: AO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 45.16% | 50.00% | -9.68% | 31 | 30 | ⚠️ |
| Paypal | 93.67% | 95.87% | -2.30% | 158 | 218 |  |
| Credit Card | 82.13% | 82.93% | -0.96% | 375 | 457 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Expired, Invalid, Closed Card, No Account | 42 | 40 | 7.45% | 5.67% | +1.77 |
| Blocked, Restricted, Not Permitted | 8 | 16 | 1.42% | 2.27% | -0.85 |
| Others | 508 | 641 | 90.07% | 90.92% | -0.85 |
| CVV/CVC Mismatch | 0 | 1 | 0.00% | 0.14% | -0.14 |
| PayPal Declined, Revoked, Payer Issue | 6 | 7 | 1.06% | 0.99% | +0.07 |

**Root Cause:** Apple + Expired,

---

## L2: CG Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Credit Card | 93.78% | 91.48% | +2.51% | 996 | 810 |  |
| Paypal | 94.82% | 92.46% | +2.55% | 251 | 199 |  |
| Apple Pay | 84.07% | 81.88% | +2.68% | 182 | 160 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 1,351 | 1,088 | 94.54% | 93.07% | +1.47 |
| PayPal Declined, Revoked, Payer Issue | 11 | 14 | 0.77% | 1.20% | -0.43 |
| CVV/CVC Mismatch | 11 | 13 | 0.77% | 1.11% | -0.34 |
| Expired, Invalid, Closed Card, No Account | 36 | 33 | 2.52% | 2.82% | -0.30 |
| Call Issuer, Voice Auth Required | 3 | 6 | 0.21% | 0.51% | -0.30 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 17 | 15 | 1.19% | 1.28% | -0.09 |

**Root Cause:** Others

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 3,127 | 3,349 | +7.1% | Stable |
| CK | Medium (>85%) | 1,319 | 1,829 | +38.7% | Stable |
| CG | Medium (>85%) | 1,169 | 1,429 | +22.2% | Stable |
| AO | Medium (>85%) | 705 | 564 | -20.0% | Stable |
| MR | Medium (>85%) | 532 | 599 | +12.6% | Stable |
| KN | Medium (>85%) | 506 | 624 | +23.3% | Stable |
| GN | Medium (>85%) | 347 | 883 | +154.5% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| AO | ↓ -2.57% | Apple Pay -9.7% | → Stable | Expired, Invalid, Closed Card, No Account +1.77pp | Apple + Expired, |
| CG | ↑ +2.64% | → Stable | → Stable | Others +1.47pp | Others |

---

*Report: 2026-04-22*
