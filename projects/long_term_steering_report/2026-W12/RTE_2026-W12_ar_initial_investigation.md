# AR Initial (LL0) Investigation: RTE 2026-W12

**Metric:** AR Initial (LL0)  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 91.4% → 90.89% (-0.56%)  
**Volume:** 31,900 orders

## Executive Summary

**Overall:** AR Initial (LL0) declined by -0.56 percentage points (pp) from 91.4% to 90.89% week-over-week, continuing a downward trend observed over the past 8 weeks with volume dropping to 31,900 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Rate | 91.4% → 90.89% | -0.56 pp | ⚠️ |
| L1: Country Threshold (±2.5%) | TO flagged at -3.02 pp | -3.02 pp | ⚠️ |
| L1: Payment Method | Apple Pay declined | -0.52 pp | ✅ |
| L1: Payment Provider | Unknown dropped significantly | -33.33 pp | ⚠️ |

**Key Findings:**
- The 8-week trend shows a consistent decline from 93.59% (W09) to 90.89% (W14), representing a cumulative drop of 2.7 pp alongside significant volume reduction (46,087 → 31,900 orders)
- TO is the only country exceeding the ±2.5% threshold with a -3.02 pp decline (77.88% → 75.53%), though volume is relatively low at 805 orders
- TZ (-2.37 pp) and TK (-2.13 pp) also show notable declines approaching the threshold
- Payment Provider "Unknown" shows a severe drop of -33.33 pp (100% → 66.67%), but with minimal volume impact (only 9 orders)
- FJ represents the largest volume (43,185 orders) and declined by -1.31 pp, contributing most to the overall metric movement

**Action:** Investigate - The sustained 8-week declining trend combined with the flagged country TO and significant volume reduction warrants deeper investigation into root causes, particularly focusing on FJ due to its volume impact.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 90.89% | 31,900 | -0.56% |
| 2026-W13 | 91.4% | 36,413 | -1.25% |
| 2026-W12 | 92.56% | 42,779 | +0.05% ← REPORTED CHANGE |
| 2026-W11 | 92.51% | 46,365 | -0.24% |
| 2026-W10 | 92.73% | 48,166 | -0.92% |
| 2026-W09 | 93.59% | 46,087 | +0.47% |
| 2026-W08 | 93.15% | 46,567 | +0.33% |
| 2026-W07 | 92.84% | 52,390 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TO | 75.53% | 77.88% | -3.02% | 805 | ⚠️ |
| TZ | 83.02% | 85.04% | -2.37% | 648 |  |
| TK | 88.53% | 90.46% | -2.13% | 436 |  |
| FJ | 85.25% | 86.39% | -1.31% | 43,185 |  |
| YE | 77.56% | 76.84% | +0.94% | 6,458 |  |
| CF | 85.51% | 84.62% | +1.06% | 7,641 |  |

**Countries exceeding ±2.5% threshold:** TO

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Apple Pay | 91.43% | 91.9% | -0.52% | 9,402 |
| PaymentMethod | Paypal | 96.29% | 96.21% | +0.09% | 4,720 |
| PaymentMethod | Credit Card | 91.99% | 91.84% | +0.17% | 26,002 |
| PaymentMethod | Others | 95.48% | 95.05% | +0.45% | 2,655 |
| PaymentProvider | Unknown | 66.67% | 100.0% | -33.33% | 9 |
| PaymentProvider | Braintree | 93.0% | 93.21% | -0.22% | 23,758 |
| PaymentProvider | ProcessOut | 92.5% | 92.66% | -0.18% | 7,755 |
| PaymentProvider | Adyen | 91.16% | 90.36% | +0.88% | 9,377 |
| PaymentProvider | No Payment | 94.31% | 93.43% | +0.94% | 1,880 |

---

*Report: 2026-04-10*
