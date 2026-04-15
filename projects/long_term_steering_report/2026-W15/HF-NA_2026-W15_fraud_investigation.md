# Fraud Investigation: HF-NA 2026-W15

**Metric:** Fraud Approval Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 90.97% → 89.66% (-1.44%)  
**Volume:** 27,572 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate declined from 90.97% to 89.66% (-1.31 pp), representing a significant week-over-week decrease with volume increasing to 27,572 customers.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Regional (HF-NA) | FAR trend stability | -1.31 pp (89.66% vs 90.97%) | ⚠️ |
| Duplicate Rate | Dup Rate increase | +0.88 pp (26.94% vs 26.06%) | ⚠️ |
| Dup Block Rate | Block rate increase | +0.22 pp (6.71% vs 6.49%) | ✅ |
| PF Block Rate | Block rate increase | +1.47 pp (2.84% vs 1.37%) | ⚠️ |
| Country: US | FAR decline | -2.39 pp (89.20% vs 91.59%) | ⚠️ |
| Country: CA | FAR improvement | +1.41 pp (90.87% vs 89.46%) | ✅ |
| Channel: Referral | FAR decline | -4.80 pp (63.00% vs 67.80%) | ⚠️ |

**Key Findings:**
- US drove the regional decline with FAR dropping -2.39 pp (91.59% → 89.20%) while volume increased by 3,331 customers (+19.9%)
- PF Block Rate more than doubled from 1.37% to 2.84% (+1.47 pp), the highest level in the 8-week trend
- Referral channel showed severe degradation with FAR falling -4.80 pp (67.80% → 63.00%), significantly underperforming Paid channel (95.63%)
- Duplicate Rate reached an 8-week high of 26.94%, continuing an upward trend from 24.93% in W08
- CA showed positive counter-trend with FAR improving +1.41 pp despite the regional decline

**Action:** Investigate — Focus on US market performance and the sharp increase in PF Block Rate; additionally review Referral channel quality as it accounts for disproportionate FAR decline.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W15 | 89.66% | 26.94% | 6.71% | 2.84% | 27,572 | -1.44% ← REPORTED CHANGE |
| 2026-W14 | 90.97% | 26.06% | 6.49% | 1.37% | 23,607 | +2.09% |
| 2026-W13 | 89.11% | 25.99% | 6.26% | 3.32% | 24,581 | -1.32% |
| 2026-W12 | 90.30% | 25.55% | 6.04% | 2.49% | 24,839 | +0.03% |
| 2026-W11 | 90.27% | 24.97% | 5.89% | 2.65% | 26,804 | -1.36% |
| 2026-W10 | 91.51% | 25.47% | 5.84% | 1.40% | 27,719 | -0.06% |
| 2026-W09 | 91.57% | 24.88% | 5.81% | 1.27% | 30,555 | +0.03% |
| 2026-W08 | 91.54% | 24.93% | 6.13% | 1.08% | 28,183 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| US | 2026-W14 | 91.59% | - | 25.49% | - | 16,726 |  |
| US | 2026-W15 | 89.20% | -2.61% | 26.41% | +3.60% | 20,057 | ⚠️ |
| CA | 2026-W14 | 89.46% | - | 27.44% | - | 6,881 |  |
| CA | 2026-W15 | 90.87% | +1.57% | 28.34% | +3.30% | 7,515 |  |

**Countries exceeding ±2.5% threshold:** US

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 96.24% | - | 24.28% | - | 19,231 |  |
| Paid | 2026-W15 | 95.63% | -0.64% | 25.81% | +6.29% | 22,526 |  |
| Referral | 2026-W14 | 67.80% | - | 33.89% | - | 4,376 |  |
| Referral | 2026-W15 | 63.00% | -7.08% | 31.99% | -5.62% | 5,046 | ⚠️ |

---

*Report: 2026-04-15*
