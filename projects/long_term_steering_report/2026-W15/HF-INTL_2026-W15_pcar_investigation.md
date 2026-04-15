# PCAR Investigation: HF-INTL 2026-W15

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 96.0% → 96.12% (+0.13%)  
**Volume:** 36,514 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate for HF-INTL improved slightly from 96.0% to 96.12% (+0.13pp) in W15, a statistically non-significant change within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (95.21%-97.31%) | +0.13pp | ✅ |
| L1: Country Scan | 2 countries exceed ±2.5% threshold (AT, DK) | AT +2.95%, DK +3.94% | ⚠️ |
| L1: Dimension Scan | No payment methods exceed threshold | Max +1.83% (Others) | ✅ |
| L2: AT Deep-Dive | Apple Pay driving improvement | +5.78% | ⚠️ |
| L2: DK Deep-Dive | Apple Pay + Braintree improving | +6.47%, +5.84% | ⚠️ |
| Mix Shift | Volume shifts stable across tiers | DK +25.6%, NO +39.2% | ✅ |

**Key Findings:**
- AT and DK both showed significant approval rate improvements (+2.95pp and +3.94pp respectively), driven primarily by reduced "Insufficient Funds" declines (-2.05pp in AT, -3.13pp in DK)
- Apple Pay performance improved substantially in both flagged countries: +5.78% in AT and +6.47% in DK
- DK volume increased +25.6% (30,036 → 37,713 orders) while maintaining improved approval rates, indicating healthy growth
- Braintree provider in DK showed +5.84% improvement, contributing to overall DK gains
- Overall HF-INTL volume decreased from prior weeks (36,514 vs 8-week high of 49,249 in W08)

**Action:** Monitor - The +0.13pp change is not statistically significant and represents positive movement. Continue tracking AT and DK improvements to confirm sustained performance gains in Apple Pay and Braintree channels.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 96.12% | 36,514 | +0.13% ← REPORTED CHANGE |
| 2026-W14 | 96.0% | 31,465 | +0.83% |
| 2026-W13 | 95.21% | 39,598 | -1.52% |
| 2026-W12 | 96.68% | 38,136 | -0.53% |
| 2026-W11 | 97.2% | 42,932 | -0.11% |
| 2026-W10 | 97.31% | 44,946 | +0.80% |
| 2026-W09 | 96.54% | 48,662 | +0.04% |
| 2026-W08 | 96.5% | 49,249 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| DE | 97.33% | 96.44% | +0.93% | 201,519 |  |
| GB | 94.14% | 93.07% | +1.15% | 185,598 |  |
| FR | 94.49% | 92.95% | +1.66% | 147,984 |  |
| IE | 91.92% | 90.41% | +1.67% | 17,513 |  |
| AT | 95.52% | 92.78% | +2.95% | 13,962 | ⚠️ |
| DK | 97.74% | 94.03% | +3.94% | 37,713 | ⚠️ |

**Countries exceeding ±2.5% threshold:** AT, DK

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Apple Pay | 98.03% | 98.16% | -0.13% | 12,006 |  |
| Credit Card | 98.22% | 98.2% | +0.03% | 13,439 |  |
| Paypal | 97.96% | 97.76% | +0.20% | 7,741 |  |
| Others | 76.47% | 75.1% | +1.83% | 3,328 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: AT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| cashcredit | 100.0% | 100.0% | +0.00% | 90 | 65 |  |
| klarna | 100.0% | 100.0% | +0.00% | 2 | 2 |  |
| sepadirectdebit | 99.32% | 98.84% | +0.49% | 884 | 775 |  |
| paypal | 97.96% | 96.99% | +0.99% | 4,941 | 4,354 |  |
| credit_card | 93.54% | 89.87% | +4.08% | 6,071 | 5,530 |  |
| applepay | 93.57% | 88.45% | +5.78% | 1,974 | 1,732 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 90 | 65 |  |
| Adyen | 95.22% | 93.61% | +1.72% | 2,470 | 2,191 |  |
| Braintree | 96.7% | 94.56% | +2.26% | 6,915 | 6,086 |  |
| ProcessOut | 93.76% | 89.58% | +4.67% | 4,487 | 4,116 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 13,336 | 11,558 | 95.52% | 92.78% | +2.74 |
| Insufficient Funds | 360 | 577 | 2.58% | 4.63% | -2.05 |
| Other reasons | 114 | 149 | 0.82% | 1.20% | -0.38 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 152 | 174 | 1.09% | 1.40% | -0.31 |

**Root Cause:** applepay + Insufficient

---

## L2: DK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 65.79% | 0.0% | +0.00% | 38 | 0 |  |
| None | 0.0% | 70.59% | -100.00% | 0 | 34 | ⚠️ |
| cashcredit | 100.0% | 100.0% | +0.00% | 238 | 173 |  |
| paypal | 96.47% | 94.78% | +1.78% | 1,104 | 901 |  |
| credit_card | 98.17% | 94.92% | +3.42% | 28,919 | 22,890 |  |
| applepay | 96.33% | 90.48% | +6.47% | 7,414 | 6,038 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| No Payment | 100.0% | 100.0% | +0.00% | 238 | 173 |  |
| Unknown | 62.5% | 62.5% | +0.00% | 32 | 24 |  |
| ProcessOut | 98.17% | 95.19% | +3.13% | 21,035 | 16,787 |  |
| Adyen | 98.15% | 94.18% | +4.22% | 7,890 | 6,113 |  |
| Braintree | 96.35% | 91.04% | +5.84% | 8,518 | 6,939 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 36,859 | 28,242 | 97.74% | 94.03% | +3.71 |
| Insufficient Funds | 436 | 1,286 | 1.16% | 4.28% | -3.13 |
| Other reasons | 230 | 309 | 0.61% | 1.03% | -0.42 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 176 | 189 | 0.47% | 0.63% | -0.16 |
| Unknown | 12 | 10 | 0.03% | 0.03% | +0.00 |

**Root Cause:** None + Braintree + Insufficient

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| GB | High (>92%) | 205,600 | 185,598 | -9.7% | Stable |
| DE | High (>92%) | 205,169 | 201,519 | -1.8% | Stable |
| FR | High (>92%) | 158,173 | 147,984 | -6.4% | Stable |
| NL | High (>92%) | 118,190 | 110,805 | -6.2% | Stable |
| AU | Medium (>85%) | 96,471 | 85,229 | -11.7% | Stable |
| BE | High (>92%) | 74,093 | 64,439 | -13.0% | Stable |
| SE | High (>92%) | 35,624 | 31,821 | -10.7% | Stable |
| DK | High (>92%) | 30,036 | 37,713 | +25.6% | Stable |
| NZ | Medium (>85%) | 19,364 | 16,941 | -12.5% | Stable |
| IE | Medium (>85%) | 18,775 | 17,513 | -6.7% | Stable |
| NO | Medium (>85%) | 13,551 | 18,868 | +39.2% | Stable |
| AT | High (>92%) | 12,458 | 13,962 | +12.1% | Stable |
| LU | High (>92%) | 2,765 | 2,731 | -1.2% | Stable |
| CH | High (>92%) | 2,174 | 2,101 | -3.4% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| AT | ↑ +2.95% | applepay +5.8% | → Stable | Insufficient Funds -2.05pp | applepay + Insufficient |
| DK | ↑ +3.94% | None -100.0% | Braintree +5.8% | Insufficient Funds -3.13pp | None + Braintree + Insufficient |

---

*Report: 2026-04-15*
