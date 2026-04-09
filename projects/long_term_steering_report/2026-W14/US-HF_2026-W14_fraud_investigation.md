# Fraud Investigation: US-HF 2026-W14

**Metric:** Fraud Approval Rate  
**Period:** 2026-W13 → 2026-W14  
**Observation:** 88.61% → 91.54% (+3.30%)  
**Volume:** 16,609 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) improved significantly from 88.61% to 91.54% (+3.30pp) in 2026-W14, returning to levels consistent with weeks W07-W10 after a two-week dip.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | FAR within historical range (89-93%) | +3.30pp | ✅ |
| L1: Country | US single-country impact | +3.30pp | ⚠️ |
| L1: Channel - Paid | Stable performance | +0.31pp | ✅ |
| L1: Channel - Referral | Significant increase | +16.00pp | ⚠️ |
| PF Block Rate | Sharp decrease from prior week | -2.68pp (3.60%→0.92%) | ⚠️ |

**Key Findings:**
- The FAR increase is primarily driven by the **Referral channel**, which jumped from 59.79% to 69.35% (+16.00pp) while volume decreased from 3,648 to 3,015 customers
- **PF Block Rate dropped significantly** from 3.60% to 0.92% (-2.68pp), which directly contributes to higher approval rates
- **Paid channel remains stable** at 96.46% (+0.31pp) with consistent volume (13,594 vs 13,927)
- **Duplicate Rate increased slightly** from 25.13% to 26.05% (+0.92pp), with Referral channel showing +14.92% increase in duplicate rate
- Overall volume decreased by 5.5% (17,575 → 16,609), continuing a downward trend from W10 peak of 20,601

**Action:** **Investigate** – The sharp drop in PF Block Rate and the significant Referral channel FAR increase warrant investigation to determine if this reflects a policy change, model update, or potential gap in fraud controls.

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
