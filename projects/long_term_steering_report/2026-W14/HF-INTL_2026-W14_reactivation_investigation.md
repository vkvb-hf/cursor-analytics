# Reactivation Investigation: HF-INTL 2026-W14

**Metric:** Reactivation  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 90.03% → 90.92% (+0.99%)  
**Volume:** 32,555 orders

## Executive Summary

**Overall:** Reactivation rate improved from 90.03% to 90.92% (+0.99pp) in W14, representing a positive weekly change on a volume of 32,555 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Rate within normal range (89.85%-90.92%) | +0.99pp | ✅ |
| L1: Country Breakdown | DK (-2.78pp), AT (-2.50pp) declined; CH (+2.98pp) improved | Mixed | ⚠️ |
| L1: Payment Method | Credit Card (+1.78pp), Apple Pay (+1.64pp) improved | Positive | ✅ |

**Key Findings:**
- Denmark (DK) showed the largest decline at -2.78pp (96.72% → 94.03%), exceeding the ±2.5% threshold, with significant volume of 30,036 orders
- Switzerland (CH) improved notably by +2.98pp (91.21% → 93.93%), though on low volume (2,174 orders)
- Credit Card payments improved by +1.78pp (84.64% → 86.15%) on 15,082 orders, contributing positively to the overall rate increase
- Volume decreased significantly from 43,179 (W13) to 32,555 (W14), a reduction of approximately 25%
- Austria (AT) declined by -2.50pp (95.19% → 92.81%), meeting the threshold for flagging

**Action:** Investigate – The overall improvement is positive, but the significant declines in DK (-2.78pp) and AT (-2.50pp) warrant further investigation to understand root causes, especially given DK's substantial order volume.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 90.92% | 32,555 | +0.99% ← REPORTED CHANGE |
| 2026-W13 | 90.03% | 43,179 | -0.19% |
| 2026-W12 | 90.2% | 42,003 | -0.20% |
| 2026-W11 | 90.38% | 45,133 | +0.33% |
| 2026-W10 | 90.08% | 48,534 | -0.90% |
| 2026-W09 | 90.9% | 55,010 | +0.04% |
| 2026-W08 | 90.86% | 54,907 | +1.12% |
| 2026-W07 | 89.85% | 44,800 | - |

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
| PaymentMethod | Others | 97.06% | 97.24% | -0.19% | 3,162 |
| PaymentMethod | Paypal | 96.61% | 96.21% | +0.42% | 8,886 |
| PaymentMethod | Apple Pay | 91.28% | 89.81% | +1.64% | 5,425 |
| PaymentMethod | Credit Card | 86.15% | 84.64% | +1.78% | 15,082 |

---

*Report: 2026-04-09*
