# Fraud Investigation: WL 2026-W12

**Metric:** Fraud Approval Rate  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 92.73% → 93.06% (+0.35%)  
**Volume:** 13,609 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) improved slightly from 92.73% to 93.06% (+0.33pp), a statistically non-significant change within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall FAR | 92.73% → 93.06% | +0.33pp | ✅ |
| L0: Duplicate Rate | 15.53% → 15.81% | +0.28pp | ✅ |
| L0: Duplicate Block | 5.07% → 5.25% | +0.18pp | ✅ |
| L0: PF Block | 0.80% → 0.84% | +0.04pp | ✅ |
| L1: Country (CK) | 94.51% → 90.99% | -3.52pp | ⚠️ |
| L1: Channel (Referral) | 77.86% → 76.03% | -1.83pp | ✅ |

**Key Findings:**
- CK country shows a significant FAR decline of -3.73% (94.51% → 90.99%) alongside a +20.54% increase in duplicate rate (22.33% → 26.91%), exceeding the ±2.5% threshold
- Overall volume decreased by 5.5% (14,394 → 13,609 customers), continuing a downward trend from W07 peak of 19,099
- PF Block rate has stabilized at ~0.80-0.84% after a significant spike in W07 (5.17%)
- Referral channel maintains notably lower FAR (76.03%) compared to Paid channel (96.19%), with both showing slight week-over-week declines

**Action:** Monitor – Focus attention on CK country where duplicate rate spike (+20.54%) correlates with the FAR decline; investigate if this represents a localized fraud pattern or operational issue.

---

---

## L0: 8-Week Trend (WL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W14 | 93.06% | 15.81% | 5.25% | 0.84% | 13,609 | +0.35% |
| 2026-W13 | 92.73% | 15.53% | 5.07% | 0.80% | 14,394 | -0.32% |
| 2026-W12 | 93.03% | 15.96% | 4.88% | 0.43% | 15,081 | -1.35% ← REPORTED CHANGE |
| 2026-W11 | 94.31% | 14.77% | 4.13% | 0.35% | 16,403 | +0.50% |
| 2026-W10 | 93.84% | 15.79% | 4.48% | 0.45% | 17,316 | +0.41% |
| 2026-W09 | 93.46% | 15.27% | 4.66% | 0.54% | 16,428 | +0.09% |
| 2026-W08 | 93.37% | 15.19% | 4.89% | 0.49% | 16,797 | +4.50% |
| 2026-W07 | 89.36% | 14.40% | 4.28% | 5.17% | 19,099 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| CK | 2026-W11 | 94.51% | - | 22.33% | - | 3,171 |  |
| CK | 2026-W12 | 90.99% | -3.73% | 26.91% | +20.54% | 2,586 | ⚠️ |
| MR | 2026-W11 | 98.02% | - | 6.24% | - | 2,582 |  |
| MR | 2026-W12 | 96.39% | -1.66% | 6.95% | +11.43% | 2,274 |  |
| AO | 2026-W11 | 90.01% | - | 25.64% | - | 1,061 |  |
| AO | 2026-W12 | 88.29% | -1.92% | 24.95% | -2.67% | 1,050 |  |
| KN | 2026-W11 | 91.78% | - | 7.68% | - | 2,409 |  |
| KN | 2026-W12 | 91.26% | -0.56% | 7.84% | +2.10% | 2,232 |  |

**Countries exceeding ±2.5% threshold:** CK

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W11 | 97.13% | - | 13.28% | - | 14,000 |  |
| Paid | 2026-W12 | 96.19% | -0.96% | 14.25% | +7.31% | 12,716 |  |
| Referral | 2026-W11 | 77.86% | - | 23.43% | - | 2,403 |  |
| Referral | 2026-W12 | 76.03% | -2.36% | 25.16% | +7.38% | 2,365 |  |

---

*Report: 2026-04-10*
