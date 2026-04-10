# PAR Investigation: HF-NA 2026-W14

**Metric:** PAR  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 93.96% → 94.0% (+0.04%)  
**Volume:** 507,188 orders

## Executive Summary

**Overall:** PAR improved marginally from 93.96% to 94.0% (+0.04 pp) on volume of 507,188 orders, continuing a steady upward trend over the past 8 weeks.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Stable/Improving | +0.04 pp | ✅ |
| L1: Country Breakdown | No country exceeds ±2.5% threshold | CA: -0.10 pp, US: -0.07 pp | ✅ |
| L1: Dimension Scan | No major dimension shifts | Range: -0.10 pp to +0.44 pp | ✅ |
| L1: Outlier Detection | One outlier detected | Unknown Provider: +6.86 pp | ⚠️ |

**Key Findings:**
- PAR has improved consistently over the 8-week period, rising from 93.5% (W07) to 94.0% (W14), a cumulative gain of +0.50 pp
- Both CA (-0.10 pp) and US (-0.07 pp) showed slight declines this week, but neither breaches the ±2.5% threshold
- Apple Pay showed the strongest improvement among major payment methods at +0.29 pp (88.28% → 88.54%)
- PaymentProvider "Unknown" showed a +6.86 pp spike (90.0% → 96.17%), but volume is minimal (758 orders, 0.15% of total)
- Volume declined by ~2% week-over-week (517,599 → 507,188), continuing a gradual volume decrease trend

**Action:** Monitor — No significant anomalies detected; the metric continues its stable upward trajectory with all major segments performing within normal ranges.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 94.0% | 507,188 | +0.04% ← REPORTED CHANGE |
| 2026-W13 | 93.96% | 517,599 | +0.10% |
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
| CA | 93.52% | 93.61% | -0.10% | 105,528 |  |
| US | 92.79% | 92.85% | -0.07% | 497,052 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Paypal | 96.19% | 96.2% | -0.01% | 61,971 |
| PaymentMethod | Credit Card | 94.58% | 94.56% | +0.02% | 372,464 |
| PaymentMethod | Apple Pay | 88.54% | 88.28% | +0.29% | 68,380 |
| PaymentMethod | Others | 99.27% | 98.83% | +0.44% | 4,373 |
| PaymentProvider | Adyen | 95.86% | 95.96% | -0.10% | 25,367 |
| PaymentProvider | ProcessOut | 92.25% | 92.29% | -0.05% | 83,447 |
| PaymentProvider | No Payment | 100.0% | 99.97% | +0.03% | 3,501 |
| PaymentProvider | Braintree | 94.19% | 94.12% | +0.08% | 394,115 |
| PaymentProvider | Unknown | 96.17% | 90.0% | +6.86% | 758 |

---

*Report: 2026-04-10*
