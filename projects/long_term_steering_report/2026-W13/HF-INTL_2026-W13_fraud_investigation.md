# Fraud Investigation: HF-INTL 2026-W13

**Metric:** Fraud Approval Rate  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 91.79% → 91.70% (-0.10%)  
**Volume:** 37,558 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) for HF-INTL declined marginally from 91.79% to 91.70% (-0.10pp) in 2026-W13, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall FAR | -0.10pp WoW | Within normal range | ✅ |
| L0: Duplicate Rate | +0.30pp (30.52% → 30.22%) | Slight decrease | ✅ |
| L0: Duplicate Block Rate | +0.81pp (6.61% → 7.42%) | Minor increase | ✅ |
| L1: Country Variance | 4 countries exceed ±2.5% threshold | NL, NZ, DK, LU flagged | ⚠️ |
| L1: Channel Category | Paid -0.39pp, Referral -0.88pp | Within normal range | ✅ |

**Key Findings:**
- **New Zealand (NZ)** experienced the largest FAR decline at -5.50pp (90.59% → 85.61%) with volume of 813 customers and a +7.60% increase in duplicate rate
- **Luxembourg (LU)** showed a -5.67pp FAR decline (98.61% → 93.02%), though on very low volume (86 customers)
- **Netherlands (NL)** declined -2.83pp in FAR (94.24% → 91.58%) accompanied by a significant +14.79% increase in duplicate rate
- **Denmark (DK)** improved +3.31pp in FAR (85.78% → 88.62%) with a -10.17% decrease in duplicate rate
- Overall volume decreased significantly from 46,689 to 37,558 customers (-19.6% WoW)

**Action:** Monitor — The overall decline is not significant and within normal weekly fluctuation. Continue monitoring NZ and NL for sustained declines, particularly the correlation between rising duplicate rates and falling FAR in these markets.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W14 | 91.70% | 30.22% | 7.42% | 0.25% | 37,558 | -0.10% |
| 2026-W13 | 91.79% | 30.52% | 6.61% | 0.27% | 46,689 | -0.17% ← REPORTED CHANGE |
| 2026-W12 | 91.94% | 30.60% | 6.86% | 0.20% | 44,707 | +0.25% |
| 2026-W11 | 91.72% | 29.91% | 7.11% | 0.15% | 49,927 | -0.70% |
| 2026-W10 | 92.36% | 29.84% | 6.44% | 0.22% | 52,844 | -0.01% |
| 2026-W09 | 92.37% | 29.17% | 6.28% | 0.37% | 54,963 | +0.86% |
| 2026-W08 | 91.58% | 29.98% | 7.05% | 0.26% | 54,577 | -0.44% |
| 2026-W07 | 91.99% | 29.94% | 6.76% | 0.16% | 54,624 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| AU | 2026-W12 | 93.97% | - | 34.51% | - | 4,459 |  |
| AU | 2026-W13 | 91.92% | -2.17% | 35.49% | +2.84% | 3,826 |  |
| NL | 2026-W12 | 94.24% | - | 25.64% | - | 2,414 |  |
| NL | 2026-W13 | 91.58% | -2.83% | 29.43% | +14.79% | 2,565 | ⚠️ |
| GB | 2026-W12 | 92.01% | - | 40.62% | - | 10,497 |  |
| GB | 2026-W13 | 92.37% | +0.40% | 40.34% | -0.69% | 11,628 |  |
| NZ | 2026-W12 | 90.59% | - | 36.24% | - | 861 |  |
| NZ | 2026-W13 | 85.61% | -5.50% | 38.99% | +7.60% | 813 | ⚠️ |
| DK | 2026-W12 | 85.78% | - | 29.10% | - | 1,385 |  |
| DK | 2026-W13 | 88.62% | +3.31% | 26.14% | -10.17% | 1,098 | ⚠️ |
| LU | 2026-W12 | 98.61% | - | 0.00% | - | 72 |  |
| LU | 2026-W13 | 93.02% | -5.67% | 0.00% | - | 86 | ⚠️ |

**Countries exceeding ±2.5% threshold:** NL, NZ, DK, LU

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W12 | 97.23% | - | 30.92% | - | 33,344 |  |
| Paid | 2026-W13 | 96.85% | -0.39% | 30.81% | -0.35% | 35,485 |  |
| Referral | 2026-W12 | 76.42% | - | 29.67% | - | 11,363 |  |
| Referral | 2026-W13 | 75.75% | -0.88% | 29.62% | -0.15% | 11,204 |  |

---

*Report: 2026-04-10*
