# AR Initial (LL0) Investigation: US-HF null

**Metric:** AR Initial (LL0)  
**Period:** 2026-W14 → null  
**Observation:** 89.02% → 89.71% (+0.78%)  
**Volume:** 12,220 orders

## Executive Summary

**Overall:** AR Initial (LL0) for US-HF improved from 89.02% to 89.71%, an increase of +0.69 percentage points week-over-week, with 12,220 orders processed in 2026-W15.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0 Trend | 8-week stability | +0.78% WoW | ✅ |
| L1 Country | Threshold ±2.5% | None flagged | ✅ |
| L1 Dimension | Anomaly scan | No data available | ⚠️ |

**Key Findings:**
- AR Initial rate increased +0.78% WoW, reaching 89.71% in W15—the highest rate in the 8-week period alongside W11 (90.11%)
- Volume decreased significantly from 19,259 (W10) to 12,220 (W15), representing a ~37% volume reduction over 5 weeks
- No countries exceeded the ±2.5% threshold, indicating stable performance across all markets
- The metric shows recovery after a dip in W12-W13 (88.7% and 87.69% respectively)
- L1 Dimension Scan returned no data, limiting root cause analysis capability

**Action:** Monitor — The metric is trending positively and within acceptable thresholds. Continue monitoring the volume decline trend and investigate if L1 dimension data becomes available.

---

---

## L0: 8-Week Trend (US-HF)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 89.71% | 12,220 | +0.78% |
| 2026-W14 | 89.02% | 11,598 | +1.52% |
| 2026-W13 | 87.69% | 10,897 | -1.14% |
| 2026-W12 | 88.7% | 14,798 | -1.56% |
| 2026-W11 | 90.11% | 15,868 | +0.95% |
| 2026-W10 | 89.26% | 19,259 | +0.01% |
| 2026-W09 | 89.25% | 18,657 | -0.36% |
| 2026-W08 | 89.57% | 18,802 | - |

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

*Report: 2026-04-13*
