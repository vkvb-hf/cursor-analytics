# Fraud Investigation: HF-NA 2026-W17

**Metric:** Fraud Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 89.77% → 90.84% (+1.19%)  
**Volume:** 23,950 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Fraud Approval Rate improved from 89.77% to 90.84% (+1.19% / +1.07pp) in 2026-W17, with volume decreasing from 27,350 to 23,950 customers (-12.4%).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: HF-NA Trend | FAR within normal 8-week range (89.10%-91.53%) | +1.07pp | ✅ |
| L1: Country | No country exceeds ±2.5% threshold | US +2.03%, CA -1.06% | ✅ |
| L1: Channel Category | Referral shows elevated duplicate rate | +13.42% Dup Rate | ⚠️ |
| L2: CA Referral | Significant FAR decline with rising blocks | -8.12% FAR, +20.18% Dup Block | ⚠️ |

**Key Findings:**
- US drove the overall FAR improvement (+2.03% to 91.44%) while experiencing a healthy decrease in duplicate rate (-1.81%)
- CA Referral channel shows concerning performance: FAR dropped 8.12% to 59.93%, duplicate rate surged 11.80% to 41.21%, and duplicate block rate increased 20.18% to 34.18%
- Paid channel performance improved across both countries (HF-NA: +2.13% FAR with -3.07% duplicate rate)
- Overall volume declined 12.4% WoW, with reductions in both US (-15.5%) and CA (-3.4%)
- PF Block rate decreased at HF-NA level from 1.55% to 1.27% (-18.1%), contributing to FAR improvement

**Action:** Investigate — The CA Referral channel requires immediate investigation due to the significant FAR decline (-8.12%), elevated duplicate rate (41.21%), and high duplicate block rate (34.18%). Review referral source quality and potential fraud patterns in this segment.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W17 | 90.84% | 27.96% | 7.11% | 1.27% | 23,950 | +1.19% ← REPORTED CHANGE |
| 2026-W16 | 89.77% | 27.79% | 7.46% | 1.55% | 27,350 | +0.10% |
| 2026-W15 | 89.68% | 26.41% | 6.36% | 2.73% | 27,678 | -1.44% |
| 2026-W14 | 90.99% | 25.96% | 6.38% | 1.35% | 23,589 | +2.12% |
| 2026-W13 | 89.10% | 25.90% | 6.18% | 3.31% | 24,575 | -1.35% |
| 2026-W12 | 90.32% | 25.52% | 6.00% | 2.48% | 24,830 | +0.08% |
| 2026-W11 | 90.25% | 24.94% | 5.87% | 2.64% | 26,801 | -1.39% |
| 2026-W10 | 91.53% | 25.43% | 5.81% | 1.39% | 27,707 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| US | 2026-W16 | 89.62% | - | 27.34% | - | 20,464 |  |
| US | 2026-W17 | 91.44% | +2.03% | 26.84% | -1.81% | 17,298 |  |
| CA | 2026-W16 | 90.23% | - | 29.13% | - | 6,886 |  |
| CA | 2026-W17 | 89.27% | -1.06% | 30.86% | +5.94% | 6,652 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 94.23% | - | 26.81% | - | 22,775 |  |
| Paid | 2026-W17 | 96.23% | +2.13% | 25.99% | -3.07% | 19,676 |  |
| Referral | 2026-W16 | 67.58% | - | 32.63% | - | 4,575 |  |
| Referral | 2026-W17 | 65.98% | -2.37% | 37.01% | +13.42% | 4,274 |  |

---

## L2: CA Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 96.28% | - | 27.26% | - | 0.72% | - | 1.75% | - | 5,543 |  |
| Paid | 2026-W17 | 97.16% | +0.91% | 28.08% | +3.01% | 0.36% | -49.77% | 1.51% | -13.88% | 5,242 |  |
| Referral | 2026-W16 | 65.23% | - | 36.86% | - | 28.44% | - | 3.95% | - | 1,343 |  |
| Referral | 2026-W17 | 59.93% | -8.12% | 41.21% | +11.80% | 34.18% | +20.18% | 4.18% | +6.03% | 1,410 | ⚠️ |

**Analysis:** The HF-NA Fraud Approval Rate increase in 2026-W17 is primarily driven by improved Paid channel performance and lower PF Block rates, particularly in US. However, the CA Referral channel exhibits a deteriorating fraud profile with significantly elevated duplicate metrics and declining approval rates, suggesting potential fraud concentration or policy tightening in this segment. Focused investigation into CA Referral traffic sources is recommended before the next reporting period.

---



*Report: 2026-04-28*
