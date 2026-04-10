# PCAR Investigation: RTE 2026-W12

**Metric:** PCAR  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 96.89% → 96.9% (+0.01%)  
**Volume:** 39,914 orders

## Executive Summary

**Overall:** PCAR improved marginally from 96.89% to 96.9% (+0.01 pp) on a volume of 39,914 orders in 2026-W12, continuing a stable trend within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate stable (96.88%-97.3% range) | +0.01 pp | ✅ |
| L1: Country Breakdown | No country exceeds ±2.5% threshold | Max: TK -1.64 pp | ✅ |
| L1: Dimension Scan | PaymentMethod "Others" shows volatility | +5.28 pp | ⚠️ |

**Key Findings:**
- TK showed the largest country decline at -1.64 pp (91.96% vs 93.49%) on 2,338 orders, though below the ±2.5% threshold
- TV declined -0.89 pp (93.47% vs 94.31%) on 2,205 orders, the second largest country movement
- PaymentMethod "Others" increased significantly by +5.28 pp (75.89% vs 72.08%) but represents low volume (1,157 orders)
- PayPal and Apple Pay both declined (-0.52 pp and -0.51 pp respectively), while Credit Card remained stable (+0.01 pp)
- Overall volume decreased from 42,897 to 39,914 orders (-6.9% WoW)

**Action:** Monitor — The +0.01 pp change is within normal fluctuation. Continue monitoring TK and TV country performance, and track PaymentMethod "Others" volatility given its low baseline rate (75.89%).

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
