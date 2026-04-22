# PCAR Investigation: WL 2026-W16

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 97.37% → 97.59% (+0.23%)  
**Volume:** 11,024 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate improved slightly from 97.37% to 97.59% (+0.22pp) in W16, a statistically non-significant change with 11,024 orders processed.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Stable upward trend | +0.23% | ✅ |
| L1: Country Scan | 1 country flagged (MR) | +2.78% | ⚠️ |
| L1: Dimension Scan | No payment methods flagged | <±2.5% | ✅ |
| L2: MR Deep-Dive | ApplePay + Braintree improvement | +7.14% / +5.88% | ⚠️ |
| Mix Shift | All countries stable | No significant shifts | ✅ |

**Key Findings:**
- MR showed a +2.78pp improvement (95.59% → 98.25%), but with very low volume (57 orders), making this statistically unreliable
- In MR, ApplePay approval rate improved significantly (+7.14pp) alongside Braintree provider (+5.88pp), though based on only 18 and 26 transactions respectively
- CVV/CVC Mismatch appeared as a new decline reason in MR (1 case, +1.75pp), but absolute numbers are minimal
- Overall volume declined 6% week-over-week (11,721 → 11,024), continuing a downward trend from W10 (16,267)
- All major countries (KN, CK, ER, CG, GN, AO) remained stable with rates above 96%

**Action:** Monitor — The overall metric shows slight improvement within normal fluctuation. The MR flag is driven by extremely low volume (57 orders) and does not warrant investigation. Continue standard monitoring.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W16 | 97.59% | 11,024 | +0.23% ← REPORTED CHANGE |
| 2026-W15 | 97.37% | 11,721 | +0.35% |
| 2026-W14 | 97.03% | 11,373 | -0.04% |
| 2026-W13 | 97.07% | 13,604 | +0.20% |
| 2026-W12 | 96.88% | 14,412 | -0.07% |
| 2026-W11 | 96.95% | 15,835 | -0.43% |
| 2026-W10 | 97.37% | 16,267 | +0.03% |
| 2026-W09 | 97.34% | 15,555 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| AO | 96.78% | 97.39% | -0.62% | 901 |  |
| ER | 96.49% | 96.18% | +0.32% | 2,278 |  |
| GN | 97.82% | 97.38% | +0.45% | 1,329 |  |
| CK | 97.59% | 96.99% | +0.62% | 2,240 |  |
| MR | 98.25% | 95.59% | +2.78% | 57 | ⚠️ |

**Countries exceeding ±2.5% threshold:** MR

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Paypal | 97.91% | 98.12% | -0.21% | 1,291 |  |
| Others | 100.0% | 100.0% | +0.00% | 1 |  |
| Credit Card | 97.32% | 97.24% | +0.08% | 5,966 |  |
| Apple Pay | 97.9% | 97.34% | +0.58% | 3,766 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: MR Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
|  | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| CreditCard | 96.77% | 96.88% | -0.10% | 31 | 32 |  |
| Paypal | 100.00% | 100.00% | +0.00% | 8 | 6 |  |
| ApplePay | 100.00% | 93.33% | +7.14% | 18 | 30 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| CreditCard | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| ProcessOut | 96.77% | 96.88% | -0.10% | 31 | 32 |  |
| Braintree | 100.00% | 94.44% | +5.88% | 26 | 36 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| CVV/CVC Mismatch | 1 | 0 | 1.75% | 0.00% | +1.75 |
| Policy, Lifecycle, Revocation, Limit Exceeded | 0 | 1 | 0.00% | 1.47% | -1.47 |
| Others | 56 | 67 | 98.25% | 98.53% | -0.28 |

**Root Cause:** ApplePay + Braintree + CVV/CVC

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| KN | High (>92%) | 2,562 | 2,145 | -16.3% | Stable |
| CK | High (>92%) | 2,491 | 2,240 | -10.1% | Stable |
| ER | High (>92%) | 2,433 | 2,278 | -6.4% | Stable |
| CG | High (>92%) | 2,029 | 2,074 | +2.2% | Stable |
| GN | High (>92%) | 1,334 | 1,329 | -0.4% | Stable |
| AO | High (>92%) | 804 | 901 | +12.1% | Stable |
| MR | High (>92%) | 68 | 57 | -16.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| MR | ↑ +2.78% | ApplePay +7.1% | Braintree +5.9% | CVV/CVC Mismatch +1.75pp | ApplePay + Braintree + CVV/CVC |

---

*Report: 2026-04-22*
