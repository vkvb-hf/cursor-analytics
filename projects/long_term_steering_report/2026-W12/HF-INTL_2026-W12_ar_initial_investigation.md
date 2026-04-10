# AR Initial (LL0) Investigation: HF-INTL 2026-W12

**Metric:** AR Initial (LL0)  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 90.12% → 90.13% (+0.01%)  
**Volume:** 31,165 orders

## Executive Summary

## Executive Summary

**Overall:** AR Initial (LL0) for HF-INTL remained essentially stable in 2026-W12, showing a marginal improvement of +0.01pp (90.12% → 90.13%) on volume of 31,165 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0 Trend | 8-week stability | +0.01pp | ✅ |
| L1 Country | ES, SE, NO, AU, CH exceed ±2.5% | -6.51pp to +4.80pp | ⚠️ |
| L1 PaymentMethod | All within threshold | -1.10pp to +0.36pp | ✅ |
| L1 PaymentProvider | No Payment declined | -2.02pp | ⚠️ |

**Key Findings:**
- ES experienced the largest decline at -6.51pp (81.26% → 75.97%) on 491 orders, indicating potential localized issues
- SE and NO also showed significant declines of -5.40pp and -3.50pp respectively, suggesting a pattern across Nordic markets
- AU improved by +2.92pp (65.72% → 67.64%) on substantial volume of 6,915 orders, partially offsetting declines elsewhere
- GB, the highest volume country at 16,115 orders, declined -2.40pp but remained within threshold
- Overall L0 rate has dropped from 91.70% (W07) to 90.13% (W14), representing a -1.57pp decline over the 8-week period

**Action:** Investigate — Multiple countries (ES, SE, NO) showing coordinated declines warrant deeper L2 analysis to identify root cause, particularly focusing on any shared payment or operational factors across European markets.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 90.13% | 31,165 | +0.01% |
| 2026-W13 | 90.12% | 34,718 | -1.28% |
| 2026-W12 | 91.29% | 39,323 | -0.29% ← REPORTED CHANGE |
| 2026-W11 | 91.56% | 42,918 | +1.24% |
| 2026-W10 | 90.44% | 47,739 | +2.70% |
| 2026-W09 | 88.06% | 46,648 | -2.38% |
| 2026-W08 | 90.21% | 46,404 | -1.62% |
| 2026-W07 | 91.7% | 52,771 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| ES | 75.97% | 81.26% | -6.51% | 491 | ⚠️ |
| SE | 82.03% | 86.71% | -5.40% | 2,048 | ⚠️ |
| NO | 80.23% | 83.14% | -3.50% | 1,664 | ⚠️ |
| GB | 79.15% | 81.1% | -2.40% | 16,115 |  |
| AU | 67.64% | 65.72% | +2.92% | 6,915 | ⚠️ |
| CH | 87.5% | 83.49% | +4.80% | 192 | ⚠️ |

**Countries exceeding ±2.5% threshold:** ES, SE, NO, AU, CH

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Apple Pay | 87.78% | 88.76% | -1.10% | 11,761 |
| PaymentMethod | Others | 93.52% | 93.92% | -0.42% | 8,103 |
| PaymentMethod | Paypal | 96.85% | 96.59% | +0.27% | 7,204 |
| PaymentMethod | Credit Card | 89.92% | 89.6% | +0.36% | 12,255 |
| PaymentProvider | No Payment | 97.4% | 99.41% | -2.02% | 231 |
| PaymentProvider | Braintree | 92.53% | 93.01% | -0.52% | 17,471 |
| PaymentProvider | Unknown | 97.32% | 97.77% | -0.46% | 2,166 |
| PaymentProvider | ProcessOut | 87.89% | 87.85% | +0.05% | 16,207 |
| PaymentProvider | Adyen | 97.17% | 96.91% | +0.27% | 3,248 |

---

*Report: 2026-04-10*
