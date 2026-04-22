# PCAR Investigation: RTE 2026-W16

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 97.22% → 97.2% (-0.02%)  
**Volume:** 44,111 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate remained essentially stable, declining marginally from 97.22% to 97.2% (-0.02 pp) week-over-week, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | Within normal 8-week range (96.88%-97.3%) | -0.02 pp | ✅ |
| L1: Country Scan | 1 country exceeds ±2.5% threshold (TT) | TT: +7.93 pp | ⚠️ |
| L1: Dimension Scan | Others PaymentMethod flagged | +8.69 pp | ⚠️ |
| L2: TT Deep-Dive | Klarna/Adyen volatility identified | Mixed | ⚠️ |
| Mix Shift | TT volume +55.2% but low-tier, minimal impact | Stable | ✅ |

**Key Findings:**
- TT showed significant improvement (+7.93 pp), driven primarily by IDeal via Adyen improving from 73.41% to 81.67% (+11.24 pp) on substantially higher volume (583 → 1,009 orders)
- Klarna in TT declined from 54.17% to 49.50% (-8.61 pp), but this was offset by improvements in other payment methods
- TT volume increased significantly (+55.2%, from 788 to 1,223 orders), but as a low-tier market it has minimal impact on overall RTE metrics
- Major markets FJ (30,779 orders) and CF (6,546 orders) remained stable with rates of 97.69% and 98.61% respectively
- 8-week trend shows metric is stable within a narrow band of 96.88%-97.3%

**Action:** Monitor – No immediate action required. The -0.02 pp overall change is not significant, and the TT fluctuations are improvements in a low-volume market. Continue monitoring Klarna performance in TT and Adyen processing rates.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 97.2% | 44,111 | -0.02% ← REPORTED CHANGE |
| 2026-W15 | 97.22% | 44,168 | +0.33% |
| 2026-W14 | 96.9% | 39,914 | +0.01% |
| 2026-W13 | 96.89% | 42,897 | +0.01% |
| 2026-W12 | 96.88% | 44,209 | -0.11% |
| 2026-W11 | 96.99% | 47,403 | +0.10% |
| 2026-W10 | 96.89% | 48,399 | -0.42% |
| 2026-W09 | 97.3% | 50,858 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| YE | 97.20% | 97.37% | -0.18% | 3,713 |  |
| FJ | 97.69% | 97.73% | -0.04% | 30,779 |  |
| CF | 98.61% | 98.21% | +0.40% | 6,546 |  |
| TZ | 98.12% | 97.10% | +1.05% | 585 |  |
| TV | 85.21% | 84.03% | +1.40% | 426 |  |
| TK | 100.00% | 98.58% | +1.44% | 340 |  |
| TT | 80.54% | 74.62% | +7.93% | 1,223 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TT

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Paypal | 98.31% | 98.58% | -0.28% | 5,148 |  |
| Credit Card | 97.87% | 97.86% | +0.01% | 27,332 |  |
| Apple Pay | 97.42% | 97.21% | +0.21% | 10,293 |  |
| Others | 77.8% | 71.58% | +8.69% | 1,338 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: TT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Klarna | 49.50% | 54.17% | -8.61% | 101 | 96 | ⚠️ |
| Paypal | 92.86% | 100.00% | -7.14% | 14 | 13 | ⚠️ |
| ApplePay | 98.28% | 100.00% | -1.72% | 58 | 37 |  |
| CreditCard | 100.00% | 98.31% | +1.72% | 41 | 59 |  |
| IDeal | 81.67% | 73.41% | +11.24% | 1,009 | 583 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Braintree | 97.22% | 100.00% | -2.78% | 72 | 50 |  |
| Adyen | 79.50% | 72.90% | +9.05% | 1,151 | 738 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Fraud, Lost/Stolen Card, Security | 0 | 3 | 0.00% | 0.38% | -0.38 |
| Others | 1,222 | 785 | 99.92% | 99.62% | +0.30 |
| PayPal Declined, Revoked, Payer Issue | 1 | 0 | 0.08% | 0.00% | +0.08 |

**Root Cause:** Klarna + Adyen

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 30,930 | 30,779 | -0.5% | Stable |
| CF | High (>92%) | 6,939 | 6,546 | -5.7% | Stable |
| YE | High (>92%) | 3,655 | 3,713 | +1.6% | Stable |
| TT | Low (>85%) | 788 | 1,223 | +55.2% | Stable |
| TZ | High (>92%) | 551 | 585 | +6.2% | Stable |
| TV | Low (>85%) | 476 | 426 | -10.5% | Stable |
| TK | High (>92%) | 423 | 340 | -19.6% | Stable |
| TO | High (>92%) | 406 | 499 | +22.9% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TT | ↑ +7.93% | Klarna -8.6% | Adyen +9.0% | → Stable | Klarna + Adyen |

---

*Report: 2026-04-22*
