# PCAR Investigation: WL 2026-W15

**Metric:** PCAR  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 97.03% → 97.37% (+0.35%)  
**Volume:** 11,721 orders

## Executive Summary

**Overall:** PCAR improved by +0.35 percentage points (97.03% → 97.37%) in WL 2026-W15, returning to the same level observed in W10 (97.37%).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL Trend | 8-week stability check | +0.35pp vs W14 | ✅ |
| L1: Country | Any country Δ > ±2.5pp | None exceeding threshold | ✅ |
| L1: PaymentMethod | Dimension variance check | Max Δ +0.71pp (Apple Pay) | ✅ |

**Key Findings:**
- WL PCAR recovered to 97.37%, matching the W10 peak and reversing four weeks of slight decline (W10-W14)
- Volume decreased 27% over the 8-week period (16,585 → 11,721 orders), which may amplify rate fluctuations
- Apple Pay showed the strongest improvement among payment methods (+0.71pp to 97.34%), while PayPal remained stable at 98.12%
- All countries showed improvement: AO led with +2.17pp, followed by MR (+1.47pp), ER (+1.23pp), and GN (+1.07pp)
- No dimensions or countries breached the ±2.5pp threshold, indicating broad-based organic improvement

**Action:** Monitor — The improvement is positive and no anomalies were detected. Continue standard weekly monitoring to confirm the upward trend sustains.

---

---

## L0: 8-Week Trend (WL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 97.37% | 11,721 | +0.35% ← REPORTED CHANGE |
| 2026-W14 | 97.03% | 11,373 | -0.04% |
| 2026-W13 | 97.07% | 13,604 | +0.20% |
| 2026-W12 | 96.88% | 14,412 | -0.07% |
| 2026-W11 | 96.95% | 15,835 | -0.43% |
| 2026-W10 | 97.37% | 16,267 | +0.03% |
| 2026-W09 | 97.34% | 15,555 | +0.50% |
| 2026-W08 | 96.86% | 16,585 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| GN | 93.32% | 92.33% | +1.07% | 13,110 |  |
| ER | 90.33% | 89.22% | +1.23% | 68,811 |  |
| MR | 81.43% | 80.25% | +1.47% | 19,468 |  |
| AO | 87.06% | 85.21% | +2.17% | 13,883 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Unknown | nan% | nan% | +nan% | 0 |
| PaymentMethod | Paypal | 98.12% | 98.13% | -0.01% | 1,327 |
| PaymentMethod | Others | 100.0% | 100.0% | +0.00% | 1 |
| PaymentMethod | Credit Card | 97.24% | 97.0% | +0.24% | 6,522 |
| PaymentMethod | Apple Pay | 97.34% | 96.65% | +0.71% | 3,871 |

---

*Report: 2026-04-14*
