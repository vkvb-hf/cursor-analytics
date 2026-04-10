# PAR Investigation: US-HF 2026-W14

**Metric:** PAR  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 93.59% → 93.63% (+0.04%)  
**Volume:** 415,885 orders

## Executive Summary

**Overall:** PAR improved marginally from 93.59% to 93.63% (+0.04 pp) on a volume of 415,885 orders, continuing a stable upward trend observed since W09.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Sustained improvement since W09 | +0.04 pp | ✅ |
| L1: Country Breakdown | US declined slightly | -0.07 pp | ⚠️ |
| L1: Payment Method | All methods stable; Apple Pay improved | +0.39 pp (Apple Pay) | ✅ |
| L1: Payment Provider | All major providers stable or improved | +0.09 pp (Braintree) | ✅ |

**Key Findings:**
- The +0.04 pp weekly improvement aligns with prior week's trajectory, indicating consistent performance rather than a one-time spike
- US showed a slight decline of -0.07 pp (92.85% → 92.79%), though no countries exceeded the ±2.5% threshold
- Apple Pay improved by +0.39 pp (87.04% → 87.38%) but remains the lowest-performing payment method at 87.38%
- Braintree, handling 372,325 orders (89.5% of volume), improved +0.09 pp to 94.10%
- "Unknown" PaymentProvider showed +8.88 pp improvement, but volume is negligible (249 orders)

**Action:** Monitor — The metric shows healthy stability with no significant degradation signals. Continue standard weekly monitoring.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 93.63% | 415,885 | +0.04% ← REPORTED CHANGE |
| 2026-W13 | 93.59% | 424,103 | +0.04% |
| 2026-W12 | 93.55% | 433,761 | -0.04% |
| 2026-W11 | 93.59% | 444,619 | +0.22% |
| 2026-W10 | 93.38% | 457,610 | +0.24% |
| 2026-W09 | 93.16% | 455,121 | +0.03% |
| 2026-W08 | 93.13% | 453,781 | -0.27% |
| 2026-W07 | 93.38% | 470,140 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.79% | 92.85% | -0.07% | 497,052 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Paypal | 96.05% | 96.06% | -0.01% | 51,200 |
| PaymentMethod | Credit Card | 94.36% | 94.35% | +0.01% | 305,088 |
| PaymentMethod | Others | 99.36% | 99.19% | +0.17% | 2,202 |
| PaymentMethod | Apple Pay | 87.38% | 87.04% | +0.39% | 57,395 |
| PaymentProvider | No Payment | 100.0% | 100.0% | +0.00% | 1,924 |
| PaymentProvider | ProcessOut | 89.01% | 88.93% | +0.08% | 41,023 |
| PaymentProvider | Braintree | 94.1% | 94.02% | +0.09% | 372,325 |
| PaymentProvider | Adyen | 96.43% | 95.74% | +0.72% | 364 |
| PaymentProvider | Unknown | 95.58% | 87.79% | +8.88% | 249 |

---

*Report: 2026-04-10*
