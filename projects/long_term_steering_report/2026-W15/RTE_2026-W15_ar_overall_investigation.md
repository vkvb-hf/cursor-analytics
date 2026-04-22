# AR Overall Investigation: RTE 2026-W15

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 92.83% → 92.65% (-0.19%)  
**Volume:** 429,385 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate declined marginally by -0.19% (from 92.83% to 92.65%) in 2026-W15, a change that is not statistically significant given the volume of 429,385 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Within normal range (91.33%-93.20%) | -0.19% | ✅ |
| L1: Country Breakdown | 1 country exceeds ±2.5% threshold (TK) | TK: +7.54% | ⚠️ |
| L1: PaymentMethod | All within normal range | -0.41% to +0.47% | ✅ |
| L1: PaymentProvider | Unknown flagged but minimal volume (130) | Unknown: +41.93% | ✅ |
| L2: TK Deep-Dive | Positive movement across all payment methods | +5.41% to +12.10% | ✅ |
| L3: Related Metrics | All metrics stable/improving | +0.03% to +0.48% | ✅ |

**Key Findings:**
- TK showed significant improvement of +7.54% (88.65% → 95.33%), driven by reduced "Insufficient Funds" declines (-5.81pp) across all payment methods
- In TK, Apple Pay improved most dramatically at +12.10%, followed by Credit Card at +6.49% and PayPal at +5.41%
- TV experienced the largest negative movement at -1.37% (93.41% → 92.14%), though volume is low (1,895 orders)
- FJ, representing 90% of total volume (388,956 orders), remained stable with a slight improvement of +0.38%
- Mix shift analysis shows stable composition despite volume declines across most countries (YE -6.8%, TZ -11.7%, TV -8.2%)

**Action:** Monitor - The overall decline is not statistically significant, and the flagged country (TK) is actually showing positive improvement. Continue standard monitoring cadence.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 92.65% | 429,385 | -0.19% |
| 2026-W15 | 92.83% | 421,406 | +0.40% ← REPORTED CHANGE |
| 2026-W14 | 92.46% | 431,856 | -0.34% |
| 2026-W13 | 92.78% | 442,530 | -0.33% |
| 2026-W12 | 93.09% | 443,994 | -0.12% |
| 2026-W11 | 93.2% | 458,408 | +1.80% |
| 2026-W10 | 91.55% | 467,998 | +0.24% |
| 2026-W09 | 91.33% | 466,696 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TV | 92.14% | 93.41% | -1.37% | 1,895 |  |
| YE | 87.77% | 88.14% | -0.42% | 42,126 |  |
| FJ | 93.97% | 93.62% | +0.38% | 388,956 |  |
| CF | 94.14% | 93.47% | +0.72% | 51,881 |  |
| TZ | 91.69% | 90.11% | +1.76% | 2,660 |  |
| TO | 86.67% | 84.89% | +2.11% | 3,204 |  |
| TK | 95.33% | 88.65% | +7.54% | 1,950 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TK

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 97.83% | 98.23% | -0.41% | 5,339 |  |
| Paypal | 96.65% | 96.45% | +0.21% | 53,618 |  |
| Apple Pay | 90.34% | 90.0% | +0.37% | 53,550 |  |
| Credit Card | 92.52% | 92.08% | +0.47% | 308,899 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 510 |  |
| ProcessOut | 91.72% | 91.65% | +0.08% | 64,367 |  |
| Adyen | 89.87% | 89.45% | +0.48% | 74,351 |  |
| Braintree | 93.87% | 93.41% | +0.49% | 282,048 |  |
| Unknown | 68.46% | 48.24% | +41.93% | 130 | ⚠️ |

---

## L2: TK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 1 | 0 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 10 | 7 |  |
| paypal | 97.46% | 92.45% | +5.41% | 118 | 106 | ⚠️ |
| credit_card | 95.81% | 89.97% | +6.49% | 1,359 | 1,256 | ⚠️ |
| applepay | 93.51% | 83.41% | +12.10% | 462 | 410 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 0.00% | +0.00% | 1 | 0 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 10 | 7 |  |
| Adyen | 95.81% | 89.97% | +6.49% | 1,359 | 1,256 | ⚠️ |
| Braintree | 94.31% | 85.27% | +10.60% | 580 | 516 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,859 | 1,577 | 95.33% | 88.65% | +6.69 |
| Insufficient Funds | 49 | 148 | 2.51% | 8.32% | -5.81 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 21 | 32 | 1.08% | 1.80% | -0.72 |
| Other reasons | 20 | 22 | 1.03% | 1.24% | -0.21 |
| Unknown | 1 | 0 | 0.05% | 0.00% | +0.05 |

**Root Cause:** paypal + Adyen + Insufficient

---

## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.25% | 90.82% | +0.48% | 421,406 | 431,856 |  |
| 2_PreDunningAR | 92.83% | 92.46% | +0.41% | 421,406 | 431,856 |  |
| 3_PostDunningAR | 94.33% | 94.3% | +0.03% | 421,406 | 431,856 |  |
| 6_PaymentApprovalRate | 94.87% | 94.75% | +0.12% | 421,406 | 431,856 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 397,332 | 388,956 | -2.1% | Stable |
| CF | High (>92%) | 52,140 | 51,881 | -0.5% | Stable |
| YE | Medium (>85%) | 45,217 | 42,126 | -6.8% | Stable |
| TT | High (>92%) | 4,924 | 4,617 | -6.2% | Stable |
| TO | Low (>85%) | 3,480 | 3,204 | -7.9% | Stable |
| TZ | Medium (>85%) | 3,013 | 2,660 | -11.7% | Stable |
| TV | High (>92%) | 2,065 | 1,895 | -8.2% | Stable |
| TK | Medium (>85%) | 1,779 | 1,950 | +9.6% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TK | ↑ +7.54% | paypal +5.4% | Adyen +6.5% | Insufficient Funds -5.81pp | paypal + Adyen + Insufficient |

---

*Report: 2026-04-22*
