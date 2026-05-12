# Reactivation Investigation: HF-INTL 2026-W19

**Metric:** Reactivation Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 90.32% → 90.32% (+0.00%)  
**Volume:** 40,935 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Reactivation Rate for HF-INTL remained flat at 90.32% in 2026-W19, showing no change from the prior week (+0.00 pp) on a volume of 40,935 orders, with the change not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Stable trend, rate within normal range (90.03%-91.47%) | +0.00 pp | ✅ |
| L1: Country Breakdown | 4 countries flagged (IT, CH, NZ, SE) exceeding ±2.5% threshold | -100.00% to -4.08% | ⚠️ |
| L1: Dimension Scan | PaymentMethod and PaymentProvider stable, no flags | -0.97% to +0.02% | ✅ |
| L2: Deep-Dive | Low-volume anomalies in IT (1 order); Credit Card declines in NZ, SE | Mixed | ⚠️ |
| Mix Shift | Volume drops in AU (-33.2%), DK (-26.4%), SE (-27.5%), LU (-35.1%) | Varied | ⚠️ |

**Key Findings:**
- IT shows a -100.00% rate drop but is statistically irrelevant with only 1 order (down from 2), caused by a single expired/invalid card decline on Credit Card
- NZ experienced a -4.38 pp decline driven by Credit Card (-5.14%), with "Others" and "Expired, Invalid, Closed Card, No Account" as primary decline reasons across 1,209 orders
- SE declined -4.08 pp with Credit Card (-5.57%) and Apple Pay (-5.36%) underperforming; "Others" decline reason accounts for 94.09% of failures
- Significant volume shifts observed: AU volume dropped -33.2% (6,062 → 4,052), while NL increased +34.6% (2,329 → 3,135)
- CH declined -5.70 pp but on minimal volume (51 orders), with PayPal dropping -8.33%

**Action:** Monitor — The overall rate is stable and the flagged countries (IT, CH) have statistically insignificant volumes. Continue monitoring NZ and SE Credit Card performance for potential emerging patterns; no immediate escalation required.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W19 | 90.32% | 40,935 | - ← REPORTED CHANGE |
| 2026-W18 | 90.32% | 43,663 | -0.46% |
| 2026-W17 | 90.74% | 40,613 | -0.54% |
| 2026-W16 | 91.23% | 46,003 | -0.26% |
| 2026-W15 | 91.47% | 41,652 | +0.60% |
| 2026-W14 | 90.92% | 32,555 | +0.99% |
| 2026-W13 | 90.03% | 43,179 | -0.19% |
| 2026-W12 | 90.2% | 42,003 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| IT | 0.00% | 50.00% | -100.00% | 1 | ⚠️ |
| CH | 90.20% | 95.65% | -5.70% | 51 | ⚠️ |
| NZ | 79.98% | 83.65% | -4.38% | 1,209 | ⚠️ |
| SE | 88.01% | 91.75% | -4.08% | 1,151 | ⚠️ |
| DE | 96.36% | 97.25% | -0.92% | 6,150 |  |
| GB | 90.11% | 89.38% | +0.82% | 13,786 |  |

**Countries exceeding ±2.5% threshold:** IT, CH, NZ, SE

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 89.93% | 90.82% | -0.97% | 7,331 |  |
| Paypal | 96.34% | 96.63% | -0.30% | 10,856 |  |
| Others | 97.32% | 97.51% | -0.19% | 4,112 |  |
| Credit Card | 85.43% | 85.41% | +0.02% | 18,636 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: IT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Paypal | 0.00% | 0.00% | +0.00% | 0 | 1 |  |
| Credit Card | 0.00% | 100.00% | -100.00% | 1 | 1 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Expired, Invalid, Closed Card, No Account | 1 | 0 | 100.00% | 0.00% | +100.00 |
| Others | 0 | 1 | 0.00% | 50.00% | -50.00 |
| PayPal Declined, Revoked, Payer Issue | 0 | 1 | 0.00% | 50.00% | -50.00 |

**Root Cause:** Credit + Expired,

---

## L2: CH Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Others | 0.00% | 0.00% | +0.00% | 1 | 0 |  |
| Paypal | 91.67% | 100.00% | -8.33% | 12 | 15 | ⚠️ |
| Credit Card | 90.32% | 90.91% | -0.65% | 31 | 22 |  |
| Apple Pay | 100.00% | 100.00% | +0.00% | 7 | 9 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 51 | 45 | 100.00% | 97.83% | +2.17 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 0 | 1 | 0.00% | 2.17% | -2.17 |

