# AR Overall Investigation: HF-NA 2026-W13

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 92.23% → 92.17% (-0.07%)  
**Volume:** 507,188 orders

## Executive Summary

**Overall:** AR Overall rate declined slightly from 92.23% to 92.17% (-0.06 pp) on a volume of 507,188 orders, representing a minor week-over-week decrease within normal fluctuation range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate stable within 91.35%-92.28% range | -0.06 pp | ✅ |
| L1: Country | No countries exceeding ±2.5% threshold | US +0.05 pp, CA +0.26 pp | ✅ |
| L1: PaymentMethod | All methods within normal range | -0.15 pp to +0.27 pp | ✅ |
| L1: PaymentProvider | Unknown provider significant decline | -5.67 pp | ⚠️ |

**Key Findings:**
- PaymentProvider "Unknown" showed a significant decline of -5.67 pp (91.04% → 85.88%), though on very low volume (510 orders)
- Both countries (US and CA) showed positive movement: US +0.05 pp and CA +0.26 pp, indicating the overall decline is not country-driven
- PayPal showed the strongest improvement among payment methods at +0.27 pp (95.24% → 95.50%)
- ProcessOut provider improved by +0.37 pp (89.48% → 89.81%) on meaningful volume of 82,249 orders
- The 8-week trend shows overall positive trajectory from 91.56% (W07) to 92.17% (W14)

**Action:** Monitor - The overall decline is minimal (-0.06 pp) and within normal weekly variance. The PaymentProvider "Unknown" decline warrants observation but represents <0.1% of total volume.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 92.17% | 507,188 | -0.07% |
| 2026-W13 | 92.23% | 517,599 | +0.10% ← REPORTED CHANGE |
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
| US | 92.85% | 92.8% | +0.05% | 505,599 |  |
| CA | 93.61% | 93.36% | +0.26% | 108,071 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Others | 98.36% | 98.51% | -0.15% | 4,953 |
| PaymentMethod | Credit Card | 92.79% | 92.73% | +0.06% | 380,055 |
| PaymentMethod | Apple Pay | 85.72% | 85.65% | +0.08% | 69,160 |
| PaymentMethod | Paypal | 95.5% | 95.24% | +0.27% | 63,431 |
| PaymentProvider | Unknown | 85.88% | 91.04% | -5.67% | 510 |
| PaymentProvider | Braintree | 92.58% | 92.51% | +0.07% | 404,848 |
| PaymentProvider | Adyen | 93.46% | 93.28% | +0.19% | 26,148 |
| PaymentProvider | No Payment | 99.97% | 99.71% | +0.27% | 3,844 |
| PaymentProvider | ProcessOut | 89.81% | 89.48% | +0.37% | 82,249 |

---

*Report: 2026-04-10*
