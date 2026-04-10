# PCAR Investigation: RTE 2026-W12

**Metric:** PCAR  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 96.89% → 96.9% (+0.01%)  
**Volume:** 39,914 orders

## Executive Summary

**Overall:** PCAR remained essentially stable at 96.9%, showing a marginal improvement of +0.01 pp from the prior week (96.89% → 96.9%) on a volume of 39,914 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Volatility within normal range | +0.01 pp | ✅ |
| L1: Country Breakdown | No country exceeds ±2.5% threshold | TK worst at -1.64 pp | ✅ |
| L1: Dimension Scan | Payment method variation detected | Others +5.28 pp, Paypal -0.52 pp | ⚠️ |

**Key Findings:**
- The +0.01 pp change is within normal fluctuation; the 8-week trend shows PCAR oscillating between 96.88% and 97.3%, indicating overall stability
- TK experienced the largest country-level decline at -1.64 pp (93.49% → 91.96%), though below the 2.5% escalation threshold
- "Others" payment method showed a significant +5.28 pp improvement (72.08% → 75.89%), but on low volume (1,157 orders)
- PayPal and Apple Pay both declined slightly (-0.52 pp and -0.51 pp respectively), though rates remain above 96%
- Volume continues a downward trend from W09 peak (50,858) to current week (39,914), representing a ~21% volume reduction over 5 weeks

**Action:** Monitor — No immediate investigation required. Continue tracking TK country performance and the declining volume trend over the next 2-3 weeks.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 96.9% | 39,914 | +0.01% |
| 2026-W13 | 96.89% | 42,897 | +0.01% |
| 2026-W12 | 96.88% | 44,209 | -0.11% ← REPORTED CHANGE |
| 2026-W11 | 96.99% | 47,403 | +0.10% |
| 2026-W10 | 96.89% | 48,399 | -0.42% |
| 2026-W09 | 97.3% | 50,858 | +0.37% |
| 2026-W08 | 96.94% | 49,908 | -0.02% |
| 2026-W07 | 96.96% | 49,262 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TK | 91.96% | 93.49% | -1.64% | 2,338 |  |
| TV | 93.47% | 94.31% | -0.89% | 2,205 |  |
| TO | 86.85% | 87.27% | -0.49% | 3,611 |  |
| FJ | 94.3% | 94.46% | -0.17% | 408,532 |  |
| CF | 93.62% | 93.52% | +0.10% | 53,267 |  |
| YE | 88.62% | 88.28% | +0.39% | 48,432 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Unknown | nan% | nan% | +nan% | 0 |
| PaymentMethod | Paypal | 97.78% | 98.29% | -0.52% | 5,079 |
| PaymentMethod | Apple Pay | 96.35% | 96.84% | -0.51% | 10,481 |
| PaymentMethod | Credit Card | 97.81% | 97.8% | +0.01% | 27,492 |
| PaymentMethod | Others | 75.89% | 72.08% | +5.28% | 1,157 |

---

*Report: 2026-04-10*
