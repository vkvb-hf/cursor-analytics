# PCAR Investigation: US-HF 2026-W12

**Metric:** PCAR  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 92.57% → 92.85% (+0.30%)  
**Volume:** 14,911 orders

## Executive Summary

**Overall:** PCAR improved from 92.57% to 92.85% (+0.30 pp) week-over-week for US-HF, with order volume of 14,911 in 2026-W12.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (92.45%-94.58%) | +0.30 pp | ✅ |
| L1: Country Breakdown | US country rate change | -0.17 pp | ✅ |
| L1: Payment Method - Credit Card | Primary payment method | -0.31 pp | ✅ |
| L1: Payment Method - Apple Pay | Secondary payment method | -0.26 pp | ✅ |
| L1: Payment Method - PayPal | Minor payment method | +1.81 pp | ✅ |
| L1: Payment Method - Others | Low volume segment | +4.36 pp | ⚠️ |

**Key Findings:**
- Overall PCAR shows modest recovery (+0.30 pp) after declining -0.38 pp the prior week, indicating stabilization
- Volume has steadily decreased from ~21K orders (W08-W09) to ~15K orders (W12-W14), representing a ~29% volume reduction over 6 weeks
- "Others" payment method showed a +4.36 pp improvement but with very low volume (118 orders), making this statistically unreliable
- Credit Card (8,810 orders) and Apple Pay (5,469 orders) both showed minor declines (-0.31 pp and -0.26 pp respectively)
- No countries exceeded the ±2.5% threshold, indicating no regional anomalies requiring investigation

**Action:** Monitor — The +0.30 pp improvement returns PCAR to the mid-range of the 8-week trend. Continue monitoring volume decline trends and ensure the rate stabilization holds through W15.

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
