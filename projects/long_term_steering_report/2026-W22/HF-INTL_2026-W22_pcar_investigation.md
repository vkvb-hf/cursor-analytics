# PCAR Investigation: HF-INTL 2026-W22

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 93.72% → 94.5% (+0.83%)  
**Volume:** 25,404 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate improved from 93.72% to 94.5% (+0.83pp) in W22, though the change is not statistically significant and volume declined by 9.9% (28,206 → 25,404 orders).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Downward trend from W16 peak (97.13%) | +0.83pp WoW | ⚠️ Recovery from W19 dip but below W15-W17 levels |
| L1: Country Variance | 2 countries exceed ±2.5% threshold | SE +3.18%, DK +6.33% | ⚠️ Flagged |
| L1: Dimension Scan | Payment methods stable | No flags | ✅ |
| L2: SE Deep-Dive | Klarna at 82.31% via Adyen | +4.61pp improvement | ⚠️ Root cause unclear |
| L2: DK Deep-Dive | Mobilepay +5.41%, ProcessOut +9.52% | Significant improvement | ⚠️ Root cause identified |
| Mix Shift | DE -20.5%, IE -23.9% volume drops | High-AR countries declining | ⚠️ Volume concentration shift |

**Key Findings:**
- DK showed the largest improvement (+6.33pp), driven by ProcessOut provider recovering from 88.82% to 97.28% (+9.52pp) and Mobilepay improving from 75.24% to 79.31% (+5.41pp)
- SE improved +3.18pp with Klarna/Adyen gaining +4.61pp (78.68% → 82.31%), though root cause remains unidentified
- "Others" payment method continues to underperform at 72.43% approval rate across 3,311 orders
- Volume declined significantly in DE (-20.5%) and IE (-23.9%), which may artificially inflate overall AR as mix shifts toward higher-performing markets
- 8-week trend shows recovery from W19 trough (92.95%) but rate remains ~2.6pp below W16 peak (97.13%)

**Action:** Monitor — The improvement is positive but not statistically significant. Continue tracking DK/ProcessOut stability and investigate the persistent "Others" payment method underperformance and SE root cause.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W22 | 94.5% | 25,404 | +0.83% ← REPORTED CHANGE |
| 2026-W21 | 93.72% | 28,206 | +0.24% |
| 2026-W20 | 93.5% | 31,674 | +0.59% |
| 2026-W19 | 92.95% | 33,686 | -1.31% |
| 2026-W18 | 94.18% | 34,181 | -2.58% |
| 2026-W17 | 96.67% | 34,080 | -0.47% |
| 2026-W16 | 97.13% | 37,314 | +1.05% |
| 2026-W15 | 96.12% | 36,514 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| GB | 98.19% | 97.72% | +0.48% | 5,907 |  |
| FR | 97.65% | 96.77% | +0.91% | 5,143 |  |
| LU | 97.33% | 95.24% | +2.20% | 75 |  |
| NO | 97.01% | 94.70% | +2.45% | 536 |  |
| SE | 90.47% | 87.68% | +3.18% | 787 | ⚠️ |
| DK | 97.97% | 92.14% | +6.33% | 888 | ⚠️ |

**Countries exceeding ±2.5% threshold:** SE, DK

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Paypal | 97.45% | 98.05% | -0.61% | 4,359 |  |
| Apple Pay | 97.61% | 97.14% | +0.49% | 8,550 |  |
| Credit Card | 98.15% | 97.25% | +0.93% | 9,184 |  |
| Others | 72.43% | 71.24% | +1.67% | 3,311 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: SE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| ApplePay | 98.82% | 100.00% | -1.18% | 170 | 170 |  |
| Paypal | 100.00% | 100.00% | +0.00% | 10 | 14 |  |
| CreditCard | 99.50% | 96.41% | +3.20% | 200 | 195 |  |
| Klarna | 82.31% | 78.68% | +4.61% | 407 | 441 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Braintree | 98.89% | 100.00% | -1.11% | 180 | 184 |  |
| ProcessOut | 99.50% | 96.41% | +3.20% | 200 | 195 |  |
| Adyen | 82.31% | 78.68% | +4.61% | 407 | 441 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Fraud, Lost/Stolen Card, Security | 1 | 1 | 0.13% | 0.12% | +0.01 |
| Others | 786 | 819 | 99.87% | 99.88% | -0.01 |

**Root Cause:** Requires investigation

---

## L2: DK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| ApplePay | 98.87% | 99.15% | -0.27% | 355 | 234 |  |
| CreditCard | 99.56% | 98.63% | +0.95% | 458 | 291 |  |
| Mobilepay | 79.31% | 75.24% | +5.41% | 58 | 210 | ⚠️ |
| Paypal | 100.00% | 93.75% | +6.67% | 17 | 16 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Adyen | 100.00% | 0.00% | +0.00% | 1 | 0 |  |
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Braintree | 98.92% | 98.80% | +0.13% | 372 | 250 |  |
| ProcessOut | 97.28% | 88.82% | +9.52% | 515 | 501 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 887 | 749 | 99.89% | 99.73% | +0.15 |
| Expired, Invalid, Closed Card, No Account | 0 | 1 | 0.00% | 0.13% | -0.13 |
| PayPal Declined, Revoked, Payer Issue | 0 | 1 | 0.00% | 0.13% | -0.13 |
| Fraud, Lost/Stolen Card, Security | 1 | 0 | 0.11% | 0.00% | +0.11 |

**Root Cause:** Mobilepay + ProcessOut

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| DE | Medium (>85%) | 6,480 | 5,152 | -20.5% | ⚠️ Volume drop |
| GB | High (>92%) | 6,052 | 5,907 | -2.4% | Stable |
| FR | High (>92%) | 5,750 | 5,143 | -10.6% | Stable |
| AU | High (>92%) | 2,907 | 2,546 | -12.4% | Stable |
| NL | Medium (>85%) | 1,250 | 1,227 | -1.8% | Stable |
| IE | High (>92%) | 1,217 | 926 | -23.9% | ⚠️ Volume drop |
| BE | Low (>85%) | 1,074 | 1,088 | +1.3% | Stable |
| SE | Medium (>85%) | 820 | 787 | -4.0% | Stable |
| NZ | High (>92%) | 820 | 683 | -16.7% | Stable |
| DK | High (>92%) | 751 | 888 | +18.2% | Stable |
| NO | High (>92%) | 509 | 536 | +5.3% | Stable |
| AT | High (>92%) | 386 | 333 | -13.7% | Stable |
| CH | Medium (>85%) | 106 | 113 | +6.6% | Stable |
| LU | High (>92%) | 84 | 75 | -10.7% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| SE | ↑ +3.18% | → Stable | → Stable | → Stable | Requires investigation |
| DK | ↑ +6.33% | Mobilepay +5.4% | ProcessOut +9.5% | → Stable | Mobilepay + ProcessOut |

---

*Report: 2026-06-02*
