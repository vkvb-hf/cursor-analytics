# Fraud Investigation: HF-NA 2026-W13

**Metric:** Fraud Approval Rate  
**Period:** 2026-W13 → 2026-W13  
**Observation:** 89.13% → 90.90% (+1.98%)  
**Volume:** 23,540 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) improved from 89.13% to 90.90% (+1.77pp) in 2026-W14, recovering from the prior week's decline and returning closer to the 8-week average of ~91%.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Regional Trend | FAR within normal range | +1.98% | ✅ |
| L0: Duplicate Rate | Dup Rate increased | +0.53pp (26.05% → 26.58%) | ✅ |
| L0: Duplicate Block | Dup Block increased | +0.53pp (6.32% → 6.85%) | ✅ |
| L0: PF Block | PF Block decreased significantly | -1.85pp (3.33% → 1.48%) | ✅ |
| L1: Country | No country exceeded ±2.5% threshold | US: -1.41%, CA: -0.98% | ✅ |
| L1: Channel | Referral channel exceeded threshold | -2.93% | ⚠️ |

**Key Findings:**
- PF Block rate dropped significantly from 3.33% to 1.48% (-1.85pp), which is the primary driver of the FAR improvement
- Referral channel shows concerning decline in FAR (62.72%, -2.93%), falling below the ±2.5% threshold and warranting attention
- Duplicate Rate continues its upward trend, reaching 26.58% (highest in the 8-week period), with Dup Block also increasing to 6.85%
- Volume decreased by 4.3% (24,590 → 23,540 customers), continuing the declining volume trend observed since W09
- Both US and CA showed slight FAR declines in W13 (-1.41% and -0.98% respectively), but neither exceeded alert thresholds

**Action:** Monitor — The FAR recovery is driven by reduced PF Block rates. Continue monitoring the Referral channel performance and the rising Duplicate Rate trend.

---

---

## L0: 8-Week Trend (HF-NA)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W14 | 90.90% | 26.58% | 6.85% | 1.48% | 23,540 | +1.98% |
| 2026-W13 | 89.13% | 26.05% | 6.32% | 3.33% | 24,590 | -1.30% ← REPORTED CHANGE |
| 2026-W12 | 90.31% | 25.61% | 6.09% | 2.50% | 24,841 | +0.05% |
| 2026-W11 | 90.27% | 25.00% | 5.92% | 2.65% | 26,806 | -1.38% |
| 2026-W10 | 91.53% | 25.50% | 5.87% | 1.40% | 27,721 | -0.06% |
| 2026-W09 | 91.58% | 24.92% | 5.85% | 1.27% | 30,559 | +0.03% |
| 2026-W08 | 91.55% | 24.95% | 6.16% | 1.08% | 28,186 | -1.05% |
| 2026-W07 | 92.52% | 23.92% | 5.50% | 0.89% | 30,135 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| US | 2026-W12 | 89.88% | - | 24.70% | - | 17,515 |  |
| US | 2026-W13 | 88.61% | -1.41% | 25.13% | +1.71% | 17,575 |  |
| CA | 2026-W12 | 91.33% | - | 27.76% | - | 7,326 |  |
| CA | 2026-W13 | 90.43% | -0.98% | 28.37% | +2.17% | 7,015 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W12 | 96.94% | - | 24.36% | - | 19,749 |  |
| Paid | 2026-W13 | 95.99% | -0.98% | 25.08% | +2.97% | 19,523 |  |
| Referral | 2026-W12 | 64.61% | - | 30.44% | - | 5,092 |  |
| Referral | 2026-W13 | 62.72% | -2.93% | 29.78% | -2.16% | 5,067 | ⚠️ |

---

*Report: 2026-04-10*
