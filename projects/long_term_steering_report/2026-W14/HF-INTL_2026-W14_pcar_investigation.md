# PCAR Investigation: HF-INTL 2026-W14

**Metric:** PCAR  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 95.21% → 96.0% (+0.83%)  
**Volume:** 31,465 orders

## Executive Summary

**Overall:** PCAR improved by +0.83pp (95.21% → 96.0%) in 2026-W14 on a volume of 31,465 orders, though this follows a -1.52pp decline in the prior week and represents the lowest volume in the 8-week trend period.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate recovering from W13 dip | +0.83pp | ✅ |
| L0: Volume Trend | Volume dropped significantly (31,465 vs 39,598) | -20.5% | ⚠️ |
| L1: Country Performance | DK and AT exceed -2.5% threshold | -2.78pp, -2.50pp | ⚠️ |
| L1: Country Outliers | CH improved significantly | +2.98pp | ✅ |
| L1: Payment Methods | All tracked methods stable or improving | +0.28pp to +0.86pp | ✅ |

**Key Findings:**
- DK showed the largest rate decline at -2.78pp (96.72% → 94.03%) on significant volume of 30,036 orders, warranting investigation
- Order volume has declined 35.6% over the 8-week period (48,803 in W07 → 31,465 in W14), with W14 representing the lowest volume observed
- AT and NO also showed notable declines of -2.50pp and -2.24pp respectively, suggesting a pattern in certain markets
- CH was the only country with significant improvement (+2.98pp), though on low volume (2,174 orders)
- Payment method "Others" continues to significantly underperform at 75.1% vs 97-98% for standard payment methods

**Action:** Investigate — Focus on DK to identify root cause of -2.78pp decline; also review AT and NO for potential regional issues. Monitor volume decline trend.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 96.0% | 31,465 | +0.83% ← REPORTED CHANGE |
| 2026-W13 | 95.21% | 39,598 | -1.52% |
| 2026-W12 | 96.68% | 38,136 | -0.53% |
| 2026-W11 | 97.2% | 42,932 | -0.11% |
| 2026-W10 | 97.31% | 44,946 | +0.80% |
| 2026-W09 | 96.54% | 48,662 | +0.04% |
| 2026-W08 | 96.5% | 49,249 | -0.49% |
| 2026-W07 | 96.98% | 48,803 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| DK | 94.03% | 96.72% | -2.78% | 30,036 | ⚠️ |
| AT | 92.81% | 95.19% | -2.50% | 12,458 |  |
| NO | 90.27% | 92.35% | -2.24% | 13,551 |  |
| BE | 94.01% | 95.31% | -1.37% | 74,093 |  |
| DE | 96.44% | 97.22% | -0.80% | 205,169 |  |
| FR | 92.95% | 93.7% | -0.80% | 158,170 |  |
| CH | 93.93% | 91.21% | +2.98% | 2,174 | ⚠️ |

**Countries exceeding ±2.5% threshold:** DK, CH

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Unknown | nan% | nan% | +nan% | 0 |
| PaymentMethod | Others | 75.1% | 74.88% | +0.28% | 2,859 |
| PaymentMethod | Credit Card | 98.2% | 97.89% | +0.31% | 12,194 |
| PaymentMethod | Paypal | 97.76% | 97.27% | +0.51% | 6,210 |
| PaymentMethod | Apple Pay | 98.16% | 97.32% | +0.86% | 10,202 |

---

*Report: 2026-04-10*
