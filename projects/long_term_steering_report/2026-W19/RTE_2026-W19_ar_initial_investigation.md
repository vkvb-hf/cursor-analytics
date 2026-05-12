# AR Initial (LL0) Investigation: RTE 2026-W19

**Metric:** Pre-Dunning Acceptance Rate (Initial Charges)  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 92.36% → 92.07% (-0.31%)  
**Volume:** 29,747 orders  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Pre-Dunning Acceptance Rate (Initial Charges) declined slightly from 92.36% to 92.07% (-0.29pp) in W19, a change that is **not statistically significant** with volume at 29,747 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | Within normal range (91-93% over 8 weeks) | -0.31% | ✅ |
| L1: Country Breakdown | 3 countries exceed ±2.5% threshold | YE -3.96%, TV +5.47%, TO +9.76% | ⚠️ |
| L1: Dimension Scan | PaymentProvider "Unknown" flagged | -12.28% | ⚠️ |
| L2: YE Deep-Dive | Insufficient Funds +3.54pp | Credit card -4.73%, Adyen -4.70% | ⚠️ |
| L2: TV Deep-Dive | Improvement driven by lower Insufficient Funds | -6.23pp decline reason improvement | ✅ |
| L2: TO Deep-Dive | Strong improvement across all methods | Insufficient Funds -5.77pp | ✅ |
| L3: Related Metrics | All funnel metrics declined proportionally | -0.28% to -0.32% | ✅ |
| Mix Shift | No significant volume shifts between AR tiers | All countries stable | ✅ |

**Key Findings:**
- **YE is the primary concern:** Declined -3.96pp driven by a +3.54pp increase in "Insufficient Funds" declines, particularly affecting credit card transactions via Adyen (-4.70%)
- **TV and TO showed strong improvements:** +5.47pp and +9.76pp respectively, both driven by significant reductions in "Insufficient Funds" declines
- **PaymentProvider "Unknown" dropped -12.28%** but represents minimal volume (80 orders), limiting overall impact
- **All related funnel metrics declined uniformly** (-0.28% to -0.32%), indicating no isolated funnel stage issue
- **Volume decreased -7.7%** (32,243 → 29,747) week-over-week, consistent with normal fluctuation

**Action:** **Monitor** – The overall decline is not statistically significant and falls within normal operating range. YE warrants observation for continued "Insufficient Funds" trends in the next 1-2 weeks. No immediate escalation required.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W19 | 92.07% | 29,747 | -0.31% ← REPORTED CHANGE |
| 2026-W18 | 92.36% | 32,243 | -0.68% |
| 2026-W17 | 92.99% | 30,395 | +0.64% |
| 2026-W16 | 92.4% | 31,056 | +0.96% |
| 2026-W15 | 91.52% | 29,063 | +0.75% |
| 2026-W14 | 90.84% | 31,837 | -0.60% |
| 2026-W13 | 91.39% | 36,500 | -1.26% |
| 2026-W12 | 92.56% | 42,779 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| YE | 86.20% | 89.76% | -3.96% | 3,305 | ⚠️ |
| FJ | 92.16% | 92.61% | -0.49% | 18,445 |  |
| CF | 94.22% | 93.00% | +1.31% | 5,956 |  |
| TV | 96.59% | 91.59% | +5.47% | 323 | ⚠️ |
| TO | 93.62% | 85.30% | +9.76% | 345 | ⚠️ |

**Countries exceeding ±2.5% threshold:** YE, TV, TO

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Others | 96.2% | 97.22% | -1.04% | 1,159 |  |
| Apple Pay | 90.93% | 91.56% | -0.70% | 6,105 |  |
| Credit Card | 91.38% | 91.61% | -0.25% | 18,859 |  |
| Paypal | 96.25% | 95.99% | +0.26% | 3,624 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | 68.75% | 78.38% | -12.28% | 80 | ⚠️ |
| Braintree | 92.77% | 93.12% | -0.37% | 9,840 |  |
| ProcessOut | 92.19% | 92.44% | -0.27% | 10,783 |  |
| Adyen | 91.33% | 91.51% | -0.20% | 9,005 |  |
| No Payment | 100.0% | 100.0% | +0.00% | 39 |  |

---

## L2: YE Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 97.30% | 0.00% | +0.00% | 74 | 0 |  |
| None | 0.00% | 96.85% | -100.00% | 0 | 127 | ⚠️ |
| credit_card | 83.46% | 87.60% | -4.73% | 2,461 | 2,509 |  |
| paypal | 93.90% | 95.19% | -1.36% | 770 | 831 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 88.89% | 96.30% | -7.69% | 18 | 27 | ⚠️ |
| Adyen | 83.83% | 87.96% | -4.70% | 2,517 | 2,609 |  |
| Braintree | 93.90% | 95.19% | -1.36% | 770 | 831 |  |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 2,849 | 3,112 | 86.20% | 89.76% | -3.56 |
| Insufficient Funds | 381 | 277 | 11.53% | 7.99% | +3.54 |
| Other reasons | 20 | 30 | 0.61% | 0.87% | -0.26 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 53 | 47 | 1.60% | 1.36% | +0.25 |
| Unknown | 2 | 1 | 0.06% | 0.03% | +0.03 |

