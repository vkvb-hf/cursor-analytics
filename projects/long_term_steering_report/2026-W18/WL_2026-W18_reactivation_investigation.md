# Reactivation Investigation: WL 2026-W18

**Metric:** Reactivation Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 85.35% → 86.51% (+1.36%)  
**Volume:** 7,436 orders  
**Significance:** Significant

## Executive Summary

**Overall:** Reactivation Rate improved significantly from 85.35% to 86.51% (+1.36%) in W18, recovering partially from the prior week's decline, with 7,436 orders processed.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL Trend | Rate recovering after W17 dip | +1.16 pp | ✅ |
| L1: Country Variance | 3 countries exceed ±2.5% threshold | CK -3.27%, KN +3.90%, AO +23.09% | ⚠️ |
| L1: Dimension Scan | PaymentMethod volatility detected | Others -33.33%, Apple Pay +4.36% | ⚠️ |
| L2: CK Deep-Dive | Broad decline across all payment methods | Credit Card -3.36%, Apple Pay -3.99% | ⚠️ |
| L2: KN Deep-Dive | Apple Pay driving improvement | Apple Pay +11.81% | ✅ |
| L2: AO Deep-Dive | Major volume drop with rate improvement | Volume -84.0%, Credit Card +31.16% | ⚠️ |

**Key Findings:**
- CK is the primary concern with a -3.27% rate decline across 1,835 orders; all payment methods underperformed with "Blocked, Restricted, Not Permitted" decline reasons increasing by +1.63 pp
- AO experienced an 84% volume drop (664 → 106 orders) which artificially inflated its rate improvement (+23.09%); this requires investigation into volume loss root cause
- KN showed genuine improvement (+3.90%) driven by Apple Pay performance increasing from 75.23% to 84.11% (+11.81 pp)
- The "Others" decline reason category dominates across all flagged countries (85-98% of declines), limiting actionable diagnosis
- Overall W18 rate (86.51%) remains below the 8-week highs seen in W12-W15 (87.5%-89.29%)

**Action:** Investigate - Priority focus on CK rate decline and AO volume collapse; request granular decline reason data to replace "Others" categorization

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W18 | 86.51% | 7,436 | +1.36% ← REPORTED CHANGE |
| 2026-W17 | 85.35% | 7,827 | -1.68% |
| 2026-W16 | 86.81% | 8,022 | -2.78% |
| 2026-W15 | 89.29% | 9,277 | +0.70% |
| 2026-W14 | 88.67% | 7,706 | -0.05% |
| 2026-W13 | 88.71% | 7,954 | -0.49% |
| 2026-W12 | 89.15% | 7,658 | +1.89% |
| 2026-W11 | 87.5% | 9,145 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CK | 77.66% | 80.28% | -3.27% | 1,835 | ⚠️ |
| ER | 89.82% | 88.97% | +0.95% | 2,494 |  |
| GN | 85.43% | 83.77% | +1.98% | 858 |  |
| KN | 92.11% | 88.65% | +3.90% | 393 | ⚠️ |
| AO | 95.28% | 77.41% | +23.09% | 106 | ⚠️ |

**Countries exceeding ±2.5% threshold:** CK, KN, AO

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 66.67% | 100.0% | -33.33% | 3 | ⚠️ |
| Paypal | 92.51% | 92.19% | +0.35% | 1,375 |  |
| Credit Card | 86.81% | 85.59% | +1.43% | 5,315 |  |
| Apple Pay | 73.35% | 70.29% | +4.36% | 743 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: CK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Others | 0.00% | 100.00% | -100.00% | 1 | 1 | ⚠️ |
| Apple Pay | 62.04% | 64.62% | -3.99% | 108 | 130 |  |
| Credit Card | 77.08% | 79.76% | -3.36% | 1,479 | 1,408 |  |
| Paypal | 88.26% | 90.80% | -2.80% | 247 | 261 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 1,557 | 1,568 | 84.85% | 87.11% | -2.26 |
| Blocked, Restricted, Not Permitted | 86 | 55 | 4.69% | 3.06% | +1.63 |
| Expired, Invalid, Closed Card, No Account | 165 | 153 | 8.99% | 8.50% | +0.49 |
| PayPal Declined, Revoked, Payer Issue | 22 | 14 | 1.20% | 0.78% | +0.42 |
| Fraud, Lost/Stolen Card, Security | 5 | 8 | 0.27% | 0.44% | -0.17 |
| Call Issuer, Voice Auth Required | 0 | 1 | 0.00% | 0.06% | -0.06 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 0 | 1 | 0.00% | 0.06% | -0.06 |

**Root Cause:** Others + Others

---

## L2: KN Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Paypal | 93.94% | 94.12% | -0.19% | 66 | 51 |  |
| Credit Card | 95.45% | 94.06% | +1.48% | 220 | 219 |  |
| Apple Pay | 84.11% | 75.23% | +11.81% | 107 | 109 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Policy, Lifecycle, Revocation, Limit Exceeded | 6 | 8 | 1.53% | 2.11% | -0.58 |
| Others | 372 | 357 | 94.66% | 94.20% | +0.46 |
| Call Issuer, Voice Auth Required | 2 | 3 | 0.51% | 0.79% | -0.28 |
| PayPal Declined, Revoked, Payer Issue | 4 | 3 | 1.02% | 0.79% | +0.23 |
| Expired, Invalid, Closed Card, No Account | 9 | 8 | 2.29% | 2.11% | +0.18 |

**Root Cause:** Apple

---

## L2: AO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 33.33% | 33.33% | +0.00% | 3 | 33 |  |
| Paypal | 100.00% | 92.96% | +7.57% | 16 | 199 | ⚠️ |
| Credit Card | 96.55% | 73.61% | +31.16% | 87 | 432 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 104 | 568 | 98.11% | 85.54% | +12.57 |
| Expired, Invalid, Closed Card, No Account | 1 | 63 | 0.94% | 9.49% | -8.54 |
| Blocked, Restricted, Not Permitted | 0 | 17 | 0.00% | 2.56% | -2.56 |
| PayPal Declined, Revoked, Payer Issue | 0 | 14 | 0.00% | 2.11% | -2.11 |
| CVV/CVC Mismatch | 1 | 0 | 0.94% | 0.00% | +0.94 |
| Fraud, Lost/Stolen Card, Security | 0 | 2 | 0.00% | 0.30% | -0.30 |

**Root Cause:** Paypal + Others

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| ER | Medium (>85%) | 2,331 | 2,494 | +7.0% | Stable |
| CK | Low (>85%) | 1,800 | 1,835 | +1.9% | Stable |
| CG | Medium (>85%) | 1,104 | 1,118 | +1.3% | Stable |
| GN | Low (>85%) | 955 | 858 | -10.2% | Stable |
| AO | Low (>85%) | 664 | 106 | -84.0% | ⚠️ Volume drop |
| MR | Medium (>85%) | 594 | 631 | +6.2% | Stable |
| KN | Medium (>85%) | 379 | 393 | +3.7% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| CK | ↓ -3.27% | Others -100.0% | → Stable | Others -2.26pp | Others + Others |
| KN | ↑ +3.90% | Apple Pay +11.8% | → Stable | → Stable | Apple |
| AO | ↑ +23.09% | Paypal +7.6% | → Stable | Others +12.57pp | Paypal + Others |

---

*Report: 2026-05-05*
