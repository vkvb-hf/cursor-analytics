# AR Overall Investigation: HF-INTL 2026-W14

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 94.16% → 93.64% (-0.55%)  
**Volume:** 784,389 orders

## Executive Summary

**Overall:** AR Overall declined by -0.55% (from 94.16% to 93.64%) in W14, continuing a downward trend observed over the past 4 weeks, with volume decreasing to 784,389 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0 Trend | 4-week declining trend (W11-W14) | -1.26pp cumulative | ⚠️ |
| L1 Country | DK, AT, NO significant declines | -2.78pp, -2.50pp, -2.24pp | ⚠️ |
| L1 PaymentMethod | Apple Pay lowest performer | -0.85pp (87.52% rate) | ⚠️ |
| L1 PaymentProvider | ProcessOut underperforming | -0.83pp (91.13% rate) | ⚠️ |
| L1 Positive Signal | CH improved significantly | +2.98pp | ✅ |

**Key Findings:**
- DK experienced the largest country-level decline at -2.78pp (96.72% → 94.03%), exceeding the ±2.5% threshold and flagged for attention
- AT and NO also showed notable declines of -2.50pp and -2.24pp respectively, indicating potential regional issues in Nordic/Central European markets
- Apple Pay continues as the lowest-performing payment method at 87.52%, declining -0.85pp, while Credit Card also underperforms at 91.6%
- ProcessOut is the weakest payment provider at 91.13% (-0.83pp), trailing Braintree (94.19%) and Adyen (95.21%)
- Volume has declined consistently from 920,370 (W07) to 784,389 (W14), a 14.8% reduction over 8 weeks

**Action:** Investigate — Focus investigation on DK to identify root cause of -2.78pp decline, and examine ProcessOut + Apple Pay combination performance across affected countries.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 93.64% | 784,389 | -0.55% ← REPORTED CHANGE |
| 2026-W13 | 94.16% | 842,480 | -0.47% |
| 2026-W12 | 94.6% | 877,187 | -0.32% |
| 2026-W11 | 94.9% | 897,106 | +1.17% |
| 2026-W10 | 93.8% | 916,831 | +0.72% |
| 2026-W09 | 93.13% | 896,537 | -0.45% |
| 2026-W08 | 93.55% | 884,970 | -0.78% |
| 2026-W07 | 94.29% | 920,370 | - |

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
| PaymentMethod | Apple Pay | 87.52% | 88.27% | -0.85% | 105,676 |
| PaymentMethod | Credit Card | 91.6% | 92.31% | -0.77% | 354,933 |
| PaymentMethod | Paypal | 97.23% | 97.66% | -0.44% | 193,296 |
| PaymentMethod | Others | 98.85% | 97.61% | +1.27% | 130,484 |
| PaymentProvider | ProcessOut | 91.13% | 91.89% | -0.83% | 226,595 |
| PaymentProvider | Braintree | 94.19% | 94.69% | -0.53% | 292,920 |
| PaymentProvider | Adyen | 95.21% | 95.59% | -0.40% | 258,061 |
| PaymentProvider | No Payment | 100.0% | 99.94% | +0.06% | 4,352 |
| PaymentProvider | Unknown | 84.32% | 82.07% | +2.74% | 2,461 |

---

*Report: 2026-04-10*
