# Fraud Investigation: WL 2026-W16

**Metric:** Fraud Approval Rate  
**Period:** 2026-W15 → 2026-W16  
**Observation:** 93.28% → 92.95% (-0.35%)  
**Volume:** 14,308 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate declined slightly from 93.28% to 92.95% (-0.33pp) in W16, a change that is not statistically significant.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL Trend | 8-week stability check | -0.35% WoW | ✅ Within normal range |
| L1: Country Scan | Threshold ±2.5% | No countries exceed | ✅ No flags |
| L1: Channel Scan | Category comparison | Referral -1.86% | ✅ Below threshold |
| L2: CG Referral | Deep-dive | -4.60% FAR | ⚠️ Elevated Dup Block |
| L2: KN Referral | Deep-dive | -16.91% FAR | ⚠️ Critical decline |
| L2: ER Referral | Deep-dive | +3.02% FAR | ✅ Improving |

**Key Findings:**
- KN Referral channel shows critical FAR decline of -16.91% (84.54% → 70.25%) with Duplicate Rate nearly doubling (+91.81%) and Dup Block Rate increasing by +76.42%
- CG Referral FAR declined -4.60% (83.92% → 80.06%) driven by Dup Rate increase of +24.19% and Dup Block increase of +42.91%
- Overall Duplicate Rate increased across WL from 15.74% to 17.14% (+1.40pp), reaching the highest level in the 8-week window
- PF Block Rate increased from 0.69% to 0.96% (+0.27pp) at the WL level, with CG Paid showing +60.34% increase in PF blocks
- Volume declined across all major countries (total -835 customers, -5.5% WoW)

**Action:** Investigate — The KN Referral channel requires immediate investigation due to the severe FAR decline and duplicate rate spike. Review duplicate detection rules and assess whether a specific referral source is driving fraudulent traffic.

---

---

## L0: 8-Week Trend (WL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W16 | 92.95% | 17.14% | 5.26% | 0.96% | 14,308 | -0.35% ← REPORTED CHANGE |
| 2026-W15 | 93.28% | 15.74% | 4.98% | 0.69% | 15,143 | +0.44% |
| 2026-W14 | 92.88% | 15.25% | 4.84% | 0.82% | 13,279 | +0.19% |
| 2026-W13 | 92.70% | 15.44% | 4.99% | 0.79% | 14,388 | -0.35% |
| 2026-W12 | 93.02% | 15.90% | 4.82% | 0.42% | 15,072 | -1.40% |
| 2026-W11 | 94.34% | 14.70% | 4.06% | 0.35% | 16,393 | +0.54% |
| 2026-W10 | 93.83% | 15.76% | 4.45% | 0.44% | 17,314 | +0.39% |
| 2026-W09 | 93.47% | 15.24% | 4.63% | 0.54% | 16,425 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| ER | 2026-W15 | 92.83% | - | 22.17% | - | 2,539 |  |
| ER | 2026-W16 | 94.02% | +1.28% | 22.92% | +3.38% | 2,408 |  |
| KN | 2026-W15 | 91.43% | - | 7.35% | - | 2,707 |  |
| KN | 2026-W16 | 90.66% | -0.84% | 9.08% | +23.56% | 2,323 |  |
| MR | 2026-W15 | 96.87% | - | 4.59% | - | 2,748 |  |
| MR | 2026-W16 | 96.19% | -0.70% | 5.52% | +20.29% | 2,230 |  |
| CK | 2026-W15 | 92.98% | - | 27.56% | - | 2,591 |  |
| CK | 2026-W16 | 92.37% | -0.65% | 28.31% | +2.71% | 2,413 |  |

**Countries exceeding ±2.5% threshold:** None

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 96.33% | - | 14.11% | - | 12,767 |  |
| Paid | 2026-W16 | 96.16% | -0.18% | 15.40% | +9.11% | 12,091 |  |
| Referral | 2026-W15 | 76.89% | - | 24.45% | - | 2,376 |  |
| Referral | 2026-W16 | 75.46% | -1.86% | 26.61% | +8.83% | 2,217 |  |

---

## L2: CG Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 94.63% | - | 12.40% | - | 2.40% | - | 1.94% | - | 1,750 |  |
| Paid | 2026-W16 | 94.39% | -0.25% | 11.06% | -10.81% | 1.56% | -35.10% | 3.12% | +60.34% | 1,926 |  |
| Referral | 2026-W15 | 83.92% | - | 15.80% | - | 13.08% | - | 0.27% | - | 367 |  |
| Referral | 2026-W16 | 80.06% | -4.60% | 19.63% | +24.19% | 18.69% | +42.91% | 0.00% | -100.00% | 321 | ⚠️ |

**Analysis:** While the overall WL Fraud Approval Rate change of -0.35% is not significant, the deep-dive analysis reveals a concentrated issue in the KN Referral channel where FAR dropped 16.91pp with duplicate rates nearly doubling. This pattern suggests a potential fraud attack or abuse vector through KN referral traffic that is being correctly caught by duplicate blocking mechanisms. Recommend focused investigation on KN Referral sources and monitoring of CG Referral for similar patterns.

---

## L2: ER Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 96.66% | - | 21.28% | - | 2.27% | - | 0.48% | - | 2,068 |  |
| Paid | 2026-W16 | 97.16% | +0.51% | 22.52% | +5.85% | 1.69% | -25.46% | 0.70% | +44.26% | 2,007 |  |
| Referral | 2026-W15 | 76.01% | - | 26.11% | - | 22.93% | - | 0.42% | - | 471 |  |
| Referral | 2026-W16 | 78.30% | +3.02% | 24.94% | -4.51% | 21.45% | -6.47% | 0.00% | -100.00% | 401 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: KN Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W15 | 92.00% | - | 6.64% | - | 5.72% | - | 0.60% | - | 2,500 |  |
| Paid | 2026-W16 | 91.78% | -0.24% | 7.90% | +19.00% | 6.86% | +19.88% | 0.36% | -39.45% | 2,202 |  |
| Referral | 2026-W15 | 84.54% | - | 15.94% | - | 15.46% | - | 0.00% | - | 207 |  |
| Referral | 2026-W16 | 70.25% | -16.91% | 30.58% | +91.81% | 27.27% | +76.42% | 1.65% | - | 121 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---



*Report: 2026-04-22*
