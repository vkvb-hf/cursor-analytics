# Fraud Investigation: US-HF 2026-W14

**Metric:** Fraud Approval Rate  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 88.61% → 91.54% (+3.30%)  
**Volume:** 16,609 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) improved from 88.61% to 91.54% (+3.30pp), returning to levels consistent with the 8-week historical range (91-92%) after a two-week dip.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: US-HF Trend | FAR within historical range | +3.30pp | ✅ |
| L1: Country | US threshold (±2.5%) | +3.30pp | ⚠️ |
| L1: Channel - Paid | Stable performance | +0.31pp | ✅ |
| L1: Channel - Referral | Threshold exceeded | +16.00pp | ⚠️ |

**Key Findings:**
- FAR recovered to 91.54%, aligning with the W07-W10 baseline range after consecutive declines in W11 (-2.04pp) and W13 (-1.41pp)
- Prefill (PF) Block Rate dropped significantly from 3.60% (W13) to 0.92% (W14), a decrease of 2.68pp, which directly contributed to the FAR improvement
- Referral channel showed substantial improvement (+16.00pp FAR), moving from 59.79% to 69.35%, with duplicate rate also increasing by +14.92pp to 32.60%
- Volume decreased by 5.5% (17,575 → 16,609 customers), continuing a downward trend from peak volume of 23,228 in W09
- Paid channel remains stable with high approval rates (96.46%) and minimal week-over-week change (+0.31pp)

**Action:** Monitor — The FAR improvement appears driven by the normalization of PF Block Rate (returning to ~1% from anomalous 3.60% in W13). Investigate the Referral channel's elevated duplicate rate (32.60%) to determine if this represents a data quality issue or genuine behavior change.

---

---

## L0: 8-Week Trend (US-HF)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W14 | 91.54% | 26.05% | 6.81% | 0.92% | 16,609 | +3.30% ← REPORTED CHANGE |
| 2026-W13 | 88.61% | 25.13% | 6.73% | 3.60% | 17,575 | -1.41% |
| 2026-W12 | 89.88% | 24.70% | 6.37% | 2.72% | 17,515 | +0.14% |
| 2026-W11 | 89.75% | 23.92% | 6.22% | 2.92% | 19,069 | -2.04% |
| 2026-W10 | 91.62% | 24.72% | 5.96% | 1.22% | 20,601 | -0.07% |
| 2026-W09 | 91.68% | 24.05% | 5.93% | 1.16% | 23,228 | +0.30% |
| 2026-W08 | 91.41% | 23.89% | 6.52% | 0.90% | 21,171 | -1.44% |
| 2026-W07 | 92.75% | 23.30% | 5.68% | 0.51% | 21,976 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| US | 2026-W13 | 88.61% | - | 25.13% | - | 17,575 |  |
| US | 2026-W14 | 91.54% | +3.30% | 26.05% | +3.68% | 16,609 | ⚠️ |

**Countries exceeding ±2.5% threshold:** US

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W13 | 96.17% | - | 24.28% | - | 13,927 |  |
| Paid | 2026-W14 | 96.46% | +0.31% | 24.60% | +1.33% | 13,594 |  |
| Referral | 2026-W13 | 59.79% | - | 28.37% | - | 3,648 |  |
| Referral | 2026-W14 | 69.35% | +16.00% | 32.60% | +14.92% | 3,015 | ⚠️ |

---

*Report: 2026-04-09*
