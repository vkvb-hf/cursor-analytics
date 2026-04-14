# Fraud Investigation: US-HF 2026-W15

**Metric:** Fraud Approval Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 91.59% → 89.21% (-2.60%)  
**Volume:** 20,056 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Fraud Approval Rate declined from 91.59% to 89.21% (-2.60pp) in 2026-W15, representing a significant drop that reversed the prior week's gains.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: US-HF Trend | FAR within normal range? | -2.60pp | ⚠️ |
| L0: Duplicate Rate | Dup Rate stable? | +0.91pp (25.50% → 26.41%) | ⚠️ |
| L0: PF Block Rate | PF Block stable? | +2.18pp (0.85% → 3.03%) | ⚠️ |
| L1: Country | US within ±2.5%? | -2.60pp | ⚠️ |
| L1: Channel - Paid | Paid channel stable? | -0.99pp | ✅ |
| L1: Channel - Referral | Referral channel stable? | -12.09pp | ⚠️ |

**Key Findings:**
- Referral channel FAR dropped significantly from 69.96% to 61.50% (-12.09pp), the largest decline across all segments
- PF Block Rate spiked from 0.85% to 3.03% (+2.18pp), a 3.5x increase week-over-week, indicating tightened fraud prevention filters
- Volume increased 19.9% (16,727 → 20,056 customers), which may correlate with increased fraud pressure
- Duplicate Rate rose from 25.50% to 26.41% (+0.91pp), continuing a 5-week upward trend from 23.87% in W08
- Paid channel remains relatively stable at 95.34% FAR (-0.99pp), suggesting issues are concentrated in Referral traffic

**Action:** Investigate — Deep dive into Referral channel performance and PF Block rule changes; review whether recent fraud prevention adjustments are appropriately calibrated or over-blocking legitimate customers.

---

---

## L0: 8-Week Trend (US-HF)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W15 | 89.21% | 26.41% | 7.04% | 3.03% | 20,056 | -2.60% ← REPORTED CHANGE |
| 2026-W14 | 91.59% | 25.50% | 6.50% | 0.85% | 16,727 | +3.41% |
| 2026-W13 | 88.57% | 25.08% | 6.69% | 3.59% | 17,571 | -1.45% |
| 2026-W12 | 89.87% | 24.66% | 6.32% | 2.72% | 17,515 | +0.13% |
| 2026-W11 | 89.75% | 23.88% | 6.18% | 2.92% | 19,067 | -2.02% |
| 2026-W10 | 91.60% | 24.70% | 5.95% | 1.22% | 20,601 | -0.08% |
| 2026-W09 | 91.68% | 24.03% | 5.91% | 1.16% | 23,224 | +0.29% |
| 2026-W08 | 91.41% | 23.87% | 6.50% | 0.90% | 21,169 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| US | 2026-W14 | 91.59% | - | 25.50% | - | 16,727 |  |
| US | 2026-W15 | 89.21% | -2.60% | 26.41% | +3.56% | 20,056 | ⚠️ |

**Countries exceeding ±2.5% threshold:** US

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 96.29% | - | 24.13% | - | 13,738 |  |
| Paid | 2026-W15 | 95.34% | -0.99% | 25.68% | +6.43% | 16,420 |  |
| Referral | 2026-W14 | 69.96% | - | 31.82% | - | 2,989 |  |
| Referral | 2026-W15 | 61.50% | -12.09% | 29.70% | -6.64% | 3,636 | ⚠️ |

---

*Report: 2026-04-14*
