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
| L0: US-HF Overall Trend | FAR dropped -2.61% vs prior week | -2.39 pp | ⚠️ |
| L1: Country Scan | US sole market, exceeds ±2.5% threshold | -2.61% | ⚠️ |
| L1: Channel Category Scan | Referral channel major outlier | -12.15% | ⚠️ |
| L2: US Paid Channel | Minor decline within tolerance | -0.98% | ✅ |
| L2: US Referral Channel | Severe FAR decline + PF Block spike | -12.15% | ⚠️ |

**Key Findings:**
- Referral channel FAR collapsed from 70.00% to 61.50% (-8.50 pp), representing the primary driver of the overall decline
- PF Block rate in Referral spiked dramatically from 2.48% to 12.62% (+409.56% relative increase), indicating aggressive fraud prevention triggering
- Overall volume increased 19.9% (16,726 → 20,057), with Referral volume up 21.7% (2,987 → 3,636)
- Paid channel remains stable at 95.34% FAR with only -0.98% change despite +6.43% increase in Dup Rate
- Dup Block rate increased across both channels, with overall rate rising from 6.49% to 7.03%

**Action:** **Investigate** — The +409.56% spike in PF Block rate within the Referral channel requires immediate review of fraud prevention rules and potential false positive analysis.

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

**Analysis:** The W15 FAR decline is directly attributable to the Referral channel in US, where the PF Block rate surged from 2.48% to 12.62%, blocking an additional ~10 pp of customers. This suggests either a fraud prevention rule change, a new fraud vector being detected, or potential over-blocking of legitimate referral traffic. Immediate investigation into the PF Block triggers for Referral customers is recommended to determine if this represents appropriate fraud detection or requires rule calibration.

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| US | ↓ -2.61% | Referral ↓ -12.15% | ↑ +3.60% | ↑ +8.45% | ↑ +253.98% | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-04-17*
