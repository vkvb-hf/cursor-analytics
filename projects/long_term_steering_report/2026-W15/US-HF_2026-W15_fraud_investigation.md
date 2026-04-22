# Fraud Investigation: US-HF 2026-W15

**Metric:** Fraud Approval Rate  
**Period:** 2026-W15 → 2026-W15  
**Observation:** 89.28% → 89.68% (+0.45%)  
**Volume:** 20,488 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) for US-HF declined by -2.53pp in 2026-W15 (89.28%) compared to 2026-W14 (91.59%), though this change was assessed as not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | FAR within normal range (88.55%-91.68%) | -2.53pp | ✅ |
| L1: Country Scan | US exceeds ±2.5% threshold | -2.53pp | ⚠️ |
| L1: Channel Category Scan | Referral exceeds threshold | -11.91pp | ⚠️ |
| L2: US Paid Channel | Minor decline | -1.03pp | ✅ |
| L2: US Referral Channel | Significant decline with PF Block spike | -11.91pp | ⚠️ |

**Key Findings:**
- The Referral channel in US drove the overall FAR decline, dropping -11.91pp (from 70.11% to 61.76%) while volume increased from 2,981 to 3,614 customers
- PF Block rate in the Referral channel spiked +411.63% (from 2.48% to 12.70%), indicating aggressive fraud prevention triggering
- Overall Duplicate Rate increased modestly (+1.93pp to 25.91%), with the Paid channel seeing a +4.82% increase in duplicates
- The Paid channel remained stable at 95.26% FAR (-1.03pp) and represents the majority of volume (16,610 of 20,224 customers)
- The 8-week trend shows FAR recovered to 89.68% in W16, suggesting the W15 decline may be transient

**Action:** Monitor – The decline is not statistically significant and FAR recovered in W16. However, investigate the PF Block rule changes affecting the Referral channel if the elevated block rate persists.

---

---

## L0: 8-Week Trend (US-HF)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W16 | 89.68% | 27.64% | 8.17% | 1.37% | 20,488 | +0.45% |
| 2026-W15 | 89.28% | 25.91% | 6.73% | 2.97% | 20,224 | -2.53% ← REPORTED CHANGE |
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
| US | 2026-W14 | 91.59% | - | 25.42% | - | 16,719 |  |
| US | 2026-W15 | 89.28% | -2.53% | 25.91% | +1.93% | 20,224 | ⚠️ |

**Countries exceeding ±2.5% threshold:** US

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 96.25% | - | 24.10% | - | 13,738 |  |
| Paid | 2026-W15 | 95.26% | -1.03% | 25.26% | +4.82% | 16,610 |  |
| Referral | 2026-W14 | 70.11% | - | 31.50% | - | 2,981 |  |
| Referral | 2026-W15 | 61.76% | -11.91% | 28.89% | -8.29% | 3,614 | ⚠️ |

---

## L2: US Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W14 | 96.25% | - | 24.10% | - | 2.18% | - | 0.50% | - | 13,738 |  |
| Paid | 2026-W15 | 95.26% | -1.03% | 25.26% | +4.82% | 2.90% | +33.05% | 0.85% | +70.21% | 16,610 |  |
| Referral | 2026-W14 | 70.11% | - | 31.50% | - | 25.93% | - | 2.48% | - | 2,981 |  |
| Referral | 2026-W15 | 61.76% | -11.91% | 28.89% | -8.29% | 24.35% | -6.10% | 12.70% | +411.63% | 3,614 | ⚠️ |

**Analysis:** The 2026-W15 FAR decline in US-HF was primarily driven by a sharp increase in PF Block activity within the Referral channel (+411.63%), which reduced that segment's approval rate by -11.91pp. Given the metric's recovery in W16 and the statistical insignificance of the change, no immediate escalation is required, though the fraud prevention rules impacting Referral traffic should be reviewed to ensure legitimate customers are not being over-blocked.

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| US | ↓ -2.53% | Referral ↓ -11.91% | → +1.93% | ↑ +4.96% | ↑ +247.44% | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-04-22*
