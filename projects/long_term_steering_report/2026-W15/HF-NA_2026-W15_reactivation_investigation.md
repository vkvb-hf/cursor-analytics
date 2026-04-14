# Reactivation Investigation: HF-NA 2026-W15

**Metric:** Reactivation  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 90.95% → 90.24% (-0.78%)  
**Volume:** 26,178 orders

## Executive Summary

**Overall:** Reactivation rate declined from 90.95% to 90.24% (-0.78%, or -0.71 pp) in W15, representing a modest pullback after several weeks of improvement, on elevated volume of 26,178 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (86.89%-91.02%) | -0.71 pp | ✅ |
| L1: Country Breakdown | No country exceeds ±2.5% threshold | CA: +0.02%, US: +0.34% | ✅ |
| L1: Payment Method | "Others" shows extreme swing on low volume | -52.38% (n=7) | ⚠️ |
| L1: Payment Method | Major methods show minor declines | Credit Card: -0.72%, PayPal: -1.26% | ✅ |

**Key Findings:**
- The -0.78% WoW decline reverses a 3-week positive trend but remains well above W08-W10 levels (86.89%-88.23%)
- W15 volume (26,178) is the second-highest in the 8-week period, 29% above W14 (20,279), suggesting volume surge may have pressured conversion
- Both US (+0.34%) and CA (+0.02%) showed stable or improved rates, indicating no country-level driver for the decline
- PayPal experienced the largest decline among major payment methods (-1.26%, from 93.97% to 92.78%) on 4,016 orders
- "Others" payment method dropped -52.38% but on only 7 orders—statistically insignificant noise

**Action:** Monitor — The decline is within normal weekly variance, no country or major dimension exceeds thresholds, and the rate remains elevated vs. recent history. Continue standard monitoring; re-evaluate if W16 shows continued decline or if PayPal degradation persists.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 90.24% | 26,178 | -0.78% ← REPORTED CHANGE |
| 2026-W14 | 90.95% | 20,279 | +0.29% |
| 2026-W13 | 90.69% | 21,909 | -0.36% |
| 2026-W12 | 91.02% | 21,059 | +1.73% |
| 2026-W11 | 89.47% | 24,019 | +1.41% |
| 2026-W10 | 88.23% | 27,936 | +1.54% |
| 2026-W09 | 86.89% | 23,884 | -0.57% |
| 2026-W08 | 87.39% | 25,523 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 93.52% | 93.5% | +0.02% | 103,253 |  |
| US | 93.1% | 92.78% | +0.34% | 492,811 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Others | 28.57% | 60.0% | -52.38% | 7 |
| PaymentMethod | Paypal | 92.78% | 93.97% | -1.26% | 4,016 |
| PaymentMethod | Credit Card | 90.17% | 90.83% | -0.72% | 18,327 |
| PaymentMethod | Apple Pay | 87.98% | 88.39% | -0.46% | 3,828 |

---

*Report: 2026-04-14*
