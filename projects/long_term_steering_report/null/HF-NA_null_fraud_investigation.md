# Fraud Investigation: HF-NA null

**Metric:** Fraud Approval Rate  
**Period:** 2026-W14 → null  
**Observation:** 90.81% → 89.67% (-1.25%)  
**Volume:** 27,588 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) declined by -1.25pp from 90.81% (2026-W14) to 89.67% (2026-W15), representing a significant week-over-week decrease amid increased volume of 27,588 customers.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Duplicate Rate | 26.36% → 26.93% | +0.57pp | ⚠️ |
| Duplicate Block Rate | 6.60% → 6.71% | +0.11pp | ✅ |
| PF Block Rate | 1.39% → 2.84% | +1.45pp | ⚠️ |
| Overall FAR | 90.81% → 89.67% | -1.14pp | ⚠️ |

**Key Findings:**
- PF Block Rate doubled from 1.39% to 2.84% (+1.45pp), the highest level in the 8-week period and the primary driver of the FAR decline
- Volume increased by 18.0% (23,383 → 27,588), indicating higher fraud service traffic coinciding with the metric decline
- Duplicate Rate reached its 8-week high at 26.93%, continuing a steady upward trend from 24.94% in W08
- No individual countries exceeded the ±2.5% threshold, suggesting the decline is distributed across the region rather than localized
- The FAR of 89.67% remains within normal weekly variance, with similar levels observed in W13 (89.11%) and W11 (90.26%)

**Action:** Monitor — The FAR decline appears driven primarily by elevated PF Block Rate. Continue monitoring PF Block trends in W16; if PF Block Rate remains above 2.5% or FAR drops below 89%, escalate for investigation into PF model behavior.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W15 | 89.67% | 26.93% | 6.71% | 2.84% | 27,588 | -1.25% |
| 2026-W14 | 90.81% | 26.36% | 6.60% | 1.39% | 23,383 | +1.90% |
| 2026-W13 | 89.11% | 26.00% | 6.27% | 3.32% | 24,583 | -1.32% |
| 2026-W12 | 90.31% | 25.57% | 6.06% | 2.50% | 24,841 | +0.05% |
| 2026-W11 | 90.26% | 24.97% | 5.90% | 2.65% | 26,805 | -1.37% |
| 2026-W10 | 91.51% | 25.48% | 5.85% | 1.40% | 27,719 | -0.06% |
| 2026-W09 | 91.57% | 24.90% | 5.83% | 1.27% | 30,556 | +0.03% |
| 2026-W08 | 91.55% | 24.94% | 6.14% | 1.08% | 28,184 | - |

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

*Report: 2026-04-13*
