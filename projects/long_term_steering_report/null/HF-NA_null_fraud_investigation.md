# Fraud Investigation: HF-NA null

**Metric:** Fraud Approval Rate  
**Period:** 2026-W14 → null  
**Observation:** 90.97% → 89.66% (-1.44%)  
**Volume:** 27,570 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) declined by 1.44 percentage points (pp) from 90.97% to 89.66% week-over-week (2026-W14 → 2026-W15), representing a significant metric movement on a volume of 27,570 customers.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Duplicate Rate | 26.08% → 26.94% | +0.86 pp | ⚠️ |
| Duplicate Block Rate | 6.50% → 6.71% | +0.21 pp | ⚠️ |
| Policy Fail Block Rate | 1.37% → 2.84% | +1.47 pp | ⚠️ |
| Final FAR | 90.97% → 89.66% | -1.31 pp | ⚠️ |

**Key Findings:**
- Policy Fail (PF) Block Rate increased significantly by +1.47 pp (1.37% → 2.84%), more than doubling from the prior week and representing the largest single contributor to the FAR decline
- Duplicate Rate rose by +0.86 pp to 26.94%, the highest level in the 8-week trend window
- Duplicate Block Rate increased modestly by +0.21 pp to 6.71%, also reaching an 8-week high
- Volume increased substantially by +16.8% (23,608 → 27,570 customers), which may have contributed to elevated block rates
- No country-level anomalies were flagged (none exceeded the ±2.5% threshold); L1 channel data is unavailable for further drill-down

**Action:** Investigate — The sharp increase in PF Block Rate (+1.47 pp) warrants immediate investigation into policy rule changes or model threshold adjustments deployed around 2026-W15. Review whether the volume surge correlates with a specific traffic source or customer segment.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W15 | 89.66% | 26.94% | 6.71% | 2.84% | 27,570 | -1.44% |
| 2026-W14 | 90.97% | 26.08% | 6.50% | 1.37% | 23,608 | +2.09% |
| 2026-W13 | 89.11% | 26.00% | 6.27% | 3.32% | 24,583 | -1.32% |
| 2026-W12 | 90.30% | 25.57% | 6.05% | 2.49% | 24,841 | +0.04% |
| 2026-W11 | 90.27% | 24.97% | 5.89% | 2.65% | 26,804 | -1.36% |
| 2026-W10 | 91.51% | 25.48% | 5.85% | 1.40% | 27,719 | -0.07% |
| 2026-W09 | 91.57% | 24.89% | 5.82% | 1.27% | 30,555 | +0.03% |
| 2026-W08 | 91.54% | 24.94% | 6.14% | 1.08% | 28,184 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|

**Countries exceeding ±2.5% threshold:** None

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|

---

*Report: 2026-04-14*