**Root Cause:** None + Unknown + Insufficient

---

## L2: TV Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| paypal | 83.33% | 100.00% | -16.67% | 6 | 4 | ⚠️ |
| cashcredit | 100.00% | 100.00% | +0.00% | 8 | 3 |  |
| klarna | 99.35% | 99.28% | +0.07% | 155 | 139 |  |
| credit_card | 95.60% | 89.77% | +6.50% | 91 | 88 | ⚠️ |
| applepay | 92.06% | 78.67% | +17.03% | 63 | 75 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| No Payment | 100.00% | 100.00% | +0.00% | 8 | 3 |  |
| Adyen | 97.97% | 95.59% | +2.48% | 246 | 227 |  |
| Braintree | 91.30% | 79.75% | +14.49% | 69 | 79 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Insufficient Funds | 6 | 25 | 1.86% | 8.09% | -6.23 |
| 1. SUCCESSFULL | 312 | 283 | 96.59% | 91.59% | +5.01 |
| Other reasons | 3 | 0 | 0.93% | 0.00% | +0.93 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 2 | 1 | 0.62% | 0.32% | +0.30 |

**Root Cause:** paypal + Braintree + Insufficient

---

## L2: TO Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| None | 0.00% | 0.00% | +0.00% | 0 | 1 |  |
| bancontact | 100.00% | 0.00% | +0.00% | 2 | 0 |  |
| cashcredit | 100.00% | 100.00% | +0.00% | 1 | 4 |  |
| paypal | 100.00% | 93.59% | +6.85% | 62 | 78 | ⚠️ |
| credit_card | 93.14% | 86.52% | +7.65% | 204 | 230 | ⚠️ |
| applepay | 89.47% | 76.47% | +17.00% | 76 | 102 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Unknown | 0.00% | 0.00% | +0.00% | 0 | 1 |  |
| No Payment | 100.00% | 100.00% | +0.00% | 1 | 4 |  |
| Adyen | 93.20% | 86.52% | +7.72% | 206 | 230 | ⚠️ |
| Braintree | 94.20% | 83.89% | +12.29% | 138 | 180 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| 1. SUCCESSFULL | 323 | 354 | 93.62% | 85.30% | +8.32 |
| Insufficient Funds | 15 | 42 | 4.35% | 10.12% | -5.77 |
| Refused - eg: Declined, Closed Card, Do Not Honor, etc. | 3 | 10 | 0.87% | 2.41% | -1.54 |
| Other reasons | 4 | 8 | 1.16% | 1.93% | -0.77 |
| Unknown | 0 | 1 | 0.00% | 0.24% | -0.24 |

**Root Cause:** paypal + Adyen + Insufficient

---

## L3: Related Metrics (Loyalty: LL0 (Initial charges))

| Metric | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|--------|--------|--------|----------|----------|----------|------|
| 1_FirstRunAR | 89.67% | 89.93% | -0.29% | 29,747 | 32,243 |  |
| 2_PreDunningAR | 92.07% | 92.36% | -0.32% | 29,747 | 32,243 |  |
| 3_PostDunningAR | 92.33% | 92.62% | -0.32% | 29,747 | 32,243 |  |
| 6_PaymentApprovalRate | 92.5% | 92.76% | -0.28% | 29,747 | 32,243 |  |

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 19,876 | 18,445 | -7.2% | Stable |
| CF | High (>92%) | 6,632 | 5,956 | -10.2% | Stable |
| YE | Medium (>85%) | 3,467 | 3,305 | -4.7% | Stable |
| TT | High (>92%) | 728 | 633 | -13.0% | Stable |
| TZ | High (>92%) | 520 | 460 | -11.5% | Stable |
| TO | Medium (>85%) | 415 | 345 | -16.9% | Stable |
| TV | Medium (>85%) | 309 | 323 | +4.5% | Stable |
| TK | Medium (>85%) | 296 | 280 | -5.4% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| YE | ↓ -3.96% | None -100.0% | Unknown -7.7% | Insufficient Funds +3.54pp | None + Unknown + Insufficient |
| TV | ↑ +5.47% | paypal -16.7% | Braintree +14.5% | Insufficient Funds -6.23pp | paypal + Braintree + Insufficient |
| TO | ↑ +9.76% | paypal +6.8% | Adyen +7.7% | Insufficient Funds -5.77pp | paypal + Adyen + Insufficient |

---

*Report: 2026-05-12*
