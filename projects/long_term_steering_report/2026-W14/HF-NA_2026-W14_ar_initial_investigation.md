# AR Initial (LL0) Investigation: HF-NA 2026-W14

**Metric:** AR Initial (LL0)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 89.1% → 89.66% (+0.63%)  
**Volume:** 17,242 orders

## Executive Summary

**Overall:** AR Initial (LL0) improved by +0.63 pp (89.1% → 89.66%) on a volume of 17,242 orders, recovering from the prior week's decline and returning to levels consistent with the 8-week trend.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0 Trend | Rate within 8-week range (89.37%-90.82%) | +0.63 pp | ✅ |
| L1 Country | Any country Δ > ±2.5 pp | US +4.43 pp | ⚠️ |
| L1 Payment Method | Any method Δ > ±2.5 pp | None | ✅ |
| L1 Payment Provider | Any provider Δ > ±2.5 pp | Adyen -4.74 pp, Unknown +3.40 pp | ⚠️ |

**Key Findings:**
- US showed significant improvement of +4.43 pp (66.77% → 69.72%) with high volume (24,598 orders), driving the overall metric increase
- CA remained stable with minimal change (+0.18 pp) at 80.88% on 7,779 orders
- Adyen experienced a notable decline of -4.74 pp (97.75% → 93.12%), though on low volume (218 orders)
- Unknown payment provider improved by +3.40 pp (95.16% → 98.39%) on 621 orders
- Volume decreased significantly from prior weeks (17,242 vs. 25,000+ in W07-W10), which may amplify rate volatility

**Action:** Monitor — The overall improvement is positive and within normal trend ranges. The US improvement warrants observation to determine if it's sustainable. Adyen's decline should be monitored given low volume but notable rate drop.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 89.66% | 17,242 | +0.63% ← REPORTED CHANGE |
| 2026-W13 | 89.1% | 16,215 | -0.60% |
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
| CA | 80.88% | 80.74% | +0.18% | 7,779 |  |
| US | 69.72% | 66.77% | +4.43% | 24,598 | ⚠️ |

**Countries exceeding ±2.5% threshold:** US

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Paypal | 90.25% | 90.77% | -0.58% | 1,333 |
| PaymentMethod | Credit Card | 89.43% | 89.0% | +0.49% | 9,781 |
| PaymentMethod | Others | 98.85% | 98.0% | +0.86% | 866 |
| PaymentMethod | Apple Pay | 88.43% | 86.78% | +1.90% | 5,262 |
| PaymentProvider | Adyen | 93.12% | 97.75% | -4.74% | 218 |
| PaymentProvider | No Payment | 100.0% | 99.5% | +0.50% | 163 |
| PaymentProvider | Braintree | 88.7% | 88.18% | +0.59% | 6,980 |
| PaymentProvider | ProcessOut | 89.54% | 88.7% | +0.94% | 9,260 |
| PaymentProvider | Unknown | 98.39% | 95.16% | +3.40% | 621 |

---

*Report: 2026-04-10*
