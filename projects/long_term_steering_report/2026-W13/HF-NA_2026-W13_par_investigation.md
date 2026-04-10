# PAR Investigation: HF-NA 2026-W13

**Metric:** PAR  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 93.96% → 94.0% (+0.04%)  
**Volume:** 507,188 orders

## Executive Summary

**Overall:** PAR improved marginally by +0.04 pp (93.96% → 94.0%) on volume of 507,188 orders, continuing a positive trend observed over the past 7 weeks.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Consistent improvement since W07 | +0.50 pp over 8 weeks | ✅ |
| L1: Country Breakdown | All countries within threshold | US +0.05 pp, CA +0.26 pp | ✅ |
| L1: Payment Method | All methods improved | +0.04 pp to +0.27 pp | ✅ |
| L1: Payment Provider | Minor decline in Unknown provider | -1.59 pp (510 orders only) | ⚠️ |

**Key Findings:**
- PAR has shown consistent week-over-week improvement since W07, rising from 93.5% to 94.0% (+0.50 pp total)
- CA outperformed US with +0.26 pp improvement vs +0.05 pp, though US represents the majority of volume (505,599 orders)
- PaymentProvider "Unknown" declined by -1.59 pp, but impact is negligible due to low volume (510 orders, 0.1% of total)
- All payment methods showed improvement, with "Others" (+0.27 pp) and PayPal (+0.23 pp) leading gains
- Order volume has been declining week-over-week (from 570,585 in W07 to 507,188 in W14), warranting separate monitoring

**Action:** Monitor — The +0.04 pp improvement is within normal variance and all key segments are performing positively. Continue tracking the declining volume trend separately.

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
