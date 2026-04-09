# PCAR Investigation: HF-INTL 2026-W14

**Metric:** PCAR  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 95.21% → 96.0% (+0.83%)  
**Volume:** 31,465 orders

## Executive Summary

**Overall:** PCAR improved from 95.21% to 96.0% (+0.83pp) in 2026-W14 on volume of 31,465 orders, partially recovering from the -1.52pp decline observed in W13.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Metric within normal range | +0.83pp vs prior week | ✅ |
| L1: Country Breakdown | 2 countries exceed ±2.5% threshold | DK -2.78pp, CH +2.98pp | ⚠️ |
| L1: Payment Method | All methods stable or improving | Range: +0.28pp to +0.86pp | ✅ |
| Volume Trend | Declining volume pattern | 31,465 (lowest in 8 weeks) | ⚠️ |

**Key Findings:**
- Denmark (DK) shows the largest decline at -2.78pp (96.72% → 94.03%) with significant volume of 30,036 orders, flagged for investigation
- Switzerland (CH) improved notably by +2.98pp (91.21% → 93.93%), though on low volume of 2,174 orders
- Volume has decreased significantly from 48,803 in W07 to 31,465 in W14, a ~35% reduction over 8 weeks
- Apple Pay showed the strongest payment method improvement at +0.86pp (97.32% → 98.16%) on 10,202 orders
- "Others" payment method remains a concern with the lowest rate at 75.1%, though stable vs prior week

**Action:** **Investigate** – While the overall metric improved, the Denmark decline (-2.78pp on 30,036 orders) requires root cause analysis, and the persistent volume decline trend warrants attention.

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

*Report: 2026-04-09*
