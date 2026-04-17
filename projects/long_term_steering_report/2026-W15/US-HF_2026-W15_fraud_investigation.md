# Fraud Investigation: US-HF 2026-W15

**Metric:** Fraud Approval Rate  
**Period:** 2026-W14 → 2026-W15  
**Observation:** 91.59% → 89.20% (-2.61%)  
**Volume:** 20,057 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** Fraud Approval Rate (FAR) declined significantly from 91.59% to 89.20% (-2.39 pp) in US-HF during W15, driven primarily by a sharp deterioration in the Referral channel.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: US-HF Trend | FAR within normal range? | -2.61% | ⚠️ |
| L1: Country | US exceeds ±2.5% threshold? | -2.61% | ⚠️ |
| L1: Channel Category | Any channel >±2.5%? | Referral -12.15% | ⚠️ |
| L2: Duplicate Rate | Significant increase? | +3.60% | ⚠️ |
| L2: Duplicate Block | Significant increase? | +8.45% | ⚠️ |
| L2: PF Block | Significant increase? | +253.98% (Referral +409.56%) | ⚠️ |

**Key Findings:**
- Referral channel FAR dropped dramatically from 70.00% to 61.50% (-8.50 pp), representing the largest channel decline
- PF Block rate in Referral surged from 2.48% to 12.62% (+409.56%), indicating a major policy or fraud pattern shift
- Overall Duplicate Rate increased from 25.49% to 26.41% (+0.92 pp) alongside volume increase (+19.9% to 20,057 customers)
- Paid channel remained relatively stable with only -0.98% FAR change despite +6.43% increase in Duplicate Rate
- W15 FAR (89.20%) represents a return to W13 levels (88.57%) after an anomalously high W14 (91.59%)

**Action:** **Investigate** – The 409% increase in PF Block rate within the Referral channel requires immediate investigation to determine if this reflects a new fraud pattern, policy change, or system issue.

---

---

## L0: 8-Week Trend (US-HF)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W15 | 89.20% | 26.41% | 7.03% | 3.03% | 20,057 | -2.61% ← REPORTED CHANGE |
| 2026-W14 | 91.59% | 25.49% | 6.49% | 0.85% | 16,726 | +3.41% |
| 2026-W13 | 88.57% | 25.07% | 6.68% | 3.59% | 17,570 | -1.45% |
| 2026-W12 | 89.87% | 24.65% | 6.31% | 2.72% | 17,514 | +0.13% |
| 2026-W11 | 89.75% | 23.87% | 6.18% | 2.92% | 19,067 | -2.02% |
| 2026-W10 | 91.60% | 24.70% | 5.94% | 1.22% | 20,601 | -0.08% |
| 2026-W09 | 91.68% | 24.02% | 5.90% | 1.16% | 23,224 | +0.30% |
| 2026-W08 | 91.41% | 23.86% | 6.49% | 0.90% | 21,168 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| US | 2026-W14 | 91.59% | - | 25.49% | - | 16,726 |  |
| US | 2026-W15 | 89.20% | -2.61% | 26.41% | +3.60% | 20,057 | ⚠️ |

**Countries exceeding ±2.5% threshold:** US

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 96.28% | - | 24.13% | - | 13,739 |  |
| Paid | 2026-W15 | 95.34% | -0.98% | 25.68% | +6.43% | 16,421 |  |
| Referral | 2026-W14 | 70.00% | - | 31.77% | - | 2,987 |  |
| Referral | 2026-W15 | 61.50% | -12.15% | 29.70% | -6.51% | 3,636 | ⚠️ |

---

## L2: US Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 96.28% | - | 24.13% | - | 2.20% | - | 0.50% | - | 13,739 |  |
| Paid | 2026-W15 | 95.34% | -0.98% | 25.68% | +6.43% | 3.01% | +36.86% | 0.90% | +79.46% | 16,421 |  |
| Referral | 2026-W14 | 70.00% | - | 31.77% | - | 26.21% | - | 2.48% | - | 2,987 |  |
| Referral | 2026-W15 | 61.50% | -12.15% | 29.70% | -6.51% | 25.22% | -3.79% | 12.62% | +409.56% | 3,636 | ⚠️ |

**Analysis:** The 2.39 pp decline in US-HF Fraud Approval Rate is primarily attributable to the Referral channel, where PF Block rates increased by over 400%, suggesting either an emerging fraud vector or a recent policy/model change affecting this segment. While the Paid channel (82% of volume) remains stable, the Referral channel degradation warrants urgent review of PF blocking rules and potential referral abuse patterns to determine appropriate remediation actions.

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| US | ↓ -2.61% | Referral ↓ -12.15% | ↑ +3.60% | ↑ +8.45% | ↑ +253.98% | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-04-17*
