# Reactivation Investigation: WL 2026-W17

**Metric:** Reactivation Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 86.81% → 85.35% (-1.68%)  
**Volume:** 7,827 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Reactivation Rate declined significantly from 86.81% to 85.35% (-1.68%) in W17, continuing a two-week downward trend that has seen the metric drop from 89.29% in W15.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL Trend | 2-week consecutive decline | -1.68% WoW | ⚠️ |
| L1: Country Breakdown | 4 countries exceed ±2.5% threshold | GN -5.83%, AO -3.41%, CG -2.90%, MR +3.87% | ⚠️ |
| L1: PaymentMethod | Apple Pay underperforming | -5.09% WoW | ⚠️ |
| L2: GN Deep-Dive | Credit Card & Apple Pay declining | CC -7.90%, AP -5.63% | ⚠️ |
| L2: AO Deep-Dive | Credit Card declining | CC -5.96% | ⚠️ |
| L2: Mix Shift | Volume shifts in low-AR countries | AO +19.9%, KN -31.3% | ⚠️ |

**Key Findings:**
- GN experienced the largest rate decline (-5.83%), driven by Credit Card (-7.90%) and Apple Pay (-5.63%) performance degradation, with "Expired, Invalid, Closed Card" declines increasing by +1.29pp
- AO saw Credit Card reactivation drop by -5.96%, with "Expired, Invalid, Closed Card" reasons rising +1.91pp and "Others" decline category shifting -3.27pp
- Apple Pay is underperforming globally at 70.29% (vs 74.05% prior week), a -5.09% decline affecting 801 orders
- MR showed improvement (+3.87%) across all payment methods, partially offsetting declines elsewhere
- Volume mix shifted unfavorably with low-AR country AO gaining +19.9% volume while higher-performing KN dropped -31.3%

**Action:** Investigate - Focus on Credit Card processing issues in GN and AO, particularly the increase in "Expired, Invalid, Closed Card" decline reasons. Coordinate with payment operations to assess if card-on-file refresh campaigns or issuer connectivity issues are contributing factors.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 85.35% | 7,827 | -1.68% ← REPORTED CHANGE |
| 2026-W16 | 86.81% | 8,022 | -2.78% |
| 2026-W15 | 89.29% | 9,277 | +0.70% |
| 2026-W14 | 88.67% | 7,706 | -0.05% |
| 2026-W13 | 88.71% | 7,954 | -0.49% |
| 2026-W12 | 89.15% | 7,658 | +1.89% |
| 2026-W11 | 87.5% | 9,145 | +1.91% |
| 2026-W10 | 85.86% | 9,675 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| GN | 83.77% | 88.96% | -5.83% | 955 | ⚠️ |
| AO | 77.41% | 80.14% | -3.41% | 664 | ⚠️ |
| CG | 89.04% | 91.70% | -2.90% | 1,104 | ⚠️ |
| MR | 88.89% | 85.58% | +3.87% | 594 | ⚠️ |

**Countries exceeding ±2.5% threshold:** GN, AO, CG, MR

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 70.29% | 74.05% | -5.09% | 801 | ⚠️ |
| Credit Card | 85.59% | 87.01% | -1.64% | 5,461 |  |
| Others | 100.0% | 100.0% | +0.00% | 3 |  |
| Paypal | 92.19% | 92.02% | +0.19% | 1,562 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: GN Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Credit Card | 79.07% | 85.85% | -7.90% | 497 | 410 | ⚠️ |
| Apple Pay | 83.27% | 88.24% | -5.63% | 257 | 221 | ⚠️ |
| Paypal | 96.02% | 96.74% | -0.74% | 201 | 184 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 882 | 772 | 92.36% | 94.72% | -2.37 |
| Expired, Invalid, Closed Card, No Account | 44 | 27 | 4.61% | 3.31% | +1.29 |
| Blocked, Restricted, Not Permitted | 19 | 10 | 1.99% | 1.23% | +0.76 |
| PayPal Declined, Revoked, Payer Issue | 7 | 4 | 0.73% | 0.49% | +0.24 |
| Fraud, Lost/Stolen Card, Security | 1 | 0 | 0.10% | 0.00% | +0.10 |
| Call Issuer, Voice Auth Required | 1 | 1 | 0.10% | 0.12% | -0.02 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 1 | 1 | 0.10% | 0.12% | -0.02 |