**Root Cause:** Paypal + Others

---

## L2: NZ Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Credit Card | 79.61% | 83.93% | -5.14% | 1,138 | 1,257 | ⚠️ |
| Apple Pay | 63.16% | 60.00% | +5.26% | 19 | 25 | ⚠️ |
| Paypal | 94.23% | 88.24% | +6.79% | 52 | 51 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 1,058 | 1,185 | 87.51% | 88.90% | -1.39 |
| Expired, Invalid, Closed Card, No Account | 121 | 119 | 10.01% | 8.93% | +1.08 |
| Blocked, Restricted, Not Permitted | 25 | 19 | 2.07% | 1.43% | +0.64 |
| 3DS Authentication Failed/Required | 0 | 2 | 0.00% | 0.15% | -0.15 |
| PayPal Declined, Revoked, Payer Issue | 3 | 5 | 0.25% | 0.38% | -0.13 |
| Fraud, Lost/Stolen Card, Security | 0 | 1 | 0.00% | 0.08% | -0.08 |
| CVV/CVC Mismatch | 2 | 2 | 0.17% | 0.15% | +0.02 |

**Root Cause:** Credit + Others

---

## L2: SE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Credit Card | 84.40% | 89.37% | -5.57% | 500 | 687 | ⚠️ |
| Apple Pay | 85.71% | 90.57% | -5.36% | 91 | 106 | ⚠️ |
| Others | 91.56% | 94.11% | -2.71% | 533 | 747 |  |
| Paypal | 92.59% | 91.67% | +1.01% | 27 | 48 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 1,083 | 1,526 | 94.09% | 96.10% | -2.00 |
| Expired, Invalid, Closed Card, No Account | 52 | 51 | 4.52% | 3.21% | +1.31 |
| 3DS Authentication Failed/Required | 10 | 4 | 0.87% | 0.25% | +0.62 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 2 | 0 | 0.17% | 0.00% | +0.17 |
| PayPal Declined, Revoked, Payer Issue | 1 | 3 | 0.09% | 0.19% | -0.10 |
| Blocked, Restricted, Not Permitted | 3 | 4 | 0.26% | 0.25% | +0.01 |

**Root Cause:** Credit + Others

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | Medium (>85%) | 13,668 | 13,786 | +0.9% | Stable |
| FR | Medium (>85%) | 7,143 | 6,932 | -3.0% | Stable |
| DE | High (>92%) | 6,587 | 6,150 | -6.6% | Stable |
| AU | Low (>85%) | 6,062 | 4,052 | -33.2% | ⚠️ Volume drop |
| NL | High (>92%) | 2,329 | 3,135 | +34.6% | Stable |
| DK | High (>92%) | 1,608 | 1,183 | -26.4% | ⚠️ Volume drop |
| SE | Medium (>85%) | 1,588 | 1,151 | -27.5% | ⚠️ Volume drop |
| BE | High (>92%) | 1,536 | 1,627 | +5.9% | Stable |
| NZ | Low (>85%) | 1,333 | 1,209 | -9.3% | Stable |
| IE | Medium (>85%) | 804 | 741 | -7.8% | Stable |
| NO | Medium (>85%) | 574 | 511 | -11.0% | Stable |
| AT | High (>92%) | 346 | 382 | +10.4% | Stable |
| CH | High (>92%) | 46 | 51 | +10.9% | Stable |
| LU | High (>92%) | 37 | 24 | -35.1% | ⚠️ Major mix shift |
| IT | Low (>85%) | 2 | 1 | -50.0% | ⚠️ Volume drop |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| IT | ↓ -100.00% | Credit Card -100.0% | → Stable | Expired, Invalid, Closed Card, No Account +100.00pp | Credit + Expired, |
| CH | ↓ -5.70% | Paypal -8.3% | → Stable | Others +2.17pp | Paypal + Others |
| NZ | ↓ -4.38% | Credit Card -5.1% | → Stable | Others -1.39pp | Credit + Others |
| SE | ↓ -4.08% | Credit Card -5.6% | → Stable | Others -2.00pp | Credit + Others |

---

*Report: 2026-05-12*
