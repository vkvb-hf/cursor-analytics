# Fraud Investigation: US-HF 2026-W14

**Metric:** Fraud Approval Rate  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 88.61% → 91.54% (+3.30%)  
**Volume:** 16,609 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

**Overall:** Fraud Approval Rate improved significantly from 88.61% to 91.54% (+3.30 pp) in W14, returning to levels consistent with W09-W10 performance after a two-week dip.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | FAR within historical range (89.75%-92.75%) | +3.30 pp | ✅ |
| L1: Country Breakdown | US exceeds ±2.5% threshold | +3.30 pp | ⚠️ |
| L1: Channel Category | Referral exceeds threshold | +16.00 pp | ⚠️ |
| L1: Channel Category | Paid stable | +0.31 pp | ✅ |

**Key Findings:**
- PF Block Rate dropped sharply from 3.60% (W13) to 0.92% (W14), a -74% relative decrease, which is the primary driver of FAR improvement
- Referral channel FAR jumped +16.00 pp (59.79% → 69.35%) with volume declining 17% (3,648 → 3,015 customers)
- Duplicate Rate increased slightly (+0.92 pp) to 26.05%, with Referral channel showing highest duplicate rate at 32.60% (+14.92% relative increase)
- Overall volume decreased 5.5% (17,575 → 16,609), suggesting fewer customers reaching fraud service
- Current FAR of 91.54% aligns with W10 (91.62%) and W09 (91.68%), indicating recovery rather than anomaly

**Action:** Monitor — The FAR improvement appears driven by reduced PF Block activity rather than process changes. Continue monitoring Referral channel for sustained performance and investigate the PF Block rate reduction to confirm it reflects legitimate operational adjustment.

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

*Report: 2026-04-10*
