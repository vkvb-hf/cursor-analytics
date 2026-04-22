# Fraud Investigation: US-HF 2026-W16

**Metric:** Fraud Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 89.28% → 89.68% (+0.45%)  
**Volume:** 20,488 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) increased slightly from 89.28% to 89.68% (+0.45 pp) in US-HF for 2026-W16, a change deemed not statistically significant within normal weekly fluctuation.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | FAR within normal range (88.55%-91.68%) | +0.45 pp | ✅ |
| L1: Country Scan | No countries exceed ±2.5% threshold | +0.45 pp | ✅ |
| L1: Channel Category | Referral exceeds threshold (+10.21 pp) | +10.21 pp | ⚠️ |
| L2: US Channel Deep-Dive | Referral FAR spike, PF Block drop significant | +10.21 pp / -58.26% | ⚠️ |

**Key Findings:**
- Referral channel FAR increased significantly from 61.76% to 68.07% (+10.21 pp), flagged as anomalous
- PF Block Rate in Referral dropped sharply from 12.70% to 5.30% (-58.26%), directly contributing to higher approvals
- Duplicate Rate increased across both channels: Paid (+6.31%) and Referral (+10.01%), with overall rate rising from 25.91% to 27.64%
- Paid channel FAR slightly decreased from 95.26% to 93.77% (-1.57 pp), partially offsetting Referral gains
- Duplicate Block Rate increased in Paid channel from 2.90% to 4.75% (+64.19%), indicating more duplicates being caught

**Action:** Monitor — The overall FAR change is not significant, but the Referral channel's sharp PF Block Rate decrease warrants monitoring over the next 1-2 weeks to determine if this represents a policy change, model adjustment, or anomaly requiring investigation.

---

---

## L0: 8-Week Trend (US-HF)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W16 | 89.68% | 27.64% | 8.17% | 1.37% | 20,488 | +0.45% ← REPORTED CHANGE |
| 2026-W15 | 89.28% | 25.91% | 6.73% | 2.97% | 20,224 | -2.53% |
| 2026-W14 | 91.59% | 25.42% | 6.41% | 0.86% | 16,719 | +3.44% |
| 2026-W13 | 88.55% | 25.05% | 6.67% | 3.59% | 17,570 | -1.49% |
| 2026-W12 | 89.89% | 24.63% | 6.29% | 2.72% | 17,509 | +0.16% |
| 2026-W11 | 89.75% | 23.85% | 6.16% | 2.92% | 19,064 | -2.04% |
| 2026-W10 | 91.62% | 24.68% | 5.92% | 1.22% | 20,597 | -0.08% |
| 2026-W09 | 91.68% | 24.00% | 5.89% | 1.16% | 23,222 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| US | 2026-W15 | 89.28% | - | 25.91% | - | 20,224 |  |
| US | 2026-W16 | 89.68% | +0.45% | 27.64% | +6.68% | 20,488 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 95.26% | - | 25.26% | - | 16,610 |  |
| Paid | 2026-W16 | 93.77% | -1.57% | 26.86% | +6.31% | 17,225 |  |
| Referral | 2026-W15 | 61.76% | - | 28.89% | - | 3,614 |  |
| Referral | 2026-W16 | 68.07% | +10.21% | 31.78% | +10.01% | 3,263 | ⚠️ |

---

## L2: US Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 95.26% | - | 25.26% | - | 2.90% | - | 0.85% | - | 16,610 |  |
| Paid | 2026-W16 | 93.77% | -1.57% | 26.86% | +6.31% | 4.75% | +64.19% | 0.62% | -27.34% | 17,225 |  |
| Referral | 2026-W15 | 61.76% | - | 28.89% | - | 24.35% | - | 12.70% | - | 3,614 |  |
| Referral | 2026-W16 | 68.07% | +10.21% | 31.78% | +10.01% | 26.17% | +7.48% | 5.30% | -58.26% | 3,263 | ⚠️ |

**Analysis:** The +0.45 pp increase in US-HF Fraud Approval Rate is not statistically significant and falls within the normal 8-week fluctuation range of 88.55%-91.68%. However, the Referral channel shows notable movement with a +10.21 pp FAR increase driven primarily by a -58.26% drop in PF Block Rate, which should be monitored for persistence. No immediate escalation is required, but if the PF Block Rate decline in Referral continues next week, further investigation into potential policy or model changes is recommended.

---



*Report: 2026-04-22*
