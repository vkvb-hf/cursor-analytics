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
| L0: US-HF Overall Trend | FAR dropped -2.61% vs W14 | -2.39 pp | ⚠️ |
| L1: Country Scan | US exceeds ±2.5% threshold | -2.61% | ⚠️ |
| L1: Channel Category Scan | Referral channel flagged | -12.15% | ⚠️ |
| L2: US Paid Channel | Stable performance | -0.98% | ✅ |
| L2: US Referral Channel | Severe FAR decline + PF Block spike | -12.15% | ⚠️ |

**Key Findings:**
- Referral channel FAR collapsed from 70.00% to 61.50% (-8.50 pp), accounting for the majority of the overall decline despite representing only 18% of volume
- PF Block rate in Referral channel surged from 2.48% to 12.62% (+409.56%), indicating a significant increase in policy/fraud-related rejections
- Duplicate Rate increased modestly overall (+3.60%), with Dup Block rate rising from 6.49% to 7.03% (+8.45%)
- Volume increased 19.9% (16,726 → 20,057), suggesting the decline is not due to volume drop but rather quality degradation in Referral traffic
- Paid channel remains stable at 95.34% FAR (-0.98%), confirming the issue is isolated to Referral

**Action:** **Investigate** — Immediate deep-dive required into Referral channel to identify source of PF Block spike (+409.56%). Review specific referral partners/programs active in W15 and coordinate with Policy/Fraud teams on recent rule changes affecting this segment.

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

**Analysis:** The -2.39 pp FAR decline in US-HF for W15 is primarily attributable to the Referral channel, where the PF Block rate increased dramatically by +409.56% (2.48% → 12.62%), causing FAR to drop from 70.00% to 61.50%. This suggests either a sudden influx of fraudulent referral traffic, a new fraud rule deployment affecting referral customers, or abuse of a specific referral program. Immediate investigation into Referral channel sources and recent policy changes is recommended before W16 reporting.

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| US | ↓ -2.61% | Referral ↓ -12.15% | ↑ +3.60% | ↑ +8.45% | ↑ +253.98% | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-04-15*