**Root Cause:** Credit + Others

---

## L2: AO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Credit Card | 73.61% | 78.27% | -5.96% | 432 | 382 | ⚠️ |
| Paypal | 92.96% | 93.20% | -0.25% | 199 | 147 |  |
| Apple Pay | 33.33% | 32.00% | +4.17% | 33 | 25 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 568 | 492 | 85.54% | 88.81% | -3.27 |
| Expired, Invalid, Closed Card, No Account | 63 | 42 | 9.49% | 7.58% | +1.91 |
| PayPal Declined, Revoked, Payer Issue | 14 | 8 | 2.11% | 1.44% | +0.66 |
| Blocked, Restricted, Not Permitted | 17 | 11 | 2.56% | 1.99% | +0.57 |
| Fraud, Lost/Stolen Card, Security | 2 | 0 | 0.30% | 0.00% | +0.30 |
| 3DS Authentication Failed/Required | 0 | 1 | 0.00% | 0.18% | -0.18 |

**Root Cause:** Credit + Others

---

## L2: CG Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Paypal | 91.67% | 95.05% | -3.56% | 180 | 182 |  |
| Credit Card | 89.99% | 92.95% | -3.18% | 769 | 893 |  |
| Others | 100.00% | 100.00% | +0.00% | 2 | 3 |  |
| Apple Pay | 81.05% | 80.98% | +0.08% | 153 | 163 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 1,026 | 1,167 | 92.93% | 94.04% | -1.10 |
| PayPal Declined, Revoked, Payer Issue | 13 | 7 | 1.18% | 0.56% | +0.61 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 15 | 12 | 1.36% | 0.97% | +0.39 |
| Expired, Invalid, Closed Card, No Account | 35 | 35 | 3.17% | 2.82% | +0.35 |
| CVV/CVC Mismatch | 9 | 14 | 0.82% | 1.13% | -0.31 |
| Fraud, Lost/Stolen Card, Security | 1 | 0 | 0.09% | 0.00% | +0.09 |
| Call Issuer, Voice Auth Required | 5 | 6 | 0.45% | 0.48% | -0.03 |

**Root Cause:** Others

---

## L2: MR Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Credit Card | 90.57% | 87.72% | +3.26% | 435 | 521 |  |
| Apple Pay | 70.18% | 67.50% | +3.96% | 57 | 80 |  |
| Paypal | 92.16% | 88.06% | +4.65% | 102 | 134 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 546 | 662 | 91.92% | 90.07% | +1.85 |
| Expired, Invalid, Closed Card, No Account | 15 | 28 | 2.53% | 3.81% | -1.28 |
| PayPal Declined, Revoked, Payer Issue | 6 | 15 | 1.01% | 2.04% | -1.03 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 21 | 24 | 3.54% | 3.27% | +0.27 |
| CVV/CVC Mismatch | 1 | 0 | 0.17% | 0.00% | +0.17 |
| Gateway Rejected, Risk Threshold | 1 | 1 | 0.17% | 0.14% | +0.03 |
| Call Issuer, Voice Auth Required | 4 | 5 | 0.67% | 0.68% | -0.01 |

**Root Cause:** Others

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 2,428 | 2,331 | -4.0% | Stable |
| CK | Low (>85%) | 1,697 | 1,800 | +6.1% | Stable |
| CG | Medium (>85%) | 1,241 | 1,104 | -11.0% | Stable |
| GN | Medium (>85%) | 815 | 955 | +17.2% | Stable |
| MR | Medium (>85%) | 735 | 594 | -19.2% | Stable |
| AO | Low (>85%) | 554 | 664 | +19.9% | Stable |
| KN | Medium (>85%) | 552 | 379 | -31.3% | ⚠️ Volume drop |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| GN | ↓ -5.83% | Credit Card -7.9% | → Stable | Others -2.37pp | Credit + Others |
| AO | ↓ -3.41% | Credit Card -6.0% | → Stable | Others -3.27pp | Credit + Others |
| CG | ↓ -2.90% | → Stable | → Stable | Others -1.10pp | Others |
| MR | ↑ +3.87% | → Stable | → Stable | Others +1.85pp | Others |

---

*Report: 2026-04-27*
