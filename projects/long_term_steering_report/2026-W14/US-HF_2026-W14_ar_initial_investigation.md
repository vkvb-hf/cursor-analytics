# AR Initial (LL0) Investigation: US-HF 2026-W14

**Metric:** AR Initial (LL0)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 87.53% → 88.84% (+1.50%)  
**Volume:** 11,716 orders

## Executive Summary

**Overall:** AR Initial (LL0) improved from 87.53% to 88.84% (+1.50%, equivalent to +1.31 pp) in W14, representing a positive recovery after the prior week's decline.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | W14 vs W13 | +1.50% | ✅ |
| L1: Country (US) | Threshold ±2.5% | +4.43% | ⚠️ |
| L1: PaymentMethod | Credit Card | +1.09% | ✅ |
| L1: PaymentMethod | Apple Pay | +2.60% | ⚠️ |
| L1: PaymentProvider | ProcessOut | +2.07% | ✅ |

**Key Findings:**
- US showed significant improvement of +4.43%, exceeding the ±2.5% threshold and flagged for attention
- Apple Pay acceptance rate improved notably by +2.60% (from 84.92% to 87.13%) with 4,000 orders
- ProcessOut provider improved by +2.07% (from 87.54% to 89.36%) handling 6,146 orders, the highest volume among providers
- Volume decreased significantly from prior weeks (11,716 in W14 vs 19,259 in W10), though rate recovered
- PayPal showed slight decline of -0.53% but remains the highest performing payment method at 90.57%

**Action:** Monitor — The metric shows healthy recovery with no critical degradations. Continue tracking US performance and Apple Pay trends to confirm sustained improvement.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 88.84% | 11,716 | +1.50% ← REPORTED CHANGE |
| 2026-W13 | 87.53% | 10,955 | -1.30% |
| 2026-W12 | 88.68% | 14,786 | -1.59% |
| 2026-W11 | 90.11% | 15,868 | +0.95% |
| 2026-W10 | 89.26% | 19,259 | +0.01% |
| 2026-W09 | 89.25% | 18,657 | -0.36% |
| 2026-W08 | 89.57% | 18,802 | +0.88% |
| 2026-W07 | 88.79% | 21,838 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 69.72% | 66.77% | +4.43% | 24,598 | ⚠️ |

**Countries exceeding ±2.5% threshold:** US

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Paypal | 90.57% | 91.05% | -0.53% | 870 |
| PaymentMethod | Others | 98.1% | 98.4% | -0.31% | 315 |
| PaymentMethod | Credit Card | 89.22% | 88.26% | +1.09% | 6,531 |
| PaymentMethod | Apple Pay | 87.13% | 84.92% | +2.60% | 4,000 |
| PaymentProvider | No Payment | 100.0% | 100.0% | +0.00% | 104 |
| PaymentProvider | Unknown | 97.16% | 96.91% | +0.26% | 211 |
| PaymentProvider | Braintree | 87.69% | 87.2% | +0.56% | 5,255 |
| PaymentProvider | ProcessOut | 89.36% | 87.54% | +2.07% | 6,146 |

---

*Report: 2026-04-10*
