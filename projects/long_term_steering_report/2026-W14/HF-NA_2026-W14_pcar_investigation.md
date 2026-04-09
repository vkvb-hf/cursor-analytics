# PCAR Investigation: HF-NA 2026-W14

**Metric:** PCAR  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 93.92% → 94.12% (+0.21%)  
**Volume:** 20,221 orders

## Executive Summary

**Overall:** PCAR improved by +0.21 percentage points (93.92% → 94.12%) on volume of 20,221 orders in W14, representing a recovery from the prior week's decline and bringing performance back in line with the 8-week average.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | Week-over-week change | +0.21 pp | ✅ |
| L1: Country Impact | Any country ±2.5% threshold | None flagged | ✅ |
| L1: Payment Method | Dimension variance check | +3.02 pp (Others) | ⚠️ |

**Key Findings:**
- The +0.21 pp improvement reverses the -0.29 pp decline from W13, stabilizing PCAR near the 94% benchmark
- No countries exceeded the ±2.5% threshold; both US (-0.07 pp) and CA (-0.10 pp) showed minimal, slightly negative movement
- "Others" payment method showed a significant +3.02 pp increase (96.27% → 99.17%), though on low volume (121 orders)
- Apple Pay improved notably by +1.13 pp (93.42% → 94.48%) on meaningful volume (6,578 orders)
- Credit Card declined by -0.41 pp (94.13% → 93.75%), which is notable given it represents the largest payment volume (11,753 orders)
- Overall order volume continues to decline (20,221 vs. 20,751 prior week), down significantly from W09 peak of 27,201

**Action:** Monitor — The improvement is positive but modest. Continue monitoring Credit Card performance given its volume significance and slight decline trend.

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

*Report: 2026-04-09*
