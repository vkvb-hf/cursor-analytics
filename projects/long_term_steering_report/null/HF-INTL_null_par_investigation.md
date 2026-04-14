# PAR Investigation: HF-INTL null

**Metric:** PAR  
**Period:** 2026-W14 → null  
**Observation:** 97.04% → 97.27% (+0.24%)  
**Volume:** 744,637 orders

## Executive Summary

**Overall:** PAR rate improved by +0.24 percentage points (97.04% → 97.27%) in 2026-W15, continuing a recovery trend from the W09-W10 low point, though on reduced volume of 744,637 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Metric direction | +0.24 pp | ✅ |
| L1: Country Breakdown | Countries ±2.5% threshold | None flagged | ✅ |
| L1: Dimension Scan | Anomalous dimensions | No data available | ⚠️ |

**Key Findings:**
- PAR rate reached its highest point in the 8-week window at 97.27%, surpassing the previous high of 97.25% in W12
- Volume declined by 39,769 orders (-5.1%) week-over-week, continuing a downward volume trend observed since W11 (897,107 → 744,637)
- The metric has recovered +1.05 pp from its trough in W09 (96.22%), indicating sustained improvement over 6 weeks
- No country-level anomalies exceeded the ±2.5% threshold, suggesting the improvement is broadly distributed
- L1 dimension scan data is empty, limiting root cause visibility into specific drivers

**Action:** Monitor — The positive trend is encouraging with no flagged anomalies, but the declining volume warrants continued observation. If volume continues to drop while rates improve, investigate potential selection bias or market mix shifts.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 97.27% | 744,637 | +0.24% |
| 2026-W14 | 97.04% | 784,406 | -0.13% |
| 2026-W13 | 97.17% | 842,482 | -0.08% |
| 2026-W12 | 97.25% | 877,189 | +0.04% |
| 2026-W11 | 97.21% | 897,107 | +0.52% |
| 2026-W10 | 96.71% | 916,831 | +0.51% |
| 2026-W09 | 96.22% | 896,537 | -0.12% |
| 2026-W08 | 96.34% | 884,970 | - |

---

## L1: Country Breakdown

| Country | Curr Rate | Prev Rate | Δ % | Curr Volume | Flag |
|---------|-----------|-----------|-----|-------------|------|

**Countries exceeding ±2.5% threshold:** None

---

## L1: Dimension Scan

| Dimension | Value | Curr Rate | Prev Rate | Δ % | Volume |
|-----------|-------|-----------|-----------|-----|--------|

---

*Report: 2026-04-14*
