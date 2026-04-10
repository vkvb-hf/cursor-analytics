# AR Overall Investigation: WL 2026-W13

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 89.72% → 89.33% (-0.43%)  
**Volume:** 165,018 orders

## Executive Summary

**Overall:** AR Overall declined by -0.43 percentage points (89.72% → 89.33%) in WL 2026-W13 with a volume of 165,018 orders, interrupting a generally positive trend observed since W07.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Consistent pattern? | -0.43 pp | ⚠️ Decline after 2 weeks of gains |
| L1: Country Impact | Any country > ±2.5%? | Max: -0.17 pp (KN) | ✅ No major outliers |
| L1: Payment Method | Any method > ±2.5%? | +12.74 pp (Others) | ⚠️ Anomaly in low-volume segment |
| L1: Payment Provider | Any provider > ±2.5%? | -37.50 pp (Unknown) | ⚠️ Severe drop in low-volume segment |

**Key Findings:**
- PaymentProvider "Unknown" experienced a severe decline of -37.50 pp (96.0% → 60.0%), though volume is minimal at only 15 orders
- PaymentMethod "Others" showed an unusual spike of +12.74 pp (87.48% → 98.62%) on 796 orders, suggesting data anomaly or classification change
- Braintree, the highest-volume provider (111,236 orders), declined slightly by -0.29 pp, contributing meaningfully to the overall drop
- All five countries remained within normal variance (±2.5% threshold), with changes ranging from -0.17 pp (KN) to +0.88 pp (CK)
- ProcessOut continues to underperform at 79.93% acceptance rate despite a +1.24 pp improvement

**Action:** Monitor — The overall decline is modest (-0.43 pp) and no major country or high-volume dimension shows significant deviation. The anomalies in "Unknown" provider and "Others" payment method warrant data quality review but involve negligible volume.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 89.33% | 165,018 | -0.43% |
| 2026-W13 | 89.72% | 169,667 | +0.07% ← REPORTED CHANGE |
| 2026-W12 | 89.66% | 169,891 | -0.14% |
| 2026-W11 | 89.79% | 174,933 | +0.80% |
| 2026-W10 | 89.08% | 179,964 | +1.01% |
| 2026-W09 | 88.19% | 180,862 | +0.06% |
| 2026-W08 | 88.14% | 179,647 | -0.50% |
| 2026-W07 | 88.58% | 186,442 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| KN | 87.61% | 87.76% | -0.17% | 10,365 |  |
| CG | 96.76% | 96.84% | -0.08% | 44,477 |  |
| ER | 89.92% | 89.54% | +0.43% | 73,655 |  |
| AO | 87.96% | 87.38% | +0.66% | 16,249 |  |
| CK | 94.15% | 93.33% | +0.88% | 42,197 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Credit Card | 89.23% | 89.34% | -0.13% | 120,798 |
| PaymentMethod | Apple Pay | 86.16% | 86.02% | +0.16% | 22,237 |
| PaymentMethod | Paypal | 94.82% | 94.61% | +0.23% | 25,836 |
| PaymentMethod | Others | 98.62% | 87.48% | +12.74% | 796 |
| PaymentProvider | Unknown | 60.0% | 96.0% | -37.50% | 15 |
| PaymentProvider | Braintree | 90.89% | 91.15% | -0.29% | 111,236 |
| PaymentProvider | No Payment | 100.0% | 99.8% | +0.20% | 747 |
| PaymentProvider | Adyen | 90.82% | 90.17% | +0.71% | 39,337 |
| PaymentProvider | ProcessOut | 79.93% | 78.95% | +1.24% | 18,332 |

---

*Report: 2026-04-10*
