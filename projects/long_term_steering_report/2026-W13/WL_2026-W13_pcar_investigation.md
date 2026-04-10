# PCAR Investigation: WL 2026-W13

**Metric:** PCAR  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 97.07% → 97.03% (-0.04%)  
**Volume:** 11,373 orders

## Executive Summary

**Overall:** PCAR declined slightly from 97.07% to 97.03% (-0.04 pp) in 2026-W13, representing a minor week-over-week decrease on a volume of 11,373 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Volatility within normal range | -0.04 pp | ✅ |
| L1: Country Breakdown | No country exceeds ±2.5% threshold | Max: +0.88 pp (CK) | ✅ |
| L1: Payment Method | Credit Card slight decline | -0.13 pp | ✅ |
| L1: Payment Method | Apple Pay & Paypal improved | +0.58 pp / +0.68 pp | ✅ |

**Key Findings:**
- The -0.04 pp decline is minimal and falls well within normal weekly fluctuation; the 8-week trend shows overall improvement from 94.85% (W07) to 97.03% (W14)
- No countries exceeded the ±2.5% threshold; KN showed the largest decline at -0.17 pp while CK improved by +0.88 pp
- Credit Card payments (67% of volume) saw a slight rate decline of -0.13 pp (96.91%), partially offset by improvements in Apple Pay (+0.58 pp) and Paypal (+0.68 pp)
- Volume decreased from 13,604 to 11,373 orders (-16.4%), which may amplify rate volatility
- ER represents the highest volume country (73,655) and showed improvement of +0.43 pp

**Action:** Monitor — The decline is negligible (-0.04 pp), no dimensional breakdowns exceed alert thresholds, and the metric remains stable within a healthy 97%+ range. Continue standard monitoring.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 97.03% | 11,373 | -0.04% |
| 2026-W13 | 97.07% | 13,604 | +0.20% ← REPORTED CHANGE |
| 2026-W12 | 96.88% | 14,412 | -0.07% |
| 2026-W11 | 96.95% | 15,835 | -0.43% |
| 2026-W10 | 97.37% | 16,267 | +0.03% |
| 2026-W09 | 97.34% | 15,555 | +0.50% |
| 2026-W08 | 96.86% | 16,585 | +2.12% |
| 2026-W07 | 94.85% | 16,452 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| KN | 87.61% | 87.76% | -0.17% | 10,365 |  |
| CG | 96.76% | 96.84% | -0.08% | 44,477 |  |
| ER | 89.92% | 89.54% | +0.43% | 73,655 |  |
| AO | 87.96% | 87.38% | +0.66% | 16,249 |  |
| CK | 94.15% | 93.33% | +0.88% | 42,197 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Unknown | nan% | nan% | +nan% | 0 |
| PaymentMethod | Others | 100.0% | nan% | +nan% | 1 |
| PaymentMethod | Credit Card | 96.91% | 97.04% | -0.13% | 7,642 |
| PaymentMethod | Apple Pay | 97.0% | 96.44% | +0.58% | 4,237 |
| PaymentMethod | Paypal | 97.97% | 97.31% | +0.68% | 1,724 |

---

*Report: 2026-04-10*
