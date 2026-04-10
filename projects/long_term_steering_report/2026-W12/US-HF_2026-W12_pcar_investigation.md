# PCAR Investigation: US-HF 2026-W12

**Metric:** PCAR  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 92.57% → 92.85% (+0.30%)  
**Volume:** 14,911 orders

## Executive Summary

**Overall:** PCAR improved from 92.57% to 92.85% (+0.28 pp) for US-HF in 2026-W12, representing a modest recovery after the prior week's decline, though still below the 8-week high of 94.58% observed in W10.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (92.45%-94.58%) | +0.28 pp | ✅ |
| L1: Country | US deviation vs prior | -0.17 pp | ✅ |
| L1: Payment - Credit Card | Primary method (59% vol) | -0.31 pp | ✅ |
| L1: Payment - Apple Pay | Secondary method (37% vol) | -0.26 pp | ✅ |
| L1: Payment - PayPal | Minor method (8% vol) | +1.81 pp | ✅ |
| L1: Payment - Others | Low volume (118 orders) | +4.36 pp | ⚠️ |

**Key Findings:**
- Overall PCAR recovered +0.28 pp week-over-week, partially offsetting the -0.38 pp decline from W13
- Volume declined 3% (14,911 vs 15,361 orders), continuing a downward trend from the W09 peak of 21,474 orders
- Credit Card and Apple Pay both showed slight declines (-0.31 pp and -0.26 pp respectively), which is notable as they represent ~96% of order volume
- PayPal showed strong improvement (+1.81 pp to 93.62%), outperforming Credit Card for the period
- "Others" payment method showed +4.36 pp improvement but with only 118 orders, making this statistically unreliable

**Action:** Monitor — The metric shows healthy recovery within normal operating range. No countries exceeded the ±2.5% threshold. Continue standard monitoring cadence with attention to the ongoing volume decline trend.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 92.85% | 14,911 | +0.30% |
| 2026-W13 | 92.57% | 15,361 | -0.38% |
| 2026-W12 | 92.92% | 15,651 | -0.09% ← REPORTED CHANGE |
| 2026-W11 | 93.0% | 16,952 | -1.67% |
| 2026-W10 | 94.58% | 17,681 | +1.54% |
| 2026-W09 | 93.15% | 21,474 | +0.13% |
| 2026-W08 | 93.03% | 20,421 | +0.63% |
| 2026-W07 | 92.45% | 20,573 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.8% | 92.95% | -0.17% | 517,442 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Unknown | nan% | nan% | +nan% | 0 |
| PaymentMethod | Credit Card | 93.51% | 93.8% | -0.31% | 8,810 |
| PaymentMethod | Apple Pay | 91.75% | 91.99% | -0.26% | 5,469 |
| PaymentMethod | Paypal | 93.62% | 91.96% | +1.81% | 1,254 |
| PaymentMethod | Others | 95.76% | 91.76% | +4.36% | 118 |

---

*Report: 2026-04-10*
