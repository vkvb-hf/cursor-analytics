# PCAR Investigation: HF-NA 2026-W14

**Metric:** PCAR  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 93.92% → 94.12% (+0.21%)  
**Volume:** 20,221 orders

## Executive Summary

**Overall:** PCAR improved from 93.92% to 94.12% (+0.20 pp) in W14, representing a modest recovery after the prior week's decline, with volume at 20,221 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Overall Rate Change | +0.20 pp improvement | +0.21% | ✅ |
| Country Deviation (>±2.5 pp) | No countries exceeded threshold | CA: -0.10 pp, US: -0.07 pp | ✅ |
| Payment Method Volatility | Others: +3.02 pp (low volume) | 121 orders | ⚠️ |
| Volume Trend | Declining volume vs W13 | -530 orders (-2.6%) | ⚠️ |
| 8-Week Trend Stability | Rate within normal range | 93.53% - 95.23% | ✅ |

**Key Findings:**
- The +0.20 pp improvement reverses the -0.29 pp decline from W13, bringing the rate close to W12 levels (94.19%)
- Both CA (93.52%, -0.10 pp) and US (92.79%, -0.07 pp) showed slight declines, indicating the overall improvement came from mix shift rather than country-level gains
- Apple Pay showed strong improvement (+1.13 pp to 94.48%) with meaningful volume (6,578 orders), while Credit Card declined (-0.41 pp to 93.75%)
- Order volume continues a downward trend (20,221 vs 26,944 in W07), representing a 25% decrease over the 8-week period
- The "Others" payment method showed +3.02 pp improvement but with only 121 orders, making it statistically insignificant

**Action:** Monitor - The improvement is positive but modest. Continue tracking Credit Card performance which declined despite being the highest-volume payment method (11,753 orders). No escalation required as no thresholds were breached.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 94.12% | 20,221 | +0.21% ← REPORTED CHANGE |
| 2026-W13 | 93.92% | 20,751 | -0.29% |
| 2026-W12 | 94.19% | 21,127 | +0.03% |
| 2026-W11 | 94.16% | 22,919 | -1.12% |
| 2026-W10 | 95.23% | 23,025 | +1.30% |
| 2026-W09 | 94.01% | 27,201 | +0.01% |
| 2026-W08 | 94.0% | 26,180 | +0.50% |
| 2026-W07 | 93.53% | 26,944 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| CA | 93.52% | 93.61% | -0.10% | 105,528 |  |
| US | 92.79% | 92.85% | -0.07% | 497,052 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Unknown | nan% | nan% | +nan% | 0 |
| PaymentMethod | Credit Card | 93.75% | 94.13% | -0.41% | 11,753 |
| PaymentMethod | Paypal | 94.97% | 94.18% | +0.84% | 1,769 |
| PaymentMethod | Apple Pay | 94.48% | 93.42% | +1.13% | 6,578 |
| PaymentMethod | Others | 99.17% | 96.27% | +3.02% | 121 |

---

*Report: 2026-04-10*
