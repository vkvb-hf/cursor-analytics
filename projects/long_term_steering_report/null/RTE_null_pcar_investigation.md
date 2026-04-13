# PCAR Investigation: RTE null

**Metric:** PCAR  
**Period:** 2026-W14 → null  
**Observation:** 96.9% → 96.89% (-0.01%)  
**Volume:** 44,166 orders

## Executive Summary

**Overall:** PCAR declined marginally by -0.01 percentage points (96.9% → 96.89%) in W15 2026, representing a negligible change within normal operational variance on a volume of 44,166 orders.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Stability check | -0.01pp | ✅ |
| L1: Country Breakdown | Threshold ±2.5% | No countries flagged | ✅ |
| L1: Dimension Scan | Anomaly detection | No anomalies detected | ✅ |

**Key Findings:**
- The -0.01pp decline is statistically insignificant and represents the smallest week-over-week change in the 8-week observation period
- PCAR has remained remarkably stable in the 96.88%-96.99% range over the past 6 weeks (W10-W15), with the exception of W09 which peaked at 97.3%
- Volume decreased by approximately 11% compared to the 8-week average (~47,199), though this did not materially impact the rate
- No country-level or dimensional anomalies were flagged, indicating the minor decline is distributed rather than concentrated
- The metric appears to have stabilized after a -0.42pp drop in W10 following the W09 peak

**Action:** Monitor – No immediate action required. The metric remains stable within acceptable bounds with no identified root cause for concern.

---

---

## L0: 8-Week Trend (RTE)

| Week | Rate % | Volume | Δ % vs Prior |
|------|--------|--------|--------------|
| 2026-W15 | 96.89% | 44,166 | -0.01% |
| 2026-W14 | 96.9% | 39,914 | +0.01% |
| 2026-W13 | 96.89% | 42,897 | +0.01% |
| 2026-W12 | 96.88% | 44,209 | -0.11% |
| 2026-W11 | 96.99% | 47,403 | +0.10% |
| 2026-W10 | 96.89% | 48,399 | -0.42% |
| 2026-W09 | 97.3% | 50,858 | +0.37% |
| 2026-W08 | 96.94% | 49,908 | - |

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
