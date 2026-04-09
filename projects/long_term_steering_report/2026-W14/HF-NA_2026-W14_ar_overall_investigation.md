# AR Overall Investigation: HF-NA 2026-W14

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 92.23% → 92.17% (-0.07%)  
**Volume:** 507,188 orders

## Executive Summary

**Overall:** AR Overall declined slightly from 92.23% to 92.17% (-0.07 pp) in W14, representing a minor week-over-week decrease on 507,188 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| 8-Week Trend Stability | Within normal variance (91.35%-92.28% range) | -0.07 pp | ✅ |
| Country Threshold (±2.5%) | No countries exceeding threshold | CA: -0.10 pp, US: -0.07 pp | ✅ |
| Payment Method Impact | All methods within normal range | -0.09 pp to +0.15 pp | ✅ |
| Payment Provider Anomaly | Unknown provider showed +6.91 pp spike | Low volume (758 orders) | ⚠️ |

**Key Findings:**
- The -0.07 pp decline is within normal weekly fluctuation, with the 8-week range spanning 91.35% to 92.28%
- Both CA (-0.10 pp) and US (-0.07 pp) showed minor declines, neither exceeding the ±2.5% threshold
- Adyen showed the largest provider decline at -0.18 pp (25,367 orders), while Braintree (largest volume at 394,115 orders) declined only -0.05 pp
- PaymentProvider "Unknown" spiked +6.91 pp but represents minimal volume (758 orders / 0.15% of total)
- Apple Pay showed slight improvement (+0.10 pp) while PayPal and Credit Card both declined marginally

**Action:** Monitor — The decline is minimal and within normal operating variance. No single dimension shows concerning degradation at significant volume. Continue standard monitoring.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 92.17% | 507,188 | -0.07% ← REPORTED CHANGE |
| 2026-W13 | 92.23% | 517,599 | +0.10% |
| 2026-W12 | 92.14% | 526,516 | -0.15% |
| 2026-W11 | 92.28% | 539,763 | +0.29% |
| 2026-W10 | 92.01% | 554,777 | +0.46% |
| 2026-W09 | 91.59% | 553,112 | +0.26% |
| 2026-W08 | 91.35% | 548,921 | -0.23% |
| 2026-W07 | 91.56% | 570,585 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 93.52% | 93.61% | -0.10% | 105,528 |  |
| US | 92.79% | 92.85% | -0.07% | 497,052 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Paypal | 95.41% | 95.5% | -0.09% | 61,971 |
| PaymentMethod | Credit Card | 92.73% | 92.79% | -0.06% | 372,464 |
| PaymentMethod | Apple Pay | 85.8% | 85.72% | +0.10% | 68,380 |
| PaymentMethod | Others | 98.51% | 98.36% | +0.15% | 4,373 |
| PaymentProvider | Adyen | 93.29% | 93.46% | -0.18% | 25,367 |
| PaymentProvider | Braintree | 92.53% | 92.58% | -0.05% | 394,115 |
| PaymentProvider | ProcessOut | 89.84% | 89.81% | +0.03% | 83,447 |
| PaymentProvider | No Payment | 100.0% | 99.97% | +0.03% | 3,501 |
| PaymentProvider | Unknown | 91.82% | 85.88% | +6.91% | 758 |

---

*Report: 2026-04-09*
