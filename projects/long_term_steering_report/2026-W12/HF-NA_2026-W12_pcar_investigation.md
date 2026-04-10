# PCAR Investigation: HF-NA 2026-W12

**Metric:** PCAR  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 93.92% → 94.12% (+0.21%)  
**Volume:** 20,221 orders

## Executive Summary

**Overall:** PCAR improved slightly from 93.92% to 94.12% (+0.20 pp) week-over-week, with volume of 20,221 orders in W12.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Trend | PCAR within normal range | +0.21% | ✅ |
| L1: Country Impact | No country exceeds ±2.5% threshold | US: -0.17%, CA: -0.01% | ✅ |
| L1: Dimension Scan | PaymentMethod variance detected | Others: +4.36% | ⚠️ |

**Key Findings:**
- PCAR has recovered from the W13 dip (93.92%) and is now trending back toward the 8-week high of 95.23% seen in W10
- Both US (-0.17 pp) and CA (-0.01 pp) showed minor declines but remained within acceptable thresholds
- PaymentMethod "Others" showed a +4.36 pp improvement (91.76% → 95.76%), though volume is minimal at 118 orders
- PayPal showed notable improvement of +1.34 pp (92.92% → 94.17%) on 1,783 orders
- Order volume continues a downward trend (from 27,201 in W09 to 20,221 in W12), representing a ~26% volume decline over 5 weeks

**Action:** Monitor – The metric is stable and improving slightly. No immediate investigation required, but continue tracking the volume decline trend.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 94.12% | 20,221 | +0.21% |
| 2026-W13 | 93.92% | 20,751 | -0.29% |
| 2026-W12 | 94.19% | 21,127 | +0.03% ← REPORTED CHANGE |
| 2026-W11 | 94.16% | 22,919 | -1.12% |
| 2026-W10 | 95.23% | 23,025 | +1.30% |
| 2026-W09 | 94.01% | 27,201 | +0.01% |
| 2026-W08 | 94.0% | 26,180 | +0.50% |
| 2026-W07 | 93.53% | 26,944 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| US | 92.8% | 92.95% | -0.17% | 517,442 |  |
| CA | 93.36% | 93.37% | -0.01% | 106,081 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Unknown | nan% | nan% | +nan% | 0 |
| PaymentMethod | Apple Pay | 93.06% | 93.18% | -0.13% | 6,799 |
| PaymentMethod | Credit Card | 94.79% | 94.88% | -0.10% | 12,427 |
| PaymentMethod | Paypal | 94.17% | 92.92% | +1.34% | 1,783 |
| PaymentMethod | Others | 95.76% | 91.76% | +4.36% | 118 |

---

*Report: 2026-04-10*
