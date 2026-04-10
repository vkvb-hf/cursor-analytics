# Fraud Investigation: RTE 2026-W13

**Metric:** Fraud Approval Rate  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 94.14% → 94.72% (+0.61%)  
**Volume:** 42,650 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) improved slightly from 94.14% to 94.72% (+0.58pp) in 2026-W13, a change that is not statistically significant and falls within normal weekly fluctuation range (8-week range: 93.82% - 94.95%).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall FAR Trend | 8-week stability check | +0.61pp | ✅ |
| L1: Country Breakdown | ±2.5% threshold | TZ +3.52pp, TK -6.23pp | ⚠️ |
| L1: Channel Category | Category stability | Paid +0.13pp, Referral +1.10pp | ✅ |

**Key Findings:**
- **TK (Tokelau) anomaly:** FAR dropped -6.23pp (94.30% → 88.42%) while Duplicate Rate spiked +108.86% (5.70% → 11.90%), indicating potential fraud pattern emergence in this small market (311 volume)
- **TZ (Tanzania) improvement:** FAR increased +3.52pp (88.29% → 91.40%) with Duplicate Rate decreasing -36.36% (12.21% → 7.77%), suggesting improved fraud detection efficiency (605 volume)
- **Volume decline observed:** Overall volume dropped from 45,581 (W12) to 43,962 (W13), continuing a downward trend from peak of 51,707 in W09
- **Channel performance stable:** Both Paid (96.63% FAR) and Referral (82.35% FAR) channels show consistent performance with minimal week-over-week changes
- **Duplicate Rate stable:** Overall duplicate rate remained steady at ~14.50%, with Duplicate Block Rate increasing slightly from 4.06% to 4.46%

**Action:** **Monitor** – Overall metric is stable and change is not significant. However, recommend targeted monitoring of TK market due to significant FAR decline and duplicate rate spike, despite low volume.

---

---

## L0: 8-Week Trend (RTE)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W14 | 94.72% | 14.31% | 4.46% | 0.20% | 42,650 | +0.61% |
| 2026-W13 | 94.14% | 14.50% | 4.06% | 0.26% | 43,962 | +0.34% ← REPORTED CHANGE |
| 2026-W12 | 93.82% | 14.53% | 4.28% | 0.22% | 45,581 | -0.63% |
| 2026-W11 | 94.41% | 14.54% | 3.91% | 0.21% | 48,713 | -0.57% |
| 2026-W10 | 94.95% | 13.98% | 3.74% | 0.16% | 50,499 | +0.53% |
| 2026-W09 | 94.45% | 14.28% | 4.09% | 0.22% | 51,707 | +0.43% |
| 2026-W08 | 94.05% | 14.98% | 4.35% | 0.12% | 48,963 | -0.20% |
| 2026-W07 | 94.25% | 14.89% | 4.17% | 0.12% | 50,465 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| FJ | 2026-W12 | 94.21% | - | 14.64% | - | 31,445 |  |
| FJ | 2026-W13 | 94.47% | +0.27% | 14.88% | +1.60% | 30,231 |  |
| CF | 2026-W12 | 93.70% | - | 13.64% | - | 6,732 |  |
| CF | 2026-W13 | 94.14% | +0.47% | 13.47% | -1.19% | 6,672 |  |
| YE | 2026-W12 | 93.34% | - | 19.52% | - | 4,309 |  |
| YE | 2026-W13 | 94.01% | +0.72% | 18.55% | -4.97% | 3,839 |  |
| TZ | 2026-W12 | 88.29% | - | 12.21% | - | 598 |  |
| TZ | 2026-W13 | 91.40% | +3.52% | 7.77% | -36.36% | 605 | ⚠️ |
| TK | 2026-W12 | 94.30% | - | 5.70% | - | 316 |  |
| TK | 2026-W13 | 88.42% | -6.23% | 11.90% | +108.86% | 311 | ⚠️ |
| TT | 2026-W12 | 89.94% | - | 7.95% | - | 1,044 |  |
| TT | 2026-W13 | 91.28% | +1.49% | 8.53% | +7.30% | 1,055 |  |
| TV | 2026-W12 | 91.75% | - | 6.53% | - | 521 |  |
| TV | 2026-W13 | 90.91% | -0.91% | 7.79% | +19.40% | 462 |  |

**Countries exceeding ±2.5% threshold:** TZ, TK

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W12 | 96.50% | - | 13.19% | - | 37,456 |  |
| Paid | 2026-W13 | 96.63% | +0.13% | 13.14% | -0.39% | 36,315 |  |
| Referral | 2026-W12 | 81.45% | - | 20.69% | - | 8,125 |  |
| Referral | 2026-W13 | 82.35% | +1.10% | 20.94% | +1.19% | 7,647 |  |

---

*Report: 2026-04-10*
