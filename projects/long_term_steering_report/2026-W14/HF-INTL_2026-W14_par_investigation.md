# PAR Investigation: HF-INTL 2026-W14

**Metric:** PAR  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 97.17% → 97.04% (-0.13%)  
**Volume:** 784,389 orders

## Executive Summary

## Executive Summary

**Overall:** PAR declined by -0.13pp (97.17% → 97.04%) on volume of 784,389 orders, continuing a two-week downward trend after peaking at 97.25% in W12.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Sustained decline? | -0.13pp (2nd consecutive week) | ⚠️ |
| L1: Country | Any >±2.5pp? | DK: -2.78pp, CH: +2.98pp | ⚠️ |
| L1: Payment Method | Any >±1.0pp? | Max: Apple Pay -0.37pp | ✅ |
| L1: Payment Provider | Any >±1.0pp? | Unknown: +2.76pp (low vol) | ✅ |

**Key Findings:**
- DK experienced the largest decline at -2.78pp (96.72% → 94.03%) on 30,036 orders, flagged as primary driver
- AT dropped -2.50pp (95.19% → 92.81%) and NO dropped -2.24pp (92.35% → 90.27%), indicating broader Nordic/DACH regional softness
- Volume declined -6.9% WoW (842,480 → 784,389), marking the 4th consecutive week of volume contraction
- CH showed anomalous improvement of +2.98pp but on minimal volume (2,174 orders)
- Payment dimensions remain stable with no method or provider exceeding ±1.0pp threshold on meaningful volume

**Action:** **Investigate** — Focus on DK to identify root cause of -2.78pp drop; secondary review of AT and NO for potential shared regional factors.

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

*Report: 2026-04-10*
