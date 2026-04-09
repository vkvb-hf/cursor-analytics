# AR Initial (LL0) Investigation: HF-INTL 2026-W14

**Metric:** AR Initial (LL0)  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 90.12% → 90.13% (+0.01%)  
**Volume:** 31,165 orders

## Executive Summary

## Executive Summary

**Overall:** AR Initial (LL0) for HF-INTL remained essentially flat week-over-week, increasing marginally from 90.12% to 90.13% (+0.01 pp) on a volume of 31,165 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall Rate | 90.12% → 90.13% | +0.01 pp | ✅ |
| L1: Country Breakdown | 6 countries exceed ±2.5% threshold | Mixed | ⚠️ |
| L1: Payment Method | Credit Card -1.79 pp, Others +4.05 pp | Mixed | ✅ |
| L1: Payment Provider | All providers within ±2.5% | Stable | ✅ |

**Key Findings:**
- **Volume decline continues:** Order volume dropped from 34,718 to 31,165 (-10.2% WoW), continuing a downward trend from 52,771 orders in W07—a 41% reduction over 8 weeks
- **Significant country-level volatility masked at aggregate:** LU (-8.41 pp), DK (-7.22 pp), AT (-7.04 pp), and DE (-4.41 pp) all declined materially, offset by CH (+11.33 pp) and GB (+2.37 pp)
- **Germany impact is notable:** DE represents 8,587 orders (27.5% of volume) and declined -4.41 pp from 85.34% to 81.58%
- **Australia remains persistently low:** AU at 64.13% is significantly below the overall benchmark, with 6,365 orders (20.4% of volume)
- **8-week trend shows recovery:** Current rate of 90.13% has stabilized after W09's dip to 88.06%, though still below W07's peak of 91.7%

**Action:** **Investigate** — While the overall metric appears stable, the country-level analysis reveals significant underlying volatility. Prioritize investigation into DE and AU performance drivers, as these two markets represent nearly 48% of total volume and are underperforming.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W14 | 90.13% | 31,165 | +0.01% ← REPORTED CHANGE |
| 2026-W13 | 90.12% | 34,718 | -1.28% |
| 2026-W12 | 91.29% | 39,323 | -0.29% |
| 2026-W11 | 91.56% | 42,918 | +1.24% |
| 2026-W10 | 90.44% | 47,739 | +2.70% |
| 2026-W09 | 88.06% | 46,648 | -2.38% |
| 2026-W08 | 90.21% | 46,404 | -1.62% |
| 2026-W07 | 91.7% | 52,771 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|
| LU | 79.38% | 86.67% | -8.41% | 97 | ⚠️ |
| DK | 82.39% | 88.8% | -7.22% | 1,153 | ⚠️ |
| AT | 80.4% | 86.49% | -7.04% | 699 | ⚠️ |
| DE | 81.58% | 85.34% | -4.41% | 8,587 | ⚠️ |
| AU | 64.13% | 66.91% | -4.14% | 6,365 | ⚠️ |
| FR | 84.43% | 85.35% | -1.08% | 11,444 |  |
| GB | 80.08% | 78.23% | +2.37% | 14,083 |  |
| CH | 86.03% | 77.27% | +11.33% | 229 | ⚠️ |

**Countries exceeding ±2.5% threshold:** LU, DK, AT, DE, AU, CH

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|
| PaymentMethod | Credit Card | 87.07% | 88.66% | -1.79% | 11,431 |
| PaymentMethod | Apple Pay | 86.33% | 86.1% | +0.27% | 9,417 |
| PaymentMethod | Paypal | 95.94% | 94.95% | +1.04% | 5,118 |
| PaymentMethod | Others | 98.04% | 94.22% | +4.05% | 5,199 |
| PaymentProvider | ProcessOut | 85.91% | 86.51% | -0.69% | 12,528 |
| PaymentProvider | Adyen | 97.08% | 97.49% | -0.42% | 3,395 |
| PaymentProvider | Braintree | 91.09% | 90.91% | +0.20% | 13,267 |
| PaymentProvider | Unknown | 98.49% | 96.51% | +2.05% | 1,917 |
| PaymentProvider | No Payment | 100.0% | 97.76% | +2.29% | 58 |

---

*Report: 2026-04-09*
