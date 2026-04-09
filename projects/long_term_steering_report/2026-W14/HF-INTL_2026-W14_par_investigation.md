# PAR Investigation: HF-INTL 2026-W14

**Metric:** PAR  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 97.17% → 97.04% (-0.13%)  
**Volume:** 784,389 orders

## Executive Summary

**Overall:** PAR declined by 0.13 percentage points (97.17% → 97.04%) on a volume of 784,389 orders, representing the second consecutive week of decline after a four-week improvement trend.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Sustained decline pattern? | -0.13pp (2nd consecutive drop) | ⚠️ |
| L1: Country Breakdown | Countries exceeding ±2.5% threshold? | DK: -2.78pp, AT: -2.50pp, CH: +2.98pp | ⚠️ |
| L1: Payment Method | Significant degradation? | Apple Pay: -0.37pp (largest drop) | ✅ |
| L1: Payment Provider | Provider-level issues? | ProcessOut: -0.28pp (largest drop) | ✅ |

**Key Findings:**
- **Denmark (DK) is the primary driver** of the decline with a -2.78pp drop (94.03% from 96.72%) on 30,036 orders, flagged as exceeding the ±2.5% threshold
- **Austria (AT) also shows significant degradation** at -2.50pp (92.81% from 95.19%) on 12,458 orders
- **Volume decreased by 6.9%** week-over-week (784,389 vs 842,480), which may be contributing to rate volatility
- **Switzerland (CH) shows anomalous improvement** of +2.98pp but on very low volume (2,174 orders), warranting verification
- **ProcessOut shows the largest provider-level decline** at -0.28pp affecting 226,595 orders (29% of total volume)

**Action:** **Investigate** — The -2.78pp drop in Denmark exceeds the threshold and requires immediate root cause analysis. Cross-reference DK performance with ProcessOut data to determine if there is a correlation between the country decline and payment provider issues.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 97.04% | 784,389 | -0.13% ← REPORTED CHANGE |
| 2026-W13 | 97.17% | 842,480 | -0.08% |
| 2026-W12 | 97.25% | 877,187 | +0.04% |
| 2026-W11 | 97.21% | 897,106 | +0.52% |
| 2026-W10 | 96.71% | 916,831 | +0.51% |
| 2026-W09 | 96.22% | 896,537 | -0.12% |
| 2026-W08 | 96.34% | 884,970 | -0.22% |
| 2026-W07 | 96.55% | 920,370 | - |

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
| PaymentMethod | Apple Pay | 92.78% | 93.13% | -0.37% | 105,676 |
| PaymentMethod | Credit Card | 96.38% | 96.62% | -0.24% | 354,933 |
| PaymentMethod | Paypal | 98.92% | 98.97% | -0.05% | 193,296 |
| PaymentMethod | Others | 99.49% | 98.77% | +0.73% | 130,484 |
| PaymentProvider | ProcessOut | 95.51% | 95.77% | -0.28% | 226,595 |
| PaymentProvider | Braintree | 97.1% | 97.2% | -0.11% | 292,920 |
| PaymentProvider | Adyen | 98.36% | 98.44% | -0.08% | 258,061 |
| PaymentProvider | No Payment | 100.0% | 99.94% | +0.06% | 4,352 |
| PaymentProvider | Unknown | 87.57% | 85.21% | +2.76% | 2,461 |

---

*Report: 2026-04-09*
