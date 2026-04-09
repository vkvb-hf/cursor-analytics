# Fraud Investigation: US-HF 2026-W14

**Metric:** Fraud Approval Rate  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 88.61% → 91.54% (+3.30%)  
**Volume:** 16,609 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) improved significantly from 88.61% to 91.54% (+3.30pp) in 2026-W14, returning to levels consistent with weeks 2026-W09 and 2026-W10.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | FAR within historical range (89-92%) | +3.30pp | ✅ |
| L1: Country | US exceeds ±2.5% threshold | +3.30pp | ⚠️ |
| L1: Channel - Paid | Stable performance | +0.31pp | ✅ |
| L1: Channel - Referral | Significant increase | +16.00pp | ⚠️ |
| PF Block Rate | Dropped from elevated W13 level | -2.68pp | ✅ |

**Key Findings:**
- The FAR increase is primarily driven by the **Referral channel**, which saw a +16.00pp improvement (59.79% → 69.35%) while volume decreased by 633 customers
- **PF Block Rate dropped significantly** from 3.60% to 0.92% (-2.68pp), suggesting a policy or system change that reduced pre-fraud blocks
- The **Paid channel remains stable** at ~96% FAR with minimal change (+0.31pp), indicating the shift is isolated to Referral
- **Duplicate Rate increased slightly** (+0.92pp to 26.05%), with Referral channel showing the highest duplicate rate at 32.60% (+14.92%)
- Overall volume declined by 966 customers (17,575 → 16,609), a -5.5% reduction week-over-week

**Action:** **Investigate** — The significant Referral channel improvement (+16.00pp) combined with the sharp PF Block Rate drop (-2.68pp) suggests a recent policy or model change. Verify if any fraud prevention rules were modified in W14 that would explain both the reduced blocking and improved approval rates.

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
