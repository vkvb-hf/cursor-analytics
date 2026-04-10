# AR Overall Investigation: HF-NA 2026-W13

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 92.23% → 92.17% (-0.07%)  
**Volume:** 507,188 orders

## Executive Summary

**Overall:** AR Overall declined slightly from 92.23% to 92.17% (-0.07pp) in 2026-W13, representing a minor dip within normal weekly fluctuation patterns across 507,188 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Stability check | -0.07pp | ✅ Within normal variance |
| L1: Country Breakdown | US & CA threshold (±2.5%) | US +0.05pp, CA +0.26pp | ✅ No flags |
| L1: PaymentMethod | Dimension scan | Range: -0.15pp to +0.27pp | ✅ Stable |
| L1: PaymentProvider | Dimension scan | Unknown: -5.67pp | ⚠️ Threshold exceeded |

**Key Findings:**
- PaymentProvider "Unknown" showed a significant decline of -5.67pp (91.04% → 85.88%), though volume is minimal at only 510 orders (0.1% of total)
- Both countries performed positively: US improved +0.05pp and CA improved +0.26pp, indicating the overall decline is not country-driven
- PayPal showed the strongest improvement among payment methods at +0.27pp (95.24% → 95.50%)
- The 8-week trend shows overall positive trajectory, with rates improving from 91.56% (W07) to 92.17% (W14), a gain of +0.61pp
- ProcessOut payment provider improved +0.37pp despite handling significant volume (82,249 orders)

**Action:** Monitor — The -0.07pp decline is within normal weekly variance. The PaymentProvider "Unknown" degradation warrants observation but low volume (510 orders) limits business impact. No immediate escalation required.

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
