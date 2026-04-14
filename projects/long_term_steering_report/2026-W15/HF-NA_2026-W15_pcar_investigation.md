# PCAR Investigation: HF-NA 2026-W15

**Metric:** PCAR  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 94.12% → 94.08% (-0.04%)  
**Volume:** 23,512 orders

## Executive Summary

**Overall:** PCAR declined marginally from 94.12% to 94.08% (-0.04pp) in W15, representing a minor fluctuation within normal operating range on volume of 23,512 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Regional Trend | W15 vs W14 | -0.04pp | ✅ |
| L1: Country Breakdown | No country ±2.5% | None flagged | ✅ |
| L1: Payment Method | "Others" declined | -2.49pp | ⚠️ |
| L1: Payment Method | Apple Pay declined | -1.08pp | ✅ |

**Key Findings:**
- The -0.04pp decline is well within the 8-week fluctuation range (93.92% to 95.23%), indicating normal variance
- Volume increased by 16.3% WoW (20,221 → 23,512 orders), which may contribute to rate normalization
- "Others" payment method showed the largest decline (-2.49pp), but with only 91 orders, impact is negligible
- Apple Pay declined by -1.08pp on 7,678 orders, representing the most meaningful segment movement
- Both US (+0.34pp) and CA (+0.02pp) showed slight improvements at the country level, suggesting no systemic geographic issues

**Action:** Monitor – The decline is minimal and within normal variance. No escalation required. Continue standard monitoring with attention to Apple Pay performance in W16.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 94.08% | 23,512 | -0.04% ← REPORTED CHANGE |
| 2026-W14 | 94.12% | 20,221 | +0.21% |
| 2026-W13 | 93.92% | 20,751 | -0.29% |
| 2026-W12 | 94.19% | 21,127 | +0.03% |
| 2026-W11 | 94.16% | 22,919 | -1.12% |
| 2026-W10 | 95.23% | 23,025 | +1.30% |
| 2026-W09 | 94.01% | 27,201 | +0.01% |
| 2026-W08 | 94.0% | 26,180 | - |

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
| PaymentMethod | Unknown | nan% | nan% | +nan% | 0 |
| PaymentMethod | Others | 96.7% | 99.17% | -2.49% | 91 |
| PaymentMethod | Apple Pay | 93.46% | 94.48% | -1.08% | 7,678 |
| PaymentMethod | Paypal | 95.42% | 94.97% | +0.48% | 1,967 |
| PaymentMethod | Credit Card | 94.21% | 93.75% | +0.50% | 13,776 |

---

*Report: 2026-04-14*
