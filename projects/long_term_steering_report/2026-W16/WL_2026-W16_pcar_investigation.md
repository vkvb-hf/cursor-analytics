# PCAR Investigation: WL 2026-W16

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 97.37% → 97.59% (+0.23%)  
**Volume:** 11,024 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate improved from 97.37% to 97.59% (+0.22pp) in W16, a non-significant increase on volume of 11,024 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Stable upward trend | +0.23% | ✅ |
| L1: Country Breakdown | 1 country exceeds ±2.5% threshold | MR +2.78% | ⚠️ |
| L1: Dimension Scan | No payment method exceeds threshold | Max: Apple Pay +0.58% | ✅ |
| L2: MR Deep-Dive | ApplePay + Braintree flagged | +7.14%, +5.88% | ⚠️ |
| Mix Shift | All countries stable | No significant shifts | ✅ |

**Key Findings:**
- MR showed a +2.78pp improvement (95.59% → 98.25%), the only country exceeding the ±2.5% threshold, though on very low volume (57 orders)
- Within MR, ApplePay improved significantly (+7.14pp, from 93.33% to 100.00%) and Braintree improved +5.88pp (94.44% → 100.00%)
- CVV/CVC Mismatch decline reason appeared in MR (1 case, +1.75pp), while Policy/Lifecycle declines decreased (-1.47pp)
- Overall volume declined 6.0% week-over-week (11,721 → 11,024 orders), continuing a downward trend from W10 peak (16,267)
- AO was the only country showing rate decline (-0.62pp), moving from 97.39% to 96.78%

**Action:** Monitor – The overall change is not statistically significant, and the MR improvement is based on very low volume (57 orders). Continue tracking ApplePay/Braintree performance in MR for sustained improvement confirmation.

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
