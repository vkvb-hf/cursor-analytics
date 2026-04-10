# PAR Investigation: HF-NA 2026-W13

**Metric:** PAR  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 93.96% → 94.0% (+0.04%)  
**Volume:** 507,188 orders

## Executive Summary

## Executive Summary

**Overall:** PAR improved marginally from 93.96% to 94.0% (+0.04 pp) in 2026-W13, continuing a steady upward trend observed over the past 8 weeks.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Consistent improvement pattern | +0.50 pp since W07 | ✅ |
| L1: Country Breakdown | No country exceeds ±2.5% threshold | US +0.05 pp, CA +0.26 pp | ✅ |
| L1: Payment Method | All methods improved | +0.04 pp to +0.27 pp | ✅ |
| L1: Payment Provider | Unknown provider declined | -1.59 pp | ⚠️ |

**Key Findings:**
- PAR has shown consistent week-over-week improvement for 5 consecutive weeks, rising from 93.27% (W08) to 94.0% (W14)
- Canada outperformed the US with a +0.26 pp improvement vs +0.05 pp, though US represents the majority of volume (505,599 orders)
- PaymentProvider "Unknown" showed a notable decline of -1.59 pp (90.0% from 91.45%), but represents minimal volume (510 orders)
- All payment methods improved, with "Others" showing the largest gain (+0.27 pp) and PayPal maintaining the highest rate at 96.2%
- Volume decreased by approximately 2% week-over-week (507,188 vs 517,599), consistent with recent weekly declines

**Action:** Monitor — The +0.04 pp improvement is within normal variance and all major segments are performing positively. Continue monitoring the "Unknown" PaymentProvider segment for any volume increases that could impact overall PAR.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 94.0% | 507,188 | +0.04% |
| 2026-W13 | 93.96% | 517,599 | +0.10% ← REPORTED CHANGE |
| 2026-W12 | 93.87% | 526,516 | -0.04% |
| 2026-W11 | 93.91% | 539,763 | +0.29% |
| 2026-W10 | 93.64% | 554,777 | +0.30% |
| 2026-W09 | 93.36% | 553,112 | +0.10% |
| 2026-W08 | 93.27% | 548,921 | -0.25% |
| 2026-W07 | 93.5% | 570,585 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.85% | 92.8% | +0.05% | 505,599 |  |
| CA | 93.61% | 93.36% | +0.26% | 108,071 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Credit Card | 94.56% | 94.52% | +0.04% | 380,055 |
| PaymentMethod | Apple Pay | 88.28% | 88.1% | +0.20% | 69,160 |
| PaymentMethod | Paypal | 96.2% | 95.98% | +0.23% | 63,431 |
| PaymentMethod | Others | 98.83% | 98.56% | +0.27% | 4,953 |
| PaymentProvider | Unknown | 90.0% | 91.45% | -1.59% | 510 |
| PaymentProvider | Braintree | 94.12% | 94.03% | +0.10% | 404,848 |
| PaymentProvider | ProcessOut | 92.29% | 92.19% | +0.11% | 82,249 |
| PaymentProvider | Adyen | 95.96% | 95.76% | +0.21% | 26,148 |
| PaymentProvider | No Payment | 99.97% | 99.71% | +0.27% | 3,844 |

---

*Report: 2026-04-10*
