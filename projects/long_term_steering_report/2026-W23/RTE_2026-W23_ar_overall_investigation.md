# AR Overall Investigation: RTE 2026-W23

**Metric:** Pre-Dunning Acceptance Rate (Overall)  
**Period:** 2026-W22 → 2026-W23  
**Observation:** 92.9% → 92.85% (-0.05%)  
**Volume:** 394,464 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Pre-Dunning Acceptance Rate remained essentially stable at 92.85%, declining marginally by -0.05pp from 92.9% in W22, a change that is not statistically significant across 394,464 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (92.0%-92.9%) | -0.05pp | ✅ |
| L1: Country Scan | TK exceeded ±2.5% threshold | -3.69pp | ⚠️ |
| L1: Dimension Scan | All PaymentMethods & Providers within threshold | <0.5pp | ✅ |
| L2: TK Deep-Dive | applepay declined significantly | -5.26pp | ⚠️ |
| L3: Related Metrics | All funnel metrics stable | <0.1pp | ✅ |
| Mix Shift | No material volume shifts impacting overall | Stable | ✅ |

**Key Findings:**
- TK is the only country exceeding the ±2.5% threshold with a -3.69pp decline (89.73% vs 93.17%), though volume is small at 1,976 orders (0.5% of total)
- Root cause in TK identified as **applepay + Insufficient Funds**: applepay dropped -5.26pp and "Insufficient Funds" declines increased by +2.70pp
- FJ dominates volume (354,405 orders, 89.8% of total) and remained stable at 93.81% (+0.02pp)
- All payment methods and providers at the global level showed minimal movement (<0.5pp changes)
- The 8-week trend shows normal fluctuation with rates consistently between 92.0% and 92.9%

**Action:** **Monitor** – The overall metric change is not significant. Continue monitoring TK's applepay performance and Insufficient Funds trend, but no immediate escalation required given the small volume impact (<100 affected orders).

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W23 | 92.85% | 394,464 | -0.05% ← REPORTED CHANGE |
| 2026-W22 | 92.9% | 386,012 | +0.18% |
| 2026-W21 | 92.73% | 401,715 | +0.01% |
| 2026-W20 | 92.72% | 414,834 | +0.78% |
| 2026-W19 | 92.0% | 427,858 | -0.59% |
| 2026-W18 | 92.55% | 430,891 | -0.20% |
| 2026-W17 | 92.74% | 430,965 | +0.11% |
| 2026-W16 | 92.64% | 429,500 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TK | 89.73% | 93.17% | -3.69% | 1,976 | ⚠️ |
| CF | 93.40% | 93.73% | -0.36% | 51,076 |  |
| YE | 90.07% | 90.26% | -0.21% | 41,850 |  |
| FJ | 93.81% | 93.79% | +0.02% | 354,405 |  |
| TZ | 91.90% | 91.04% | +0.94% | 2,974 |  |
| TV | 94.75% | 93.47% | +1.37% | 1,866 |  |

**Countries exceeding ±2.5% threshold:** TK

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 97.73% | 98.06% | -0.33% | 5,783 |  |
| Apple Pay | 90.43% | 90.53% | -0.11% | 49,308 |  |
| Paypal | 96.5% | 96.55% | -0.06% | 50,591 |  |
| Credit Card | 92.53% | 92.57% | -0.04% | 288,782 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 56.52% | 56.76% | -0.41% | 92 |  |
| Adyen | 90.6% | 90.89% | -0.32% | 73,549 |  |
| ProcessOut | 91.66% | 91.76% | -0.11% | 83,969 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 666 |  |
| Braintree | 93.98% | 93.93% | +0.05% | 236,188 |  |

---

## L2: TK Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| applepay | 85.53% | 90.28% | -5.26% | 456 | 432 | ⚠️ |
| credit_card | 90.65% | 93.79% | -3.35% | 1,390 | 1,321 |  |
| paypal | 93.81% | 96.33% | -2.62% | 113 | 109 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 17 | 11 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Braintree | 87.17% | 91.50% | -4.73% | 569 | 541 |  |
| Adyen | 90.65% | 93.79% | -3.35% | 1,390 | 1,321 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 17 | 11 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 1,773 | 1,745 | 89.73% | 93.17% | -3.44 |
| Insufficient Funds | 141 | 83 | 7.14% | 4.43% | +2.70 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 27 | 15 | 1.37% | 0.80% | +0.57 |
| Other reasons | 35 | 30 | 1.77% | 1.60% | +0.17 |

**Root Cause:** applepay + Insufficient

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
| YE | Medium (>85%) | 41,924 | 41,850 | -0.2% | Stable |
| TT | High (>92%) | 4,429 | 4,695 | +6.0% | Stable |
| TO | Medium (>85%) | 2,689 | 2,997 | +11.5% | Stable |
| TZ | Medium (>85%) | 2,489 | 2,974 | +19.5% | Stable |
| TK | High (>92%) | 1,873 | 1,976 | +5.5% | Stable |
| TV | High (>92%) | 1,746 | 1,866 | +6.9% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TK | ↓ -3.69% | applepay -5.3% | → Stable | Insufficient Funds +2.70pp | applepay + Insufficient |

---

*Report: 2026-06-09*
