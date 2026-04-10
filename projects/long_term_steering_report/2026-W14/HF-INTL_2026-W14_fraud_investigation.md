# Fraud Investigation: HF-INTL 2026-W14

**Metric:** Fraud Approval Rate  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 91.79% → 91.70% (-0.10%)  
**Volume:** 37,558 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate for HF-INTL declined marginally from 91.79% to 91.70% (-0.10pp) in 2026-W14, a change deemed not statistically significant against a volume of 37,558 customers.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: HF-INTL Trend | FAR within normal 8-week range (91.58%-92.37%) | -0.10pp | ✅ |
| L0: Duplicate Rate | Slight decrease in duplicate rate | -0.30pp | ✅ |
| L0: Duplicate Block Rate | Increased blocking | +0.81pp | ⚠️ |
| L1: Country Variance | NZ (+4.56pp), LU (+4.71pp) exceed threshold | Mixed | ⚠️ |
| L1: Channel Category | Paid and Referral channels stable | <1pp | ✅ |

**Key Findings:**
- Volume decreased significantly from 46,689 to 37,558 customers (-19.6%), which may amplify percentage fluctuations
- NZ showed notable FAR improvement (+4.56pp to 89.51%) accompanied by a -7.76pp drop in duplicate rate (from 38.99% to 35.97%)
- LU experienced the largest FAR increase (+4.71pp to 97.40%), though on very low volume (77 customers)
- AT saw elevated duplicate rate (+21.46% relative increase, from 19.02% to 23.10%) alongside a -2.24pp FAR decline
- FR contributed the largest negative impact with FAR declining -0.93pp on the highest individual country volume (9,239)

**Action:** Monitor — The overall change is not significant and falls within normal weekly variance. Continue tracking AT duplicate rate trends and FR performance in the coming week.

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

*Report: 2026-04-10*
