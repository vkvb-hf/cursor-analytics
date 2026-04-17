# Reactivation Investigation: RTE 2026-W15

**Metric:** Reactivation Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 89.2% → 90.41% (+1.36%)  
**Volume:** 19,757 orders  
**Significance:** Significant

## Executive Summary

**Overall:** Reactivation Rate improved significantly from 89.2% to 90.41% (+1.36%) in W15, continuing a positive 8-week upward trend from 84.71% in W08.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Consistent upward trend | +5.70pp since W08 | ✅ |
| L1: Country Scan | 1 country exceeds ±2.5% threshold | TK +7.54% | ⚠️ |
| L1: Dimension Scan | 1 payment method exceeds threshold | Others +2.78% | ⚠️ |
| L2: TK Deep-Dive | Multiple payment improvements | applepay +12.10%, credit_card +6.49% | ✅ |
| L2: Decline Analysis | Insufficient Funds significantly reduced | -5.81pp | ✅ |

**Key Findings:**
- TK drove the largest country-level improvement at +7.54%, with applepay showing the strongest gain (+12.10%) followed by credit_card (+6.49%) and paypal (+5.41%)
- Insufficient Funds declines in TK dropped substantially from 8.32% to 2.51% (-5.81pp), indicating improved payment processing or customer payment capability
- Both Braintree (+10.60%) and Adyen (+6.49%) providers in TK showed significant rate improvements
- Mix shift analysis shows stable volume distribution across AR tiers with TK volume increasing +9.6% while maintaining improvement
- Minor declines in TV (-1.37%) and YE (-0.43%) were offset by broad-based improvements across other markets

**Action:** Monitor - The improvement is driven by positive operational changes (reduced Insufficient Funds declines) rather than anomalies. Continue tracking TK performance to confirm sustainability of gains.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 90.41% | 19,757 | +1.36% ← REPORTED CHANGE |
| 2026-W14 | 89.2% | 17,264 | +0.68% |
| 2026-W13 | 88.6% | 19,685 | - |
| 2026-W12 | 88.6% | 20,873 | +1.87% |
| 2026-W11 | 86.97% | 23,790 | +2.19% |
| 2026-W10 | 85.11% | 26,102 | +0.75% |
| 2026-W09 | 84.48% | 24,364 | -0.27% |
| 2026-W08 | 84.71% | 24,536 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TV | 92.14% | 93.41% | -1.37% | 1,895 |  |
| YE | 87.77% | 88.15% | -0.43% | 42,126 |  |
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
| Apple Pay | 68.62% | 69.66% | -1.50% | 1,893 |  |
| Paypal | 93.4% | 92.54% | +0.92% | 3,241 |  |
| Credit Card | 92.71% | 91.26% | +1.59% | 14,461 |  |
| Others | 80.25% | 78.08% | +2.78% | 162 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: TK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.0% | 0.0% | +0.00% | 1 | 0 |  |
| cashcredit | 100.0% | 100.0% | +0.00% | 10 | 7 |  |
| paypal | 97.46% | 92.45% | +5.41% | 118 | 106 | ⚠️ |
| credit_card | 95.81% | 89.97% | +6.49% | 1,359 | 1,256 | ⚠️ |
| applepay | 93.51% | 83.41% | +12.10% | 462 | 410 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.0% | 0.0% | +0.00% | 1 | 0 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 10 | 7 |  |
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


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 397,332 | 388,956 | -2.1% | Stable |
| CF | High (>92%) | 52,140 | 51,881 | -0.5% | Stable |
| YE | Medium (>85%) | 45,214 | 42,126 | -6.8% | Stable |
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

*Report: 2026-04-17*
