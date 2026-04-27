# Reactivation Investigation: RTE 2026-W17

**Metric:** Reactivation Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 89.16% → 87.33% (-2.05%)  
**Volume:** 19,371 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Reactivation Rate declined significantly from 89.16% to 87.33% (-2.05%, -1.83pp) in W17, representing the second consecutive weekly decline and dropping the metric to its lowest point in the 8-week trend window.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Consecutive decline W16→W17 | -2.05% | ⚠️ |
| L1: Country Breakdown | 4 countries exceed ±2.5% threshold | YE -13.10%, TO -11.76%, TT -5.13%, TV +7.69% | ⚠️ |
| L1: PaymentMethod | 2 methods flagged | Others -23.56%, Apple Pay -9.53% | ⚠️ |
| L2: YE Deep-Dive | Major volume increase with rate collapse | +351.6% volume, -13.10% rate | ⚠️ |
| Mix Shift | YE shifted from low to high volume | 306 → 1,382 orders (+351.6%) | ⚠️ |

**Key Findings:**
- YE is the primary driver of the decline: volume surged 351.6% (306 → 1,382 orders) while reactivation rate collapsed from 95.42% to 82.92% (-13.10%), with "Expired, Invalid, Closed Card, No Account" decline reasons increasing by +4.84pp
- "Others" payment method shows severe degradation globally (-23.56%) and within YE specifically (-24.65%), indicating a potential issue with alternative payment processing
- Apple Pay reactivation rate dropped significantly from 69.47% to 62.85% (-9.53%) across 1,946 orders, contributing materially to the overall decline
- Credit Card performance in YE deteriorated sharply (-15.34%) despite being the highest volume method (834 orders), with "Blocked, Restricted, Not Permitted" reasons increasing by +2.49pp
- TO and TT show rate declines but with minimal volume impact (17 and 39 orders respectively)

**Action:** Investigate — The significant volume surge in YE combined with degraded reactivation performance across multiple payment methods suggests a systemic issue requiring immediate root cause analysis, particularly focusing on card validity and payment method processing in the YE market.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W17 | 87.33% | 19,371 | -2.05% ← REPORTED CHANGE |
| 2026-W16 | 89.16% | 18,508 | -1.38% |
| 2026-W15 | 90.41% | 19,757 | +1.36% |
| 2026-W14 | 89.2% | 17,264 | +0.68% |
| 2026-W13 | 88.6% | 19,685 | - |
| 2026-W12 | 88.6% | 20,873 | +1.87% |
| 2026-W11 | 86.97% | 23,790 | +2.19% |
| 2026-W10 | 85.11% | 26,102 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| YE | 82.92% | 95.42% | -13.10% | 1,382 | ⚠️ |
| TO | 88.24% | 100.00% | -11.76% | 17 | ⚠️ |
| TT | 94.87% | 100.00% | -5.13% | 39 | ⚠️ |
| CF | 86.19% | 87.74% | -1.77% | 1,991 |  |
| FJ | 87.82% | 89.17% | -1.52% | 15,915 |  |
| TV | 100.00% | 92.86% | +7.69% | 10 | ⚠️ |

**Countries exceeding ±2.5% threshold:** YE, TO, TT, TV

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 69.49% | 90.91% | -23.56% | 177 | ⚠️ |
| Apple Pay | 62.85% | 69.47% | -9.53% | 1,946 | ⚠️ |
| Credit Card | 89.94% | 91.3% | -1.49% | 13,930 |  |
| Paypal | 91.68% | 91.94% | -0.28% | 3,318 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: YE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Others | 65.31% | 86.67% | -24.65% | 147 | 15 | ⚠️ |
| Credit Card | 81.41% | 96.17% | -15.34% | 834 | 235 | ⚠️ |
| Paypal | 92.52% | 94.64% | -2.24% | 401 | 56 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 1,220 | 296 | 88.28% | 96.73% | -8.45 |
| Expired, Invalid, Closed Card, No Account | 85 | 4 | 6.15% | 1.31% | +4.84 |
| Blocked, Restricted, Not Permitted | 48 | 3 | 3.47% | 0.98% | +2.49 |
| PayPal Declined, Revoked, Payer Issue | 28 | 1 | 2.03% | 0.33% | +1.70 |
| 3DS Authentication Failed/Required | 0 | 1 | 0.00% | 0.33% | -0.33 |
| CVV/CVC Mismatch | 0 | 1 | 0.00% | 0.33% | -0.33 |
| Fraud, Lost/Stolen Card, Security | 1 | 0 | 0.07% | 0.00% | +0.07 |

**Root Cause:** Others + Others

---

## L2: TO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 66.67% | 0.00% | +0.00% | 3 | 0 |  |
| Others | 0.00% | 100.00% | -100.00% | 0 | 1 | ⚠️ |
| Credit Card | 90.00% | 100.00% | -10.00% | 10 | 17 | ⚠️ |
| Paypal | 100.00% | 100.00% | +0.00% | 4 | 5 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 17 | 23 | 100.00% | 100.00% | +0.00 |

**Root Cause:** Others

---

## L2: TT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Credit Card | 75.00% | 100.00% | -25.00% | 4 | 9 | ⚠️ |
| Others | 96.97% | 100.00% | -3.03% | 33 | 30 |  |
| Apple Pay | 100.00% | 100.00% | +0.00% | 1 | 2 |  |
| Paypal | 100.00% | 100.00% | +0.00% | 1 | 4 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 39 | 45 | 100.00% | 100.00% | +0.00 |

**Root Cause:** Credit

---

## L2: TV Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 100.00% | 100.00% | +0.00% | 1 | 3 |  |
| Credit Card | 100.00% | 100.00% | +0.00% | 5 | 3 |  |
| Others | 100.00% | 87.50% | +14.29% | 4 | 8 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 10 | 14 | 100.00% | 100.00% | +0.00 |

**Root Cause:** Others

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | Medium (>85%) | 15,807 | 15,915 | +0.7% | Stable |
| CF | Medium (>85%) | 2,284 | 1,991 | -12.8% | Stable |
| YE | High (>92%) | 306 | 1,382 | +351.6% | Stable |
| TT | High (>92%) | 45 | 39 | -13.3% | Stable |
| TZ | High (>92%) | 26 | 14 | -46.2% | ⚠️ Major mix shift |
| TO | High (>92%) | 23 | 17 | -26.1% | ⚠️ Volume drop |
| TV | High (>92%) | 14 | 10 | -28.6% | ⚠️ Volume drop |
| TK | High (>92%) | 3 | 3 | +0.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| YE | ↓ -13.10% | Others -24.6% | → Stable | Others -8.45pp | Others + Others |
| TO | ↓ -11.76% | Others -100.0% | → Stable | → Stable | Others |
| TT | ↓ -5.13% | Credit Card -25.0% | → Stable | → Stable | Credit |
| TV | ↑ +7.69% | Others +14.3% | → Stable | → Stable | Others |

---

*Report: 2026-04-27*
