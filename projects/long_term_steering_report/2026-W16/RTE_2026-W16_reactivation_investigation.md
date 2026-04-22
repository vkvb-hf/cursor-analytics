# Reactivation Investigation: RTE 2026-W16

**Metric:** Reactivation Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 90.41% → 89.16% (-1.38%)  
**Volume:** 18,508 orders  
**Significance:** Significant

## Executive Summary

**Overall:** Reactivation Rate declined from 90.41% to 89.16% (-1.38%) in W16, representing a statistically significant drop across 18,508 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (84.48%-90.41%) | -1.25pp | ✅ |
| L1: Country Breakdown | CF shows significant decline | -4.03% | ⚠️ |
| L1: PaymentMethod | Others shows anomaly (+13.29%) but low volume | -1.56% (Paypal) | ✅ |
| L2: CF Deep-Dive | Credit Card decline driving country drop | -4.67% | ⚠️ |
| Mix Shift | YE volume dropped 78.2% | -78.2% vol | ⚠️ |

**Key Findings:**
- CF experienced the largest negative impact with a -4.03% decline in reactivation rate, driven primarily by Credit Card performance dropping -4.67% (1,955 orders)
- YE saw a dramatic 78.2% volume reduction (1,403 → 306 orders) while paradoxically improving rate by +6.68%, suggesting potential data quality or operational changes
- CF decline reasons show "Expired, Invalid, Closed Card, No Account" increased by +1.23pp and "Blocked, Restricted, Not Permitted" increased by +1.03pp, indicating card validity issues
- FJ, the highest volume country (15,807 orders / 85% of total), showed a moderate decline of -1.32% contributing to overall metric movement
- Small markets (TT, TO) showed positive swings but with volumes under 50 orders, providing minimal offset to the decline

**Action:** Investigate — Focus on CF Credit Card processing issues, specifically the increase in expired/invalid card declines and blocked transactions. Additionally, clarify the cause of the significant volume drop in YE to rule out data pipeline issues.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 89.16% | 18,508 | -1.38% ← REPORTED CHANGE |
| 2026-W15 | 90.41% | 19,757 | +1.36% |
| 2026-W14 | 89.2% | 17,264 | +0.68% |
| 2026-W13 | 88.6% | 19,685 | - |
| 2026-W12 | 88.6% | 20,873 | +1.87% |
| 2026-W11 | 86.97% | 23,790 | +2.19% |
| 2026-W10 | 85.11% | 26,102 | +0.75% |
| 2026-W09 | 84.48% | 24,364 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CF | 87.74% | 91.42% | -4.03% | 2,284 | ⚠️ |
| FJ | 89.17% | 90.36% | -1.32% | 15,807 |  |
| YE | 95.42% | 89.45% | +6.68% | 306 | ⚠️ |
| TT | 100.00% | 90.91% | +10.00% | 45 | ⚠️ |
| TO | 100.00% | 88.89% | +12.50% | 23 | ⚠️ |

**Countries exceeding ±2.5% threshold:** CF, YE, TT, TO

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 91.94% | 93.4% | -1.56% | 2,879 |  |
| Credit Card | 91.3% | 92.71% | -1.52% | 13,671 |  |
| Apple Pay | 69.47% | 68.62% | +1.24% | 1,903 |  |
| Others | 90.91% | 80.25% | +13.29% | 55 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: CF Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Others | 0.00% | 0.00% | +0.00% | 1 | 0 |  |
| Credit Card | 86.96% | 91.21% | -4.67% | 1,955 | 1,764 |  |
| Paypal | 92.68% | 92.83% | -0.16% | 328 | 265 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 2,105 | 1,917 | 92.16% | 94.48% | -2.32 |
| Expired, Invalid, Closed Card, No Account | 81 | 47 | 3.55% | 2.32% | +1.23 |
| Blocked, Restricted, Not Permitted | 72 | 43 | 3.15% | 2.12% | +1.03 |
| PayPal Declined, Revoked, Payer Issue | 21 | 15 | 0.92% | 0.74% | +0.18 |
| Fraud, Lost/Stolen Card, Security | 5 | 6 | 0.22% | 0.30% | -0.08 |
| CVV/CVC Mismatch | 0 | 1 | 0.00% | 0.05% | -0.05 |

**Root Cause:** Others

---

## L2: YE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Paypal | 94.64% | 94.03% | +0.65% | 56 | 402 |  |
| Others | 86.67% | 82.69% | +4.81% | 15 | 156 |  |
| Credit Card | 96.17% | 88.52% | +8.64% | 235 | 845 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 296 | 1,293 | 96.73% | 92.16% | +4.57 |
| Expired, Invalid, Closed Card, No Account | 4 | 54 | 1.31% | 3.85% | -2.54 |
| Blocked, Restricted, Not Permitted | 3 | 37 | 0.98% | 2.64% | -1.66 |
| PayPal Declined, Revoked, Payer Issue | 1 | 16 | 0.33% | 1.14% | -0.81 |
| 3DS Authentication Failed/Required | 1 | 0 | 0.33% | 0.00% | +0.33 |
| CVV/CVC Mismatch | 1 | 3 | 0.33% | 0.21% | +0.11 |

**Root Cause:** Credit + Others

---

## L2: TT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 100.00% | 0.00% | +0.00% | 2 | 0 |  |
| Paypal | 100.00% | 100.00% | +0.00% | 4 | 4 |  |
| Others | 100.00% | 95.24% | +5.00% | 30 | 21 |  |
| Credit Card | 100.00% | 75.00% | +33.33% | 9 | 8 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Expired, Invalid, Closed Card, No Account | 0 | 1 | 0.00% | 3.03% | -3.03 |
| Others | 45 | 32 | 100.00% | 96.97% | +3.03 |

**Root Cause:** Credit + Expired,

---

## L2: TO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 0.00% | 66.67% | -100.00% | 0 | 3 | ⚠️ |
| Credit Card | 100.00% | 100.00% | +0.00% | 17 | 8 |  |
| Paypal | 100.00% | 100.00% | +0.00% | 5 | 4 |  |
| Others | 100.00% | 66.67% | +50.00% | 1 | 3 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Expired, Invalid, Closed Card, No Account | 0 | 2 | 0.00% | 11.11% | -11.11 |
| Others | 23 | 16 | 100.00% | 88.89% | +11.11 |

**Root Cause:** Apple + Expired,

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | Medium (>85%) | 16,241 | 15,807 | -2.7% | Stable |
| CF | Medium (>85%) | 2,029 | 2,284 | +12.6% | Stable |
| YE | Medium (>85%) | 1,403 | 306 | -78.2% | ⚠️ Volume drop |
| TT | Medium (>85%) | 33 | 45 | +36.4% | Stable |
| TZ | High (>92%) | 19 | 26 | +36.8% | Stable |
| TO | Medium (>85%) | 18 | 23 | +27.8% | Stable |
| TV | Medium (>85%) | 12 | 14 | +16.7% | Stable |
| TK | High (>92%) | 2 | 3 | +50.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| CF | ↓ -4.03% | → Stable | → Stable | Others -2.32pp | Others |
| YE | ↑ +6.68% | Credit Card +8.6% | → Stable | Others +4.57pp | Credit + Others |
| TT | ↑ +10.00% | Credit Card +33.3% | → Stable | Expired, Invalid, Closed Card, No Account -3.03pp | Credit + Expired, |
| TO | ↑ +12.50% | Apple Pay -100.0% | → Stable | Expired, Invalid, Closed Card, No Account -11.11pp | Apple + Expired, |

---

*Report: 2026-04-22*
