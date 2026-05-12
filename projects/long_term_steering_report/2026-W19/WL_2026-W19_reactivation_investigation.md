# Reactivation Investigation: WL 2026-W19

**Metric:** Reactivation Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 86.51% → 88.73% (+2.57%)  
**Volume:** 9,047 orders  
**Significance:** Significant

## Executive Summary

**Overall:** Reactivation Rate improved significantly from 86.51% to 88.73% (+2.57%) in W19, with volume increasing to 9,047 orders, representing a recovery toward the 8-week high of 89.15% seen in W12.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate recovering from W17 dip | +2.57% | ✅ |
| L1: Country Variance | 3 countries exceed ±2.5% threshold | AO -7.44%, GN +4.57%, CK +7.08% | ⚠️ |
| L1: Payment Method | Credit Card driving improvement | +3.21% | ⚠️ |
| L2: AO Deep-Dive | Apple Pay failure, Credit Card decline | -7.44% overall | ⚠️ |
| L2: GN Deep-Dive | Credit Card improvement | +7.73% | ✅ |
| L2: CK Deep-Dive | Credit Card & Apple Pay improvement | +6.97%, +26.65% | ✅ |
| Mix Shift | No significant impact detected | Stable | ✅ |

**Key Findings:**
- CK showed the strongest improvement (+7.08%), driven by Credit Card (+6.97%) and Apple Pay (+26.65%) performance gains, with "Expired, Invalid, Closed Card" declines dropping from 8.99% to 7.34%
- AO experienced a significant decline (-7.44%) due to Apple Pay dropping from 33.33% to 0.00% (on low volume of 3 orders) and Credit Card falling from 96.55% to 88.39%
- GN improved by +4.57%, primarily driven by Credit Card reactivation rate increasing from 82.97% to 89.39% (+7.73%)
- Credit Card as a payment method was the primary driver at the global level, improving from 86.81% to 89.60% (+3.21%) on 6,461 orders
- The "Others" decline reason category shows mixed signals: improving in CK (+2.68pp) and GN (+1.88pp), but declining in AO (-4.95pp)

**Action:** Monitor - The overall improvement is positive and driven by legitimate Credit Card performance gains in CK and GN. Investigate AO's Apple Pay failures if volume increases, but current impact is minimal (3 orders). Continue monitoring W20 to confirm trend stability.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W19 | 88.73% | 9,047 | +2.57% ← REPORTED CHANGE |
| 2026-W18 | 86.51% | 7,436 | +1.36% |
| 2026-W17 | 85.35% | 7,827 | -1.68% |
| 2026-W16 | 86.81% | 8,022 | -2.78% |
| 2026-W15 | 89.29% | 9,277 | +0.70% |
| 2026-W14 | 88.67% | 7,706 | -0.05% |
| 2026-W13 | 88.71% | 7,954 | -0.49% |
| 2026-W12 | 89.15% | 7,658 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| AO | 88.20% | 95.28% | -7.44% | 161 | ⚠️ |
| KN | 90.85% | 92.11% | -1.37% | 437 |  |
| ER | 90.40% | 89.82% | +0.65% | 2,937 |  |
| CG | 91.16% | 90.25% | +1.01% | 1,358 |  |
| GN | 89.33% | 85.43% | +4.57% | 825 | ⚠️ |
| CK | 83.16% | 77.66% | +7.08% | 1,716 | ⚠️ |

**Countries exceeding ±2.5% threshold:** AO, GN, CK

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 92.34% | 92.51% | -0.18% | 1,762 |  |
| Apple Pay | 74.11% | 73.35% | +1.04% | 819 |  |
| Credit Card | 89.6% | 86.81% | +3.21% | 6,461 | ⚠️ |
| Others | 80.0% | 66.67% | +20.00% | 5 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: AO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 0.00% | 33.33% | -100.00% | 3 | 3 | ⚠️ |
| Credit Card | 88.39% | 96.55% | -8.45% | 112 | 87 | ⚠️ |
| Paypal | 93.48% | 100.00% | -6.52% | 46 | 16 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 150 | 104 | 93.17% | 98.11% | -4.95 |
| Expired, Invalid, Closed Card, No Account | 5 | 1 | 3.11% | 0.94% | +2.16 |
| PayPal Declined, Revoked, Payer Issue | 3 | 0 | 1.86% | 0.00% | +1.86 |
| Blocked, Restricted, Not Permitted | 1 | 0 | 0.62% | 0.00% | +0.62 |
| CVV/CVC Mismatch | 2 | 1 | 1.24% | 0.94% | +0.30 |

**Root Cause:** Apple + Others

---

## L2: GN Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Paypal | 95.57% | 98.15% | -2.63% | 158 | 162 |  |
| Apple Pay | 85.19% | 81.47% | +4.57% | 243 | 232 |  |
| Credit Card | 89.39% | 82.97% | +7.73% | 424 | 464 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 778 | 793 | 94.30% | 92.42% | +1.88 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 2 | 7 | 0.24% | 0.82% | -0.57 |
| Expired, Invalid, Closed Card, No Account | 30 | 36 | 3.64% | 4.20% | -0.56 |
| Blocked, Restricted, Not Permitted | 8 | 13 | 0.97% | 1.52% | -0.55 |
| Fraud, Lost/Stolen Card, Security | 1 | 3 | 0.12% | 0.35% | -0.23 |
| PayPal Declined, Revoked, Payer Issue | 4 | 4 | 0.48% | 0.47% | +0.02 |
| Call Issuer, Voice Auth Required | 2 | 2 | 0.24% | 0.23% | +0.01 |

**Root Cause:** Credit + Others

---

## L2: CK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Others | 0.00% | 0.00% | +0.00% | 1 | 1 |  |
| Paypal | 89.02% | 88.26% | +0.86% | 264 | 247 |  |
| Credit Card | 82.45% | 77.08% | +6.97% | 1,339 | 1,479 | ⚠️ |
| Apple Pay | 78.57% | 62.04% | +26.65% | 112 | 108 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 1,502 | 1,557 | 87.53% | 84.85% | +2.68 |
| Expired, Invalid, Closed Card, No Account | 126 | 165 | 7.34% | 8.99% | -1.65 |
| Blocked, Restricted, Not Permitted | 57 | 86 | 3.32% | 4.69% | -1.36 |
| Fraud, Lost/Stolen Card, Security | 9 | 5 | 0.52% | 0.27% | +0.25 |
| Call Issuer, Voice Auth Required | 1 | 0 | 0.06% | 0.00% | +0.06 |
| PayPal Declined, Revoked, Payer Issue | 21 | 22 | 1.22% | 1.20% | +0.02 |

**Root Cause:** Credit + Others

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 2,494 | 2,937 | +17.8% | Stable |
| CK | Low (>85%) | 1,835 | 1,716 | -6.5% | Stable |
| CG | Medium (>85%) | 1,118 | 1,358 | +21.5% | Stable |
| GN | Medium (>85%) | 858 | 825 | -3.8% | Stable |
| MR | Medium (>85%) | 631 | 1,613 | +155.6% | Stable |
| KN | High (>92%) | 393 | 437 | +11.2% | Stable |
| AO | High (>92%) | 106 | 161 | +51.9% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| AO | ↓ -7.44% | Apple Pay -100.0% | → Stable | Others -4.95pp | Apple + Others |
| GN | ↑ +4.57% | Credit Card +7.7% | → Stable | Others +1.88pp | Credit + Others |
| CK | ↑ +7.08% | Credit Card +7.0% | → Stable | Others +2.68pp | Credit + Others |

---

*Report: 2026-05-12*
