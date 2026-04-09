# Fraud Investigation: HF-INTL 2026-W14

**Metric:** Fraud Approval Rate  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 91.79% → 91.70% (-0.10%)  
**Volume:** 37,558 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) for HF-INTL declined marginally from 91.79% to 91.70% (-0.09 pp) in 2026-W14, a statistically non-significant change accompanied by a notable 19.6% decrease in volume (46,689 → 37,558 customers).

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: Overall FAR | 91.79% → 91.70% | -0.09 pp | ✅ |
| L0: Duplicate Rate | 30.52% → 30.22% | -0.30 pp | ✅ |
| L0: Duplicate Block Rate | 6.61% → 7.42% | +0.81 pp | ⚠️ |
| L0: PF Block Rate | 0.27% → 0.25% | -0.02 pp | ✅ |
| L1: Country Variance | NZ +4.56 pp, LU +4.71 pp | Exceeds ±2.5% | ⚠️ |
| L1: Channel Variance | Paid +0.77 pp, Referral +0.18 pp | Within threshold | ✅ |

**Key Findings:**
- **Volume decline:** Total volume dropped significantly from 46,689 to 37,558 (-19.6%), continuing a 4-week downward trend from the W09 peak of 54,963
- **Duplicate Block Rate increased:** Rose from 6.61% to 7.42% (+0.81 pp), the highest level in the 8-week period, potentially contributing to the slight FAR decline
- **NZ showed notable improvement:** FAR increased +4.56 pp (85.61% → 89.51%) with duplicate rate dropping -7.76 pp (38.99% → 35.97%)
- **FR continues underperformance:** FAR declined -0.93 pp to 87.97%, remaining the lowest-performing major market
- **AT duplicate rate spike:** Duplicate rate increased +21.46% (19.02% → 23.10%) though FAR impact was moderate (-2.24 pp)

**Action:** Monitor — The overall FAR change is non-significant and within normal fluctuation. Continue monitoring the Duplicate Block Rate trend and FR market performance over the next 1-2 weeks.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W14 | 91.70% | 30.22% | 7.42% | 0.25% | 37,558 | -0.10% ← REPORTED CHANGE |
| 2026-W13 | 91.79% | 30.52% | 6.61% | 0.27% | 46,689 | -0.17% |
| 2026-W12 | 91.94% | 30.60% | 6.86% | 0.20% | 44,707 | +0.25% |
| 2026-W11 | 91.72% | 29.91% | 7.11% | 0.15% | 49,927 | -0.70% |
| 2026-W10 | 92.36% | 29.84% | 6.44% | 0.22% | 52,844 | -0.01% |
| 2026-W09 | 92.37% | 29.17% | 6.28% | 0.37% | 54,963 | +0.86% |
| 2026-W08 | 91.58% | 29.98% | 7.05% | 0.26% | 54,577 | -0.44% |
| 2026-W07 | 91.99% | 29.94% | 6.76% | 0.16% | 54,624 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| FR | 2026-W13 | 88.80% | - | 25.69% | - | 10,733 |  |
| FR | 2026-W14 | 87.97% | -0.93% | 25.90% | +0.83% | 9,239 |  |
| GB | 2026-W13 | 92.37% | - | 40.34% | - | 11,628 |  |
| GB | 2026-W14 | 92.73% | +0.39% | 39.58% | -1.89% | 8,861 |  |
| NZ | 2026-W13 | 85.61% | - | 38.99% | - | 813 |  |
| NZ | 2026-W14 | 89.51% | +4.56% | 35.97% | -7.76% | 734 | ⚠️ |
| AU | 2026-W13 | 91.92% | - | 35.49% | - | 3,826 |  |
| AU | 2026-W14 | 92.46% | +0.58% | 36.22% | +2.06% | 3,009 |  |
| AT | 2026-W13 | 92.87% | - | 19.02% | - | 673 |  |
| AT | 2026-W14 | 90.79% | -2.24% | 23.10% | +21.46% | 619 |  |
| LU | 2026-W13 | 93.02% | - | 0.00% | - | 86 |  |
| LU | 2026-W14 | 97.40% | +4.71% | 9.09% | - | 77 | ⚠️ |
| CH | 2026-W13 | 92.90% | - | 11.48% | - | 183 |  |
| CH | 2026-W14 | 90.60% | -2.47% | 11.11% | -3.17% | 117 |  |

**Countries exceeding ±2.5% threshold:** NZ, LU

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W13 | 96.85% | - | 30.81% | - | 35,485 |  |
| Paid | 2026-W14 | 97.60% | +0.77% | 30.16% | -2.11% | 27,353 |  |
| Referral | 2026-W13 | 75.75% | - | 29.62% | - | 11,204 |  |
| Referral | 2026-W14 | 75.88% | +0.18% | 30.39% | +2.58% | 10,205 |  |

---

*Report: 2026-04-09*
