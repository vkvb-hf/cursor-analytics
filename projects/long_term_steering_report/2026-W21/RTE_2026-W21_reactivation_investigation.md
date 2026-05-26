# Reactivation Investigation: RTE 2026-W21

**Metric:** Reactivation Rate  
**Period:** 2026-W20 → 2026-W21  
**Observation:** 89.27% → 89.38% (+0.12%)  
**Volume:** 17,485 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Reactivation rate showed a marginal improvement from 89.27% to 89.38% (+0.12pp) in W21, representing a statistically insignificant change across 17,485 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (87-90%) | +0.12pp | ✅ |
| L1: Country Breakdown | 3 countries exceed ±2.5% threshold | TV -27.78pp, TT -10.00pp, TO +3.64pp | ⚠️ |
| L1: PaymentMethod | 1 dimension flagged | Apple Pay +3.09pp | ⚠️ |
| L2: TV Deep-Dive | Severe drop, ultra-low volume | -27.78pp (6 orders) | ⚠️ |
| L2: TT Deep-Dive | Moderate drop, low volume | -10.00pp (20 orders) | ⚠️ |
| L2: TO Deep-Dive | Improvement, low volume | +3.64pp (22 orders) | ✅ |
| Mix Shift | Major shifts in TV, TZ, TK | Volume drops 38-60% | ⚠️ |

**Key Findings:**
- TV experienced a -27.78pp decline driven by "Others" payment method (-66.67%) with only 6 orders total, making this statistically unreliable
- TT saw a -10.00pp drop with Credit Card performance falling from 100% to 50% (only 2 orders), root cause attributed to Credit Card issues
- Major volume mix shifts occurred in low-volume countries: TV (-53.8%), TK (-60.0%), and TZ (-37.5%), but combined these represent <25 orders
- Core markets FJ (12,709 orders) and YE (2,705 orders) remained stable at +0.06pp and +1.29pp respectively, representing 88% of total volume
- Apple Pay showed a +3.09pp improvement globally (1,572 orders), contributing positively to overall rate

**Action:** Monitor — The +0.12pp change is not statistically significant, and flagged countries (TV, TT, TO) represent <0.3% of total volume (48 orders combined). No immediate action required.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W21 | 89.38% | 17,485 | +0.12% ← REPORTED CHANGE |
| 2026-W20 | 89.27% | 18,697 | +0.29% |
| 2026-W19 | 89.01% | 20,405 | +2.26% |
| 2026-W18 | 87.04% | 19,909 | -0.33% |
| 2026-W17 | 87.33% | 19,371 | -2.05% |
| 2026-W16 | 89.16% | 18,508 | -1.38% |
| 2026-W15 | 90.41% | 19,757 | +1.36% |
| 2026-W14 | 89.2% | 17,264 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TV | 66.67% | 92.31% | -27.78% | 6 | ⚠️ |
| TT | 90.00% | 100.00% | -10.00% | 20 | ⚠️ |
| CF | 92.42% | 92.67% | -0.26% | 2,006 |  |
| FJ | 89.09% | 89.03% | +0.06% | 12,709 |  |
| YE | 88.50% | 87.37% | +1.29% | 2,705 |  |
| TO | 86.36% | 83.33% | +3.64% | 22 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TV, TT, TO

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 77.11% | 77.95% | -1.08% | 284 |  |
| Credit Card | 91.38% | 91.52% | -0.15% | 12,547 |  |
| Paypal | 93.45% | 93.21% | +0.25% | 3,082 |  |
| Apple Pay | 67.62% | 65.59% | +3.09% | 1,572 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: TV Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 100.00% | 0.00% | +0.00% | 1 | 0 |  |
| Others | 33.33% | 100.00% | -66.67% | 3 | 4 | ⚠️ |
| Credit Card | 100.00% | 88.89% | +12.50% | 2 | 9 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 3DS Authentication Failed/Required | 0 | 1 | 0.00% | 7.69% | -7.69 |
| Others | 6 | 12 | 100.00% | 92.31% | +7.69 |

**Root Cause:** Others + 3DS

---

## L2: TT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Paypal | 100.00% | 0.00% | +0.00% | 3 | 0 |  |
| Credit Card | 50.00% | 100.00% | -50.00% | 2 | 6 | ⚠️ |
| Others | 92.31% | 100.00% | -7.69% | 13 | 20 | ⚠️ |
| Apple Pay | 100.00% | 100.00% | +0.00% | 2 | 1 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 20 | 27 | 100.00% | 100.00% | +0.00 |

**Root Cause:** Credit

---

## L2: TO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 100.00% | 0.00% | +0.00% | 2 | 1 |  |
| Others | 66.67% | 0.00% | +0.00% | 3 | 1 |  |
| Paypal | 87.50% | 100.00% | -12.50% | 8 | 5 | ⚠️ |
| Credit Card | 88.89% | 90.91% | -2.22% | 9 | 11 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 21 | 16 | 95.45% | 88.89% | +6.57 |
| Expired, Invalid, Closed Card, No Account | 0 | 1 | 0.00% | 5.56% | -5.56 |
| Fraud, Lost/Stolen Card, Security | 0 | 1 | 0.00% | 5.56% | -5.56 |
| PayPal Declined, Revoked, Payer Issue | 1 | 0 | 4.55% | 0.00% | +4.55 |

**Root Cause:** Paypal + Others

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | Medium (>85%) | 14,144 | 12,709 | -10.1% | Stable |
| YE | Medium (>85%) | 2,352 | 2,705 | +15.0% | Stable |
| CF | High (>92%) | 2,114 | 2,006 | -5.1% | Stable |
| TT | High (>92%) | 27 | 20 | -25.9% | ⚠️ Volume drop |
| TZ | High (>92%) | 24 | 15 | -37.5% | ⚠️ Major mix shift |
| TO | Low (>85%) | 18 | 22 | +22.2% | Stable |
| TV | High (>92%) | 13 | 6 | -53.8% | ⚠️ Major mix shift |
| TK | High (>92%) | 5 | 2 | -60.0% | ⚠️ Major mix shift |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TV | ↓ -27.78% | Others -66.7% | → Stable | 3DS Authentication Failed/Required -7.69pp | Others + 3DS |
| TT | ↓ -10.00% | Credit Card -50.0% | → Stable | → Stable | Credit |
| TO | ↑ +3.64% | Paypal -12.5% | → Stable | Others +6.57pp | Paypal + Others |

---

*Report: 2026-05-26*
