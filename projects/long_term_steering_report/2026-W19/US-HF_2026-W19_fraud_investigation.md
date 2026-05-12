# Fraud Investigation: US-HF 2026-W19

**Metric:** Fraud Approval Rate  
**Period:** 2026-W18 → 2026-W19  
**Observation:** 92.19% → 91.34% (-0.92%)  
**Volume:** 18,589 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

**Overall:** Fraud Approval Rate declined by 0.85 percentage points (92.19% → 91.34%) in US-HF during W19, a change deemed not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: US-HF Overall | FAR 91.34% (-0.92%) | -0.85pp | ✅ |
| L1: Country (US) | FAR 91.34% (-0.92%) | -0.85pp | ✅ |
| L1: Channel - Paid | FAR 96.39% (+0.76%) | +0.73pp | ✅ |
| L1: Channel - Referral | FAR 65.68% (-9.90%) | -7.22pp | ⚠️ |
| L2: US Referral - PF Block | PF Block 10.45% (+835.02%) | +9.33pp | ⚠️ |

**Key Findings:**
- Referral channel FAR dropped sharply from 72.90% to 65.68% (-7.22pp), accounting for the overall decline despite Paid channel improvement
- PF Block rate in Referral channel surged dramatically from 1.12% to 10.45% (+9.33pp), an 835% relative increase
- Duplicate Rate increased across US overall (+2.61pp) and Paid channel (+3.08pp), though Referral saw slight improvement (-0.42pp)
- Paid channel (83.6% of volume) performed strongly at 96.39% FAR, partially offsetting Referral degradation
- 8-week trend shows FAR remains within normal operating range (88.52% - 92.19%)

**Action:** Investigate - The extreme PF Block spike (+835%) in Referral channel requires immediate root cause analysis to determine if this reflects a policy change, model update, or emerging fraud pattern.

---

---

## L0: 8-Week Trend (US-HF)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W19 | 91.34% | 24.02% | 5.52% | 2.39% | 18,589 | -0.92% ← REPORTED CHANGE |
| 2026-W18 | 92.19% | 21.41% | 4.98% | 0.68% | 18,198 | +1.03% |
| 2026-W17 | 91.25% | 26.57% | 6.70% | 0.94% | 17,213 | +1.86% |
| 2026-W16 | 89.59% | 27.23% | 7.79% | 1.34% | 20,453 | +0.38% |
| 2026-W15 | 89.25% | 25.80% | 6.64% | 2.97% | 20,215 | -2.56% |
| 2026-W14 | 91.59% | 25.31% | 6.30% | 0.85% | 16,709 | +3.47% |
| 2026-W13 | 88.52% | 25.00% | 6.62% | 3.58% | 17,566 | -1.53% |
| 2026-W12 | 89.90% | 24.59% | 6.25% | 2.73% | 17,501 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| US | 2026-W18 | 92.19% | - | 21.41% | - | 18,198 |  |
| US | 2026-W19 | 91.34% | -0.92% | 24.02% | +12.19% | 18,589 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 95.66% | - | 20.05% | - | 15,423 |  |
| Paid | 2026-W19 | 96.39% | +0.76% | 23.13% | +15.37% | 15,535 |  |
| Referral | 2026-W18 | 72.90% | - | 29.01% | - | 2,775 |  |
| Referral | 2026-W19 | 65.68% | -9.90% | 28.59% | -1.46% | 3,054 | ⚠️ |

---

## L2: US Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W18 | 95.66% | - | 20.05% | - | 1.55% | - | 0.60% | - | 15,423 |  |
| Paid | 2026-W19 | 96.39% | +0.76% | 23.13% | +15.37% | 2.10% | +35.42% | 0.81% | +34.51% | 15,535 |  |
| Referral | 2026-W18 | 72.90% | - | 29.01% | - | 24.07% | - | 1.12% | - | 2,775 |  |
| Referral | 2026-W19 | 65.68% | -9.90% | 28.59% | -1.46% | 22.92% | -4.78% | 10.45% | +835.02% | 3,054 | ⚠️ |

**Analysis:** The W19 FAR decline is driven almost entirely by Referral channel deterioration, specifically a 9.33pp increase in PF Block rate that warrants investigation. While the overall metric change is not statistically significant and Paid channel continues to perform well, the anomalous PF Block behavior in Referral should be examined to confirm whether this represents intended fraud prevention or an unintended system issue.

---



*Report: 2026-05-12*
