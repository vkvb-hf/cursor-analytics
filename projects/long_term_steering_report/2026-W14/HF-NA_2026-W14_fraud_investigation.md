# Fraud Investigation: HF-NA 2026-W14

**Metric:** Fraud Approval Rate  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 89.13% → 90.90% (+1.98%)  
**Volume:** 23,540 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Fraud Approval Rate improved from 89.13% to 90.90% (+1.98pp), returning closer to the 8-week average after a dip in W13.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Regional Trend | FAR within normal range (W07-W14: 89-92%) | +1.98pp | ✅ |
| L1: Country | US exceeds ±2.5% threshold | +3.30pp | ⚠️ |
| L1: Channel | Referral exceeds threshold | +6.81pp | ⚠️ |
| PF Block Rate | Significant decrease from W13 | -1.85pp | ✅ |
| Dup Rate | Slight increase | +0.53pp | ✅ |

**Key Findings:**
- US drove the regional FAR increase, improving +3.30pp (88.61% → 91.54%) while volume decreased by 966 customers
- Referral channel showed significant volatility with FAR +6.81pp and Duplicate Rate spiking +17.19pp (29.78% → 34.90%)
- PF Block Rate dropped sharply from 3.33% (W13) to 1.48% (W14), contributing to higher approvals
- Overall volume continues declining trend: 30,135 (W07) → 23,540 (W14), down ~22% over 8 weeks
- Canada moved counter to the regional trend, declining -1.20pp (90.43% → 89.35%)

**Action:** Monitor – The FAR increase appears to be a reversion to normal levels after W13's dip, primarily driven by reduced PF blocking. However, investigate the Referral channel's unusual duplicate rate spike (+17.19pp) to rule out potential abuse patterns.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W14 | 90.90% | 26.58% | 6.85% | 1.48% | 23,540 | +1.98% ← REPORTED CHANGE |
| 2026-W13 | 89.13% | 26.05% | 6.32% | 3.33% | 24,590 | -1.30% |
| 2026-W12 | 90.31% | 25.61% | 6.09% | 2.50% | 24,841 | +0.05% |
| 2026-W11 | 90.27% | 25.00% | 5.92% | 2.65% | 26,806 | -1.38% |
| 2026-W10 | 91.53% | 25.50% | 5.87% | 1.40% | 27,721 | -0.06% |
| 2026-W09 | 91.58% | 24.92% | 5.85% | 1.27% | 30,559 | +0.03% |
| 2026-W08 | 91.55% | 24.95% | 6.16% | 1.08% | 28,186 | -1.05% |
| 2026-W07 | 92.52% | 23.92% | 5.50% | 0.89% | 30,135 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| US | 2026-W13 | 88.61% | - | 25.13% | - | 17,575 |  |
| US | 2026-W14 | 91.54% | +3.30% | 26.05% | +3.68% | 16,609 | ⚠️ |
| CA | 2026-W13 | 90.43% | - | 28.37% | - | 7,015 |  |
| CA | 2026-W14 | 89.35% | -1.20% | 27.85% | -1.84% | 6,931 |  |

**Countries exceeding ±2.5% threshold:** US

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W13 | 95.99% | - | 25.08% | - | 19,523 |  |
| Paid | 2026-W14 | 96.46% | +0.49% | 24.64% | -1.75% | 19,096 |  |
| Referral | 2026-W13 | 62.72% | - | 29.78% | - | 5,067 |  |
| Referral | 2026-W14 | 66.99% | +6.81% | 34.90% | +17.19% | 4,444 | ⚠️ |

---

*Report: 2026-04-09*
