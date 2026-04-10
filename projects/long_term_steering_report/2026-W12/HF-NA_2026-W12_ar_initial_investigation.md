# AR Initial (LL0) Investigation: HF-NA 2026-W12

**Metric:** AR Initial (LL0)  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 89.1% → 89.66% (+0.63%)  
**Volume:** 17,242 orders

## Executive Summary

**Overall:** AR Initial (LL0) improved week-over-week from 89.1% to 89.66% (+0.56 pp), with the metric stabilizing within a normal fluctuation range observed over the 8-week trend period.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within historical range (89.37%-90.82%) | +0.56 pp | ✅ |
| L1: Country Impact | No country exceeding ±2.5% threshold | US: -0.86 pp, CA: +0.33 pp | ✅ |
| L1: Payment Method | All methods declined but within threshold | PayPal: -2.02 pp (largest) | ⚠️ |
| L1: Payment Provider | Braintree & ProcessOut declined | Braintree: -1.50 pp | ⚠️ |

**Key Findings:**
- Volume decreased significantly from 21,080 (W12) to 17,242 (W12→W14), representing an 18% reduction in order volume
- PayPal experienced the largest payment method decline at -2.02 pp (91.47% → 89.62%) with 1,619 orders
- Braintree, the highest-volume provider (12,049 orders), declined by -1.50 pp (90.02% → 88.67%)
- All payment methods showed negative movement, suggesting a systemic rather than isolated issue
- Adyen was the only payment provider showing improvement (+1.27 pp), though with relatively low volume (627 orders)

**Action:** Monitor — The overall metric improved and remains within historical norms. Continue monitoring PayPal and Braintree performance; if declines persist beyond -2.5% threshold in the next reporting period, escalate for deeper investigation.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 89.66% | 17,242 | +0.63% |
| 2026-W13 | 89.1% | 16,215 | -0.60% |
| 2026-W12 | 89.64% | 21,080 | -1.30% ← REPORTED CHANGE |
| 2026-W11 | 90.82% | 21,784 | +1.09% |
| 2026-W10 | 89.84% | 25,446 | +0.25% |
| 2026-W09 | 89.62% | 25,208 | -0.19% |
| 2026-W08 | 89.79% | 25,674 | +0.47% |
| 2026-W07 | 89.37% | 28,927 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 68.09% | 68.68% | -0.86% | 27,055 |  |
| CA | 80.95% | 80.69% | +0.33% | 8,495 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Paypal | 89.62% | 91.47% | -2.02% | 1,619 |
| PaymentMethod | Credit Card | 89.04% | 90.45% | -1.56% | 11,382 |
| PaymentMethod | Apple Pay | 88.08% | 88.99% | -1.02% | 6,258 |
| PaymentMethod | Others | 98.85% | 99.09% | -0.25% | 1,821 |
| PaymentProvider | Braintree | 88.67% | 90.02% | -1.50% | 12,049 |
| PaymentProvider | ProcessOut | 88.97% | 90.15% | -1.30% | 7,155 |
| PaymentProvider | No Payment | 98.22% | 98.78% | -0.57% | 674 |
| PaymentProvider | Unknown | 99.3% | 99.38% | -0.07% | 575 |
| PaymentProvider | Adyen | 97.93% | 96.7% | +1.27% | 627 |

---

*Report: 2026-04-10*
