# PAR Investigation: HF-NA 2026-W12

**Metric:** PAR  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 93.96% → 94.0% (+0.04%)  
**Volume:** 507,188 orders

## Executive Summary

## Executive Summary

**Overall:** PAR improved slightly from 93.96% to 94.0% (+0.04 pp) on 507,188 orders, continuing a positive 8-week trend from 93.5% in W07.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Sustained improvement pattern | +0.50 pp over 8 weeks | ✅ |
| L1: Country Breakdown | No country exceeds ±2.5% threshold | US -0.17 pp, CA -0.01 pp | ✅ |
| L1: Payment Method | All methods within normal variance | Apple Pay +0.28 pp (best performer) | ✅ |
| L1: Payment Provider | Unknown provider shows decline | Unknown -2.02 pp | ⚠️ |

**Key Findings:**
- PAR has shown consistent week-over-week improvement, climbing from 93.5% (W07) to 94.0% (W14), representing a +0.50 pp gain over the 8-week period
- US market declined -0.17 pp (92.95% → 92.8%) while CA remained essentially flat at -0.01 pp (93.37% → 93.36%)
- PaymentProvider "Unknown" dropped -2.02 pp (93.33% → 91.45%), though volume is minimal at only 737 orders (0.15% of total)
- ProcessOut showed the strongest provider improvement at +0.65 pp (91.6% → 92.19%) on 81,514 orders
- Apple Pay improved +0.28 pp (87.86% → 88.1%) but remains the lowest-performing payment method at 88.1%

**Action:** Monitor — The +0.04 pp improvement aligns with the positive 8-week trend. No dimensions exceed the ±2.5% threshold. Continue standard monitoring; consider investigating Apple Pay's persistently lower performance (88.1% vs. 94.0% overall) as a potential optimization opportunity.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 94.0% | 507,188 | +0.04% |
| 2026-W13 | 93.96% | 517,599 | +0.10% |
| 2026-W12 | 93.87% | 526,516 | -0.04% ← REPORTED CHANGE |
| 2026-W11 | 93.91% | 539,763 | +0.29% |
| 2026-W10 | 93.64% | 554,777 | +0.30% |
| 2026-W09 | 93.36% | 553,112 | +0.10% |
| 2026-W08 | 93.27% | 548,921 | -0.25% |
| 2026-W07 | 93.5% | 570,585 | - |

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
| PaymentMethod | Others | 98.56% | 98.88% | -0.32% | 5,772 |
| PaymentMethod | Credit Card | 94.52% | 94.61% | -0.09% | 384,303 |
| PaymentMethod | Paypal | 95.98% | 95.99% | -0.01% | 64,729 |
| PaymentMethod | Apple Pay | 88.1% | 87.86% | +0.28% | 71,712 |
| PaymentProvider | Unknown | 91.45% | 93.33% | -2.02% | 737 |
| PaymentProvider | No Payment | 99.71% | 99.84% | -0.13% | 4,426 |
| PaymentProvider | Braintree | 94.03% | 94.11% | -0.09% | 414,527 |
| PaymentProvider | Adyen | 95.76% | 95.82% | -0.07% | 25,312 |
| PaymentProvider | ProcessOut | 92.19% | 91.6% | +0.65% | 81,514 |

---

*Report: 2026-04-10*
