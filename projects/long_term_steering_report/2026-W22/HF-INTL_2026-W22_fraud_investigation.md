# Fraud Investigation: HF-INTL 2026-W22

**Metric:** Fraud Approval Rate  
**Period:** 2026-W21 → 2026-W22  
**Observation:** 91.81% → 92.55% (+0.81%)  
**Volume:** 35,348 customers reaching fraud service  
**Significance:** Not significant

## Executive Summary

## Executive Summary

**Overall:** The Fraud Approval Rate (FAR) for HF-INTL improved from 91.81% to 92.55% (+0.74pp) in 2026-W22, a change deemed not statistically significant, with volume increasing to 35,348 customers.

**Funnel Analysis:**

| Step | Check | Δ Conv | Result |
| ---- | ----- | ------ | ------ |
| L0: 8-Week Trend | FAR within normal range (91.18%-92.55%) | +0.74pp | ✅ |
| L1: Country Scan | 4 countries exceed ±2.5% threshold | BE +5.94pp, IE +3.35pp, LU +8.97pp, CH +3.70pp | ⚠️ |
| L1: Channel Category | Paid & Referral stable | Paid +0.43pp, Referral -0.05pp | ✅ |
| L2: Country Deep-Dives | Referral channel flagged in multiple countries | AT -6.01pp, CH +9.41pp, BE +11.54pp | ⚠️ |

**Key Findings:**
- BE showed the largest volume impact with FAR jumping +5.94pp (90.95% → 96.35%), driven by a significant drop in Duplicate Rate (-46.89%) and reduced blocking across both Paid (-49.64% Dup Rate) and Referral (-31.05% Dup Rate) channels
- LU experienced the highest FAR increase (+8.97pp) but with low volume (128 customers), accompanied by a sharp rise in Dup Block Rate (+225.00%)
- CH showed unusual patterns with Duplicate Rate surging +162.83% and Referral channel Dup Block Rate increasing +388.14%, yet FAR still improved +3.70pp
- Referral channel consistently underperforms Paid channel across all countries (typically 20-30pp lower FAR), with elevated Duplicate Block rates driving rejections
- Overall 8-week trend remains stable with FAR fluctuating within a narrow 0.93pp band (91.18%-92.11%) prior to this week

**Action:** Monitor — The overall change is not statistically significant and falls within normal operating range. Continue monitoring BE and CH for sustained pattern changes, particularly the unusual inverse relationship between rising duplicate rates and improving FAR in CH.

---

---

## L0: 8-Week Trend (HF-INTL)

| Week | FAR % | Dup Rate % | Dup Block % | PF Block % | Volume | Δ FAR % |
|------|-------|------------|-------------|------------|--------|---------|
| 2026-W22 | 92.55% | 31.87% | 5.81% | 0.37% | 35,348 | +0.81% ← REPORTED CHANGE |
| 2026-W21 | 91.81% | 32.47% | 6.10% | 0.31% | 33,429 | +0.70% |
| 2026-W20 | 91.18% | 32.27% | 6.71% | 0.31% | 38,799 | -1.01% |
| 2026-W19 | 92.10% | 28.61% | 5.39% | 0.25% | 39,995 | +0.32% |
| 2026-W18 | 91.81% | 28.81% | 5.20% | 0.54% | 41,069 | -0.31% |
| 2026-W17 | 92.10% | 34.26% | 6.02% | 0.31% | 41,741 | +0.11% |
| 2026-W16 | 92.00% | 32.92% | 6.42% | 0.23% | 44,968 | -0.12% |
| 2026-W15 | 92.11% | 30.62% | 6.48% | 0.24% | 42,691 | - |

---

## L1: Country Breakdown

| Country | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|---------|------|-------|-----|------------|-----|--------|------|
| BE | 2026-W21 | 90.95% | - | 32.81% | - | 1,149 |  |
| BE | 2026-W22 | 96.35% | +5.94% | 17.43% | -46.89% | 1,974 | ⚠️ |
| FR | 2026-W21 | 88.54% | - | 25.16% | - | 6,474 |  |
| FR | 2026-W22 | 89.51% | +1.09% | 25.46% | +1.18% | 6,442 |  |
| IE | 2026-W21 | 91.65% | - | 22.88% | - | 1,473 |  |
| IE | 2026-W22 | 94.72% | +3.35% | 25.78% | +12.70% | 2,009 | ⚠️ |
| DE | 2026-W21 | 93.60% | - | 31.45% | - | 6,849 |  |
| DE | 2026-W22 | 93.15% | -0.48% | 29.70% | -5.55% | 6,208 |  |
| LU | 2026-W21 | 81.73% | - | 0.00% | - | 104 |  |
| LU | 2026-W22 | 89.06% | +8.97% | 8.59% | - | 128 | ⚠️ |
| CH | 2026-W21 | 81.10% | - | 6.30% | - | 127 |  |
| CH | 2026-W22 | 84.11% | +3.70% | 16.56% | +162.83% | 151 | ⚠️ |

**Countries exceeding ±2.5% threshold:** BE, IE, LU, CH

---

## L1: Channel Category Scan

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|--------|------|
| Paid | 2026-W21 | 97.34% | - | 33.21% | - | 25,427 |  |
| Paid | 2026-W22 | 97.76% | +0.43% | 32.23% | -2.94% | 27,544 |  |
| Referral | 2026-W21 | 74.23% | - | 30.14% | - | 8,002 |  |
| Referral | 2026-W22 | 74.19% | -0.05% | 30.59% | +1.47% | 7,804 |  |

