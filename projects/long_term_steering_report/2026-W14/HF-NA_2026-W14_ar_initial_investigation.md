# AR Initial (LL0) Investigation: HF-NA 2026-W14

**Metric:** AR Initial (LL0)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 89.1% → 89.66% (+0.63%)  
**Volume:** 17,242 orders

## Executive Summary

## Executive Summary

**Overall:** AR Initial (LL0) improved from 89.1% to 89.66% (+0.63 pp) in W14, representing a recovery from the prior week's decline and returning closer to the 8-week average performance.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | Rate increased +0.63 pp on lower volume (17,242 vs 16,215) | +0.63 pp | ✅ |
| L1: Country - CA | Stable performance | +0.18 pp | ✅ |
| L1: Country - US | Significant increase exceeding ±2.5% threshold | +4.43 pp | ⚠️ |
| L1: PaymentProvider - Adyen | Notable decline on low volume (218 orders) | -4.74 pp | ⚠️ |
| L1: PaymentProvider - Unknown | Increase exceeding typical variance | +3.40 pp | ✅ |

**Key Findings:**
- US showed a significant +4.43 pp improvement (66.77% → 69.72%), flagged for exceeding the ±2.5% threshold, driving the overall metric increase
- PaymentProvider Adyen experienced a -4.74 pp decline (97.75% → 93.12%), though on limited volume of only 218 orders
- Volume decreased substantially from W11-W12 levels (~21K) to current W14 (17,242), continuing a downward trend from W07 peak (28,927)
- Apple Pay showed solid improvement of +1.90 pp (86.78% → 88.43%) on meaningful volume (5,262 orders)
- The metric has fluctuated within a narrow band of 89.1%-90.82% over the past 8 weeks, indicating relative stability

**Action:** Monitor – The overall improvement is positive and within normal operating range. Continue monitoring US performance to confirm the +4.43 pp gain is sustained, and watch Adyen provider for potential emerging issues despite low volume.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 89.66% | 17,242 | +0.63% ← REPORTED CHANGE |
| 2026-W13 | 89.1% | 16,215 | -0.60% |
| 2026-W12 | 89.64% | 21,080 | -1.30% |
| 2026-W11 | 90.82% | 21,784 | +1.09% |
| 2026-W10 | 89.84% | 25,446 | +0.25% |
| 2026-W09 | 89.62% | 25,208 | -0.19% |
| 2026-W08 | 89.79% | 25,674 | +0.47% |
| 2026-W07 | 89.37% | 28,927 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 80.88% | 80.74% | +0.18% | 7,779 |  |
| US | 69.72% | 66.77% | +4.43% | 24,598 | ⚠️ |

**Countries exceeding ±2.5% threshold:** US

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Paypal | 90.25% | 90.77% | -0.58% | 1,333 |
| PaymentMethod | Credit Card | 89.43% | 89.0% | +0.49% | 9,781 |
| PaymentMethod | Others | 98.85% | 98.0% | +0.86% | 866 |
| PaymentMethod | Apple Pay | 88.43% | 86.78% | +1.90% | 5,262 |
| PaymentProvider | Adyen | 93.12% | 97.75% | -4.74% | 218 |
| PaymentProvider | No Payment | 100.0% | 99.5% | +0.50% | 163 |
| PaymentProvider | Braintree | 88.7% | 88.18% | +0.59% | 6,980 |
| PaymentProvider | ProcessOut | 89.54% | 88.7% | +0.94% | 9,260 |
| PaymentProvider | Unknown | 98.39% | 95.16% | +3.40% | 621 |

---

*Report: 2026-04-09*
