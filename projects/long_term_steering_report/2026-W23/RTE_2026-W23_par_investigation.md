# PAR Investigation: RTE 2026-W23

**Metric:** Payment Approval Rate  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 94.94% → 94.97% (+0.03%)  
**Volume:** 394,464 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Approval Rate remained essentially stable at 94.97%, increasing by +0.03pp from the prior week—a statistically insignificant change within normal operating variance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (94.15%-94.97%) | +0.03pp | ✅ |
| L1: Country Breakdown | 1 country exceeds ±2.5% threshold | TK -3.24pp | ⚠️ |
| L1: Dimension Scan | All payment methods/providers stable | <±0.5pp | ✅ |
| L2: TK Deep-Dive | Root cause identified | applepay -5.97pp, Braintree -5.30pp | ⚠️ |
| L3: Related Metrics | Funnel metrics stable | ≤±0.06pp | ✅ |
| Mix Shift | No significant volume shifts | All stable | ✅ |

**Key Findings:**
- TK experienced a significant decline of -3.24pp (94.87% → 91.80%), but represents only 0.5% of total volume (1,976 orders)
- Root cause in TK isolated to Apple Pay via Braintree: Apple Pay declined -5.97pp and Braintree declined -5.30pp
- "Insufficient Funds" decline reason in TK increased by +2.46pp (3.36% → 5.82%), accounting for the majority of the degradation
- Global payment methods and providers remained stable with all changes under ±0.3pp
- 8-week trend shows consistent improvement from W19 low of 94.15% to current 94.97%

**Action:** Monitor — The overall metric is stable and statistically insignificant. Continue monitoring TK's Apple Pay + Braintree performance for potential recurring patterns; no immediate escalation required given low volume impact.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W23 | 94.97% | 394,464 | +0.03% ← REPORTED CHANGE |
| 2026-W22 | 94.94% | 386,012 | +0.11% |
| 2026-W21 | 94.84% | 401,715 | +0.06% |
| 2026-W20 | 94.78% | 414,834 | +0.67% |
| 2026-W19 | 94.15% | 427,858 | -0.52% |
| 2026-W18 | 94.64% | 430,891 | -0.20% |
| 2026-W17 | 94.83% | 430,965 | +0.02% |
| 2026-W16 | 94.81% | 429,500 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TK | 91.80% | 94.87% | -3.24% | 1,976 | ⚠️ |
| TT | 98.04% | 98.26% | -0.22% | 4,695 |  |
| CF | 94.77% | 94.97% | -0.21% | 51,076 |  |
| FJ | 95.62% | 95.55% | +0.07% | 354,405 |  |
| TO | 93.09% | 92.82% | +0.29% | 2,997 |  |
| TV | 95.71% | 94.56% | +1.22% | 1,866 |  |

**Countries exceeding ±2.5% threshold:** TK

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 98.2% | 98.48% | -0.28% | 5,783 |  |
| Paypal | 97.56% | 97.62% | -0.06% | 50,591 |  |
| Apple Pay | 92.72% | 92.75% | -0.03% | 49,308 |  |
| Credit Card | 94.83% | 94.77% | +0.07% | 288,782 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 56.52% | 56.76% | -0.41% | 92 |  |
| Adyen | 93.71% | 93.81% | -0.11% | 73,549 |  |
| ProcessOut | 93.48% | 93.5% | -0.02% | 83,969 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 666 |  |
| Braintree | 95.89% | 95.79% | +0.11% | 236,188 |  |

---

## L2: TK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| applepay | 87.06% | 92.59% | -5.97% | 456 | 432 | ⚠️ |
| paypal | 95.58% | 98.17% | -2.64% | 113 | 109 |  |
| credit_card | 92.95% | 95.31% | -2.47% | 1,390 | 1,321 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 17 | 11 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Braintree | 88.75% | 93.72% | -5.30% | 569 | 541 | ⚠️ |
| Adyen | 92.95% | 95.31% | -2.47% | 1,390 | 1,321 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 17 | 11 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,814 | 1,777 | 91.80% | 94.87% | -3.07 |
| Insufficient Funds | 115 | 63 | 5.82% | 3.36% | +2.46 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 21 | 11 | 1.06% | 0.59% | +0.48 |
| Other reasons | 26 | 22 | 1.32% | 1.17% | +0.14 |

**Root Cause:** applepay + Braintree + Insufficient

---

## L3: Related Metrics (Overall Total Box Candidates)

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 91.21% | 91.21% | +0.00% | 394,464 | 386,012 |  |
| 2_PreDunningAR | 92.85% | 92.9% | -0.05% | 394,464 | 386,012 |  |
| 3_PostDunningAR | 94.38% | 94.44% | -0.06% | 394,464 | 386,012 |  |
| 6_PaymentApprovalRate | 94.97% | 94.94% | +0.03% | 394,464 | 386,012 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 345,821 | 354,405 | +2.5% | Stable |
| CF | High (>92%) | 50,438 | 51,076 | +1.3% | Stable |
| YE | High (>92%) | 41,924 | 41,850 | -0.2% | Stable |
| TT | High (>92%) | 4,429 | 4,695 | +6.0% | Stable |
| TO | High (>92%) | 2,689 | 2,997 | +11.5% | Stable |
| TZ | High (>92%) | 2,489 | 2,974 | +19.5% | Stable |
| TK | High (>92%) | 1,873 | 1,976 | +5.5% | Stable |
| TV | High (>92%) | 1,746 | 1,866 | +6.9% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TK | ↓ -3.24% | applepay -6.0% | Braintree -5.3% | Insufficient Funds +2.46pp | applepay + Braintree + Insufficient |

---

*Report: 2026-06-09*
