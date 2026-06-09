# Reactivation Investigation: RTE 2026-W23

**Metric:** Reactivation Rate  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 89.71% → 89.99% (+0.31%)  
**Volume:** 20,228 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Reactivation rate improved marginally from 89.71% to 89.99% (+0.28pp), a statistically non-significant change within normal weekly fluctuation.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Stable upward trend since W19 | +0.31% | ✅ |
| L1: Country Breakdown | 3 countries flagged (TK, TO, TV) | Mixed | ⚠️ |
| L1: Dimension Scan | Others payment method +5.64% | Low volume (351) | ✅ |
| L2: TK Deep-Dive | Apple Pay -33.33% | 9 orders total | ⚠️ |
| L2: TO Deep-Dive | Credit Card -10.00% | 38 orders total | ⚠️ |
| L2: TV Deep-Dive | PayPal -100.00% (0 orders) | 29 orders total | ⚠️ |
| Mix Shift | All countries stable impact | No material shifts | ✅ |

**Key Findings:**
- TK experienced -11.11pp decline driven by Apple Pay failures (3 orders) with "Expired, Invalid, Closed Card, No Account" decline reason increasing by +11.11pp
- TO declined -7.89pp due to Credit Card performance dropping from 100% to 90% (20 orders), with new "Blocked, Restricted, Not Permitted" declines appearing
- TV improved +3.45pp despite PayPal dropping from 1 order to 0; the gain came from Credit Card and Others maintaining 100% rates
- All flagged countries have extremely low volumes (TK: 9, TO: 38, TV: 29 orders), making rate swings statistically unreliable
- Overall trend shows consistent recovery from W18 low of 87.04% to current 89.99% over 5 weeks

**Action:** Monitor — No action required. The +0.28pp change is not statistically significant, and flagged country variations are driven by volumes under 50 orders where single-order outcomes cause large rate swings.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W23 | 89.99% | 20,228 | +0.31% ← REPORTED CHANGE |
| 2026-W22 | 89.71% | 19,183 | +0.37% |
| 2026-W21 | 89.38% | 17,485 | +0.12% |
| 2026-W20 | 89.27% | 18,697 | +0.29% |
| 2026-W19 | 89.01% | 20,405 | +2.26% |
| 2026-W18 | 87.04% | 19,909 | -0.33% |
| 2026-W17 | 87.33% | 19,371 | -2.05% |
| 2026-W16 | 89.16% | 18,508 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TK | 88.89% | 100.00% | -11.11% | 9 | ⚠️ |
| TO | 92.11% | 100.00% | -7.89% | 38 | ⚠️ |
| TT | 92.11% | 93.55% | -1.54% | 76 |  |
| YE | 86.90% | 87.50% | -0.68% | 2,703 |  |
| CF | 92.11% | 91.83% | +0.30% | 2,318 |  |
| FJ | 90.17% | 89.71% | +0.51% | 14,996 |  |
| TV | 96.55% | 93.33% | +3.45% | 29 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TK, TO, TV

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Paypal | 92.39% | 93.01% | -0.67% | 3,495 |  |
| Apple Pay | 68.19% | 68.25% | -0.09% | 1,688 |  |
| Credit Card | 92.24% | 91.88% | +0.40% | 14,694 |  |
| Others | 76.64% | 72.55% | +5.64% | 351 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: TK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 66.67% | 100.00% | -33.33% | 3 | 4 | ⚠️ |
| Credit Card | 100.00% | 100.00% | +0.00% | 6 | 6 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Expired, Invalid, Closed Card, No Account | 1 | 0 | 11.11% | 0.00% | +11.11 |
| Others | 8 | 10 | 88.89% | 100.00% | -11.11 |

**Root Cause:** Apple + Expired,

---

## L2: TO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 75.00% | 0.00% | +0.00% | 4 | 0 |  |
| Credit Card | 90.00% | 100.00% | -10.00% | 20 | 12 | ⚠️ |
| Others | 100.00% | 100.00% | +0.00% | 3 | 8 |  |
| Paypal | 100.00% | 100.00% | +0.00% | 11 | 5 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 36 | 25 | 94.74% | 100.00% | -5.26 |
| Blocked, Restricted, Not Permitted | 1 | 0 | 2.63% | 0.00% | +2.63 |
| Expired, Invalid, Closed Card, No Account | 1 | 0 | 2.63% | 0.00% | +2.63 |

**Root Cause:** Credit + Others

---

## L2: TV Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Paypal | 0.00% | 100.00% | -100.00% | 0 | 1 | ⚠️ |
| Apple Pay | 66.67% | 80.00% | -16.67% | 3 | 5 | ⚠️ |
| Credit Card | 100.00% | 100.00% | +0.00% | 9 | 4 |  |
| Others | 100.00% | 100.00% | +0.00% | 17 | 5 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 29 | 15 | 100.00% | 100.00% | +0.00 |

**Root Cause:** Paypal

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | Medium (>85%) | 13,682 | 14,996 | +9.6% | Stable |
| YE | Medium (>85%) | 2,792 | 2,703 | -3.2% | Stable |
| CF | Medium (>85%) | 2,570 | 2,318 | -9.8% | Stable |
| TT | High (>92%) | 62 | 76 | +22.6% | Stable |
| TZ | High (>92%) | 27 | 59 | +118.5% | Stable |
| TO | High (>92%) | 25 | 38 | +52.0% | Stable |
| TV | High (>92%) | 15 | 29 | +93.3% | Stable |
| TK | High (>92%) | 10 | 9 | -10.0% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TK | ↓ -11.11% | Apple Pay -33.3% | → Stable | Expired, Invalid, Closed Card, No Account +11.11pp | Apple + Expired, |
| TO | ↓ -7.89% | Credit Card -10.0% | → Stable | Others -5.26pp | Credit + Others |
| TV | ↑ +3.45% | Paypal -100.0% | → Stable | → Stable | Paypal |

---

*Report: 2026-06-09*
