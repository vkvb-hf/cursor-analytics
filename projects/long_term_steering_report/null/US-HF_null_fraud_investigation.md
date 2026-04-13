# Fraud Investigation: US-HF null

**Metric:** Fraud Approval Rate  
**Period:** 2026-W14 → null  
**Observation:** 91.48% → 89.22% (-2.47%)  
**Volume:** 20,071 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) declined by -2.47 percentage points from 91.48% (2026-W14) to 89.22% (2026-W15), representing a significant decrease amid increased volume (20,071 vs 16,517 customers).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | FAR dropped while volume increased 21.5% | -2.47 pp | ⚠️ |
| L0: Duplicate Rate | Increased from 25.86% to 26.40% | +0.54 pp | ⚠️ |
| L0: Duplicate Block Rate | Increased from 6.61% to 7.03% | +0.42 pp | ⚠️ |
| L0: PF Block Rate | Significant increase from 0.87% to 3.03% | +2.16 pp | ⚠️ |
| L1: Country Breakdown | No data available | N/A | ✅ |
| L1: Channel Category | No data available | N/A | ✅ |

**Key Findings:**
- PF Block Rate spiked significantly from 0.87% to 3.03% (+2.16 pp), the highest level in the 8-week trend and likely the primary driver of the FAR decline
- Volume increased by 21.5% (16,517 → 20,071) week-over-week, which may have introduced higher-risk traffic
- Duplicate Rate reached its highest point in the 8-week window at 26.40%, with Duplicate Block Rate also at peak (7.03%)
- The FAR decline follows a pattern of volatility, with W14 showing an unusual spike to 91.48% that has now corrected
- No L1 country or channel data is available to isolate the root cause of the degradation

**Action:** Investigate — The significant increase in PF Block Rate (+2.16 pp) requires immediate investigation to identify the underlying policy or model change driving elevated blocks; additionally, the missing L1 data should be populated to enable proper root cause analysis.

---

---

## L0: 8-Week Trend (US-HF)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W15 | 89.22% | 26.40% | 7.03% | 3.03% | 20,071 | -2.47% |
| 2026-W14 | 91.48% | 25.86% | 6.61% | 0.87% | 16,517 | +3.27% |
| 2026-W13 | 88.58% | 25.08% | 6.69% | 3.59% | 17,571 | -1.45% |
| 2026-W12 | 89.88% | 24.67% | 6.33% | 2.72% | 17,515 | +0.14% |
| 2026-W11 | 89.75% | 23.88% | 6.19% | 2.92% | 19,068 | -2.03% |
| 2026-W10 | 91.61% | 24.70% | 5.95% | 1.22% | 20,601 | -0.08% |
| 2026-W09 | 91.68% | 24.04% | 5.92% | 1.16% | 23,225 | +0.29% |
| 2026-W08 | 91.41% | 23.87% | 6.50% | 0.90% | 21,169 | - |

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
