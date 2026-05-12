# PCAR Investigation: RTE 2026-W19

**Metric:** Payment Checkout Approval Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 96.52% → 96.66% (+0.15%)  
**Volume:** 38,661 orders  
**Significance:** Not significant

## Executive Summary

**Overall:** Payment Checkout Approval Rate improved slightly from 96.52% to 96.66% (+0.15pp) in W19, a change that is not statistically significant, with total volume of 38,661 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (96.66% vs 96.88-97.22% historical) | +0.15pp | ✅ |
| L1: Country Scan | 1 country (TV) exceeds ±2.5% threshold | TV +4.60pp | ⚠️ |
| L1: Dimension Scan | No payment methods flagged | - | ✅ |
| L2: TV Deep-Dive | Klarna +6.44pp, Adyen +5.18pp identified | Improvement | ⚠️ |
| Mix Shift | All countries stable, no significant volume shifts | - | ✅ |

**Key Findings:**
- TV showed the largest rate improvement (+4.60pp, from 81.40% to 85.15%), driven by Klarna (+6.44pp) and Adyen (+5.18pp) performance gains
- TT experienced a notable decline (-2.40pp, from 77.34% to 75.49%) but remains below the ±2.5% flag threshold
- Overall volume decreased by ~4% week-over-week (40,202 → 38,661 orders), consistent with a gradual downward trend from W12 peak (44,209)
- FJ dominates volume (27,034 orders, 70% of total) with stable performance (+0.08pp)
- The 8-week trend shows a slight recovery from W18's dip (-0.55pp) but remains below the W15-W16 peak (~97.2%)

**Action:** Monitor - The +0.15pp improvement is not statistically significant and represents normal fluctuation. Continue tracking TV's Klarna/Adyen improvement to determine if gains are sustained, and monitor TT's declining trend.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W19 | 96.66% | 38,661 | +0.15% ← REPORTED CHANGE |
| 2026-W18 | 96.52% | 40,202 | -0.55% |
| 2026-W17 | 97.05% | 42,589 | -0.15% |
| 2026-W16 | 97.2% | 44,111 | -0.02% |
| 2026-W15 | 97.22% | 44,168 | +0.33% |
| 2026-W14 | 96.9% | 39,914 | +0.01% |
| 2026-W13 | 96.89% | 42,897 | +0.01% |
| 2026-W12 | 96.88% | 44,209 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TT | 75.49% | 77.34% | -2.40% | 824 |  |
| FJ | 97.26% | 97.19% | +0.08% | 27,034 |  |
| CF | 97.95% | 97.31% | +0.66% | 6,009 |  |
| TZ | 97.38% | 96.27% | +1.15% | 496 |  |
| TO | 94.20% | 92.23% | +2.13% | 448 |  |
| TV | 85.15% | 81.40% | +4.60% | 377 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TV

---

## L1: Dimension Scan

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|
| Unknown | nan% | nan% | +nan% | 0 |  |
| Others | 72.6% | 73.15% | -0.74% | 938 |  |
| Paypal | 98.09% | 98.14% | -0.05% | 4,444 |  |
| Credit Card | 97.09% | 96.9% | +0.20% | 24,437 |  |
| Apple Pay | 97.31% | 97.07% | +0.25% | 8,842 |  |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Flag |
|-------|--------|--------|----------|----------|------|

---

## L2: TV Deep-Dive

### PaymentMethod

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Paypal | 100.00% | 100.00% | +0.00% | 5 | 8 |  |
| CreditCard | 98.89% | 97.65% | +1.27% | 90 | 85 |  |
| ApplePay | 100.00% | 98.59% | +1.43% | 82 | 71 |  |
| Klarna | 72.50% | 68.12% | +6.44% | 200 | 207 | ⚠️ |

### PaymentProvider

| Value | Curr % | Prev % | Change % | Curr Vol | Prev Vol | Flag |
|-------|--------|--------|----------|----------|----------|------|
| Data not available | 0.00% | 0.00% | +0.00% | 0 | 0 |  |
| Braintree | 100.00% | 98.73% | +1.28% | 87 | 79 |  |
| Adyen | 80.69% | 76.71% | +5.18% | 290 | 292 | ⚠️ |

### Decline Reasons

| Reason | Curr Count | Prev Count | Curr % | Prev % | Δ pp |
|--------|------------|------------|--------|--------|------|
| Others | 377 | 371 | 100.00% | 100.00% | +0.00 |

**Root Cause:** Klarna + Adyen

---


## Mix Shift Analysis

| Country | AR Tier | Prev Volume | Curr Volume | Volume Δ | Impact |
| ------- | ------- | ----------- | ----------- | -------- | ------ |
| FJ | High (>92%) | 28,528 | 27,034 | -5.2% | Stable |
| CF | High (>92%) | 5,977 | 6,009 | +0.5% | Stable |
| YE | High (>92%) | 3,291 | 3,125 | -5.0% | Stable |
| TT | Low (>85%) | 843 | 824 | -2.3% | Stable |
| TZ | High (>92%) | 456 | 496 | +8.8% | Stable |
| TO | High (>92%) | 412 | 448 | +8.7% | Stable |
| TV | Low (>85%) | 371 | 377 | +1.6% | Stable |
| TK | High (>92%) | 324 | 348 | +7.4% | Stable |

---


## Decision Framework

**Root Cause Derivation:**

| Country | AR Change | PaymentMethod | PaymentProvider | Decline Reason | Root Cause |
| ------- | --------- | ------------- | --------------- | -------------- | ---------- |
| TV | ↑ +4.60% | Klarna +6.4% | Adyen +5.2% | → Stable | Klarna + Adyen |

---

*Report: 2026-05-12*
