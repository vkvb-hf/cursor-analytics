# Fraud Investigation: WL 2026-W17

**Metric:** Fraud Approval Rate  
**Period:** 2026-W16 → 2026-W17  
**Observation:** 92.72% → 91.88% (-0.90%)  
**Volume:** 14,244 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** Fraud Approval Rate declined from 92.72% to 91.88% (-0.84pp) in W17, a statistically non-significant change affecting 14,244 customers.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | Sustained decline pattern | -0.90% WoW | ⚠️ |
| L1: Country Scan | No country exceeds ±2.5% threshold | ER -2.28%, CK -1.59% | ✅ |
| L1: Channel Category | Referral below threshold | -4.33% | ⚠️ |
| L2: CK Referral | Severe FAR decline + Dup spike | -11.53% FAR, +30.36% Dup Rate | ⚠️ |
| L2: ER Referral | Moderate decline | -2.80% FAR | ⚠️ |
| L2: CG Referral | Moderate decline | -4.75% FAR | ⚠️ |

**Key Findings:**
- Referral channel is the primary driver of FAR decline across all markets, dropping from 75.90% to 72.61% (-4.33%) at WL level while Paid channel remains stable at 95.54%
- CK Referral shows the most severe degradation: FAR plummeted -11.53% (71.04% → 62.85%) with Duplicate Rate surging +30.36% (31.08% → 40.51%) and Dup Block Rate increasing +33.22%
- Duplicate Rate increased across all major markets in the Referral channel: CK +30.36%, KN -7.57% (improved), ER -0.70% (stable), CG +8.86%
- ER Paid channel shows concerning PF Block Rate spike of +254.25% (0.72% → 2.56%), warranting monitoring
- Overall WL Duplicate Rate rose from 16.83% to 18.16% (+7.90%) and Dup Block Rate increased from 4.95% to 6.11% (+23.43%)

**Action:** Investigate — Focus on CK Referral channel to identify root cause of duplicate surge and FAR collapse; review referral partner quality and potential abuse patterns

---

---

## L0: 8-Week Trend (WL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W17 | 91.88% | 18.16% | 6.11% | 1.14% | 14,244 | -0.90% ← REPORTED CHANGE |
| 2026-W16 | 92.72% | 16.83% | 4.95% | 0.94% | 13,995 | -0.58% |
| 2026-W15 | 93.26% | 15.65% | 4.90% | 0.68% | 15,139 | +0.44% |
| 2026-W14 | 92.85% | 15.23% | 4.83% | 0.81% | 13,277 | +0.19% |
| 2026-W13 | 92.67% | 15.41% | 4.96% | 0.79% | 14,387 | -0.38% |
| 2026-W12 | 93.03% | 15.88% | 4.80% | 0.42% | 15,070 | -1.38% |
| 2026-W11 | 94.33% | 14.69% | 4.05% | 0.35% | 16,393 | +0.53% |
| 2026-W10 | 93.83% | 15.75% | 4.44% | 0.44% | 17,314 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| ER | 2026-W16 | 93.91% | - | 22.78% | - | 2,331 |  |
| ER | 2026-W17 | 91.77% | -2.28% | 23.12% | +1.49% | 2,418 |  |
| CK | 2026-W16 | 92.14% | - | 28.08% | - | 2,340 |  |
| CK | 2026-W17 | 90.67% | -1.59% | 32.49% | +15.70% | 2,241 |  |
| KN | 2026-W16 | 90.47% | - | 8.07% | - | 2,256 |  |
| KN | 2026-W17 | 90.18% | -0.32% | 9.35% | +15.88% | 2,749 |  |
| GN | 2026-W16 | 94.61% | - | 19.89% | - | 1,669 |  |
| GN | 2026-W17 | 94.13% | -0.51% | 19.48% | -2.05% | 1,550 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 95.80% | - | 15.18% | - | 11,829 |  |
| Paid | 2026-W17 | 95.54% | -0.27% | 16.23% | +6.88% | 11,973 |  |
| Referral | 2026-W16 | 75.90% | - | 25.85% | - | 2,166 |  |
| Referral | 2026-W17 | 72.61% | -4.33% | 28.36% | +9.68% | 2,271 | ⚠️ |

---

## L2: CG Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 93.82% | - | 11.08% | - | 1.49% | - | 3.09% | - | 1,878 |  |
| Paid | 2026-W17 | 94.90% | +1.15% | 12.72% | +14.89% | 1.63% | +9.03% | 2.69% | -12.88% | 1,784 |  |
| Referral | 2026-W16 | 79.94% | - | 18.79% | - | 17.83% | - | 0.00% | - | 314 |  |
| Referral | 2026-W17 | 76.14% | -4.75% | 20.45% | +8.86% | 19.89% | +11.51% | 1.70% | - | 352 | ⚠️ |

**Analysis:** The W17 FAR decline is predominantly driven by deteriorating performance in the Referral channel, with CK experiencing the most acute impact (-11.53% FAR coupled with a 30.36% increase in Duplicate Rate). While the overall metric change is not statistically significant and the Paid channel remains healthy, the consistent Referral degradation across multiple markets suggests a systematic issue requiring investigation into referral source quality and duplicate detection thresholds. Immediate focus should be placed on CK Referral partner review and potential tightening of duplicate blocking rules.

---

## L2: CK Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 97.48% | - | 27.32% | - | 0.43% | - | 0.05% | - | 1,867 |  |
| Paid | 2026-W17 | 98.79% | +1.34% | 30.14% | +10.35% | 0.40% | -5.84% | 0.00% | -100.00% | 1,735 |  |
| Referral | 2026-W16 | 71.04% | - | 31.08% | - | 26.85% | - | 0.00% | - | 473 |  |
| Referral | 2026-W17 | 62.85% | -11.53% | 40.51% | +30.36% | 35.77% | +33.22% | 0.20% | - | 506 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: ER Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 96.86% | - | 22.51% | - | 1.65% | - | 0.72% | - | 1,941 |  |
| Paid | 2026-W17 | 94.89% | -2.03% | 22.95% | +1.92% | 1.85% | +12.44% | 2.56% | +254.25% | 1,996 |  |
| Referral | 2026-W16 | 79.23% | - | 24.10% | - | 20.51% | - | 0.00% | - | 390 |  |
| Referral | 2026-W17 | 77.01% | -2.80% | 23.93% | -0.70% | 21.33% | +3.97% | 1.42% | - | 422 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: KN Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W16 | 91.49% | - | 6.97% | - | 5.89% | - | 0.33% | - | 2,138 |  |
| Paid | 2026-W17 | 91.08% | -0.44% | 8.42% | +20.77% | 7.46% | +26.51% | 0.23% | -29.57% | 2,602 |  |
| Referral | 2026-W16 | 72.03% | - | 27.97% | - | 24.58% | - | 1.69% | - | 118 |  |
| Referral | 2026-W17 | 74.15% | +2.94% | 25.85% | -7.57% | 25.85% | +5.18% | 0.00% | -100.00% | 147 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---



*Report: 2026-04-27*
