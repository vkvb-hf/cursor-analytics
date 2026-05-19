# PCAR Investigation: RTE 2026-W20

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W19 → 2026-W20  
**Observation:** 96.66% → 96.49% (-0.18%)  
**Volume:** 38,879 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Payment Checkout Approval Rate declined by -0.18pp (96.66% → 96.49%) in W20, a statistically not significant change on 38,879 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Gradual decline from 97.22% (W15) to 96.49% (W20) | -0.73pp over 5 weeks | ⚠️ |
| L1: Country Breakdown | 1 country (TT) exceeds ±2.5% threshold | TT: +6.37pp | ⚠️ |
| L1: Dimension Scan | Others PaymentMethod flagged | +5.50pp | ⚠️ |
| L2: TT Deep-Dive | Klarna declining, IDeal/Adyen improving | Mixed signals | ⚠️ |
| Mix Shift | TT volume +15.2%, all tiers stable | No material impact | ✅ |

**Key Findings:**
- TT showed the largest country-level movement at +6.37pp (75.49% → 80.30%), driven by IDeal improvement (+8.58pp) and Adyen recovery (+6.85pp)
- Klarna in TT declined significantly (-8.82pp, from 64.71% → 59.00%) but represents low volume (100 orders)
- CF experienced the largest decline at -1.57pp (97.95% → 96.42%) on 5,525 orders, contributing to overall metric degradation
- 8-week trend shows persistent gradual decline of -0.73pp since W15, suggesting underlying systemic pressure
- "Others" PaymentMethod improved +5.50pp but has low volume (1,004 orders)

**Action:** Monitor — The weekly change is not statistically significant and TT improvements offset CF/TO declines. Continue monitoring the gradual downward trend; escalate if W21 continues the decline pattern or CF degradation persists.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W20 | 96.49% | 38,879 | -0.18% ← REPORTED CHANGE |
| 2026-W19 | 96.66% | 38,661 | +0.15% |
| 2026-W18 | 96.52% | 40,203 | -0.55% |
| 2026-W17 | 97.05% | 42,589 | -0.15% |
| 2026-W16 | 97.2% | 44,111 | -0.02% |
| 2026-W15 | 97.22% | 44,168 | +0.33% |
| 2026-W14 | 96.9% | 39,914 | +0.01% |
| 2026-W13 | 96.89% | 42,897 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CF | 96.42% | 97.95% | -1.57% | 5,525 |  |
| TO | 92.80% | 94.20% | -1.48% | 403 |  |
| TK | 98.71% | 99.71% | -1.01% | 309 |  |
| FJ | 97.19% | 97.26% | -0.07% | 27,653 |  |
| YE | 96.80% | 95.90% | +0.94% | 3,220 |  |
| TT | 80.30% | 75.49% | +6.37% | 949 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TT

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Credit Card | 96.8% | 97.09% | -0.31% | 23,998 |  |
| Paypal | 97.84% | 98.09% | -0.25% | 4,580 |  |
| Apple Pay | 97.19% | 97.31% | -0.12% | 9,297 |  |
| Others | 76.59% | 72.6% | +5.50% | 1,004 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: TT Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Klarna | 59.00% | 64.71% | -8.82% | 100 | 102 | ⚠️ |
| Paypal | 93.33% | 100.00% | -6.67% | 15 | 8 | ⚠️ |
| ApplePay | 100.00% | 100.00% | +0.00% | 65 | 52 |  |
| CreditCard | 100.00% | 100.00% | +0.00% | 45 | 32 |  |
| IDeal | 79.97% | 73.65% | +8.58% | 724 | 630 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Braintree | 98.75% | 100.00% | -1.25% | 80 | 60 |  |
| Adyen | 78.60% | 73.56% | +6.85% | 869 | 764 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Fraud, Lost/Stolen Card, Security | 4 | 4 | 0.42% | 0.49% | -0.06 |
| Others | 945 | 820 | 99.58% | 99.51% | +0.06 |

**Root Cause:** Klarna + Adyen

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 27,034 | 27,653 | +2.3% | Stable |
| CF | High (>92%) | 6,009 | 5,525 | -8.1% | Stable |
| YE | High (>92%) | 3,125 | 3,220 | +3.0% | Stable |
| TT | Low (>85%) | 824 | 949 | +15.2% | Stable |
| TZ | High (>92%) | 496 | 491 | -1.0% | Stable |
| TO | High (>92%) | 448 | 403 | -10.0% | Stable |
| TV | Medium (>85%) | 377 | 329 | -12.7% | Stable |
| TK | High (>92%) | 348 | 309 | -11.2% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TT | ↑ +6.37% | Klarna -8.8% | Adyen +6.8% | → Stable | Klarna + Adyen |

---

*Report: 2026-05-19*
