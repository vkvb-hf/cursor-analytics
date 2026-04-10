# AR Initial (LL0) Investigation: HF-NA 2026-W13

**Metric:** AR Initial (LL0)  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 89.1% → 89.66% (+0.63%)  
**Volume:** 17,242 orders

## Executive Summary

**Overall:** AR Initial (LL0) improved by +0.63% (from 89.1% to 89.66%) in 2026-W14, recovering from the prior week's decline and returning to levels consistent with the 8-week trend.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | Rate increased +0.63% WoW | +0.56pp | ✅ |
| L1: Country Impact | No country exceeds ±2.5% threshold | US -1.95%, CA -0.26% | ✅ |
| L1: Payment Method | Apple Pay declined most | -1.48% | ✅ |
| L1: Payment Provider | Unknown provider significant drop | -4.18% | ⚠️ |

**Key Findings:**
- The +0.63% improvement reverses the -0.60% decline seen in W13, bringing the rate back to 89.66% which aligns with the 8-week average (~89.5%)
- PaymentProvider "Unknown" shows a notable decline of -4.18% (95.16% vs 99.30%), though volume is limited at 351 orders
- US shows a -1.95% decline (66.77% vs 68.09%) with the largest volume (23,515 orders), remaining below threshold but worth monitoring
- Apple Pay declined -1.48% (86.78% vs 88.08%) with meaningful volume of 4,750 orders
- PayPal showed positive movement at +1.28% (90.77% vs 89.62%)

**Action:** Monitor — The overall metric has recovered and no country breaches the ±2.5% threshold. Continue to watch the "Unknown" PaymentProvider trend and US performance in coming weeks.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 89.66% | 17,242 | +0.63% |
| 2026-W13 | 89.1% | 16,215 | -0.60% ← REPORTED CHANGE |
| 2026-W12 | 89.64% | 21,080 | -1.30% |
| 2026-W11 | 90.82% | 21,784 | +1.09% |
| 2026-W10 | 89.84% | 25,446 | +0.25% |
| 2026-W09 | 89.62% | 25,208 | -0.19% |
| 2026-W08 | 89.79% | 25,674 | +0.47% |
| 2026-W07 | 89.37% | 28,927 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 66.77% | 68.09% | -1.95% | 23,515 |  |
| CA | 80.74% | 80.95% | -0.26% | 7,706 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Apple Pay | 86.78% | 88.08% | -1.48% | 4,750 |
| PaymentMethod | Others | 98.0% | 98.85% | -0.85% | 1,101 |
| PaymentMethod | Credit Card | 89.0% | 89.04% | -0.05% | 9,096 |
| PaymentMethod | Paypal | 90.77% | 89.62% | +1.28% | 1,268 |
| PaymentProvider | Unknown | 95.16% | 99.3% | -4.18% | 351 |
| PaymentProvider | Braintree | 88.18% | 88.67% | -0.56% | 7,739 |
| PaymentProvider | ProcessOut | 88.7% | 88.97% | -0.31% | 7,256 |
| PaymentProvider | Adyen | 97.75% | 97.93% | -0.18% | 668 |
| PaymentProvider | No Payment | 99.5% | 98.22% | +1.31% | 201 |

---

*Report: 2026-04-10*
