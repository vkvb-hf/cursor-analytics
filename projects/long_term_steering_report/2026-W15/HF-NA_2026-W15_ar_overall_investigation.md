# AR Overall Investigation: HF-NA 2026-W15

**Metric:** AR Overall  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 92.17% → 92.43% (+0.28%)  
**Volume:** 497,775 orders

## Executive Summary

**Overall:** AR Overall improved from 92.17% to 92.43% (+0.26 pp) in W15, continuing a gradual upward trend observed over the 8-week period, with volume of 497,775 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | 8-week trend showing steady improvement from 91.35% to 92.43% | +0.26 pp | ✅ |
| L1: Country Impact | No countries exceeding ±2.5% threshold | US +0.34 pp, CA +0.02 pp | ✅ |
| L1: Payment Method | All methods within normal range | Apple Pay +0.56 pp (largest gain) | ✅ |
| L1: Payment Provider | Unknown provider declined but minimal volume | Unknown -0.91 pp (776 orders) | ⚠️ |

**Key Findings:**
- US drove the majority of the improvement with +0.34 pp gain on 492,811 orders (largest volume contributor)
- Apple Pay showed the strongest improvement among payment methods at +0.56 pp, though it maintains the lowest absolute rate (86.28%)
- Payment Provider "Unknown" declined -0.91 pp but represents minimal volume (776 orders, <0.2% of total)
- Braintree, the dominant provider (385,044 orders), improved +0.32 pp to 92.82%
- Volume decreased by ~9,400 orders (-1.9%) compared to W14, continuing a gradual volume decline trend

**Action:** Monitor – The improvement is modest and within normal fluctuation range. No dimensions exceeded alert thresholds, and the positive trend is consistent across major segments.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 92.43% | 497,775 | +0.28% ← REPORTED CHANGE |
| 2026-W14 | 92.17% | 507,189 | -0.07% |
| 2026-W13 | 92.23% | 517,599 | +0.10% |
| 2026-W12 | 92.14% | 526,516 | -0.15% |
| 2026-W11 | 92.28% | 539,763 | +0.30% |
| 2026-W10 | 92.0% | 554,777 | +0.45% |
| 2026-W09 | 91.59% | 553,112 | +0.26% |
| 2026-W08 | 91.35% | 548,921 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 93.52% | 93.5% | +0.02% | 103,253 |  |
| US | 93.1% | 92.78% | +0.34% | 492,811 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Others | 98.21% | 98.54% | -0.33% | 4,413 |
| PaymentMethod | Paypal | 95.59% | 95.4% | +0.20% | 60,610 |
| PaymentMethod | Credit Card | 92.94% | 92.72% | +0.24% | 366,508 |
| PaymentMethod | Apple Pay | 86.28% | 85.8% | +0.56% | 66,244 |
| PaymentProvider | Unknown | 91.11% | 91.94% | -0.91% | 776 |
| PaymentProvider | Adyen | 93.19% | 93.25% | -0.06% | 24,575 |
| PaymentProvider | No Payment | 100.0% | 100.0% | +0.00% | 3,578 |
| PaymentProvider | ProcessOut | 90.07% | 89.84% | +0.26% | 83,802 |
| PaymentProvider | Braintree | 92.82% | 92.52% | +0.32% | 385,044 |

---

*Report: 2026-04-14*
