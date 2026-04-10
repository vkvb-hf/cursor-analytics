# AR Initial (LL0) Investigation: HF-INTL 2026-W12

**Metric:** AR Initial (LL0)  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 90.12% → 90.13% (+0.01%)  
**Volume:** 31,165 orders

## Executive Summary

## Executive Summary

**Overall:** AR Initial (LL0) for HF-INTL remained essentially flat at 90.13% in 2026-W12, with a minimal +0.01pp increase versus the prior week, on a volume of 31,165 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0 Trend | 8-week pattern | +0.01pp | ✅ |
| L1 Country | ES, SE, NO, AU, CH outside ±2.5% | -6.51pp to +4.80pp | ⚠️ |
| L1 PaymentMethod | All within threshold | -1.10pp to +0.36pp | ✅ |
| L1 PaymentProvider | No Payment flagged | -2.02pp | ⚠️ |

**Key Findings:**
- **ES experienced the largest decline** at -6.51pp (81.26% → 75.97%), though volume is relatively low at 491 orders
- **SE and NO also declined significantly** by -5.40pp and -3.50pp respectively, with SE contributing 2,048 orders and NO contributing 1,664 orders
- **AU showed notable improvement** at +2.92pp (65.72% → 67.64%) on substantial volume of 6,915 orders
- **GB remains stable** at -2.40pp with the highest volume (16,115 orders), staying within acceptable range
- **Consistent volume decline** observed over 8 weeks: from 52,771 (W07) to 31,165 (W14), representing a ~41% reduction

**Action:** **Investigate** — The significant declines in ES (-6.51pp), SE (-5.40pp), and NO (-3.50pp) warrant deeper L2 analysis to identify root causes, particularly in the Nordic region where a pattern may be emerging.

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
