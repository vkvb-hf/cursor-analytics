# AR Overall Investigation: US-HF 2026-W14

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 91.98% → 91.93% (-0.05%)  
**Volume:** 415,885 orders

## Executive Summary

**Overall:** AR Overall declined marginally by -0.05 percentage points (91.98% → 91.93%) on volume of 415,885 orders, representing a minor fluctuation within the normal operating range observed over the 8-week period.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Volatility within ±0.34pp range | -0.05pp | ✅ |
| L1: Country Breakdown | US only, no country >±2.5% threshold | -0.06pp | ✅ |
| L1: PaymentMethod | Others showed largest decline | -0.29pp | ✅ |
| L1: PaymentProvider | Unknown showed unusual swing | +8.23pp | ⚠️ |

**Key Findings:**
- The -0.05pp decline is within normal weekly volatility (8-week range: 91.48% to 92.09%), and reverses the +0.05pp gain from the prior week
- No country-level anomalies detected; US is the sole country and declined by -0.06pp
- PaymentMethod "Others" showed the largest decline (-0.29pp) but represents minimal volume (2,202 orders)
- PaymentProvider "Unknown" showed a +8.23pp improvement, but volume is negligible (249 orders) making this statistically insignificant
- Primary payment flows (Braintree at 372,325 orders, Credit Card at 305,088 orders) showed stable performance with only -0.05pp and -0.06pp changes respectively

**Action:** **Monitor** – The decline is minimal, within historical volatility, and no significant dimensional drivers were identified. Continue standard monitoring; no immediate investigation required.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 91.93% | 415,885 | -0.05% ← REPORTED CHANGE |
| 2026-W13 | 91.98% | 424,103 | +0.05% |
| 2026-W12 | 91.93% | 433,761 | -0.17% |
| 2026-W11 | 92.09% | 444,619 | +0.14% |
| 2026-W10 | 91.96% | 457,610 | +0.34% |
| 2026-W09 | 91.65% | 455,121 | +0.19% |
| 2026-W08 | 91.48% | 453,781 | -0.20% |
| 2026-W07 | 91.66% | 470,140 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.79% | 92.85% | -0.06% | 497,052 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Others | 98.37% | 98.65% | -0.29% | 2,202 |
| PaymentMethod | Paypal | 95.34% | 95.44% | -0.11% | 51,200 |
| PaymentMethod | Credit Card | 92.7% | 92.76% | -0.06% | 305,088 |
| PaymentMethod | Apple Pay | 84.57% | 84.44% | +0.15% | 57,395 |
| PaymentProvider | Braintree | 92.44% | 92.49% | -0.05% | 372,325 |
| PaymentProvider | No Payment | 100.0% | 100.0% | +0.00% | 1,924 |
| PaymentProvider | Adyen | 95.05% | 94.99% | +0.07% | 364 |
| PaymentProvider | ProcessOut | 86.9% | 86.57% | +0.38% | 41,023 |
| PaymentProvider | Unknown | 86.75% | 80.15% | +8.23% | 249 |

---

*Report: 2026-04-09*
