# AR Initial (LL0) Investigation: US-HF 2026-W14

**Metric:** AR Initial (LL0)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 87.53% → 88.84% (+1.50%)  
**Volume:** 11,716 orders

## Executive Summary

**Overall:** AR Initial (LL0) improved from 87.53% to 88.84% (+1.31 pp) in W14, recovering partially from the prior week's decline but remaining below the W11 peak of 90.11%.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Rate | 87.53% → 88.84% | +1.31 pp | ✅ |
| L1: US Country | 66.77% → 69.72% | +2.95 pp | ⚠️ |
| L1: Apple Pay | 84.92% → 87.13% | +2.21 pp | ⚠️ |
| L1: ProcessOut | 87.54% → 89.36% | +1.82 pp | ✅ |
| L1: Credit Card | 88.26% → 89.22% | +0.96 pp | ✅ |

**Key Findings:**
- US country performance improved significantly by +4.43% (66.77% → 69.72%), exceeding the ±2.5% monitoring threshold
- Apple Pay showed the largest payment method improvement at +2.60 pp (84.92% → 87.13%), with 4,000 orders processed
- ProcessOut provider improved by +2.07 pp (87.54% → 89.36%) on 6,146 orders, contributing to overall gains
- Volume decreased 38% from W10 peak (19,259) to W14 (11,716), which may amplify rate volatility
- PayPal and Others payment methods showed minor declines (-0.53 pp and -0.31 pp respectively) but with low volume impact

**Action:** Monitor — The improvement is positive but follows a volatile 8-week trend. Continue monitoring US performance and Apple Pay/ProcessOut to confirm sustained recovery toward the W11 benchmark of 90.11%.

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

*Report: 2026-04-09*
