# Reactivation Investigation: RTE 2026-W17

**Metric:** Reactivation Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 89.16% → 87.33% (-2.05%)  
**Volume:** 19,371 orders  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Reactivation Rate declined significantly from 89.16% to 87.33% (-2.05%) in W17, representing the second consecutive weekly decline and the lowest rate in the 8-week trend period.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Sustained decline pattern | -2.05% WoW | ⚠️ |
| L1: Country Scan | 4 countries exceed ±2.5% threshold | YE -13.10%, TO -11.76%, TT -5.13%, TV +7.69% | ⚠️ |
| L1: Payment Method | Apple Pay & Others underperforming | Others -23.56%, Apple Pay -9.53% | ⚠️ |
| L2: YE Deep-Dive | Volume surge with rate collapse | +351.6% volume, -13.10% rate | ⚠️ |
| Mix Shift | YE volume surge from low-rate tier | 306 → 1,382 orders (+351.6%) | ⚠️ |

**Key Findings:**
- YE experienced a massive volume increase (+351.6%, from 306 to 1,382 orders) while its reactivation rate collapsed from 95.42% to 82.92% (-13.10pp), making it the primary driver of the overall decline
- In YE, "Others" payment method declined sharply from 86.67% to 65.31% (-24.65pp) and Credit Card dropped from 96.17% to 81.41% (-15.34pp)
- YE decline reasons show a significant shift: "Expired, Invalid, Closed Card, No Account" increased from 1.31% to 6.15% (+4.84pp) and "Blocked, Restricted, Not Permitted" rose from 0.98% to 3.47% (+2.49pp)
- Apple Pay globally underperformed at 62.85% vs 69.47% prior week (-9.53pp), with 1,946 orders affected
- TO and TT showed rate declines but with minimal volume impact (17 and 39 orders respectively)

**Action:** Investigate — Prioritize YE market investigation focusing on Credit Card and Others payment methods; coordinate with payment provider to understand the surge in card-related declines (expired/invalid cards, blocked transactions) coinciding with the 4x volume increase.

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

*Report: 2026-04-28*
