# AR Overall Investigation: HF-INTL 2026-W14

**Metric:** AR Overall  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 94.16% → 93.64% (-0.55%)  
**Volume:** 784,389 orders

## Executive Summary

**Overall:** AR Overall declined from 94.16% to 93.64% (-0.55pp) in W14, continuing a 4-week downward trend from the W11 peak of 94.9%.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0 Trend | 4 consecutive weeks of decline (W11→W14) | -1.26pp cumulative | ⚠️ |
| L1 Country | DK (-2.78pp), AT (-2.51pp) exceed threshold | -2.78pp max | ⚠️ |
| L1 PaymentMethod | Apple Pay lowest at 87.52% | -0.85pp | ✅ |
| L1 PaymentProvider | ProcessOut lowest at 91.13% | -0.83pp | ✅ |

**Key Findings:**
- **Denmark (DK)** showed the largest country-level decline at -2.78pp (96.72% → 94.03%) with 30,036 orders, significantly exceeding the ±2.5% threshold
- **Austria (AT)** also exceeded threshold with -2.51pp decline (95.19% → 92.8%) on 12,458 orders
- **Sustained downward trend:** AR Overall has declined for 4 consecutive weeks, dropping 1.26pp from the W11 peak (94.9% → 93.64%)
- **Volume decline:** Order volume decreased 6.9% WoW (842,480 → 784,389), continuing a 4-week volume contraction from W10's 916,831
- **Switzerland (CH)** was the only country showing significant improvement at +2.98pp (91.21% → 93.93%), though on low volume (2,174 orders)

**Action:** **Investigate** – Prioritize root cause analysis for Denmark and Austria, which together account for 42,494 orders and showed declines exceeding the 2.5pp threshold. The sustained 4-week declining trend warrants deeper examination of country-specific factors.

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
| AT | 92.8% | 95.19% | -2.51% | 12,458 | ⚠️ |
| NO | 90.27% | 92.35% | -2.24% | 13,551 |  |
| BE | 94.01% | 95.32% | -1.38% | 74,093 |  |
| DE | 96.44% | 97.22% | -0.80% | 205,169 |  |
| FR | 92.95% | 93.7% | -0.80% | 158,169 |  |
| CH | 93.93% | 91.21% | +2.98% | 2,174 | ⚠️ |

**Countries exceeding ±2.5% threshold:** DK, AT, CH

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

*Report: 2026-04-09*
