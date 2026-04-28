# Fraud Investigation: US-HF 2026-W17

**Metric:** Fraud Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 89.62% → 91.44% (+2.03%)  
**Volume:** 17,298 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

**Overall:** Fraud Approval Rate (FAR) improved significantly from 89.62% to 91.44% (+1.82pp) in 2026-W17, driven primarily by the Paid channel while volume decreased by 15.5%.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: US-HF Trend | FAR within 8-week range (88.53%-91.62%) | +1.82pp | ✅ |
| L1: Country Breakdown | US threshold ±2.5% | +2.03% (below threshold) | ✅ |
| L1: Channel - Paid | FAR change | +2.34pp (93.56%→95.90%) | ⚠️ |
| L1: Channel - Referral | FAR change | +0.40pp (68.56%→68.96%) | ✅ |
| Duplicate Rate | Overall change | -0.50pp (27.34%→26.84%) | ✅ |
| PF Block Rate | Week-over-week | -0.37pp (1.34%→0.97%) | ✅ |

**Key Findings:**
- Paid channel FAR increased by +2.34pp to 95.90%, accounting for 83% of total volume and driving the overall improvement
- Duplicate Rate in Referral channel spiked by +13.19% (30.88%→34.95%), indicating potential abuse pattern despite stable FAR
- Volume decreased significantly by 3,166 customers (-15.5%), with declines in both Paid (-16.2%) and Referral (-11.4%) channels
- PF Block Rate dropped from 1.34% to 0.97% (-0.37pp), contributing to higher approval rates
- Dup Block Rate decreased from 7.90% to 6.94% (-0.96pp), also supporting FAR improvement

**Action:** Monitor – The FAR improvement is within normal 8-week variance and appears driven by reduced blocking rates. However, the +13.19% spike in Referral Duplicate Rate warrants close observation in the coming weeks for potential fraud pattern emergence.

---

---

## L0: 8-Week Trend (US-HF)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W17 | 91.44% | 26.84% | 6.94% | 0.97% | 17,298 | +2.03% ← REPORTED CHANGE |
| 2026-W16 | 89.62% | 27.34% | 7.90% | 1.34% | 20,464 | +0.40% |
| 2026-W15 | 89.26% | 25.84% | 6.68% | 2.97% | 20,222 | -2.56% |
| 2026-W14 | 91.61% | 25.38% | 6.37% | 0.85% | 16,713 | +3.47% |
| 2026-W13 | 88.53% | 25.01% | 6.64% | 3.59% | 17,570 | -1.51% |
| 2026-W12 | 89.89% | 24.62% | 6.28% | 2.72% | 17,509 | +0.16% |
| 2026-W11 | 89.75% | 23.84% | 6.15% | 2.92% | 19,064 | -2.04% |
| 2026-W10 | 91.62% | 24.67% | 5.91% | 1.22% | 20,591 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| US | 2026-W16 | 89.62% | - | 27.34% | - | 20,464 |  |
| US | 2026-W17 | 91.44% | +2.03% | 26.84% | -1.81% | 17,298 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 93.56% | - | 26.67% | - | 17,232 |  |
| Paid | 2026-W17 | 95.90% | +2.49% | 25.23% | -5.40% | 14,434 |  |
| Referral | 2026-W16 | 68.56% | - | 30.88% | - | 3,232 |  |
| Referral | 2026-W17 | 68.96% | +0.58% | 34.95% | +13.19% | 2,864 |  |

---



*Report: 2026-04-28*
