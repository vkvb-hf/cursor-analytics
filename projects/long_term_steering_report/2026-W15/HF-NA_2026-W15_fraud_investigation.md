# Fraud Investigation: HF-NA 2026-W15

**Metric:** Fraud Approval Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 90.97% → 89.66% (-1.44%)  
**Volume:** 27,570 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) declined from 90.97% to 89.66% (-1.31 pp) in 2026-W15, representing a significant week-over-week decrease amid a 16.8% volume increase (23,608 → 27,570 customers).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: HF-NA Overall | FAR 90.97% → 89.66% | -1.31 pp | ⚠️ |
| L0: Duplicate Rate | 26.08% → 26.94% | +0.86 pp | ✅ |
| L0: Dup Block Rate | 6.50% → 6.71% | +0.21 pp | ✅ |
| L0: PF Block Rate | 1.37% → 2.84% | +1.47 pp | ⚠️ |
| L1: Country - US | FAR 91.59% → 89.21% | -2.38 pp | ⚠️ |
| L1: Country - CA | FAR 89.46% → 90.88% | +1.42 pp | ✅ |
| L1: Channel - Paid | FAR 96.26% → 95.63% | -0.63 pp | ✅ |
| L1: Channel - Referral | FAR 67.76% → 63.01% | -4.75 pp | ⚠️ |

**Key Findings:**
- US drove the majority of FAR decline (-2.38 pp), exceeding the ±2.5% threshold and representing 73% of total volume in W15
- Referral channel experienced a significant FAR drop of -4.75 pp (67.76% → 63.01%), the largest decline across all segments
- PF Block Rate more than doubled from 1.37% to 2.84% (+1.47 pp), indicating increased policy-based rejections
- Volume surged 16.8% WoW while FAR declined, suggesting quality degradation in higher-volume traffic
- 8-week trend shows FAR fluctuating between 89.11% and 91.57%, with W15 near the lower end of this range

**Action:** Investigate – Focus drill-down on US market and Referral channel to identify root cause of elevated PF Block rates and declining approval rates.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W15 | 89.66% | 26.94% | 6.71% | 2.84% | 27,570 | -1.44% ← REPORTED CHANGE |
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
| US | 2026-W14 | 91.59% | - | 25.50% | - | 16,727 |  |
| US | 2026-W15 | 89.21% | -2.60% | 26.41% | +3.56% | 20,056 | ⚠️ |
| CA | 2026-W14 | 89.46% | - | 27.47% | - | 6,881 |  |
| CA | 2026-W15 | 90.88% | +1.59% | 28.35% | +3.20% | 7,514 |  |

**Countries exceeding ±2.5% threshold:** US

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 96.26% | - | 24.28% | - | 19,229 |  |
| Paid | 2026-W15 | 95.63% | -0.65% | 25.81% | +6.28% | 22,525 |  |
| Referral | 2026-W14 | 67.76% | - | 33.96% | - | 4,379 |  |
| Referral | 2026-W15 | 63.01% | -7.00% | 31.99% | -5.79% | 5,045 | ⚠️ |

---

*Report: 2026-04-14*
