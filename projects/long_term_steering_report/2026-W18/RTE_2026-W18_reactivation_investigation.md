# Reactivation Investigation: RTE 2026-W18

**Metric:** Reactivation Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 87.33% → 87.04% (-0.33%)  
**Volume:** 19,909 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Reactivation Rate declined slightly from 87.33% to 87.04% (-0.29pp) in W18, a statistically non-significant change affecting 19,909 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range | -0.33% | ✅ |
| L1: Country Breakdown | 3 countries exceed ±2.5% threshold | TV -33.33%, YE -4.55%, TT -3.38% | ⚠️ |
| L1: Dimension Scan | Apple Pay shows positive movement | +5.89% | ✅ |
| L2: TV Deep-Dive | Severe decline but minimal volume | 12 orders total | ⚠️ |
| L2: YE Deep-Dive | Credit Card underperformance | -7.70% on 1,348 orders | ⚠️ |
| L2: TT Deep-Dive | Others payment method decline | -5.71% on 35 orders | ⚠️ |
| Mix Shift | YE volume increased significantly | +66.2% | ✅ |

**Key Findings:**
- TV experienced a -33.33pp rate drop driven by Apple Pay (0% from 100%), but with only 12 total orders the impact is negligible
- YE shows the most material concern: Credit Card reactivation fell -7.70pp (75.15% vs 81.41%) on 1,348 orders, with "Expired, Invalid, Closed Card, No Account" decline reasons increasing +2.21pp
- YE volume surged +66.2% (1,382 → 2,297 orders), meaning more transactions are flowing through a lower-performing segment
- TT decline (-3.38pp) is driven by "Others" payment method dropping -5.71pp, though volume remains minimal at 48 orders
- Overall 8-week trend shows a gradual decline from 89.16% (W16) to 87.04% (W18), suggesting a sustained downward pattern

**Action:** Monitor - The W18 change is not statistically significant and the largest country declines (TV, TT) involve minimal volume. However, continue monitoring YE Credit Card performance given the volume increase and elevated card expiration/invalid card decline reasons. If YE Credit Card rate continues below 78% for two consecutive weeks, escalate for provider review.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W18 | 87.04% | 19,909 | -0.33% ← REPORTED CHANGE |
| 2026-W17 | 87.33% | 19,371 | -2.05% |
| 2026-W16 | 89.16% | 18,508 | -1.38% |
| 2026-W15 | 90.41% | 19,757 | +1.36% |
| 2026-W14 | 89.2% | 17,264 | +0.68% |
| 2026-W13 | 88.6% | 19,685 | - |
| 2026-W12 | 88.6% | 20,873 | +1.87% |
| 2026-W11 | 86.97% | 23,790 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TV | 66.67% | 100.00% | -33.33% | 12 | ⚠️ |
| YE | 79.15% | 82.92% | -4.55% | 2,297 | ⚠️ |
| TT | 91.67% | 94.87% | -3.38% | 48 | ⚠️ |
| CF | 84.70% | 86.19% | -1.73% | 2,078 |  |
| FJ | 88.51% | 87.82% | +0.79% | 15,428 |  |

**Countries exceeding ±2.5% threshold:** TV, YE, TT

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 68.5% | 69.49% | -1.42% | 327 |  |
| Credit Card | 89.0% | 89.94% | -1.05% | 14,127 |  |
| Paypal | 92.12% | 91.68% | +0.48% | 3,527 |  |
| Apple Pay | 66.55% | 62.85% | +5.89% | 1,928 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: TV Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 0.00% | 100.00% | -100.00% | 0 | 1 | ⚠️ |
| Credit Card | 33.33% | 100.00% | -66.67% | 3 | 5 | ⚠️ |
| Others | 77.78% | 100.00% | -22.22% | 9 | 4 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 12 | 10 | 100.00% | 100.00% | +0.00 |

**Root Cause:** Apple

---

## L2: YE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Credit Card | 75.15% | 81.41% | -7.70% | 1,348 | 834 | ⚠️ |
| Paypal | 92.42% | 92.52% | -0.10% | 660 | 401 |  |
| Others | 67.47% | 65.31% | +3.32% | 289 | 147 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 1,969 | 1,220 | 85.72% | 88.28% | -2.56 |
| Expired, Invalid, Closed Card, No Account | 192 | 85 | 8.36% | 6.15% | +2.21 |
| Blocked, Restricted, Not Permitted | 92 | 48 | 4.01% | 3.47% | +0.53 |
| PayPal Declined, Revoked, Payer Issue | 39 | 28 | 1.70% | 2.03% | -0.33 |
| Fraud, Lost/Stolen Card, Security | 5 | 1 | 0.22% | 0.07% | +0.15 |

**Root Cause:** Credit + Others

---

## L2: TT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Others | 91.43% | 96.97% | -5.71% | 35 | 33 | ⚠️ |
| Apple Pay | 100.00% | 100.00% | +0.00% | 4 | 1 |  |
| Paypal | 100.00% | 100.00% | +0.00% | 2 | 1 |  |
| Credit Card | 85.71% | 75.00% | +14.29% | 7 | 4 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Expired, Invalid, Closed Card, No Account | 1 | 0 | 2.08% | 0.00% | +2.08 |
| Others | 47 | 39 | 97.92% | 100.00% | -2.08 |

**Root Cause:** Others + Expired,

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | Medium (>85%) | 15,915 | 15,428 | -3.1% | Stable |
| CF | Medium (>85%) | 1,991 | 2,078 | +4.4% | Stable |
| YE | Low (>85%) | 1,382 | 2,297 | +66.2% | Stable |
| TT | High (>92%) | 39 | 48 | +23.1% | Stable |
| TO | Medium (>85%) | 17 | 19 | +11.8% | Stable |
| TZ | High (>92%) | 14 | 25 | +78.6% | Stable |
| TV | High (>92%) | 10 | 12 | +20.0% | Stable |
| TK | High (>92%) | 3 | 2 | -33.3% | ⚠️ Major mix shift |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TV | ↓ -33.33% | Apple Pay -100.0% | → Stable | → Stable | Apple |
| YE | ↓ -4.55% | Credit Card -7.7% | → Stable | Others -2.56pp | Credit + Others |
| TT | ↓ -3.38% | Others -5.7% | → Stable | Expired, Invalid, Closed Card, No Account +2.08pp | Others + Expired, |

---

*Report: 2026-05-05*
