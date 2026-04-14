# PCAR Investigation: RTE 2026-W15

**Metric:** PCAR  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 96.9% → 97.22% (+0.33%)  
**Volume:** 44,168 orders

## Executive Summary

**Overall:** PCAR improved by +0.33 percentage points (96.9% → 97.22%) in W15, reaching the highest level in the 8-week trend period with 44,168 orders processed.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Sustained improvement after W10-W14 plateau | +0.33 pp | ✅ |
| L1: Country Breakdown | 1 country (TK) exceeds ±2.5% threshold | +7.54 pp (TK) | ⚠️ |
| L1: Payment Method | "Others" payment method declined significantly | -4.35 pp | ⚠️ |

**Key Findings:**
- TK showed exceptional improvement of +7.54 pp (88.65% → 95.33%), flagged for exceeding the ±2.5% threshold; low volume (1,950 orders) suggests potential data volatility or process change
- TV and YE experienced declines of -1.37 pp and -0.43 pp respectively, though neither exceeded the alert threshold
- "Others" payment method declined sharply by -4.35 pp (74.83% → 71.58%) but represents minimal volume (950 orders)
- Core payment methods (Credit Card, PayPal, Apple Pay) all improved, with PayPal leading at 98.58% (+0.45 pp)
- Overall volume increased by 10.7% (39,914 → 44,168 orders) week-over-week

**Action:** Monitor – The overall metric improvement is positive and driven by broad gains across major payment methods. Investigate TK's significant swing to determine if this reflects a sustainable process improvement or data anomaly.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 97.22% | 44,168 | +0.33% ← REPORTED CHANGE |
| 2026-W14 | 96.9% | 39,914 | +0.01% |
| 2026-W13 | 96.89% | 42,897 | +0.01% |
| 2026-W12 | 96.88% | 44,209 | -0.11% |
| 2026-W11 | 96.99% | 47,403 | +0.10% |
| 2026-W10 | 96.89% | 48,399 | -0.42% |
| 2026-W09 | 97.3% | 50,858 | +0.37% |
| 2026-W08 | 96.94% | 49,908 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| TV | 92.14% | 93.41% | -1.37% | 1,895 |  |
| YE | 87.77% | 88.15% | -0.43% | 42,126 |  |
| FJ | 93.97% | 93.62% | +0.38% | 388,956 |  |
| CF | 94.14% | 93.47% | +0.72% | 51,881 |  |
| TZ | 91.69% | 90.11% | +1.76% | 2,660 |  |
| TO | 86.67% | 84.89% | +2.11% | 3,204 |  |
| TK | 95.33% | 88.65% | +7.54% | 1,950 | ⚠️ |

**Countries exceeding ±2.5% threshold:** TK

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Unknown | nan% | nan% | +nan% | 0 |
| PaymentMethod | Others | 71.58% | 74.83% | -4.35% | 950 |
| PaymentMethod | Credit Card | 97.86% | 97.58% | +0.29% | 27,463 |
| PaymentMethod | Paypal | 98.58% | 98.14% | +0.45% | 5,081 |
| PaymentMethod | Apple Pay | 97.21% | 96.65% | +0.58% | 10,674 |

---

*Report: 2026-04-14*
