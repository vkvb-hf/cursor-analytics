# AR Initial (LL0) Investigation: RTE 2026-W12

**Metric:** AR Initial (LL0)  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 91.4% → 90.89% (-0.56%)  
**Volume:** 31,900 orders

## Executive Summary

## Executive Summary

**Overall:** AR Initial (LL0) declined from 91.4% to 90.89% (-0.56pp) week-over-week, continuing a downward trend observed over the past 8 weeks from a high of 93.59% in W09.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0 Trend | 8-week pattern | -2.70pp from W09 peak | ⚠️ |
| L1 Country | TO threshold breach | -3.02pp | ⚠️ |
| L1 Country | TZ decline | -2.37pp | ⚠️ |
| L1 Country | TK decline | -2.13pp | ⚠️ |
| L1 Payment Provider | Unknown provider | -33.33pp | ⚠️ |
| L1 Payment Method | Apple Pay | -0.52pp | ✅ |

**Key Findings:**
- **Sustained decline:** The metric has dropped consistently from 93.59% (W09) to 90.89% (W14), a cumulative decline of 2.70pp over 6 weeks
- **Volume reduction:** Order volume decreased significantly from 46,087 (W09) to 31,900 (W14), a 31% drop in volume
- **TO country flagged:** TO exceeded the ±2.5% threshold with a -3.02pp decline (77.88% → 75.53%) on 805 orders
- **Multiple countries declining:** TZ (-2.37pp) and TK (-2.13pp) also show notable deterioration, though below threshold
- **Unknown PaymentProvider anomaly:** Shows -33.33pp drop but on minimal volume (9 orders), likely noise

**Action:** **Investigate** — The persistent multi-week decline combined with significant volume reduction and TO country breach warrants deeper investigation into root causes, particularly focusing on TO market conditions and the correlation between declining volume and rate deterioration.

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
