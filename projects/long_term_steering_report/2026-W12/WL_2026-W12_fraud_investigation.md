# Fraud Investigation: WL 2026-W12

**Metric:** Fraud Approval Rate  
**Period:** 2026-W13 → 2026-W12  
**Observation:** 92.73% → 93.06% (+0.35%)  
**Volume:** 13,609 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) declined by 1.35pp (94.31% → 93.03%) in 2026-W12, though the change is not statistically significant and remains within normal operating range.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL Trend | FAR within 8-week range | -1.35pp | ✅ |
| L1: Country | CK exceeds ±2.5% threshold | -3.73pp | ⚠️ |
| L1: Channel | All categories within threshold | -0.96pp to -2.36pp | ✅ |
| Duplicate Rate | Elevated in CK | +20.54% | ⚠️ |
| PF Block Rate | Stable at 0.43% | +0.08pp | ✅ |

**Key Findings:**
- CK shows the largest FAR decline (-3.73pp, from 94.51% to 90.99%) with a significant duplicate rate increase (+20.54%, reaching 26.91%)
- Volume decreased 8.1% WoW (16,403 → 15,081 customers reaching fraud service)
- Referral channel has consistently lower FAR (76.03%) compared to Paid channel (96.19%), with both declining slightly WoW
- The 2026-W07 anomaly (PF Block 5.17%, FAR 89.36%) has fully normalized, with PF Block now stable at 0.43%
- MR showed secondary decline of -1.66pp in FAR with moderate duplicate rate increase (+11.43%)

**Action:** Monitor – Focus attention on CK duplicate rate trends; if CK FAR continues declining or duplicate rate exceeds 30% in 2026-W13, escalate for deeper investigation.

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
