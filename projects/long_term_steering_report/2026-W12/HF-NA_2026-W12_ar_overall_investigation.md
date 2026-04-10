# AR Overall Investigation: HF-NA 2026-W12

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 92.23% → 92.17% (-0.07%)  
**Volume:** 507,188 orders

## Executive Summary

## Executive Summary

**Overall:** AR Overall declined by -0.07 percentage points (92.23% → 92.17%) on volume of 507,188 orders in 2026-W12, representing a minor week-over-week decrease within normal fluctuation range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (91.35%-92.28%) | -0.07pp | ✅ |
| L1: Country Breakdown | No country exceeds ±2.5% threshold | US: -0.17pp, CA: -0.01pp | ✅ |
| L1: Payment Method | Credit Card shows largest volume impact | -0.20pp on 384,303 orders | ⚠️ |
| L1: Payment Provider | Unknown provider shows significant drop | -2.12pp (low volume: 737) | ⚠️ |

**Key Findings:**
- The -0.07pp decline is modest and the current rate of 92.17% remains within the 8-week range (91.35% to 92.28%)
- US drove most of the decline at -0.17pp on 517,442 orders, while CA remained essentially flat at -0.01pp
- Credit Card payments declined -0.20pp on the highest volume (384,303 orders), contributing most to the overall drop
- PaymentProvider "Unknown" showed a notable -2.12pp decline, but on minimal volume (737 orders), limiting overall impact
- ProcessOut showed positive movement at +0.32pp on 81,514 orders, partially offsetting declines elsewhere

**Action:** Monitor – The decline is within normal weekly variance, no country exceeded the ±2.5% threshold, and the 8-week trend shows overall improvement from W07 (91.56%) to W12 (92.17%). Continue standard monitoring; no escalation required.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 92.17% | 507,188 | -0.07% |
| 2026-W13 | 92.23% | 517,599 | +0.10% |
| 2026-W12 | 92.14% | 526,516 | -0.15% ← REPORTED CHANGE |
| 2026-W11 | 92.28% | 539,763 | +0.29% |
| 2026-W10 | 92.01% | 554,777 | +0.46% |
| 2026-W09 | 91.59% | 553,112 | +0.26% |
| 2026-W08 | 91.35% | 548,921 | -0.23% |
| 2026-W07 | 91.56% | 570,585 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.8% | 92.95% | -0.17% | 517,442 |  |
| CA | 93.36% | 93.37% | -0.01% | 106,081 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Others | 98.51% | 98.82% | -0.31% | 5,772 |
| PaymentMethod | Credit Card | 92.73% | 92.92% | -0.20% | 384,303 |
| PaymentMethod | Paypal | 95.24% | 95.28% | -0.05% | 64,729 |
| PaymentMethod | Apple Pay | 85.65% | 85.55% | +0.12% | 71,712 |
| PaymentProvider | Unknown | 91.04% | 93.02% | -2.12% | 737 |
| PaymentProvider | No Payment | 99.71% | 99.84% | -0.13% | 4,426 |
| PaymentProvider | Braintree | 92.51% | 92.63% | -0.13% | 414,527 |
| PaymentProvider | Adyen | 93.28% | 93.36% | -0.08% | 25,312 |
| PaymentProvider | ProcessOut | 89.48% | 89.19% | +0.32% | 81,514 |

---

*Report: 2026-04-10*
