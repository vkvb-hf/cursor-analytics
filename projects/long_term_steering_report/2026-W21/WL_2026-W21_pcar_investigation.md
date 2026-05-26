# PCAR Investigation: WL 2026-W21

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 95.62% → 96.86% (+1.30%)  
**Volume:** 9,450 orders  
**Significance:** Significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate improved significantly from 95.62% to 96.86% (+1.30%) in WL 2026-W21, representing a positive recovery toward the higher rates observed in earlier weeks.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate recovering from W19 dip | +1.30% | ✅ |
| L1: Country Breakdown | CK exceeds ±2.5% threshold (+3.35%) | +3.35% | ⚠️ |
| L1: Dimension Scan | Credit Card improved +2.38% | +2.38% | ✅ |
| L2: CK Deep-Dive | Adyen/CreditCard improved +4.33% | +4.33% | ✅ |
| Mix Shift | GN volume dropped -22.1% | N/A | ⚠️ |

**Key Findings:**
- CK drove the largest country-level improvement at +3.35%, primarily through Credit Card transactions processed via Adyen (+4.33%)
- Fraud-related declines in CK decreased significantly from 1.07% to 0.30% (-0.77pp), indicating improved fraud filtering or customer quality
- Expired/Invalid card declines in CK also dropped from 0.84% to 0.35% (-0.49pp)
- Overall Credit Card payment method improved +2.38% across the region (94.54% → 96.79%)
- GN experienced a significant volume drop of -22.1% (1,234 → 961 orders) which warrants monitoring

**Action:** Monitor - The improvement is positive and appears driven by reduced fraud and card validity declines in CK via Adyen. Continue monitoring GN volume trends and the "Others" decline category which remains dominant at 98.25% of CK declines.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W21 | 96.86% | 9,450 | +1.30% ← REPORTED CHANGE |
| 2026-W20 | 95.62% | 10,330 | +0.36% |
| 2026-W19 | 95.28% | 10,480 | -0.77% |
| 2026-W18 | 96.02% | 10,753 | -1.03% |
| 2026-W17 | 97.02% | 10,957 | -0.58% |
| 2026-W16 | 97.59% | 11,025 | +0.23% |
| 2026-W15 | 97.37% | 11,722 | +0.35% |
| 2026-W14 | 97.03% | 11,373 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CG | 97.57% | 96.81% | +0.79% | 1,727 |  |
| KN | 97.84% | 97.00% | +0.86% | 2,220 |  |
| ER | 94.72% | 93.23% | +1.60% | 1,610 |  |
| MR | 100.00% | 97.67% | +2.38% | 117 |  |
| CK | 96.94% | 93.80% | +3.35% | 1,995 | ⚠️ |

**Countries exceeding ±2.5% threshold:** CK

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | nan% | nan% | +nan% | 0 |  |
| Apple Pay | 96.46% | 96.71% | -0.26% | 2,963 |  |
| Paypal | 98.16% | 97.56% | +0.61% | 1,194 |  |
| Credit Card | 96.79% | 94.54% | +2.38% | 5,293 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: CK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Paypal | 98.10% | 97.84% | +0.26% | 263 | 232 |  |
| ApplePay | 98.34% | 97.55% | +0.81% | 301 | 327 |  |
| CreditCard | 96.44% | 92.43% | +4.33% | 1,431 | 1,586 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Braintree | 98.23% | 97.67% | +0.57% | 564 | 559 |  |
| Adyen | 96.44% | 92.43% | +4.33% | 1,431 | 1,586 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 1,960 | 2,071 | 98.25% | 96.55% | +1.70 |
| Fraud, Lost/Stolen Card, Security | 6 | 23 | 0.30% | 1.07% | -0.77 |
| Expired, Invalid, Closed Card, No Account | 7 | 18 | 0.35% | 0.84% | -0.49 |
| Blocked, Restricted, Not Permitted | 3 | 13 | 0.15% | 0.61% | -0.46 |
| CVV/CVC Mismatch | 11 | 11 | 0.55% | 0.51% | +0.04 |
| 3DS Authentication Failed/Required | 4 | 5 | 0.20% | 0.23% | -0.03 |
| PayPal Declined, Revoked, Payer Issue | 4 | 4 | 0.20% | 0.19% | +0.01 |

**Root Cause:** Others

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| KN | High (>92%) | 2,604 | 2,220 | -14.7% | Stable |
| CK | High (>92%) | 2,145 | 1,995 | -7.0% | Stable |
| CG | High (>92%) | 1,785 | 1,727 | -3.2% | Stable |
| ER | High (>92%) | 1,714 | 1,610 | -6.1% | Stable |
| GN | High (>92%) | 1,234 | 961 | -22.1% | ⚠️ Volume drop |
| AO | High (>92%) | 762 | 820 | +7.6% | Stable |
| MR | High (>92%) | 86 | 117 | +36.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| CK | ↑ +3.35% | → Stable | → Stable | Others +1.70pp | Others |

---

*Report: 2026-05-26*
