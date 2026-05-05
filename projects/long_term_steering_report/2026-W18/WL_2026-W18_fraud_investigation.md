# Fraud Investigation: WL 2026-W18

**Metric:** Fraud Approval Rate  
**Period:** 2026-W17 → 2026-W18  
**Observation:** 91.76% → 92.87% (+1.21%)  
**Volume:** 14,048 customers reaching fraud service  
**Significance:** Significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) improved from 91.76% to 92.87% (+1.21 pp) in W18, recovering from the prior week's decline and returning to levels seen in W16.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: WL Trend | FAR within normal 8-week range (91.76%-94.33%) | +1.21 pp | ✅ |
| L1: Country Scan | 1 of 5 countries exceeded ±2.5% threshold | AO +3.22 pp | ⚠️ |
| L1: Channel Scan | Referral channel exceeded threshold | +4.20 pp | ⚠️ |
| L2: AO Deep-Dive | Referral channel driving improvement | +5.12 pp | ⚠️ |
| L2: CK Deep-Dive | Referral channel significant improvement | +7.59 pp | ⚠️ |
| L2: CG Deep-Dive | Referral channel significant improvement | +7.63 pp | ⚠️ |
| L2: KN Deep-Dive | Referral channel improvement | +5.74 pp | ⚠️ |

**Key Findings:**
- Referral channel drove the FAR improvement across all markets, with global Referral FAR increasing from 73.23% to 76.31% (+4.20 pp) while Paid remained stable (+0.60 pp)
- Duplicate Rate decreased globally from 17.82% to 16.92% (-0.90 pp), with corresponding reductions in Dup Block rates across Referral channels (CK: -8.79%, AO: -8.96%, CG: -10.75%, KN: -21.57%)
- AO showed the largest country-level FAR improvement (+3.22 pp), driven by Referral channel (+5.12 pp) with a significant drop in Dup Rate (-9.71%)
- CG Referral showed the highest FAR improvement (+7.63 pp) alongside a notable PF Block reduction (-85.29%)
- Overall volume remained stable at 14,048 customers (+0.6% vs W17)

**Action:** Monitor - The FAR improvement appears driven by legitimate reductions in duplicate blocking across Referral channels. Continue monitoring Referral channel duplicate patterns to ensure the trend is sustainable and not indicative of loosened fraud controls.

---

---

## L0: 8-Week Trend (WL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W18 | 92.87% | 16.92% | 5.33% | 1.21% | 14,048 | +1.21% ← REPORTED CHANGE |
| 2026-W17 | 91.76% | 17.82% | 5.76% | 1.10% | 13,958 | -1.18% |
| 2026-W16 | 92.86% | 16.73% | 4.84% | 0.93% | 13,991 | -0.44% |
| 2026-W15 | 93.27% | 15.57% | 4.82% | 0.67% | 15,134 | +0.45% |
| 2026-W14 | 92.85% | 15.19% | 4.79% | 0.81% | 13,276 | +0.22% |
| 2026-W13 | 92.65% | 15.40% | 4.96% | 0.79% | 14,386 | -0.39% |
| 2026-W12 | 93.02% | 15.87% | 4.78% | 0.42% | 15,070 | -1.39% |
| 2026-W11 | 94.33% | 14.66% | 4.02% | 0.35% | 16,393 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| CK | 2026-W17 | 90.45% | - | 32.12% | - | 2,189 |  |
| CK | 2026-W18 | 92.10% | +1.82% | 31.13% | -3.06% | 2,303 |  |
| CG | 2026-W17 | 91.86% | - | 13.55% | - | 2,089 |  |
| CG | 2026-W18 | 93.23% | +1.49% | 14.90% | +9.98% | 2,141 |  |
| KN | 2026-W17 | 90.27% | - | 8.64% | - | 2,662 |  |
| KN | 2026-W18 | 91.32% | +1.16% | 8.57% | -0.78% | 2,753 |  |
| ER | 2026-W17 | 91.46% | - | 22.92% | - | 2,343 |  |
| ER | 2026-W18 | 92.72% | +1.37% | 22.20% | -3.15% | 2,293 |  |
| AO | 2026-W17 | 86.76% | - | 30.23% | - | 1,042 |  |
| AO | 2026-W18 | 89.55% | +3.22% | 27.29% | -9.71% | 861 | ⚠️ |

