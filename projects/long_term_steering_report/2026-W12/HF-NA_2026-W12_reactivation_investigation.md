# Reactivation Investigation: HF-NA 2026-W12

**Metric:** Reactivation  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 90.69% → 90.95% (+0.29%)  
**Volume:** 20,279 orders

## Executive Summary

**Overall:** Reactivation rate improved slightly from 90.69% to 90.95% (+0.26 pp), continuing a positive 8-week upward trend from 86.03% in W07 to 90.95% in W14.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Consistent improvement over period | +4.92 pp (W07→W14) | ✅ |
| L1: Country Breakdown | No country exceeds ±2.5% threshold | US: -0.17 pp, CA: -0.01 pp | ✅ |
| L1: Dimension Scan | Payment method variance detected | Credit Card: +2.78 pp | ⚠️ |

**Key Findings:**
- The reactivation rate has shown consistent improvement over 8 weeks, climbing from 86.03% (W07) to 90.95% (W14), a gain of +4.92 pp
- Both US (92.8%) and CA (93.36%) show stable performance with minimal week-over-week changes (-0.17 pp and -0.01 pp respectively)
- Credit Card payments showed the largest positive shift at +2.78 pp (88.29% → 90.74%), representing the highest volume segment at 14,613 orders
- PayPal (-0.64 pp) and Apple Pay (-0.56 pp) showed minor declines but remain within acceptable thresholds
- Volume decreased from 21,909 to 20,279 orders (-7.4%), though this did not negatively impact the reactivation rate

**Action:** Monitor — No significant anomalies detected. Continue tracking Credit Card payment performance as the primary volume driver.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 90.95% | 20,279 | +0.29% |
| 2026-W13 | 90.69% | 21,909 | -0.36% |
| 2026-W12 | 91.02% | 21,059 | +1.73% ← REPORTED CHANGE |
| 2026-W11 | 89.47% | 24,019 | +1.41% |
| 2026-W10 | 88.23% | 27,936 | +1.54% |
| 2026-W09 | 86.89% | 23,884 | -0.57% |
| 2026-W08 | 87.39% | 25,523 | +1.58% |
| 2026-W07 | 86.03% | 24,977 | - |

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
| PaymentMethod | Paypal | 93.7% | 94.3% | -0.64% | 3,271 |
| PaymentMethod | Apple Pay | 89.57% | 90.07% | -0.56% | 3,173 |
| PaymentMethod | Credit Card | 90.74% | 88.29% | +2.78% | 14,613 |
| PaymentMethod | Others | 50.0% | 33.33% | +50.00% | 2 |

---

*Report: 2026-04-10*