---

## L2: AT Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W21 | 97.97% | - | 22.71% | - | 0.00% | - | 0.00% | - | 295 |  |
| Paid | 2026-W22 | 98.32% | +0.36% | 22.48% | -1.01% | 0.34% | - | 0.00% | - | 298 |  |
| Referral | 2026-W21 | 71.21% | - | 21.21% | - | 16.67% | - | 0.00% | - | 132 |  |
| Referral | 2026-W22 | 66.94% | -6.01% | 23.39% | +10.25% | 21.77% | +30.65% | 0.00% | - | 124 | ⚠️ |

**Analysis:** The +0.74pp FAR improvement in 2026-W22 represents normal week-over-week variation within historical bounds and requires no immediate action. The flagged movements in BE, IE, LU, and CH appear driven primarily by shifts in duplicate detection rates and blocking behavior rather than systemic fraud pattern changes, with BE's improvement notably linked to reduced duplicate activity. Continued monitoring is recommended to confirm these country-level fluctuations normalize in subsequent weeks.

---

## L2: AU Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W21 | 96.53% | - | 36.36% | - | 1.11% | - | 1.46% | - | 2,885 |  |
| Paid | 2026-W22 | 96.44% | -0.10% | 36.85% | +1.35% | 0.58% | -47.99% | 2.38% | +63.16% | 2,947 |  |
| Referral | 2026-W21 | 66.41% | - | 43.01% | - | 30.70% | - | 0.00% | - | 658 |  |
| Referral | 2026-W22 | 69.44% | +4.56% | 38.89% | -9.58% | 27.92% | -9.04% | 0.15% | - | 684 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: BE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W21 | 96.02% | - | 32.95% | - | 0.11% | - | 0.80% | - | 880 |  |
| Paid | 2026-W22 | 98.64% | +2.72% | 16.60% | -49.64% | 0.12% | +4.33% | 0.18% | -77.64% | 1,687 | ⚠️ |
| Referral | 2026-W21 | 74.35% | - | 32.34% | - | 17.47% | - | 0.00% | - | 269 |  |
| Referral | 2026-W22 | 82.93% | +11.54% | 22.30% | -31.05% | 13.59% | -22.23% | 0.00% | - | 287 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: CH Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W21 | 93.67% | - | 5.06% | - | 0.00% | - | 2.53% | - | 79 |  |
| Paid | 2026-W22 | 95.65% | +2.12% | 17.39% | +243.48% | 0.00% | - | 0.00% | -100.00% | 92 |  |
| Referral | 2026-W21 | 60.42% | - | 8.33% | - | 2.08% | - | 0.00% | - | 48 |  |
| Referral | 2026-W22 | 66.10% | +9.41% | 15.25% | +83.05% | 10.17% | +388.14% | 0.00% | - | 59 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: NZ Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W21 | 97.33% | - | 35.86% | - | 0.56% | - | 0.56% | - | 711 |  |
| Paid | 2026-W22 | 98.94% | +1.66% | 39.79% | +10.94% | 0.30% | -46.22% | 0.76% | +34.46% | 661 |  |
| Referral | 2026-W21 | 55.23% | - | 41.42% | - | 36.40% | - | 0.00% | - | 239 |  |
| Referral | 2026-W22 | 57.71% | +4.49% | 41.85% | +1.03% | 35.24% | -3.19% | 0.44% | - | 227 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---

## L2: SE Deep-Dive

### Channel Category

| Category | Week | FAR % | Δ % | Dup Rate % | Δ % | Dup Block % | Δ % | PF Block % | Δ % | Volume | Flag |
|----------|------|-------|-----|------------|-----|-------------|-----|------------|-----|--------|------|
| Paid | 2026-W21 | 98.02% | - | 32.63% | - | 0.53% | - | 0.13% | - | 757 |  |
| Paid | 2026-W22 | 98.81% | +0.81% | 29.96% | -8.17% | 0.59% | +12.51% | 0.00% | -100.00% | 841 |  |
| Referral | 2026-W21 | 85.32% | - | 20.63% | - | 5.56% | - | 0.00% | - | 252 |  |
| Referral | 2026-W22 | 87.46% | +2.51% | 23.69% | +14.82% | 6.62% | +19.16% | 0.35% | - | 287 | ⚠️ |

**Analysis:** [AI_SUMMARY_PLACEHOLDER]

---


## Decision Framework

**Root Cause Derivation:**

| Country | FAR Change | Channel Driver | Dup Rate | Dup Block | PF Block | Root Cause |
|---------|------------|----------------|----------|-----------|----------|------------|
| BE | ↑ +5.94% | Paid ↑ +2.72%, Referral ↑ +11.54% | ↓ -46.89% | ↓ -50.28% | ↓ -75.05% | [AI_SUMMARY_PLACEHOLDER] |
| IE | ↑ +3.35% | - | ↑ +12.70% | ↓ -35.17% | ↓ -26.68% | [AI_SUMMARY_PLACEHOLDER] |
| LU | ↑ +8.97% | - | → - | ↑ +225.00% | → - | [AI_SUMMARY_PLACEHOLDER] |
| CH | ↑ +3.70% | Referral ↑ +9.41% | ↑ +162.83% | ↑ +404.64% | ↓ -100.00% | [AI_SUMMARY_PLACEHOLDER] |

---


*Report: 2026-06-02*
