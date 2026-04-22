# Reactivation Investigation: HF-INTL 2026-W16

**Metric:** Reactivation Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 91.47% → 91.23% (-0.26%)  
**Volume:** 46,003 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** HF-INTL Reactivation Rate declined slightly from 91.47% to 91.23% (-0.24pp) in W16, a change that is not statistically significant given the 46,003 order volume.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (90.03%-91.47%) | -0.24pp | ✅ |
| L1: Country Breakdown | CH flagged at -4.69%, LU at +3.03% | ±2.5% threshold | ⚠️ |
| L1: Dimension Scan | PaymentMethod stable, no flags | Max -1.33pp | ✅ |
| L2: CH Deep-Dive | Apple Pay -20.00%, Credit Card -5.38% | Low volume (55) | ⚠️ |
| L2: LU Deep-Dive | Apple Pay +11.11% improvement | Low volume (37) | ✅ |
| Mix Shift | DK volume drop -23.9% | Stable impact | ✅ |

**Key Findings:**
- CH experienced a -4.69pp rate decline driven by Apple Pay (-20.00pp) and Credit Card (-5.38pp), but total volume is only 55 orders, limiting statistical significance
- LU showed improvement (+3.03pp) with Apple Pay recovering from 90.00% to 100.00%, though on minimal volume (37 orders)
- GB, the largest market (16,889 orders), declined -1.90pp but remains within acceptable range at 89.32%
- DK experienced a -23.9% volume drop (1,776 → 1,352) while rate improved slightly (+0.68pp)
- Overall 8-week trend shows W16 rate (91.23%) remains the highest in the period despite the week-over-week decline

**Action:** Monitor — The -0.24pp decline is not statistically significant and the flagged countries (CH, LU) have insufficient volume to warrant investigation. Continue standard monitoring with attention to GB performance given its volume contribution.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 91.23% | 46,003 | -0.26% ← REPORTED CHANGE |
| 2026-W15 | 91.47% | 41,652 | +0.60% |
| 2026-W14 | 90.92% | 32,555 | +0.99% |
| 2026-W13 | 90.03% | 43,179 | -0.19% |
| 2026-W12 | 90.2% | 42,003 | -0.20% |
| 2026-W11 | 90.38% | 45,133 | +0.33% |
| 2026-W10 | 90.08% | 48,534 | -0.90% |
| 2026-W09 | 90.9% | 55,010 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CH | 83.64% | 87.76% | -4.69% | 55 | ⚠️ |
| GB | 89.32% | 91.05% | -1.90% | 16,889 |  |
| FR | 88.70% | 88.98% | -0.32% | 4,681 |  |
| DK | 92.46% | 91.84% | +0.68% | 1,352 |  |
| NZ | 81.68% | 80.60% | +1.34% | 1,392 |  |
| AT | 95.89% | 94.29% | +1.71% | 414 |  |
| LU | 100.00% | 97.06% | +3.03% | 37 | ⚠️ |

**Countries exceeding ±2.5% threshold:** CH, LU

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Apple Pay | 91.29% | 92.51% | -1.33% | 8,090 |  |
| Credit Card | 86.09% | 86.79% | -0.81% | 20,152 |  |
| Paypal | 97.07% | 97.09% | -0.02% | 13,923 |  |
| Others | 96.9% | 96.47% | +0.45% | 3,838 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: CH Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Apple Pay | 80.00% | 100.00% | -20.00% | 10 | 7 | ⚠️ |
| Credit Card | 81.48% | 86.11% | -5.38% | 27 | 36 | ⚠️ |
| Paypal | 88.89% | 83.33% | +6.67% | 18 | 6 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 50 | 43 | 90.91% | 87.76% | +3.15 |
| Blocked, Restricted, Not Permitted | 0 | 1 | 0.00% | 2.04% | -2.04 |
| PayPal Declined, Revoked, Payer Issue | 0 | 1 | 0.00% | 2.04% | -2.04 |
| Expired, Invalid, Closed Card, No Account | 5 | 4 | 9.09% | 8.16% | +0.93 |

**Root Cause:** Apple + Others

---

## L2: LU Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Credit Card | 100.00% | 100.00% | +0.00% | 21 | 15 |  |
| Others | 100.00% | 100.00% | +0.00% | 3 | 3 |  |
| Paypal | 100.00% | 100.00% | +0.00% | 7 | 6 |  |
| Apple Pay | 100.00% | 90.00% | +11.11% | 6 | 10 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 37 | 34 | 100.00% | 100.00% | +0.00 |

**Root Cause:** Apple

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | Medium (>85%) | 14,090 | 16,889 | +19.9% | Stable |
| DE | High (>92%) | 7,103 | 9,803 | +38.0% | Stable |
| FR | Medium (>85%) | 5,644 | 4,681 | -17.1% | Stable |
| AU | Medium (>85%) | 4,223 | 3,990 | -5.5% | Stable |
| NL | High (>92%) | 2,437 | 2,512 | +3.1% | Stable |
| DK | Medium (>85%) | 1,776 | 1,352 | -23.9% | ⚠️ Volume drop |
| SE | Medium (>85%) | 1,769 | 1,520 | -14.1% | Stable |
| BE | High (>92%) | 1,317 | 1,453 | +10.3% | Stable |
| NZ | Low (>85%) | 1,299 | 1,392 | +7.2% | Stable |
| NO | Medium (>85%) | 843 | 916 | +8.7% | Stable |
| IE | Medium (>85%) | 613 | 989 | +61.3% | Stable |
| AT | High (>92%) | 455 | 414 | -9.0% | Stable |
| CH | Medium (>85%) | 49 | 55 | +12.2% | Stable |
| LU | High (>92%) | 34 | 37 | +8.8% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| CH | ↓ -4.69% | Apple Pay -20.0% | → Stable | Others +3.15pp | Apple + Others |
| LU | ↑ +3.03% | Apple Pay +11.1% | → Stable | → Stable | Apple |

---

*Report: 2026-04-22*