**Countries exceeding ±2.5% threshold:** AO

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W17 | 95.35% | - | 16.03% | - | 11,694 |  |
| Paid | 2026-W18 | 95.92% | +0.60% | 15.30% | -4.55% | 11,866 |  |
| Referral | 2026-W17 | 73.23% | - | 27.03% | - | 2,264 |  |
| Referral | 2026-W18 | 76.31% | +4.20% | 25.71% | -4.89% | 2,182 | ⚠️ |

---

## L2: AO Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W17 | 97.41% | - | 28.51% | - | 0.15% | - | 0.00% | - | 656 |  |
| Paid | 2026-W18 | 99.28% | +1.92% | 25.91% | -9.12% | 0.00% | -100.00% | 0.00% | - | 552 |  |
| Referral | 2026-W17 | 68.65% | - | 33.16% | - | 30.57% | - | 0.00% | - | 386 |  |
| Referral | 2026-W18 | 72.17% | +5.12% | 29.77% | -10.21% | 27.83% | -8.96% | 0.00% | - | 309 | ⚠️ |

**Analysis:** The W18 FAR improvement of +1.21 pp represents a recovery to W16 levels, primarily driven by reduced duplicate blocking in the Referral channel across all markets. The consistent pattern of lower Dup Rates and Dup Block percentages in Referral suggests either improved customer behavior or adjustments to duplicate detection logic. No immediate action is required, but the Referral channel should be monitored to ensure fraud prevention effectiveness is maintained alongside the improved approval rates.

---

## L2: CG Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W17 | 94.78% | - | 12.67% | - | 1.38% | - | 2.58% | - | 1,744 |  |
| Paid | 2026-W18 | 95.13% | +0.36% | 14.23% | +12.30% | 1.27% | -7.46% | 3.27% | +26.61% | 1,806 |  |
| Referral | 2026-W17 | 77.10% | - | 17.97% | - | 17.39% | - | 2.03% | - | 345 |  |
| Referral | 2026-W18 | 82.99% | +7.63% | 18.51% | +2.99% | 15.52% | -10.75% | 0.30% | -85.29% | 335 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: CK Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W17 | 98.35% | - | 30.24% | - | 0.41% | - | 0.00% | - | 1,693 |  |
| Paid | 2026-W18 | 99.05% | +0.71% | 30.02% | -0.73% | 0.39% | -4.99% | 0.00% | - | 1,782 |  |
| Referral | 2026-W17 | 63.51% | - | 38.51% | - | 33.67% | - | 0.20% | - | 496 |  |
| Referral | 2026-W18 | 68.33% | +7.59% | 34.93% | -9.28% | 30.71% | -8.79% | 0.00% | -100.00% | 521 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: KN Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W17 | 91.05% | - | 7.79% | - | 6.91% | - | 0.20% | - | 2,502 |  |
| Paid | 2026-W18 | 91.78% | +0.80% | 7.95% | +2.06% | 7.04% | +1.76% | 0.31% | +53.09% | 2,615 |  |
| Referral | 2026-W17 | 78.13% | - | 21.88% | - | 21.25% | - | 0.00% | - | 160 |  |
| Referral | 2026-W18 | 82.61% | +5.74% | 20.29% | -7.25% | 16.67% | -21.57% | 0.00% | - | 138 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| AO | ↑ +3.22% | Referral ↑ +5.12% | ↓ -9.71% | ↓ -12.54% | → - | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-05-05*
