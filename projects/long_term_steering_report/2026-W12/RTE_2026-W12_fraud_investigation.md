# Fraud Investigation: RTE 2026-W12

**Metric:** Fraud Approval Rate  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 94.14% → 94.72% (+0.61%)  
**Volume:** 42,650 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Fraud Approval Rate improved by +0.61pp (94.14% → 94.72%) in 2026-W12, with the change flagged as not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| Overall FAR | +0.61pp WoW | 94.14% → 94.72% | ✅ |
| Duplicate Rate | -0.19pp WoW | 14.50% → 14.31% | ✅ |
| Duplicate Block Rate | +0.40pp WoW | 4.06% → 4.46% | ✅ |
| PF Block Rate | -0.06pp WoW | 0.26% → 0.20% | ✅ |
| Country Breakdown | 2 countries exceed ±2.5% threshold | TZ, TV flagged | ⚠️ |
| Channel Category | No categories exceed threshold | Stable | ✅ |

**Key Findings:**
- TZ experienced significant FAR decline of -3.59pp (91.58% → 88.29%) coupled with a +35.30% increase in duplicate rate (9.02% → 12.21%), suggesting potential localized fraud pattern changes
- TV showed FAR decline of -2.53pp (94.13% → 91.75%) with duplicate rate increasing +31.73% (4.95% → 6.53%)
- FJ, the highest-volume country (31,445 customers), saw a moderate FAR decline of -0.91pp but remains within normal variance
- Overall volume decreased by approximately 3% (43,962 → 42,650 customers reaching fraud service)
- 8-week trend shows FAR oscillating within a narrow band (93.82% - 94.95%), indicating stable performance

**Action:** Monitor – The overall metric change is not significant and within historical variance. However, continue monitoring TZ and TV for sustained duplicate rate increases that may indicate emerging fraud vectors.

---

---

## L0: 8-Week Trend (RTE)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W14 | 94.72% | 14.31% | 4.46% | 0.20% | 42,650 | +0.61% |
| 2026-W13 | 94.14% | 14.50% | 4.06% | 0.26% | 43,962 | +0.34% |
| 2026-W12 | 93.82% | 14.53% | 4.28% | 0.22% | 45,581 | -0.63% ← REPORTED CHANGE |
| 2026-W11 | 94.41% | 14.54% | 3.91% | 0.21% | 48,713 | -0.57% |
| 2026-W10 | 94.95% | 13.98% | 3.74% | 0.16% | 50,499 | +0.53% |
| 2026-W09 | 94.45% | 14.28% | 4.09% | 0.22% | 51,707 | +0.43% |
| 2026-W08 | 94.05% | 14.98% | 4.35% | 0.12% | 48,963 | -0.20% |
| 2026-W07 | 94.25% | 14.89% | 4.17% | 0.12% | 50,465 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| FJ | 2026-W11 | 95.07% | - | 14.78% | - | 34,355 |  |
| FJ | 2026-W12 | 94.21% | -0.91% | 14.64% | -0.94% | 31,445 |  |
| CF | 2026-W11 | 93.24% | - | 13.84% | - | 6,863 |  |
| CF | 2026-W12 | 93.70% | +0.50% | 13.64% | -1.49% | 6,732 |  |
| YE | 2026-W11 | 92.70% | - | 19.26% | - | 4,082 |  |
| YE | 2026-W12 | 93.34% | +0.69% | 19.52% | +1.36% | 4,309 |  |
| TZ | 2026-W11 | 91.58% | - | 9.02% | - | 665 |  |
| TZ | 2026-W12 | 88.29% | -3.59% | 12.21% | +35.30% | 598 | ⚠️ |
| TT | 2026-W11 | 91.65% | - | 7.24% | - | 1,078 |  |
| TT | 2026-W12 | 89.94% | -1.86% | 7.95% | +9.88% | 1,044 |  |
| TV | 2026-W11 | 94.13% | - | 4.95% | - | 545 |  |
| TV | 2026-W12 | 91.75% | -2.53% | 6.53% | +31.73% | 521 | ⚠️ |
| TK | 2026-W11 | 92.45% | - | 8.63% | - | 371 |  |
| TK | 2026-W12 | 94.30% | +2.00% | 5.70% | -33.96% | 316 |  |

**Countries exceeding ±2.5% threshold:** TZ, TV

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W11 | 97.09% | - | 13.20% | - | 40,283 |  |
| Paid | 2026-W12 | 96.50% | -0.61% | 13.19% | -0.08% | 37,456 |  |
| Referral | 2026-W11 | 81.60% | - | 20.90% | - | 8,430 |  |
| Referral | 2026-W12 | 81.45% | -0.18% | 20.69% | -1.02% | 8,125 |  |

---

*Report: 2026-04-10*
