# Reactivation Investigation: RTE 2026-W19

**Metric:** Reactivation Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 87.04% → 89.01% (+2.26%)  
**Volume:** 20,405 orders  
**Significance:** Significant

## Executive Summary

**Overall:** Reactivation Rate improved significantly from 87.04% to 89.01% (+2.26%) in W19, representing a positive recovery after two consecutive weeks of decline.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (88.6%-90.4%) | +2.26% | ✅ |
| L1: Country Breakdown | 4 countries exceed ±2.5% threshold (YE, TT, CF, TV) | +5.23% to +50.00% | ⚠️ |
| L1: Dimension Scan | PaymentMethod "Others" flagged at +3.17% | +3.17% | ⚠️ |
| L2: Deep-Dives | Credit Card driving improvements in YE, CF; low-volume anomalies in TT, TV | Varies | ⚠️ |
| Mix Shift | TT volume dropped -22.9%; YE volume increased +23.2% | Volume shifts | ⚠️ |

**Key Findings:**
- YE showed strong improvement (+5.23%) driven by Credit Card (+7.46%) and Others payment methods (+6.33%), with volume increasing 23.2% (2,297 → 2,830 orders)
- CF improved +7.22% primarily through Credit Card performance (+7.92%), with decline in "Expired, Invalid, Closed Card, No Account" reasons (-2.43pp)
- TV and TT show dramatic percentage changes (+50.00% and +6.14% respectively) but are statistically unreliable due to extremely low volumes (11 and 37 orders)
- The "Others" decline reason category increased across multiple countries, suggesting improved handling of previously uncategorized decline scenarios
- FJ, the highest-volume country (15,339 orders, 75% of total), showed modest improvement (+1.41%) providing stable baseline performance

**Action:** Monitor - The improvement is positive and returns the metric to historical norms. Continue tracking YE and CF Credit Card performance to confirm sustainability; no immediate escalation required given low-volume markets (TV, TT) are not materially impacting overall results.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W19 | 89.01% | 20,405 | +2.26% ← REPORTED CHANGE |
| 2026-W18 | 87.04% | 19,909 | -0.33% |
| 2026-W17 | 87.33% | 19,371 | -2.05% |
| 2026-W16 | 89.16% | 18,508 | -1.38% |
| 2026-W15 | 90.41% | 19,757 | +1.36% |
| 2026-W14 | 89.2% | 17,264 | +0.68% |
| 2026-W13 | 88.6% | 19,685 | - |
| 2026-W12 | 88.6% | 20,873 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| FJ | 89.76% | 88.51% | +1.41% | 15,339 |  |
| YE | 83.29% | 79.15% | +5.23% | 2,830 | ⚠️ |
| TT | 97.30% | 91.67% | +6.14% | 37 | ⚠️ |
| CF | 90.81% | 84.70% | +7.22% | 2,133 | ⚠️ |
| TV | 100.00% | 66.67% | +50.00% | 11 | ⚠️ |

**Countries exceeding ±2.5% threshold:** YE, TT, CF, TV

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 93.28% | 92.12% | +1.26% | 3,556 |  |
| Apple Pay | 67.86% | 66.55% | +1.97% | 1,789 |  |
| Credit Card | 90.99% | 89.0% | +2.24% | 14,702 |  |
| Others | 70.67% | 68.5% | +3.17% | 358 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: YE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Paypal | 93.35% | 92.42% | +1.00% | 827 | 660 |  |
| Others | 71.75% | 67.47% | +6.33% | 361 | 289 | ⚠️ |
| Credit Card | 80.76% | 75.15% | +7.46% | 1,642 | 1,348 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 2,501 | 1,969 | 88.37% | 85.72% | +2.65 |
| Expired, Invalid, Closed Card, No Account | 178 | 192 | 6.29% | 8.36% | -2.07 |
| Blocked, Restricted, Not Permitted | 106 | 92 | 3.75% | 4.01% | -0.26 |
| Fraud, Lost/Stolen Card, Security | 1 | 5 | 0.04% | 0.22% | -0.18 |
| PayPal Declined, Revoked, Payer Issue | 44 | 39 | 1.55% | 1.70% | -0.14 |

**Root Cause:** Others + Others

---

## L2: TT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 100.00% | 100.00% | +0.00% | 2 | 4 |  |
| Paypal | 100.00% | 100.00% | +0.00% | 3 | 2 |  |
| Others | 96.00% | 91.43% | +5.00% | 25 | 35 |  |
| Credit Card | 100.00% | 85.71% | +16.67% | 7 | 7 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Expired, Invalid, Closed Card, No Account | 0 | 1 | 0.00% | 2.08% | -2.08 |
| Others | 37 | 47 | 100.00% | 97.92% | +2.08 |

**Root Cause:** Credit + Expired,

---

## L2: CF Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Paypal | 94.27% | 91.79% | +2.70% | 314 | 280 |  |
| Credit Card | 90.21% | 83.59% | +7.92% | 1,819 | 1,798 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 2,009 | 1,875 | 94.19% | 90.23% | +3.96 |
| Expired, Invalid, Closed Card, No Account | 56 | 105 | 2.63% | 5.05% | -2.43 |
| Blocked, Restricted, Not Permitted | 48 | 72 | 2.25% | 3.46% | -1.21 |
| PayPal Declined, Revoked, Payer Issue | 14 | 17 | 0.66% | 0.82% | -0.16 |
| Fraud, Lost/Stolen Card, Security | 6 | 9 | 0.28% | 0.43% | -0.15 |

**Root Cause:** Credit + Others

---

## L2: TV Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 100.00% | 0.00% | +0.00% | 2 | 0 |  |
| Paypal | 100.00% | 0.00% | +0.00% | 1 | 0 |  |
| Others | 100.00% | 77.78% | +28.57% | 6 | 9 | ⚠️ |
| Credit Card | 100.00% | 33.33% | +200.00% | 2 | 3 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 11 | 12 | 100.00% | 100.00% | +0.00 |

**Root Cause:** Others

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | Medium (>85%) | 15,428 | 15,339 | -0.6% | Stable |
| YE | Low (>85%) | 2,297 | 2,830 | +23.2% | Stable |
| CF | Low (>85%) | 2,078 | 2,133 | +2.6% | Stable |
| TT | Medium (>85%) | 48 | 37 | -22.9% | ⚠️ Volume drop |
| TZ | High (>92%) | 25 | 21 | -16.0% | Stable |
| TO | Medium (>85%) | 19 | 30 | +57.9% | Stable |
| TV | Low (>85%) | 12 | 11 | -8.3% | Stable |
| TK | High (>92%) | 2 | 4 | +100.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| YE | ↑ +5.23% | Others +6.3% | → Stable | Others +2.65pp | Others + Others |
| TT | ↑ +6.14% | Credit Card +16.7% | → Stable | Expired, Invalid, Closed Card, No Account -2.08pp | Credit + Expired, |
| CF | ↑ +7.22% | Credit Card +7.9% | → Stable | Others +3.96pp | Credit + Others |
| TV | ↑ +50.00% | Others +28.6% | → Stable | → Stable | Others |

---

*Report: 2026-05-12*
